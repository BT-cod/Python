#import Section
import math

#SuperClass Section
class Shape:
    def calculate_area(self):
        pass

#SubClass Section
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

#Giving Inputs 
triangle = Triangle(3, 4)
circle = Circle(5)
rectangle = Rectangle(5, 4)

#Printing Output
print("Area of Circle:", circle.calculate_area(), "units")
print("Area of Rectangle:", rectangle.calculate_area(), "units")
print("Area of Triangle:", triangle.calculate_area(), "units")

