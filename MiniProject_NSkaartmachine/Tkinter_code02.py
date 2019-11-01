from tkinter import *
from tkinter.messagebox import showinfo
from Miniprojectkopie.NS_API_Miniproject import *


def stationClick():
    stationInput = stationEntry.get()

    frameMidden = Frame(master=infoFrame, background='#f7d117')
    frameMidden.pack(anchor='c', side=BOTTOM)

    if stationInput == '':
        bericht = "U heeft geen station ingevoerd"
        showinfo(title='Error', message=bericht)
    else:
        index = 0
        index01 = 0

        # label01 = Label()
        label01 = Label(master=frameMidden, text=("Actuele reisinformatie {}: ".format(stationInput)), bg='#f7d117', pady=90, font=('Frutiger LT Std 57 Cn Bold', 20), fg='#00387b', anchor='n')
        label01.pack()
        stations = NS_API(stationInput)

        for station in stations:
            label02 = Label(master=frameMidden, text=("De {} naar {} vertrekt om {} van spoor {}".format(station['soort'], station['station'], station['time'], station['spoor'])), bg='#f7d117', font=('Arial', 8, 'bold'))
            label02.pack()
            index += 40
            index01 += 1
            if index01 == 10:
                break


def reisinformatieClick():
    startframe.pack_forget()
    infoFrame.pack()


def toonHoofdMenuFrame():
    infoFrame.pack_forget()
    startframe.pack()


# def back02():
#     extraframe.pack_forget()  # Hij vergeet het extraframe niet, maar overschrijft het gewoon(31/10(16:16))
#     infoFrame.pack()


def ErrorClick():
    bericht = "Error! Deze functie werkt nog niet."
    showinfo(title='Error', message=bericht)


def closeApplicatie():
    root.destroy()


# Start TKinter
root = Tk()

# Root Settings
root.title("NS Kaartautomaat")
root.geometry("800x400")
root.resizable(0, 0)

# ------ StartFrame ------
startframe = Frame(master=root)
startframe.pack(fill='both', expand=True)
startframe.configure(background='#f7d117')

mainLabel = Label(master=startframe, text='Welkom bij NS', background='#f7d117', pady=90, font=('Frutiger LT Std 57 Cn Bold', 50), fg='#00387b')
mainLabel.pack()

buttonFrameCenter = Frame(master=startframe, background='#f7d117')
buttonFrameCenter.pack(anchor='c')

knop1 = Button(master=buttonFrameCenter, text="Kopen los kaartje", fg="white", bg="#00387b", height=3, width=15, wraplength=90, bd=0, command=ErrorClick)
knop1.pack(side=LEFT, padx=10, pady=5)

knop2 = Button(master=buttonFrameCenter, text="Kopen anonieme OV-Chipkaart", fg="white", bg="#00387b", height=3, width=15, wraplength=100, bd=0, command=ErrorClick)
knop2.pack(side=LEFT, padx=10, pady=10)

knop3 = Button(master=buttonFrameCenter, text="Ik wil naar het buitenland", fg="white", bg="#00387b", height=3, width=15, wraplength=90, bd=0, command=ErrorClick)
knop3.pack(side=LEFT, padx=10, pady=10)

knop4 = Button(master=buttonFrameCenter, text="Actuele reisinformatie", fg="white", bg="#00387b", height=3, width=15, wraplength=90, bd=0, command=reisinformatieClick)
knop4.pack(side=LEFT, padx=10, pady=10)

knop5 = Button(master=startframe, text="Sluit af", fg="white", bg="darkred", height=3, width=15, wraplength=90, bd=0, command=closeApplicatie)
knop5.pack(side=RIGHT, padx=10, pady=10)


# ------ infoFrame ------
infoFrame = Frame(master=root)
infoFrame.pack(fill='both', expand=True)
infoFrame.configure(background='#f7d117')

frameBottom = Frame(master=infoFrame, background='#f7d117')
frameBottom.pack(anchor='se', side=BOTTOM)

stationNaam = Label(master=infoFrame, text="Vul uw station in: ", font=('Arial', 15, 'bold'), background="#f7d117")
stationNaam.pack()

frameCenter = Frame(master=infoFrame, background='#f7d117')
frameCenter.pack(anchor='c')

stationEntry = Entry(master=frameCenter, font=('Arial', 15, 'bold'))
stationEntry.pack(side=LEFT)

button07 = Button(master=frameCenter, text="Enter", command=stationClick, fg="white", bg="#00387b", height=1, width=5, wraplength=90, bd=0, padx=10, pady=10)
button07.pack()

button02 = Button(master=frameBottom, text='Terug', command=toonHoofdMenuFrame, fg="white", bg="darkred", height=1, width=5, wraplength=90, bd=0, padx=10, pady=10)
button02.pack(side=RIGHT, padx=10, pady=10)

# toonHoofdMenuFrame()
root.mainloop()
