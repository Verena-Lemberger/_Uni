import tkinter as tk


class View(tk.Frame):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Fahrenheit / Celcius Umrechner")

        self.__listener = None

        self.heading = tk.Label(self.window, font="Artial 11 bold", text="Fahrenheit / Celcius Umrechner")
        self.heading.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.entry = tk.Scale(self.window, from_=-200, to=200, orient="horizontal", command = self.trigger_action)
        self.entry.grid(row=1, column=0, columnspan=2, sticky=tk.W + tk.E, padx=20)

        self.fahrenheit = tk.Label(self.window, font="Artial 9 bold", text="Fahrenheit")
        self.fahrenheit.grid(row=2, column=0, pady=20)

        self.celcius = tk.Label(self.window, font="Artial 9 bold", text="celcius")
        self.celcius.grid(row=2, column=1, pady=20)

    @property
    def value(self):
        return self.entry.get()

    def set_listener(self, listener):
        self.__listener = listener

    def trigger_action(self, value):
        if(self.__listener):
            self.__listener(int(value))

    def set_values(self, fahrenheit, celcius):
        self.fahrenheit["text"] = "{:.2f}° C entspricht \n {:.2f} °F".format(self.value, fahrenheit)
        self.celcius["text"] = "{:.2f}° F entspricht \n {:.2f} °C".format(self.value, celcius)
    
    def show(self):
        self.window.mainloop()
