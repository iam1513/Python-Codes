import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

def calculate_area(shape_instance):
    return shape_instance.area()

circle = Circle(radius=5)
square = Square(side_length=4)

print("Circle area:", calculate_area(circle))
print("Square area:", calculate_area(square))
