/* Copyright (C) 2014 by Jacob Alexander
 *
 * This file is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This file is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this file.  If not, see <http://www.gnu.org/licenses/>.
 */

// ----- Includes -----

// Qt
#include <QFileDialog>
#include <QScrollBar>
#include <QRadioButton>
#include <QPixmap>
#include <QString>
#include <QProgressBar>
// Local
#include "mainwindow.h"
#include "ui_mainwindow.h"



// ----- Functions -----

MainWindow::MainWindow( QWidget *parent ) : QMainWindow( parent ), ui( new Ui::MainWindow )
{
	ui->setupUi( this );

	// Connections
	connect( ui->fileBrowseButton, SIGNAL( released() ), this, SLOT( browseFiles() ) );
	connect( ui->flashButton, SIGNAL( released() ), this, SLOT( dfuFlashBinary() ) );
	connect( ui->CustomFirmwareSelector, SIGNAL( released() ), this, SLOT( setFirmwareCustom() ) );
	connect( ui->FreeRunningFirmwareSelector, SIGNAL( released() ), this, SLOT( setFirmwareFreeRunning() ) );
	connect( ui->PLLFirmwareSelector, SIGNAL( released() ), this, SLOT( setFirmwarePLL() ) );
	connect( ui->GateSequencerFirmwareSelector, SIGNAL( released() ), this, SLOT( setFirmwareGateSequencer() ) );
	connect( ui->listDevicesButton, SIGNAL( released() ), this, SLOT( dfuListDevices() ) );
	connect( &dfuUtilProcess, SIGNAL( readyReadStandardOutput() ), this, SLOT( dfuCommandStatus() ) );
	connect( &dfuUtilProcess, SIGNAL( finished( int, QProcess::ExitStatus ) ), this, SLOT( dfuCommandComplete( int ) ) );

	// Only use the included dfu-util
	binaryPath = QFileInfo( QCoreApplication::applicationFilePath() ).dir().absolutePath();
	dfuUtilProcess.setWorkingDirectory( binaryPath );

	// Merge the output channels
	dfuUtilProcess.setProcessChannelMode( QProcess::MergedChannels );
	
	// Display faceplate
    QPixmap customPixmap("://img/pll.png");
    QPixmap pllPixmap("://img/pll.png");
    QPixmap FreeRunningPixmap("://img/free-running.png");
    QPixmap GateSequencerPixmap("://img/gate-seqeuencer.png");
	ui->faceplate->setPixmap(customPixmap);
	ui->flashButton->setDisabled( true );
}

MainWindow::~MainWindow()
{
	delete ui;
}



// ----- Slots -----

void MainWindow::setFirmwareCustom()
{
        selectedFirmware = ( ui->fileBrowseLineEdit->text() );
    QPixmap customPixmap("://img/custom.png");
	ui->faceplate->setPixmap(customPixmap);
}


void MainWindow::setFirmwareFreeRunning()
{
        selectedFirmware = QString("FreeRunningFirmware.bin");
    QPixmap FreeRunningPixmap("://img/free-running.png");
	ui->faceplate->setPixmap(FreeRunningPixmap);
}

void MainWindow::setFirmwarePLL()
{
        selectedFirmware = QString("PLLFirmware.bin");
    QPixmap pllPixmap("://img/pll.png");
	ui->faceplate->setPixmap(pllPixmap);
}

void MainWindow::setFirmwareGateSequencer()
{
        selectedFirmware = QString("GateSequencerFirmware.bin");
    QPixmap GateSequencerPixmap("://img/gate-sequencer.png");
	ui->faceplate->setPixmap(GateSequencerPixmap);
}

void MainWindow::browseFiles()
{
	ui->fileBrowseLineEdit->setText(
		QFileDialog::getOpenFileName(
			this,
			tr("Select firmware"),
			QString(),
			tr("DFU Binary ( *.dfu);;All Files ( * )")
		)
	);
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
	// Set Custom Firmware if radiobutton is selected
	if (ui->CustomFirmwareSelector->isChecked()){
		setFirmwareCustom();
	}
	// Check if file exists
	QFile flashFile(selectedFirmware);
	if ( !flashFile.exists() )
	{
		// Error if no file selected
		if ( flashFile.fileName() == QString() )
		{
			QString output = tr("No file selected...");
			ui->dfuResultsTextEdit->append( output );
		}
		// Error if it doesn't exist
		else
		{
			QString output = tr("'%1' does not exist...").arg( flashFile.fileName() );
			ui->dfuResultsTextEdit->append( output );
		}

		return;
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
	QString dfuCmd = QString("%1 -a 0 -s 0x08000000 -D %2").arg( dfuUtil.fileName(), flashFile.fileName() );
	dfuUtilProcess.start( dfuCmd );

	// Disable the flash button while command is running
	ui->flashButton->setDisabled( true );
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
	dfuUtilProcess.start( dfuCmd );

	// Disable the flash button while command is running
	ui->flashButton->setDisabled( true );
	ui->listDevicesButton->setDisabled( true );
}

void MainWindow::dfuCommandStatus()
{
	// Append text to the viewer
	QString outtxt(dfuUtilProcess.readAllStandardOutput());
	int percentageLocation = outtxt.indexOf("%");
	int percentage = outtxt.mid(percentageLocation-3, 3).toInt();
	if (percentageLocation){
		ui->flashProgress->setValue(percentage);
	}
	if (outtxt.contains("Found DFU: [0483:df11]")){
		QString serString = ("VIA mcu identified with Serial # ");
		serString.append(outtxt.right(15));
		ui->dfuResultsTextEdit->append(serString);
		ui->flashButton->setDisabled( false );
	}
	// Scroll to bottom
	ui->dfuResultsTextEdit->verticalScrollBar()->setValue( ui->dfuResultsTextEdit->verticalScrollBar()->maximum() );
}

void MainWindow::dfuCommandComplete( int exitCode )
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

