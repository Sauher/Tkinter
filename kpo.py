from tkinter import *


def dkpo(foablak):
    kpo_ablak = Toplevel(foablak, width=600, height=400)
    kpo_ablak.minsize(width=600, height=400)
    kpo_ablak.maxsize(width=600, height=400)
    kpo_ablak.title("Kő, Papír, olló")

    def kovalasztva():
        kob.config(font=("Times", 35))
        papirb.config(font=("Times", 30))
        ollob.config(font=("Times", 30))
        kob.place(anchor=NW,relx=0.08, rely=0.725)
    def papirvalasztva():
        kob.config(font=("Times", 30))
        papirb.config(font=("Times", 35))
        ollob.config(font=("Times", 30))
    def ollovalasztva():
        kob.config(font=("Times", 30))
        papirb.config(font=("Times", 30))
        ollob.config(font=("Times", 35))







    jatekoslab = Label(kpo_ablak, text="Te")
    geplab = Label(kpo_ablak, text="Gép")
    jatekostitok = Label(kpo_ablak, text="?")
    geptitok = Label(kpo_ablak, text="?")
    felmutatb = Button(kpo_ablak, text="Felmutat")
    kob = Button(kpo_ablak, text="Kő     ", command=kovalasztva)
    papirb = Button(kpo_ablak, text="Papír ", command=papirvalasztva)
    ollob = Button(kpo_ablak, text="Olló ", command=ollovalasztva)




    jatekoslab.place(anchor=NW, relx=0.1, rely=0.04)
    jatekoslab.config(font=('bold',30))
    geplab.place(anchor=NE, relx=0.9, rely=0.04)
    geplab.config(font=("bold", 30))
    jatekostitok.place(anchor=NW, relx=0.15, rely=0.2)
    jatekostitok.config(font=("bold", 100))
    geptitok.place(anchor=NE, relx=0.85, rely=0.2)
    geptitok.config(font=("bold", 100))
    felmutatb.place(anchor=NW, relx=0.425, rely=0.55)
    felmutatb.config(font=("Times", 15))
    kob.place(anchor=NW, relx=0.1, rely=0.75)
    kob.config(font=("Times", 30))
    papirb.place(anchor=NW, relx=0.4, rely=0.75)
    papirb.config(font=("Times", 30))
    ollob.place(anchor=NW, relx=0.7, rely=0.75)
    ollob.config(font=("Times", 30))

    
    kpo_ablak.mainloop()
    
