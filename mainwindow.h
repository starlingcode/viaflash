#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QString>
#include <QMessageBox>
#include <QFont>
#include <QFontDatabase>
#include <QProgressDialog>
#include <QDesktopServices>
#include <QProcess>
#include <QFile>
#include <QFileDialog>
#include <QFileInfo>
#include <QIODevice>
#include <QProcess>
#include <QWidget>
#include <QDebug>
#include "filedownloader.h"
#include "repo.h"
#include "viaflash_process.h"
#include "updatedialog.h"
//#include "dfuutil.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    QString firmwareIDToString(int id);
    bool haveRepo;


public slots:
    void updateStatusBar(QString message);
    void progressUpdater(int percent);
    void viaFirmwareIDToName(QString serial);
    void promptForCalibration();
    void optionBytesCompleted(int);


private slots:
    void loadImage();
    void initRepository();
    void detectedVia();
    void updateDfuFlashing();
    void flashingFirmwareCompleted(int);
    void flashingPresetsCompleted(int);
    void downloadError();
    void binaryDownloadError();
    void on_flashButton_clicked();
    void on_firmwareInfoButton_clicked();
    void on_detectButton_clicked();
//    void on_comboBox_currentIndexChanged(int index);
    void on_comboBox_activated(int index);
    void binaryDownloadCompleted();

private:
    Repo *repository;
    Ui::MainWindow *ui;
    QString selectedFirmware;
    int m_repoSize;
    bool m_enableStorePreset;
    bool m_local; // true if file is local, false if file is remote
    QFileInfo m_localFirmwareSelection;
    int m_localFirmwareIndex;
    bool m_flashing;
    QString m_app_path;
    FileDownloader *httpFaceplate;
    FileDownloader *httpBinary;
    FileDownloader *httpRepo;
    QString repositoryUrl;
    void downloadImage(QString token);
    void checkRepository();
    void startFlash();
    void downloadBinary(QString token);
    void downloadPreset(QString token);
    void selectLocalFirmware();
    bool checkDFU(QFile *dfuUtil);
    QPixmap blankPanel;
    Process *dfuProcess;
    bool m_waiting;
    updateDialog *ud;


signals:
    void message(QString);
    void viaFoundWithFirmware(QString);

};

#endif // MAINWINDOW_H
