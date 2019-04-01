#ifndef PROCESS_H
#define PROCESS_H

#include <QObject>
#include <QProcess>
#include <QString>
#include <QDateTime>
#include <QFileInfo>
#include <QFile>
#include <QDebug>
#include <QDir>
#include <QDateTime>
#include <QRegularExpression>
#include <QChar>
#include <QMainWindow>
#include <QCoreApplication>

class Process : public QObject
{
    Q_OBJECT
public:
    explicit Process(QObject *parent = 0);
    void checkForVia();
    int getFirmwareID();
    int getFirmwareVersion();
    void flashPresets();
    void flashCalibration();
    void flashFirmware(QString);
    void savePresetAsCal();
    QString generatePresetName();
    QString generateCalibrationName();
    QString getLastPreset(int);
    QDateTime getLastPresetTime(int);
    QString getLastPresetVersion(int);
    QDateTime getLastCalibrationTime();
    QString getLastCalibration();
    QString serial;
    QProcess dfuScan;
    QProcess dfuDownloadOptionBytes;
    QProcess dfuUploadOptionBytes;
    QProcess dfuDownloadPresets;
    QProcess dfuDownloadFirmware;
    QProcess dfuFlashFirmware;
    QProcess dfuFlashPresets;
    bool viaCanProvideCalibrationData();
    bool checkPresetCondition(int, int);
    void writeOptionBytes(unsigned char, unsigned char);
    void flashPresets(int);


private:
    QString m_path;  //QCoreApplication::applicationDirPath();
    QString m_executable;
    QString m_obpath;
    unsigned char m_firmwareID;
    unsigned char m_firmwareVersion;

signals:
    void updateStatus(int);
    void message(QString);
    void updateProgress(int);
    void viaFoundWithFirmware(QString);
    void viaHasNoCal();
    void dfuBeganFlashing();



public slots:
    void parseFlashProgress();
    void parseScan();
    void parseOptionBytes();
    void showOB();
    void savePresets(int);


};

#endif // PROCESS_H
