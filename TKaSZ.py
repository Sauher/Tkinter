from tkinter import *
from random import *


def dtkasz(foablak):
    tkasz_ablak = Toplevel(foablak, height=400, width=600)
    tkasz_ablak.minsize(width=600, height=400)
    tkasz_ablak.title("Találd ki a számot!")
    #----------------------------------------------------------------






    #----------------------------------------------------------------
    diff_lab = Label(tkasz_ablak, text="Nehézségi szint:")
    konnyu_lab = Label(tkasz_ablak, text="  Könnyű:")
    konnyu_radio = Radiobutton(tkasz_ablak)
    kozepes_lab = Label(tkasz_ablak, text="  Közepes:")
    kozepes_radio = Radiobutton(tkasz_ablak)
    nehez_lab = Label(tkasz_ablak, text="  Nehéz:")
    nehez_radio = Radiobutton(tkasz_ablak)
    inditas_button = Button(tkasz_ablak, text="Indtítás")
    flavor_lab = Label(tkasz_ablak, text="Találd ki a számot:")
    talaldki_ent = Entry(tkasz_ablak, width=50)
    bevitel_button = Button(tkasz_ablak, text="Bevitel")




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

    bevitel_button.place(relx=0.631,rely=0.35, anchor=NW)


    tkasz_ablak.mainloop()