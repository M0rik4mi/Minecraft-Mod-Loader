# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PopupDnfSnl.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Popup(object):
    def setupUi(self, Popup):
        if not Popup.objectName():
            Popup.setObjectName(u"Popup")
        Popup.resize(500, 300)
        self.verticalLayout = QVBoxLayout(Popup)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Popup)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(194, 194, 194);	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 50px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 0, 400, 100))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.OkayButton = QPushButton(self.frame)
        self.OkayButton.setObjectName(u"OkayButton")
        self.OkayButton.setGeometry(QRect(150, 150, 200, 50))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.OkayButton.setFont(font1)
        self.OkayButton.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.AbbruchButton = QPushButton(self.frame)
        self.AbbruchButton.setObjectName(u"AbbruchButton")
        self.AbbruchButton.setGeometry(QRect(150, 200, 200, 50))
        self.AbbruchButton.setFont(font1)
        self.AbbruchButton.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.OrdnerButton = QPushButton(self.frame)
        self.OrdnerButton.setObjectName(u"OrdnerButton")
        self.OrdnerButton.setGeometry(QRect(150, 100, 200, 50))
        self.OrdnerButton.setFont(font1)
        self.OrdnerButton.setStyleSheet(u"QPushButton {	\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Popup)

        QMetaObject.connectSlotsByName(Popup)
    # setupUi

    def retranslateUi(self, Popup):
        Popup.setWindowTitle(QCoreApplication.translate("Popup", u"Form", None))
        self.label.setText(QCoreApplication.translate("Popup", u"TextLabel", None))
        self.OkayButton.setText(QCoreApplication.translate("Popup", u"PushButton", None))
        self.AbbruchButton.setText(QCoreApplication.translate("Popup", u"PushButton", None))
        self.OrdnerButton.setText(QCoreApplication.translate("Popup", u"PushButton", None))
    # retranslateUi

