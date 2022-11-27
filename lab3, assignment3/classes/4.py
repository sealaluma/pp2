import math 
class Point: 
    def __init__(self, x1, y1): 
        self.x = x1
        self.y = y1
     
    def show(self): 
        print(self.x, self.y) 
         
    def move(self, a, b): 
        self.x += a 
        self.y += b 
     
    def dist(self): 
        print(math.sqrt(self.x**2 + self.y**2))

pnt = Point(1, 1)
pnt.show()
pnt.move(3, 5)
pnt.show()
pnt.dist()