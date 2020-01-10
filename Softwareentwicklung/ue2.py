class Vehicle:
    def __init__(self, tires):
        self.number_of_tires = 0
        self.max_tires = tires

    def add_tire(self):
        self.number_of_tires = self.number_of_tires + 1

    def remove_tire(self):
        self.number_of_tires = self.number_of_tires - 1

    def drive(self):
        print("I can drive", self.number_of_tires ==
              self.max_tires and self.max_tires > 1)


class Motorbike(Vehicle):
    def __init__(self, max_tires):
        super().__init__(max_tires)


class Car(Vehicle):
    def __init__(self, max_tires):
        super().__init__(max_tires)


class Truck(Vehicle):
    def __init__(self, max_tires):
        super().__init__(max_tires)


bike = Motorbike(2)
bike.add_tire()
bike.add_tire()
bike.drive()
bike.remove_tire()
bike.drive()

car = Car(4)
car.add_tire()
car.add_tire()
car.add_tire()
car.add_tire()
car.drive()

truck = Truck(6)
truck.add_tire()
truck.add_tire()
truck.add_tire()
truck.add_tire()
truck.add_tire()
truck.add_tire()
truck.drive()
