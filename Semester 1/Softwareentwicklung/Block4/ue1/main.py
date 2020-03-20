import tkinter as tk
from random import randint

from tkinter import Button


class View(tk.Frame):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Übung 1")
        self.window.geometry("300x300")

        self.button = Button(self.window, command=self.btnCallback, padx = 10, pady = 10)
        self.button.place(x=50, y=50)

    def btnCallback(self):
        # generate a random 
        newX = randint(50, 250)
        newY = randint(50, 250)
        print(newX, newY)
        self.button.place(x=newX, y=newY)
        
    def show(self):
        self.window.mainloop()


v = View()
v.show()
