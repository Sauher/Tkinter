from tkinter import *
from random import *


def dtkasz(foablak):
    tkasz_ablak = Toplevel(foablak, height=400, width=600)
    tkasz_ablak.minsize(width=600, height=400)
    tkasz_ablak.title("Találd ki a számot!")
    
    diff_lab = Label(tkasz_ablak, text="Nehézségi szint:")
    konnyu_lab = Label(tkasz_ablak, text="Könnyű:")
    konnyu_radio = Radiobutton(tkasz_ablak)
    kozepes_lab = Label(tkasz_ablak, text="Közepes:")
    kozepes_radio = Radiobutton(tkasz_ablak)
    nehez_lab = Label(tkasz_ablak, text="Nehéz:")
    nehez_radio = Radiobutton(tkasz_ablak)
    inditas_button = Button(tkasz_ablak, text="Indtítás")
    flavor_lab = Label(tkasz_ablak, text="Találd ki a számot:")
    talaldki_ent = Entry(tkasz_ablak)
    bevitel_button = Button(tkasz_ablak, text="Bevitel")




    diff_lab.grid(row=0,column=0)
    konnyu_lab.grid(row=1,column=0)
    konnyu_radio.grid(row=1,column=1)
    kozepes_lab.grid(row=2,column=0)
    kozepes_radio.grid(row=2,column=1)
    nehez_lab.grid(row=3,column=0)
    nehez_radio.grid(row=3,column=1)
    inditas_button.grid(row=3,column=2)
    flavor_lab.grid(row=4,column=0)
    talaldki_ent.grid(row=4,column=1)
    bevitel_button.grid(row=5)

    tkasz_ablak.mainloop()