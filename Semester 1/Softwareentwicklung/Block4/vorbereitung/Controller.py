class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_listener(self.change_value)

    def change_value(self, value):
        fahrenheit = self.model.calc_fahrenheit(value)
        celcius = self.model.calc_celcius(value)
        self.view.set_values(fahrenheit, celcius)

    def start(self):
        self.change_value(0)
        self.view.show()