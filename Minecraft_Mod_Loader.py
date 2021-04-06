import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory, askopenfilename
import os
from zipfile import ZipFile


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


#Pfad Minecraft Ordner
suche_path=os.path.expanduser("~/appdata/roaming/.minecraft/mods/")
suche_path_noMod=os.path.expanduser("~/appdata/roaming/.minecraft/")


#Programm Start
root = tk.Tk()


#Hintergrund
root.configure(background='black')


#Titel
root.title('Minecraft Mod Downloader für die Chaospur Server')


#Icon
root.iconbitmap(resource_path('minecraft_logo.ico'))


#Layout anlegen
canvas = tk.Canvas(root, width=800, height=600,)
canvas.grid(columnspan=3, rowspan=8, padx=5, pady=5)


#logo
logo = Image.open(resource_path("minecraft.jpg"))
logo = ImageTk.PhotoImage(logo)
logo_label = ttk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=1, padx='5', pady='0')


#instructions
instructions = tk.Label(root, text="Wähle den gewünschten Minecraft Server aus.", font=("shanti", 18))
instructions.grid(columnspan=3, column=0, row=3, padx='5', pady='10')


#browse button Minecraft 1.16.4
browse0_text = tk.StringVar()
browse0_btn = tk.Button(root, textvariable=browse0_text, command=lambda:popupmsg(url0, browse0_text, 'Minecraft 1.16.4 Create'), bg="#20bebe", fg="white", height=3, width=30)
browse0_text.set("Minecraft 1.16.4 Create")
browse0_btn.grid(column=0, row=5, padx='0', pady='0')


#browse button Minecraft 1.16.5
browse1_text = tk.StringVar()
browse1_btn = tk.Button(root, textvariable=browse1_text, command=lambda:noDownload(browse1_text), bg="#20bebe", fg="white", height=3, width=30)
browse1_text.set("Minecraft 1.16.5")
browse1_btn.grid(column=1, row=5, padx='0', pady='0')


#browse button Minecraft Life in the Woods
browse2_text = tk.StringVar()
browse2_btn = tk.Button(root, textvariable=browse2_text, command=lambda:popupmsg(url2, browse2_text, 'Minecraft Life in the Woods'), bg="#20bebe", fg="white", height=3, width=30)
browse2_text.set("Minecraft Life in the Woods")
browse2_btn.grid(column=2, row=5, padx='0', pady='0')


#Textbox
Endtext_Label = tk.Label(root, text='Mods noch nicht geladen.', font=('shanti', 18), fg='red')
Endtext_Label.grid(columnspan=3, column=0, row=6, padx='5', pady='5')


def noDownload(button):
    button.set('Keine Mods verfügbar')


#Popup öffnen Ordner Leer abfrage
def popupmsg(url,button,text):
            popup = tk.Tk()
            popup.wm_title("!")
            label = ttk.Label(popup, text='Ist der Modordner leer?', font=("shanti", 18))
            label.pack(side="top", fill="x", pady=10)
            OkayButton = ttk.Button(popup, text="Okay", command=lambda:[save(url,button,text) or funktion_popup(popup)])
            OkayButton.pack(side="bottom", pady=5)
            OrdnerButton = ttk.Button(popup, text='Öffne Ordner', command=lambda:suche())
            OrdnerButton.pack(side="bottom", pady=20)
   
            
#Popup schließen            
def funktion_popup(popup):
    funktion1=popup.destroy()


#Ordner durchsuchen um Mods zu löschen
def suche():
    if not os.path.exists(suche_path):
        if os.path.exists(suche_path_noMod):
            os.makedirs(suche_path) 
    os.startfile(suche_path, 'explore')

    

#Speichern Funktion mit Download und Extrahieren der Zip
def save(url,button,text):

            #Change Button Name
            button.set("loading...")

            folder = askdirectory(initialdir=suche_path, title="Wähle deinen Mod Ordner")

            #Download der Datei
            r = requests.get(url)

            temp=folder +"/tmp"
            if r is None:
                return None
            file=open(temp, "wb")
            file.write(r.content)
            file.close()

            #Change Button Name
            button.set("Extracting...")

            #Extrahieren der Zip
            zf=ZipFile(temp)
            zf.extractall(path=folder)
            zf.close()
            os.remove(temp)

            #Change Button Name
            button.set(text)

            #Change Endtext
            Endtext_Label.configure (text= text + " Mods sind fertig geladen.\n \n Viel Spaß beim Spielen.", fg='black')


#Programm Ende
root.mainloop()

