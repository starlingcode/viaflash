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
    QProcess dfuFlashFirmware;
    QProcess dfuFlashPresets;

private:
    QString m_path;  //QDir::currentPath();
    QString m_executable;
    int m_firmwareID;
    int m_firmwareVersion;




signals:
    void updateStatus(int);

public slots:
//    void parseFlashProgress();
    void parseScan();
};

#endif // PROCESS_H
