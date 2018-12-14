#include "dfuutil.h"

dfuUtil::dfuUtil(QObject *parent) : QObject(parent)
{
    binaryPath = QCoreApplication::applicationDirPath();

#ifdef WIN32
    QFile dfuExecutable( binaryPath + "/" + "dfu-util.exe");
#else
    QFile dfuExecutable( binaryPath + "/" + "dfu-util" );
#endif

}

dfuUtil::~dfuUtil(){}


// Make sure dfu-util can be found
bool dfuUtil::checkToolExists( QFile *toolFile )
{
    // Make sure dfu-util exists
    if ( !toolFile->exists() )
    {
        return false;
    }
    else
    {
       return true;
    }
}

void dfuUtil::flashFirmware(QString firmware)
{
    // Run dfu-util command
    QString dfuCmd = QString("%1 --device 0483:df11 -a 0 -s 0x08000000 -D %2").arg( dfuExecutable.fileName(), firmware);
    dfuFlashProcess.start( dfuCmd );
}

void dfuUtil::dfuListDevices()
{
    // Run dfu-util command
    QString dfuCmd = QString("%1 -l").arg( dfuUtil.fileName() );
    dfuScanProcess.start( dfuCmd );
}

void dfuUtil::dfuFlashStatus()
{
    // Append text to the viewer
    QString outtxt(dfuFlashProcess.readAllStandardOutput());
    int percentageLocation = outtxt.indexOf("%");
    int percentage = outtxt.mid(percentageLocation-3, 3).toInt();
    if (percentageLocation){
        emit progressUpdate(percentage);
    }
}

void dfuUtil::dfuFlashComplete( int exitCode )
{
    // Re-enable button after command completes

    // Append return code
    QString output = tr("Error: %1").arg( exitCode );
    switch (exitCode){
    case 74:
        ui->dfuResultsTextEdit->append(QString("File does not exist."));
        break;

    case 0:
        ui->dfuResultsTextEdit->append(QString("Success!"));
        break;

    default:
        ui->dfuResultsTextEdit->append(output);
        break;
    }
}


void dfuUtil::dfuScanStatus()
{
    // Append text to the viewer
    QString outtxt(dfuScanProcess.readAllStandardOutput());
    int percentageLocation = outtxt.indexOf("%");
    int percentage = outtxt.mid(percentageLocation-3, 3).toInt();
    if (percentageLocation){
        ui->flashProgress->setValue(percentage);
    }
    if (outtxt.contains("Found DFU: [0483:df11]")){
        repositoryUrl = "https://raw.githubusercontent.com/smrl/viafirmware/master/";
        QString serString = ("VIA mcu identified with Serial # ");
        serString.append(outtxt.right(15));
        ui->dfuResultsTextEdit->append(serString.trimmed());
        if (!m_haveRepo){
            // get appropriate repo
            ui->dfuResultsTextEdit->append("fetching repository...");
            httpRepo = new FileDownloader(QUrl("https://raw.githubusercontent.com/smrl/viafirmware/master/manifest.json"), this);
            connect(httpRepo, SIGNAL (downloaded()), this, SLOT (getRepository()));
        }
    // Scroll to bottom
    ui->dfuResultsTextEdit->verticalScrollBar()->setValue( ui->dfuResultsTextEdit->verticalScrollBar()->maximum() );
    }
}

void dfuUtil::dfuScanComplete( int exitCode )
{
    // Append return code
    QString output = tr("Error: %1").arg( exitCode );
    if (exitCode != 0){
        ui->dfuResultsTextEdit->append(output);
    }
}

