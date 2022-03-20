# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wavetable_editor.ui'
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
    QDialogButtonBox, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_syncWavetableEditor(object):
    def setupUi(self, syncWavetableEditor):
        if not syncWavetableEditor.objectName():
            syncWavetableEditor.setObjectName(u"syncWavetableEditor")
        syncWavetableEditor.resize(401, 669)
        self.layoutWidget = QWidget(syncWavetableEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 381, 651))
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

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot1 = QPushButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setMinimumSize(QSize(30, 0))
        self.slot1.setCheckable(True)

        self.slotGroup1.addWidget(self.slot1)

        self.slot2 = QPushButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy3)
        self.slot2.setMinimumSize(QSize(30, 0))
        self.slot2.setCheckable(True)

        self.slotGroup1.addWidget(self.slot2)

        self.slot3 = QPushButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy3.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy3)
        self.slot3.setMinimumSize(QSize(30, 0))
        self.slot3.setCheckable(True)

        self.slotGroup1.addWidget(self.slot3)

        self.slot4 = QPushButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy3.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy3)
        self.slot4.setMinimumSize(QSize(30, 0))
        self.slot4.setCheckable(True)

        self.slotGroup1.addWidget(self.slot4)

        self.slot5 = QPushButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy3.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy3)
        self.slot5.setMinimumSize(QSize(30, 0))
        self.slot5.setCheckable(True)

        self.slotGroup1.addWidget(self.slot5)

        self.slot6 = QPushButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy3.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy3)
        self.slot6.setMinimumSize(QSize(30, 0))
        self.slot6.setCheckable(True)

        self.slotGroup1.addWidget(self.slot6)

        self.slot7 = QPushButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy3.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy3)
        self.slot7.setMinimumSize(QSize(30, 0))
        self.slot7.setCheckable(True)

        self.slotGroup1.addWidget(self.slot7)

        self.slot8 = QPushButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy3.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy3)
        self.slot8.setMinimumSize(QSize(30, 0))
        self.slot8.setCheckable(True)

        self.slotGroup1.addWidget(self.slot8)


        self.verticalLayout.addLayout(self.slotGroup1)

        self.slotGroup2 = QHBoxLayout()
        self.slotGroup2.setObjectName(u"slotGroup2")
        self.slotGroup2.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot9 = QPushButton(self.layoutWidget)
        self.slot9.setObjectName(u"slot9")
        self.slot9.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot9.sizePolicy().hasHeightForWidth())
        self.slot9.setSizePolicy(sizePolicy2)
        self.slot9.setMinimumSize(QSize(30, 0))
        self.slot9.setCheckable(True)

        self.slotGroup2.addWidget(self.slot9)

        self.slot10 = QPushButton(self.layoutWidget)
        self.slot10.setObjectName(u"slot10")
        sizePolicy3.setHeightForWidth(self.slot10.sizePolicy().hasHeightForWidth())
        self.slot10.setSizePolicy(sizePolicy3)
        self.slot10.setMinimumSize(QSize(30, 0))
        self.slot10.setCheckable(True)

        self.slotGroup2.addWidget(self.slot10)

        self.slot11 = QPushButton(self.layoutWidget)
        self.slot11.setObjectName(u"slot11")
        sizePolicy3.setHeightForWidth(self.slot11.sizePolicy().hasHeightForWidth())
        self.slot11.setSizePolicy(sizePolicy3)
        self.slot11.setMinimumSize(QSize(30, 0))
        self.slot11.setCheckable(True)

        self.slotGroup2.addWidget(self.slot11)

        self.slot12 = QPushButton(self.layoutWidget)
        self.slot12.setObjectName(u"slot12")
        sizePolicy3.setHeightForWidth(self.slot12.sizePolicy().hasHeightForWidth())
        self.slot12.setSizePolicy(sizePolicy3)
        self.slot12.setMinimumSize(QSize(30, 0))
        self.slot12.setCheckable(True)

        self.slotGroup2.addWidget(self.slot12)

        self.slot13 = QPushButton(self.layoutWidget)
        self.slot13.setObjectName(u"slot13")
        sizePolicy3.setHeightForWidth(self.slot13.sizePolicy().hasHeightForWidth())
        self.slot13.setSizePolicy(sizePolicy3)
        self.slot13.setMinimumSize(QSize(30, 0))
        self.slot13.setCheckable(True)

        self.slotGroup2.addWidget(self.slot13)

        self.slot14 = QPushButton(self.layoutWidget)
        self.slot14.setObjectName(u"slot14")
        sizePolicy3.setHeightForWidth(self.slot14.sizePolicy().hasHeightForWidth())
        self.slot14.setSizePolicy(sizePolicy3)
        self.slot14.setMinimumSize(QSize(30, 0))
        self.slot14.setCheckable(True)

        self.slotGroup2.addWidget(self.slot14)

        self.slot15 = QPushButton(self.layoutWidget)
        self.slot15.setObjectName(u"slot15")
        sizePolicy3.setHeightForWidth(self.slot15.sizePolicy().hasHeightForWidth())
        self.slot15.setSizePolicy(sizePolicy3)
        self.slot15.setMinimumSize(QSize(30, 0))
        self.slot15.setCheckable(True)

        self.slotGroup2.addWidget(self.slot15)

        self.slot16 = QPushButton(self.layoutWidget)
        self.slot16.setObjectName(u"slot16")
        sizePolicy3.setHeightForWidth(self.slot16.sizePolicy().hasHeightForWidth())
        self.slot16.setSizePolicy(sizePolicy3)
        self.slot16.setMinimumSize(QSize(30, 0))
        self.slot16.setCheckable(True)

        self.slotGroup2.addWidget(self.slot16)


        self.verticalLayout.addLayout(self.slotGroup2)

        self.slotGroup3 = QHBoxLayout()
        self.slotGroup3.setObjectName(u"slotGroup3")
        self.slotGroup3.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot17 = QPushButton(self.layoutWidget)
        self.slot17.setObjectName(u"slot17")
        self.slot17.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot17.sizePolicy().hasHeightForWidth())
        self.slot17.setSizePolicy(sizePolicy2)
        self.slot17.setMinimumSize(QSize(30, 0))
        self.slot17.setCheckable(True)

        self.slotGroup3.addWidget(self.slot17)

        self.slot18 = QPushButton(self.layoutWidget)
        self.slot18.setObjectName(u"slot18")
        sizePolicy3.setHeightForWidth(self.slot18.sizePolicy().hasHeightForWidth())
        self.slot18.setSizePolicy(sizePolicy3)
        self.slot18.setMinimumSize(QSize(30, 0))
        self.slot18.setCheckable(True)

        self.slotGroup3.addWidget(self.slot18)

        self.slot19 = QPushButton(self.layoutWidget)
        self.slot19.setObjectName(u"slot19")
        sizePolicy3.setHeightForWidth(self.slot19.sizePolicy().hasHeightForWidth())
        self.slot19.setSizePolicy(sizePolicy3)
        self.slot19.setMinimumSize(QSize(30, 0))
        self.slot19.setCheckable(True)

        self.slotGroup3.addWidget(self.slot19)

        self.slot20 = QPushButton(self.layoutWidget)
        self.slot20.setObjectName(u"slot20")
        sizePolicy3.setHeightForWidth(self.slot20.sizePolicy().hasHeightForWidth())
        self.slot20.setSizePolicy(sizePolicy3)
        self.slot20.setMinimumSize(QSize(30, 0))
        self.slot20.setCheckable(True)

        self.slotGroup3.addWidget(self.slot20)

        self.slot21 = QPushButton(self.layoutWidget)
        self.slot21.setObjectName(u"slot21")
        sizePolicy3.setHeightForWidth(self.slot21.sizePolicy().hasHeightForWidth())
        self.slot21.setSizePolicy(sizePolicy3)
        self.slot21.setMinimumSize(QSize(30, 0))
        self.slot21.setCheckable(True)

        self.slotGroup3.addWidget(self.slot21)

        self.slot22 = QPushButton(self.layoutWidget)
        self.slot22.setObjectName(u"slot22")
        sizePolicy3.setHeightForWidth(self.slot22.sizePolicy().hasHeightForWidth())
        self.slot22.setSizePolicy(sizePolicy3)
        self.slot22.setMinimumSize(QSize(30, 0))
        self.slot22.setCheckable(True)

        self.slotGroup3.addWidget(self.slot22)

        self.slot23 = QPushButton(self.layoutWidget)
        self.slot23.setObjectName(u"slot23")
        sizePolicy3.setHeightForWidth(self.slot23.sizePolicy().hasHeightForWidth())
        self.slot23.setSizePolicy(sizePolicy3)
        self.slot23.setMinimumSize(QSize(30, 0))
        self.slot23.setCheckable(True)

        self.slotGroup3.addWidget(self.slot23)

        self.slot24 = QPushButton(self.layoutWidget)
        self.slot24.setObjectName(u"slot24")
        sizePolicy3.setHeightForWidth(self.slot24.sizePolicy().hasHeightForWidth())
        self.slot24.setSizePolicy(sizePolicy3)
        self.slot24.setMinimumSize(QSize(30, 0))
        self.slot24.setCheckable(True)

        self.slotGroup3.addWidget(self.slot24)


        self.verticalLayout.addLayout(self.slotGroup3)

        self.slotGroup3_2 = QHBoxLayout()
        self.slotGroup3_2.setObjectName(u"slotGroup3_2")
        self.slotGroup3_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot25 = QPushButton(self.layoutWidget)
        self.slot25.setObjectName(u"slot25")
        self.slot25.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot25.sizePolicy().hasHeightForWidth())
        self.slot25.setSizePolicy(sizePolicy2)
        self.slot25.setMinimumSize(QSize(30, 0))
        self.slot25.setCheckable(True)

        self.slotGroup3_2.addWidget(self.slot25)


        self.verticalLayout.addLayout(self.slotGroup3_2)

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
        self.displayType = QComboBox(self.layoutWidget)
        self.displayType.setObjectName(u"displayType")

        self.previewControls.addWidget(self.displayType)

        self.tableIndex = QSpinBox(self.layoutWidget)
        self.tableIndex.setObjectName(u"tableIndex")

        self.previewControls.addWidget(self.tableIndex)


        self.verticalLayout.addLayout(self.previewControls)

        self.tableViz = QVBoxLayout()
        self.tableViz.setObjectName(u"tableViz")
        self.vizSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tableViz.addItem(self.vizSpacer)


        self.verticalLayout.addLayout(self.tableViz)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(syncWavetableEditor)
        self.buttonBox.rejected.connect(syncWavetableEditor.reject)
        self.buttonBox.accepted.connect(syncWavetableEditor.accept)

        QMetaObject.connectSlotsByName(syncWavetableEditor)
    # setupUi

    def retranslateUi(self, syncWavetableEditor):
        syncWavetableEditor.setWindowTitle(QCoreApplication.translate("syncWavetableEditor", u"Wavetable Set Editor", None))
        self.windowTitle.setText(QCoreApplication.translate("syncWavetableEditor", u"Edit Wavetable Set", None))
        self.saveResourceSet.setText(QCoreApplication.translate("syncWavetableEditor", u"Save Set Data", None))
        self.saveForRack.setText(QCoreApplication.translate("syncWavetableEditor", u"Save for Rack", None))
        self.windowTitle_2.setText(QCoreApplication.translate("syncWavetableEditor", u"Select wavetable slot for editing:", None))
        self.slot1.setText(QCoreApplication.translate("syncWavetableEditor", u"I-1", None))
        self.slot2.setText(QCoreApplication.translate("syncWavetableEditor", u"I-2", None))
        self.slot3.setText(QCoreApplication.translate("syncWavetableEditor", u"I-3", None))
        self.slot4.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot5.setText(QCoreApplication.translate("syncWavetableEditor", u"II-1", None))
        self.slot6.setText(QCoreApplication.translate("syncWavetableEditor", u"II-2", None))
        self.slot7.setText(QCoreApplication.translate("syncWavetableEditor", u"II-3", None))
        self.slot8.setText(QCoreApplication.translate("syncWavetableEditor", u"II-4", None))
        self.slot9.setText(QCoreApplication.translate("syncWavetableEditor", u"I-1", None))
        self.slot10.setText(QCoreApplication.translate("syncWavetableEditor", u"I-2", None))
        self.slot11.setText(QCoreApplication.translate("syncWavetableEditor", u"I-3", None))
        self.slot12.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot13.setText(QCoreApplication.translate("syncWavetableEditor", u"II-1", None))
        self.slot14.setText(QCoreApplication.translate("syncWavetableEditor", u"II-2", None))
        self.slot15.setText(QCoreApplication.translate("syncWavetableEditor", u"II-3", None))
        self.slot16.setText(QCoreApplication.translate("syncWavetableEditor", u"II-4", None))
        self.slot17.setText(QCoreApplication.translate("syncWavetableEditor", u"I-1", None))
        self.slot18.setText(QCoreApplication.translate("syncWavetableEditor", u"I-2", None))
        self.slot19.setText(QCoreApplication.translate("syncWavetableEditor", u"I-3", None))
        self.slot20.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot21.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot22.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot23.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot24.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot25.setText(QCoreApplication.translate("syncWavetableEditor", u"Drum", None))
        self.tableName.setText(QCoreApplication.translate("syncWavetableEditor", u"TABLENAME", None))
        self.openBrowser.setText(QCoreApplication.translate("syncWavetableEditor", u"Browser", None))
        self.label.setText(QCoreApplication.translate("syncWavetableEditor", u"Visualizer", None))
    # retranslateUi

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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_syncWavetableEditor(object):
    def setupUi(self, syncWavetableEditor):
        if not syncWavetableEditor.objectName():
            syncWavetableEditor.setObjectName(u"syncWavetableEditor")
        syncWavetableEditor.resize(401, 669)
        self.layoutWidget = QWidget(syncWavetableEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 381, 651))
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

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot1 = QPushButton(self.layoutWidget)
        self.buttonGroup = QButtonGroup(syncWavetableEditor)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.slot1)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setMinimumSize(QSize(30, 0))
        self.slot1.setCheckable(True)

        self.slotGroup1.addWidget(self.slot1)

        self.slot2 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot2)
        self.slot2.setObjectName(u"slot2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy3)
        self.slot2.setMinimumSize(QSize(30, 0))
        self.slot2.setCheckable(True)

        self.slotGroup1.addWidget(self.slot2)

        self.slot3 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot3)
        self.slot3.setObjectName(u"slot3")
        sizePolicy3.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy3)
        self.slot3.setMinimumSize(QSize(30, 0))
        self.slot3.setCheckable(True)

        self.slotGroup1.addWidget(self.slot3)

        self.slot4 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot4)
        self.slot4.setObjectName(u"slot4")
        sizePolicy3.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy3)
        self.slot4.setMinimumSize(QSize(30, 0))
        self.slot4.setCheckable(True)

        self.slotGroup1.addWidget(self.slot4)

        self.slot5 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot5)
        self.slot5.setObjectName(u"slot5")
        sizePolicy3.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy3)
        self.slot5.setMinimumSize(QSize(30, 0))
        self.slot5.setCheckable(True)

        self.slotGroup1.addWidget(self.slot5)

        self.slot6 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot6)
        self.slot6.setObjectName(u"slot6")
        sizePolicy3.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy3)
        self.slot6.setMinimumSize(QSize(30, 0))
        self.slot6.setCheckable(True)

        self.slotGroup1.addWidget(self.slot6)

        self.slot7 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot7)
        self.slot7.setObjectName(u"slot7")
        sizePolicy3.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy3)
        self.slot7.setMinimumSize(QSize(30, 0))
        self.slot7.setCheckable(True)

        self.slotGroup1.addWidget(self.slot7)

        self.slot8 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot8)
        self.slot8.setObjectName(u"slot8")
        sizePolicy3.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy3)
        self.slot8.setMinimumSize(QSize(30, 0))
        self.slot8.setCheckable(True)

        self.slotGroup1.addWidget(self.slot8)


        self.verticalLayout.addLayout(self.slotGroup1)

        self.slotGroup2 = QHBoxLayout()
        self.slotGroup2.setObjectName(u"slotGroup2")
        self.slotGroup2.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot9 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot9)
        self.slot9.setObjectName(u"slot9")
        self.slot9.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot9.sizePolicy().hasHeightForWidth())
        self.slot9.setSizePolicy(sizePolicy2)
        self.slot9.setMinimumSize(QSize(30, 0))
        self.slot9.setCheckable(True)

        self.slotGroup2.addWidget(self.slot9)

        self.slot10 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot10)
        self.slot10.setObjectName(u"slot10")
        sizePolicy3.setHeightForWidth(self.slot10.sizePolicy().hasHeightForWidth())
        self.slot10.setSizePolicy(sizePolicy3)
        self.slot10.setMinimumSize(QSize(30, 0))
        self.slot10.setCheckable(True)

        self.slotGroup2.addWidget(self.slot10)

        self.slot11 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot11)
        self.slot11.setObjectName(u"slot11")
        sizePolicy3.setHeightForWidth(self.slot11.sizePolicy().hasHeightForWidth())
        self.slot11.setSizePolicy(sizePolicy3)
        self.slot11.setMinimumSize(QSize(30, 0))
        self.slot11.setCheckable(True)

        self.slotGroup2.addWidget(self.slot11)

        self.slot12 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot12)
        self.slot12.setObjectName(u"slot12")
        sizePolicy3.setHeightForWidth(self.slot12.sizePolicy().hasHeightForWidth())
        self.slot12.setSizePolicy(sizePolicy3)
        self.slot12.setMinimumSize(QSize(30, 0))
        self.slot12.setCheckable(True)

        self.slotGroup2.addWidget(self.slot12)

        self.slot13 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot13)
        self.slot13.setObjectName(u"slot13")
        sizePolicy3.setHeightForWidth(self.slot13.sizePolicy().hasHeightForWidth())
        self.slot13.setSizePolicy(sizePolicy3)
        self.slot13.setMinimumSize(QSize(30, 0))
        self.slot13.setCheckable(True)

        self.slotGroup2.addWidget(self.slot13)

        self.slot14 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot14)
        self.slot14.setObjectName(u"slot14")
        sizePolicy3.setHeightForWidth(self.slot14.sizePolicy().hasHeightForWidth())
        self.slot14.setSizePolicy(sizePolicy3)
        self.slot14.setMinimumSize(QSize(30, 0))
        self.slot14.setCheckable(True)

        self.slotGroup2.addWidget(self.slot14)

        self.slot15 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot15)
        self.slot15.setObjectName(u"slot15")
        sizePolicy3.setHeightForWidth(self.slot15.sizePolicy().hasHeightForWidth())
        self.slot15.setSizePolicy(sizePolicy3)
        self.slot15.setMinimumSize(QSize(30, 0))
        self.slot15.setCheckable(True)

        self.slotGroup2.addWidget(self.slot15)

        self.slot16 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot16)
        self.slot16.setObjectName(u"slot16")
        sizePolicy3.setHeightForWidth(self.slot16.sizePolicy().hasHeightForWidth())
        self.slot16.setSizePolicy(sizePolicy3)
        self.slot16.setMinimumSize(QSize(30, 0))
        self.slot16.setCheckable(True)

        self.slotGroup2.addWidget(self.slot16)


        self.verticalLayout.addLayout(self.slotGroup2)

        self.slotGroup3 = QHBoxLayout()
        self.slotGroup3.setObjectName(u"slotGroup3")
        self.slotGroup3.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot17 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot17)
        self.slot17.setObjectName(u"slot17")
        self.slot17.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot17.sizePolicy().hasHeightForWidth())
        self.slot17.setSizePolicy(sizePolicy2)
        self.slot17.setMinimumSize(QSize(30, 0))
        self.slot17.setCheckable(True)

        self.slotGroup3.addWidget(self.slot17)

        self.slot18 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot18)
        self.slot18.setObjectName(u"slot18")
        sizePolicy3.setHeightForWidth(self.slot18.sizePolicy().hasHeightForWidth())
        self.slot18.setSizePolicy(sizePolicy3)
        self.slot18.setMinimumSize(QSize(30, 0))
        self.slot18.setCheckable(True)

        self.slotGroup3.addWidget(self.slot18)

        self.slot19 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot19)
        self.slot19.setObjectName(u"slot19")
        sizePolicy3.setHeightForWidth(self.slot19.sizePolicy().hasHeightForWidth())
        self.slot19.setSizePolicy(sizePolicy3)
        self.slot19.setMinimumSize(QSize(30, 0))
        self.slot19.setCheckable(True)

        self.slotGroup3.addWidget(self.slot19)

        self.slot20 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot20)
        self.slot20.setObjectName(u"slot20")
        sizePolicy3.setHeightForWidth(self.slot20.sizePolicy().hasHeightForWidth())
        self.slot20.setSizePolicy(sizePolicy3)
        self.slot20.setMinimumSize(QSize(30, 0))
        self.slot20.setCheckable(True)

        self.slotGroup3.addWidget(self.slot20)

        self.slot21 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot21)
        self.slot21.setObjectName(u"slot21")
        sizePolicy3.setHeightForWidth(self.slot21.sizePolicy().hasHeightForWidth())
        self.slot21.setSizePolicy(sizePolicy3)
        self.slot21.setMinimumSize(QSize(30, 0))
        self.slot21.setCheckable(True)

        self.slotGroup3.addWidget(self.slot21)

        self.slot22 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot22)
        self.slot22.setObjectName(u"slot22")
        sizePolicy3.setHeightForWidth(self.slot22.sizePolicy().hasHeightForWidth())
        self.slot22.setSizePolicy(sizePolicy3)
        self.slot22.setMinimumSize(QSize(30, 0))
        self.slot22.setCheckable(True)

        self.slotGroup3.addWidget(self.slot22)

        self.slot23 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot23)
        self.slot23.setObjectName(u"slot23")
        sizePolicy3.setHeightForWidth(self.slot23.sizePolicy().hasHeightForWidth())
        self.slot23.setSizePolicy(sizePolicy3)
        self.slot23.setMinimumSize(QSize(30, 0))
        self.slot23.setCheckable(True)

        self.slotGroup3.addWidget(self.slot23)

        self.slot24 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot24)
        self.slot24.setObjectName(u"slot24")
        sizePolicy3.setHeightForWidth(self.slot24.sizePolicy().hasHeightForWidth())
        self.slot24.setSizePolicy(sizePolicy3)
        self.slot24.setMinimumSize(QSize(30, 0))
        self.slot24.setCheckable(True)

        self.slotGroup3.addWidget(self.slot24)


        self.verticalLayout.addLayout(self.slotGroup3)

        self.slotGroup3_2 = QHBoxLayout()
        self.slotGroup3_2.setObjectName(u"slotGroup3_2")
        self.slotGroup3_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot25 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot25)
        self.slot25.setObjectName(u"slot25")
        self.slot25.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot25.sizePolicy().hasHeightForWidth())
        self.slot25.setSizePolicy(sizePolicy2)
        self.slot25.setMinimumSize(QSize(30, 0))
        self.slot25.setCheckable(True)

        self.slotGroup3_2.addWidget(self.slot25)


        self.verticalLayout.addLayout(self.slotGroup3_2)

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
        self.displayType = QComboBox(self.layoutWidget)
        self.displayType.setObjectName(u"displayType")

        self.previewControls.addWidget(self.displayType)

        self.tableIndex = QSpinBox(self.layoutWidget)
        self.tableIndex.setObjectName(u"tableIndex")

        self.previewControls.addWidget(self.tableIndex)


        self.verticalLayout.addLayout(self.previewControls)

        self.tableViz = QVBoxLayout()
        self.tableViz.setObjectName(u"tableViz")
        self.vizSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tableViz.addItem(self.vizSpacer)


        self.verticalLayout.addLayout(self.tableViz)

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(syncWavetableEditor)
        self.buttonBox.rejected.connect(syncWavetableEditor.reject)
        self.buttonBox.accepted.connect(syncWavetableEditor.accept)

        QMetaObject.connectSlotsByName(syncWavetableEditor)
    # setupUi

    def retranslateUi(self, syncWavetableEditor):
        syncWavetableEditor.setWindowTitle(QCoreApplication.translate("syncWavetableEditor", u"Wavetable Set Editor", None))
        self.windowTitle.setText(QCoreApplication.translate("syncWavetableEditor", u"Edit Wavetable Set", None))
        self.saveResourceSet.setText(QCoreApplication.translate("syncWavetableEditor", u"Save Set Data", None))
        self.saveForRack.setText(QCoreApplication.translate("syncWavetableEditor", u"Save for Rack", None))
        self.windowTitle_2.setText(QCoreApplication.translate("syncWavetableEditor", u"Select wavetable slot for editing:", None))
        self.slot1.setText(QCoreApplication.translate("syncWavetableEditor", u"I-1", None))
        self.slot2.setText(QCoreApplication.translate("syncWavetableEditor", u"I-2", None))
        self.slot3.setText(QCoreApplication.translate("syncWavetableEditor", u"I-3", None))
        self.slot4.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot5.setText(QCoreApplication.translate("syncWavetableEditor", u"II-1", None))
        self.slot6.setText(QCoreApplication.translate("syncWavetableEditor", u"II-2", None))
        self.slot7.setText(QCoreApplication.translate("syncWavetableEditor", u"II-3", None))
        self.slot8.setText(QCoreApplication.translate("syncWavetableEditor", u"II-4", None))
        self.slot9.setText(QCoreApplication.translate("syncWavetableEditor", u"I-1", None))
        self.slot10.setText(QCoreApplication.translate("syncWavetableEditor", u"I-2", None))
        self.slot11.setText(QCoreApplication.translate("syncWavetableEditor", u"I-3", None))
        self.slot12.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot13.setText(QCoreApplication.translate("syncWavetableEditor", u"II-1", None))
        self.slot14.setText(QCoreApplication.translate("syncWavetableEditor", u"II-2", None))
        self.slot15.setText(QCoreApplication.translate("syncWavetableEditor", u"II-3", None))
        self.slot16.setText(QCoreApplication.translate("syncWavetableEditor", u"II-4", None))
        self.slot17.setText(QCoreApplication.translate("syncWavetableEditor", u"I-1", None))
        self.slot18.setText(QCoreApplication.translate("syncWavetableEditor", u"I-2", None))
        self.slot19.setText(QCoreApplication.translate("syncWavetableEditor", u"I-3", None))
        self.slot20.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot21.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot22.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot23.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot24.setText(QCoreApplication.translate("syncWavetableEditor", u"I-4", None))
        self.slot25.setText(QCoreApplication.translate("syncWavetableEditor", u"Drum", None))
        self.tableName.setText(QCoreApplication.translate("syncWavetableEditor", u"TABLENAME", None))
        self.openBrowser.setText(QCoreApplication.translate("syncWavetableEditor", u"Browser", None))
        self.label.setText(QCoreApplication.translate("syncWavetableEditor", u"Visualizer", None))
    # retranslateUi

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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_wavetableSetEditor(object):
    def setupUi(self, wavetableSetEditor):
        if not wavetableSetEditor.objectName():
            wavetableSetEditor.setObjectName(u"wavetableSetEditor")
        wavetableSetEditor.resize(401, 669)
        self.layoutWidget = QWidget(wavetableSetEditor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 381, 651))
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

        self.slotGroup1 = QHBoxLayout()
        self.slotGroup1.setObjectName(u"slotGroup1")
        self.slotGroup1.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot1 = QPushButton(self.layoutWidget)
        self.buttonGroup = QButtonGroup(wavetableSetEditor)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.slot1)
        self.slot1.setObjectName(u"slot1")
        self.slot1.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy2)
        self.slot1.setMinimumSize(QSize(30, 0))
        self.slot1.setCheckable(True)

        self.slotGroup1.addWidget(self.slot1)

        self.slot2 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot2)
        self.slot2.setObjectName(u"slot2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy3)
        self.slot2.setMinimumSize(QSize(30, 0))
        self.slot2.setCheckable(True)

        self.slotGroup1.addWidget(self.slot2)

        self.slot3 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot3)
        self.slot3.setObjectName(u"slot3")
        sizePolicy3.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy3)
        self.slot3.setMinimumSize(QSize(30, 0))
        self.slot3.setCheckable(True)

        self.slotGroup1.addWidget(self.slot3)

        self.slot4 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot4)
        self.slot4.setObjectName(u"slot4")
        sizePolicy3.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy3)
        self.slot4.setMinimumSize(QSize(30, 0))
        self.slot4.setCheckable(True)

        self.slotGroup1.addWidget(self.slot4)

        self.slot5 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot5)
        self.slot5.setObjectName(u"slot5")
        sizePolicy3.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy3)
        self.slot5.setMinimumSize(QSize(30, 0))
        self.slot5.setCheckable(True)

        self.slotGroup1.addWidget(self.slot5)

        self.slot6 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot6)
        self.slot6.setObjectName(u"slot6")
        sizePolicy3.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy3)
        self.slot6.setMinimumSize(QSize(30, 0))
        self.slot6.setCheckable(True)

        self.slotGroup1.addWidget(self.slot6)

        self.slot7 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot7)
        self.slot7.setObjectName(u"slot7")
        sizePolicy3.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy3)
        self.slot7.setMinimumSize(QSize(30, 0))
        self.slot7.setCheckable(True)

        self.slotGroup1.addWidget(self.slot7)

        self.slot8 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot8)
        self.slot8.setObjectName(u"slot8")
        sizePolicy3.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy3)
        self.slot8.setMinimumSize(QSize(30, 0))
        self.slot8.setCheckable(True)

        self.slotGroup1.addWidget(self.slot8)


        self.verticalLayout.addLayout(self.slotGroup1)

        self.slotGroup2 = QHBoxLayout()
        self.slotGroup2.setObjectName(u"slotGroup2")
        self.slotGroup2.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot9 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot9)
        self.slot9.setObjectName(u"slot9")
        self.slot9.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot9.sizePolicy().hasHeightForWidth())
        self.slot9.setSizePolicy(sizePolicy2)
        self.slot9.setMinimumSize(QSize(30, 0))
        self.slot9.setCheckable(True)

        self.slotGroup2.addWidget(self.slot9)

        self.slot10 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot10)
        self.slot10.setObjectName(u"slot10")
        sizePolicy3.setHeightForWidth(self.slot10.sizePolicy().hasHeightForWidth())
        self.slot10.setSizePolicy(sizePolicy3)
        self.slot10.setMinimumSize(QSize(30, 0))
        self.slot10.setCheckable(True)

        self.slotGroup2.addWidget(self.slot10)

        self.slot11 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot11)
        self.slot11.setObjectName(u"slot11")
        sizePolicy3.setHeightForWidth(self.slot11.sizePolicy().hasHeightForWidth())
        self.slot11.setSizePolicy(sizePolicy3)
        self.slot11.setMinimumSize(QSize(30, 0))
        self.slot11.setCheckable(True)

        self.slotGroup2.addWidget(self.slot11)

        self.slot12 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot12)
        self.slot12.setObjectName(u"slot12")
        sizePolicy3.setHeightForWidth(self.slot12.sizePolicy().hasHeightForWidth())
        self.slot12.setSizePolicy(sizePolicy3)
        self.slot12.setMinimumSize(QSize(30, 0))
        self.slot12.setCheckable(True)

        self.slotGroup2.addWidget(self.slot12)

        self.slot13 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot13)
        self.slot13.setObjectName(u"slot13")
        sizePolicy3.setHeightForWidth(self.slot13.sizePolicy().hasHeightForWidth())
        self.slot13.setSizePolicy(sizePolicy3)
        self.slot13.setMinimumSize(QSize(30, 0))
        self.slot13.setCheckable(True)

        self.slotGroup2.addWidget(self.slot13)

        self.slot14 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot14)
        self.slot14.setObjectName(u"slot14")
        sizePolicy3.setHeightForWidth(self.slot14.sizePolicy().hasHeightForWidth())
        self.slot14.setSizePolicy(sizePolicy3)
        self.slot14.setMinimumSize(QSize(30, 0))
        self.slot14.setCheckable(True)

        self.slotGroup2.addWidget(self.slot14)

        self.slot15 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot15)
        self.slot15.setObjectName(u"slot15")
        sizePolicy3.setHeightForWidth(self.slot15.sizePolicy().hasHeightForWidth())
        self.slot15.setSizePolicy(sizePolicy3)
        self.slot15.setMinimumSize(QSize(30, 0))
        self.slot15.setCheckable(True)

        self.slotGroup2.addWidget(self.slot15)

        self.slot16 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot16)
        self.slot16.setObjectName(u"slot16")
        sizePolicy3.setHeightForWidth(self.slot16.sizePolicy().hasHeightForWidth())
        self.slot16.setSizePolicy(sizePolicy3)
        self.slot16.setMinimumSize(QSize(30, 0))
        self.slot16.setCheckable(True)

        self.slotGroup2.addWidget(self.slot16)


        self.verticalLayout.addLayout(self.slotGroup2)

        self.slotGroup3 = QHBoxLayout()
        self.slotGroup3.setObjectName(u"slotGroup3")
        self.slotGroup3.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot17 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot17)
        self.slot17.setObjectName(u"slot17")
        self.slot17.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot17.sizePolicy().hasHeightForWidth())
        self.slot17.setSizePolicy(sizePolicy2)
        self.slot17.setMinimumSize(QSize(30, 0))
        self.slot17.setCheckable(True)

        self.slotGroup3.addWidget(self.slot17)

        self.slot18 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot18)
        self.slot18.setObjectName(u"slot18")
        sizePolicy3.setHeightForWidth(self.slot18.sizePolicy().hasHeightForWidth())
        self.slot18.setSizePolicy(sizePolicy3)
        self.slot18.setMinimumSize(QSize(30, 0))
        self.slot18.setCheckable(True)

        self.slotGroup3.addWidget(self.slot18)

        self.slot19 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot19)
        self.slot19.setObjectName(u"slot19")
        sizePolicy3.setHeightForWidth(self.slot19.sizePolicy().hasHeightForWidth())
        self.slot19.setSizePolicy(sizePolicy3)
        self.slot19.setMinimumSize(QSize(30, 0))
        self.slot19.setCheckable(True)

        self.slotGroup3.addWidget(self.slot19)

        self.slot20 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot20)
        self.slot20.setObjectName(u"slot20")
        sizePolicy3.setHeightForWidth(self.slot20.sizePolicy().hasHeightForWidth())
        self.slot20.setSizePolicy(sizePolicy3)
        self.slot20.setMinimumSize(QSize(30, 0))
        self.slot20.setCheckable(True)

        self.slotGroup3.addWidget(self.slot20)

        self.slot21 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot21)
        self.slot21.setObjectName(u"slot21")
        sizePolicy3.setHeightForWidth(self.slot21.sizePolicy().hasHeightForWidth())
        self.slot21.setSizePolicy(sizePolicy3)
        self.slot21.setMinimumSize(QSize(30, 0))
        self.slot21.setCheckable(True)

        self.slotGroup3.addWidget(self.slot21)

        self.slot22 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot22)
        self.slot22.setObjectName(u"slot22")
        sizePolicy3.setHeightForWidth(self.slot22.sizePolicy().hasHeightForWidth())
        self.slot22.setSizePolicy(sizePolicy3)
        self.slot22.setMinimumSize(QSize(30, 0))
        self.slot22.setCheckable(True)

        self.slotGroup3.addWidget(self.slot22)

        self.slot23 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot23)
        self.slot23.setObjectName(u"slot23")
        sizePolicy3.setHeightForWidth(self.slot23.sizePolicy().hasHeightForWidth())
        self.slot23.setSizePolicy(sizePolicy3)
        self.slot23.setMinimumSize(QSize(30, 0))
        self.slot23.setCheckable(True)

        self.slotGroup3.addWidget(self.slot23)

        self.slot24 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot24)
        self.slot24.setObjectName(u"slot24")
        sizePolicy3.setHeightForWidth(self.slot24.sizePolicy().hasHeightForWidth())
        self.slot24.setSizePolicy(sizePolicy3)
        self.slot24.setMinimumSize(QSize(30, 0))
        self.slot24.setCheckable(True)

        self.slotGroup3.addWidget(self.slot24)


        self.verticalLayout.addLayout(self.slotGroup3)

        self.slotGroup3_2 = QHBoxLayout()
        self.slotGroup3_2.setObjectName(u"slotGroup3_2")
        self.slotGroup3_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.slot25 = QPushButton(self.layoutWidget)
        self.buttonGroup.addButton(self.slot25)
        self.slot25.setObjectName(u"slot25")
        self.slot25.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.slot25.sizePolicy().hasHeightForWidth())
        self.slot25.setSizePolicy(sizePolicy2)
        self.slot25.setMinimumSize(QSize(30, 0))
        self.slot25.setCheckable(True)

        self.slotGroup3_2.addWidget(self.slot25)


        self.verticalLayout.addLayout(self.slotGroup3_2)

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
        self.displayType = QComboBox(self.layoutWidget)
        self.displayType.setObjectName(u"displayType")

        self.previewControls.addWidget(self.displayType)

        self.tableIndex = QSpinBox(self.layoutWidget)
        self.tableIndex.setObjectName(u"tableIndex")

        self.previewControls.addWidget(self.tableIndex)


        self.verticalLayout.addLayout(self.previewControls)

        self.tableViz = QVBoxLayout()
        self.tableViz.setObjectName(u"tableViz")
        self.vizSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tableViz.addItem(self.vizSpacer)


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
        self.slot1.setText(QCoreApplication.translate("wavetableSetEditor", u"I-1", None))
        self.slot2.setText(QCoreApplication.translate("wavetableSetEditor", u"I-2", None))
        self.slot3.setText(QCoreApplication.translate("wavetableSetEditor", u"I-3", None))
        self.slot4.setText(QCoreApplication.translate("wavetableSetEditor", u"I-4", None))
        self.slot5.setText(QCoreApplication.translate("wavetableSetEditor", u"II-1", None))
        self.slot6.setText(QCoreApplication.translate("wavetableSetEditor", u"II-2", None))
        self.slot7.setText(QCoreApplication.translate("wavetableSetEditor", u"II-3", None))
        self.slot8.setText(QCoreApplication.translate("wavetableSetEditor", u"II-4", None))
        self.slot9.setText(QCoreApplication.translate("wavetableSetEditor", u"I-1", None))
        self.slot10.setText(QCoreApplication.translate("wavetableSetEditor", u"I-2", None))
        self.slot11.setText(QCoreApplication.translate("wavetableSetEditor", u"I-3", None))
        self.slot12.setText(QCoreApplication.translate("wavetableSetEditor", u"I-4", None))
        self.slot13.setText(QCoreApplication.translate("wavetableSetEditor", u"II-1", None))
        self.slot14.setText(QCoreApplication.translate("wavetableSetEditor", u"II-2", None))
        self.slot15.setText(QCoreApplication.translate("wavetableSetEditor", u"II-3", None))
        self.slot16.setText(QCoreApplication.translate("wavetableSetEditor", u"II-4", None))
        self.slot17.setText(QCoreApplication.translate("wavetableSetEditor", u"I-1", None))
        self.slot18.setText(QCoreApplication.translate("wavetableSetEditor", u"I-2", None))
        self.slot19.setText(QCoreApplication.translate("wavetableSetEditor", u"I-3", None))
        self.slot20.setText(QCoreApplication.translate("wavetableSetEditor", u"I-4", None))
        self.slot21.setText(QCoreApplication.translate("wavetableSetEditor", u"I-4", None))
        self.slot22.setText(QCoreApplication.translate("wavetableSetEditor", u"I-4", None))
        self.slot23.setText(QCoreApplication.translate("wavetableSetEditor", u"I-4", None))
        self.slot24.setText(QCoreApplication.translate("wavetableSetEditor", u"I-4", None))
        self.slot25.setText(QCoreApplication.translate("wavetableSetEditor", u"Drum", None))
        self.tableName.setText(QCoreApplication.translate("wavetableSetEditor", u"TABLENAME", None))
        self.openBrowser.setText(QCoreApplication.translate("wavetableSetEditor", u"Browser", None))
        self.label.setText(QCoreApplication.translate("wavetableSetEditor", u"Visualizer", None))
    # retranslateUi

