# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanner_wavetable_editor.ui'
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
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 296)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.resourceSetSaveLoad = QHBoxLayout(self.horizontalLayoutWidget)
        self.resourceSetSaveLoad.setObjectName(u"resourceSetSaveLoad")
        self.resourceSetSaveLoad.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.resourceSetSaveLoad.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.resourceSetSaveLoad.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.resourceSetSaveLoad.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 200, 381, 41))
        self.resourceSaveLoad = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.resourceSaveLoad.setObjectName(u"resourceSaveLoad")
        self.resourceSaveLoad.setContentsMargins(0, 0, 0, 0)
        self.openBrowser = QPushButton(self.horizontalLayoutWidget_2)
        self.openBrowser.setObjectName(u"openBrowser")

        self.resourceSaveLoad.addWidget(self.openBrowser)

        self.openPreview = QPushButton(self.horizontalLayoutWidget_2)
        self.openPreview.setObjectName(u"openPreview")

        self.resourceSaveLoad.addWidget(self.openPreview)

        self.resourceSetSlots = QGroupBox(gateseqPatternEditor)
        self.resourceSetSlots.setObjectName(u"resourceSetSlots")
        self.resourceSetSlots.setGeometry(QRect(9, 100, 381, 51))
        self.layoutWidget = QWidget(self.resourceSetSlots)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 384, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.windowTitle = QLabel(gateseqPatternEditor)
        self.windowTitle.setObjectName(u"windowTitle")
        self.windowTitle.setGeometry(QRect(8, 10, 381, 20))
        self.windowTitle.setAlignment(Qt.AlignCenter)
        self.layoutWidget_2 = QWidget(gateseqPatternEditor)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 150, 384, 48))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.slot1layout_2 = QVBoxLayout()
        self.slot1layout_2.setObjectName(u"slot1layout_2")
        self.slot1layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.slot9 = QRadioButton(self.layoutWidget_2)
        self.slot9.setObjectName(u"slot9")
        sizePolicy.setHeightForWidth(self.slot9.sizePolicy().hasHeightForWidth())
        self.slot9.setSizePolicy(sizePolicy)
        self.slot9.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_11.addWidget(self.slot9)


        self.slot1layout_2.addLayout(self.horizontalLayout_11)

        self.label1_2 = QLabel(self.layoutWidget_2)
        self.label1_2.setObjectName(u"label1_2")
        self.label1_2.setAlignment(Qt.AlignCenter)

        self.slot1layout_2.addWidget(self.label1_2)


        self.horizontalLayout_6.addLayout(self.slot1layout_2)

        self.slot2layout_2 = QVBoxLayout()
        self.slot2layout_2.setObjectName(u"slot2layout_2")
        self.slot2layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.slot10 = QRadioButton(self.layoutWidget_2)
        self.slot10.setObjectName(u"slot10")
        sizePolicy.setHeightForWidth(self.slot10.sizePolicy().hasHeightForWidth())
        self.slot10.setSizePolicy(sizePolicy)
        self.slot10.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_12.addWidget(self.slot10)


        self.slot2layout_2.addLayout(self.horizontalLayout_12)

        self.label2_2 = QLabel(self.layoutWidget_2)
        self.label2_2.setObjectName(u"label2_2")
        self.label2_2.setAlignment(Qt.AlignCenter)

        self.slot2layout_2.addWidget(self.label2_2)


        self.horizontalLayout_6.addLayout(self.slot2layout_2)

        self.slot3layout_2 = QVBoxLayout()
        self.slot3layout_2.setObjectName(u"slot3layout_2")
        self.slot3layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.slot11 = QRadioButton(self.layoutWidget_2)
        self.slot11.setObjectName(u"slot11")
        sizePolicy.setHeightForWidth(self.slot11.sizePolicy().hasHeightForWidth())
        self.slot11.setSizePolicy(sizePolicy)
        self.slot11.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_13.addWidget(self.slot11)


        self.slot3layout_2.addLayout(self.horizontalLayout_13)

        self.label3_2 = QLabel(self.layoutWidget_2)
        self.label3_2.setObjectName(u"label3_2")
        self.label3_2.setAlignment(Qt.AlignCenter)

        self.slot3layout_2.addWidget(self.label3_2)


        self.horizontalLayout_6.addLayout(self.slot3layout_2)

        self.slot4layout_2 = QVBoxLayout()
        self.slot4layout_2.setObjectName(u"slot4layout_2")
        self.slot4layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.slot12 = QRadioButton(self.layoutWidget_2)
        self.slot12.setObjectName(u"slot12")
        sizePolicy.setHeightForWidth(self.slot12.sizePolicy().hasHeightForWidth())
        self.slot12.setSizePolicy(sizePolicy)
        self.slot12.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_14.addWidget(self.slot12)


        self.slot4layout_2.addLayout(self.horizontalLayout_14)

        self.label4_2 = QLabel(self.layoutWidget_2)
        self.label4_2.setObjectName(u"label4_2")
        self.label4_2.setAlignment(Qt.AlignCenter)

        self.slot4layout_2.addWidget(self.label4_2)


        self.horizontalLayout_6.addLayout(self.slot4layout_2)

        self.slot5layout_2 = QVBoxLayout()
        self.slot5layout_2.setObjectName(u"slot5layout_2")
        self.slot5layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.slot13 = QRadioButton(self.layoutWidget_2)
        self.slot13.setObjectName(u"slot13")
        sizePolicy.setHeightForWidth(self.slot13.sizePolicy().hasHeightForWidth())
        self.slot13.setSizePolicy(sizePolicy)
        self.slot13.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.slot13)


        self.slot5layout_2.addLayout(self.horizontalLayout_15)

        self.label5_2 = QLabel(self.layoutWidget_2)
        self.label5_2.setObjectName(u"label5_2")
        self.label5_2.setAlignment(Qt.AlignCenter)

        self.slot5layout_2.addWidget(self.label5_2)


        self.horizontalLayout_6.addLayout(self.slot5layout_2)

        self.slot6layout_2 = QVBoxLayout()
        self.slot6layout_2.setObjectName(u"slot6layout_2")
        self.slot6layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.slot14 = QRadioButton(self.layoutWidget_2)
        self.slot14.setObjectName(u"slot14")
        sizePolicy.setHeightForWidth(self.slot14.sizePolicy().hasHeightForWidth())
        self.slot14.setSizePolicy(sizePolicy)
        self.slot14.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.slot14)


        self.slot6layout_2.addLayout(self.horizontalLayout_16)

        self.label6_2 = QLabel(self.layoutWidget_2)
        self.label6_2.setObjectName(u"label6_2")
        self.label6_2.setAlignment(Qt.AlignCenter)

        self.slot6layout_2.addWidget(self.label6_2)


        self.horizontalLayout_6.addLayout(self.slot6layout_2)

        self.slot7layout_2 = QVBoxLayout()
        self.slot7layout_2.setObjectName(u"slot7layout_2")
        self.slot7layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.slot15 = QRadioButton(self.layoutWidget_2)
        self.slot15.setObjectName(u"slot15")
        sizePolicy.setHeightForWidth(self.slot15.sizePolicy().hasHeightForWidth())
        self.slot15.setSizePolicy(sizePolicy)
        self.slot15.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_17.addWidget(self.slot15)


        self.slot7layout_2.addLayout(self.horizontalLayout_17)

        self.label7_2 = QLabel(self.layoutWidget_2)
        self.label7_2.setObjectName(u"label7_2")
        self.label7_2.setAlignment(Qt.AlignCenter)

        self.slot7layout_2.addWidget(self.label7_2)


        self.horizontalLayout_6.addLayout(self.slot7layout_2)

        self.slot8layout_2 = QVBoxLayout()
        self.slot8layout_2.setObjectName(u"slot8layout_2")
        self.slot8layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.slot16 = QRadioButton(self.layoutWidget_2)
        self.slot16.setObjectName(u"slot16")
        sizePolicy.setHeightForWidth(self.slot16.sizePolicy().hasHeightForWidth())
        self.slot16.setSizePolicy(sizePolicy)
        self.slot16.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_18.addWidget(self.slot16)


        self.slot8layout_2.addLayout(self.horizontalLayout_18)

        self.label8_2 = QLabel(self.layoutWidget_2)
        self.label8_2.setObjectName(u"label8_2")
        self.label8_2.setAlignment(Qt.AlignCenter)

        self.slot8layout_2.addWidget(self.label8_2)


        self.horizontalLayout_6.addLayout(self.slot8layout_2)

        self.windowTitle_2 = QLabel(gateseqPatternEditor)
        self.windowTitle_2.setObjectName(u"windowTitle_2")
        self.windowTitle_2.setGeometry(QRect(10, 80, 381, 20))
        self.windowTitle_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Set Data", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.openBrowser.setText(QCoreApplication.translate("gateseqPatternEditor", u"Browser", None))
        self.openPreview.setText(QCoreApplication.translate("gateseqPatternEditor", u"Preview", None))
        self.resourceSetSlots.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-8", None))
        self.windowTitle.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Wavetable Set", None))
        self.slot9.setText("")
        self.label1_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-1", None))
        self.slot10.setText("")
        self.label2_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-2", None))
        self.slot11.setText("")
        self.label3_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-3", None))
        self.slot12.setText("")
        self.label4_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-4", None))
        self.slot13.setText("")
        self.label5_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-5", None))
        self.slot14.setText("")
        self.label6_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-6", None))
        self.slot15.setText("")
        self.label7_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-7", None))
        self.slot16.setText("")
        self.label8_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-8", None))
        self.windowTitle_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Select wavetable slot for editing:", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanner_wavetable_editor.ui'
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
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 296)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 250, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.resourceSetSaveLoad = QHBoxLayout(self.horizontalLayoutWidget)
        self.resourceSetSaveLoad.setObjectName(u"resourceSetSaveLoad")
        self.resourceSetSaveLoad.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.resourceSetSaveLoad.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.resourceSetSaveLoad.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.resourceSetSaveLoad.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 200, 381, 41))
        self.resourceSaveLoad = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.resourceSaveLoad.setObjectName(u"resourceSaveLoad")
        self.resourceSaveLoad.setContentsMargins(0, 0, 0, 0)
        self.openBrowser = QPushButton(self.horizontalLayoutWidget_2)
        self.openBrowser.setObjectName(u"openBrowser")

        self.resourceSaveLoad.addWidget(self.openBrowser)

        self.openPreview = QPushButton(self.horizontalLayoutWidget_2)
        self.openPreview.setObjectName(u"openPreview")

        self.resourceSaveLoad.addWidget(self.openPreview)

        self.resourceSetSlots = QGroupBox(gateseqPatternEditor)
        self.resourceSetSlots.setObjectName(u"resourceSetSlots")
        self.resourceSetSlots.setGeometry(QRect(9, 100, 381, 51))
        self.layoutWidget = QWidget(self.resourceSetSlots)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 384, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.windowTitle = QLabel(gateseqPatternEditor)
        self.windowTitle.setObjectName(u"windowTitle")
        self.windowTitle.setGeometry(QRect(8, 10, 381, 20))
        self.windowTitle.setAlignment(Qt.AlignCenter)
        self.layoutWidget_2 = QWidget(gateseqPatternEditor)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 150, 384, 48))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.slot1layout_2 = QVBoxLayout()
        self.slot1layout_2.setObjectName(u"slot1layout_2")
        self.slot1layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.slot9 = QRadioButton(self.layoutWidget_2)
        self.slot9.setObjectName(u"slot9")
        sizePolicy.setHeightForWidth(self.slot9.sizePolicy().hasHeightForWidth())
        self.slot9.setSizePolicy(sizePolicy)
        self.slot9.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_11.addWidget(self.slot9)


        self.slot1layout_2.addLayout(self.horizontalLayout_11)

        self.label1_2 = QLabel(self.layoutWidget_2)
        self.label1_2.setObjectName(u"label1_2")
        self.label1_2.setAlignment(Qt.AlignCenter)

        self.slot1layout_2.addWidget(self.label1_2)


        self.horizontalLayout_6.addLayout(self.slot1layout_2)

        self.slot2layout_2 = QVBoxLayout()
        self.slot2layout_2.setObjectName(u"slot2layout_2")
        self.slot2layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.slot10 = QRadioButton(self.layoutWidget_2)
        self.slot10.setObjectName(u"slot10")
        sizePolicy.setHeightForWidth(self.slot10.sizePolicy().hasHeightForWidth())
        self.slot10.setSizePolicy(sizePolicy)
        self.slot10.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_12.addWidget(self.slot10)


        self.slot2layout_2.addLayout(self.horizontalLayout_12)

        self.label2_2 = QLabel(self.layoutWidget_2)
        self.label2_2.setObjectName(u"label2_2")
        self.label2_2.setAlignment(Qt.AlignCenter)

        self.slot2layout_2.addWidget(self.label2_2)


        self.horizontalLayout_6.addLayout(self.slot2layout_2)

        self.slot3layout_2 = QVBoxLayout()
        self.slot3layout_2.setObjectName(u"slot3layout_2")
        self.slot3layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.slot11 = QRadioButton(self.layoutWidget_2)
        self.slot11.setObjectName(u"slot11")
        sizePolicy.setHeightForWidth(self.slot11.sizePolicy().hasHeightForWidth())
        self.slot11.setSizePolicy(sizePolicy)
        self.slot11.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_13.addWidget(self.slot11)


        self.slot3layout_2.addLayout(self.horizontalLayout_13)

        self.label3_2 = QLabel(self.layoutWidget_2)
        self.label3_2.setObjectName(u"label3_2")
        self.label3_2.setAlignment(Qt.AlignCenter)

        self.slot3layout_2.addWidget(self.label3_2)


        self.horizontalLayout_6.addLayout(self.slot3layout_2)

        self.slot4layout_2 = QVBoxLayout()
        self.slot4layout_2.setObjectName(u"slot4layout_2")
        self.slot4layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.slot12 = QRadioButton(self.layoutWidget_2)
        self.slot12.setObjectName(u"slot12")
        sizePolicy.setHeightForWidth(self.slot12.sizePolicy().hasHeightForWidth())
        self.slot12.setSizePolicy(sizePolicy)
        self.slot12.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_14.addWidget(self.slot12)


        self.slot4layout_2.addLayout(self.horizontalLayout_14)

        self.label4_2 = QLabel(self.layoutWidget_2)
        self.label4_2.setObjectName(u"label4_2")
        self.label4_2.setAlignment(Qt.AlignCenter)

        self.slot4layout_2.addWidget(self.label4_2)


        self.horizontalLayout_6.addLayout(self.slot4layout_2)

        self.slot5layout_2 = QVBoxLayout()
        self.slot5layout_2.setObjectName(u"slot5layout_2")
        self.slot5layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.slot13 = QRadioButton(self.layoutWidget_2)
        self.slot13.setObjectName(u"slot13")
        sizePolicy.setHeightForWidth(self.slot13.sizePolicy().hasHeightForWidth())
        self.slot13.setSizePolicy(sizePolicy)
        self.slot13.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.slot13)


        self.slot5layout_2.addLayout(self.horizontalLayout_15)

        self.label5_2 = QLabel(self.layoutWidget_2)
        self.label5_2.setObjectName(u"label5_2")
        self.label5_2.setAlignment(Qt.AlignCenter)

        self.slot5layout_2.addWidget(self.label5_2)


        self.horizontalLayout_6.addLayout(self.slot5layout_2)

        self.slot6layout_2 = QVBoxLayout()
        self.slot6layout_2.setObjectName(u"slot6layout_2")
        self.slot6layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.slot14 = QRadioButton(self.layoutWidget_2)
        self.slot14.setObjectName(u"slot14")
        sizePolicy.setHeightForWidth(self.slot14.sizePolicy().hasHeightForWidth())
        self.slot14.setSizePolicy(sizePolicy)
        self.slot14.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.slot14)


        self.slot6layout_2.addLayout(self.horizontalLayout_16)

        self.label6_2 = QLabel(self.layoutWidget_2)
        self.label6_2.setObjectName(u"label6_2")
        self.label6_2.setAlignment(Qt.AlignCenter)

        self.slot6layout_2.addWidget(self.label6_2)


        self.horizontalLayout_6.addLayout(self.slot6layout_2)

        self.slot7layout_2 = QVBoxLayout()
        self.slot7layout_2.setObjectName(u"slot7layout_2")
        self.slot7layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.slot15 = QRadioButton(self.layoutWidget_2)
        self.slot15.setObjectName(u"slot15")
        sizePolicy.setHeightForWidth(self.slot15.sizePolicy().hasHeightForWidth())
        self.slot15.setSizePolicy(sizePolicy)
        self.slot15.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_17.addWidget(self.slot15)


        self.slot7layout_2.addLayout(self.horizontalLayout_17)

        self.label7_2 = QLabel(self.layoutWidget_2)
        self.label7_2.setObjectName(u"label7_2")
        self.label7_2.setAlignment(Qt.AlignCenter)

        self.slot7layout_2.addWidget(self.label7_2)


        self.horizontalLayout_6.addLayout(self.slot7layout_2)

        self.slot8layout_2 = QVBoxLayout()
        self.slot8layout_2.setObjectName(u"slot8layout_2")
        self.slot8layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.slot16 = QRadioButton(self.layoutWidget_2)
        self.slot16.setObjectName(u"slot16")
        sizePolicy.setHeightForWidth(self.slot16.sizePolicy().hasHeightForWidth())
        self.slot16.setSizePolicy(sizePolicy)
        self.slot16.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_18.addWidget(self.slot16)


        self.slot8layout_2.addLayout(self.horizontalLayout_18)

        self.label8_2 = QLabel(self.layoutWidget_2)
        self.label8_2.setObjectName(u"label8_2")
        self.label8_2.setAlignment(Qt.AlignCenter)

        self.slot8layout_2.addWidget(self.label8_2)


        self.horizontalLayout_6.addLayout(self.slot8layout_2)

        self.windowTitle_2 = QLabel(gateseqPatternEditor)
        self.windowTitle_2.setObjectName(u"windowTitle_2")
        self.windowTitle_2.setGeometry(QRect(10, 80, 381, 20))
        self.windowTitle_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Set Data", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.openBrowser.setText(QCoreApplication.translate("gateseqPatternEditor", u"Browser", None))
        self.openPreview.setText(QCoreApplication.translate("gateseqPatternEditor", u"Preview", None))
        self.resourceSetSlots.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"X-8", None))
        self.windowTitle.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Wavetable Set", None))
        self.slot9.setText("")
        self.label1_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-1", None))
        self.slot10.setText("")
        self.label2_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-2", None))
        self.slot11.setText("")
        self.label3_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-3", None))
        self.slot12.setText("")
        self.label4_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-4", None))
        self.slot13.setText("")
        self.label5_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-5", None))
        self.slot14.setText("")
        self.label6_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-6", None))
        self.slot15.setText("")
        self.label7_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-7", None))
        self.slot16.setText("")
        self.label8_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Y-8", None))
        self.windowTitle_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Select wavetable slot for editing:", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scanner_wavetable_editor.ui'
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
    QDialogButtonBox, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_scannerWavetableEditor(object):
    def setupUi(self, scannerWavetableEditor):
        if not scannerWavetableEditor.objectName():
            scannerWavetableEditor.setObjectName(u"scannerWavetableEditor")
        scannerWavetableEditor.resize(400, 321)
        self.buttonBox = QDialogButtonBox(scannerWavetableEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 280, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(scannerWavetableEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.resourceSetSaveLoad = QHBoxLayout(self.horizontalLayoutWidget)
        self.resourceSetSaveLoad.setObjectName(u"resourceSetSaveLoad")
        self.resourceSetSaveLoad.setContentsMargins(0, 0, 0, 0)
        self.selectResourceSet = QComboBox(self.horizontalLayoutWidget)
        self.selectResourceSet.setObjectName(u"selectResourceSet")

        self.resourceSetSaveLoad.addWidget(self.selectResourceSet)

        self.saveResourceSet = QPushButton(self.horizontalLayoutWidget)
        self.saveResourceSet.setObjectName(u"saveResourceSet")

        self.resourceSetSaveLoad.addWidget(self.saveResourceSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.resourceSetSaveLoad.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(scannerWavetableEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 220, 381, 41))
        self.resourceSaveLoad = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.resourceSaveLoad.setObjectName(u"resourceSaveLoad")
        self.resourceSaveLoad.setContentsMargins(0, 0, 0, 0)
        self.openBrowser = QPushButton(self.horizontalLayoutWidget_2)
        self.openBrowser.setObjectName(u"openBrowser")

        self.resourceSaveLoad.addWidget(self.openBrowser)

        self.openPreview = QPushButton(self.horizontalLayoutWidget_2)
        self.openPreview.setObjectName(u"openPreview")

        self.resourceSaveLoad.addWidget(self.openPreview)

        self.resourceSetSlots = QGroupBox(scannerWavetableEditor)
        self.resourceSetSlots.setObjectName(u"resourceSetSlots")
        self.resourceSetSlots.setGeometry(QRect(9, 100, 381, 51))
        self.layoutWidget = QWidget(self.resourceSetSlots)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 384, 48))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slot1layout = QVBoxLayout()
        self.slot1layout.setObjectName(u"slot1layout")
        self.slot1layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.slot1 = QRadioButton(self.layoutWidget)
        self.slot1.setObjectName(u"slot1")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy)
        self.slot1.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.slot1)


        self.slot1layout.addLayout(self.horizontalLayout_2)

        self.label1 = QLabel(self.layoutWidget)
        self.label1.setObjectName(u"label1")
        self.label1.setAlignment(Qt.AlignCenter)

        self.slot1layout.addWidget(self.label1)


        self.horizontalLayout.addLayout(self.slot1layout)

        self.slot2layout = QVBoxLayout()
        self.slot2layout.setObjectName(u"slot2layout")
        self.slot2layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.slot2 = QRadioButton(self.layoutWidget)
        self.slot2.setObjectName(u"slot2")
        sizePolicy.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy)
        self.slot2.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.slot2)


        self.slot2layout.addLayout(self.horizontalLayout_3)

        self.label2 = QLabel(self.layoutWidget)
        self.label2.setObjectName(u"label2")
        self.label2.setAlignment(Qt.AlignCenter)

        self.slot2layout.addWidget(self.label2)


        self.horizontalLayout.addLayout(self.slot2layout)

        self.slot3layout = QVBoxLayout()
        self.slot3layout.setObjectName(u"slot3layout")
        self.slot3layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.slot3 = QRadioButton(self.layoutWidget)
        self.slot3.setObjectName(u"slot3")
        sizePolicy.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy)
        self.slot3.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.slot3)


        self.slot3layout.addLayout(self.horizontalLayout_4)

        self.label3 = QLabel(self.layoutWidget)
        self.label3.setObjectName(u"label3")
        self.label3.setAlignment(Qt.AlignCenter)

        self.slot3layout.addWidget(self.label3)


        self.horizontalLayout.addLayout(self.slot3layout)

        self.slot4layout = QVBoxLayout()
        self.slot4layout.setObjectName(u"slot4layout")
        self.slot4layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.slot4 = QRadioButton(self.layoutWidget)
        self.slot4.setObjectName(u"slot4")
        sizePolicy.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy)
        self.slot4.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.slot4)


        self.slot4layout.addLayout(self.horizontalLayout_5)

        self.label4 = QLabel(self.layoutWidget)
        self.label4.setObjectName(u"label4")
        self.label4.setAlignment(Qt.AlignCenter)

        self.slot4layout.addWidget(self.label4)


        self.horizontalLayout.addLayout(self.slot4layout)

        self.slot5layout = QVBoxLayout()
        self.slot5layout.setObjectName(u"slot5layout")
        self.slot5layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.slot5 = QRadioButton(self.layoutWidget)
        self.slot5.setObjectName(u"slot5")
        sizePolicy.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy)
        self.slot5.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.slot5)


        self.slot5layout.addLayout(self.horizontalLayout_7)

        self.label5 = QLabel(self.layoutWidget)
        self.label5.setObjectName(u"label5")
        self.label5.setAlignment(Qt.AlignCenter)

        self.slot5layout.addWidget(self.label5)


        self.horizontalLayout.addLayout(self.slot5layout)

        self.slot6layout = QVBoxLayout()
        self.slot6layout.setObjectName(u"slot6layout")
        self.slot6layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.slot6 = QRadioButton(self.layoutWidget)
        self.slot6.setObjectName(u"slot6")
        sizePolicy.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy)
        self.slot6.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_8.addWidget(self.slot6)


        self.slot6layout.addLayout(self.horizontalLayout_8)

        self.label6 = QLabel(self.layoutWidget)
        self.label6.setObjectName(u"label6")
        self.label6.setAlignment(Qt.AlignCenter)

        self.slot6layout.addWidget(self.label6)


        self.horizontalLayout.addLayout(self.slot6layout)

        self.slot7layout = QVBoxLayout()
        self.slot7layout.setObjectName(u"slot7layout")
        self.slot7layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.slot7 = QRadioButton(self.layoutWidget)
        self.slot7.setObjectName(u"slot7")
        sizePolicy.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy)
        self.slot7.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_9.addWidget(self.slot7)


        self.slot7layout.addLayout(self.horizontalLayout_9)

        self.label7 = QLabel(self.layoutWidget)
        self.label7.setObjectName(u"label7")
        self.label7.setAlignment(Qt.AlignCenter)

        self.slot7layout.addWidget(self.label7)


        self.horizontalLayout.addLayout(self.slot7layout)

        self.slot8layout = QVBoxLayout()
        self.slot8layout.setObjectName(u"slot8layout")
        self.slot8layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.slot8 = QRadioButton(self.layoutWidget)
        self.slot8.setObjectName(u"slot8")
        sizePolicy.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.windowTitle = QLabel(scannerWavetableEditor)
        self.windowTitle.setObjectName(u"windowTitle")
        self.windowTitle.setGeometry(QRect(8, 10, 381, 20))
        self.windowTitle.setAlignment(Qt.AlignCenter)
        self.layoutWidget_2 = QWidget(scannerWavetableEditor)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 150, 384, 48))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.slot1layout_2 = QVBoxLayout()
        self.slot1layout_2.setObjectName(u"slot1layout_2")
        self.slot1layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.slot9 = QRadioButton(self.layoutWidget_2)
        self.slot9.setObjectName(u"slot9")
        sizePolicy.setHeightForWidth(self.slot9.sizePolicy().hasHeightForWidth())
        self.slot9.setSizePolicy(sizePolicy)
        self.slot9.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_11.addWidget(self.slot9)


        self.slot1layout_2.addLayout(self.horizontalLayout_11)

        self.label1_2 = QLabel(self.layoutWidget_2)
        self.label1_2.setObjectName(u"label1_2")
        self.label1_2.setAlignment(Qt.AlignCenter)

        self.slot1layout_2.addWidget(self.label1_2)


        self.horizontalLayout_6.addLayout(self.slot1layout_2)

        self.slot2layout_2 = QVBoxLayout()
        self.slot2layout_2.setObjectName(u"slot2layout_2")
        self.slot2layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.slot10 = QRadioButton(self.layoutWidget_2)
        self.slot10.setObjectName(u"slot10")
        sizePolicy.setHeightForWidth(self.slot10.sizePolicy().hasHeightForWidth())
        self.slot10.setSizePolicy(sizePolicy)
        self.slot10.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_12.addWidget(self.slot10)


        self.slot2layout_2.addLayout(self.horizontalLayout_12)

        self.label2_2 = QLabel(self.layoutWidget_2)
        self.label2_2.setObjectName(u"label2_2")
        self.label2_2.setAlignment(Qt.AlignCenter)

        self.slot2layout_2.addWidget(self.label2_2)


        self.horizontalLayout_6.addLayout(self.slot2layout_2)

        self.slot3layout_2 = QVBoxLayout()
        self.slot3layout_2.setObjectName(u"slot3layout_2")
        self.slot3layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.slot11 = QRadioButton(self.layoutWidget_2)
        self.slot11.setObjectName(u"slot11")
        sizePolicy.setHeightForWidth(self.slot11.sizePolicy().hasHeightForWidth())
        self.slot11.setSizePolicy(sizePolicy)
        self.slot11.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_13.addWidget(self.slot11)


        self.slot3layout_2.addLayout(self.horizontalLayout_13)

        self.label3_2 = QLabel(self.layoutWidget_2)
        self.label3_2.setObjectName(u"label3_2")
        self.label3_2.setAlignment(Qt.AlignCenter)

        self.slot3layout_2.addWidget(self.label3_2)


        self.horizontalLayout_6.addLayout(self.slot3layout_2)

        self.slot4layout_2 = QVBoxLayout()
        self.slot4layout_2.setObjectName(u"slot4layout_2")
        self.slot4layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.slot12 = QRadioButton(self.layoutWidget_2)
        self.slot12.setObjectName(u"slot12")
        sizePolicy.setHeightForWidth(self.slot12.sizePolicy().hasHeightForWidth())
        self.slot12.setSizePolicy(sizePolicy)
        self.slot12.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_14.addWidget(self.slot12)


        self.slot4layout_2.addLayout(self.horizontalLayout_14)

        self.label4_2 = QLabel(self.layoutWidget_2)
        self.label4_2.setObjectName(u"label4_2")
        self.label4_2.setAlignment(Qt.AlignCenter)

        self.slot4layout_2.addWidget(self.label4_2)


        self.horizontalLayout_6.addLayout(self.slot4layout_2)

        self.slot5layout_2 = QVBoxLayout()
        self.slot5layout_2.setObjectName(u"slot5layout_2")
        self.slot5layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.slot13 = QRadioButton(self.layoutWidget_2)
        self.slot13.setObjectName(u"slot13")
        sizePolicy.setHeightForWidth(self.slot13.sizePolicy().hasHeightForWidth())
        self.slot13.setSizePolicy(sizePolicy)
        self.slot13.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_15.addWidget(self.slot13)


        self.slot5layout_2.addLayout(self.horizontalLayout_15)

        self.label5_2 = QLabel(self.layoutWidget_2)
        self.label5_2.setObjectName(u"label5_2")
        self.label5_2.setAlignment(Qt.AlignCenter)

        self.slot5layout_2.addWidget(self.label5_2)


        self.horizontalLayout_6.addLayout(self.slot5layout_2)

        self.slot6layout_2 = QVBoxLayout()
        self.slot6layout_2.setObjectName(u"slot6layout_2")
        self.slot6layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.slot14 = QRadioButton(self.layoutWidget_2)
        self.slot14.setObjectName(u"slot14")
        sizePolicy.setHeightForWidth(self.slot14.sizePolicy().hasHeightForWidth())
        self.slot14.setSizePolicy(sizePolicy)
        self.slot14.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_16.addWidget(self.slot14)


        self.slot6layout_2.addLayout(self.horizontalLayout_16)

        self.label6_2 = QLabel(self.layoutWidget_2)
        self.label6_2.setObjectName(u"label6_2")
        self.label6_2.setAlignment(Qt.AlignCenter)

        self.slot6layout_2.addWidget(self.label6_2)


        self.horizontalLayout_6.addLayout(self.slot6layout_2)

        self.slot7layout_2 = QVBoxLayout()
        self.slot7layout_2.setObjectName(u"slot7layout_2")
        self.slot7layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.slot15 = QRadioButton(self.layoutWidget_2)
        self.slot15.setObjectName(u"slot15")
        sizePolicy.setHeightForWidth(self.slot15.sizePolicy().hasHeightForWidth())
        self.slot15.setSizePolicy(sizePolicy)
        self.slot15.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_17.addWidget(self.slot15)


        self.slot7layout_2.addLayout(self.horizontalLayout_17)

        self.label7_2 = QLabel(self.layoutWidget_2)
        self.label7_2.setObjectName(u"label7_2")
        self.label7_2.setAlignment(Qt.AlignCenter)

        self.slot7layout_2.addWidget(self.label7_2)


        self.horizontalLayout_6.addLayout(self.slot7layout_2)

        self.slot8layout_2 = QVBoxLayout()
        self.slot8layout_2.setObjectName(u"slot8layout_2")
        self.slot8layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.slot16 = QRadioButton(self.layoutWidget_2)
        self.slot16.setObjectName(u"slot16")
        sizePolicy.setHeightForWidth(self.slot16.sizePolicy().hasHeightForWidth())
        self.slot16.setSizePolicy(sizePolicy)
        self.slot16.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_18.addWidget(self.slot16)


        self.slot8layout_2.addLayout(self.horizontalLayout_18)

        self.label8_2 = QLabel(self.layoutWidget_2)
        self.label8_2.setObjectName(u"label8_2")
        self.label8_2.setAlignment(Qt.AlignCenter)

        self.slot8layout_2.addWidget(self.label8_2)


        self.horizontalLayout_6.addLayout(self.slot8layout_2)

        self.windowTitle_2 = QLabel(scannerWavetableEditor)
        self.windowTitle_2.setObjectName(u"windowTitle_2")
        self.windowTitle_2.setGeometry(QRect(10, 80, 381, 20))
        self.windowTitle_2.setAlignment(Qt.AlignCenter)
        self.tableName = QLabel(scannerWavetableEditor)
        self.tableName.setObjectName(u"tableName")
        self.tableName.setGeometry(QRect(10, 200, 381, 20))
        self.tableName.setAlignment(Qt.AlignCenter)

        self.retranslateUi(scannerWavetableEditor)
        self.buttonBox.accepted.connect(scannerWavetableEditor.accept)
        self.buttonBox.rejected.connect(scannerWavetableEditor.reject)

        QMetaObject.connectSlotsByName(scannerWavetableEditor)
    # setupUi

    def retranslateUi(self, scannerWavetableEditor):
        scannerWavetableEditor.setWindowTitle(QCoreApplication.translate("scannerWavetableEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("scannerWavetableEditor", u"Save Set Data", None))
        self.saveForRack.setText(QCoreApplication.translate("scannerWavetableEditor", u"Save for Rack", None))
        self.openBrowser.setText(QCoreApplication.translate("scannerWavetableEditor", u"Browser", None))
        self.openPreview.setText(QCoreApplication.translate("scannerWavetableEditor", u"Preview", None))
        self.resourceSetSlots.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-5", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-6", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-7", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("scannerWavetableEditor", u"X-8", None))
        self.windowTitle.setText(QCoreApplication.translate("scannerWavetableEditor", u"Edit Wavetable Set", None))
        self.slot9.setText("")
        self.label1_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-1", None))
        self.slot10.setText("")
        self.label2_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-2", None))
        self.slot11.setText("")
        self.label3_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-3", None))
        self.slot12.setText("")
        self.label4_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-4", None))
        self.slot13.setText("")
        self.label5_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-5", None))
        self.slot14.setText("")
        self.label6_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-6", None))
        self.slot15.setText("")
        self.label7_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-7", None))
        self.slot16.setText("")
        self.label8_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Y-8", None))
        self.windowTitle_2.setText(QCoreApplication.translate("scannerWavetableEditor", u"Select wavetable slot for editing:", None))
        self.tableName.setText(QCoreApplication.translate("scannerWavetableEditor", u"TABLENAME", None))
    # retranslateUi

