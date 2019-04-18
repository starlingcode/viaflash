#include "mainwindow.h"
#include "ui_mainwindow.h"





MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    int plexMonoID = QFontDatabase::addApplicationFont(":/fonts/IBMPlexMono-Regular.ttf");
    int plexSansID = QFontDatabase::addApplicationFont(":/fonts/IBMPlexSans-Regular.ttf");

    qDebug() << plexMonoID;
    qDebug() << plexSansID;

    QFont plexSans = QFont("IBM Plex Sans", 10, 1);
    QFont plexMono = QFont("IBM Plex Mono", 10, 1);


    ui->setupUi(this);
    //ui->MainWindow->setFont(plexSans);
    ui->statusBar->setStyleSheet("background-color:rgb(0, 0, 0); color:rgb(255, 255, 255);");

    m_app_path = QCoreApplication::applicationDirPath();

    m_localFirmwareIndex = 0;  // index of local firmware in comboBox

    this->setFixedSize(QSize(585, 640));    //force size so no resizing possible

    ui->flashButton->setDisabled(true);  // disable flash button until selection is made

    // load default wireframe via faceplate before hardware is detected
    blankPanel = QPixmap("://img/blank.png");
    ui->faceplate->setPixmap(blankPanel);

    connect(this, SIGNAL( message( QString ) ), this, SLOT( updateStatusBar(QString) ) );

    // disable UI elements until hardware is detected
    ui->comboBox->setDisabled(true);
    ui->flashButton->setDisabled( true );
    ui->firmwareInfoButton->setDisabled( true );
    ui->loadDefaultButton->setCheckable(false);

    // Attempt to download repository
    emit message("Attempting to load repository...");
    ui->detectButton->setEnabled(false);
    repositoryUrl = "https://raw.githubusercontent.com/starlingcode/viafirmware/master/";
    httpRepo = new FileDownloader(QUrl("https://raw.githubusercontent.com/starlingcode/viafirmware/master/manifest.json"), this);
    connect(httpRepo, SIGNAL (downloaded()), this, SLOT (initRepository()));

    ui->comboBox->insertItem(0, "Select local firmware:");

    // dfuProcess handles interacting with dfu-util and the filesystem
    dfuProcess = new Process(this);

    connect( &dfuProcess->dfuScan, SIGNAL( finished( int, QProcess::ExitStatus ) ), this, SLOT( detectedVia() ) );
    connect( dfuProcess, SIGNAL( updateProgress( int ) ), this, SLOT( progressUpdater(int) ) );
    connect( &dfuProcess->dfuFlashFirmware, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( flashingFirmwareCompleted(int) ) );
    connect( &dfuProcess->dfuFlashPresets, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( flashingPresetsCompleted(int) ) );
    connect( dfuProcess, SIGNAL( viaFoundWithFirmware(QString)) , this, SLOT( viaFirmwareIDToName(QString)) );
    connect( dfuProcess, SIGNAL( viaHasNoCal()) , this, SLOT( promptForCalibration()) );
    connect( &dfuProcess->dfuUploadOptionBytes, SIGNAL( finished(int,QProcess::ExitStatus)), this, SLOT( optionBytesCompleted(int) ) );


    // messages globally get pushed onto the status bar
    connect( dfuProcess, SIGNAL( message( QString ) ), this, SLOT( updateStatusBar(QString) ) );
    connect( dfuProcess, SIGNAL( dfuBeganFlashing() ), this, SLOT( updateDfuFlashing() ) );



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
    ui->detectButton->setEnabled(true); // not in indeterminate state, can detect.
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
    if (haveRepo){
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
    if(haveRepo)
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
    QFileInfo binary;

    if (m_local)  // if the firmware is local
    {
        binary = m_localFirmwareSelection.filePath();
        qDebug() << m_localFirmwareSelection.filePath();
    }
    else
    {
        binary = m_app_path + "/" + selectedFirmware;
    }

    if (!binary.exists())
    {
        ud->setText("Firmware not found.");
//        ud->showButton("Cancel");
    }
    else if (binary.size() > 252000)
    {
        ud->setText("Firmware too large to flash!");
//        ud->showButton("Cancel");

    }
    else
    {
        ui->detectButton->setDisabled(true);
        ui->comboBox->setDisabled(true);
        ui->firmwareInfoButton->setDisabled(true);
        ui->flashButton->setDisabled(true);
        ui->loadDefaultButton->setDisabled(true);
        ud->setText(QString("Erasing Flash Memory..."));

        dfuProcess->flashFirmware(binary.absoluteFilePath());
    }
}


