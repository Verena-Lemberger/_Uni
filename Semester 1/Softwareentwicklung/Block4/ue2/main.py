import tkinter as tk
from random import randint

from tkinter import Button
from tkinter import messagebox


class View(tk.Frame):
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.title("Übung 2")

        self.heading = tk.Label(self.window, font="Artial 11 bold", text="Jahr:")
        self.heading.grid(row=0, column=0, columnspan=2, padx=20, pady=5)

        self.entry = tk.Entry(self.window)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E, padx=20)

        self.button = Button(self.window, text="Berechnen", command=self.btnCallback, padx=10, pady=10)
        self.button.grid(row=2, column=0, columnspan=2, sticky=tk.W + tk.E, padx=20)

    def isLeapYear(self, year):
        isLeapYear = False
        # case 1: divide by 4 without rest
        if((year % 4) > 0):
            return isLeapYear
        # case 2: is secular year
        if((year % 400) == 0):
            isLeapYear = True
            return isLeapYear
        # case 3: is secular year
        if((year % 100) == 0):
            return isLeapYear

        isLeapYear = True
        return isLeapYear

    def btnCallback(self):
        year = int(self.entry.get())
        messagebox.showerror("Information", ("{} ist {} Schaltjahr".format(year, "ein" if self.isLeapYear(year) else "kein")))

    def show(self):
        self.window.mainloop()


v = View()
v.show()
