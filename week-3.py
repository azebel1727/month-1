class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return "Vehicle"
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        self.__num_doors = num_doors

    def describe(self):
        return "Car"

    def get_num_doors(self):
        return "number of doors on cars"
class Bike(Vehicle):
    def describe(self):
        return "Bike"
car = Car("Toyota", "Corolla", 4)
bike = Bike("Yamaha", "MT-15")


