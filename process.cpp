#include "process.h"

Process::Process(QObject *parent) : QObject(parent)
{
    m_path = QDir::currentPath();

#ifdef WIN32
    m_executable = QString( m_path + "/" + "dfu-util.exe");
#else
    m_executable =  QString( m_path + "/" + "dfu-util" );
#endif

    // link dfu-util stdout to parseScan function
    connect( &dfuScan, SIGNAL( readyReadStandardOutput() ), this, SLOT( parseScan() ) );
    connect( &dfuFlashFirmware, SIGNAL( readyReadStandardOutput() ), this, SLOT( parseFlashProgress() ) );
    connect( &dfuDownloadOptionBytes, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( parseOptionBytes() ) );
    connect( &dfuDownloadPresets, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( savePresets() ) );
    connect( &dfuUploadOptionBytes, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( checkOptionBytesSuccess(int) ) );
    connect( &dfuUploadOptionBytes, SIGNAL( readyReadStandardOutput()), this, SLOT( showOB() ) );

}


void Process::checkForVia()
{
    if (QFile(m_executable).exists())
    {
        QString dfuCmd = QString("%1 -l").arg( m_executable );
        dfuScan.start( dfuCmd );
    }
    else
    {
        emit message("dfu-util not found. Check for dfu-util executable in program directory.");
    }
}

void Process::flashFirmware(QString filename)
{
    QString dfuCmd = QString("%1 --device 0483:df11 -a 0 -s 0x08000000 -D %2 -R").arg( m_executable, filename);
    dfuFlashFirmware.start( dfuCmd );
}

void Process::parseScan()
{
    QString outtxt = dfuScan.readAllStandardOutput();
    if (outtxt.contains("Found DFU: [0483:df11]"))
    {
        QString serString = outtxt.right(15);
        serial = serString.trimmed();
        serial.remove('"');
        // download option bytes
        QString dfuCmd = QString("%1 --device 0483:df11 -a 1 -s 0x1FFFF804:4 -U optionbytes.temp").arg( m_executable);
        emit message(QString("Via found with Serial # " + serial + "     Detecting Installed Firmware..."));
        dfuDownloadOptionBytes.start( dfuCmd );
    }
    else
    {
        emit message("No hardware detected -- Pushed DFU button?  Removed expander cable?");
    }
}

void Process::parseOptionBytes()
{
    QFile optionbytes("optionbytes.temp");
    char tmp;
    optionbytes.open(QIODevice::ReadOnly);
    optionbytes.read(&tmp,sizeof(char));
    m_firmwareID = tmp;
    optionbytes.read(&tmp,sizeof(char)); // complement, not needed.
    optionbytes.read(&tmp,sizeof(char));
    m_firmwareVersion = tmp;
    optionbytes.close();
    optionbytes.remove();
    if (m_firmwareID == 255 && m_firmwareVersion == 255)
    {
        emit message(QString("Via found with Serial # " + serial + "     Option bytes failure.  Presets won't be saved."));
        generatePresetName();
    }
    else if (m_firmwareID == 255 && m_firmwareVersion == 0)
    {
        emit message(QString("Via found with Serial # " + serial + "     Flash memory is blank.  A perfect time to calibrate."));
        generatePresetName();
    }
    else if (m_firmwareID == 0 && m_firmwareVersion == 0)
    {
        emit message(QString("Via found with Serial # " + serial + "     Firmware unknown, presets won't be saved."));
    }
    else if (m_firmwareID == 254 && m_firmwareVersion == 0)
    {
        emit message(QString("Via found with Serial # " + serial + "     Calibration Firmware loaded but no calibration data."));
    }
    else if (m_firmwareID == 254 && m_firmwareVersion == 255)
    {
        emit message(QString("Via found with Serial # " + serial + "     Calibration Data exists and is being stored."));
        savePresetAsCal();
    }
    else
    {
        emit viaFoundWithFirmware(serial);
        QString dfuCmd = QString("%1 --device 0483:df11 -a 0 -s 0x0803F000:4096 -U " + generatePresetName()).arg( m_executable);
        dfuDownloadPresets.start( dfuCmd );
        if (getLastCalibration().isValid() == false)
        {
            emit viaHasNoCal();
        }
    }
}


QString Process::generatePresetName()
{
    QDateTime now = QDateTime::currentDateTime();
    QString dateTime = now.toString("yyyyMMddHHmmss");
    QString outtxt = QString(QString::number(m_firmwareID) + "-" + QString::number(m_firmwareVersion) + "-" + serial + "-" + dateTime + ".preset");
    return outtxt;
}

QString Process::generateCalibrationName()
{
    QDateTime now = QDateTime::currentDateTime();
    QString dateTime = now.toString("yyyyMMddHHmmss");
    return QString(serial + "-" + dateTime + ".calibration");
}

QDateTime Process::getLastPreset(int firmwareID, int firmwareVersion)
{
    QDir directory(""); // no argument should yield same path as presets are stored.
    QDateTime lastPresetTime;
    QStringList presets = directory.entryList(QStringList() << "*.preset",QDir::Files);
    QStringList presetsForThisVia = presets.filter(QRegularExpression(serial));
    foreach(QString filename, presetsForThisVia) {
        QStringList presetVars = filename.split("-");
        if (((presetVars.at(0) == QString::number(firmwareID))))
        {

            QString dateTimeString = presetVars.at(3);

            dateTimeString = dateTimeString.remove(".preset");
            QDateTime dateTimeFromString = QDateTime::fromString(dateTimeString, "yyyyMMddHHmmss");
            if (dateTimeFromString > lastPresetTime)
            {
                lastPresetTime = dateTimeFromString;
            }
        }
    }
    return lastPresetTime;
}

