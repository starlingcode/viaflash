# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_scale_editor.ui'
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
    QDial, QDialog, QDialogButtonBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

from resourcesetbuttons import (Slot1Button, Slot2Button, Slot3Button, Slot4Button,
    Slot5Button, Slot6Button, Slot7Button, Slot8Button)

class Ui_sync3ScaleEditor(object):
    def setupUi(self, sync3ScaleEditor):
        if not sync3ScaleEditor.objectName():
            sync3ScaleEditor.setObjectName(u"sync3ScaleEditor")
        sync3ScaleEditor.resize(700, 760)
        sync3ScaleEditor.setMinimumSize(QSize(700, 760))
        sync3ScaleEditor.setMaximumSize(QSize(700, 760))
        self.layoutWidget = QWidget(sync3ScaleEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 681, 741))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scalesSetButtons = QHBoxLayout()
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
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


        self.verticalLayout_8.addLayout(self.scalesSetButtons)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line)

        self.saveLoadScale = QHBoxLayout()
        self.saveLoadScale.setObjectName(u"saveLoadScale")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.saveLoadScale.addWidget(self.label_9)

        self.selectResource = QComboBox(self.layoutWidget)
        self.selectResource.setObjectName(u"selectResource")

        self.saveLoadScale.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.layoutWidget)
        self.saveResource.setObjectName(u"saveResource")

        self.saveLoadScale.addWidget(self.saveResource)


        self.verticalLayout_8.addLayout(self.saveLoadScale)

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot1 = Slot1Button(self.layoutWidget)
        self.buttonGroup = QButtonGroup(sync3ScaleEditor)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.slot1)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
        self.slot1.setMinimumSize(QSize(50, 50))
        self.slot1.setMaximumSize(QSize(30, 16777215))
        self.slot1.setCheckable(True)

        self.slotGroup1.addWidget(self.slot1)

        self.slot2 = Slot2Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot2)
        self.slot2.setObjectName(u"slot2")
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
        self.slot2.setMinimumSize(QSize(50, 50))
        self.slot2.setMaximumSize(QSize(30, 16777215))
        self.slot2.setCheckable(True)

        self.slotGroup1.addWidget(self.slot2)

        self.slot3 = Slot3Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot3)
        self.slot3.setObjectName(u"slot3")
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
        self.slot3.setMinimumSize(QSize(50, 50))
        self.slot3.setMaximumSize(QSize(30, 16777215))
        self.slot3.setCheckable(True)

        self.slotGroup1.addWidget(self.slot3)

        self.slot4 = Slot4Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot4)
        self.slot4.setObjectName(u"slot4")
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
        self.slot4.setMinimumSize(QSize(50, 50))
        self.slot4.setMaximumSize(QSize(30, 16777215))
        self.slot4.setCheckable(True)

        self.slotGroup1.addWidget(self.slot4)

        self.slot5 = Slot5Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot5)
        self.slot5.setObjectName(u"slot5")
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
        self.slot5.setMinimumSize(QSize(50, 50))
        self.slot5.setMaximumSize(QSize(50, 50))
        self.slot5.setCheckable(True)

        self.slotGroup1.addWidget(self.slot5)

        self.slot6 = Slot6Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot6)
        self.slot6.setObjectName(u"slot6")
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
        self.slot6.setMinimumSize(QSize(50, 50))
        self.slot6.setMaximumSize(QSize(30, 16777215))
        self.slot6.setCheckable(True)

        self.slotGroup1.addWidget(self.slot6)

        self.slot7 = Slot7Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot7)
        self.slot7.setObjectName(u"slot7")
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
        self.slot7.setMinimumSize(QSize(50, 50))
        self.slot7.setMaximumSize(QSize(30, 16777215))
        self.slot7.setCheckable(True)

        self.slotGroup1.addWidget(self.slot7)

        self.slot8 = Slot8Button(self.layoutWidget)
        self.buttonGroup.addButton(self.slot8)
        self.slot8.setObjectName(u"slot8")
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setMinimumSize(QSize(50, 50))
        self.slot8.setMaximumSize(QSize(30, 16777215))
        self.slot8.setCheckable(True)

        self.slotGroup1.addWidget(self.slot8)


        self.verticalLayout_8.addLayout(self.slotGroup1)

        self.scaleDescription = QLabel(self.layoutWidget)
        self.scaleDescription.setObjectName(u"scaleDescription")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scaleDescription.sizePolicy().hasHeightForWidth())
        self.scaleDescription.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(11)
        self.scaleDescription.setFont(font)
        self.scaleDescription.setAlignment(Qt.AlignCenter)
        self.scaleDescription.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.scaleDescription)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.scaleEditor = QHBoxLayout()
        self.scaleEditor.setObjectName(u"scaleEditor")
        self.seedEditor = QVBoxLayout()
        self.seedEditor.setObjectName(u"seedEditor")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.seedEditor.addWidget(self.label_7)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.addSeedRatio = QPushButton(self.layoutWidget)
        self.addSeedRatio.setObjectName(u"addSeedRatio")

        self.horizontalLayout_15.addWidget(self.addSeedRatio)

        self.addFromScala = QPushButton(self.layoutWidget)
        self.addFromScala.setObjectName(u"addFromScala")

        self.horizontalLayout_15.addWidget(self.addFromScala)

        self.clearSeedRatios = QPushButton(self.layoutWidget)
        self.clearSeedRatios.setObjectName(u"clearSeedRatios")

        self.horizontalLayout_15.addWidget(self.clearSeedRatios)


        self.seedEditor.addLayout(self.horizontalLayout_15)

        self.seedScrollArea = QScrollArea(self.layoutWidget)
        self.seedScrollArea.setObjectName(u"seedScrollArea")
        self.seedScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 317, 358))
        self.seedScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.seedEditor.addWidget(self.seedScrollArea)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.sorted = QPushButton(self.layoutWidget)
        self.buttonGroup_3 = QButtonGroup(sync3ScaleEditor)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.sorted)
        self.sorted.setObjectName(u"sorted")
        self.sorted.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.sorted)

        self.unsorted = QPushButton(self.layoutWidget)
        self.buttonGroup_3.addButton(self.unsorted)
        self.unsorted.setObjectName(u"unsorted")
        self.unsorted.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.unsorted)


        self.seedEditor.addLayout(self.horizontalLayout_3)

        self.sortedHelp = QLabel(self.layoutWidget)
        self.sortedHelp.setObjectName(u"sortedHelp")
        sizePolicy2.setHeightForWidth(self.sortedHelp.sizePolicy().hasHeightForWidth())
        self.sortedHelp.setSizePolicy(sizePolicy2)
        self.sortedHelp.setFont(font)
        self.sortedHelp.setAlignment(Qt.AlignCenter)
        self.sortedHelp.setWordWrap(True)

        self.seedEditor.addWidget(self.sortedHelp)


        self.scaleEditor.addLayout(self.seedEditor)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.scaleEditor.addWidget(self.line_2)

        self.tilingAndPreview = QVBoxLayout()
        self.tilingAndPreview.setObjectName(u"tilingAndPreview")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.tilingAndPreview.addWidget(self.label_2)

        self.previewLayout = QVBoxLayout()
        self.previewLayout.setObjectName(u"previewLayout")
        self.previewContainer = QHBoxLayout()
        self.previewContainer.setObjectName(u"previewContainer")

        self.previewLayout.addLayout(self.previewContainer)


        self.tilingAndPreview.addLayout(self.previewLayout)

        self.knobCV = QHBoxLayout()
        self.knobCV.setObjectName(u"knobCV")
        self.knobLayout = QVBoxLayout()
        self.knobLayout.setObjectName(u"knobLayout")
        self.knob = QDial(self.layoutWidget)
        self.knob.setObjectName(u"knob")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.knob.sizePolicy().hasHeightForWidth())
        self.knob.setSizePolicy(sizePolicy3)
        self.knob.setMaximum(16)
        self.knob.setPageStep(8)
        self.knob.setSliderPosition(8)

        self.knobLayout.addWidget(self.knob)


        self.knobCV.addLayout(self.knobLayout)

        self.cvSliderLayout = QVBoxLayout()
        self.cvSliderLayout.setObjectName(u"cvSliderLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.cvSliderLayout.addItem(self.verticalSpacer_2)

        self.cvSlider = QSlider(self.layoutWidget)
        self.cvSlider.setObjectName(u"cvSlider")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.cvSlider.sizePolicy().hasHeightForWidth())
        self.cvSlider.setSizePolicy(sizePolicy4)
        self.cvSlider.setMinimum(-50)
        self.cvSlider.setMaximum(50)
        self.cvSlider.setValue(0)
        self.cvSlider.setSliderPosition(0)
        self.cvSlider.setOrientation(Qt.Horizontal)

        self.cvSliderLayout.addWidget(self.cvSlider)

        self.cvLabel = QLabel(self.layoutWidget)
        self.cvLabel.setObjectName(u"cvLabel")
        sizePolicy3.setHeightForWidth(self.cvLabel.sizePolicy().hasHeightForWidth())
        self.cvLabel.setSizePolicy(sizePolicy3)
        self.cvLabel.setAlignment(Qt.AlignCenter)

        self.cvSliderLayout.addWidget(self.cvLabel)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.cvSliderLayout.addItem(self.verticalSpacer_3)


        self.knobCV.addLayout(self.cvSliderLayout)


        self.tilingAndPreview.addLayout(self.knobCV)

        self.fillButtonLayout = QHBoxLayout()
        self.fillButtonLayout.setObjectName(u"fillButtonLayout")
        self.fillOctave = QPushButton(self.layoutWidget)
        self.buttonGroup_2 = QButtonGroup(sync3ScaleEditor)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.fillOctave)
        self.fillOctave.setObjectName(u"fillOctave")
        self.fillOctave.setCheckable(True)

        self.fillButtonLayout.addWidget(self.fillOctave)

        self.fillTritave = QPushButton(self.layoutWidget)
        self.buttonGroup_2.addButton(self.fillTritave)
        self.fillTritave.setObjectName(u"fillTritave")
        self.fillTritave.setCheckable(True)

        self.fillButtonLayout.addWidget(self.fillTritave)

        self.fillExpand = QPushButton(self.layoutWidget)
        self.buttonGroup_2.addButton(self.fillExpand)
        self.fillExpand.setObjectName(u"fillExpand")
        self.fillExpand.setCheckable(True)

        self.fillButtonLayout.addWidget(self.fillExpand)


        self.tilingAndPreview.addLayout(self.fillButtonLayout)

        self.fillHelp = QLabel(self.layoutWidget)
        self.fillHelp.setObjectName(u"fillHelp")
        sizePolicy2.setHeightForWidth(self.fillHelp.sizePolicy().hasHeightForWidth())
        self.fillHelp.setSizePolicy(sizePolicy2)
        self.fillHelp.setFont(font)
        self.fillHelp.setAlignment(Qt.AlignCenter)
        self.fillHelp.setWordWrap(True)

        self.tilingAndPreview.addWidget(self.fillHelp)


        self.scaleEditor.addLayout(self.tilingAndPreview)


        self.verticalLayout_8.addLayout(self.scaleEditor)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_8.addWidget(self.buttonBox)


        self.retranslateUi(sync3ScaleEditor)
        self.buttonBox.rejected.connect(sync3ScaleEditor.reject)
        self.buttonBox.accepted.connect(sync3ScaleEditor.accept)

        QMetaObject.connectSlotsByName(sync3ScaleEditor)
    # setupUi

    def retranslateUi(self, sync3ScaleEditor):
        sync3ScaleEditor.setWindowTitle(QCoreApplication.translate("sync3ScaleEditor", u"SYNC3 Scale Set Editor", None))
        self.label_8.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale Set:", None))
        self.saveResourceSet.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale Set", None))
        self.saveForRack.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save for VCV Rack", None))
        self.label_9.setText(QCoreApplication.translate("sync3ScaleEditor", u"Select scale for editing:", None))
        self.saveResource.setText(QCoreApplication.translate("sync3ScaleEditor", u"Save Scale", None))
        self.slot1.setText("")
        self.slot2.setText("")
        self.slot3.setText("")
        self.slot4.setText("")
        self.slot5.setText("")
        self.slot6.setText("")
        self.slot7.setText("")
        self.slot8.setText("")
        self.scaleDescription.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill Labe", None))
        self.label_7.setText(QCoreApplication.translate("sync3ScaleEditor", u"Edit Scale", None))
        self.addSeedRatio.setText(QCoreApplication.translate("sync3ScaleEditor", u"Add Ratio", None))
        self.addFromScala.setText(QCoreApplication.translate("sync3ScaleEditor", u"Import From Scala", None))
        self.clearSeedRatios.setText(QCoreApplication.translate("sync3ScaleEditor", u"Clear", None))
        self.sorted.setText(QCoreApplication.translate("sync3ScaleEditor", u"Sorted", None))
        self.unsorted.setText(QCoreApplication.translate("sync3ScaleEditor", u"Unsorted", None))
        self.sortedHelp.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill Labe", None))
        self.label_2.setText(QCoreApplication.translate("sync3ScaleEditor", u"Preview", None))
        self.cvLabel.setText(QCoreApplication.translate("sync3ScaleEditor", u"CV: 0V", None))
        self.fillOctave.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill Octave", None))
        self.fillTritave.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill Tritave", None))
        self.fillExpand.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill Expand", None))
        self.fillHelp.setText(QCoreApplication.translate("sync3ScaleEditor", u"Fill Labe", None))
    # retranslateUi

