class Vehicle:
    def create(self):
        pass

class Car(Vehicle):
    def create(self):
        return "Car created."

class Bike(Vehicle):
    def create(self):
        return "Bike created."

class VehicleFactory:
    def get_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "bike":
            return Bike()

# Usage
factory = VehicleFactory()
vehicle = factory.get_vehicle("car")
print(vehicle.create())
