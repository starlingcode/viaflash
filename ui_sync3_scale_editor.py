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
        Sync3ScaleEdit.resize(400, 606)
        self.buttonBox = QDialogButtonBox(Sync3ScaleEdit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.loadScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.loadScaleSet.setObjectName(u"loadScaleSet")

        self.scalesSetButtons.addWidget(self.loadScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scaleSelect = QComboBox(self.horizontalLayoutWidget_2)
        self.scaleSelect.setObjectName(u"scaleSelect")

        self.horizontalLayout_2.addWidget(self.scaleSelect)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.horizontalLayout_2.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(Sync3ScaleEdit)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_3 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 60, 381, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.slotSelect = QGroupBox(self.horizontalLayoutWidget_3)
        self.slotSelect.setObjectName(u"slotSelect")
        self.slotSelect.setAlignment(Qt.AlignCenter)
        self.slot1 = QRadioButton(self.slotSelect)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setGeometry(QRect(30, 20, 41, 26))
        self.slot2 = QRadioButton(self.slotSelect)
        self.slot2.setObjectName(u"slot2")
        self.slot2.setGeometry(QRect(70, 20, 41, 26))
        self.slot3 = QRadioButton(self.slotSelect)
        self.slot3.setObjectName(u"slot3")
        self.slot3.setGeometry(QRect(110, 20, 41, 26))
        self.slot4 = QRadioButton(self.slotSelect)
        self.slot4.setObjectName(u"slot4")
        self.slot4.setGeometry(QRect(150, 20, 41, 26))
        self.slot5 = QRadioButton(self.slotSelect)
        self.slot5.setObjectName(u"slot5")
        self.slot5.setGeometry(QRect(190, 20, 41, 26))
        self.slot6 = QRadioButton(self.slotSelect)
        self.slot6.setObjectName(u"slot6")
        self.slot6.setGeometry(QRect(230, 20, 41, 26))
        self.slot7 = QRadioButton(self.slotSelect)
        self.slot7.setObjectName(u"slot7")
        self.slot7.setGeometry(QRect(270, 20, 41, 26))
        self.slot8 = QRadioButton(self.slotSelect)
        self.slot8.setObjectName(u"slot8")
        self.slot8.setGeometry(QRect(310, 20, 41, 26))

        self.horizontalLayout_3.addWidget(self.slotSelect)

        self.horizontalLayoutWidget_4 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 20, 381, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")

        self.horizontalLayout_6.addWidget(self.tileTritave)

        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")

        self.horizontalLayout_6.addWidget(self.tileFill)

        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")

        self.horizontalLayout_6.addWidget(self.tileOctave)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.verticalSlider)

        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.horizontalLayout_4.addWidget(self.dial)

        self.horizontalLayoutWidget_6 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.horizontalLayout_5.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_5.addWidget(self.addFromScala)


        self.retranslateUi(Sync3ScaleEdit)
        self.buttonBox.accepted.connect(Sync3ScaleEdit.accept)
        self.buttonBox.rejected.connect(Sync3ScaleEdit.reject)

        QMetaObject.connectSlotsByName(Sync3ScaleEdit)
    # setupUi

    def retranslateUi(self, Sync3ScaleEdit):
        Sync3ScaleEdit.setWindowTitle(QCoreApplication.translate("Sync3ScaleEdit", u"Dialog", None))
        self.loadScaleSet.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Open Scale Set", None))
        self.saveScaleSet.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Save Scale", None))
        self.slotSelect.setTitle(QCoreApplication.translate("Sync3ScaleEdit", u"Slot Select", None))
        self.slot1.setText(QCoreApplication.translate("Sync3ScaleEdit", u"1", None))
        self.slot2.setText(QCoreApplication.translate("Sync3ScaleEdit", u"2", None))
        self.slot3.setText(QCoreApplication.translate("Sync3ScaleEdit", u"3", None))
        self.slot4.setText(QCoreApplication.translate("Sync3ScaleEdit", u"4", None))
        self.slot5.setText(QCoreApplication.translate("Sync3ScaleEdit", u"5", None))
        self.slot6.setText(QCoreApplication.translate("Sync3ScaleEdit", u"6", None))
        self.slot7.setText(QCoreApplication.translate("Sync3ScaleEdit", u"7", None))
        self.slot8.setText(QCoreApplication.translate("Sync3ScaleEdit", u"8", None))
        self.groupBox.setTitle(QCoreApplication.translate("Sync3ScaleEdit", u"Tiling Method", None))
        self.tileTritave.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Tritave", None))
        self.tileFill.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Fill", None))
        self.tileOctave.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Octave", None))
        self.addSeedRatio.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Add From Scala", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
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
        Sync3ScaleEdit.resize(400, 606)
        self.buttonBox = QDialogButtonBox(Sync3ScaleEdit)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.scaleSelect = QComboBox(self.horizontalLayoutWidget_2)
        self.scaleSelect.setObjectName(u"scaleSelect")

        self.saveLoadScale.addWidget(self.scaleSelect)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(Sync3ScaleEdit)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_3 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 60, 381, 51))
        self.slotSelectButtons = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.slotSelectButtons.setObjectName(u"slotSelectButtons")
        self.slotSelectButtons.setContentsMargins(0, 0, 0, 0)
        self.slotSelect = QGroupBox(self.horizontalLayoutWidget_3)
        self.slotSelect.setObjectName(u"slotSelect")
        self.slotSelect.setAlignment(Qt.AlignCenter)
        self.slot1 = QRadioButton(self.slotSelect)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setGeometry(QRect(30, 20, 41, 26))
        self.slot2 = QRadioButton(self.slotSelect)
        self.slot2.setObjectName(u"slot2")
        self.slot2.setGeometry(QRect(70, 20, 41, 26))
        self.slot3 = QRadioButton(self.slotSelect)
        self.slot3.setObjectName(u"slot3")
        self.slot3.setGeometry(QRect(110, 20, 41, 26))
        self.slot4 = QRadioButton(self.slotSelect)
        self.slot4.setObjectName(u"slot4")
        self.slot4.setGeometry(QRect(150, 20, 41, 26))
        self.slot5 = QRadioButton(self.slotSelect)
        self.slot5.setObjectName(u"slot5")
        self.slot5.setGeometry(QRect(190, 20, 41, 26))
        self.slot6 = QRadioButton(self.slotSelect)
        self.slot6.setObjectName(u"slot6")
        self.slot6.setGeometry(QRect(230, 20, 41, 26))
        self.slot7 = QRadioButton(self.slotSelect)
        self.slot7.setObjectName(u"slot7")
        self.slot7.setGeometry(QRect(270, 20, 41, 26))
        self.slot8 = QRadioButton(self.slotSelect)
        self.slot8.setObjectName(u"slot8")
        self.slot8.setGeometry(QRect(310, 20, 41, 26))

        self.slotSelectButtons.addWidget(self.slotSelect)

        self.horizontalLayoutWidget_4 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 20, 381, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")

        self.horizontalLayout_6.addWidget(self.tileOctave)

        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")

        self.horizontalLayout_6.addWidget(self.tileTritave)

        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")

        self.horizontalLayout_6.addWidget(self.tileFill)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.previewControls.addWidget(self.verticalSlider)

        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.previewControls.addWidget(self.dial)

        self.horizontalLayoutWidget_6 = QWidget(Sync3ScaleEdit)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)


        self.retranslateUi(Sync3ScaleEdit)
        self.buttonBox.accepted.connect(Sync3ScaleEdit.accept)
        self.buttonBox.rejected.connect(Sync3ScaleEdit.reject)

        QMetaObject.connectSlotsByName(Sync3ScaleEdit)
    # setupUi

    def retranslateUi(self, Sync3ScaleEdit):
        Sync3ScaleEdit.setWindowTitle(QCoreApplication.translate("Sync3ScaleEdit", u"Dialog", None))
        self.saveScaleSet.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Save Scale", None))
        self.slotSelect.setTitle(QCoreApplication.translate("Sync3ScaleEdit", u"Slot Select", None))
        self.slot1.setText(QCoreApplication.translate("Sync3ScaleEdit", u"1", None))
        self.slot2.setText(QCoreApplication.translate("Sync3ScaleEdit", u"2", None))
        self.slot3.setText(QCoreApplication.translate("Sync3ScaleEdit", u"3", None))
        self.slot4.setText(QCoreApplication.translate("Sync3ScaleEdit", u"4", None))
        self.slot5.setText(QCoreApplication.translate("Sync3ScaleEdit", u"5", None))
        self.slot6.setText(QCoreApplication.translate("Sync3ScaleEdit", u"6", None))
        self.slot7.setText(QCoreApplication.translate("Sync3ScaleEdit", u"7", None))
        self.slot8.setText(QCoreApplication.translate("Sync3ScaleEdit", u"8", None))
        self.groupBox.setTitle(QCoreApplication.translate("Sync3ScaleEdit", u"Tiling Method", None))
        self.tileOctave.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Octave", None))
        self.tileTritave.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Tritave", None))
        self.tileFill.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Fill", None))
        self.addSeedRatio.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("Sync3ScaleEdit", u"Add From Scala", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 606)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.scaleSelect = QComboBox(self.horizontalLayoutWidget_2)
        self.scaleSelect.setObjectName(u"scaleSelect")

        self.saveLoadScale.addWidget(self.scaleSelect)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 60, 381, 51))
        self.slotSelectButtons = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.slotSelectButtons.setObjectName(u"slotSelectButtons")
        self.slotSelectButtons.setContentsMargins(0, 0, 0, 0)
        self.slotSelect = QGroupBox(self.horizontalLayoutWidget_3)
        self.slotSelect.setObjectName(u"slotSelect")
        self.slotSelect.setAlignment(Qt.AlignCenter)
        self.slot1 = QRadioButton(self.slotSelect)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setGeometry(QRect(30, 20, 41, 26))
        self.slot2 = QRadioButton(self.slotSelect)
        self.slot2.setObjectName(u"slot2")
        self.slot2.setGeometry(QRect(70, 20, 41, 26))
        self.slot3 = QRadioButton(self.slotSelect)
        self.slot3.setObjectName(u"slot3")
        self.slot3.setGeometry(QRect(110, 20, 41, 26))
        self.slot4 = QRadioButton(self.slotSelect)
        self.slot4.setObjectName(u"slot4")
        self.slot4.setGeometry(QRect(150, 20, 41, 26))
        self.slot5 = QRadioButton(self.slotSelect)
        self.slot5.setObjectName(u"slot5")
        self.slot5.setGeometry(QRect(190, 20, 41, 26))
        self.slot6 = QRadioButton(self.slotSelect)
        self.slot6.setObjectName(u"slot6")
        self.slot6.setGeometry(QRect(230, 20, 41, 26))
        self.slot7 = QRadioButton(self.slotSelect)
        self.slot7.setObjectName(u"slot7")
        self.slot7.setGeometry(QRect(270, 20, 41, 26))
        self.slot8 = QRadioButton(self.slotSelect)
        self.slot8.setObjectName(u"slot8")
        self.slot8.setGeometry(QRect(310, 20, 41, 26))

        self.slotSelectButtons.addWidget(self.slotSelect)

        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 20, 381, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")

        self.horizontalLayout_6.addWidget(self.tileOctave)

        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")

        self.horizontalLayout_6.addWidget(self.tileTritave)

        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")

        self.horizontalLayout_6.addWidget(self.tileFill)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.previewControls.addWidget(self.verticalSlider)

        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.previewControls.addWidget(self.dial)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Dialog", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.slotSelect.setTitle(QCoreApplication.translate("sync3ScaleEditor", u"Slot Select", None))
        self.slot1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.groupBox.setTitle(QCoreApplication.translate("sync3ScaleEditor", u"Tiling Method", None))
        self.tileOctave.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 606)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 60, 381, 51))
        self.slotSelectButtons = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.slotSelectButtons.setObjectName(u"slotSelectButtons")
        self.slotSelectButtons.setContentsMargins(0, 0, 0, 0)
        self.slotSelect = QGroupBox(self.horizontalLayoutWidget_3)
        self.slotSelect.setObjectName(u"slotSelect")
        self.slotSelect.setAlignment(Qt.AlignCenter)
        self.slot1 = QRadioButton(self.slotSelect)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setGeometry(QRect(30, 20, 41, 26))
        self.slot2 = QRadioButton(self.slotSelect)
        self.slot2.setObjectName(u"slot2")
        self.slot2.setGeometry(QRect(70, 20, 41, 26))
        self.slot3 = QRadioButton(self.slotSelect)
        self.slot3.setObjectName(u"slot3")
        self.slot3.setGeometry(QRect(110, 20, 41, 26))
        self.slot4 = QRadioButton(self.slotSelect)
        self.slot4.setObjectName(u"slot4")
        self.slot4.setGeometry(QRect(150, 20, 41, 26))
        self.slot5 = QRadioButton(self.slotSelect)
        self.slot5.setObjectName(u"slot5")
        self.slot5.setGeometry(QRect(190, 20, 41, 26))
        self.slot6 = QRadioButton(self.slotSelect)
        self.slot6.setObjectName(u"slot6")
        self.slot6.setGeometry(QRect(230, 20, 41, 26))
        self.slot7 = QRadioButton(self.slotSelect)
        self.slot7.setObjectName(u"slot7")
        self.slot7.setGeometry(QRect(270, 20, 41, 26))
        self.slot8 = QRadioButton(self.slotSelect)
        self.slot8.setObjectName(u"slot8")
        self.slot8.setGeometry(QRect(310, 20, 41, 26))

        self.slotSelectButtons.addWidget(self.slotSelect)

        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 20, 381, 31))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")

        self.horizontalLayout_6.addWidget(self.tileOctave)

        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")

        self.horizontalLayout_6.addWidget(self.tileTritave)

        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")

        self.horizontalLayout_6.addWidget(self.tileFill)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.previewControls.addWidget(self.verticalSlider)

        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.previewControls.addWidget(self.dial)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Dialog", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.slotSelect.setTitle(QCoreApplication.translate("sync3ScaleEditor", u"Slot Select", None))
        self.slot1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.groupBox.setTitle(QCoreApplication.translate("sync3ScaleEditor", u"Tiling Method", None))
        self.tileOctave.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 381, 111))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.widget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.widget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.widget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.widget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.widget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.widget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.widget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.widget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.widget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.widget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.widget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.widget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.widget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.widget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.widget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.widget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Dialog", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.groupBox.setTitle("")
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 381, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.widget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.widget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.widget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.widget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.widget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.widget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.widget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.widget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.widget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.widget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.widget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.widget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.widget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.widget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.widget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.widget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Dialog", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
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
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 381, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Dialog", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
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
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 381, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Dialog", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 381, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 341, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 341, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Numerator.setObjectName(u"Numerator")
        self.Numerator.setMinimum(1)
        self.Numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Numerator)

        self.Denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.Denominator.setObjectName(u"Denominator")
        self.Denominator.setMinimum(1)
        self.Denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.Denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.seedRatioEditor.addItem(self.horizontalSpacer)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 341, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tileOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileOctave.setObjectName(u"tileOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tileOctave.sizePolicy().hasHeightForWidth())
        self.tileOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.tileOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tileFill = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileFill.setObjectName(u"tileFill")
        sizePolicy.setHeightForWidth(self.tileFill.sizePolicy().hasHeightForWidth())
        self.tileFill.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.tileFill)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(256)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.seedRatioEditor.addItem(self.horizontalSpacer)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.tileOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.tileFill.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 341, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tileTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.tileTritave.setObjectName(u"tileTritave")
        sizePolicy.setHeightForWidth(self.tileTritave.sizePolicy().hasHeightForWidth())
        self.tileTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.tileTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 409, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_6)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.seedRatioEditor.addWidget(self.clearSeedRatios)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.tileTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Expand", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 341, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 409, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_6)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.seedRatioEditor.addWidget(self.clearSeedRatios)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Expand", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Seed Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 331, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.previewLayout.addLayout(self.horizontalLayout_15)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 412, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_6)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.seedRatioEditor.addWidget(self.clearSeedRatios)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Expand", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 331, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalSlider = QSlider(self.horizontalLayoutWidget_5)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(15)
        self.verticalSlider.setValue(8)
        self.verticalSlider.setSliderPosition(8)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.dial = QDial(self.horizontalLayoutWidget_5)
        self.dial.setObjectName(u"dial")
        self.dial.setMaximum(15)
        self.dial.setPageStep(8)

        self.verticalLayout_6.addWidget(self.dial)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 412, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_6)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.seedRatioEditor.addWidget(self.clearSeedRatios)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Expand", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(10, 240, 381, 111))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 331, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 360, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 420, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(15)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 412, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.addFromScala = QPushButton(self.horizontalLayoutWidget_6)
        self.addFromScala.setObjectName(u"addFromScala")

        self.seedRatioEditor.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_6)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.seedRatioEditor.addWidget(self.clearSeedRatios)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Expand", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectScaleSet = QComboBox(self.horizontalLayoutWidget)
        self.selectScaleSet.setObjectName(u"selectScaleSet")

        self.scalesSetButtons.addWidget(self.selectScaleSet)

        self.saveScaleSet = QPushButton(self.horizontalLayoutWidget)
        self.saveScaleSet.setObjectName(u"saveScaleSet")

        self.scalesSetButtons.addWidget(self.saveScaleSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveScale = QPushButton(self.horizontalLayoutWidget_2)
        self.saveScale.setObjectName(u"saveScale")

        self.saveLoadScale.addWidget(self.saveScale)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -20, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(15)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveScaleSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveScale.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(15)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectScale = QComboBox(self.horizontalLayoutWidget_2)
        self.selectScale.setObjectName(u"selectScale")

        self.saveLoadScale.addWidget(self.selectScale)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(15)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(15)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        sync3ScaleEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setFrameShadow(QFrame.Sunken)
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 105))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setFrameShadow(QFrame.Sunken)
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(True)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(6, 0, 363, 85))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setFrameShadow(QFrame.Sunken)
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(True)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(6, 0, 363, 85))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setFrameShadow(QFrame.Sunken)
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(6, 0, 363, 85))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setFrameShadow(QFrame.Sunken)
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(6, 0, 363, 85))
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy1)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(400, 640)
        self.buttonBox = QDialogButtonBox(sync3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 601, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(11, 31, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(12, 121, 381, 41))
        self.saveLoadScale = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.saveLoadScale.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)

        self.seedRatios = QScrollArea(sync3ScaleEditor)
        self.seedRatios.setObjectName(u"seedRatios")
        self.seedRatios.setGeometry(QRect(11, 291, 381, 91))
        self.seedRatios.setFrameShadow(QFrame.Sunken)
        self.seedRatios.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.seedRatios.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.seedRatios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.seedRatios.setWidgetResizable(False)
        self.seedRatios.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(6, 0, 363, 85))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 351, 241))
        self.seedRatioGrid = QGridLayout(self.gridLayoutWidget)
        self.seedRatioGrid.setObjectName(u"seedRatioGrid")
        self.seedRatioGrid.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.seedRatioGrid.setContentsMargins(0, 0, 0, 0)
        self.seedRatios.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_4 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(11, 381, 381, 51))
        self.tilingMethodButtons = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.tilingMethodButtons.setObjectName(u"tilingMethodButtons")
        self.tilingMethodButtons.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.horizontalLayoutWidget_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setTitle(u"")
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(0, 0, 381, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fillOctave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillOctave.setObjectName(u"fillOctave")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fillOctave.sizePolicy().hasHeightForWidth())
        self.fillOctave.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.fillOctave)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label = QLabel(self.horizontalLayoutWidget_7)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.fillTritave = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillTritave.setObjectName(u"fillTritave")
        sizePolicy1.setHeightForWidth(self.fillTritave.sizePolicy().hasHeightForWidth())
        self.fillTritave.setSizePolicy(sizePolicy1)

        self.horizontalLayout_12.addWidget(self.fillTritave)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.horizontalLayoutWidget_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.fillExpand = QRadioButton(self.horizontalLayoutWidget_7)
        self.fillExpand.setObjectName(u"fillExpand")
        sizePolicy1.setHeightForWidth(self.fillExpand.sizePolicy().hasHeightForWidth())
        self.fillExpand.setSizePolicy(sizePolicy1)

        self.horizontalLayout_13.addWidget(self.fillExpand)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.label_4 = QLabel(self.horizontalLayoutWidget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)


        self.tilingMethodButtons.addWidget(self.groupBox)

        self.horizontalLayoutWidget_5 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(11, 461, 381, 131))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cvSlider = QSlider(self.horizontalLayoutWidget_5)
        self.cvSlider.setObjectName(u"cvSlider")
        self.cvSlider.setMaximum(15)
        self.cvSlider.setValue(8)
        self.cvSlider.setSliderPosition(8)
        self.cvSlider.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.cvSlider)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.previewControls.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.knob = QDial(self.horizontalLayoutWidget_5)
        self.knob.setObjectName(u"knob")
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)

        self.verticalLayout_6.addWidget(self.knob)

        self.label_5 = QLabel(self.horizontalLayoutWidget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.previewControls.addLayout(self.verticalLayout_6)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)

        self.previewSelect = QComboBox(self.horizontalLayoutWidget_5)
        self.previewSelect.setObjectName(u"previewSelect")

        self.previewLayout.addWidget(self.previewSelect)


        self.previewControls.addLayout(self.previewLayout)

        self.horizontalLayoutWidget_6 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(11, 191, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addSeedRatio = QPushButton(self.horizontalLayoutWidget_6)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.seedRatioEditor.addWidget(self.addSeedRatio)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.numerator = QSpinBox(self.horizontalLayoutWidget_6)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimumSize(QSize(103, 26))
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.numerator)

        self.denominator = QSpinBox(self.horizontalLayoutWidget_6)
        self.denominator.setObjectName(u"denominator")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.denominator.sizePolicy().hasHeightForWidth())
        self.denominator.setSizePolicy(sizePolicy2)
        self.denominator.setMinimumSize(QSize(103, 26))
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.denominator)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(sync3ScaleEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(11, 71, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy3)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy3.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy3)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy3.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy3)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy3.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy3)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy3.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy3)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy3.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy3)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy3.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy3)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy3.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy3)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 251, 381, 41))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.addFromScala = QPushButton(self.horizontalLayoutWidget_3)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)

        self.horizontalLayoutWidget_8 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 440, 381, 21))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_2)

        self.horizontalLayoutWidget_9 = QWidget(sync3ScaleEditor)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 170, 381, 21))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_8 = QLabel(sync3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.fillOctave.setText("")
        self.label.setText(QCoreApplication.translate("sync3ScaleEditor", u"Octave", None))
        self.fillTritave.setText("")
        self.label_3.setText(QCoreApplication.translate("sync3ScaleEditor", u"Tritave", None))
        self.fillExpand.setText("")
        self.label_4.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill", None))
        self.label_6.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.label_5.setText(QCoreApplication.translate("sync3ScaleEditor", u"Knob Position", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("sync3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("sync3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("sync3ScaleEditor", u"3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("sync3ScaleEditor", u"4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("sync3ScaleEditor", u"5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("sync3ScaleEditor", u"6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("sync3ScaleEditor", u"7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("sync3ScaleEditor", u"8", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set", None))
    # retranslateUi

