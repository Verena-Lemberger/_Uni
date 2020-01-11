import tkinter as tk
from random import randrange

from tkinter import Button


class View(tk.Frame):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Übung 1")
        self.window.geometry("300x300")

        self.button = Button(self.window, command=self.btnCallback, padx = 20, pady = 20)
        self.button.place(x=50, y=50)

    def btnCallback(self):
        newX = randrange(200)
        newY = randrange(200)
        print(newX, newY)
        self.button.place(x=newX, y=newY)
        
    def show(self):
        self.window.mainloop()


v = View()
v.show()
