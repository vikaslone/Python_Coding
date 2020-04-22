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

class Line:

	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)

	def slope(self):
		return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])

coordinate1 = (3,2)		
coordinate2 = (8,10)

# instantiate an object of type Line
line1 = Line(coordinate1, coordinate2)

print(f'distance -> {line1.distance()}')
print(f'distance -> {line1.slope()}')

