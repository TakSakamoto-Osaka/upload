using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO.Ports;
using System.Diagnostics;

namespace EUTCom
{
    public class EUTSerialCom
    {
        public int PortNo { get; private set; }

        SerialPort SerialPortObj;

        public EUTSerialCom( int PortNo )
        {
            this.PortNo = PortNo;
        }

        public void Open()
        {
            try {
                SerialPortObj = new SerialPort( $"COM{PortNo}", 57600, Parity.None, 8, StopBits.One );
                SerialPortObj.Open();

            } catch {
                throw;
            }
        }

        public void Close()
        {
            try {
                SerialPortObj.Close();

            } catch {
                throw;
            }
        }

        private void SendData( TcTmId tctmid, ushort data )
        {
            try {
                List<byte> sendBuff = new List<byte>();

                sendBuff.Add( 0x07 );               //  スタートデータ
                sendBuff.Add( ( byte )tctmid );     //  tc tm Id

                sendBuff.Add( ( byte ) ( data & 0x00FF ) );     //  データの下位バイト
                sendBuff.Add( ( byte ) ( data / 0x100 ) );      //  データの上位バイト

                //  チェックサム計算
                int sumbuf = sendBuff.Sum( x => x );
                sendBuff.Add( ( byte ) ( sumbuf & 0xFF ) );     //  サムの下位バイト

                SerialPortObj.Write( sendBuff.ToArray(), 0, sendBuff.Count );

            } catch {
                throw;
            }
        }

        private ( RecResponse res, List<byte> recBuf ) RecieveData( TcTmId tctmid, int timeOutSec = 3 )
        {
            try {
                List<byte> recTmp = new List<byte>();   //  受信バッファ
                List<byte> recBuf = new List<byte>();   //  返信用受信バッファ
                RecResponse res;

                Stopwatch sw = new Stopwatch();
                sw.Start();

                while ( true ) {
                    //  受信データをバッファにコピー
                    int recSize = 0;

                    do {
                        recSize = SerialPortObj.BytesToRead;    //  受信バイト数

                        if ( recSize > 0 ) {            //  受信データがあった場合
                            byte[] readBuf = new byte[ recSize ];
                            SerialPortObj.Read( readBuf, 0, recSize );

                            recTmp.AddRange( readBuf );
                        }

                    } while ( recSize > 0 );

                    //  受信バイト数チェック
                    if ( recTmp.Count >= 5 ) {
                        if ( recTmp[0] != 0x13 ) {
                            //  開始文字確認
                            res = RecResponse.START_CHR_ERROR;
                        } else if ( recTmp[1] != (byte)tctmid ) {
                            //  tctmidチェック
                            res = RecResponse.TCTMID_ERROR;
                        } else {
                            //  チェックサム確認
                            int sumbuf = recTmp.GetRange( 0, 4 ).Sum( x => x );

                            if ( (byte)( sumbuf & 0xff ) != recTmp[4] ) {
                                res = RecResponse.CHECKSUM_ERROR;
                            } else {
                                res = RecResponse.SUCCESS;
                                recBuf.AddRange( recTmp.GetRange( 2, 2 ) );
                            }
                        }

                        break;
                    }

                    if ( sw.Elapsed.TotalSeconds > timeOutSec ) {
                        res = RecResponse.TIME_OUT;
                        break;
                    }
                }

                return (res, recBuf);

            } catch {
                throw;
            }
        }

        public RecResponse ALLStop( StopMode mode )
        {
            try {
                SendData( TcTmId.ALL_STOP, ( ushort )mode );
                (RecResponse res, List<byte> recBuf) val = RecieveData( TcTmId.ALL_STOP );

                return ( val.res );

            } catch {
                throw;
            }
        }


    }
}
