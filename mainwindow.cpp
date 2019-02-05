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


    m_localFirmwareIndex = 0;  // index of local firmware in comboBox

    this->setFixedSize(QSize(584, 642));    //force size so no resizing possible

    ui->flashButton->setDisabled(true);  // disable flash button until selection is made

    // load default wireframe via faceplate before hardware is detected
    blankPanel = QPixmap("://img/blank.png");
    ui->faceplate->setPixmap(blankPanel);

    // disable UI elements until hardware is detected
    ui->comboBox->setDisabled(true);
    ui->flashButton->setDisabled( true );
    ui->firmwareInfoButton->setDisabled( true );
    ui->loadDefaultButton->setCheckable(false);
    emit message("Local mode only, no repository loaded.");

    // Attempt to download repository
    repositoryUrl = "https://raw.githubusercontent.com/smrl/viafirmware/master/";
    httpRepo = new FileDownloader(QUrl("https://raw.githubusercontent.com/smrl/viafirmware/master/manifest.json"), this);
    connect(httpRepo, SIGNAL (downloaded()), this, SLOT (initRepository()));

    ui->comboBox->insertItem(0, "Select local firmware:");

    // dfuProcess handles interacting with dfu-util and the filesystem
    dfuProcess = new Process(this);

    connect( &dfuProcess->dfuScan, SIGNAL( finished( int, QProcess::ExitStatus ) ), this, SLOT( detectedVia() ) );
    connect( dfuProcess, SIGNAL( updateProgress( int ) ), this, SLOT( progressUpdater(int) ) );
    connect( &dfuProcess->dfuFlashFirmware, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( flashingCompleted() ) );
    connect( dfuProcess, SIGNAL( viaFoundWithFirmware(QString)) , this, SLOT( viaFirmwareIDToName(QString)) );
    connect( dfuProcess, SIGNAL( viaHasNoCal()) , this, SLOT( promptForCalibration()) );
    connect( dfuProcess, SIGNAL( success(bool)) , this, SLOT( optionBytesCompleted(bool)) );

    // messages globally get pushed onto the status bar
    connect(this, SIGNAL( message( QString ) ), this, SLOT( updateStatusBar(QString) ) );
    connect( dfuProcess, SIGNAL( message( QString ) ), this, SLOT( updateStatusBar(QString) ) );



}

MainWindow::~MainWindow()
{
    delete ui;
}

// attempts a download of repository JSON file, constructs new object with result.
void MainWindow::initRepository()
{
    repository = new Repo(httpRepo->downloadedData(), this);
    connect( repository, SIGNAL( message( QString ) ), this, SLOT( updateStatusBar(QString) ) );
    if (repository->exists)
    {
        emit message("Firmware repository loaded.");
        haveRepo = true;
    }
    else
    {
        emit message("Firmware repository not loaded. Local mode only.");
        haveRepo = false;
    }

    // index of -1 is blank/unselected combobox entry
    ui->comboBox->setCurrentIndex(-1);
    if (repository->exists){
        //populate firmware names in comboBox
        for (int i = 0; i < repository->length(); i++){
            ui->comboBox->insertItem(i, repository->nameAt(i));
        }
        // local firmware is located at the end of the list
        m_localFirmwareIndex = repository->length();
    }
}

// sets message in status bar
void MainWindow::updateStatusBar(QString message)
{
    ui->statusBar->showMessage(message);
}

// helper to link firmware name with firmware ID when displaying currently installed firmware in status bar
void MainWindow::viaFirmwareIDToName(QString serial)
{
    if(repository->exists)
    {
        emit message(QString("Via found with Serial # " + serial + "     " + repository->returnFirmwareName(dfuProcess->getFirmwareID()) + " Firmware Version " + QString::number(dfuProcess->getFirmwareVersion()) + ". Saving Presets."));
    }
    else
    {
        emit message(QString("Via found with Serial # " + serial + "     Firmware ID " + QString::number(dfuProcess->getFirmwareID()) + " Version " + QString::number(dfuProcess->getFirmwareVersion()) + ". Saving Presets."));
    }
}