void MainWindow::updateDfuFlashing()
{
    if (m_local) // if it's a local firmware
    {
        QFileInfo binary = m_localFirmwareSelection;
        ud->setText(QString("Flashing " + QString::number(binary.size()) + " bytes..."));
    }
    else
    {
        QFileInfo binary = m_app_path + "/" + selectedFirmware;
        ud->setText(QString("Flashing " + QString::number(binary.size()) + " bytes..."));
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
        selectedFirmware = QString(m_localFirmwareSelection.fileName());
        m_local = true;
        ui->statusBar->showMessage("loaded " + selectedFirmware);
        ui->comboBox->setItemText(m_localFirmwareIndex, selectedFirmware);
        ui->flashButton->setEnabled(true);
    }

    else
    {
        ui->statusBar->showMessage("no file selected.");
        ui->comboBox->setCurrentIndex(-1);
        selectedFirmware = "";
        ui->flashButton->setEnabled(false);
        ui->comboBox->setItemText(m_localFirmwareIndex, "Select local firmware:");
        m_local = false;
    }
}

//void MainWindow::on_comboBox_currentIndexChanged(int index)
//{
//}

void MainWindow::on_comboBox_activated(int index)
{
    if (index == m_localFirmwareIndex)
    {
        ui->firmwareInfoButton->setDisabled( true );
        ui->loadDefaultButton->setCheckable(false);
        repository->selectFirmware(0);// firmware 0 = non-repository acknowledged firmware
        selectLocalFirmware();
    }
    else
    {
        m_local = false;
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
    if (dfuProcess->serial == "rial=UNKNOWN")  // fix for dfu - util .9
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

void MainWindow::flashingFirmwareCompleted(int exitCode)
{
    if (exitCode == 0)
    {
        if (ui->loadDefaultButton->isChecked())
        {
            QDateTime lastCalibration = dfuProcess->getLastCalibrationTime();
            if(lastCalibration.isValid())
            {
                dfuProcess->flashCalibration();
                ud->setText("Loading Calibration Data...");
            }
            else
            {
                qDebug() << "no calibration data to load.";
                flashingPresetsCompleted(0);
            }
        }
        else if (ui->comboBox->currentIndex() == m_localFirmwareIndex)
        {
            flashingPresetsCompleted(0);
        }
        else
        {
            dfuProcess->flashPresets();
            ud->setText("Restoring presets...");
        }
    }
    else
    {
        ud->setText("Flashing Firmware Failed.");
//        ud->showButton("Ok");
    }
}

void MainWindow::flashingPresetsCompleted(int exitCode)
{
    if (exitCode != 0)
    {
        qDebug() << "Flashing Presets Failed!";
        ud->setText("Flashing presets failed!");
//        ud->showButton("Ok");
    }
    if (ui->comboBox->currentIndex() == m_localFirmwareIndex) // if local firmware
    {
        dfuProcess->writeOptionBytes(0, 0);
    }
    else if (repository->firmwareOptionByte == 254)  // if calibration
    {
        dfuProcess->writeOptionBytes(254, 0);
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
    QFile downloadedBinary(m_app_path + "/" + selectedFirmware);
    downloadedBinary.remove(); // delete any existing firmware
    downloadedBinary.open(QIODevice::WriteOnly);
    downloadedBinary.write(httpBinary->downloadedData());
    //downloadedBinary.close();
    startFlash();
}

void MainWindow::binaryDownloadError()
{
    ud->setText("Flashing failed - file download error!");
//    ud->showButton("OK");
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


void MainWindow::optionBytesCompleted(int exitCode)
{
    if (exitCode == 0)
    {
        emit message("Remove module now.  To flash again, reconnect to USB and restart Viaflash.");
        ud->setText("Update succeeded!");
//        ud->showButton("Ok");

    }
    else
    {
        emit message(QString("dfu util exited with some other value: " + QString(exitCode)));
        ud->setText("Option byte error.");
//        ud->showButton("Ok");
    }
}

