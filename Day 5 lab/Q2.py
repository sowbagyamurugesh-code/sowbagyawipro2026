# 1. Base class Calculator
class Calculator:
    def add(self, a, b):
        print("Calculator add:", a + b)

# 2. Derived class overriding add method
class AdvancedCalculator(Calculator):
    def add(self, a, b):
        print("AdvancedCalculator add (doubles first number):", (a*2) + b)

# 3. Operator overloading
class Number:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return Number(self.number + other.number)

    def __str__(self):
        return str(self.number)

# 4. Polymorphism
class Shape:
    def area(self):
        print("Generic shape")

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        print("Square area:", self.side * self.side)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        print("Circle area:", 3.14 * self.radius * self.radius)
# Method overriding
calc = Calculator()
calc.add(5, 3)

adv_calc = AdvancedCalculator()
adv_calc.add(5, 3)

# Operator overloading
num1 = Number(10)
num2 = Number(20)
num3 = num1 + num2
print("Operator overloading result:", num3)

# Polymorphism
shapes = [Square(4), Circle(3)]
for shape in shapes:
    shape.area()
