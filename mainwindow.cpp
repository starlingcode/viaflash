/*
 * todo
 *
 *  get rid of m_flashing
 *
 */

#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "filedownloader.h"
#include "qdebug.h"
#include "repo.h"
#include <QFile>
#include <QString>
#include <QPixmap>
#include <QJsonDocument>
#include <QComboBox>
#include <QJsonObject>
#include <QJsonArray>
#include <QFileDialog>
#include <QBrush>

MainWindow::MainWindow(QWidget *parent) :

    QMainWindow(parent),
    ui(new Ui::MainWindow)

{
    ui->setupUi(this);
    //connect(httpBinary, SIGNAL (downloaded()), this, SLOT (saveBinaryToDisk()));

    // load default wireframe via faceplate before hardware is detected
    QPixmap wireframe("://img/wireframe.png");
    ui->faceplate->setPixmap(wireframe);

    // disable UI elements until hardware is detected
    ui->flashButton->setDisabled( true );
    ui->fileBrowseButton->setDisabled( true );

    connect( ui->listDevicesButton, SIGNAL( released() ), this, SLOT( dfuListDevices() ) );
    connect( &dfuFlashProcess, SIGNAL( readyReadStandardOutput() ), this, SLOT( dfuFlashStatus() ) );
    connect( &dfuFlashProcess, SIGNAL( finished( int, QProcess::ExitStatus ) ), this, SLOT( dfuFlashComplete( int ) ) );
    connect( &dfuScanProcess, SIGNAL( readyReadStandardOutput() ), this, SLOT( dfuScanStatus() ) );
    connect( &dfuScanProcess, SIGNAL( finished( int, QProcess::ExitStatus ) ), this, SLOT( dfuScanComplete( int ) ) );

    // Only use the included dfu-util
    binaryPath = QFileInfo( QCoreApplication::applicationFilePath() ).dir().absolutePath();
    dfuFlashProcess.setWorkingDirectory( binaryPath );
    dfuScanProcess.setWorkingDirectory( binaryPath );

    // Merge the output channels
    dfuFlashProcess.setProcessChannelMode( QProcess::MergedChannels );
    dfuScanProcess.setProcessChannelMode( QProcess::MergedChannels );

    m_haveRepo = 0;

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::getRepository()
{ 
    // download json and convert to UTF-8
    m_json = QJsonDocument::fromJson(QString(httpRepo->downloadedData()).toUtf8());
    if (!m_json.isNull()){
        m_haveRepo = true;
        ui->dfuResultsTextEdit->append("repository found!");
    }
    m_elements = m_json.array();
    m_repoSize = m_elements.size();
    ui->repoComboBox->insertItem(0, "Select From Repository...");

    // remember these are indexed starting from 1, not 0! (0 is dialog text)
    for (int i = 0; i < m_repoSize; i++){
        QJsonObject obj = m_elements.at(i).toObject();
        QJsonValue val = obj["name"];
        ui->repoComboBox->insertItem(i+1, val.toString());
    }

}



void MainWindow::downloadImage(QString token)
{
    httpFaceplate = new FileDownloader(QUrl(repositoryUrl + "/img/" + token + ".png"));
    connect(httpFaceplate, SIGNAL (downloaded()), this, SLOT (loadImage()));
}

void MainWindow::downloadBinary(QString token)
{
    httpBinary = new FileDownloader(QUrl(repositoryUrl + "/binaries/" + token + ".bin"));
    connect(httpBinary, SIGNAL (downloaded()), this, SLOT (saveBinaryToDisk()));
    connect(httpBinary, SIGNAL (networkError()), this, SLOT (binaryDownloadError()));
}

void MainWindow::loadImage()
{
    QPixmap newImage;
    newImage.loadFromData(httpFaceplate->downloadedData());
    ui->faceplate->setPixmap(newImage);
}

void MainWindow::saveBinaryToDisk()
{
    QFile file(httpBinary->fileName);
    file.open(QIODevice::WriteOnly);
    file.write(QByteArray(httpBinary->downloadedData()));
    file.close();
    if (m_flashing == true)
    {
    ui->dfuResultsTextEdit->append("flashing binary from repository...");
    dfuFlashBinary();
    }
}


void MainWindow::on_repoComboBox_currentIndexChanged(int index)
{
    if (index != 0){
        QBrush linkBrush;
        linkBrush.setColor(Qt::blue);
        linkBrush.setStyle(Qt::SolidPattern);
        ui->fileBrowseLineEdit->clear();
        QJsonObject obj = m_elements.at(index - 1).toObject();
        QJsonValue val = obj["name"];
        ui->firmwareInfo->setItem(0, 0, new QTableWidgetItem(QJsonValue(obj["name"]).toString()));
        m_latestVersion = QJsonValue(obj["latestVersion"]).toString();
        ui->firmwareInfo->setItem(0, 1, new QTableWidgetItem(m_latestVersion));
        ui->firmwareInfo->setItem(0, 2, new QTableWidgetItem(QJsonValue(obj["author"]).toString()));
        ui->firmwareInfo->setItem(0, 3, new QTableWidgetItem(QJsonValue(obj["license"]).toString()));
        QTableWidgetItem *sourceUrl = new QTableWidgetItem(QJsonValue(obj["sourceUrl"]).toString());
        sourceUrl->setForeground(linkBrush);
        ui->firmwareInfo->setItem(0, 4, sourceUrl);
        QTableWidgetItem *manualUrl = new QTableWidgetItem(QJsonValue(obj["manualUrl"]).toString());
        manualUrl->setForeground(linkBrush);
        ui->firmwareInfo->setItem(0, 5, manualUrl);
        ui->firmwareInfo->setItem(0, 6, new QTableWidgetItem(QJsonValue(obj["description"]).toString()));
        m_token = QJsonValue(obj["token"]).toString();
        downloadImage(m_token);
        ui->flashButton->setDisabled( false );
        m_local = false;
    }
    else
    {
        if (ui->fileBrowseLineEdit->text().isEmpty())
      {
        ui->flashButton->setDisabled( true );
        ui->firmwareInfo->setItem(0, 0, new QTableWidgetItem(""));
        ui->firmwareInfo->setItem(0, 1, new QTableWidgetItem(""));
        ui->firmwareInfo->setItem(0, 2, new QTableWidgetItem(""));
        ui->firmwareInfo->setItem(0, 3, new QTableWidgetItem(""));
        ui->firmwareInfo->setItem(0, 4, new QTableWidgetItem(""));
        ui->firmwareInfo->setItem(0, 5, new QTableWidgetItem(""));
        ui->firmwareInfo->setItem(0, 6, new QTableWidgetItem(""));
        }
    }


}

// Make sure dfu-util can be found
bool MainWindow::checkDFU( QFile *dfuUtil )
{
    // Make sure dfu-util exists
    if ( !dfuUtil->exists() )
    {
        // Error, dfu-util not installed locally
        QString output = tr("dfu-util cannot be found. Either build dfu-util and copy the binary to this directory or symlink it.\ne.g. ln -s /usr/bin/dfu-util %1/.").arg( binaryPath );
        ui->dfuResultsTextEdit->append( output );

        return false;
    }

    return true;
}

void MainWindow::dfuFlashBinary()
{
    // Check if file exists
    QFile flashFile(selectedFirmware);
    if ( !flashFile.exists() )
    {
        // Error if no file selected
        if ( flashFile.fileName() == QString() )
        {
            QString output = tr("No firmware selected...");
            ui->dfuResultsTextEdit->append( output );
            return;
        }
        // Error if it doesn't exist
        else
        {
            QString output = tr("'%1' does not exist...").arg( flashFile.fileName() );
            ui->dfuResultsTextEdit->append( output );
        }


    }

#ifdef WIN32
    QFile dfuUtil( binaryPath + "/" + "dfu-util.exe");
#else
    QFile dfuUtil( binaryPath + "/" + "dfu-util" );
#endif

    // Only run dfu-util if it exists
    if ( !checkDFU( &dfuUtil ) )
    {
        return;
    }

    // Run dfu-util command
    QString dfuCmd = QString("%1 --device 0483:df11 -a 0 -s 0x08000000 -D %2").arg( dfuUtil.fileName(), flashFile.fileName() );
    dfuFlashProcess.start( dfuCmd );

    // Disable the flash button while command is running
    ui->flashButton->setDisabled( true );
    //ui->firmwareInfo->setDisabled( true );
    ui->listDevicesButton->setDisabled( true );
}

void MainWindow::dfuListDevices()
{
#ifdef WIN32
    QFile dfuUtil( binaryPath + "/" + "dfu-util.exe");
#else
    QFile dfuUtil( binaryPath + "/" + "dfu-util" );
#endif

    // Only run dfu-util if it exists
    if ( !checkDFU( &dfuUtil ) )
    {
        return;
    }

    // Run dfu-util command
    QString dfuCmd = QString("%1 -l").arg( dfuUtil.fileName() );
    dfuScanProcess.start( dfuCmd );

    // Disable the flash button while command is running
    ui->flashButton->setDisabled( true );
    ui->listDevicesButton->setDisabled( true );

}

void MainWindow::dfuFlashStatus()
{
    // Append text to the viewer
    QString outtxt(dfuFlashProcess.readAllStandardOutput());
    int percentageLocation = outtxt.indexOf("%");
    int percentage = outtxt.mid(percentageLocation-3, 3).toInt();
    if (percentageLocation){
        ui->flashProgress->setValue(percentage);
        //ui->dfuResultsTextEdit->append( outtxt );
    }
}

void MainWindow::dfuFlashComplete( int exitCode )
{
    // Re-enable button after command completes
//	ui->flashButton->setDisabled( false );
    ui->listDevicesButton->setDisabled( false );

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
        ui->dfuResultsTextEdit->append(QString("Error!" + exitCode));
        break;
    }
}


