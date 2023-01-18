# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio_display.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ratioDisplay(object):
    def setupUi(self, ratioDisplay):
        if not ratioDisplay.objectName():
            ratioDisplay.setObjectName(u"ratioDisplay")
        ratioDisplay.resize(142, 170)
        self.layoutWidget = QWidget(ratioDisplay)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 142, 171))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.xyLayout = QVBoxLayout()
        self.xyLayout.setObjectName(u"xyLayout")

        self.horizontalLayout_3.addLayout(self.xyLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.decimalLabel = QLabel(self.layoutWidget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalLabel)

        self.decimalData = QLabel(self.layoutWidget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalData)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.semitonesLabel = QLabel(self.layoutWidget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.semitonesLabel.sizePolicy().hasHeightForWidth())
        self.semitonesLabel.setSizePolicy(sizePolicy1)
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesLabel)

        self.semitonesData = QLabel(self.layoutWidget)
        self.semitonesData.setObjectName(u"semitonesData")
        sizePolicy1.setHeightForWidth(self.semitonesData.sizePolicy().hasHeightForWidth())
        self.semitonesData.setSizePolicy(sizePolicy1)
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesData)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(ratioDisplay)

        QMetaObject.connectSlotsByName(ratioDisplay)
    # setupUi

    def retranslateUi(self, ratioDisplay):
        ratioDisplay.setWindowTitle(QCoreApplication.translate("ratioDisplay", u"Form", None))
        self.label.setText(QCoreApplication.translate("ratioDisplay", u"XY:", None))
        self.decimalLabel.setText(QCoreApplication.translate("ratioDisplay", u"Decimal:", None))
        self.decimalData.setText(QCoreApplication.translate("ratioDisplay", u"TextLabel", None))
        self.semitonesLabel.setText(QCoreApplication.translate("ratioDisplay", u"Semitones:", None))
        self.semitonesData.setText(QCoreApplication.translate("ratioDisplay", u"TextLabel", None))
    # retranslateUi

