'''
LESSON 16 - POLYMORPHISM
manage diff classes at same time
'''

class Shape:
    def area(self):
        return 'Area not defined'

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Recatangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

circle = Circle(5)
rectangle = Recatangle(2,3)
shape = Shape() 
shapes = [circle, rectangle, shape]
for s in shapes:
    print(f'area: {s.area()}\n'
          f'Is a Shape: {isinstance(s, Shape)}\n'
          f'Is a circle: {isinstance(s, Circle)}\n'
          f'Is a Rectangle: {isinstance(s, Recatangle)}\n')      