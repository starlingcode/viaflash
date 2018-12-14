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
#include <QDateTime>
#include <QProcess>
#include "filedownloader.h"
#include "repo.h"
#include "process.h"
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

private slots:
    void loadImage();
    void initRepository();
    void detectedVia();
    void binaryDownloadError();
    void on_flashButton_clicked();
    void on_firmwareInfoButton_clicked();
    void on_detectButton_clicked();
    void on_comboBox_currentIndexChanged(int index);
    void on_comboBox_activated(int index);

private:
    Repo *repository;
    Ui::MainWindow *ui;
    QString selectedFirmware;
    int m_repoSize;
    bool m_haveRepo;
    bool m_enableStorePreset;
    bool m_local; // true if file is local, false if file is remote
    QFileInfo m_localFirmwareSelection;
    int m_localFirmwareIndex;
    bool m_flashing;
    FileDownloader *httpFaceplate;
    FileDownloader *httpBinary;
    FileDownloader *httpRepo;
    QString repositoryUrl;
    void downloadImage(QString token);
    void checkRepository();
    void downloadBinary(QString token);
    void selectLocalFirmware();
    bool checkDFU( QFile *dfuUtil );
    QPixmap blankPanel;
    void dfuFlashBinary();
    void dfuScanStatus();
    Process *dfuProcess;

};

#endif // MAINWINDOW_H
