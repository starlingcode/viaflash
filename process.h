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
#include <QChar>

class Process : public QObject
{
    Q_OBJECT
public:
    explicit Process(QObject *parent = 0);
    void checkForVia();
    bool checkToolExists();
    QString serial;
    int getFirmwareID();
    int getFirmwareVersion();
    void savePresets();
    void loadPresetFile(QString);
    void flashFirmware(QString);
    QProcess dfuScan;
    QProcess dfuDownloadOptionBytes;
    QProcess dfuFlashFirmware;
    QProcess dfuFlashPresets;

private:
    QString m_path;  //QDir::currentPath();
    QString m_executable;
    unsigned char m_firmwareID;
    unsigned char m_firmwareVersion;




signals:
    void updateStatus(int);
    void message(QString);

public slots:
//    void parseFlashProgress();
    void parseScan();
    void parseOptionBytes();
};

#endif // PROCESS_H
