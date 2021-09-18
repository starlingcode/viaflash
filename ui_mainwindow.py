# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 224))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.comboBox.setPalette(palette1)
        self.comboBox.setInsertPolicy(QComboBox.InsertAtTop)
        self.comboBox.setFrame(False)

        self.verticalLayout.addWidget(self.comboBox)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(233, 0, 351, 618))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy1)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.label)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(233, 0, 351, 618))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy1)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.label)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit1Label.sizePolicy().hasHeightForWidth())
        self.edit1Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")
        sizePolicy2.setHeightForWidth(self.edit2Label.sizePolicy().hasHeightForWidth())
        self.edit2Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(233, 0, 351, 618))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy3)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.label)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit1Label.sizePolicy().hasHeightForWidth())
        self.edit1Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")
        sizePolicy2.setHeightForWidth(self.edit2Label.sizePolicy().hasHeightForWidth())
        self.edit2Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(233, 0, 351, 618))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy3)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.firmwareSelectLabel = QLabel(self.verticalLayoutWidget)
        self.firmwareSelectLabel.setObjectName(u"firmwareSelectLabel")
        self.firmwareSelectLabel.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firmwareSelectLabel.sizePolicy().hasHeightForWidth())
        self.firmwareSelectLabel.setSizePolicy(sizePolicy1)
        self.firmwareSelectLabel.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.firmwareSelectLabel)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit1Label.sizePolicy().hasHeightForWidth())
        self.edit1Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")
        sizePolicy2.setHeightForWidth(self.edit2Label.sizePolicy().hasHeightForWidth())
        self.edit2Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(233, 0, 351, 618))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy3)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.firmwareSelectLabel.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.firmwareSelectLabel = QLabel(self.verticalLayoutWidget)
        self.firmwareSelectLabel.setObjectName(u"firmwareSelectLabel")
        self.firmwareSelectLabel.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firmwareSelectLabel.sizePolicy().hasHeightForWidth())
        self.firmwareSelectLabel.setSizePolicy(sizePolicy1)
        self.firmwareSelectLabel.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.firmwareSelectLabel)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush5 = QBrush(QColor(92, 92, 92, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(77, 77, 77, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(64, 64, 64, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.loadDefaultButton.setPalette(palette2)
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit1Label.sizePolicy().hasHeightForWidth())
        self.edit1Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")
        sizePolicy2.setHeightForWidth(self.edit2Label.sizePolicy().hasHeightForWidth())
        self.edit2Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(240, -20, 351, 618))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy3)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.firmwareSelectLabel.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.firmwareSelectLabel = QLabel(self.verticalLayoutWidget)
        self.firmwareSelectLabel.setObjectName(u"firmwareSelectLabel")
        self.firmwareSelectLabel.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firmwareSelectLabel.sizePolicy().hasHeightForWidth())
        self.firmwareSelectLabel.setSizePolicy(sizePolicy1)
        self.firmwareSelectLabel.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.firmwareSelectLabel)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush5 = QBrush(QColor(92, 92, 92, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(77, 77, 77, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(64, 64, 64, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.loadDefaultButton.setPalette(palette2)
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit1Label.sizePolicy().hasHeightForWidth())
        self.edit1Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")
        sizePolicy2.setHeightForWidth(self.edit2Label.sizePolicy().hasHeightForWidth())
        self.edit2Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(240, -20, 351, 618))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy3)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.firmwareSelectLabel.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.firmwareSelectLabel = QLabel(self.verticalLayoutWidget)
        self.firmwareSelectLabel.setObjectName(u"firmwareSelectLabel")
        self.firmwareSelectLabel.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firmwareSelectLabel.sizePolicy().hasHeightForWidth())
        self.firmwareSelectLabel.setSizePolicy(sizePolicy1)
        self.firmwareSelectLabel.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.firmwareSelectLabel)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush5 = QBrush(QColor(92, 92, 92, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(77, 77, 77, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(64, 64, 64, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.loadDefaultButton.setPalette(palette2)
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit1Label.sizePolicy().hasHeightForWidth())
        self.edit1Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")
        sizePolicy2.setHeightForWidth(self.edit2Label.sizePolicy().hasHeightForWidth())
        self.edit2Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(240, -20, 351, 618))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy3)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.firmwareSelectLabel.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(496, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(496, 750))
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"IBM Plex Sans"])
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAcceptDrops(False)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 211, 451))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.detectButton = QPushButton(self.verticalLayoutWidget)
        self.detectButton.setObjectName(u"detectButton")

        self.verticalLayout.addWidget(self.detectButton)

        self.firmwareSelectLabel = QLabel(self.verticalLayoutWidget)
        self.firmwareSelectLabel.setObjectName(u"firmwareSelectLabel")
        self.firmwareSelectLabel.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.firmwareSelectLabel.sizePolicy().hasHeightForWidth())
        self.firmwareSelectLabel.setSizePolicy(sizePolicy1)
        self.firmwareSelectLabel.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.firmwareSelectLabel)

        self.firmwareSelect = QComboBox(self.verticalLayoutWidget)
        self.firmwareSelect.setObjectName(u"firmwareSelect")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(214, 214, 214, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        self.firmwareSelect.setPalette(palette1)
        self.firmwareSelect.setInsertPolicy(QComboBox.InsertAtTop)
        self.firmwareSelect.setFrame(False)

        self.verticalLayout.addWidget(self.firmwareSelect)

        self.loadDefaultButton = QRadioButton(self.verticalLayoutWidget)
        self.loadDefaultButton.setObjectName(u"loadDefaultButton")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush5 = QBrush(QColor(92, 92, 92, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush5)
        brush6 = QBrush(QColor(77, 77, 77, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush6)
        brush7 = QBrush(QColor(64, 64, 64, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.loadDefaultButton.setPalette(palette2)
        self.loadDefaultButton.setFont(font)
        self.loadDefaultButton.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"color:rgb(255,255,255);")

        self.verticalLayout.addWidget(self.loadDefaultButton)

        self.firmwareInfoButton = QPushButton(self.verticalLayoutWidget)
        self.firmwareInfoButton.setObjectName(u"firmwareInfoButton")

        self.verticalLayout.addWidget(self.firmwareInfoButton)

        self.edit1Label = QLabel(self.verticalLayoutWidget)
        self.edit1Label.setObjectName(u"edit1Label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.edit1Label.sizePolicy().hasHeightForWidth())
        self.edit1Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit1Label)

        self.edit1Select = QComboBox(self.verticalLayoutWidget)
        self.edit1Select.setObjectName(u"edit1Select")

        self.verticalLayout.addWidget(self.edit1Select)

        self.openEdit1 = QPushButton(self.verticalLayoutWidget)
        self.openEdit1.setObjectName(u"openEdit1")

        self.verticalLayout.addWidget(self.openEdit1)

        self.edit2Label = QLabel(self.verticalLayoutWidget)
        self.edit2Label.setObjectName(u"edit2Label")
        sizePolicy2.setHeightForWidth(self.edit2Label.sizePolicy().hasHeightForWidth())
        self.edit2Label.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.edit2Label)

        self.edit2Select = QComboBox(self.verticalLayoutWidget)
        self.edit2Select.setObjectName(u"edit2Select")

        self.verticalLayout.addWidget(self.edit2Select)

        self.openEdit2 = QPushButton(self.verticalLayoutWidget)
        self.openEdit2.setObjectName(u"openEdit2")

        self.verticalLayout.addWidget(self.openEdit2)

        self.flashButton = QPushButton(self.verticalLayoutWidget)
        self.flashButton.setObjectName(u"flashButton")

        self.verticalLayout.addWidget(self.flashButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.faceplate = QLabel(self.centralWidget)
        self.faceplate.setObjectName(u"faceplate")
        self.faceplate.setGeometry(QRect(240, 0, 351, 618))
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.faceplate.sizePolicy().hasHeightForWidth())
        self.faceplate.setSizePolicy(sizePolicy3)
        self.faceplate.setLayoutDirection(Qt.LeftToRight)
        self.faceplate.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"VIA Flash Utility", None))
        self.detectButton.setText(QCoreApplication.translate("MainWindow", u"Detect Via Module", None))
        self.firmwareSelectLabel.setText(QCoreApplication.translate("MainWindow", u"Select Firmware:", None))
        self.loadDefaultButton.setText(QCoreApplication.translate("MainWindow", u"Load Default Presets", None))
        self.firmwareInfoButton.setText(QCoreApplication.translate("MainWindow", u"Firmware Info", None))
        self.edit1Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 1:", None))
        self.openEdit1.setText(QCoreApplication.translate("MainWindow", u"Open Editor 1", None))
        self.edit2Label.setText(QCoreApplication.translate("MainWindow", u"Select Edit 2:", None))
        self.openEdit2.setText(QCoreApplication.translate("MainWindow", u"Open Editor 2", None))
        self.flashButton.setText(QCoreApplication.translate("MainWindow", u"Flash!", None))
        self.faceplate.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

