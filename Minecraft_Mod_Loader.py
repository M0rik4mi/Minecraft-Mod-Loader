#-*- coding: utf-8 -*-

import sys
import platform
import requests
import os
import threading
import subprocess
from zipfile import ZipFile
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QThread, QObject, Signal
from PySide6.QtGui import QColor, QIcon, QScreen
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QGraphicsDropShadowEffect, QMessageBox, QFileDialog

#Grafik
from ui_MainWindow import Ui_MainWindow
from ui_Popup import Ui_Popup


#Temp-Ordner zum Entpacken
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


#url Sammlung
url0 = 'https://www.chaospur.de/wp-content/uploads/2021/02/1-16-4-Create-Mods.zip'
url1 = 'Gibt keine Mods'
url2 = 'https://www.chaospur.de/wp-content/uploads/2021/02/1-7-10-Life-in-the-Woods.zip'
url3 = 'https://www.chaospur.de/download/1-12-2-zombie-apocalypse/?wpdmdl=181&masterkey=6071c7df042dd'


#Pfad Minecraft Ordner
if os.name == 'nt':
    suche_path=os.path.expanduser("~\\appdata\\roaming\\.minecraft\\mods\\")
elif os.name == 'posix':
    suche_path=os.path.expanduser("~/.minecraft/mods/")
elif os.name == "darwin":
    suche_path=os.path.expanduser("~/appdata/roaming/.minecraft/mods/")  


#Pfad Minecraft Ordner
if os.name == 'nt':
    suche_path_noMod=os.path.expanduser("~~\\appdata\\roaming\\.minecraft\\mods\\")
elif os.name == 'posix':
    suche_path_noMod=os.path.expanduser("~/.minecraft/mods/")
elif os.name == "darwin":
    suche_path_noMod=os.path.expanduser("~/appdata/roaming/.minecraft/mods/")


#Kein Download
def noDownload(self, button):
        button.setText('Keine Mods verfügbar')

        #Change Endtext
        self.ui.label_Endtext.setStyleSheet("color:Black")
        self.ui.label_Endtext.setText("Es gibt keine Mods \n Viel Spaß beim Spielen.")
 
            
#Öffne .minecraft/Mod Ordner
def suche():
    if not os.path.exists(suche_path):
        #if os.path.exists(suche_path_noMod):   Funktioniert mit der Systemabfrage nicht mehr!!!
        os.makedirs(suche_path)
    open_ordner()

def open_ordner():
        if sys.platform == 'win32':
            os.startfile(suche_path)
        else:    
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, suche_path])
        

#Speichern Funktion mit Download und Extrahieren der Zip
def save(self,url,button,text):

            #Change Button Name
            button.setText("loading...")

            folder = str(QFileDialog.getExistingDirectory(None, "Wähle deinen Mod Ordner", suche_path))

            the_filesize = requests.get(url, stream=True).headers['Content-Length']
            the_filepath = folder +"/tmp"
            the_fileobj = open(the_filepath, 'wb')
            buffer = 10240
            #Create Download Thread
            self.downloadThread = downloadThread(self, url, button, text, the_filesize, the_fileobj, buffer, folder)
            self.downloadThread.download_proess_signal.connect(self.set_progressbar_value)
            self.downloadThread.start()


#Download thread
class downloadThread(QThread):
    download_proess_signal = Signal(int)                        #Create signal

    def __init__(self,self_Mainwindow, url, button, text, filesize, fileobj, buffer, folder):
        super(downloadThread, self).__init__()
        self.url = url
        self.filesize = filesize
        self.fileobj = fileobj
        self.buffer = buffer
        self.button = button
        self.text = text
        self.folder = folder
        self.self_Mainwindow = self_Mainwindow


    def run(self):
        try:
            rsp = requests.get(self.url, stream=True)                #Streaming download mode
            offset = 0
            for chunk in rsp.iter_content(chunk_size=self.buffer):
                if not chunk: break
                self.fileobj.seek(offset)                            #Setting Pointer Position
                self.fileobj.write(chunk)                            #write file
                offset = offset + len(chunk)
                proess = offset / int(self.filesize) * 100
                self.download_proess_signal.emit(int(proess))        #Sending signal
            
            self.fileobj.close()    #Close file

            #Change Button Name
            self.button.setText("Extracting...")

            #Extrahieren der Zip
            temp=self.folder +"/tmp"
            zf=ZipFile(temp)
            zf.extractall(path=self.folder)
            zf.close()
            os.remove(temp)

            #Change Button Name
            self.button.setText(self.text)

            self.self_Mainwindow.ui.label_Endtext.setStyleSheet("color:Black; background-color: rgb(240, 240, 240); border-radius: 25px;")
            self.self_Mainwindow.ui.label_Endtext.setText(self.text + "Mods sind fertig geladen. \n Viel Spaß beim Spielen.")
            
            self.exit(0)            #Close thread

        except Exception as e:
            print(e)


