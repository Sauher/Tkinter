from tkinter import *
lay = []


def scrum(foablak):
    def exit_btn():
        scrum_ablak = lay[0]
        scrum_ablak.quit()
        scrum_ablak.destroy()
    def beadas():
        pontszam = 0
        if k1.get() == 1:
            pontszam +=1
        if k2.get() == 1:
            pontszam +=1
        if k3.get() == 1:
            pontszam +=1
        if k4.get() == 1:
            pontszam +=1
        if k5.get() == 1:
            pontszam +=1
        eredmeny = Label(scrum_ablak, text="A pontszámod: "+str(pontszam)+".",borderwidth=1,relief="solid", width=30, height=5)
        eredmeny.place(relx=0.25, rely=0.80, anchor=NW)
    k1 = IntVar()
    k2 = IntVar()
    k3 = IntVar()
    k4 = IntVar()
    k5 = IntVar()
    scrum_ablak = Toplevel(foablak, width=600, height=400)
    lay.append(scrum_ablak)
    scrum_ablak.minsize(width=600, height=400)
    scrum_ablak.title("Scrum teszt")
    kerdes1 = Label(scrum_ablak,text="Hány szerepkör van a scrum-ban?",font=("Arial",15))
    kerdes2 = Label(scrum_ablak,text="Van-e főnökük a fejlesztőknek?",font=("Arial",15))
    kerdes3 = Label(scrum_ablak,text="Rugalmas a scrum?",font=("Arial",15))
    kerdes4 = Label(scrum_ablak,text="Hány dokumentum van a scrum-ban?",font=("Arial",15))
    kerdes5 = Label(scrum_ablak,text="Hány esemény van a scrumban?",font=("Arial",15))
    valaszgomb1_1 = Radiobutton(scrum_ablak, text="5",variable=k1, value=0)
    valaszgomb1_2 = Radiobutton(scrum_ablak, text="3",variable=k1, value=1)
    valaszgomb1_3 = Radiobutton(scrum_ablak, text="4",variable=k1, value=2)
    valaszgomb2_1 = Radiobutton(scrum_ablak, text="Nincs",variable=k2, value=1)
    valaszgomb2_2 = Radiobutton(scrum_ablak, text="Van",variable=k2, value=2)
    valaszgomb2_3 = Radiobutton(scrum_ablak, text="Totya a főnök",variable=k2, value=0)
    valaszgomb3_1 = Radiobutton(scrum_ablak, text="Igen",variable=k3, value=1)
    valaszgomb3_2 = Radiobutton(scrum_ablak, text="Nem",variable=k3, value=2)
    valaszgomb3_3 = Radiobutton(scrum_ablak, text="Félig",variable=k3, value=0)
    valaszgomb4_1 = Radiobutton(scrum_ablak, text="4",variable=k4, value=2)
    valaszgomb4_2 = Radiobutton(scrum_ablak, text="3",variable=k4, value=1)
    valaszgomb4_3 = Radiobutton(scrum_ablak, text="6",variable=k4, value=0)
    valaszgomb5_1 = Radiobutton(scrum_ablak, text="3",variable=k5, value=2)
    valaszgomb5_2 = Radiobutton(scrum_ablak, text="7",variable=k5, value=0)
    valaszgomb5_3 = Radiobutton(scrum_ablak, text="5",variable=k5, value=1)
    beadasgomb = Button(scrum_ablak, text="Beadás", command=beadas)
    kilepesgomb = Button(scrum_ablak, text="Kilépés", command=exit_btn)

    kerdes1.place(relx=0.02, rely=0.02, anchor=NW)
    kerdes2.place(relx=0.02, rely=0.17, anchor=NW)
    kerdes3.place(relx=0.02, rely=0.32, anchor=NW)
    kerdes4.place(relx=0.02, rely=0.47, anchor=NW)
    kerdes5.place(relx=0.02, rely=0.62, anchor=NW)
    valaszgomb1_1.place(relx=0.60, rely=0.01, anchor=NW)
    valaszgomb1_2.place(relx=0.60, rely=0.06, anchor=NW)
    valaszgomb1_3.place(relx=0.60, rely=0.11, anchor=NW)
    valaszgomb2_1.place(relx=0.60, rely=0.16, anchor=NW)
    valaszgomb2_2.place(relx=0.60, rely=0.21, anchor=NW)
    valaszgomb2_3.place(relx=0.60, rely=0.26, anchor=NW)
    valaszgomb3_1.place(relx=0.60, rely=0.31, anchor=NW)
    valaszgomb3_2.place(relx=0.60, rely=0.36, anchor=NW)
    valaszgomb3_3.place(relx=0.60, rely=0.41, anchor=NW)
    valaszgomb4_1.place(relx=0.60, rely=0.46, anchor=NW)
    valaszgomb4_2.place(relx=0.60, rely=0.51, anchor=NW)
    valaszgomb4_3.place(relx=0.60, rely=0.56, anchor=NW)
    valaszgomb5_1.place(relx=0.60, rely=0.61, anchor=NW)
    valaszgomb5_2.place(relx=0.60, rely=0.66, anchor=NW)
    valaszgomb5_3.place(relx=0.60, rely=0.71, anchor=NW)
    beadasgomb.place(relx=0.10, rely=0.875, anchor=NW)
    kilepesgomb.place(relx=0.60, rely=0.875, anchor=NW)

    valaszgomb1_1.select()
    valaszgomb2_1.select()
    valaszgomb3_1.select()
    valaszgomb4_1.select()
    valaszgomb5_1.select()


    scrum_ablak.mainloop()