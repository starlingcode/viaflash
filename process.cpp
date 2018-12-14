#include "process.h"

Process::Process(QObject *parent) : QObject(parent)
{
    m_path = QDir::currentPath();

#ifdef WIN32
    m_executable = QString( m_path + "/" + "dfu-util.exe");
#else
    m_executable =  QString( m_path + "/" + "dfu-util" );
#endif

    if (checkToolExists())
    {
        qDebug() << "has dfu-util";
    }
    else
    {
        qDebug() << "no dfu-util";
    }

    connect( &dfuScan, SIGNAL( readyReadStandardOutput() ), this, SLOT( parseScan() ) );

}

bool Process::checkToolExists()
{
    return QFile(m_executable).exists();
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
    }
}
