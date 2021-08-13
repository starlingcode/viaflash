# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scales.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Sync3ScaleEdit(object):
    def setupUi(self, Sync3ScaleEdit):
        if not Sync3ScaleEdit.objectName():
            Sync3ScaleEdit.setObjectName(u"Sync3ScaleEdit")
        Sync3ScaleEdit.resize(400, 480)
        self.buttonBox = QDialogButtonBox(Sync3ScaleEdit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 440, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.horizontalLayoutWidget = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalLayoutWidget_2 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 60, 381, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.frame = QFrame(Sync3ScaleEdit)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 120, 81, 61))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(Sync3ScaleEdit)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 130, 131, 32))
        self.Denominator = QSpinBox(Sync3ScaleEdit)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setGeometry(QRect(220, 150, 84, 26))
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)
        self.Numerator = QSpinBox(Sync3ScaleEdit)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setGeometry(QRect(220, 120, 84, 26))
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)
        self.scrollArea = QScrollArea(Sync3ScaleEdit)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 190, 381, 111))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Sync3ScaleEdit)
        self.buttonBox.accepted.connect(Sync3ScaleEdit.accept)
        self.buttonBox.rejected.connect(Sync3ScaleEdit.reject)

        QMetaObject.connectSlotsByName(Sync3ScaleEdit)
    # setupUi

    def retranslateUi(self, Sync3ScaleEdit):
        Sync3ScaleEdit.setWindowTitle(QCoreApplication.translate("Sync3ScaleEdit", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Open Scale Set", None))
        self.pushButton.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Save Scale Set", None))
        self.pushButton_4.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Load Scale", None))
        self.pushButton_3.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Save Scale", None))
        self.pushButton_5.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Add Seed Ratio", None))
    # retranslateUi

