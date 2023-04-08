# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'osc3_quantization_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

from resourcesetbuttons import (Slot2Button, Slot3Button, Slot4Button)

class Ui_osc3QuantizationEditor(object):
    def setupUi(self, osc3QuantizationEditor):
        if not osc3QuantizationEditor.objectName():
            osc3QuantizationEditor.setObjectName(u"osc3QuantizationEditor")
        osc3QuantizationEditor.resize(531, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(osc3QuantizationEditor.sizePolicy().hasHeightForWidth())
        osc3QuantizationEditor.setSizePolicy(sizePolicy)
        osc3QuantizationEditor.setMinimumSize(QSize(0, 0))
        osc3QuantizationEditor.setMaximumSize(QSize(1000000, 1000000))
        self.layoutWidget = QWidget(osc3QuantizationEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 515, 751))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scalesSetButtons = QHBoxLayout()
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.scalesSetButtons.addWidget(self.label_8)

        self.selectResourceSet = QComboBox(self.layoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.scalesSetButtons.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.layoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.scalesSetButtons.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.layoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)


        self.verticalLayout_3.addLayout(self.scalesSetButtons)

        self.setDescription = QLabel(self.layoutWidget)
        self.setDescription.setObjectName(u"setDescription")
        font = QFont()
        font.setPointSize(11)
        self.setDescription.setFont(font)
        self.setDescription.setAlignment(Qt.AlignCenter)
        self.setDescription.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.setDescription)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.saveLoadScale = QHBoxLayout()
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.editChordsLabel_3 = QLabel(self.layoutWidget)
        self.editChordsLabel_3.setObjectName(u"editChordsLabel_3")
        self.editChordsLabel_3.setAlignment(Qt.AlignCenter)

        self.saveLoadScale.addWidget(self.editChordsLabel_3)

        self.selectResource = QComboBox(self.layoutWidget)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.layoutWidget)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)


        self.verticalLayout_3.addLayout(self.saveLoadScale)

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot1 = Slot2Button(self.layoutWidget)
        self.buttonGroup = QButtonGroup(osc3QuantizationEditor)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.slot1)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy)
        self.slot1.setMinimumSize(QSize(50, 50))
        self.slot1.setMaximumSize(QSize(50, 50))
        self.slot1.setCheckable(True)

        self.slotGroup1.addWidget(self.slot1)

        self.slot2 = Slot3Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot2)
        self.slot2.setObjectName(u"slot2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy2)
        self.slot2.setMinimumSize(QSize(50, 50))
        self.slot2.setMaximumSize(QSize(50, 50))
        self.slot2.setCheckable(True)

        self.slotGroup1.addWidget(self.slot2)

        self.slot3 = Slot4Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot3)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setMinimumSize(QSize(50, 50))
        self.slot3.setMaximumSize(QSize(50, 50))
        self.slot3.setCheckable(True)

        self.slotGroup1.addWidget(self.slot3)


        self.verticalLayout_3.addLayout(self.slotGroup1)

        self.resourceDescription = QLabel(self.layoutWidget)
        self.resourceDescription.setObjectName(u"resourceDescription")
        self.resourceDescription.setFont(font)
        self.resourceDescription.setAlignment(Qt.AlignCenter)
        self.resourceDescription.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.resourceDescription)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.editChordsLabel_2 = QLabel(self.layoutWidget)
        self.editChordsLabel_2.setObjectName(u"editChordsLabel_2")
        self.editChordsLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.editChordsLabel_2)

        self.editChordsLabel_4 = QLabel(self.layoutWidget)
        self.editChordsLabel_4.setObjectName(u"editChordsLabel_4")
        self.editChordsLabel_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.editChordsLabel_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.note2 = QPushButton(self.layoutWidget)
        self.note2.setObjectName(u"note2")
        sizePolicy2.setHeightForWidth(self.note2.sizePolicy().hasHeightForWidth())
        self.note2.setSizePolicy(sizePolicy2)
        self.note2.setMinimumSize(QSize(25, 0))
        self.note2.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.note2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_9)

        self.note4 = QPushButton(self.layoutWidget)
        self.note4.setObjectName(u"note4")
        sizePolicy2.setHeightForWidth(self.note4.sizePolicy().hasHeightForWidth())
        self.note4.setSizePolicy(sizePolicy2)
        self.note4.setMinimumSize(QSize(25, 0))
        self.note4.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.note4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_10)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_15)

        self.note7 = QPushButton(self.layoutWidget)
        self.note7.setObjectName(u"note7")
        sizePolicy2.setHeightForWidth(self.note7.sizePolicy().hasHeightForWidth())
        self.note7.setSizePolicy(sizePolicy2)
        self.note7.setMinimumSize(QSize(25, 0))
        self.note7.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.note7)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.note9 = QPushButton(self.layoutWidget)
        self.note9.setObjectName(u"note9")
        sizePolicy2.setHeightForWidth(self.note9.sizePolicy().hasHeightForWidth())
        self.note9.setSizePolicy(sizePolicy2)
        self.note9.setMinimumSize(QSize(25, 0))
        self.note9.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.note9)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)

        self.note11 = QPushButton(self.layoutWidget)
        self.note11.setObjectName(u"note11")
        sizePolicy2.setHeightForWidth(self.note11.sizePolicy().hasHeightForWidth())
        self.note11.setSizePolicy(sizePolicy2)
        self.note11.setMinimumSize(QSize(25, 0))
        self.note11.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.note11)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.note1 = QPushButton(self.layoutWidget)
        self.note1.setObjectName(u"note1")
        sizePolicy2.setHeightForWidth(self.note1.sizePolicy().hasHeightForWidth())
        self.note1.setSizePolicy(sizePolicy2)
        self.note1.setMinimumSize(QSize(25, 0))
        self.note1.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.note1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.note3 = QPushButton(self.layoutWidget)
        self.note3.setObjectName(u"note3")
        sizePolicy2.setHeightForWidth(self.note3.sizePolicy().hasHeightForWidth())
        self.note3.setSizePolicy(sizePolicy2)
        self.note3.setMinimumSize(QSize(25, 0))
        self.note3.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.note3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.note5 = QPushButton(self.layoutWidget)
        self.note5.setObjectName(u"note5")
        sizePolicy2.setHeightForWidth(self.note5.sizePolicy().hasHeightForWidth())
        self.note5.setSizePolicy(sizePolicy2)
        self.note5.setMinimumSize(QSize(25, 0))
        self.note5.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.note5)

        self.note6 = QPushButton(self.layoutWidget)
        self.note6.setObjectName(u"note6")
        sizePolicy2.setHeightForWidth(self.note6.sizePolicy().hasHeightForWidth())
        self.note6.setSizePolicy(sizePolicy2)
        self.note6.setMinimumSize(QSize(25, 0))
        self.note6.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.note6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.note8 = QPushButton(self.layoutWidget)
        self.note8.setObjectName(u"note8")
        sizePolicy2.setHeightForWidth(self.note8.sizePolicy().hasHeightForWidth())
        self.note8.setSizePolicy(sizePolicy2)
        self.note8.setMinimumSize(QSize(25, 0))
        self.note8.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.note8)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.note10 = QPushButton(self.layoutWidget)
        self.note10.setObjectName(u"note10")
        sizePolicy2.setHeightForWidth(self.note10.sizePolicy().hasHeightForWidth())
        self.note10.setSizePolicy(sizePolicy2)
        self.note10.setMinimumSize(QSize(25, 0))
        self.note10.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.note10)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.note12 = QPushButton(self.layoutWidget)
        self.note12.setObjectName(u"note12")
        sizePolicy2.setHeightForWidth(self.note12.sizePolicy().hasHeightForWidth())
        self.note12.setSizePolicy(sizePolicy2)
        self.note12.setMinimumSize(QSize(25, 0))
        self.note12.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.note12)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.editChordsLabel = QLabel(self.layoutWidget)
        self.editChordsLabel.setObjectName(u"editChordsLabel")
        self.editChordsLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.editChordsLabel)

        self.addChordControls = QHBoxLayout()
        self.addChordControls.setObjectName(u"addChordControls")
        self.addChord = QPushButton(self.layoutWidget)
        self.addChord.setObjectName(u"addChord")

        self.addChordControls.addWidget(self.addChord)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.osc2Pitch = QSpinBox(self.layoutWidget)
        self.osc2Pitch.setObjectName(u"osc2Pitch")
        self.osc2Pitch.setMinimumSize(QSize(71, 26))
        self.osc2Pitch.setMinimum(0)
        self.osc2Pitch.setMaximum(0)

        self.verticalLayout_2.addWidget(self.osc2Pitch)

        self.osc3Pitch = QSpinBox(self.layoutWidget)
        self.osc3Pitch.setObjectName(u"osc3Pitch")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.osc3Pitch.sizePolicy().hasHeightForWidth())
        self.osc3Pitch.setSizePolicy(sizePolicy3)
        self.osc3Pitch.setMinimumSize(QSize(79, 26))
        self.osc3Pitch.setMinimum(1)
        self.osc3Pitch.setMaximum(64)

        self.verticalLayout_2.addWidget(self.osc3Pitch)


        self.addChordControls.addLayout(self.verticalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.osc2Note = QLabel(self.layoutWidget)
        self.osc2Note.setObjectName(u"osc2Note")
        self.osc2Note.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.osc2Note)

        self.osc3Note = QLabel(self.layoutWidget)
        self.osc3Note.setObjectName(u"osc3Note")
        self.osc3Note.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.osc3Note)


        self.addChordControls.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.addChordControls.addLayout(self.verticalLayout_8)


        self.verticalLayout_3.addLayout(self.addChordControls)

        self.seedEditor = QVBoxLayout()
        self.seedEditor.setObjectName(u"seedEditor")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.clearAll = QPushButton(self.layoutWidget)
        self.clearAll.setObjectName(u"clearAll")

        self.horizontalLayout.addWidget(self.clearAll)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.seedEditor.addLayout(self.horizontalLayout)

        self.chordScrollArea = QScrollArea(self.layoutWidget)
        self.chordScrollArea.setObjectName(u"chordScrollArea")
        self.chordScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 499, 177))
        self.chordScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.seedEditor.addWidget(self.chordScrollArea)


        self.verticalLayout_3.addLayout(self.seedEditor)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(osc3QuantizationEditor)
        self.buttonBox.accepted.connect(osc3QuantizationEditor.accept)
        self.buttonBox.rejected.connect(osc3QuantizationEditor.reject)

        QMetaObject.connectSlotsByName(osc3QuantizationEditor)
    # setupUi

    def retranslateUi(self, osc3QuantizationEditor):
        osc3QuantizationEditor.setWindowTitle(QCoreApplication.translate("osc3QuantizationEditor", u"OSC3 Quantization Editor", None))
        self.label_8.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Edit Quantization Set:", None))
        self.saveResourceSet.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Save Set", None))
        self.saveForRack.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Save for VCV Rack", None))
        self.setDescription.setText(QCoreApplication.translate("osc3QuantizationEditor", u"TextLabel", None))
        self.editChordsLabel_3.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Select quantization:", None))
        self.saveResource.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Save Quantization", None))
        self.slot1.setText("")
        self.slot2.setText("")
        self.slot3.setText("")
        self.resourceDescription.setText(QCoreApplication.translate("osc3QuantizationEditor", u"TextLabel", None))
        self.editChordsLabel_2.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Edit Quantization", None))
        self.editChordsLabel_4.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Select pitches in scale when root is C:", None))
        self.note2.setText(QCoreApplication.translate("osc3QuantizationEditor", u"C#", None))
        self.note4.setText(QCoreApplication.translate("osc3QuantizationEditor", u"D#", None))
        self.note7.setText(QCoreApplication.translate("osc3QuantizationEditor", u"F#", None))
        self.note9.setText(QCoreApplication.translate("osc3QuantizationEditor", u"G#", None))
        self.note11.setText(QCoreApplication.translate("osc3QuantizationEditor", u"A#", None))
        self.note1.setText(QCoreApplication.translate("osc3QuantizationEditor", u"C", None))
        self.note3.setText(QCoreApplication.translate("osc3QuantizationEditor", u"D", None))
        self.note5.setText(QCoreApplication.translate("osc3QuantizationEditor", u"E", None))
        self.note6.setText(QCoreApplication.translate("osc3QuantizationEditor", u"F", None))
        self.note8.setText(QCoreApplication.translate("osc3QuantizationEditor", u"G", None))
        self.note10.setText(QCoreApplication.translate("osc3QuantizationEditor", u"A", None))
        self.note12.setText(QCoreApplication.translate("osc3QuantizationEditor", u"B", None))
        self.editChordsLabel.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Add and edit chords as offsets in scale:", None))
        self.addChord.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Add Chord", None))
        self.osc2Note.setText(QCoreApplication.translate("osc3QuantizationEditor", u"C", None))
        self.osc3Note.setText(QCoreApplication.translate("osc3QuantizationEditor", u"D", None))
        self.label_7.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Oscillator 2 Pitch", None))
        self.label_2.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Oscilllator 3 Pitch", None))
        self.clearAll.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Clear All", None))
        self.label_3.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Scale Degrees", None))
        self.label.setText(QCoreApplication.translate("osc3QuantizationEditor", u"Notes (With C as Root)", None))
    # retranslateUi