void MainWindow::dfuScanStatus()
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
        ui->fileBrowseButton->setDisabled( false );
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

void MainWindow::dfuScanComplete( int exitCode )
{
    // Re-enable button after command completes
//	ui->flashButton->setDisabled( false );
    ui->listDevicesButton->setDisabled( false );

    // Append return code
    QString output = tr("Error: %1").arg( exitCode );
    if (exitCode != 0){
        ui->dfuResultsTextEdit->append(output);
    }
}


void MainWindow::on_firmwareInfo_itemClicked(QTableWidgetItem *item)
{
    if (item->text().contains("http")){
        QDesktopServices::openUrl(QUrl(item->text()));
    }
}

void MainWindow::on_fileBrowseButton_released()
{
    ui->fileBrowseLineEdit->setText(
        QFileDialog::getOpenFileName(
            this,
            tr("Select firmware"),
            QString(),
            tr("Via Firmware ( *.bin);;All Files ( * )")
        ));
    selectedFirmware = ui->fileBrowseLineEdit->text();
    if (!ui->fileBrowseLineEdit->text().isEmpty()){
    ui->repoComboBox->setCurrentIndex(0);
    ui->firmwareInfo->setItem(0, 0, new QTableWidgetItem("Custom Firmware"));
    ui->firmwareInfo->setItem(0, 1, new QTableWidgetItem("Unknown"));
    ui->firmwareInfo->setItem(0, 2, new QTableWidgetItem("Unknown"));
    ui->firmwareInfo->setItem(0, 3, new QTableWidgetItem("Unknown"));
    ui->firmwareInfo->setItem(0, 4, new QTableWidgetItem("Unknown"));
    ui->firmwareInfo->setItem(0, 5, new QTableWidgetItem("Unknown"));
    ui->firmwareInfo->setItem(0, 6, new QTableWidgetItem("Unknown"));
    QPixmap custom("://img/custom.png");
    ui->faceplate->setPixmap(custom);
    ui->flashButton->setDisabled( false );
    m_local = true;
}
}

void MainWindow::on_listDevicesButton_released()
{
    ui->dfuResultsTextEdit->append("detecting hardware...");
}

void MainWindow::on_flashButton_released()
{
    if (m_local == false){
        downloadBinary(m_token);
        selectedFirmware = (QString (m_token + ".bin"));
        ui->dfuResultsTextEdit->append("downloading firmware from repository...");
        m_flashing = true;
    }
    else
    {
        dfuFlashBinary();
    }

}

void MainWindow::binaryDownloadError()
{
    ui->dfuResultsTextEdit->append("network error: content not found");
}
