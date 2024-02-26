import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        return round(math.pi * self.radius ** 2, 2)

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height
        
    def getVolume(self):
        return round(self.getArea() * self.height, 2)

c = Circle(4)
print("Circle area is:", c.getArea())

cy = Cylinder(2, 5)
print("Cylinder volume is:", cy.getVolume())

'''
Execution results:
Circle area is: 50.27    
Cylinder volume is: 62.85
'''

print("end of program.")