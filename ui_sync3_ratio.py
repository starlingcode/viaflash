# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_ratio.ui'
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
    QVBoxLayout, QWidget)

from ratio_display import RatioDisplay

class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(180, 270)
        sync3Ratio.setMinimumSize(QSize(180, 270))
        sync3Ratio.setMaximumSize(QSize(180, 270))
        self.layoutWidget = QWidget(sync3Ratio)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ratioDisplay = RatioDisplay(self.layoutWidget)
        self.ratioDisplay.setObjectName(u"ratioDisplay")

        self.verticalLayout.addWidget(self.ratioDisplay)

        self.removeRatio = QPushButton(self.layoutWidget)
        self.removeRatio.setObjectName(u"removeRatio")

        self.verticalLayout.addWidget(self.removeRatio)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)


        self.retranslateUi(sync3Ratio)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
        self.close.setText(QCoreApplication.translate("sync3Ratio", u"Close", None))
    # retranslateUi

