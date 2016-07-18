#############################################################################
#
# An expressive way to describe geometrical shapes using distance functions. 
# 
# Contributors:
#	- created by damien.marchal@univ-lille1.fr
#############################################################################
import math
from linalg import Vec2

class Shape(object):
        """Base class for implicit shape description based on distance field. 
        An implicit shape description consist in a field covering the R2 or R3
        domain. The field can be queried using the method getValueAt(pos).
        The object interior is then defined for each 'pos' that match a given
        criteria as in:
                if getValue(pos) < 0.0:
                        print("Inside")
                else:
                        print("Outside"
        """
        def getValueAt(self, pos):
                """returns an array of values. The amount of values depends on 
                   the amount of informations that needs to be encoded into 
                   the field. 
                   eg:
                        [0] = float value encoding the signed distance to the border
                        [1] = an index telling the primitive (cube, circle) that generated the distance
                        [2] = a set of r,g,b values or colors or material stifness or young modulus. 
                        [3] = any other value that need to be transported in the field        
                """
                return [0.0]

class ShapeOperator(Shape):
        def getValueAt(self, pos):
                return [0.0]
                
class Rectangle(Shape):
        """A rectangular shape defined by it center cx,cy 
           and its halfwidth/halfheight. 
           Example:
                r=Rectangle(1,1,2,3) 
                defines a rectangle centerd at (1,1) with a 
                width of length 4 and a height of length of length 6
           """
        def __init__(self, cx, cy, halfwidth, halfheight):
                self.left = cx-halfwidth
                self.right = cx+halfwidth
                self.bottom = cy-halfheight
                self.top = cy+halfheight
                self.center = Vec2(cx-halfwidth, cy-halfheight)
                self.dim = Vec2(halfwidth, halfheight)
                
        def getValueAt(self, pos):
                if not isinstance(pos, Vec2):
                        pos = Vec2(pos[0],pos[1])
                pos = pos - self.center 
                # Centered distance field         
                d = pos.abs() - self.dim;
                return [min(max(d.x,d.y),0.0) + Vec2.length(Vec2.max(d,Vec2())) ]
                
class Inverse(ShapeOperator):
        """ Returns the inverse of the children """
        def __init__(self, aShape):
                self.child = aShape
                
        def getValueAt(self, pos):
                res = self.child.getValueAt(pos)
                res[0] = -res[0]                
                return res

class Difference(ShapeOperator):
        """ Returns the difference of the first child minus the others shapes"""
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
                assert(len(self.children)>0)
                res=[1.0, 1]
                
                # Left part
                ares=(self.children[0].getValueAt(pos))
                amax=ares[0]
                 
                # Union of the shape that will be subtracted
                minv=float("inf")
                for f in self.children[1:]:
                        v = f.getValueAt(pos)
                        if(v[0]<minv):
                                minv = v[0]
                                res = v 
                
                if amax > -(minv):
                        return ares
                return res

                
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
        """Generate a symetric shape along the specified axis located at origin. """
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

class Offset(ShapeOperator):
        def __init__(self, aChild, offset=0.1):
                self.child = aChild
                self.offset = offset
        
        def getValueAt(self, pos):
                res = self.child.getValueAt(pos)
                res[0] = res[0]-self.offset
                return res 
                                
                                
class Circle(Shape):
        def __init__(self, cx, cy, radius):
                self.cx = cx 
                self.cy = cy
                self.radius = radius
                        
        def getValueAt(self, pos):
                dx=pos[0]-self.cx 
                dy=pos[1]-self.cy 
                return [math.sqrt(dx*dx + dy*dy)-self.radius]

