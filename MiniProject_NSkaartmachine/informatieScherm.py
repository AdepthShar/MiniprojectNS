from tkinter import *

def createInformatieWindow():
    # Instellingen voor het informatiescherm
    root = Tk()                                             # Hoofdschermroot.
    root.configure(background='#f7d117')                    # Window Achtergrond kleur
    root.title("NS Kaartautomaat - Reisinformatiescherm")   # Window Titel
    root.geometry('1000x700')                               # Window Size
    root.iconbitmap('logo.ico')                             # Window Icon

    root.mainloop()
