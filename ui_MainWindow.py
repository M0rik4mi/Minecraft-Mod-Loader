# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowXFhiBw.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropSchadowframe = QFrame(self.centralwidget)
        self.dropSchadowframe.setObjectName(u"dropSchadowframe")
        self.dropSchadowframe.setStyleSheet(u"QFrame#dropSchadowframe {\n"
"	background-color: rgb(240, 240, 240);	\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 50px\n"
"}")
        self.dropSchadowframe.setFrameShape(QFrame.StyledPanel)
        self.dropSchadowframe.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.dropSchadowframe)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(5, 5, 970, 570))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(194, 194, 194);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 50px\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(65, 410, 850, 35))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(20, 20, 20);	\n"
"	color:rgb(255, 255, 255);\n"
"	border-style: none;\n"
"	border-radius: 17px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{	\n"
"	border-radius: 17px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.341, x2:1, y2:0.739, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(0, 0, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.pushButton_Minecraft_1_16_5 = QPushButton(self.frame)
        self.pushButton_Minecraft_1_16_5.setObjectName(u"pushButton_Minecraft_1_16_5")
        self.pushButton_Minecraft_1_16_5.setGeometry(QRect(365, 315, 250, 70))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(True)
        self.pushButton_Minecraft_1_16_5.setFont(font1)
        self.pushButton_Minecraft_1_16_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.pushButton_Minecraft_1_16_4_Create = QPushButton(self.frame)
        self.pushButton_Minecraft_1_16_4_Create.setObjectName(u"pushButton_Minecraft_1_16_4_Create")
        self.pushButton_Minecraft_1_16_4_Create.setGeometry(QRect(65, 315, 250, 70))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.pushButton_Minecraft_1_16_4_Create.setFont(font2)
        self.pushButton_Minecraft_1_16_4_Create.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(255, 255, 255);\n"
" }")
        self.label_Endtext = QLabel(self.frame)
        self.label_Endtext.setObjectName(u"label_Endtext")
        self.label_Endtext.setGeometry(QRect(40, 460, 900, 100))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(25)
        self.label_Endtext.setFont(font3)
        self.label_Endtext.setAutoFillBackground(False)
        self.label_Endtext.setStyleSheet(u"QLabel{	\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(240, 240, 240);	\n"
"	border-radius: 25px;\n"
"}")
        self.label_Endtext.setAlignment(Qt.AlignCenter)
        self.pushButton_Close = QPushButton(self.frame)
        self.pushButton_Close.setObjectName(u"pushButton_Close")
        self.pushButton_Close.setGeometry(QRect(920, 15, 25, 25))
        font4 = QFont()
        font4.setFamily(u"Javanese Text")
        self.pushButton_Close.setFont(font4)
        self.pushButton_Close.setAutoFillBackground(False)
        self.pushButton_Close.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(80, 80, 80);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/CloseButton/X.png", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_Close.setIcon(icon)
        self.pushButton_Close.setIconSize(QSize(25, 25))
        self.pushButton_Close.setFlat(True)
        self.label_description = QLabel(self.frame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(5, 90, 960, 200))
        self.label_description.setMaximumSize(QSize(16777215, 16777215))
        self.label_description.setFont(font3)
        self.label_description.setAutoFillBackground(False)
        self.label_description.setStyleSheet(u"QLabel{	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(240, 240, 240);	\n"
"	border-radius: 25px;\n"
"}")
        self.label_description.setLineWidth(0)
        self.label_description.setText(u"")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description.setWordWrap(True)
        self.pushButton_Minecraft_Life_in_the_Woods = QPushButton(self.frame)
        self.pushButton_Minecraft_Life_in_the_Woods.setObjectName(u"pushButton_Minecraft_Life_in_the_Woods")
        self.pushButton_Minecraft_Life_in_the_Woods.setGeometry(QRect(665, 315, 250, 70))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setKerning(True)
        self.pushButton_Minecraft_Life_in_the_Woods.setFont(font5)
        self.pushButton_Minecraft_Life_in_the_Woods.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(150, 150, 150);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.label_titel = QLabel(self.frame)
        self.label_titel.setObjectName(u"label_titel")
        self.label_titel.setGeometry(QRect(190, 10, 600, 60))
        self.label_titel.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(40)
        self.label_titel.setFont(font6)
        self.label_titel.setAutoFillBackground(False)
        self.label_titel.setStyleSheet(u"QLabel{	\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(240, 240, 240);	\n"
"	border-radius: 25px;\n"
"}")
        self.label_titel.setLineWidth(0)
        self.label_titel.setText(u"")
        self.label_titel.setAlignment(Qt.AlignCenter)
        self.label_titel.setWordWrap(True)

        self.verticalLayout.addWidget(self.dropSchadowframe)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_Minecraft_1_16_5.setText("")
        self.pushButton_Minecraft_1_16_4_Create.setText("")
        self.label_Endtext.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_Close.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_Close.setText("")
        self.pushButton_Minecraft_Life_in_the_Woods.setText("")
    # retranslateUi

