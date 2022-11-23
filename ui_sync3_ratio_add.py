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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.semitonesLabel = QLabel(self.layoutWidget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semitonesLabel.sizePolicy().hasHeightForWidth())
        self.semitonesLabel.setSizePolicy(sizePolicy)
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesLabel)

        self.semitonesData = QLabel(self.layoutWidget)
        self.semitonesData.setObjectName(u"semitonesData")
        sizePolicy.setHeightForWidth(self.semitonesData.sizePolicy().hasHeightForWidth())
        self.semitonesData.setSizePolicy(sizePolicy)
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesData)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

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

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.xyLayout = QVBoxLayout()
        self.xyLayout.setObjectName(u"xyLayout")

        self.horizontalLayout_3.addLayout(self.xyLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

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
        sync3RatioAdd.setWindowTitle(QCoreApplication.translate("sync3RatioAdd", u"Ratio", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3RatioAdd", u"Semitones:", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3RatioAdd", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3RatioAdd", u"Decimal:", None))
        self.decimalData.setText(QCoreApplication.translate("sync3RatioAdd", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sync3RatioAdd", u"XY:", None))
        self.addRatio.setText(QCoreApplication.translate("sync3RatioAdd", u"Add", None))
        self.close.setText(QCoreApplication.translate("sync3RatioAdd", u"Close", None))
    # retranslateUi

