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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

from wavetable_viz_panel import WavetableVizPanel

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(800, 625)
        wavetableBrowser.setMinimumSize(QSize(800, 625))
        wavetableBrowser.setMaximumSize(QSize(800, 625))
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 601))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 10, 160, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slopePair = QRadioButton(self.verticalLayoutWidget)
        self.slopePair.setObjectName(u"slopePair")

        self.verticalLayout_2.addWidget(self.slopePair)

        self.cycle = QRadioButton(self.verticalLayoutWidget)
        self.cycle.setObjectName(u"cycle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cycle.sizePolicy().hasHeightForWidth())
        self.cycle.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.cycle)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.tableSize = QComboBox(self.layoutWidget)
        self.tableSize.setObjectName(u"tableSize")

        self.verticalLayout.addWidget(self.tableSize)

        self.tableSizeWarning = QLabel(self.layoutWidget)
        self.tableSizeWarning.setObjectName(u"tableSizeWarning")
        sizePolicy.setHeightForWidth(self.tableSizeWarning.sizePolicy().hasHeightForWidth())
        self.tableSizeWarning.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.tableSizeWarning)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.selectTable = QComboBox(self.layoutWidget)
        self.selectTable.setObjectName(u"selectTable")

        self.verticalLayout.addWidget(self.selectTable)

        self.swapTable = QPushButton(self.layoutWidget)
        self.swapTable.setObjectName(u"swapTable")

        self.verticalLayout.addWidget(self.swapTable)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)

        self.widget = QWidget(wavetableBrowser)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(181, 11, 611, 600))
        self.tableViz_2 = QVBoxLayout(self.widget)
        self.tableViz_2.setObjectName(u"tableViz_2")
        self.tableViz_2.setContentsMargins(0, 0, 0, 0)
        self.topViz = QHBoxLayout()
        self.topViz.setObjectName(u"topViz")
        self.viz1 = WavetableVizPanel(self.widget)
        self.viz1.setObjectName(u"viz1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.viz1.sizePolicy().hasHeightForWidth())
        self.viz1.setSizePolicy(sizePolicy3)
        self.viz1.setMinimumSize(QSize(275, 275))

        self.topViz.addWidget(self.viz1)

        self.viz2 = WavetableVizPanel(self.widget)
        self.viz2.setObjectName(u"viz2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.viz2.sizePolicy().hasHeightForWidth())
        self.viz2.setSizePolicy(sizePolicy4)
        self.viz2.setMinimumSize(QSize(275, 275))

        self.topViz.addWidget(self.viz2)


        self.tableViz_2.addLayout(self.topViz)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.tableIdx = QSlider(self.widget)
        self.tableIdx.setObjectName(u"tableIdx")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableIdx.sizePolicy().hasHeightForWidth())
        self.tableIdx.setSizePolicy(sizePolicy5)
        self.tableIdx.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.tableIdx)

        self.tableIdxLabel = QLabel(self.widget)
        self.tableIdxLabel.setObjectName(u"tableIdxLabel")
        sizePolicy.setHeightForWidth(self.tableIdxLabel.sizePolicy().hasHeightForWidth())
        self.tableIdxLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.tableIdxLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.tableViz_2.addLayout(self.horizontalLayout_2)

        self.bottomViz = QHBoxLayout()
        self.bottomViz.setObjectName(u"bottomViz")
        self.viz3 = WavetableVizPanel(self.widget)
        self.viz3.setObjectName(u"viz3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.viz3.sizePolicy().hasHeightForWidth())
        self.viz3.setSizePolicy(sizePolicy6)
        self.viz3.setMinimumSize(QSize(275, 275))

        self.bottomViz.addWidget(self.viz3)

        self.viz4 = WavetableVizPanel(self.widget)
        self.viz4.setObjectName(u"viz4")
        sizePolicy6.setHeightForWidth(self.viz4.sizePolicy().hasHeightForWidth())
        self.viz4.setSizePolicy(sizePolicy6)
        self.viz4.setMinimumSize(QSize(275, 275))

        self.bottomViz.addWidget(self.viz4)


        self.tableViz_2.addLayout(self.bottomViz)


        self.retranslateUi(wavetableBrowser)

        QMetaObject.connectSlotsByName(wavetableBrowser)
    # setupUi

    def retranslateUi(self, wavetableBrowser):
        wavetableBrowser.setWindowTitle(QCoreApplication.translate("wavetableBrowser", u"Wavetable Browser", None))
        self.label_3.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table Type:", None))
        self.groupBox.setTitle("")
        self.slopePair.setText(QCoreApplication.translate("wavetableBrowser", u"Slope Pair", None))
        self.cycle.setText(QCoreApplication.translate("wavetableBrowser", u"Cycle", None))
        self.label.setText(QCoreApplication.translate("wavetableBrowser", u"Numer of Waveforms:", None))
        self.tableSizeWarning.setText(QCoreApplication.translate("wavetableBrowser", u"(the first N will be used)", None))
        self.label_2.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table:", None))
        self.swapTable.setText(QCoreApplication.translate("wavetableBrowser", u"Select", None))
        self.close.setText(QCoreApplication.translate("wavetableBrowser", u"Cancel", None))
        self.label_4.setText(QCoreApplication.translate("wavetableBrowser", u"Table Index:", None))
        self.tableIdxLabel.setText(QCoreApplication.translate("wavetableBrowser", u"0", None))
    # retranslateUi

