''' 
Fill in the Line class methods to accept coordinates as a pair of tuples 
and return the slope and distance of the line.

class Line:
    
    def __init__(self,coor1,coor2):
        pass
    
    def distance(self):
        pass
    
    def slope(self):
        pass

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()

Out[3]:
9.433981132056603


li.slope()

Out[4]:
1.6

'''
import math

# Create a new class. Class names will alsways start with Capital letter and use Camel casing
# __init__ method is a constructor to set the object (instance) variables
# self represent the current object (instance)
class Line:

	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)

	def slope(self):
		return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])

# Inputs
coordinate1 = (3,2)		
coordinate2 = (8,10)

# instantiate an object of type Line and pass the inputs
# Here the __init__ method will be called and these inputs will be set for this instance line1
line1 = Line(coordinate1, coordinate2)

# Call the functions inside the class using the instance
# and they will have access to the variables set dueing object instantiation
print(f'distance -> {line1.distance()}')
print(f'distance -> {line1.slope()}')

