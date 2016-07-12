#############################################################################
#
# An expressive way to describe geometrical shapes using distance functions. 
# 
# Contributors:
#	- created by damien.marchal@univ-lille1.fr
#############################################################################
import math

class Shape(object):
        def getValueAt(self, pos):
                return [0.0]
                
class Rectangle(Shape):
        def __init__(self, cx, cy, halfwidth, halfheight):
                self.left = cx-halfwidth
                self.right = cx+halfwidth
                self.bottom = cy-halfheight
                self.top = cy+halfheight
                
        def getValueAt(self, pos):
                if pos[0] >= self.left and pos[0] <= self.right and pos[1] >= self.bottom and pos[1] <= self.top:
                        return [-1.0]
                return [1.0]         
                
class Circle(Shape):
        def __init__(self, cx, cy, radius):
                self.cx = cx 
                self.cy = cy
                self.radius = radius
                        
        def getValueAt(self, pos):
                dx=pos[0]-self.cx 
                dy=pos[1]-self.cy 
                return [math.sqrt(dx*dx + dy*dy)-self.radius]

