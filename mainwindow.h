#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QString>
#include <QJsonDocument>
#include "filedownloader.h"
#include "repo.h"
#include <QTableWidget>
#include <QTableWidgetItem>
#include <QDesktopServices>
#include <QProcess>
#include <QFile>
#include <QScrollBar>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();


private:
    Ui::MainWindow *ui;
    FileDownloader *httpFaceplate;
    FileDownloader *httpBinary;
    FileDownloader *httpRepo;
    QString repositoryUrl;
    void downloadImage(QString token);
    void downloadBinary(QString token);
    bool checkDFU( QFile *dfuUtil );


    QProcess dfuFlashProcess;
    QProcess dfuScanProcess;
    QString binaryPath;
    QString selectedFirmware;
    QJsonDocument m_json;
    QJsonArray m_elements;
    int m_repoSize;
    bool m_haveRepo;
    bool m_local; // true if file is local, false if file is remote
    QString m_token;
    QString m_latestVersion;
    bool m_flashing;

private slots:
    void loadImage();
    void saveBinaryToDisk();
    void getRepository();
    void on_repoComboBox_currentIndexChanged(int index);
    void on_firmwareInfo_itemClicked(QTableWidgetItem *item);
    void on_fileBrowseButton_released();
    void on_listDevicesButton_released();
    void dfuFlashBinary();
    void dfuListDevices();
    void dfuFlashStatus();
    void dfuFlashComplete( int exitCode );
    void dfuScanStatus();
    void dfuScanComplete( int exitCode );
    void on_flashButton_released();
    void binaryDownloadError();
};

#endif // MAINWINDOW_H
