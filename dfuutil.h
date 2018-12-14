#ifndef DFUUTIL_H
#define DFUUTIL_H

#include <QObject>
#include <QFile>
#include <QFileInfo>
#include <QProcess>
#include <QByteArray>
#include <QDesktopServices>
#include <QCoreApplication>

class dfuUtil : public QObject
{
    Q_OBJECT
    

public:
    QString binaryPath;
    explicit dfuUtil(QObject *parent = nullptr);
    virtual ~dfuUtil();
    void flashFirmware(QString);
    void flashPresets(QString);
    void readPresets(QString);
    QByteArray getFirmwareID();
    QString getSerialNumber();
    bool checkToolExists(QFile *);
    QFile dfuExecutable;

private:

    QProcess dfuFlashProcess;
    QProcess dfuScanProcess;
    void dfuFlashStatus();
    void dfuFlashComplete( int exitCode );
    void dfuScanStatus();

signals:
    void dfuSuccess();
    int progressUpdate();

public slots:

};
#endif // DFUUTIL_H
