import math


class Dimension:
    def area(self):
        print('Shape is undefined')


class Triangle(Dimension):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2


class Circle(Dimension):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Dimension):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


triangle = Triangle(10, 5)
circle = Circle(7)
rectangle = Rectangle(8, 6)

print("Triangle Area:", triangle.area())
print("Circle Area:", circle.area())
print("Rectangle Area:", rectangle.area())