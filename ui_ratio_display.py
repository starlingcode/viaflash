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
        ratioDisplay.resize(225, 214)
        self.verticalLayout = QVBoxLayout(ratioDisplay)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(ratioDisplay)
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
        self.decimalLabel = QLabel(ratioDisplay)
        self.decimalLabel.setObjectName(u"decimalLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.decimalLabel.sizePolicy().hasHeightForWidth())
        self.decimalLabel.setSizePolicy(sizePolicy1)
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalLabel)

        self.decimalData = QLabel(ratioDisplay)
        self.decimalData.setObjectName(u"decimalData")
        sizePolicy1.setHeightForWidth(self.decimalData.sizePolicy().hasHeightForWidth())
        self.decimalData.setSizePolicy(sizePolicy1)
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalData)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.semitonesLabel = QLabel(ratioDisplay)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.semitonesLabel.sizePolicy().hasHeightForWidth())
        self.semitonesLabel.setSizePolicy(sizePolicy2)
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesLabel)

        self.semitonesData = QLabel(ratioDisplay)
        self.semitonesData.setObjectName(u"semitonesData")
        sizePolicy2.setHeightForWidth(self.semitonesData.sizePolicy().hasHeightForWidth())
        self.semitonesData.setSizePolicy(sizePolicy2)
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

