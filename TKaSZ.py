from tkinter import *
from random import *


def dtkasz(foablak):
    tkasz_ablak = Toplevel(foablak, height=400, width=600)
    tkasz_ablak.minsize(width=600, height=400)
    tkasz_ablak.maxsize(width=600, height=400)
    tkasz_ablak.title("Találd ki a számot!")
    #----------------------------------------------------------------

    talalatoklab = Label(tkasz_ablak, text="")
    nehezseg = 0
    hibal = Label(tkasz_ablak,text="Kérlek előszőr válassz egy nehézségi szintet!")


    def inditas():
        global talalatok
        global randomszam
        global rvl
        
        if  nehezseg.get() == 1:
            rvl = []
            randomszam = randint(1,50)
            talalatok = 8
            rvl.append([randomszam,talalatok])
            gondolatlab = Label(tkasz_ablak, text="Gondoltam egy számra 1 és 50 között!")
            talalatoklab = Label(tkasz_ablak, text="Hátralévő találatok:")
            talalatokszaml = Label(tkasz_ablak, text=str(rvl[0][1]))
            talalatokszaml.place(anchor=NW, relx=0.2, rely=0.45)
            gondolatlab.place(anchor=NW, relx=0.02, rely=0.40)
            talalatoklab.place(anchor=NW, relx=0.02,   rely=0.45)
            bevitel_button.place(relx=0.631,rely=0.35, anchor=NW)
            hibal.config(text="")
            return rvl
        elif nehezseg.get() == 2:
            rvl = []
            randomszam = randint(1, 75)
            talalatok = 5
            rvl.append([randomszam,talalatok])
            gondolatlab = Label(tkasz_ablak, text="Gondoltam egy számra 1 és 75 között!")
            talalatoklab = Label(tkasz_ablak, text="Hátralévő találatok:")
            talalatokszaml = Label(tkasz_ablak, text=str(rvl[0][1]))
            talalatokszaml.place(anchor=NW, relx=0.2, rely=0.45)
            gondolatlab.place(anchor=NW, relx=0.02, rely=0.40)
            talalatoklab.place(anchor=NW, relx=0.02,   rely=0.45)
            bevitel_button.place(relx=0.631,rely=0.35, anchor=NW)
            hibal.config(text="")
            return rvl
        elif nehezseg.get() == 3:
            rvl = []
            randomszam = randint(1,100)
            talalatok = 3
            rvl.append([randomszam,talalatok])
            gondolatlab = Label(tkasz_ablak, text="Gondoltam egy számra 1 és 100 között!")
            talalatoklab = Label(tkasz_ablak, text="Hátralévő találatok:")
            talalatokszaml = Label(tkasz_ablak, text=str(rvl[0][1]))
            talalatokszaml.place(anchor=NW, relx=0.2, rely=0.45)
            gondolatlab.place(anchor=NW, relx=0.02, rely=0.40)
            talalatoklab.place(anchor=NW, relx=0.02,   rely=0.45)
            bevitel_button.place(relx=0.631,rely=0.35, anchor=NW)
            hibal.config(text="")
            return rvl
        else:
            hibal.place(anchor=NW,relx=0.02, rely=0.5)
            hibal.config(font=("Times", 15))
    def bevitel():
        tippv = talaldki_ent.get()
        if rvl[0][1] > 1:
            rvl[0][1] -= 1
            if int(tippv) > randomszam:
                nagyobbl = Label(tkasz_ablak, text="A szám amire gondoltam kissebb!   ")
                nagyobbl.place(anchor=NW, relx=0.02, rely=0.55)
                talalatokszaml = Label(tkasz_ablak, text=str(rvl[0][1]))
                talalatokszaml.place(anchor=NW, relx=0.2, rely=0.45)
            elif int(tippv) < randomszam:
                kisebbl = Label(tkasz_ablak, text="A szám amire gondoltam nagyobb!")
                kisebbl.place(anchor=NW, relx=0.02, rely=0.55)
                talalatokszaml = Label(tkasz_ablak, text=str(rvl[0][1]))
                talalatokszaml.place(anchor=NW, relx=0.2, rely=0.45)
            else:
                telibel = Label(tkasz_ablak, text="Eltaláltad a számot, nyertél!")
                telibel.place(anchor=NW, relx=0.02, rely=0.6)
                bevitel_button.destroy()
                kilepesb = Button(tkasz_ablak, text="Kilépés", command=exit)
                kilepesb.place(anchor=NW, relx=0.02, rely=0.75)
        else:
            rvl[0][1] -= 1
            elfogylab = Label(tkasz_ablak, text="Elfogytak a találataid, vesztettél!")
            elfogylab.place(anchor=NW, relx=0.02, rely=0.7)
            bevitel_button.destroy()
            talalatokszaml = Label(tkasz_ablak, text=str(rvl[0][1]))
            talalatokszaml.place(anchor=NW, relx=0.2, rely=0.45)
            kilepesb = Button(tkasz_ablak, text="Kilépés", command=exit)
            kilepesb.place(anchor=NW, relx=0.02, rely=0.85)
            reveall = Label(tkasz_ablak, text="A szám amire gondoltam:")
            reveall.place(anchor=NW, relx=0.02, rely=0.75)
            revealsz = Label(tkasz_ablak, text=str(rvl[0][0]))
            revealsz.place(anchor=NW, relx=0.25, rely=0.75)
    def exit():
        tkasz_ablak.destroy()

    #----------------------------------------------------------------
    nehezseg = IntVar()
    diff_lab = Label(tkasz_ablak, text="Nehézségi szint:")
    konnyu_lab = Label(tkasz_ablak, text="  Könnyű:")
    konnyu_radio = Radiobutton(tkasz_ablak , variable=nehezseg, value=1)
    kozepes_lab = Label(tkasz_ablak, text="  Közepes:")
    kozepes_radio = Radiobutton(tkasz_ablak, variable=nehezseg, value=2)
    nehez_lab = Label(tkasz_ablak, text="  Nehéz:")
    nehez_radio = Radiobutton(tkasz_ablak , variable=nehezseg, value=3)
    inditas_button = Button(tkasz_ablak, text="Indtítás", command=inditas)
    flavor_lab = Label(tkasz_ablak, text="Találd ki a számot:")
    talaldki_ent = Entry(tkasz_ablak, width=50)
    bevitel_button = Button(tkasz_ablak, text="Bevitel", command=bevitel)




    diff_lab.place(relx=0.02,rely=0.05, anchor=NW)
    konnyu_lab.place(relx=0.02,rely=0.10, anchor=NW)
    kozepes_lab.place(relx=0.02,rely=0.15, anchor=NW)
    nehez_lab.place(relx=0.02,rely=0.20, anchor=NW)

    konnyu_radio.place(relx=0.12,rely=0.10, anchor=NW)
    kozepes_radio.place(relx=0.12,rely=0.15, anchor=NW)
    nehez_radio.place(relx=0.12,rely=0.20, anchor=NW)

    inditas_button.place(relx=0.2,rely=0.18, anchor=NW)

    flavor_lab.place(relx=0.02,rely=0.28, anchor=NW)
    talaldki_ent.place(relx=0.2,rely=0.28, anchor=NW)

    bevitel_button.place(relx=1,rely=1, anchor=NW)


    tkasz_ablak.mainloop()