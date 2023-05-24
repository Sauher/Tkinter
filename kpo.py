from tkinter import *
from random import * 
from time import * 

def dkpo(foablak):
    kpo_ablak = Toplevel(foablak, width=600, height=400)
    kpo_ablak.minsize(width=600, height=400)
    kpo_ablak.maxsize(width=600, height=400)
    kpo_ablak.title("Kő, Papír, olló")


    koigen = False
    papirigen = False
    olloigen = False


    def kovalasztva():
        kob.config(font=("Times", 35))
        papirb.config(font=("Times", 30))
        ollob.config(font=("Times", 30))
        kob.place(anchor=NW,relx=0.08, rely=0.725)
        #kob.place(anchor=NW, relx=0.1, rely=0.75)
        papirb.place(anchor=NW, relx=0.4, rely=0.75)
        ollob.place(anchor=NW, relx=0.7, rely=0.75)
        
        jatekosko = Label(kpo_ablak, text="Kő   ")
        jatekosko.place(anchor=NW, relx=0.08, rely=0.2)
        jatekosko.config(font=("bold", 100))
        jatekostitok.config(font=("", 0))

        koigen == True
        return koigen


    def papirvalasztva():
        kob.config(font=("Times", 30))
        papirb.config(font=("Times", 35))
        ollob.config(font=("Times", 30))
        #papirb.place(anchor=NW, relx=0.4, rely=0.75)
        papirb.place(anchor=NW, relx=0.38, rely=0.725)
        kob.place(anchor=NW, relx=0.1, rely=0.75)
        ollob.place(anchor=NW, relx=0.7, rely=0.75)

        jatekospapir = Label(kpo_ablak, text="Papír")
        jatekospapir.place(anchor=NW, relx=0.08, rely=0.2)
        jatekospapir.config(font=("bold", 80))
        jatekostitok.config(font=("",0))

        papirigen == True
        return papirigen

        


    def ollovalasztva():
        kob.config(font=("Times", 30))
        papirb.config(font=("Times", 30))
        ollob.config(font=("Times", 35))
        #ollob.place(anchor=NW, relx=0.7, rely=0.75)
        ollob.place(anchor=NW, relx=0.68, rely=0.725)
        kob.place(anchor=NW, relx=0.1, rely=0.75)
        papirb.place(anchor=NW, relx=0.4, rely=0.75)

        jatekosollo = Label(kpo_ablak, text="Olló   ")
        jatekosollo.place(anchor=NW, relx=0.08, rely=0.2)
        jatekosollo.config(font=("bold", 100))
        jatekostitok.config(font=("",0))

        olloigen == True
        return olloigen
        
    def felmutat():
        gepvalasztas = randint(0,3)
        if gepvalasztas == 0:
            gepko = Label(kpo_ablak, text="Kő")
            gepko.place(anchor=NW, relx=0, rely=0)
        elif gepvalasztas == 1:
            geppapir = Label(kpo_ablak, text="Papír")
            geppapir.place(anchor=NW, relx=0, rely=0)
        else:
            gepollo = Label(kpo_ablak, text="Olló")
            gepollo.place(anchor=NW, relx=0, rely=0)






    jatekoslab = Label(kpo_ablak, text="Te")
    geplab = Label(kpo_ablak, text="Gép")
    jatekostitok = Label(kpo_ablak, text="?")
    geptitok = Label(kpo_ablak, text="?")
    felmutatb = Button(kpo_ablak, text="Felmutat", command=felmutat)
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
    felmutatb.place(anchor=NW, relx=0.425, rely=0.59)
    felmutatb.config(font=("Times", 15))
    kob.place(anchor=NW, relx=0.1, rely=0.75)
    kob.config(font=("Times", 30))
    papirb.place(anchor=NW, relx=0.4, rely=0.75)
    papirb.config(font=("Times", 30))
    ollob.place(anchor=NW, relx=0.7, rely=0.75)
    ollob.config(font=("Times", 30))

    
    kpo_ablak.mainloop()
    


