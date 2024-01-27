from abc import ABC, abstractmethod

# Calculator Interfaces
class Adder(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

class Subtractor(ABC):
    @abstractmethod
    def subtract(self, a, b):
        pass

class Multiplier(ABC):
    @abstractmethod
    def multiply(self, a, b):
        pass

class Divider(ABC):
    @abstractmethod
    def divide(self, a, b):
        pass

# Calculator Implementation with Strategies
class Calculator:
    def __init__(self, adder, subtractor, multiplier, divider):
        self.adder = adder
        self.subtractor = subtractor
        self.multiplier = multiplier
        self.divider = divider

    def perform_operations(self, a, b):
        print(f"Addition: {self.adder.add(a, b)}")
        print(f"Subtraction: {self.subtractor.subtract(a, b)}")
        print(f"Multiplication: {self.multiplier.multiply(a, b)}")
        print(f"Division: {self.divider.divide(a, b)}")

# Simple Implementation Strategies
class SimpleAdder(Adder):
    def add(self, a, b):
        return a + b

class SimpleSubtractor(Subtractor):
    def subtract(self, a, b):
        return a - b

class SimpleMultiplier(Multiplier):
    def multiply(self, a, b):
        return a * b

class SimpleDivider(Divider):
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# Using Calculator with Simple Implementation Strategies
simple_calculator = Calculator(SimpleAdder(), SimpleSubtractor(), SimpleMultiplier(), SimpleDivider())
simple_calculator.perform_operations(10, 5)
