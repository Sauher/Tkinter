from tkinter import *
from string import ascii_lowercase
from random import choice

def akasztofa_toplevel(foablak):

    global szo
    global hibak
    global kitalalt_betuk

    def random_szo():
        szavak = open("szavak.txt").read().splitlines()
        random_szo = choice(szavak)
        return random_szo

    def betu_bevitel(betu):
        print(betu)
    

    top = Toplevel(foablak)
    top.geometry("600x400")
    top.title("Akasztófa")

    oszlop = 0
    sor = 1
    
    def uj_jatek():
        global szo
        global hibak
        global kitalalt_betuk
        szo = random_szo()
        hibak = 0
        kitalalt_betuk = []
    
    for betu in ascii_lowercase:
        gombok = Button(top, text=betu, command= lambda x = betu: betu_bevitel(x))
        gombok.grid(row=sor, column=oszlop)
        oszlop += 1
        if oszlop % 8 == 0:
            oszlop = 0
            sor += 1

    uj_jatek_gomb = Button(top, text="Új játék", command=uj_jatek)

    uj_jatek()


