from tkinter import *
from string import ascii_lowercase
from random import choice

def akasztofa_toplevel(foablak):

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
    
    for betu in ascii_lowercase:
        gombok = Button(top, text=betu, command= lambda x = betu: betu_bevitel(x))
        gombok.grid(row=sor, column=oszlop)
        oszlop += 1
        if oszlop % 8 == 0:
            oszlop = 0
            sor += 1


