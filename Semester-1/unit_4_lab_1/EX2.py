# A Class to Define Circles
# Dawson Gall

# Import
import math


# Class & Definition
class Circle:
    def __init__(self, radius):
        self.radius = int(radius)

    def circle_area(self):
        area = float(math.pi * (self.radius ** 2)).__round__(2)
        print(f'The area of a circle with {self.radius} will be {area}')

    def circle_perimeter(self):
        perimeter = float(2 * math.pi * self.radius).__round__(2)
        print(f'The perimeter of a circle with {self.radius} will be {perimeter}')


# Circle Info
circle_radius = 4
circle_info = Circle(circle_radius)
circle_info.circle_area()
circle_info.circle_perimeter()
