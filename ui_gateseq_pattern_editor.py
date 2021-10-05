# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 603)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 560, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectPatternSet = QComboBox(self.horizontalLayoutWidget)
        self.selectPatternSet.setObjectName(u"selectPatternSet")

        self.scalesSetButtons.addWidget(self.selectPatternSet)

        self.savePatternSet = QPushButton(self.horizontalLayoutWidget)
        self.savePatternSet.setObjectName(u"savePatternSet")

        self.scalesSetButtons.addWidget(self.savePatternSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadPattern = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadPattern.setObjectName(u"saveLoadPattern")
        self.saveLoadPattern.setContentsMargins(0, 0, 0, 0)
        self.selectPattern = QComboBox(self.horizontalLayoutWidget_2)
        self.selectPattern.setObjectName(u"selectPattern")

        self.saveLoadPattern.addWidget(self.selectPattern)

        self.savePattern = QPushButton(self.horizontalLayoutWidget_2)
        self.savePattern.setObjectName(u"savePattern")

        self.saveLoadPattern.addWidget(self.savePattern)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 169, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.seedRatioEditor.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(1)
        self.steps.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(1)
        self.length.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.length)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.seedRatioEditor.addLayout(self.verticalLayout_8)

        self.groupBox_2 = QGroupBox(gateseqPatternEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 60, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(1, 0, 381, 48))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 230, 381, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.horizontalLayout_6.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.horizontalLayout_6.addWidget(self.addText)

        self.clearPatterns = QPushButton(self.horizontalLayoutWidget_3)
        self.clearPatterns.setObjectName(u"clearPatterns")

        self.horizontalLayout_6.addWidget(self.clearPatterns)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 309, 388, 244))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2_2 = QPushButton(self.gridLayoutWidget)
        self.sequence2_2.setObjectName(u"sequence2_2")

        self.verticalLayout_4.addWidget(self.sequence2_2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.horizontalLayoutWidget_4 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(9, 279, 381, 31))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label)


        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.savePatternSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.savePattern.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearPatterns.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.label.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequences:", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectPatternSet = QComboBox(self.horizontalLayoutWidget)
        self.selectPatternSet.setObjectName(u"selectPatternSet")

        self.scalesSetButtons.addWidget(self.selectPatternSet)

        self.savePatternSet = QPushButton(self.horizontalLayoutWidget)
        self.savePatternSet.setObjectName(u"savePatternSet")

        self.scalesSetButtons.addWidget(self.savePatternSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadPattern = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadPattern.setObjectName(u"saveLoadPattern")
        self.saveLoadPattern.setContentsMargins(0, 0, 0, 0)
        self.selectPattern = QComboBox(self.horizontalLayoutWidget_2)
        self.selectPattern.setObjectName(u"selectPattern")

        self.saveLoadPattern.addWidget(self.selectPattern)

        self.savePattern = QPushButton(self.horizontalLayoutWidget_2)
        self.savePattern.setObjectName(u"savePattern")

        self.saveLoadPattern.addWidget(self.savePattern)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 189, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.seedRatioEditor.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(1)
        self.steps.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(1)
        self.length.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.length)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.seedRatioEditor.addLayout(self.verticalLayout_8)

        self.groupBox_2 = QGroupBox(gateseqPatternEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 70, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 250, 381, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.horizontalLayout_6.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.horizontalLayout_6.addWidget(self.addText)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.horizontalLayout_6.addWidget(self.clearSequences)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 300, 381, 244))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2_2 = QPushButton(self.gridLayoutWidget)
        self.sequence2_2.setObjectName(u"sequence2_2")

        self.verticalLayout_4.addWidget(self.sequence2_2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.label_20 = QLabel(gateseqPatternEditor)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 170, 379, 19))
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(gateseqPatternEditor)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(8, 10, 381, 20))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.savePatternSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.savePattern.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.label_20.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.label_21.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectPatternSet = QComboBox(self.horizontalLayoutWidget)
        self.selectPatternSet.setObjectName(u"selectPatternSet")

        self.scalesSetButtons.addWidget(self.selectPatternSet)

        self.savePatternSet = QPushButton(self.horizontalLayoutWidget)
        self.savePatternSet.setObjectName(u"savePatternSet")

        self.scalesSetButtons.addWidget(self.savePatternSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadPattern = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadPattern.setObjectName(u"saveLoadPattern")
        self.saveLoadPattern.setContentsMargins(0, 0, 0, 0)
        self.selectPattern = QComboBox(self.horizontalLayoutWidget_2)
        self.selectPattern.setObjectName(u"selectPattern")

        self.saveLoadPattern.addWidget(self.selectPattern)

        self.savePattern = QPushButton(self.horizontalLayoutWidget_2)
        self.savePattern.setObjectName(u"savePattern")

        self.saveLoadPattern.addWidget(self.savePattern)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 189, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.seedRatioEditor.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(1)
        self.steps.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(1)
        self.length.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.length)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.seedRatioEditor.addLayout(self.verticalLayout_8)

        self.groupBox_2 = QGroupBox(gateseqPatternEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 70, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 250, 381, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.horizontalLayout_6.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.horizontalLayout_6.addWidget(self.addText)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.horizontalLayout_6.addWidget(self.clearSequences)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 300, 381, 244))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2 = QPushButton(self.gridLayoutWidget)
        self.sequence2.setObjectName(u"sequence2")

        self.verticalLayout_4.addWidget(self.sequence2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.label_20 = QLabel(gateseqPatternEditor)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 170, 379, 19))
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(gateseqPatternEditor)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(8, 10, 381, 20))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.savePatternSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.savePattern.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.label_20.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.label_21.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectPatternSet = QComboBox(self.horizontalLayoutWidget)
        self.selectPatternSet.setObjectName(u"selectPatternSet")

        self.scalesSetButtons.addWidget(self.selectPatternSet)

        self.savePatternSet = QPushButton(self.horizontalLayoutWidget)
        self.savePatternSet.setObjectName(u"savePatternSet")

        self.scalesSetButtons.addWidget(self.savePatternSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadPattern = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadPattern.setObjectName(u"saveLoadPattern")
        self.saveLoadPattern.setContentsMargins(0, 0, 0, 0)
        self.selectPattern = QComboBox(self.horizontalLayoutWidget_2)
        self.selectPattern.setObjectName(u"selectPattern")

        self.saveLoadPattern.addWidget(self.selectPattern)

        self.savePattern = QPushButton(self.horizontalLayoutWidget_2)
        self.savePattern.setObjectName(u"savePattern")

        self.saveLoadPattern.addWidget(self.savePattern)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 189, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.seedRatioEditor.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(1)
        self.steps.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(1)
        self.length.setMaximum(65535)

        self.verticalLayout_2.addWidget(self.length)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.seedRatioEditor.addLayout(self.verticalLayout_8)

        self.groupBox_2 = QGroupBox(gateseqPatternEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 70, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 250, 381, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.horizontalLayout_6.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.horizontalLayout_6.addWidget(self.addText)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.horizontalLayout_6.addWidget(self.clearSequences)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 300, 381, 244))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2 = QPushButton(self.gridLayoutWidget)
        self.sequence2.setObjectName(u"sequence2")

        self.verticalLayout_4.addWidget(self.sequence2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.label_20 = QLabel(gateseqPatternEditor)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 170, 379, 19))
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(gateseqPatternEditor)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(8, 10, 381, 20))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.savePatternSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.savePattern.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.label_20.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.label_21.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectPatternSet = QComboBox(self.horizontalLayoutWidget)
        self.selectPatternSet.setObjectName(u"selectPatternSet")

        self.scalesSetButtons.addWidget(self.selectPatternSet)

        self.savePatternSet = QPushButton(self.horizontalLayoutWidget)
        self.savePatternSet.setObjectName(u"savePatternSet")

        self.scalesSetButtons.addWidget(self.savePatternSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadPattern = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadPattern.setObjectName(u"saveLoadPattern")
        self.saveLoadPattern.setContentsMargins(0, 0, 0, 0)
        self.selectPattern = QComboBox(self.horizontalLayoutWidget_2)
        self.selectPattern.setObjectName(u"selectPattern")

        self.saveLoadPattern.addWidget(self.selectPattern)

        self.savePattern = QPushButton(self.horizontalLayoutWidget_2)
        self.savePattern.setObjectName(u"savePattern")

        self.saveLoadPattern.addWidget(self.savePattern)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 189, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.seedRatioEditor.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(0)
        self.steps.setMaximum(64)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(0)
        self.length.setMaximum(64)

        self.verticalLayout_2.addWidget(self.length)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.seedRatioEditor.addLayout(self.verticalLayout_8)

        self.groupBox_2 = QGroupBox(gateseqPatternEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 70, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 250, 381, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.horizontalLayout_6.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.horizontalLayout_6.addWidget(self.addText)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.horizontalLayout_6.addWidget(self.clearSequences)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 300, 381, 244))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2 = QPushButton(self.gridLayoutWidget)
        self.sequence2.setObjectName(u"sequence2")

        self.verticalLayout_4.addWidget(self.sequence2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.label_20 = QLabel(gateseqPatternEditor)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 170, 379, 19))
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(gateseqPatternEditor)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(8, 10, 381, 20))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.savePatternSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.savePattern.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.label_20.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.label_21.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectPatternSet = QComboBox(self.horizontalLayoutWidget)
        self.selectPatternSet.setObjectName(u"selectPatternSet")

        self.scalesSetButtons.addWidget(self.selectPatternSet)

        self.savePatternSet = QPushButton(self.horizontalLayoutWidget)
        self.savePatternSet.setObjectName(u"savePatternSet")

        self.scalesSetButtons.addWidget(self.savePatternSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadPattern = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadPattern.setObjectName(u"saveLoadPattern")
        self.saveLoadPattern.setContentsMargins(0, 0, 0, 0)
        self.selectPattern = QComboBox(self.horizontalLayoutWidget_2)
        self.selectPattern.setObjectName(u"selectPattern")

        self.saveLoadPattern.addWidget(self.selectPattern)

        self.savePattern = QPushButton(self.horizontalLayoutWidget_2)
        self.savePattern.setObjectName(u"savePattern")

        self.saveLoadPattern.addWidget(self.savePattern)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 189, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.seedRatioEditor.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(0)
        self.steps.setMaximum(0)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(0)
        self.length.setMaximum(64)

        self.verticalLayout_2.addWidget(self.length)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.seedRatioEditor.addLayout(self.verticalLayout_8)

        self.groupBox_2 = QGroupBox(gateseqPatternEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 70, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 250, 381, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.horizontalLayout_6.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.horizontalLayout_6.addWidget(self.addText)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.horizontalLayout_6.addWidget(self.clearSequences)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 300, 381, 244))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2 = QPushButton(self.gridLayoutWidget)
        self.sequence2.setObjectName(u"sequence2")

        self.verticalLayout_4.addWidget(self.sequence2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.label_20 = QLabel(gateseqPatternEditor)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 170, 379, 19))
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(gateseqPatternEditor)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(8, 10, 381, 20))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.savePatternSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.savePattern.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.label_20.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.label_21.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 550, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.horizontalLayoutWidget = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 381, 41))
        self.scalesSetButtons = QHBoxLayout(self.horizontalLayoutWidget)
        self.scalesSetButtons.setObjectName(u"scalesSetButtons")
        self.scalesSetButtons.setContentsMargins(0, 0, 0, 0)
        self.selectPatternSet = QComboBox(self.horizontalLayoutWidget)
        self.selectPatternSet.setObjectName(u"selectPatternSet")

        self.scalesSetButtons.addWidget(self.selectPatternSet)

        self.savePatternSet = QPushButton(self.horizontalLayoutWidget)
        self.savePatternSet.setObjectName(u"savePatternSet")

        self.scalesSetButtons.addWidget(self.savePatternSet)

        self.saveForRack = QPushButton(self.horizontalLayoutWidget)
        self.saveForRack.setObjectName(u"saveForRack")

        self.scalesSetButtons.addWidget(self.saveForRack)

        self.horizontalLayoutWidget_2 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.saveLoadPattern = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.saveLoadPattern.setObjectName(u"saveLoadPattern")
        self.saveLoadPattern.setContentsMargins(0, 0, 0, 0)
        self.selectPattern = QComboBox(self.horizontalLayoutWidget_2)
        self.selectPattern.setObjectName(u"selectPattern")

        self.saveLoadPattern.addWidget(self.selectPattern)

        self.savePattern = QPushButton(self.horizontalLayoutWidget_2)
        self.savePattern.setObjectName(u"savePattern")

        self.saveLoadPattern.addWidget(self.savePattern)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 189, 381, 62))
        self.seedRatioEditor = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.seedRatioEditor.setObjectName(u"seedRatioEditor")
        self.seedRatioEditor.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.seedRatioEditor.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(0)
        self.steps.setMaximum(0)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(1)
        self.length.setMaximum(64)

        self.verticalLayout_2.addWidget(self.length)


        self.seedRatioEditor.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.seedRatioEditor.addLayout(self.verticalLayout_8)

        self.groupBox_2 = QGroupBox(gateseqPatternEditor)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 70, 381, 51))
        self.layoutWidget = QWidget(self.groupBox_2)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 250, 381, 41))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.horizontalLayout_6.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.horizontalLayout_6.addWidget(self.addText)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.horizontalLayout_6.addWidget(self.clearSequences)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 300, 381, 244))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2 = QPushButton(self.gridLayoutWidget)
        self.sequence2.setObjectName(u"sequence2")

        self.verticalLayout_4.addWidget(self.sequence2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.gridLayout.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.gridLayout.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.gridLayout.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.gridLayout.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.gridLayout.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.gridLayout.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.gridLayout.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.gridLayout.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.gridLayout.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.gridLayout.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.label_20 = QLabel(gateseqPatternEditor)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 170, 379, 19))
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_21 = QLabel(gateseqPatternEditor)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(8, 10, 381, 20))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.savePatternSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.savePattern.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.groupBox_2.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.label_20.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.label_21.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set", None))
    # retranslateUi

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gateseq_pattern_editor.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_gateseqPatternEditor(object):
    def setupUi(self, gateseqPatternEditor):
        if not gateseqPatternEditor.objectName():
            gateseqPatternEditor.setObjectName(u"gateseqPatternEditor")
        gateseqPatternEditor.resize(400, 590)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(92, 92, 92, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(77, 77, 77, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(64, 64, 64, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        gateseqPatternEditor.setPalette(palette)
        self.buttonBox = QDialogButtonBox(gateseqPatternEditor)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 550, 341, 32))
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
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 120, 381, 41))
        self.resourceSaveLoad = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.resourceSaveLoad.setObjectName(u"resourceSaveLoad")
        self.resourceSaveLoad.setContentsMargins(0, 0, 0, 0)
        self.selectResource = QComboBox(self.horizontalLayoutWidget_2)
        self.selectResource.setObjectName(u"selectResource")

        self.resourceSaveLoad.addWidget(self.selectResource)

        self.saveResource = QPushButton(self.horizontalLayoutWidget_2)
        self.saveResource.setObjectName(u"saveResource")

        self.resourceSaveLoad.addWidget(self.saveResource)

        self.horizontalLayoutWidget_6 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 189, 381, 62))
        self.addEuclideanControls = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.addEuclideanControls.setObjectName(u"addEuclideanControls")
        self.addEuclideanControls.setContentsMargins(0, 0, 0, 0)
        self.addEuclidean = QPushButton(self.horizontalLayoutWidget_6)
        self.addEuclidean.setObjectName(u"addEuclidean")

        self.addEuclideanControls.addWidget(self.addEuclidean)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.steps = QSpinBox(self.horizontalLayoutWidget_6)
        self.steps.setObjectName(u"steps")
        self.steps.setMinimumSize(QSize(50, 26))
        self.steps.setMinimum(0)
        self.steps.setMaximum(0)

        self.verticalLayout_2.addWidget(self.steps)

        self.length = QSpinBox(self.horizontalLayoutWidget_6)
        self.length.setObjectName(u"length")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.length.sizePolicy().hasHeightForWidth())
        self.length.setSizePolicy(sizePolicy)
        self.length.setMinimumSize(QSize(50, 26))
        self.length.setMinimum(1)
        self.length.setMaximum(64)

        self.verticalLayout_2.addWidget(self.length)


        self.addEuclideanControls.addLayout(self.verticalLayout_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_7)

        self.label_2 = QLabel(self.horizontalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)


        self.addEuclideanControls.addLayout(self.verticalLayout_8)

        self.resourceSetSlots = QGroupBox(gateseqPatternEditor)
        self.resourceSetSlots.setObjectName(u"resourceSetSlots")
        self.resourceSetSlots.setGeometry(QRect(9, 70, 381, 51))
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slot1.sizePolicy().hasHeightForWidth())
        self.slot1.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot2.sizePolicy().hasHeightForWidth())
        self.slot2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot3.sizePolicy().hasHeightForWidth())
        self.slot3.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot4.sizePolicy().hasHeightForWidth())
        self.slot4.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot5.sizePolicy().hasHeightForWidth())
        self.slot5.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot6.sizePolicy().hasHeightForWidth())
        self.slot6.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot7.sizePolicy().hasHeightForWidth())
        self.slot7.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.slot8.sizePolicy().hasHeightForWidth())
        self.slot8.setSizePolicy(sizePolicy1)
        self.slot8.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_10.addWidget(self.slot8)


        self.slot8layout.addLayout(self.horizontalLayout_10)

        self.label8 = QLabel(self.layoutWidget)
        self.label8.setObjectName(u"label8")
        self.label8.setAlignment(Qt.AlignCenter)

        self.slot8layout.addWidget(self.label8)


        self.horizontalLayout.addLayout(self.slot8layout)

        self.horizontalLayoutWidget_3 = QWidget(gateseqPatternEditor)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 250, 381, 41))
        self.addSequenceButtons = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.addSequenceButtons.setObjectName(u"addSequenceButtons")
        self.addSequenceButtons.setContentsMargins(0, 0, 0, 0)
        self.addX0x = QPushButton(self.horizontalLayoutWidget_3)
        self.addX0x.setObjectName(u"addX0x")

        self.addSequenceButtons.addWidget(self.addX0x)

        self.addText = QPushButton(self.horizontalLayoutWidget_3)
        self.addText.setObjectName(u"addText")

        self.addSequenceButtons.addWidget(self.addText)

        self.clearSequences = QPushButton(self.horizontalLayoutWidget_3)
        self.clearSequences.setObjectName(u"clearSequences")

        self.addSequenceButtons.addWidget(self.clearSequences)

        self.gridLayoutWidget = QWidget(gateseqPatternEditor)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 300, 381, 244))
        self.sequenceGrid = QGridLayout(self.gridLayoutWidget)
        self.sequenceGrid.setObjectName(u"sequenceGrid")
        self.sequenceGrid.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sequence1 = QPushButton(self.gridLayoutWidget)
        self.sequence1.setObjectName(u"sequence1")

        self.verticalLayout.addWidget(self.sequence1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)


        self.sequenceGrid.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.sequence2 = QPushButton(self.gridLayoutWidget)
        self.sequence2.setObjectName(u"sequence2")

        self.verticalLayout_4.addWidget(self.sequence2)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)


        self.sequenceGrid.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sequence3 = QPushButton(self.gridLayoutWidget)
        self.sequence3.setObjectName(u"sequence3")

        self.verticalLayout_5.addWidget(self.sequence3)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_5)


        self.sequenceGrid.addLayout(self.verticalLayout_5, 0, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.sequence4 = QPushButton(self.gridLayoutWidget)
        self.sequence4.setObjectName(u"sequence4")

        self.verticalLayout_6.addWidget(self.sequence4)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6)


        self.sequenceGrid.addLayout(self.verticalLayout_6, 0, 3, 1, 1)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.sequence5 = QPushButton(self.gridLayoutWidget)
        self.sequence5.setObjectName(u"sequence5")

        self.verticalLayout_7.addWidget(self.sequence5)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)


        self.sequenceGrid.addLayout(self.verticalLayout_7, 1, 0, 1, 1)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.sequence6 = QPushButton(self.gridLayoutWidget)
        self.sequence6.setObjectName(u"sequence6")

        self.verticalLayout_14.addWidget(self.sequence6)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)


        self.sequenceGrid.addLayout(self.verticalLayout_14, 1, 1, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.sequence7 = QPushButton(self.gridLayoutWidget)
        self.sequence7.setObjectName(u"sequence7")

        self.verticalLayout_16.addWidget(self.sequence7)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_10)


        self.sequenceGrid.addLayout(self.verticalLayout_16, 1, 2, 1, 1)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.sequence8 = QPushButton(self.gridLayoutWidget)
        self.sequence8.setObjectName(u"sequence8")

        self.verticalLayout_17.addWidget(self.sequence8)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_11)


        self.sequenceGrid.addLayout(self.verticalLayout_17, 1, 3, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.sequence9 = QPushButton(self.gridLayoutWidget)
        self.sequence9.setObjectName(u"sequence9")

        self.verticalLayout_13.addWidget(self.sequence9)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_12)


        self.sequenceGrid.addLayout(self.verticalLayout_13, 2, 0, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.sequence10 = QPushButton(self.gridLayoutWidget)
        self.sequence10.setObjectName(u"sequence10")

        self.verticalLayout_15.addWidget(self.sequence10)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_13)


        self.sequenceGrid.addLayout(self.verticalLayout_15, 2, 1, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.sequence11 = QPushButton(self.gridLayoutWidget)
        self.sequence11.setObjectName(u"sequence11")

        self.verticalLayout_18.addWidget(self.sequence11)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_14)


        self.sequenceGrid.addLayout(self.verticalLayout_18, 2, 2, 1, 1)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.sequence12 = QPushButton(self.gridLayoutWidget)
        self.sequence12.setObjectName(u"sequence12")

        self.verticalLayout_19.addWidget(self.sequence12)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_15)


        self.sequenceGrid.addLayout(self.verticalLayout_19, 2, 3, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.sequence16 = QPushButton(self.gridLayoutWidget)
        self.sequence16.setObjectName(u"sequence16")

        self.verticalLayout_12.addWidget(self.sequence16)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16)


        self.sequenceGrid.addLayout(self.verticalLayout_12, 3, 3, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.sequence15 = QPushButton(self.gridLayoutWidget)
        self.sequence15.setObjectName(u"sequence15")

        self.verticalLayout_11.addWidget(self.sequence15)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_17)


        self.sequenceGrid.addLayout(self.verticalLayout_11, 3, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.sequence14 = QPushButton(self.gridLayoutWidget)
        self.sequence14.setObjectName(u"sequence14")

        self.verticalLayout_10.addWidget(self.sequence14)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_18)


        self.sequenceGrid.addLayout(self.verticalLayout_10, 3, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sequence13 = QPushButton(self.gridLayoutWidget)
        self.sequence13.setObjectName(u"sequence13")

        self.verticalLayout_3.addWidget(self.sequence13)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)


        self.sequenceGrid.addLayout(self.verticalLayout_3, 3, 0, 1, 1)

        self.editPatternLabel = QLabel(gateseqPatternEditor)
        self.editPatternLabel.setObjectName(u"editPatternLabel")
        self.editPatternLabel.setGeometry(QRect(10, 170, 379, 19))
        self.editPatternLabel.setAlignment(Qt.AlignCenter)
        self.editPatternSetLabel = QLabel(gateseqPatternEditor)
        self.editPatternSetLabel.setObjectName(u"editPatternSetLabel")
        self.editPatternSetLabel.setGeometry(QRect(8, 10, 381, 20))
        self.editPatternSetLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(gateseqPatternEditor)
        self.buttonBox.accepted.connect(gateseqPatternEditor.accept)
        self.buttonBox.rejected.connect(gateseqPatternEditor.reject)

        QMetaObject.connectSlotsByName(gateseqPatternEditor)
    # setupUi

    def retranslateUi(self, gateseqPatternEditor):
        gateseqPatternEditor.setWindowTitle(QCoreApplication.translate("gateseqPatternEditor", u"Sync3 Scale Set Editor", None))
        self.saveResourceSet.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern Set", None))
        self.saveForRack.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save for Rack", None))
        self.saveResource.setText(QCoreApplication.translate("gateseqPatternEditor", u"Save Pattern", None))
        self.addEuclidean.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add Euclidean", None))
        self.label_7.setText(QCoreApplication.translate("gateseqPatternEditor", u"Steps", None))
        self.label_2.setText(QCoreApplication.translate("gateseqPatternEditor", u"Length", None))
        self.resourceSetSlots.setTitle("")
        self.slot1.setText("")
        self.label1.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-1", None))
        self.slot2.setText("")
        self.label2.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-2", None))
        self.slot3.setText("")
        self.label3.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-3", None))
        self.slot4.setText("")
        self.label4.setText(QCoreApplication.translate("gateseqPatternEditor", u"I-4", None))
        self.slot5.setText("")
        self.label5.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-1", None))
        self.slot6.setText("")
        self.label6.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-2", None))
        self.slot7.setText("")
        self.label7.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-3", None))
        self.slot8.setText("")
        self.label8.setText(QCoreApplication.translate("gateseqPatternEditor", u"II-4", None))
        self.addX0x.setText(QCoreApplication.translate("gateseqPatternEditor", u"Add as x0x", None))
        self.addText.setText(QCoreApplication.translate("gateseqPatternEditor", u"Pad to Fill", None))
        self.clearSequences.setText(QCoreApplication.translate("gateseqPatternEditor", u"Clear All", None))
        self.sequence1.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 1", None))
        self.sequence2.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_4.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 2", None))
        self.sequence3.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 3", None))
        self.sequence4.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_6.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 4", None))
        self.sequence5.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_8.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 5", None))
        self.sequence6.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_9.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 6", None))
        self.sequence7.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_10.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 7", None))
        self.sequence8.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_11.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 8", None))
        self.sequence9.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_12.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 9", None))
        self.sequence10.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_13.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 10", None))
        self.sequence11.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_14.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 11", None))
        self.sequence12.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_15.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 12", None))
        self.sequence16.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_16.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 16", None))
        self.sequence15.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 15", None))
        self.sequence14.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_18.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 14", None))
        self.sequence13.setText(QCoreApplication.translate("gateseqPatternEditor", u"PushButton", None))
        self.label_19.setText(QCoreApplication.translate("gateseqPatternEditor", u"Sequence 13", None))
        self.editPatternLabel.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern", None))
        self.editPatternSetLabel.setText(QCoreApplication.translate("gateseqPatternEditor", u"Edit Pattern Set", None))
    # retranslateUi