#Popup Window
class Popup(QWidget):
    def __init__(self,self_Mainwindow,url,button,text):
        QWidget.__init__(self)
        self.Popup = Ui_Popup()
        self.Popup.setupUi(self)

        #Remove Titelbar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Set to Screen center
        qtRectangle = self.frameGeometry()
        centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        #Popup Text
        self.Popup.label.setText('Ist der Modordner leer?')

        #Popup Buttons
        self.Popup.OkayButton.setText("Ja")
        self.Popup.OkayButton.clicked.connect(lambda:self.save(self_Mainwindow, url, button, text))
        self.Popup.OrdnerButton.setText('Öffne Ordner')
        self.Popup.OrdnerButton.clicked.connect(lambda:suche())
        self.Popup.AbbruchButton.setText('Abbrechen')
        self.Popup.AbbruchButton.clicked.connect(lambda:self.schließen())

    def save(self,self_Mainwindow,url,button,text):
        self.close()
        self.save = save(self_Mainwindow,url,button,text)

    def schließen(self):
        self.close()
        

#Main Window
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        
        #Remove Titelbar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #Set to Screen center
        qtRectangle = self.frameGeometry()
        centerPoint = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        #Drop Shadow Effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropSchadowframe.setGraphicsEffect(self.shadow)

        #Titel
        self.ui.label_titel.setText("Minecraft Mod Loader")

        #Description
        #self.ui.label_description.setWordWrap(true)
        self.ui.label_description.setText("1.Wähle den gewünschten Server. <br> 2.Stelle sicher das der Modordner leer ist. <br> 3.Fertig <br> Ob grade ein Eventserver läuft erfahrt ihr im TS!<br>Falls ihr die Skins geändert haben wollt liegt im Download eine Zip für die Assets. Lasst den Ordner vom Popup dafür einfach offen.")

        #Button Minecraft_1_16_5
        self.ui.pushButton_Event.setText('Event-Server')
        button_event=self.ui.pushButton_Event
        self.ui.pushButton_Event.clicked.connect(lambda:self.popup(url3, button_event, 'Event-Server'))

        #Button Minecraft_1_16_5
        self.ui.pushButton_Minecraft_1_16_5.setText('Minecraft 1.16.5')
        self.ui.pushButton_Minecraft_1_16_5.clicked.connect(lambda:noDownload(self, self.ui.pushButton_Minecraft_1_16_5))

        #Button Minecraft_1_16_4_Create
        self.ui.pushButton_Minecraft_1_16_4_Create.setText('Minecraft 1.16.4 Create')
        button0 = self.ui.pushButton_Minecraft_1_16_4_Create
        self.ui.pushButton_Minecraft_1_16_4_Create.clicked.connect(lambda:self.popup(url0, button0, 'Minecraft 1.16.4 Create'))

        #Button Minecraft_Life_in_the_Woods
        self.ui.pushButton_Minecraft_Life_in_the_Woods.setText('Minecraft Life in the Woods')
        button2 = self.ui.pushButton_Minecraft_Life_in_the_Woods
        self.ui.pushButton_Minecraft_Life_in_the_Woods.clicked.connect(lambda:self.popup(url2, button2, 'Minecraft Life in the Woods'))

        #Close Button
        close_image = resource_path("X.png")
        self.ui.pushButton_Close.setIcon(QIcon(close_image))
        self.ui.pushButton_Close.clicked.connect(lambda:self.closeIt())

        #Progress Bar
        self.ui.progressBar.setValue(0)

        #Endtext
        self.ui.label_Endtext.setText("Mods sind noch nicht geladen")

    
    # Setting progress bar
    def set_progressbar_value(self, value):
        self.ui.progressBar.setValue(value)
        

    # Deffiniere den Button Press   
    def popup(self, url, button, text):
        self.create_popup = Popup(self,url,button,text)  
        self.create_popup.show()

    #Deffiniere self.close
    def closeIt(self):
        app = QApplication.instance()
        app.closeAllWindows()


if __name__ == "__main__":
    app= QApplication(sys.argv)
    window = MainWindow() 
    window.show()

    app.setWindowIcon(QIcon('minecraft_logo.ico'))
    window.setWindowIcon(QIcon('minecraft_logo.ico'))

    sys.exit(app.exec_())