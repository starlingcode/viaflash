/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.5.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout;
    QGridLayout *gridLayout;
    QHBoxLayout *horizontalLayout;
    QLineEdit *fileBrowseLineEdit;
    QPushButton *fileBrowseButton;
    QPushButton *listDevicesButton;
    QRadioButton *FreeRunningFirmwareSelector;
    QRadioButton *CustomFirmwareSelector;
    QRadioButton *PLLFirmwareSelector;
    QLabel *faceplate;
    QProgressBar *flashProgress;
    QTextEdit *dfuResultsTextEdit;
    QRadioButton *GateSequencerFirmwareSelector;
    QPushButton *flashButton;
    QRadioButton *radioButton;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(734, 620);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        MainWindow->setAcceptDrops(false);
        MainWindow->setAutoFillBackground(false);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        centralWidget->setEnabled(true);
        QSizePolicy sizePolicy1(QSizePolicy::MinimumExpanding, QSizePolicy::MinimumExpanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy1);
        verticalLayout = new QVBoxLayout(centralWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        gridLayout = new QGridLayout();
        gridLayout->setSpacing(6);
        gridLayout->setObjectName(QStringLiteral("gridLayout"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        fileBrowseLineEdit = new QLineEdit(centralWidget);
        fileBrowseLineEdit->setObjectName(QStringLiteral("fileBrowseLineEdit"));
        fileBrowseLineEdit->setReadOnly(false);

        horizontalLayout->addWidget(fileBrowseLineEdit);

        fileBrowseButton = new QPushButton(centralWidget);
        fileBrowseButton->setObjectName(QStringLiteral("fileBrowseButton"));

        horizontalLayout->addWidget(fileBrowseButton);


        gridLayout->addLayout(horizontalLayout, 0, 0, 1, 1);

        listDevicesButton = new QPushButton(centralWidget);
        listDevicesButton->setObjectName(QStringLiteral("listDevicesButton"));

        gridLayout->addWidget(listDevicesButton, 7, 0, 1, 1);

        FreeRunningFirmwareSelector = new QRadioButton(centralWidget);
        FreeRunningFirmwareSelector->setObjectName(QStringLiteral("FreeRunningFirmwareSelector"));

        gridLayout->addWidget(FreeRunningFirmwareSelector, 3, 0, 1, 1);

        CustomFirmwareSelector = new QRadioButton(centralWidget);
        CustomFirmwareSelector->setObjectName(QStringLiteral("CustomFirmwareSelector"));

        gridLayout->addWidget(CustomFirmwareSelector, 2, 0, 1, 1);

        PLLFirmwareSelector = new QRadioButton(centralWidget);
        PLLFirmwareSelector->setObjectName(QStringLiteral("PLLFirmwareSelector"));

        gridLayout->addWidget(PLLFirmwareSelector, 4, 0, 1, 1);

        faceplate = new QLabel(centralWidget);
        faceplate->setObjectName(QStringLiteral("faceplate"));
        faceplate->setMinimumSize(QSize(281, 600));
        faceplate->setTextFormat(Qt::PlainText);
        faceplate->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop);

        gridLayout->addWidget(faceplate, 0, 1, 12, 1);

        flashProgress = new QProgressBar(centralWidget);
        flashProgress->setObjectName(QStringLiteral("flashProgress"));
        flashProgress->setValue(0);

        gridLayout->addWidget(flashProgress, 10, 0, 1, 1);

        dfuResultsTextEdit = new QTextEdit(centralWidget);
        dfuResultsTextEdit->setObjectName(QStringLiteral("dfuResultsTextEdit"));
        QSizePolicy sizePolicy2(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(dfuResultsTextEdit->sizePolicy().hasHeightForWidth());
        dfuResultsTextEdit->setSizePolicy(sizePolicy2);
        dfuResultsTextEdit->setReadOnly(true);

        gridLayout->addWidget(dfuResultsTextEdit, 11, 0, 1, 1);

        GateSequencerFirmwareSelector = new QRadioButton(centralWidget);
        GateSequencerFirmwareSelector->setObjectName(QStringLiteral("GateSequencerFirmwareSelector"));

        gridLayout->addWidget(GateSequencerFirmwareSelector, 5, 0, 1, 1);

        flashButton = new QPushButton(centralWidget);
        flashButton->setObjectName(QStringLiteral("flashButton"));

        gridLayout->addWidget(flashButton, 8, 0, 1, 1);

        radioButton = new QRadioButton(centralWidget);
        radioButton->setObjectName(QStringLiteral("radioButton"));

        gridLayout->addWidget(radioButton, 6, 0, 1, 1);


        verticalLayout->addLayout(gridLayout);

        MainWindow->setCentralWidget(centralWidget);
        QWidget::setTabOrder(fileBrowseButton, fileBrowseLineEdit);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "VIA Flashing Utility", 0));
        fileBrowseLineEdit->setPlaceholderText(QApplication::translate("MainWindow", "Select Custom Firmware", 0));
        fileBrowseButton->setText(QApplication::translate("MainWindow", "Browse", 0));
        listDevicesButton->setText(QApplication::translate("MainWindow", "Detect Module", 0));
        FreeRunningFirmwareSelector->setText(QApplication::translate("MainWindow", "Free-Running", 0));
        CustomFirmwareSelector->setText(QApplication::translate("MainWindow", "Custom Firmware", 0));
        PLLFirmwareSelector->setText(QApplication::translate("MainWindow", "PLL", 0));
        faceplate->setText(QApplication::translate("MainWindow", "TextLabel", 0));
        GateSequencerFirmwareSelector->setText(QApplication::translate("MainWindow", "Gate Sequencer", 0));
        flashButton->setText(QApplication::translate("MainWindow", "Flash", 0));
        radioButton->setText(QApplication::translate("MainWindow", "OSC1", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