// initiate flashing process
void MainWindow::on_flashButton_clicked()
{
    ui->flashButton->setEnabled(false);
    ud = new updateDialog(this);
    if (ui->comboBox->currentIndex() == m_localFirmwareIndex) // local firmware
    {
        startFlash();
    }
    else
    {
        ud->setText("Downloading binary...");
        downloadBinary(selectedFirmware);
    }
}

void MainWindow::startFlash()
{

    QFileInfo binary = selectedFirmware;
    if (!binary.exists())
    {
        ud->setText("Firmware not found.");
        ud->showButton("Cancel");
    }
    else if (binary.size() > 252000)
    {
        ud->setText("Firmware too large to flash!");
        ud->showButton("Cancel");

    }
    else
    {
        ui->detectButton->setDisabled(true);
        ui->comboBox->setDisabled(true);
        ui->firmwareInfoButton->setDisabled(true);
        ui->flashButton->setDisabled(true);
        ui->loadDefaultButton->setDisabled(true);
        ud->setText(QString("Flashing " + QString::number(binary.size()) + " bytes..."));
        dfuProcess->flashFirmware(selectedFirmware);
    }
}

// firmware infobox display
void MainWindow::on_firmwareInfoButton_clicked()
{
    QMessageBox infoBox;
    infoBox.setIcon(QMessageBox::NoIcon);
    infoBox.setText(repository->firmwareInfo);
    infoBox.setStandardButtons(QMessageBox::Ok);
    infoBox.setDefaultButton(QMessageBox::Ok);
    infoBox.exec();
}

void MainWindow::downloadError()
{
    ui->statusBar->showMessage("download error: content not found");
}

void MainWindow::on_detectButton_clicked()
{
    ui->statusBar->showMessage("scanning for Via Modules...");
    ui->comboBox->setCurrentIndex(-1);
    ui->flashButton->setDisabled( true );
    ui->faceplate->setPixmap(blankPanel);
    ui->firmwareInfoButton->setDisabled( true );
    ui->loadDefaultButton->setCheckable(false);
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
        selectedFirmware = m_localFirmwareSelection.fileName();
        ui->statusBar->showMessage("loaded " + selectedFirmware);
        ui->comboBox->setItemText(m_localFirmwareIndex, selectedFirmware);
    }

    else
    {
        ui->statusBar->showMessage("no file selected.");
        ui->comboBox->setCurrentIndex(-1);
        selectedFirmware = "";

    }
}

void MainWindow::on_comboBox_currentIndexChanged(int index)
{
}

void MainWindow::on_comboBox_activated(int index)
{
    if (index == m_localFirmwareIndex)
    {
        ui->firmwareInfoButton->setDisabled( true );
        ui->loadDefaultButton->setCheckable(false);
        repository->selectFirmware(0);// firmware 0 = non-repository acknowledged firmware
        selectLocalFirmware();
        ui->flashButton->setEnabled(true);
    }
    else
    {
        repository->selectFirmware(index);
        downloadImage(repository->firmwareToken);
        ui->firmwareInfoButton->setDisabled( false );
        ui->loadDefaultButton->setCheckable(true);
        ui->statusBar->showMessage("fetched firmware information.");
        selectedFirmware = QString(repository->firmwareToken + ".bin");
        ui->flashButton->setEnabled(true);
        bool presetsExist = dfuProcess->checkPresetCondition(repository->firmwareOptionByte, repository->firmwareOptionByte2);
        if (presetsExist)
        {
            ui->loadDefaultButton->setChecked(false);
            ui->loadDefaultButton->setDisabled(false);
        }
        else
        {
            ui->loadDefaultButton->setChecked(true);
            ui->loadDefaultButton->setDisabled(true);
        }
    }
}


