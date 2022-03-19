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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(180, 273)
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 251))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 160, 61))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slopePair = QRadioButton(self.verticalLayoutWidget)
        self.slopePair.setObjectName(u"slopePair")

        self.verticalLayout_2.addWidget(self.slopePair)

        self.cycle = QRadioButton(self.verticalLayoutWidget)
        self.cycle.setObjectName(u"cycle")

        self.verticalLayout_2.addWidget(self.cycle)


        self.horizontalLayout.addWidget(self.groupBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.tableSize = QComboBox(self.layoutWidget)
        self.tableSize.setObjectName(u"tableSize")

        self.verticalLayout.addWidget(self.tableSize)

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


        self.retranslateUi(wavetableBrowser)

        QMetaObject.connectSlotsByName(wavetableBrowser)
    # setupUi

    def retranslateUi(self, wavetableBrowser):
        wavetableBrowser.setWindowTitle(QCoreApplication.translate("wavetableBrowser", u"Ratio", None))
        self.groupBox.setTitle(QCoreApplication.translate("wavetableBrowser", u"Table Type:", None))
        self.slopePair.setText(QCoreApplication.translate("wavetableBrowser", u"Slope Pair", None))
        self.cycle.setText(QCoreApplication.translate("wavetableBrowser", u"Cycle", None))
        self.label.setText(QCoreApplication.translate("wavetableBrowser", u"Numer of Waveforms:", None))
        self.label_2.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table:", None))
        self.swapTable.setText(QCoreApplication.translate("wavetableBrowser", u"Swap", None))
        self.close.setText(QCoreApplication.translate("wavetableBrowser", u"Close", None))
    # retranslateUi

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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(570, 331)
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 311))
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

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.selectTable = QComboBox(self.layoutWidget)
        self.selectTable.setObjectName(u"selectTable")

        self.verticalLayout.addWidget(self.selectTable)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.swapTable = QPushButton(self.layoutWidget)
        self.swapTable.setObjectName(u"swapTable")

        self.verticalLayout.addWidget(self.swapTable)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)

        self.horizontalLayoutWidget_3 = QWidget(wavetableBrowser)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(180, 10, 381, 41))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.displayType = QComboBox(self.horizontalLayoutWidget_3)
        self.displayType.setObjectName(u"displayType")

        self.previewControls.addWidget(self.displayType)

        self.tableIndex = QSpinBox(self.horizontalLayoutWidget_3)
        self.tableIndex.setObjectName(u"tableIndex")

        self.previewControls.addWidget(self.tableIndex)

        self.verticalLayoutWidget_2 = QWidget(wavetableBrowser)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(180, 60, 381, 261))
        self.tableViz = QVBoxLayout(self.verticalLayoutWidget_2)
        self.tableViz.setObjectName(u"tableViz")
        self.tableViz.setContentsMargins(0, 0, 0, 0)

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
        self.label_2.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table:", None))
        self.swapTable.setText(QCoreApplication.translate("wavetableBrowser", u"Swap", None))
        self.close.setText(QCoreApplication.translate("wavetableBrowser", u"Close", None))
    # retranslateUi

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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(570, 331)
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 311))
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

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label_2)

        self.selectTable = QComboBox(self.layoutWidget)
        self.selectTable.setObjectName(u"selectTable")

        self.verticalLayout.addWidget(self.selectTable)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.swapTable = QPushButton(self.layoutWidget)
        self.swapTable.setObjectName(u"swapTable")

        self.verticalLayout.addWidget(self.swapTable)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)

        self.horizontalLayoutWidget_3 = QWidget(wavetableBrowser)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(180, 10, 381, 41))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.displayType = QComboBox(self.horizontalLayoutWidget_3)
        self.displayType.setObjectName(u"displayType")

        self.previewControls.addWidget(self.displayType)

        self.tableIndex = QSpinBox(self.horizontalLayoutWidget_3)
        self.tableIndex.setObjectName(u"tableIndex")

        self.previewControls.addWidget(self.tableIndex)

        self.verticalLayoutWidget_2 = QWidget(wavetableBrowser)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(180, 60, 381, 261))
        self.tableViz = QVBoxLayout(self.verticalLayoutWidget_2)
        self.tableViz.setObjectName(u"tableViz")
        self.tableViz.setContentsMargins(0, 0, 0, 0)

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
        self.label_2.setText(QCoreApplication.translate("wavetableBrowser", u"Select Table:", None))
        self.swapTable.setText(QCoreApplication.translate("wavetableBrowser", u"Swap", None))
        self.close.setText(QCoreApplication.translate("wavetableBrowser", u"Close", None))
    # retranslateUi

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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(570, 331)
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 311))
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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.swapTable = QPushButton(self.layoutWidget)
        self.swapTable.setObjectName(u"swapTable")

        self.verticalLayout.addWidget(self.swapTable)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)

        self.horizontalLayoutWidget_3 = QWidget(wavetableBrowser)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(180, 10, 381, 41))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.displayType = QComboBox(self.horizontalLayoutWidget_3)
        self.displayType.setObjectName(u"displayType")

        self.previewControls.addWidget(self.displayType)

        self.tableIndex = QSpinBox(self.horizontalLayoutWidget_3)
        self.tableIndex.setObjectName(u"tableIndex")

        self.previewControls.addWidget(self.tableIndex)

        self.verticalLayoutWidget_2 = QWidget(wavetableBrowser)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(180, 60, 381, 261))
        self.tableViz = QVBoxLayout(self.verticalLayoutWidget_2)
        self.tableViz.setObjectName(u"tableViz")
        self.tableViz.setContentsMargins(0, 0, 0, 0)

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
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_wavetableBrowser(object):
    def setupUi(self, wavetableBrowser):
        if not wavetableBrowser.objectName():
            wavetableBrowser.setObjectName(u"wavetableBrowser")
        wavetableBrowser.resize(570, 331)
        self.layoutWidget = QWidget(wavetableBrowser)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 161, 311))
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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.swapTable = QPushButton(self.layoutWidget)
        self.swapTable.setObjectName(u"swapTable")

        self.verticalLayout.addWidget(self.swapTable)

        self.close = QPushButton(self.layoutWidget)
        self.close.setObjectName(u"close")

        self.verticalLayout.addWidget(self.close)

        self.horizontalLayoutWidget_3 = QWidget(wavetableBrowser)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(180, 10, 381, 41))
        self.previewControls = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.previewControls.setObjectName(u"previewControls")
        self.previewControls.setContentsMargins(0, 0, 0, 0)
        self.displayType = QComboBox(self.horizontalLayoutWidget_3)
        self.displayType.setObjectName(u"displayType")

        self.previewControls.addWidget(self.displayType)

        self.tableIndex = QSpinBox(self.horizontalLayoutWidget_3)
        self.tableIndex.setObjectName(u"tableIndex")

        self.previewControls.addWidget(self.tableIndex)

        self.verticalLayoutWidget_2 = QWidget(wavetableBrowser)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(180, 60, 381, 261))
        self.tableViz = QVBoxLayout(self.verticalLayoutWidget_2)
        self.tableViz.setObjectName(u"tableViz")
        self.tableViz.setContentsMargins(0, 0, 0, 0)

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

