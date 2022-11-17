# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(262, 126)
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        sync3Ratio.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3Ratio)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 90, 201, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.horizontalLayoutWidget = QWidget(sync3Ratio)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 261, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.decimalData = QLabel(self.horizontalLayoutWidget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalData)

        self.decimalLabel = QLabel(self.horizontalLayoutWidget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.semitonesData = QLabel(self.horizontalLayoutWidget)
        self.semitonesData.setObjectName(u"semitonesData")
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesData)

        self.semitonesLabel = QLabel(self.horizontalLayoutWidget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(sync3Ratio)
        self.buttonBox.accepted.connect(sync3Ratio.accept)
        self.buttonBox.rejected.connect(sync3Ratio.reject)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(262, 126)
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        sync3Ratio.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3Ratio)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 90, 201, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.horizontalLayoutWidget = QWidget(sync3Ratio)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 261, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.decimalData = QLabel(self.horizontalLayoutWidget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalData)

        self.decimalLabel = QLabel(self.horizontalLayoutWidget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.semitonesData = QLabel(self.horizontalLayoutWidget)
        self.semitonesData.setObjectName(u"semitonesData")
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesData)

        self.semitonesLabel = QLabel(self.horizontalLayoutWidget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.pushButton = QPushButton(sync3Ratio)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 90, 90, 32))

        self.retranslateUi(sync3Ratio)
        self.buttonBox.accepted.connect(sync3Ratio.accept)
        self.buttonBox.rejected.connect(sync3Ratio.reject)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones", None))
        self.pushButton.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(262, 126)
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        sync3Ratio.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3Ratio)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 90, 201, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.horizontalLayoutWidget = QWidget(sync3Ratio)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 261, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.decimalData = QLabel(self.horizontalLayoutWidget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalData)

        self.decimalLabel = QLabel(self.horizontalLayoutWidget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.semitonesData = QLabel(self.horizontalLayoutWidget)
        self.semitonesData.setObjectName(u"semitonesData")
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesData)

        self.semitonesLabel = QLabel(self.horizontalLayoutWidget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.removeRatio = QPushButton(sync3Ratio)
        self.removeRatio.setObjectName(u"removeRatio")
        self.removeRatio.setGeometry(QRect(60, 90, 90, 32))

        self.retranslateUi(sync3Ratio)
        self.buttonBox.accepted.connect(sync3Ratio.accept)
        self.buttonBox.rejected.connect(sync3Ratio.reject)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(262, 126)
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        sync3Ratio.setPalette(palette)
        self.buttonBox = QDialogButtonBox(sync3Ratio)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 90, 201, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.horizontalLayoutWidget = QWidget(sync3Ratio)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 261, 81))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.decimalData = QLabel(self.horizontalLayoutWidget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalData)

        self.decimalLabel = QLabel(self.horizontalLayoutWidget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.decimalLabel)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.semitonesData = QLabel(self.horizontalLayoutWidget)
        self.semitonesData.setObjectName(u"semitonesData")
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesData)

        self.semitonesLabel = QLabel(self.horizontalLayoutWidget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.semitonesLabel)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.xyLayout = QVBoxLayout()
        self.xyLayout.setObjectName(u"xyLayout")

        self.horizontalLayout.addLayout(self.xyLayout)

        self.removeRatio = QPushButton(sync3Ratio)
        self.removeRatio.setObjectName(u"removeRatio")
        self.removeRatio.setGeometry(QRect(60, 90, 90, 32))

        self.retranslateUi(sync3Ratio)
        self.buttonBox.accepted.connect(sync3Ratio.accept)
        self.buttonBox.rejected.connect(sync3Ratio.reject)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(180, 271)
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        sync3Ratio.setPalette(palette)
        self.widget = QWidget(sync3Ratio)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 181, 271))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.semitonesLabel = QLabel(self.widget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semitonesLabel.sizePolicy().hasHeightForWidth())
        self.semitonesLabel.setSizePolicy(sizePolicy)
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesLabel)

        self.semitonesData = QLabel(self.widget)
        self.semitonesData.setObjectName(u"semitonesData")
        sizePolicy.setHeightForWidth(self.semitonesData.sizePolicy().hasHeightForWidth())
        self.semitonesData.setSizePolicy(sizePolicy)
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesData)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.decimalLabel = QLabel(self.widget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalLabel)

        self.decimalData = QLabel(self.widget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalData)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget)
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

        self.removeRatio = QPushButton(self.widget)
        self.removeRatio.setObjectName(u"removeRatio")

        self.verticalLayout.addWidget(self.removeRatio)

        self.close = QPushButton(self.widget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)


        self.retranslateUi(sync3Ratio)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones:", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal:", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sync3Ratio", u"XY", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
        self.close.setText(QCoreApplication.translate("sync3Ratio", u"Close", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(180, 271)
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        sync3Ratio.setPalette(palette)
        self.widget = QWidget(sync3Ratio)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 181, 271))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.semitonesLabel = QLabel(self.widget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semitonesLabel.sizePolicy().hasHeightForWidth())
        self.semitonesLabel.setSizePolicy(sizePolicy)
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesLabel)

        self.semitonesData = QLabel(self.widget)
        self.semitonesData.setObjectName(u"semitonesData")
        sizePolicy.setHeightForWidth(self.semitonesData.sizePolicy().hasHeightForWidth())
        self.semitonesData.setSizePolicy(sizePolicy)
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesData)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.decimalLabel = QLabel(self.widget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalLabel)

        self.decimalData = QLabel(self.widget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalData)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget)
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

        self.removeRatio = QPushButton(self.widget)
        self.removeRatio.setObjectName(u"removeRatio")

        self.verticalLayout.addWidget(self.removeRatio)

        self.close = QPushButton(self.widget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)


        self.retranslateUi(sync3Ratio)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones:", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal:", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sync3Ratio", u"XY", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
        self.close.setText(QCoreApplication.translate("sync3Ratio", u"Close", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(180, 271)
        palette = QPalette()
        brush = QBrush(QColor(200, 200, 200, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush3 = QBrush(QColor(255, 255, 220, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush1)
        sync3Ratio.setPalette(palette)
        self.widget = QWidget(sync3Ratio)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 161, 251))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.semitonesLabel = QLabel(self.widget)
        self.semitonesLabel.setObjectName(u"semitonesLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.semitonesLabel.sizePolicy().hasHeightForWidth())
        self.semitonesLabel.setSizePolicy(sizePolicy)
        self.semitonesLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesLabel)

        self.semitonesData = QLabel(self.widget)
        self.semitonesData.setObjectName(u"semitonesData")
        sizePolicy.setHeightForWidth(self.semitonesData.sizePolicy().hasHeightForWidth())
        self.semitonesData.setSizePolicy(sizePolicy)
        self.semitonesData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.semitonesData)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.decimalLabel = QLabel(self.widget)
        self.decimalLabel.setObjectName(u"decimalLabel")
        self.decimalLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalLabel)

        self.decimalData = QLabel(self.widget)
        self.decimalData.setObjectName(u"decimalData")
        self.decimalData.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.decimalData)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.widget)
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

        self.removeRatio = QPushButton(self.widget)
        self.removeRatio.setObjectName(u"removeRatio")

        self.verticalLayout.addWidget(self.removeRatio)

        self.close = QPushButton(self.widget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)


        self.retranslateUi(sync3Ratio)

        QMetaObject.connectSlotsByName(sync3Ratio)
    # setupUi

    def retranslateUi(self, sync3Ratio):
        sync3Ratio.setWindowTitle(QCoreApplication.translate("sync3Ratio", u"Ratio", None))
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones:", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal:", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sync3Ratio", u"XY:", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
        self.close.setText(QCoreApplication.translate("sync3Ratio", u"Close", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sync3_ratio.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_sync3Ratio(object):
    def setupUi(self, sync3Ratio):
        if not sync3Ratio.objectName():
            sync3Ratio.setObjectName(u"sync3Ratio")
        sync3Ratio.resize(180, 271)
        self.layoutWidget = QWidget(sync3Ratio)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 251))
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
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones:", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal:", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sync3Ratio", u"XY:", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
        self.close.setText(QCoreApplication.translate("sync3Ratio", u"Close", None))
    # retranslateUi

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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.semitonesLabel.setText(QCoreApplication.translate("sync3Ratio", u"Semitones:", None))
        self.semitonesData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.decimalLabel.setText(QCoreApplication.translate("sync3Ratio", u"Decimal:", None))
        self.decimalData.setText(QCoreApplication.translate("sync3Ratio", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("sync3Ratio", u"XY:", None))
        self.removeRatio.setText(QCoreApplication.translate("sync3Ratio", u"Remove", None))
        self.close.setText(QCoreApplication.translate("sync3Ratio", u"Close", None))
    # retranslateUi

