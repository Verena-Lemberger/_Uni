import tkinter as tk
from random import randint

from tkinter import Button


class View(tk.Frame):
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.window.title("Übung 3")

        self.label1 = tk.Label(self.window, font="Artial 11 bold", text="Input 1:", padx=10, pady=10)
        self.label1.grid(row=1, column=0)

        self.entry1 = tk.Entry(self.window)
        self.entry1.grid(row=1, column=1)

        self.label2 = tk.Label(self.window, font="Artial 11 bold", text="Input 2:", padx=10, pady=10)
        self.label2.grid(row=2, column=0)

        self.entry2 = tk.Entry(self.window)
        self.entry2.grid(row=2, column=1)

        self.label3 = tk.Label(self.window, font="Artial 11 bold", text="Result:", padx=10, pady=10)
        self.label3.grid(row=4, column=0)

        self.entry3 = tk.Entry(self.window)
        self.entry3.grid(row=4, column=1)

        self.button_add = Button(self.window, text="+", command=self.btnCallback_add, padx=5, pady=5)
        self.button_add.grid(row=3, column=0)

        self.button_sub = Button(self.window, text="-", command=self.btnCallback_sub, padx=5, pady=5)
        self.button_sub.grid(row=3, column=1)

        self.button_mul = Button(self.window, text="*", command=self.btnCallback_mul, padx=5, pady=5)
        self.button_mul.grid(row=3, column=2)

        self.button_div = Button(self.window, text="/", command=self.btnCallback_div, padx=5, pady=5)
        self.button_div.grid(row=3, column=3)

    def btnCallback_add(self):
        self.caluculate("+")

    def btnCallback_sub(self):
        self.caluculate("-")

    def btnCallback_mul(self):
        self.caluculate("*")

    def btnCallback_div(self):
        self.caluculate("/")

    def caluculate(self, operator):
        result = None
        number1 = int(self.entry1.get())
        number2 = int(self.entry2.get())
        if(operator == "+"):
            result = number1 + number2
        if(operator == "-"):
            result = number1 - number2
        if(operator == "*"):
            result = number1 * number2
        if(operator == "/"):
            result = number1 / number2
        print(result)
        self.entry3.delete(0, len(self.entry3.get()))
        self.entry3.insert(0, result)

    def show(self):
        self.window.mainloop()


v = View()
v.show()
