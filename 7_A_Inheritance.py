#By using the concept of inheritance write a python program to find the area of triangle, circle and rectangle.

#Import section
import math
#SuperClass Sections
class Shape:
    def calculate_area(self):
        pass
#Subclass Sections
class Traingle(Shape):
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
triangle = Traingle(3, 4)
circle = Circle(5)
rectangle = Rectangle(5, 4)
#Printing Output
print("Area of Triangle is", triangle.calculate_area(), "units")
print("Area of Circle is", circle.calculate_area(), "units")
print("Area of Rectangle is", rectangle.calculate_area(), "units")

# ------------------------------------------------------------------------Manual Program--------------------------------------------------------------------------
# import math

# class Shape:
#  def __init__(self):
#         self.area = 0
#         self.name = ""

#  def showArea(self):
#         print("The area of the", self.name, "is", self.area, "units")

# class Circle(Shape):
#  def __init__(self,radius):
#         self.area = 0
#         self.name = "Circle"
#         self.radius = radius

#  def calcArea(self):
#         self.area = math.pi * self.radius * self.radius

# class Rectangle(Shape):
#  def __init__(self,length,breadth):
#         self.area = 0
#         self.name = "Rectangle"
#         self.length = length
#         self.breadth = breadth

#  def calcArea(self):
#         self.area = self.length * self.breadth
# class Triangle(Shape):
#  def __init__(self,base,height):
#         self.area = 0
#         self.name = "Triangle"
#         self.base = base
#         self.height = height

#  def calcArea(self):
#         self.area = self.base * self.height / 2


# c1 = Circle(5)
# c1.calcArea()
# c1.showArea()
# r1 = Rectangle(5, 4)
# r1.calcArea()
# r1.showArea()
# t1 = Triangle(3, 4)
# t1.calcArea()
# t1.showArea()