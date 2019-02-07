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

class Process : public QObject
{
    Q_OBJECT
public:
    explicit Process(QObject *parent = 0);
    void checkForVia();
    int getFirmwareID();
    int getFirmwareVersion();
    void savePresets();
    void loadPresetFile(QString);
    void flashFirmware(QString);
    void savePresetAsCal();
    QString generatePresetName();
    QString generateCalibrationName();
    QDateTime getLastPreset(int, int);
    QDateTime getLastCalibration();
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


private:
    QString m_path;  //QDir::currentPath();
    QString m_executable;
    unsigned char m_firmwareID;
    unsigned char m_firmwareVersion;

signals:
    void updateStatus(int);
    void message(QString);
    void updateProgress(int);
    void viaFoundWithFirmware(QString);
    void viaHasNoCal();
    void success(bool);
    void dfuBeganFlashing();



public slots:
    void parseFlashProgress();
    void parseScan();
    void parseOptionBytes();
    void checkOptionBytesSuccess(int);
    void showOB();
};

#endif // PROCESS_H
