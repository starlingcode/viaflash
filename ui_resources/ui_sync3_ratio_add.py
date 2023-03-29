# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_ratio_add.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

from ratio_display import RatioDisplay

class Ui_sync3RatioAdd(object):
    def setupUi(self, sync3RatioAdd):
        if not sync3RatioAdd.objectName():
            sync3RatioAdd.setObjectName(u"sync3RatioAdd")
        sync3RatioAdd.resize(180, 350)
        sync3RatioAdd.setMinimumSize(QSize(180, 350))
        sync3RatioAdd.setMaximumSize(QSize(180, 350))
        self.layoutWidget = QWidget(sync3RatioAdd)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 331))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ratioDisplay = RatioDisplay(self.layoutWidget)
        self.ratioDisplay.setObjectName(u"ratioDisplay")

        self.verticalLayout.addWidget(self.ratioDisplay)

        self.numerator = QSpinBox(self.layoutWidget)
        self.numerator.setObjectName(u"numerator")
        self.numerator.setMinimum(1)
        self.numerator.setMaximum(255)

        self.verticalLayout.addWidget(self.numerator)

        self.denominator = QSpinBox(self.layoutWidget)
        self.denominator.setObjectName(u"denominator")
        self.denominator.setMinimum(1)
        self.denominator.setMaximum(255)

        self.verticalLayout.addWidget(self.denominator)

        self.addRatio = QPushButton(self.layoutWidget)
        self.addRatio.setObjectName(u"addRatio")

        self.verticalLayout.addWidget(self.addRatio)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)


        self.retranslateUi(sync3RatioAdd)

        QMetaObject.connectSlotsByName(sync3RatioAdd)
    # setupUi

    def retranslateUi(self, sync3RatioAdd):
        sync3RatioAdd.setWindowTitle(QCoreApplication.translate("sync3RatioAdd", u"Add Ratio", None))
        self.addRatio.setText(QCoreApplication.translate("sync3RatioAdd", u"Add", None))
        self.close.setText(QCoreApplication.translate("sync3RatioAdd", u"Close", None))
    # retranslateUi

