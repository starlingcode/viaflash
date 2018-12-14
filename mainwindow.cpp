#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "qfontdatabase.h"

//QFontDatabase::addApplicationFont(":/fonts/IBMPlexMono-Regular");
//QString plexMono = QFontDatabase::applicationFontFamilies(db).at(0);
//QFont monospace(plexMono);

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->statusBar()->showMessage("No repository loaded; Local Mode");
    m_localFirmwareIndex = 0;  // index of local firmware in comboBox

    this->setFixedSize(QSize(584, 642));
    ui->flashButton->setDisabled(true);  // disable flash button until selection is made

    // load default wireframe via faceplate before hardware is detected
    blankPanel = QPixmap("://img/blank.png");
    ui->faceplate->setPixmap(blankPanel);

    // disable UI elements until hardware is detected
    ui->flashButton->setDisabled( true );
    ui->firmwareInfoButton->setDisabled( true );
    ui->loadDefaultButton->setCheckable(false);
    ui->loadSavedButton->setCheckable(false);

    this->statusBar()->showMessage("Local mode only, no repository loaded.");

    // Attempt to download repository
    repositoryUrl = "https://raw.githubusercontent.com/smrl/viafirmware/master/";
    httpRepo = new FileDownloader(QUrl("https://raw.githubusercontent.com/smrl/viafirmware/master/manifest.json"), this);
    connect(httpRepo, SIGNAL (downloaded()), this, SLOT (initRepository()));
    ui->comboBox->insertItem(0, "Select local firmware:");

    dfuProcess = new Process(this);
    connect( &dfuProcess->dfuScan, SIGNAL( finished( int, QProcess::ExitStatus ) ), this, SLOT( detectedVia() ) );
    connect( dfuProcess, SIGNAL( message( QString ) ), this, SLOT( updateStatusBar(QString) ) );
}

MainWindow::~MainWindow()
{
    delete ui;
}

// attempts a download of repository JSON file, starts new class with result.
void MainWindow::initRepository()
{
    repository = new Repo(httpRepo->downloadedData(), this);
    ui->comboBox->setCurrentIndex(-1);
    if (repository->exists){
        ui->statusBar->showMessage(repository->repoStatus);
        //populate firmware names in comboBox
        for (int i = 0; i < repository->length(); i++){
            ui->comboBox->insertItem(i, repository->nameAt(i));
        }
        // local firmware is located at the end of the list
        m_localFirmwareIndex = repository->length();
    }
}

void MainWindow::updateStatusBar(QString message)
{
    ui->statusBar->showMessage(message);
}

void MainWindow::on_flashButton_clicked()
{
    QProgressDialog progress;
    QString output = "<font face = 'IBM Plex Sans' size = 10> Flashing firmware...";
    progress.setLabelText(output);
    progress.exec();
}

void MainWindow::on_firmwareInfoButton_clicked()
{
    QMessageBox infoBox;
    infoBox.setIcon(QMessageBox::NoIcon);
    infoBox.setText(repository->firmwareInfo);
    infoBox.setStandardButtons(QMessageBox::Ok);
    infoBox.setDefaultButton(QMessageBox::Ok);
    infoBox.exec();
}

void MainWindow::binaryDownloadError()
{
    ui->statusBar->showMessage("network error: content not found");
}

void MainWindow::on_detectButton_clicked()
{
    ui->statusBar->showMessage("scanning for Via Modules...");
    dfuProcess->checkForVia();
}


void MainWindow::selectLocalFirmware()
{
    //disable firmware info button for local firmware
    ui->firmwareInfoButton->setDisabled( true );
    ui->comboBox->setCurrentIndex(m_localFirmwareIndex);
    ui->faceplate->setPixmap(blankPanel);
    m_localFirmwareSelection = QFileDialog::getOpenFileName(
            this,
            tr("Select firmware"),
            QString(),
            tr("Via Firmware ( *.bin);;All Files ( * )")
        );
    if(m_localFirmwareSelection.isFile()){
        ui->statusBar->showMessage("loaded " + m_localFirmwareSelection.fileName());
        ui->comboBox->setItemText(m_localFirmwareIndex, m_localFirmwareSelection.fileName());
    }

    else
    {
        ui->statusBar->showMessage("no file selected.");
        ui->comboBox->setCurrentIndex(-1);

    }
}

void MainWindow::on_comboBox_currentIndexChanged(int index)
{
}

void MainWindow::on_comboBox_activated(int index)
{
    if (index == m_localFirmwareIndex){
        ui->firmwareInfoButton->setDisabled( true );
        ui->loadDefaultButton->setCheckable(false);
        ui->loadSavedButton->setCheckable(false);
        repository->selectFirmware(0);// firmware 0 = non-repository acknowledged firmware
        selectLocalFirmware();}
    else
    {
        repository->selectFirmware(index);
        downloadImage(repository->firmwareToken);
        ui->firmwareInfoButton->setDisabled( false );
        ui->loadDefaultButton->setCheckable(true);
        ui->loadSavedButton->setCheckable(true);
        ui->statusBar->showMessage("fetched firmware information.");

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

void MainWindow::detectedVia()
{
    if (dfuProcess->serial != "")
    {
        //ui->statusBar->showMessage(QString("Via module found with serial # " + dfuProcess->serial));
        ui->flashButton->setDisabled(false);
    }
    else
    {
        //ui->statusBar->showMessage(QString("No hardware found -- Pushed DFU button?  Removed expander cable?"));
        ui->flashButton->setDisabled(true);
    }
}

void MainWindow::dfuScanStatus()
{/*
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
        if (!m_haveRepo){
            // get appropriate repo
            ui->dfuResultsTextEdit->append("fetching repository...");
            httpRepo = new FileDownloader(QUrl("https://raw.githubusercontent.com/smrl/viafirmware/master/manifest.json"), this);
            connect(httpRepo, SIGNAL (downloaded()), this, SLOT (getRepository()));
        }
    // Scroll to bottom
    ui->dfuResultsTextEdit->verticalScrollBar()->setValue( ui->dfuResultsTextEdit->verticalScrollBar()->maximum() );

}
*/
}
/*
void MainWindow::dfuScanComplete( int exitCode )
{
    // Re-enable button after command completes
//	ui->flashButton->setDisabled( false );
    ui->detectButton->setDisabled( false );

    // Append return code
    QString output = tr("Error: %1").arg( exitCode );
    if (exitCode != 0){
        ui->dfuResultsTextEdit->append(output);
    }
}

QDateTime now;
now = QDateTime::currentDateTime();
QString presetName = QString(ui->statusBar->showMessage(m_firmwareVal + now.toString(".yy-MM-dd.HH.mm.ss")) + ".preset");

*/

