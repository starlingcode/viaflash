# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
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
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpinBox, QVBoxLayout, QWidget)

from resourcesetbuttons import (Slot1Button, Slot2Button, Slot3Button, Slot4Button)

class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(600, 700)
        gateseqPatternEditor.setMinimumSize(QSize(600, 700))
        gateseqPatternEditor.setMaximumSize(QSize(600, 700))
        self.layoutWidget = QWidget(gateseqPatternEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 10, 581, 681))
        self.verticalLayout_9 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.resourceSetSaveLoad = QHBoxLayout()
        self.resourceSetSaveLoad.setObjectName(u"resourceSetSaveLoad")
        self.editPatternSetLabel = QLabel(self.layoutWidget)
        self.editPatternSetLabel.setObjectName(u"editPatternSetLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editPatternSetLabel.sizePolicy().hasHeightForWidth())
        self.editPatternSetLabel.setSizePolicy(sizePolicy)
        self.editPatternSetLabel.setAlignment(Qt.AlignCenter)

        self.resourceSetSaveLoad.addWidget(self.editPatternSetLabel)

        self.selectResourceSet = QComboBox(self.layoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.resourceSetSaveLoad.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.layoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.resourceSetSaveLoad.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.layoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.resourceSetSaveLoad.addWidget(self.saveForRack)


        self.verticalLayout_9.addLayout(self.resourceSetSaveLoad)

        self.setDescription = QLabel(self.layoutWidget)
        self.setDescription.setObjectName(u"setDescription")
        font = QFont()
        font.setPointSize(11)
        self.setDescription.setFont(font)
        self.setDescription.setAlignment(Qt.AlignCenter)
        self.setDescription.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.setDescription)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.editPatternLabel_2 = QLabel(self.layoutWidget)
        self.editPatternLabel_2.setObjectName(u"editPatternLabel_2")
        self.editPatternLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.editPatternLabel_2)

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(30, 0))
        self.label.setMaximumSize(QSize(40, 16777215))

        self.slotGroup1.addWidget(self.label)

        self.slot1 = Slot1Button(self.layoutWidget)
        self.buttonGroup = QButtonGroup(gateseqPatternEditor)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.slot1)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setMinimumSize(QSize(50, 50))
        self.slot1.setMaximumSize(QSize(50, 50))
        self.slot1.setCheckable(True)

        self.slotGroup1.addWidget(self.slot1)

        self.slot2 = Slot2Button(self.layoutWidget)
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

        self.slot3 = Slot3Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot3)
        self.slot3.setObjectName(u"slot3")
        sizePolicy2.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy2)
        self.slot3.setMinimumSize(QSize(50, 50))
        self.slot3.setMaximumSize(QSize(50, 50))
        self.slot3.setCheckable(True)

        self.slotGroup1.addWidget(self.slot3)

        self.slot4 = Slot4Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot4)
        self.slot4.setObjectName(u"slot4")
        sizePolicy2.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy2)
        self.slot4.setMinimumSize(QSize(50, 50))
        self.slot4.setMaximumSize(QSize(50, 50))
        self.slot4.setCheckable(True)

        self.slotGroup1.addWidget(self.slot4)

        self.label_20 = QLabel(self.layoutWidget)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setMinimumSize(QSize(35, 0))
        self.label_20.setMaximumSize(QSize(40, 16777215))

        self.slotGroup1.addWidget(self.label_20)

        self.slot5 = Slot1Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot5)
        self.slot5.setObjectName(u"slot5")
        sizePolicy2.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy2)
        self.slot5.setMinimumSize(QSize(50, 50))
        self.slot5.setMaximumSize(QSize(50, 50))
        self.slot5.setCheckable(True)

        self.slotGroup1.addWidget(self.slot5)

        self.slot6 = Slot2Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot6)
        self.slot6.setObjectName(u"slot6")
        sizePolicy2.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy2)
        self.slot6.setMinimumSize(QSize(50, 50))
        self.slot6.setMaximumSize(QSize(50, 50))
        self.slot6.setCheckable(True)

        self.slotGroup1.addWidget(self.slot6)

        self.slot7 = Slot3Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot7)
        self.slot7.setObjectName(u"slot7")
        sizePolicy2.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy2)
        self.slot7.setMinimumSize(QSize(50, 50))
        self.slot7.setMaximumSize(QSize(50, 50))
        self.slot7.setCheckable(True)

        self.slotGroup1.addWidget(self.slot7)

        self.slot8 = Slot4Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot8)
        self.slot8.setObjectName(u"slot8")
        sizePolicy2.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy2)
        self.slot8.setMinimumSize(QSize(50, 50))
        self.slot8.setMaximumSize(QSize(50, 50))
        self.slot8.setCheckable(True)

        self.slotGroup1.addWidget(self.slot8)


        self.verticalLayout_9.addLayout(self.slotGroup1)

        self.resourceSaveLoad = QHBoxLayout()
        self.resourceSaveLoad.setObjectName(u"resourceSaveLoad")
        self.selectResource = QComboBox(self.layoutWidget)
        self.selectResource.setObjectName(u"selectResource")

        self.resourceSaveLoad.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.layoutWidget)
        self.saveResource.setObjectName(u"saveResource")

        self.resourceSaveLoad.addWidget(self.saveResource)


        self.verticalLayout_9.addLayout(self.resourceSaveLoad)

        self.editPatternLabel = QLabel(self.layoutWidget)
        self.editPatternLabel.setObjectName(u"editPatternLabel")
        self.editPatternLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.editPatternLabel)

        self.addEuclideanControls = QHBoxLayout()
        self.addEuclideanControls.setObjectName(u"addEuclideanControls")
        self.addEuclidean = QPushButton(self.layoutWidget)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.addEuclideanControls.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.layoutWidget)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(71, 26))
        self.steps.setMinimum(0)
        self.steps.setMaximum(0)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.layoutWidget)
        self.length.setObjectName(u"length")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy3)
        self.length.setMinimumSize(QSize(79, 26))
        self.length.setMinimum(1)
        self.length.setMaximum(64)

        self.verticalLayout_2.addWidget(self.length)


        self.addEuclideanControls.addLayout(self.verticalLayout_2)

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


        self.addEuclideanControls.addLayout(self.verticalLayout_8)


        self.verticalLayout_9.addLayout(self.addEuclideanControls)

        self.addSequenceButtons = QHBoxLayout()
        self.addSequenceButtons.setObjectName(u"addSequenceButtons")
        self.addText = QPushButton(self.layoutWidget)
        self.addText.setObjectName(u"addText")

        self.addSequenceButtons.addWidget(self.addText)

        self.padToFill = QPushButton(self.layoutWidget)
        self.padToFill.setObjectName(u"padToFill")

        self.addSequenceButtons.addWidget(self.padToFill)

        self.clearSequences = QPushButton(self.layoutWidget)
        self.clearSequences.setObjectName(u"clearSequences")

        self.addSequenceButtons.addWidget(self.clearSequences)


        self.verticalLayout_9.addLayout(self.addSequenceButtons)

        self.sequenceGrid = QGridLayout()
        self.sequenceGrid.setObjectName(u"sequenceGrid")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.layoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.sequenceGrid.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2 = QPushButton(self.layoutWidget)
        self.sequence2.setObjectName(u"sequence2")

        self.verticalLayout_4.addWidget(self.sequence2)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.sequenceGrid.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.layoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.sequenceGrid.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.layoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.sequenceGrid.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.layoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.sequenceGrid.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.layoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.sequenceGrid.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.layoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.sequenceGrid.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.layoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.sequenceGrid.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.layoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.sequenceGrid.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.layoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.layoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.sequenceGrid.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.layoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.sequenceGrid.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.layoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.sequenceGrid.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.layoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.sequenceGrid.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.layoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.sequenceGrid.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.layoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.sequenceGrid.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.layoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.layoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.sequenceGrid.addLayout(self.verticalLayout_3, 3, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.sequenceGrid)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_9.addWidget(self.buttonBox)


        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"GATESEQ Pattern Editor", None))
        self.editPatternSetLabel.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set:", None))
        self.saveResourceSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for VCV Rack", None))
        self.setDescription.setText(QCoreApplication.translate("gateseqPatternEditor", u"TextLabel", None))
        self.editPatternLabel_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Select pattern for editing:", None))
        self.label.setText(QCoreApplication.translate("gateseqPatternEditor", u"Seq I:", None))
        self.slot1.setText("")
        self.slot2.setText("")
        self.slot3.setText("")
        self.slot4.setText("")
        self.label_20.setText(QCoreApplication.translate("gateseqPatternEditor", u"Seq II:", None))
        self.slot5.setText("")
        self.slot6.setText("")
        self.slot7.setText("")
        self.slot8.setText("")
        self.saveResource.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.editPatternLabel.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as Text", None))
        self.padToFill.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
    # retranslateUi

