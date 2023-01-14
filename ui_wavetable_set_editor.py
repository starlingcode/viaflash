# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wavetable_set_editor.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from wavetable_viz_panel import WavetableVizPanel

class Ui_wavetableSetEditor(object):
    def setupUi(self, wavetableSetEditor):
        if not wavetableSetEditor.objectName():
            wavetableSetEditor.setObjectName(u"wavetableSetEditor")
        wavetableSetEditor.resize(600, 800)
        wavetableSetEditor.setMinimumSize(QSize(600, 800))
        wavetableSetEditor.setMaximumSize(QSize(600, 800))
        self.layoutWidget = QWidget(wavetableSetEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 581, 781))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.windowTitle = QLabel(self.layoutWidget)
        self.windowTitle.setObjectName(u"windowTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowTitle.sizePolicy().hasHeightForWidth())
        self.windowTitle.setSizePolicy(sizePolicy)
        self.windowTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.windowTitle)

        self.resourceSetSaveLoad = QHBoxLayout()
        self.resourceSetSaveLoad.setObjectName(u"resourceSetSaveLoad")
        self.selectResourceSet = QComboBox(self.layoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")
        sizePolicy.setHeightForWidth(self.selectResourceSet.sizePolicy().hasHeightForWidth())
        self.selectResourceSet.setSizePolicy(sizePolicy)

        self.resourceSetSaveLoad.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.layoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.saveResourceSet.sizePolicy().hasHeightForWidth())
        self.saveResourceSet.setSizePolicy(sizePolicy1)

        self.resourceSetSaveLoad.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.layoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")
        sizePolicy1.setHeightForWidth(self.saveForRack.sizePolicy().hasHeightForWidth())
        self.saveForRack.setSizePolicy(sizePolicy1)

        self.resourceSetSaveLoad.addWidget(self.saveForRack)


        self.verticalLayout.addLayout(self.resourceSetSaveLoad)

        self.windowTitle_2 = QLabel(self.layoutWidget)
        self.windowTitle_2.setObjectName(u"windowTitle_2")
        sizePolicy.setHeightForWidth(self.windowTitle_2.sizePolicy().hasHeightForWidth())
        self.windowTitle_2.setSizePolicy(sizePolicy)
        self.windowTitle_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.windowTitle_2)

        self.tableMode = QComboBox(self.layoutWidget)
        self.tableMode.setObjectName(u"tableMode")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableMode.sizePolicy().hasHeightForWidth())
        self.tableMode.setSizePolicy(sizePolicy2)
        self.tableMode.setMinimumSize(QSize(200, 0))
        self.tableMode.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.tableMode, 0, Qt.AlignHCenter)

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout.addLayout(self.slotGroup1)

        self.resourceSaveLoad = QHBoxLayout()
        self.resourceSaveLoad.setObjectName(u"resourceSaveLoad")
        self.tableName = QLabel(self.layoutWidget)
        self.tableName.setObjectName(u"tableName")
        sizePolicy.setHeightForWidth(self.tableName.sizePolicy().hasHeightForWidth())
        self.tableName.setSizePolicy(sizePolicy)
        self.tableName.setAlignment(Qt.AlignCenter)

        self.resourceSaveLoad.addWidget(self.tableName)

        self.openBrowser = QPushButton(self.layoutWidget)
        self.openBrowser.setObjectName(u"openBrowser")

        self.resourceSaveLoad.addWidget(self.openBrowser)


        self.verticalLayout.addLayout(self.resourceSaveLoad)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.previewControls = QHBoxLayout()
        self.previewControls.setObjectName(u"previewControls")

        self.verticalLayout.addLayout(self.previewControls)

        self.tableViz = QVBoxLayout()
        self.tableViz.setObjectName(u"tableViz")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.viz1 = WavetableVizPanel(self.layoutWidget)
        self.viz1.setObjectName(u"viz1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.viz1.sizePolicy().hasHeightForWidth())
        self.viz1.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.viz1, 0, 0, 1, 1)

        self.viz2 = WavetableVizPanel(self.layoutWidget)
        self.viz2.setObjectName(u"viz2")
        sizePolicy3.setHeightForWidth(self.viz2.sizePolicy().hasHeightForWidth())
        self.viz2.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.viz2, 0, 1, 1, 1)

        self.viz3 = WavetableVizPanel(self.layoutWidget)
        self.viz3.setObjectName(u"viz3")
        sizePolicy3.setHeightForWidth(self.viz3.sizePolicy().hasHeightForWidth())
        self.viz3.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.viz3, 1, 0, 1, 1)

        self.viz4 = WavetableVizPanel(self.layoutWidget)
        self.viz4.setObjectName(u"viz4")
        sizePolicy3.setHeightForWidth(self.viz4.sizePolicy().hasHeightForWidth())
        self.viz4.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.viz4, 1, 1, 1, 1)


        self.tableViz.addLayout(self.gridLayout)


        self.verticalLayout.addLayout(self.tableViz)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(wavetableSetEditor)
        self.buttonBox.rejected.connect(wavetableSetEditor.reject)
        self.buttonBox.accepted.connect(wavetableSetEditor.accept)

        QMetaObject.connectSlotsByName(wavetableSetEditor)
    # setupUi

    def retranslateUi(self, wavetableSetEditor):
        wavetableSetEditor.setWindowTitle(QCoreApplication.translate("wavetableSetEditor", u"Wavetable Set Editor", None))
        self.windowTitle.setText(QCoreApplication.translate("wavetableSetEditor", u"Edit Wavetable Set", None))
        self.saveResourceSet.setText(QCoreApplication.translate("wavetableSetEditor", u"Save Set Data", None))
        self.saveForRack.setText(QCoreApplication.translate("wavetableSetEditor", u"Save for Rack", None))
        self.windowTitle_2.setText(QCoreApplication.translate("wavetableSetEditor", u"Select wavetable slot for editing:", None))
        self.tableName.setText(QCoreApplication.translate("wavetableSetEditor", u"TABLENAME", None))
        self.openBrowser.setText(QCoreApplication.translate("wavetableSetEditor", u"Browser", None))
        self.label.setText(QCoreApplication.translate("wavetableSetEditor", u"Visualizer", None))
    # retranslateUi

