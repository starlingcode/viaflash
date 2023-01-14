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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

from wavetable_viz_panel import WavetableVizPanel

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(800, 600)
        wavetableBrowser.setMinimumSize(QSize(800, 600))
        wavetableBrowser.setMaximumSize(QSize(800, 600))
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 581))
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

        self.verticalLayoutWidget_2 = QWidget(wavetableBrowser)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(180, 10, 611, 581))
        self.tableViz = QVBoxLayout(self.verticalLayoutWidget_2)
        self.tableViz.setObjectName(u"tableViz")
        self.tableViz.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.viz3 = WavetableVizPanel(self.verticalLayoutWidget_2)
        self.viz3.setObjectName(u"viz3")

        self.gridLayout.addWidget(self.viz3, 1, 0, 1, 1)

        self.viz1 = WavetableVizPanel(self.verticalLayoutWidget_2)
        self.viz1.setObjectName(u"viz1")

        self.gridLayout.addWidget(self.viz1, 0, 0, 1, 1)

        self.viz2 = WavetableVizPanel(self.verticalLayoutWidget_2)
        self.viz2.setObjectName(u"viz2")

        self.gridLayout.addWidget(self.viz2, 0, 1, 1, 1)

        self.viz4 = WavetableVizPanel(self.verticalLayoutWidget_2)
        self.viz4.setObjectName(u"viz4")

        self.gridLayout.addWidget(self.viz4, 1, 1, 1, 1)


        self.tableViz.addLayout(self.gridLayout)


        self.retranslateUi(wavetableBrowser)

        QMetaObject.connectSlotsByName(wavetableBrowser)
    # setupUi

    def retranslateUi(self, wavetableBrowser):
        wavetableBrowser.setWindowTitle(QCoreApplication.translate("wavetableBrowser", u"Ratio", None))
        self.label_3.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table Type:", None))
        self.groupBox.setTitle("")
        self.slopePair.setText(QCoreApplication.translate("wavetableBrowser", u"Slope Pair", None))
        self.cycle.setText(QCoreApplication.translate("wavetableBrowser", u"Cycle", None))
        self.label.setText(QCoreApplication.translate("wavetableBrowser", u"Numer of Waveforms:", None))
        self.tableSizeWarning.setText(QCoreApplication.translate("wavetableBrowser", u"(the first N will be used)", None))
        self.label_2.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table:", None))
        self.swapTable.setText(QCoreApplication.translate("wavetableBrowser", u"Swap", None))
        self.close.setText(QCoreApplication.translate("wavetableBrowser", u"Close", None))
    # retranslateUi

