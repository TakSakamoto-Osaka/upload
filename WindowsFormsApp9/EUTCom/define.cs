using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EUTCom
{
    public enum RecResponse : int
    {
        /// <summary>成功</summary>
        SUCCESS,

        /// <summary>タイムアウト</summary>
        TIME_OUT,

        /// <summary>開始文字エラー</summary>
        START_CHR_ERROR,

        /// <summary>TcTmIDエラー</summary>
        TCTMID_ERROR,

        /// <summary>チェックサムエラー</summary>
        CHECKSUM_ERROR
    }

    public enum TcTmId : byte
    {
        /// <summary>全停止</summary>
        ALL_STOP = 0x00,
    }

    public enum StopMode : ushort
    {
        /// <summary>強制停止</summary>
        FORCE = 0x0001,
        
        /// <summary>スロープ停止</summary>
        SLOPE = 0x0002,
    }




}
