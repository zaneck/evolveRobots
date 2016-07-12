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

class ShapeOperator(Shape):
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

class Union(ShapeOperator):
        """ Returns the unions of all the children shapes"""
        def __init__(self):
                self.children = []
        
        def __getitem__(self, idx):
                return self.children[idx]
        
        def __len__(self):
                return len(self.children)
        
        def remove(self, aShape):
                self.children.remove(aShape)
        
        def addShape(self, aShape):
                self.children.append(aShape)
                
        def getValueAt(self, pos):
                res=[1.0, 1]
                minv=float("inf")
                for f in self.children:
                        v = f.getValueAt(pos)
                        if(v[0]<minv):
                                minv = v[0]
                                res = v 
                return res

class Symmetry(ShapeOperator):
        def __init__(self, aChild, axis="x"):
                self.axis = axis
                self.child = aChild

        def setChild(self, aShape):
                self.child = aShape

        def getValueAt(self, pos):
                nx=pos[0]
                ny=pos[1]
                if self.axis == "x":
                        if pos[0] < 0:
                                nx = -pos[0] 
                else:
                        if pos[1] < 0:
                                ny = -pos[1] 
                return self.child.getValueAt((nx,ny))
                                
                                
class Circle(Shape):
        def __init__(self, cx, cy, radius):
                self.cx = cx 
                self.cy = cy
                self.radius = radius
                        
        def getValueAt(self, pos):
                dx=pos[0]-self.cx 
                dy=pos[1]-self.cy 
                return [math.sqrt(dx*dx + dy*dy)-self.radius]

