from tkinter import *
from random import * 
from time import * 

def dkpo(foablak):
    kpo_ablak = Toplevel(foablak, width=600, height=400)
    kpo_ablak.minsize(width=600, height=400)
    kpo_ablak.maxsize(width=600, height=400)
    kpo_ablak.title("Kő, Papír, olló")

    global koigen
    global papirigen
    global olloigen


    koigen = False
    papirigen = False
    olloigen = False

    def kovalasztva():
        kob.config(font=("Times", 35), bg="white")
        papirb.config(font=("Times", 30), bg="gray")
        ollob.config(font=("Times", 30), bg="gray")
        kob.place(anchor=NW,relx=0.08, rely=0.725)
        #kob.place(anchor=NW, relx=0.1, rely=0.75)
        papirb.place(anchor=NW, relx=0.4, rely=0.75)
        ollob.place(anchor=NW, relx=0.7, rely=0.75)

        felmutatb.place(anchor=NW, relx=0.425, rely=0.59)
        felmutatb.config(font=("Times", 15), bg="white")
        jatekosko = Label(kpo_ablak, text="Kő   ")
        jatekosko.place(anchor=NW, relx=0.08, rely=0.2)
        jatekosko.config(font=("bold", 100))
        jatekostitok.config(font=("", 0))

        global koigen
        global papirigen
        global olloigen
        koigen = True
        papirigen = False
        olloigen = False


    def papirvalasztva():
        kob.config(font=("Times", 30), bg="gray")
        papirb.config(font=("Times", 35), bg="white")
        ollob.config(font=("Times", 30), bg="gray")
        #papirb.place(anchor=NW, relx=0.4, rely=0.75)
        papirb.place(anchor=NW, relx=0.38, rely=0.725)
        kob.place(anchor=NW, relx=0.1, rely=0.75)
        ollob.place(anchor=NW, relx=0.7, rely=0.75)

        felmutatb.place(anchor=NW, relx=0.425, rely=0.59)
        felmutatb.config(font=("Times", 15), bg="white")
        jatekospapir = Label(kpo_ablak, text="Papír")
        jatekospapir.place(anchor=NW, relx=0.08, rely=0.2)
        jatekospapir.config(font=("bold", 80))
        jatekostitok.config(font=("",0))



        global koigen
        global papirigen
        global olloigen        
        koigen = False
        papirigen = True
        olloigen = False
        


    def ollovalasztva():
        kob.config(font=("Times", 30), bg="gray")
        papirb.config(font=("Times", 30), bg="gray")
        ollob.config(font=("Times", 35), bg="white")
        #ollob.place(anchor=NW, relx=0.7, rely=0.75)
        ollob.place(anchor=NW, relx=0.68, rely=0.725)
        kob.place(anchor=NW, relx=0.1, rely=0.75)
        papirb.place(anchor=NW, relx=0.4, rely=0.75)

        felmutatb.place(anchor=NW, relx=0.425, rely=0.59)
        felmutatb.config(font=("Times", 15), bg="white")   
        jatekosollo = Label(kpo_ablak, text="Olló   ")
        jatekosollo.place(anchor=NW, relx=0.08, rely=0.2)
        jatekosollo.config(font=("bold", 100))
        jatekostitok.config(font=("",0))

        global koigen
        global papirigen
        global olloigen
        koigen = False
        papirigen = False
        olloigen = True



    def restart():
        kpo_ablak.destroy()
        dkpo



    def felmutat():
        gepvalasztas = randint(0,3)

        #time.sleep(2.5)
        if gepvalasztas == 0:
            geptitok.place(anchor=NW,relx=1,rely=1)
            gepko = Label(kpo_ablak, text="Kő    ")
            gepko.place(anchor=NW, relx=0.55, rely=0.2)
            gepko.config(font=("bold", 100))
            if koigen == True:
                dontetlenl = Label(kpo_ablak, text="Döntetlen!")
                dontetlenl.place(anchor=NW, relx=0.375, rely=0.625)
                dontetlenl.config(font=("Times", 30), bg="white")
            elif papirigen == True:
                jatekosnyl = Label(kpo_ablak, text="Nyertél!")
                jatekosnyl.place(anchor=NW, relx=0.375, rely=0.625)
                jatekosnyl.config(font=("Times", 30), bg="white")
            elif olloigen == True:
                gepnyl = Label(kpo_ablak, text="Vesztettél!")
                gepnyl.place(anchor=NW, relx=0.375, rely=0.625)
                gepnyl.config(font=("Times", 30), bg="white")   
        elif gepvalasztas == 1:
            geptitok.place(anchor=NW, relx=0.55, rely=0.5)
            geptitok.config(font=("Times",0))
            geppapir = Label(kpo_ablak, text="Papír   ")
            geppapir.place(anchor=NW, relx=0.55, rely=0.25)
            geppapir.config(font=("bold", 65))
            if koigen == True:
                gepnyl = Label(kpo_ablak, text="Vesztettél!")
                gepnyl.place(anchor=NW, relx=0.375, rely=0.625)
                gepnyl.config(font=("Times", 30), bg="white")   
            elif papirigen == True:
                dontetlenl = Label(kpo_ablak, text="Döntetlen!")
                dontetlenl.place(anchor=NW, relx=0.375, rely=0.625)
                dontetlenl.config(font=("Times", 30), bg="white")  
            elif olloigen == True:
                jatekosnyl = Label(kpo_ablak, text="Nyertél!")
                jatekosnyl.place(anchor=NW, relx=0.375, rely=0.625)
                jatekosnyl.config(font=("Times", 30), bg="white")  
        else:
            geptitok.config(font=("Times",0))
            gepollo = Label(kpo_ablak, text="Olló   ")
            gepollo.place(anchor=NW, relx=0.55, rely=0.2)
            gepollo.config(font=("bold", 100))
            if koigen == True:
                jatekosnyl = Label(kpo_ablak, text="Nyertél!")
                jatekosnyl.place(anchor=NW, relx=0.375, rely=0.625)
                jatekosnyl.config(font=("Times", 30), bg="white")  
            elif papirigen == True:
                gepnyl = Label(kpo_ablak, text="Vesztettél!")
                gepnyl.place(anchor=NW, relx=0.375, rely=0.625)
                gepnyl.config(font=("Times", 30), bg="white")                  
            elif olloigen == True:
                dontetlenl = Label(kpo_ablak, text="Döntetlen!")
                dontetlenl.place(anchor=NW, relx=0.375, rely=0.625)
                dontetlenl.config(font=("Times", 30), bg="white")  
        kob.destroy()
        papirb.destroy()
        ollob.destroy()
        felmutatb.destroy()




        restartb = Button(kpo_ablak, text="Kilépés", command=restart)
        restartb.place(anchor=NW, relx=0.375, rely=0.775)
        restartb.config(font=("Times", 30), bg="white")






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

    kob.place(anchor=NW, relx=0.1, rely=0.75)
    kob.config(font=("Times", 30), bg="gray")
    papirb.place(anchor=NW, relx=0.4, rely=0.75)
    papirb.config(font=("Times", 30), bg="gray")
    ollob.place(anchor=NW, relx=0.7, rely=0.75)
    ollob.config(font=("Times", 30), bg="gray")

    
    kpo_ablak.mainloop()
    


