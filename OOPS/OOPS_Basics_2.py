'''
Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass

# EXAMPLE OUTPUT
c = Cylinder(2,3)

c.volume()

Out[7]:
56.52

c.surface_area()

Out[8]:
94.2

'''
import math

class Cylinder:
    def __init__(self, height = 1, radius = 1):
        self.height = height
        self.radius = radius
    
    def volume(self):
        return math.pi * (self.radius ** 2) * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.height + self.radius)

c1 = Cylinder(2,3)

print(f'Volume of the cylinder -> {c1.volume()}')

print(f'Surface Area of the cylinder -> {c1.surface_area()}')
