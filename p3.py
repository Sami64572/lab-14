from abc import ABC, abstractmethod

# Vehicle Interface
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def move(self):
        pass

# Concrete Classes implementing Vehicle Interface
class Car(Vehicle):
    def start(self):
        print("Car starting...")

    def stop(self):
        print("Car stopping...")

    def move(self):
        print("Car moving...")

class Bike(Vehicle):
    def start(self):
        print("Bike starting...")

    def stop(self):
        print("Bike stopping...")

    def move(self):
        print("Bike moving...")

class Plane(Vehicle):
    def start(self):
        print("Plane starting...")

    def stop(self):
        print("Plane stopping...")

    def move(self):
        print("Plane moving...")

# Using the Vehicle Interface and Concrete Classes
car = Car()
bike = Bike()
plane = Plane()

car.start()
car.move()
car.stop()

bike.start()
bike.move()
bike.stop()

plane.start()
plane.move()
plane.stop()
