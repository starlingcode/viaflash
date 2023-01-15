# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wavetable_set_editor.ui'
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
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

from wavetable_viz_panel import WavetableVizPanel

class Ui_wavetableSetEditor(object):
    def setupUi(self, wavetableSetEditor):
        if not wavetableSetEditor.objectName():
            wavetableSetEditor.setObjectName(u"wavetableSetEditor")
        wavetableSetEditor.resize(600, 800)
        wavetableSetEditor.setMinimumSize(QSize(600, 800))
        wavetableSetEditor.setMaximumSize(QSize(600, 800))
        self.layoutWidget = QWidget(wavetableSetEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 581, 781))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.windowTitle = QLabel(self.layoutWidget)
        self.windowTitle.setObjectName(u"windowTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowTitle.sizePolicy().hasHeightForWidth())
        self.windowTitle.setSizePolicy(sizePolicy)
        self.windowTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.windowTitle)

        self.resourceSetSaveLoad = QHBoxLayout()
#ifndef Q_OS_MAC
        self.resourceSetSaveLoad.setSpacing(-1)
#endif
        self.resourceSetSaveLoad.setObjectName(u"resourceSetSaveLoad")
        self.selectResourceSet = QComboBox(self.layoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")
        sizePolicy.setHeightForWidth(self.selectResourceSet.sizePolicy().hasHeightForWidth())
        self.selectResourceSet.setSizePolicy(sizePolicy)

        self.resourceSetSaveLoad.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.layoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.saveResourceSet.sizePolicy().hasHeightForWidth())
        self.saveResourceSet.setSizePolicy(sizePolicy1)

        self.resourceSetSaveLoad.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.layoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")
        sizePolicy1.setHeightForWidth(self.saveForRack.sizePolicy().hasHeightForWidth())
        self.saveForRack.setSizePolicy(sizePolicy1)

        self.resourceSetSaveLoad.addWidget(self.saveForRack)


        self.verticalLayout.addLayout(self.resourceSetSaveLoad)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.windowTitle_2 = QLabel(self.layoutWidget)
        self.windowTitle_2.setObjectName(u"windowTitle_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.windowTitle_2.sizePolicy().hasHeightForWidth())
        self.windowTitle_2.setSizePolicy(sizePolicy2)
        self.windowTitle_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.windowTitle_2)

        self.tableMode = QComboBox(self.layoutWidget)
        self.tableMode.setObjectName(u"tableMode")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableMode.sizePolicy().hasHeightForWidth())
        self.tableMode.setSizePolicy(sizePolicy3)
        self.tableMode.setMinimumSize(QSize(200, 0))
        self.tableMode.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_2.addWidget(self.tableMode)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout.addLayout(self.slotGroup1)

        self.resourceSaveLoad = QHBoxLayout()
        self.resourceSaveLoad.setObjectName(u"resourceSaveLoad")
        self.tableName = QLabel(self.layoutWidget)
        self.tableName.setObjectName(u"tableName")
        sizePolicy.setHeightForWidth(self.tableName.sizePolicy().hasHeightForWidth())
        self.tableName.setSizePolicy(sizePolicy)
        self.tableName.setAlignment(Qt.AlignCenter)

        self.resourceSaveLoad.addWidget(self.tableName)

        self.openBrowser = QPushButton(self.layoutWidget)
        self.openBrowser.setObjectName(u"openBrowser")

        self.resourceSaveLoad.addWidget(self.openBrowser)


        self.verticalLayout.addLayout(self.resourceSaveLoad)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.tableViz = QVBoxLayout()
        self.tableViz.setObjectName(u"tableViz")
        self.topViz = QHBoxLayout()
        self.topViz.setObjectName(u"topViz")
        self.viz1 = WavetableVizPanel(self.layoutWidget)
        self.viz1.setObjectName(u"viz1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.viz1.sizePolicy().hasHeightForWidth())
        self.viz1.setSizePolicy(sizePolicy4)
        self.viz1.setMinimumSize(QSize(200, 200))

        self.topViz.addWidget(self.viz1)

        self.viz2 = WavetableVizPanel(self.layoutWidget)
        self.viz2.setObjectName(u"viz2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.viz2.sizePolicy().hasHeightForWidth())
        self.viz2.setSizePolicy(sizePolicy5)
        self.viz2.setMinimumSize(QSize(200, 0))

        self.topViz.addWidget(self.viz2)


        self.tableViz.addLayout(self.topViz)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)

        self.tableIdx = QSlider(self.layoutWidget)
        self.tableIdx.setObjectName(u"tableIdx")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tableIdx.sizePolicy().hasHeightForWidth())
        self.tableIdx.setSizePolicy(sizePolicy6)
        self.tableIdx.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.tableIdx)

        self.tableIdxLabel = QLabel(self.layoutWidget)
        self.tableIdxLabel.setObjectName(u"tableIdxLabel")
        sizePolicy.setHeightForWidth(self.tableIdxLabel.sizePolicy().hasHeightForWidth())
        self.tableIdxLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.tableIdxLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.tableViz.addLayout(self.horizontalLayout)

        self.bottomViz = QHBoxLayout()
        self.bottomViz.setObjectName(u"bottomViz")
        self.viz3 = WavetableVizPanel(self.layoutWidget)
        self.viz3.setObjectName(u"viz3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.viz3.sizePolicy().hasHeightForWidth())
        self.viz3.setSizePolicy(sizePolicy7)
        self.viz3.setMinimumSize(QSize(200, 200))

        self.bottomViz.addWidget(self.viz3)

        self.viz4 = WavetableVizPanel(self.layoutWidget)
        self.viz4.setObjectName(u"viz4")
        sizePolicy7.setHeightForWidth(self.viz4.sizePolicy().hasHeightForWidth())
        self.viz4.setSizePolicy(sizePolicy7)
        self.viz4.setMinimumSize(QSize(200, 200))

        self.bottomViz.addWidget(self.viz4)


        self.tableViz.addLayout(self.bottomViz)


        self.verticalLayout.addLayout(self.tableViz)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy8)
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(wavetableSetEditor)
        self.buttonBox.rejected.connect(wavetableSetEditor.reject)
        self.buttonBox.accepted.connect(wavetableSetEditor.accept)

        QMetaObject.connectSlotsByName(wavetableSetEditor)
    # setupUi

    def retranslateUi(self, wavetableSetEditor):
        wavetableSetEditor.setWindowTitle(QCoreApplication.translate("wavetableSetEditor", u"Wavetable Set Editor", None))
        self.windowTitle.setText(QCoreApplication.translate("wavetableSetEditor", u"Edit Wavetable Set", None))
        self.saveResourceSet.setText(QCoreApplication.translate("wavetableSetEditor", u"Save Set Data", None))
        self.saveForRack.setText(QCoreApplication.translate("wavetableSetEditor", u"Save for VCV Rack", None))
        self.windowTitle_2.setText(QCoreApplication.translate("wavetableSetEditor", u"Select wavetable slot for editing:", None))
        self.tableName.setText(QCoreApplication.translate("wavetableSetEditor", u"TABLENAME", None))
        self.openBrowser.setText(QCoreApplication.translate("wavetableSetEditor", u"Browser", None))
        self.label_2.setText(QCoreApplication.translate("wavetableSetEditor", u"Table Index:", None))
        self.tableIdxLabel.setText(QCoreApplication.translate("wavetableSetEditor", u"0", None))
        self.label.setText(QCoreApplication.translate("wavetableSetEditor", u"Waveform", None))
        self.label_4.setText(QCoreApplication.translate("wavetableSetEditor", u"Harmonics", None))
    # retranslateUi

