from tkinter import *


def scrum(foablak):
    var = IntVar()
    scrum_ablak = Toplevel(foablak, width=600, height=400)
    scrum_ablak.minsize(width=600, height=400)
    scrum_ablak.title("Scrum teszt")
    kerdes1 = Label(text="Hány szerepkör van a scrum-ban?")
    kerdes2 = Label(text="Van-e főnökük a fejlesztőknek?")
    kerdes3 = Label(text="Rugalmas a scrum?")
    kerdes4 = Label(text="Hány dokumentuzm van a scrum-ban?")
    kerdes5 = Label(text="")
    valaszgomb1_1 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb1_2 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb1_3 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb2_1 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb2_2 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb2_3 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb3_1 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb3_2 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb3_3 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb4_1 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb4_2 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb4_3 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb5_1 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb5_2 = Radiobutton(scrum_ablak, text="",variable=var, value=1)
    valaszgomb5_3 = Radiobutton(scrum_ablak, text="",variable=var, value=1)

    
    scrum_ablak.mainloop()