# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'osc3_scale_editor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

class Ui_osc3ScaleEditor(object):
    def setupUi(self, osc3ScaleEditor):
        if not osc3ScaleEditor.objectName():
            osc3ScaleEditor.setObjectName(u"osc3ScaleEditor")
        osc3ScaleEditor.resize(402, 690)
        self.buttonBox = QDialogButtonBox(osc3ScaleEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(31, 650, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(osc3ScaleEditor)
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

        self.horizontalLayoutWidget_2 = QWidget(osc3ScaleEditor)
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

        self.groupBox_2 = QGroupBox(osc3ScaleEditor)
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
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.label_8 = QLabel(osc3ScaleEditor)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 10, 379, 19))
        self.label_8.setAlignment(Qt.AlignCenter)
        self.horizontalLayoutWidget_6 = QWidget(osc3ScaleEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 279, 381, 62))
        self.addChordControls = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.addChordControls.setObjectName(u"addChordControls")
        self.addChordControls.setContentsMargins(0, 0, 0, 0)
        self.addChord = QPushButton(self.horizontalLayoutWidget_6)
        self.addChord.setObjectName(u"addChord")

        self.addChordControls.addWidget(self.addChord)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.osc2Pitch = QSpinBox(self.horizontalLayoutWidget_6)
        self.osc2Pitch.setObjectName(u"osc2Pitch")
        self.osc2Pitch.setMinimumSize(QSize(71, 26))
        self.osc2Pitch.setMinimum(0)
        self.osc2Pitch.setMaximum(0)

        self.verticalLayout_2.addWidget(self.osc2Pitch)

        self.osc3Pitch = QSpinBox(self.horizontalLayoutWidget_6)
        self.osc3Pitch.setObjectName(u"osc3Pitch")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.osc3Pitch.sizePolicy().hasHeightForWidth())
        self.osc3Pitch.setSizePolicy(sizePolicy1)
        self.osc3Pitch.setMinimumSize(QSize(79, 26))
        self.osc3Pitch.setMinimum(1)
        self.osc3Pitch.setMaximum(64)

        self.verticalLayout_2.addWidget(self.osc3Pitch)


        self.addChordControls.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.addChordControls.addLayout(self.verticalLayout_8)

        self.gridLayoutWidget = QWidget(osc3ScaleEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 393, 381, 241))
        self.sequenceGrid_2 = QGridLayout(self.gridLayoutWidget)
        self.sequenceGrid_2.setObjectName(u"sequenceGrid_2")
        self.sequenceGrid_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.chord1 = QPushButton(self.gridLayoutWidget)
        self.chord1.setObjectName(u"chord1")

        self.verticalLayout_9.addWidget(self.chord1)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_21)


        self.sequenceGrid_2.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.chord2 = QPushButton(self.gridLayoutWidget)
        self.chord2.setObjectName(u"chord2")

        self.verticalLayout_20.addWidget(self.chord2)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_22)


        self.sequenceGrid_2.addLayout(self.verticalLayout_20, 0, 1, 1, 1)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.chord3 = QPushButton(self.gridLayoutWidget)
        self.chord3.setObjectName(u"chord3")

        self.verticalLayout_21.addWidget(self.chord3)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_23)


        self.sequenceGrid_2.addLayout(self.verticalLayout_21, 0, 2, 1, 1)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.chord4 = QPushButton(self.gridLayoutWidget)
        self.chord4.setObjectName(u"chord4")

        self.verticalLayout_22.addWidget(self.chord4)

        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_24)


        self.sequenceGrid_2.addLayout(self.verticalLayout_22, 0, 3, 1, 1)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.chord5 = QPushButton(self.gridLayoutWidget)
        self.chord5.setObjectName(u"chord5")

        self.verticalLayout_23.addWidget(self.chord5)

        self.label_25 = QLabel(self.gridLayoutWidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_25)


        self.sequenceGrid_2.addLayout(self.verticalLayout_23, 1, 0, 1, 1)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.chord6 = QPushButton(self.gridLayoutWidget)
        self.chord6.setObjectName(u"chord6")

        self.verticalLayout_24.addWidget(self.chord6)

        self.label_26 = QLabel(self.gridLayoutWidget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_26)


        self.sequenceGrid_2.addLayout(self.verticalLayout_24, 1, 1, 1, 1)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.chord7 = QPushButton(self.gridLayoutWidget)
        self.chord7.setObjectName(u"chord7")

        self.verticalLayout_25.addWidget(self.chord7)

        self.label_27 = QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_27)


        self.sequenceGrid_2.addLayout(self.verticalLayout_25, 1, 2, 1, 1)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.chord8 = QPushButton(self.gridLayoutWidget)
        self.chord8.setObjectName(u"chord8")

        self.verticalLayout_26.addWidget(self.chord8)

        self.label_28 = QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_28)


        self.sequenceGrid_2.addLayout(self.verticalLayout_26, 1, 3, 1, 1)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.chord9 = QPushButton(self.gridLayoutWidget)
        self.chord9.setObjectName(u"chord9")

        self.verticalLayout_27.addWidget(self.chord9)

        self.label_29 = QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_29)


        self.sequenceGrid_2.addLayout(self.verticalLayout_27, 2, 0, 1, 1)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.chord10 = QPushButton(self.gridLayoutWidget)
        self.chord10.setObjectName(u"chord10")

        self.verticalLayout_28.addWidget(self.chord10)

        self.label_30 = QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_30)


        self.sequenceGrid_2.addLayout(self.verticalLayout_28, 2, 1, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.chord11 = QPushButton(self.gridLayoutWidget)
        self.chord11.setObjectName(u"chord11")

        self.verticalLayout_29.addWidget(self.chord11)

        self.label_31 = QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_31)


        self.sequenceGrid_2.addLayout(self.verticalLayout_29, 2, 2, 1, 1)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.chord12 = QPushButton(self.gridLayoutWidget)
        self.chord12.setObjectName(u"chord12")

        self.verticalLayout_30.addWidget(self.chord12)

        self.label_32 = QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_32)


        self.sequenceGrid_2.addLayout(self.verticalLayout_30, 2, 3, 1, 1)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.chord16 = QPushButton(self.gridLayoutWidget)
        self.chord16.setObjectName(u"chord16")

        self.verticalLayout_31.addWidget(self.chord16)

        self.label_33 = QLabel(self.gridLayoutWidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_33)


        self.sequenceGrid_2.addLayout(self.verticalLayout_31, 3, 3, 1, 1)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.chord15 = QPushButton(self.gridLayoutWidget)
        self.chord15.setObjectName(u"chord15")

        self.verticalLayout_32.addWidget(self.chord15)

        self.label_34 = QLabel(self.gridLayoutWidget)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_34)


        self.sequenceGrid_2.addLayout(self.verticalLayout_32, 3, 2, 1, 1)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.chord14 = QPushButton(self.gridLayoutWidget)
        self.chord14.setObjectName(u"chord14")

        self.verticalLayout_33.addWidget(self.chord14)

        self.label_35 = QLabel(self.gridLayoutWidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_35)


        self.sequenceGrid_2.addLayout(self.verticalLayout_33, 3, 1, 1, 1)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.chord13 = QPushButton(self.gridLayoutWidget)
        self.chord13.setObjectName(u"chord13")

        self.verticalLayout_34.addWidget(self.chord13)

        self.label_36 = QLabel(self.gridLayoutWidget)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.label_36)


        self.sequenceGrid_2.addLayout(self.verticalLayout_34, 3, 0, 1, 1)

        self.horizontalLayoutWidget_3 = QWidget(osc3ScaleEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 340, 381, 41))
        self.addSequenceButtons = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.addSequenceButtons.setObjectName(u"addSequenceButtons")
        self.addSequenceButtons.setContentsMargins(0, 0, 0, 0)
        self.padToFill = QPushButton(self.horizontalLayoutWidget_3)
        self.padToFill.setObjectName(u"padToFill")

        self.addSequenceButtons.addWidget(self.padToFill)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.addSequenceButtons.addWidget(self.clearSequences)

        self.editChordsLabel = QLabel(osc3ScaleEditor)
        self.editChordsLabel.setObjectName(u"editChordsLabel")
        self.editChordsLabel.setGeometry(QRect(10, 260, 379, 19))
        self.editChordsLabel.setAlignment(Qt.AlignCenter)
        self.editChordsLabel_2 = QLabel(osc3ScaleEditor)
        self.editChordsLabel_2.setObjectName(u"editChordsLabel_2")
        self.editChordsLabel_2.setGeometry(QRect(10, 170, 379, 19))
        self.editChordsLabel_2.setAlignment(Qt.AlignCenter)
        self.note1 = QRadioButton(osc3ScaleEditor)
        self.note1.setObjectName(u"note1")
        self.note1.setGeometry(QRect(40, 220, 16, 23))
        self.note3 = QRadioButton(osc3ScaleEditor)
        self.note3.setObjectName(u"note3")
        self.note3.setGeometry(QRect(90, 220, 16, 23))
        self.note5 = QRadioButton(osc3ScaleEditor)
        self.note5.setObjectName(u"note5")
        self.note5.setGeometry(QRect(140, 220, 16, 23))
        self.note6 = QRadioButton(osc3ScaleEditor)
        self.note6.setObjectName(u"note6")
        self.note6.setGeometry(QRect(190, 220, 16, 23))
        self.note8 = QRadioButton(osc3ScaleEditor)
        self.note8.setObjectName(u"note8")
        self.note8.setGeometry(QRect(240, 220, 16, 23))
        self.note10 = QRadioButton(osc3ScaleEditor)
        self.note10.setObjectName(u"note10")
        self.note10.setGeometry(QRect(290, 220, 16, 23))
        self.note12 = QRadioButton(osc3ScaleEditor)
        self.note12.setObjectName(u"note12")
        self.note12.setGeometry(QRect(340, 220, 16, 23))
        self.note2 = QRadioButton(osc3ScaleEditor)
        self.note2.setObjectName(u"note2")
        self.note2.setGeometry(QRect(60, 190, 16, 23))
        self.note4 = QRadioButton(osc3ScaleEditor)
        self.note4.setObjectName(u"note4")
        self.note4.setGeometry(QRect(110, 190, 16, 23))
        self.note7 = QRadioButton(osc3ScaleEditor)
        self.note7.setObjectName(u"note7")
        self.note7.setGeometry(QRect(210, 190, 16, 23))
        self.note9 = QRadioButton(osc3ScaleEditor)
        self.note9.setObjectName(u"note9")
        self.note9.setGeometry(QRect(260, 190, 16, 23))
        self.note11 = QRadioButton(osc3ScaleEditor)
        self.note11.setObjectName(u"note11")
        self.note11.setGeometry(QRect(310, 190, 16, 23))

        self.retranslateUi(osc3ScaleEditor)
        self.buttonBox.accepted.connect(osc3ScaleEditor.accept)
        self.buttonBox.rejected.connect(osc3ScaleEditor.reject)

        QMetaObject.connectSlotsByName(osc3ScaleEditor)
    # setupUi

    def retranslateUi(self, osc3ScaleEditor):
        osc3ScaleEditor.setWindowTitle(QCoreApplication.translate("osc3ScaleEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("osc3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("osc3ScaleEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("osc3ScaleEditor", u"Save Scale", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("osc3ScaleEditor", u"1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("osc3ScaleEditor", u"2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("osc3ScaleEditor", u"3", None))
        self.label_8.setText(QCoreApplication.translate("osc3ScaleEditor", u"Edit Scale Set", None))
        self.addChord.setText(QCoreApplication.translate("osc3ScaleEditor", u"Add Chord", None))
        self.label_7.setText(QCoreApplication.translate("osc3ScaleEditor", u"Oscillator 2 Pitch", None))
        self.label_2.setText(QCoreApplication.translate("osc3ScaleEditor", u"Oscilllator 3 Pitch", None))
        self.chord1.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_21.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 1", None))
        self.chord2.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_22.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 2", None))
        self.chord3.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_23.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 3", None))
        self.chord4.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_24.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 4", None))
        self.chord5.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_25.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 5", None))
        self.chord6.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_26.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 6", None))
        self.chord7.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_27.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 7", None))
        self.chord8.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_28.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 8", None))
        self.chord9.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_29.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 9", None))
        self.chord10.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_30.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 10", None))
        self.chord11.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_31.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 11", None))
        self.chord12.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_32.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 12", None))
        self.chord16.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_33.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 16", None))
        self.chord15.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_34.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 15", None))
        self.chord14.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_35.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 14", None))
        self.chord13.setText(QCoreApplication.translate("osc3ScaleEditor", u"PushButton", None))
        self.label_36.setText(QCoreApplication.translate("osc3ScaleEditor", u"Chord 13", None))
        self.padToFill.setText(QCoreApplication.translate("osc3ScaleEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("osc3ScaleEditor", u"Clear All", None))
        self.editChordsLabel.setText(QCoreApplication.translate("osc3ScaleEditor", u"Edit Chords", None))
        self.editChordsLabel_2.setText(QCoreApplication.translate("osc3ScaleEditor", u"Edit Scale", None))
        self.note1.setText("")
        self.note3.setText("")
        self.note5.setText("")
        self.note6.setText("")
        self.note8.setText("")
        self.note10.setText("")
        self.note12.setText("")
        self.note2.setText("")
        self.note4.setText("")
        self.note7.setText("")
        self.note9.setText("")
        self.note11.setText("")
    # retranslateUi

