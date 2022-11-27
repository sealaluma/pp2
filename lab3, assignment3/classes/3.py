class Shape():
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, w):
        Shape.__init__(self)
        self.length = lenght
        self.width  = width

    def area(self):
        return self.length * self.width

l = int(input())
w = int(input())
rectangle = Rectangle(l, w)
print(rectangle.area())