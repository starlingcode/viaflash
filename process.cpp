#include "process.h"

Process::Process(QObject *parent) : QObject(parent)
{
    m_path = QDir::currentPath();

#ifdef WIN32
    m_executable = QString( m_path + "/" + "dfu-util.exe");
#else
    m_executable =  QString( m_path + "/" + "dfu-util" );
#endif

    // check tool exists
    if (QFile(m_executable).exists())
    {
        emit message("dfu-util exists.");
    }
    else
    {
        emit message("dfu-util not found. Check for dfu-util executable in program directory.");
    }

    // link dfu-util stdout to parseScan function
    connect( &dfuScan, SIGNAL( readyReadStandardOutput() ), this, SLOT( parseScan() ) );
    connect( &dfuDownloadOptionBytes, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( parseOptionBytes() ) );

}


void Process::checkForVia()
{
    QString dfuCmd = QString("%1 -l").arg( m_executable );
    dfuScan.start( dfuCmd );
}

void Process::parseScan()
{
    QString outtxt = dfuScan.readAllStandardOutput();
    if (outtxt.contains("Found DFU: [0483:df11]")){
        QString serString = outtxt.right(15);
        serial = serString.trimmed();
        serial.remove('"');
        // download option bytes
        QString dfuCmd = QString("%1 --device 0483:df11 -a 1 -s 0x1FFFF804:2 -U optionbytes.temp").arg( m_executable);
        dfuDownloadOptionBytes.start( dfuCmd );
    }
}

void Process::parseOptionBytes()
{
    qDebug() << dfuDownloadOptionBytes.exitStatus();
    QFile optionbytes("optionbytes.temp");
    char tmp;
    optionbytes.open(QIODevice::ReadOnly);
    optionbytes.read(&tmp,sizeof(char));
    m_firmwareID = tmp;
    optionbytes.read(&tmp,sizeof(char));
    m_firmwareVersion = tmp;
    optionbytes.close();
    optionbytes.remove();
    if (m_firmwareID == 255 && m_firmwareVersion == 255)
    {
        emit message(QString("Via found with Serial # " + serial + "     Firmware is custom or flash memory is blank"));
    }
    else
    {
        emit message(QString("Via found with Serial # " + serial + "     Firmware ID: " + QString::number(m_firmwareID) + " Firmware version " + QString::number(m_firmwareVersion)));
    }
}