QDateTime Process::getLastCalibration()
{
    QDir directory(""); // no argument should yield same path as calibration files are stored.
    QDateTime lastCalTime;
    QStringList cals = directory.entryList(QStringList() << "*.calibration",QDir::Files);
    QStringList calsForThisVia = cals.filter(QRegularExpression(serial));
    foreach(QString filename, calsForThisVia)
    {
        QStringList calVars = filename.split("-");
            QString dateTimeString = calVars.at(1);
            dateTimeString = dateTimeString.remove(".calibration");
            QDateTime dateTimeFromString = QDateTime::fromString(dateTimeString, "yyyyMMddHHmmss");
            if (dateTimeFromString > lastCalTime)
            {
                lastCalTime = dateTimeFromString;
            }
     }
    return lastCalTime;
}


void Process::parseFlashProgress()
{
    QString outtxt = dfuFlashFirmware.readAllStandardOutput();
    qDebug() << outtxt;
    int percentageLocation = outtxt.indexOf("%");
    int percentage = outtxt.mid(percentageLocation-3, 3).toInt();
    if (percentageLocation){
        emit updateProgress(percentage);
        if (outtxt.contains("Download") && !outtxt.contains("Downloading"))
        {
            emit dfuBeganFlashing();
        }
    }
}


void Process::savePresets()
{
emit message(QString("Via found with Serial # " + serial + "     Firmware ID " + QString(m_firmwareID) + " Version " + QString(m_firmwareVersion) + ". Presets stored."));
}


int Process::getFirmwareID()
{
    return (int)(m_firmwareID);
}

int Process::getFirmwareVersion()
{
    return (int)(m_firmwareVersion);
}

void Process::savePresetAsCal()
{
    QString dfuCmd = QString("%1 --device 0483:df11 -a 0 -s 0x0803F000:4096 -U " + generateCalibrationName()).arg( m_executable);
    dfuDownloadPresets.start( dfuCmd );
}

// returns false if no presets are available
bool Process::checkPresetCondition(int firmwareID, int firmwareVersion)
{

    QDateTime lastPreset = getLastPreset(firmwareID, firmwareVersion);
    if (firmwareID == 254)
    {
        emit message("Warning: running this firmware will invalidate all currently stored presets!");
        return false;
    }
    QDateTime lastCalibration = getLastCalibration();
    if (lastPreset.isValid())
    {
        if (lastCalibration.isValid())
        {
            if (lastPreset > lastCalibration)
            {
                QString lastStored = lastPreset.toString("ddd MMMM d yyyy hh:mm:ss");
                emit message(QString("Stored preset data is available for this firmware from " + lastStored));
                return true;
            }
            else
            {
                QString lastStored = lastCalibration.toString("ddd MMMM d yyyy");
                emit message(QString("Calibration data from " + lastStored +  " is newer than saved presets.  Loading Defaults."));
                return true;
            }
        }
        else
        {
            QString lastStored = lastPreset.toString("ddd MMMM d yyyy hh:mm:ss");
            emit message(QString("Stored preset data is available for this firmware from " + lastStored));
            return true;
        }
    }
    else
    {
        emit message(QString("No preset data available, will load default presets."));
        return false;
    }
}

void Process::writeOptionBytes(unsigned char firmwareID, unsigned char firmwareVersion)
{
    QFile optionbytes("optionbytes2.temp");
    char tmp[16];
    tmp[0] = 0xAA; // The value of this byte defines the Flash memory protection level
    tmp[1] = 0x55; // complement
    tmp[2] = 0xFF; // hardware watchdog/reset event configuration
    tmp[3] = 0x00; // complement
    tmp[4] = firmwareID;
    tmp[5] = ~firmwareID; // complement
    tmp[6] = firmwareVersion;
    tmp[7] = ~firmwareVersion; // complement
    tmp[8] = 0xFF; // write protect flash memory region off
    tmp[9] = 0x00; // complement
    tmp[10] = 0xFF; // write protect flash memory region off
    tmp[11] = 0x00; // complement
    tmp[12] = 0xFF; // write protect flash memory region off
    tmp[13] = 0x00; // complement
    tmp[14] = 0xFF; // write protect flash memory region off
    tmp[15] = 0x00; // complement
    qDebug() << tmp;
    optionbytes.open(QIODevice::WriteOnly);
    optionbytes.write(tmp,sizeof(tmp));
    optionbytes.close();
    QString dfuCmd = QString("%1 --device 0483:df11 -a 1 -s 0x1FFFF800:will-reset -D optionbytes2.temp").arg( m_executable);
    dfuUploadOptionBytes.start( dfuCmd );

}

void Process::checkOptionBytesSuccess(int exitCode)
{

    QFile optionbytes("optionbytes.temp");
    //optionbytes.remove();
    if (exitCode == 0)
    {
        emit message("Remove module now.  To flash again, reconnect to USB and restart Viaflash.");
        emit success(true);
    }
    else
    {
        emit message(QString("dfu util exited with some other value: " + QString(exitCode)));
        emit success(false);
    }
}

void Process::showOB()
{
    qDebug() << m_path;
    qDebug() << dfuUploadOptionBytes.readAllStandardOutput();
}
