from tkinter import *
from kpo import dkpo
from TKaSZ import dtkasz

ablak = Tk()
ablak.title("Főmenü")
ablak.geometry("600x400")

udvozles = Label(ablak, text="Üdvözöllek a minijáték kollekciónkban", font=("Arial", 22))
udvozles.place(relx=0.5, rely=0.4, anchor=CENTER)
jo_jatekot = Label(ablak, text="Jó játékot!", font=("Arial", 22))
jo_jatekot.place(relx=0.5, rely=0.5, anchor=CENTER)

menusor = Frame(ablak)
menusor.pack(side=TOP, fill=X)

akasztofa_gomb = Button(menusor, text="Akasztófa")
akasztofa_gomb.pack(side=LEFT)
kpo_gomb = Button(menusor, text="Kő papír olló", command=lambda:dkpo(ablak))
kpo_gomb.pack(side=LEFT)
scrum_gomb = Button(menusor, text="Scrum teszt")
scrum_gomb.pack(side=LEFT)
tkasz_gomb = Button(menusor, text="Találd ki a számot",command=lambda:dtkasz(ablak))
tkasz_gomb.pack(side=LEFT)

ablak.mainloop()
