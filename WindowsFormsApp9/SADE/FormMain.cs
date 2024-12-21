using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using EUTCom;

namespace SADE
{
    public partial class FormMain : Form
    {
        EUTSerialCom EUTSerialComObj;


        public FormMain()
        {
            InitializeComponent();
        }

        private void button1_Click( object sender, EventArgs e )
        {
            EUTSerialComObj = new EUTSerialCom( 12 );

            EUTSerialComObj.Open();

            EUTSerialComObj.ALLStop( StopMode.FORCE );

            EUTSerialComObj.Close();
        }
    }
}