void MainWindow::downloadImage(QString token)
{
    httpFaceplate = new FileDownloader(QUrl(repositoryUrl + "/img/" + token + ".png"));
    connect(httpFaceplate, SIGNAL (downloaded()), this, SLOT (loadImage()));
}

void MainWindow::downloadBinary(QString token)
{
    httpBinary = new FileDownloader(QUrl(repositoryUrl + "/binaries/" + selectedFirmware));
    connect(httpBinary, SIGNAL (networkError()), this, SLOT (binaryDownloadError()));
    connect(httpBinary, SIGNAL (downloaded()), this, SLOT (binaryDownloadCompleted()));

}


void MainWindow::loadImage()
{
    QPixmap newImage;
    newImage.loadFromData(httpFaceplate->downloadedData());
    ui->faceplate->setPixmap(newImage);
}

void MainWindow::detectedVia()
{
    qDebug() << dfuProcess->serial;
    if (dfuProcess->serial == "rial=UNKNOWN")
    {
        QMessageBox detectError;
        detectError.setIcon(QMessageBox::Warning);
        detectError.setWindowTitle(" ");
        detectError.setText("Module found in incorrect state!");
        detectError.setInformativeText("Disconnect from USB, reconnect, and try detecting again.");
        detectError.setStandardButtons(QMessageBox::Ok);
        detectError.setDefaultButton(QMessageBox::Ok);
        detectError.exec();

        ui->statusBar->showMessage("Module found in wrong state.  Disconnect, reconnect, and try detecting again.");

    }
    else if (dfuProcess->serial != "")
    {
        ui->comboBox->setDisabled(false);

    }
    else
    {
        ui->flashButton->setDisabled(true);
        ui->comboBox->setDisabled(true);
    }
}

void MainWindow::flashingCompleted()
{
    if (ui->comboBox->currentIndex() == m_localFirmwareIndex) // if local firmware
    {
        dfuProcess->writeOptionBytes(0, 0);
    }
    else
    {
        if (ui->loadDefaultButton->isChecked())
        {
            dfuProcess->writeOptionBytes(254, 255);
        }
        else
        {
            dfuProcess->writeOptionBytes(repository->firmwareOptionByte, repository->firmwareOptionByte2);
        }
    }
    ud->setText("Writing option bytes...");
    ud->updateValue(100);
}

void MainWindow::binaryDownloadCompleted()
{
    QFile downloadedBinary(selectedFirmware);
    downloadedBinary.remove(); // delete any existing firmware
    downloadedBinary.open(QIODevice::WriteOnly);
    downloadedBinary.write(httpBinary->downloadedData());
    //downloadedBinary.close();
    startFlash();
}

void MainWindow::binaryDownloadError()
{
    ud->setText("Flashing failed - file download error!");
    ud->showButton("OK");
}

void MainWindow::progressUpdater(int percent)
{
    ud->updateValue(percent);
}


QString MainWindow::firmwareIDToString(int id)
{
    return repository->returnFirmwareName(id);
}

void MainWindow::promptForCalibration()
{
   QMessageBox calibrationDialog;
   calibrationDialog.setIcon(QMessageBox::Question);
   calibrationDialog.setWindowTitle(" ");
   calibrationDialog.setText("This Via has no stored calibration data on this computer.");
   calibrationDialog.setInformativeText("Would you like to store the calibration data on the module for future use?");
   calibrationDialog.setStandardButtons(QMessageBox::No | QMessageBox::Yes);
   calibrationDialog.setDefaultButton(QMessageBox::Yes);
   int ret = calibrationDialog.exec();
   switch (ret) {
     case QMessageBox::Yes:
         dfuProcess->savePresetAsCal();
     case QMessageBox::No:
         break;
     default:
         break;
   }
}

void MainWindow::optionBytesCompleted(bool success)
{
    if (success)
    {
        ud->setText("Firmware successfully loaded.");
        ud->showButton("Ok");
    }
    else
    {
        ud->setText("Option byte error.");
        ud->showButton("Ok");
    }
}

