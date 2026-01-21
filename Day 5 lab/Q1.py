class Vehicle:
    total_vehicles = 0

    def __init__(self, name):
        self.name = name
        Vehicle.total_vehicles += 1

class Bike(Vehicle):
    bike_count = 0

    def __init__(self, name):
        super().__init__(name)
        Bike.bike_count += 1

class Car(Vehicle):
    car_count = 0

    def __init__(self, name):
        super().__init__(name)
        Car.car_count += 1

class ElectricCar(Car):
    electric_car_count = 0

    def __init__(self, name):
        super().__init__(name)
        ElectricCar.electric_car_count += 1

b1 = Bike("Yamaha")
b2 = Bike("Royal Enfield")

c1 = Car("Honda City")
c2 = Car("Hyundai i20")

e1 = ElectricCar("Tesla Model 3")

print("Total Vehicles:", Vehicle.total_vehicles)
print("Total Bikes:", Bike.bike_count)
print("Total Cars:", Car.car_count)
print("Total Electric Cars:", ElectricCar.electric_car_count)
