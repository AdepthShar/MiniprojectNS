from tkinter import *
from tkinter.messagebox import showinfo
from informatieScherm import createInformatieWindow

# from reisInformatie import *

# Instellingen voor het hoofdscherm
root = Tk()                           # Hoofdschermroot.
root.configure(background='#f7d117')  # Window Achtergrond kleur
root.title("NS Kaartautomaat")        # Window Titel
root.geometry('1000x700')             # Window Size
root.iconbitmap('logo.ico')           # Window Icon

mainLabel = Label(master=root, text='Welkom bij NS', background='#f7d117', pady=90, font=('Frutiger LT Std 57 Cn Bold', 50), fg='#00387b')
mainLabel.pack()

# Functies
def nietWerkend():
    bericht = 'Deze functie werkt (nog) niet!'
    showinfo(title='Melding', message=bericht)

def openInformatieScherm():
    createInformatieWindow()

def closeApplicatie():
    root.destroy()

# def getReisInformatie():
#

# def getReisInformatieStation():
#

# Alle knoppen op main screen
buttonFrameCenter = Frame(master=root, background='#f7d117')
buttonFrameCenter.pack(anchor='c')

knop1 = Button(master=buttonFrameCenter, text="Kopen los kaartje", fg="white", bg="#00387b", height=3, width=15, wraplength=90, bd=0, command=nietWerkend)
knop1.pack(side=LEFT, padx=10, pady=5)

knop2 = Button(master=buttonFrameCenter, text="Kopen anonieme OV-Chipkaart", fg="white", bg="#00387b", height=3, width=15, wraplength=100, bd=0, command=nietWerkend)
knop2.pack(side=LEFT, padx=10, pady=10)

knop3 = Button(master=buttonFrameCenter, text="Ik wil naar het buitenland", fg="white", bg="#00387b", height=3, width=15, wraplength=90, bd=0, command=nietWerkend)
knop3.pack(side=LEFT, padx=10, pady=10)

# Deze knop moet het informatie scherm openen
knop4 = Button(master=buttonFrameCenter, text="Actuele reisinformatie", fg="white", bg="#00387b", height=3, width=15, wraplength=90, bd=0, command=openInformatieScherm)
knop4.pack(side=LEFT, padx=10, pady=10)

# Sluit de applicatie
knop5 = Button(master=buttonFrameCenter, text="Sluit af", fg="white", bg="#00387b", height=3, width=15, wraplength=90, bd=0, command=closeApplicatie)
knop5.pack(side=LEFT, padx=10, pady=10)

root.mainloop()