from tkinter import *


def scrum(foablak):
    def beadas():
        pontszam = 0
        if k1.get() == True:
            pontszam +=1
        if k2.get() == True:
            pontszam +=1
        if k3.get() == True:
            pontszam +=1
        if k4.get() == True:
            pontszam +=1
        if k5.get() == True:
            pontszam +=1
        eredmeny = Label(scrum_ablak, text="A pontszámod: "+str(pontszam)+".",borderwidth=1,relief="solid", width=30, height=5)
        eredmeny.place(relx=0.30, rely=0.70, anchor=NW)
    k1 = BooleanVar()
    k2 = BooleanVar()
    k3 = BooleanVar()
    k4 = BooleanVar()
    k5 = BooleanVar()
    scrum_ablak = Toplevel(foablak, width=600, height=400)
    scrum_ablak.minsize(width=600, height=400)
    scrum_ablak.title("Scrum teszt")
    kerdes1 = Label(scrum_ablak,text="Hány szerepkör van a scrum-ban?",font=25)
    kerdes2 = Label(scrum_ablak,text="Van-e főnökük a fejlesztőknek?",font=25)
    kerdes3 = Label(scrum_ablak,text="Rugalmas a scrum?",font=25)
    kerdes4 = Label(scrum_ablak,text="Hány dokumentum van a scrum-ban?",font=25)
    kerdes5 = Label(scrum_ablak,text="Hány esemény van a scrumban?",font=25)
    valaszgomb1_1 = Radiobutton(scrum_ablak, text="5",variable=k1, value=False)
    valaszgomb1_2 = Radiobutton(scrum_ablak, text="3",variable=k1, value=True)
    valaszgomb1_3 = Radiobutton(scrum_ablak, text="4",variable=k1, value=False)
    valaszgomb2_1 = Radiobutton(scrum_ablak, text="Nincs",variable=k2, value=True)
    valaszgomb2_2 = Radiobutton(scrum_ablak, text="Van",variable=k2, value=False)
    valaszgomb2_3 = Radiobutton(scrum_ablak, text="Totya a főnök",variable=k2, value=False)
    valaszgomb3_1 = Radiobutton(scrum_ablak, text="Igen",variable=k3, value=True)
    valaszgomb3_2 = Radiobutton(scrum_ablak, text="Nem",variable=k3, value=False)
    valaszgomb3_3 = Radiobutton(scrum_ablak, text="Félig",variable=k3, value=False)
    valaszgomb4_1 = Radiobutton(scrum_ablak, text="4",variable=k4, value=False)
    valaszgomb4_2 = Radiobutton(scrum_ablak, text="3",variable=k4, value=True)
    valaszgomb4_3 = Radiobutton(scrum_ablak, text="6",variable=k4, value=False)
    valaszgomb5_1 = Radiobutton(scrum_ablak, text="3",variable=k5, value=False)
    valaszgomb5_2 = Radiobutton(scrum_ablak, text="7",variable=k5, value=False)
    valaszgomb5_3 = Radiobutton(scrum_ablak, text="5",variable=k5, value=True)
    beadasgomb = Button(scrum_ablak, text="Beadás", command=beadas)

    kerdes1.place(relx=0.02, rely=0.02, anchor=NW)
    kerdes2.place(relx=0.02, rely=0.10, anchor=NW)
    kerdes3.place(relx=0.02, rely=0.18, anchor=NW)
    kerdes4.place(relx=0.02, rely=0.26, anchor=NW)
    kerdes5.place(relx=0.02, rely=0.34, anchor=NW)
    valaszgomb1_1.place(relx=0.20, rely=0.01, anchor=NW)
    valaszgomb1_2.place(relx=0.20, rely=0.04, anchor=NW)
    valaszgomb1_3.place(relx=0.20, rely=0.07, anchor=NW)
    valaszgomb2_1.place(relx=0.20, rely=0.20, anchor=NW)
    valaszgomb2_2.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb2_3.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb3_1.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb3_2.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb3_3.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb4_1.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb4_2.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb4_3.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb5_1.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb5_2.place(relx=0.20, rely=0.22, anchor=NW)
    valaszgomb5_3.place(relx=0.20, rely=0.50, anchor=NW)
    beadasgomb.place(relx=0.60, rely=0.60, anchor=NW)

    
    scrum_ablak.mainloop()