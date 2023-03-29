# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wavetable_browser.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QDialog, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)

from superqt import QLabeledRangeSlider
from wavetable_viz_panel import WavetableVizPanel

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(970, 616)
        wavetableBrowser.setMinimumSize(QSize(0, 0))
        wavetableBrowser.setMaximumSize(QSize(10000, 10000))
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(160, 10, 191, 601))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.tableList = QListWidget(self.layoutWidget)
        self.tableList.setObjectName(u"tableList")

        self.verticalLayout.addWidget(self.tableList)

        self.swapTable = QPushButton(self.layoutWidget)
        self.swapTable.setObjectName(u"swapTable")

        self.verticalLayout.addWidget(self.swapTable)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)

        self.layoutWidgetNO = QWidget(wavetableBrowser)
        self.layoutWidgetNO.setObjectName(u"layoutWidgetNO")
        self.layoutWidgetNO.setGeometry(QRect(350, 10, 611, 600))
        self.tableViz_2 = QVBoxLayout(self.layoutWidgetNO)
        self.tableViz_2.setObjectName(u"tableViz_2")
        self.tableViz_2.setContentsMargins(0, 0, 0, 0)
        self.topViz = QHBoxLayout()
        self.topViz.setObjectName(u"topViz")
        self.viz1 = WavetableVizPanel(self.layoutWidgetNO)
        self.viz1.setObjectName(u"viz1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viz1.sizePolicy().hasHeightForWidth())
        self.viz1.setSizePolicy(sizePolicy1)
        self.viz1.setMinimumSize(QSize(275, 275))

        self.topViz.addWidget(self.viz1)

        self.viz2 = WavetableVizPanel(self.layoutWidgetNO)
        self.viz2.setObjectName(u"viz2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.viz2.sizePolicy().hasHeightForWidth())
        self.viz2.setSizePolicy(sizePolicy2)
        self.viz2.setMinimumSize(QSize(275, 275))

        self.topViz.addWidget(self.viz2)


        self.tableViz_2.addLayout(self.topViz)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.layoutWidgetNO)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.tableIdx = QSlider(self.layoutWidgetNO)
        self.tableIdx.setObjectName(u"tableIdx")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableIdx.sizePolicy().hasHeightForWidth())
        self.tableIdx.setSizePolicy(sizePolicy3)
        self.tableIdx.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.tableIdx)

        self.tableIdxLabel = QLabel(self.layoutWidgetNO)
        self.tableIdxLabel.setObjectName(u"tableIdxLabel")
        sizePolicy.setHeightForWidth(self.tableIdxLabel.sizePolicy().hasHeightForWidth())
        self.tableIdxLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.tableIdxLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.tableViz_2.addLayout(self.horizontalLayout_2)

        self.bottomViz = QHBoxLayout()
        self.bottomViz.setObjectName(u"bottomViz")
        self.viz3 = WavetableVizPanel(self.layoutWidgetNO)
        self.viz3.setObjectName(u"viz3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.viz3.sizePolicy().hasHeightForWidth())
        self.viz3.setSizePolicy(sizePolicy4)
        self.viz3.setMinimumSize(QSize(275, 275))

        self.bottomViz.addWidget(self.viz3)

        self.viz4 = WavetableVizPanel(self.layoutWidgetNO)
        self.viz4.setObjectName(u"viz4")
        sizePolicy4.setHeightForWidth(self.viz4.sizePolicy().hasHeightForWidth())
        self.viz4.setSizePolicy(sizePolicy4)
        self.viz4.setMinimumSize(QSize(275, 275))

        self.bottomViz.addWidget(self.viz4)


        self.tableViz_2.addLayout(self.bottomViz)

        self.layoutWidget_2 = QWidget(wavetableBrowser)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 10, 141, 601))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_8)

        self.tagList = QListWidget(self.layoutWidget_2)
        self.tagList.setObjectName(u"tagList")

        self.verticalLayout_3.addWidget(self.tagList)

        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.orButton = QRadioButton(self.layoutWidget_2)
        self.buttonGroup = QButtonGroup(wavetableBrowser)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.orButton)
        self.orButton.setObjectName(u"orButton")

        self.horizontalLayout.addWidget(self.orButton)

        self.andButton = QRadioButton(self.layoutWidget_2)
        self.buttonGroup.addButton(self.andButton)
        self.andButton.setObjectName(u"andButton")

        self.horizontalLayout.addWidget(self.andButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.clearTags = QPushButton(self.layoutWidget_2)
        self.clearTags.setObjectName(u"clearTags")

        self.verticalLayout_3.addWidget(self.clearTags)

        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_9)

        self.tableSize = QLabeledRangeSlider(self.layoutWidget_2)
        self.tableSize.setObjectName(u"tableSize")
        self.tableSize.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.tableSize)

        self.tableSizeWarning = QLabel(self.layoutWidget_2)
        self.tableSizeWarning.setObjectName(u"tableSizeWarning")
        sizePolicy.setHeightForWidth(self.tableSizeWarning.sizePolicy().hasHeightForWidth())
        self.tableSizeWarning.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.tableSizeWarning)


        self.retranslateUi(wavetableBrowser)

        QMetaObject.connectSlotsByName(wavetableBrowser)
    # setupUi

    def retranslateUi(self, wavetableBrowser):
        wavetableBrowser.setWindowTitle(QCoreApplication.translate("wavetableBrowser", u"Wavetable Browser", None))
        self.label_2.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table:", None))
        self.swapTable.setText(QCoreApplication.translate("wavetableBrowser", u"Select", None))
        self.close.setText(QCoreApplication.translate("wavetableBrowser", u"Cancel", None))
        self.label_4.setText(QCoreApplication.translate("wavetableBrowser", u"Table Index:", None))
        self.tableIdxLabel.setText(QCoreApplication.translate("wavetableBrowser", u"0", None))
        self.label_8.setText(QCoreApplication.translate("wavetableBrowser", u"Filter by Tag:", None))
        self.label.setText(QCoreApplication.translate("wavetableBrowser", u"Tag combine mode:", None))
        self.orButton.setText(QCoreApplication.translate("wavetableBrowser", u"Or", None))
        self.andButton.setText(QCoreApplication.translate("wavetableBrowser", u"And", None))
        self.clearTags.setText(QCoreApplication.translate("wavetableBrowser", u"Clear Tag Filter", None))
        self.label_9.setText(QCoreApplication.translate("wavetableBrowser", u"Numer of Waveforms:", None))
        self.tableSizeWarning.setText(QCoreApplication.translate("wavetableBrowser", u"(first N will be used)", None))
    # retranslateUi

