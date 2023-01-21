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
    QDialog, QDialogButtonBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

from resourcesetbuttons import (Slot1Button, Slot2Button, Slot3Button, Slot4Button)

class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(900, 700)
        gateseqPatternEditor.setMinimumSize(QSize(0, 0))
        gateseqPatternEditor.setMaximumSize(QSize(10000, 10000))
        self.layoutWidget = QWidget(gateseqPatternEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(8, 10, 881, 681))
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

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)
        self.editPatternLabel_2 = QLabel(self.layoutWidget)
        self.editPatternLabel_2.setObjectName(u"editPatternLabel_2")
        self.editPatternLabel_2.setAlignment(Qt.AlignCenter)

        self.slotGroup1.addWidget(self.editPatternLabel_2)

        self.selectResource = QComboBox(self.layoutWidget)
        self.selectResource.setObjectName(u"selectResource")

        self.slotGroup1.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.layoutWidget)
        self.saveResource.setObjectName(u"saveResource")

        self.slotGroup1.addWidget(self.saveResource)

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

        self.resourceDescription = QLabel(self.layoutWidget)
        self.resourceDescription.setObjectName(u"resourceDescription")
        self.resourceDescription.setFont(font)
        self.resourceDescription.setAlignment(Qt.AlignCenter)
        self.resourceDescription.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.resourceDescription)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.editPatternLabel = QLabel(self.layoutWidget)
        self.editPatternLabel.setObjectName(u"editPatternLabel")
        self.editPatternLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.editPatternLabel)

        self.addEuclideanControls = QHBoxLayout()
        self.addEuclideanControls.setObjectName(u"addEuclideanControls")
        self.addEuclidean = QPushButton(self.layoutWidget)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.addEuclideanControls.addWidget(self.addEuclidean)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.addEuclideanControls.addWidget(self.label_7)

        self.steps = QSpinBox(self.layoutWidget)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(71, 26))
        self.steps.setMinimum(0)
        self.steps.setMaximum(0)

        self.addEuclideanControls.addWidget(self.steps)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.addEuclideanControls.addWidget(self.label_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.addEuclideanControls.addItem(self.horizontalSpacer)

        self.clearSequences = QPushButton(self.layoutWidget)
        self.clearSequences.setObjectName(u"clearSequences")

        self.addEuclideanControls.addWidget(self.clearSequences)


        self.verticalLayout_9.addLayout(self.addEuclideanControls)

        self.sequenceEditLayout = QVBoxLayout()
        self.sequenceEditLayout.setObjectName(u"sequenceEditLayout")

        self.verticalLayout_9.addLayout(self.sequenceEditLayout)

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
        self.editPatternLabel_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Select pattern:", None))
        self.saveResource.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
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
        self.resourceDescription.setText(QCoreApplication.translate("gateseqPatternEditor", u"TextLabel", None))
        self.editPatternLabel.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps:", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length:", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
    # retranslateUi

