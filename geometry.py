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
                                
class Inverse(ShapeOperator):
        """ Returns the inverse of the children """
        def __init__(self, aShape):
                self.child = aShape
                
        def getValueAt(self, pos):
                res = self.child.getValueAt(pos)
                res[0] = -res[0]                
                return res

class Difference(ShapeOperator):
        """ Returns the difference between the first child minus the others shapes"""
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
        """Displace the object border of a given value."""
        def __init__(self, aChild, offset=0.1):
                self.child = aChild
                self.offset = offset
        
        def getValueAt(self, pos):
                res = self.child.getValueAt(pos)
                res[0] = res[0]-self.offset
                return res 

class Repeat(ShapeOperator):
        def __init__(self, child, c):
                self.child=child
                self.c=c
       
        def getValueAt(self, pos):
             if not isinstance(pos, Vec2):
                pos = Vec2(pos[0],pos[1])
             
             q = Vec2.mod(pos+0.5,self.c) - (self.c*0.5) 
             return self.child.getValueAt(q)  

class MicroStructure(ShapeOperator):
       """Implements a very simple substructuring operator to see if it works"""
       def __init__(self, child):
                self.child = child
                self.c = Vec2(0.1,0.1)
       
       def getValueAt(self, pos):
               if not isinstance(pos, Vec2):
                      pos = Vec2(pos[0],pos[1])
                      
               # Distance Field inside the circle 
               res = self.child.getValueAt(pos)
               if res[0] < 0:
                        s="s"
                        sp=0.1
                        dpos = Vec2.mod(pos, Vec2(sp, sp))
                        dpos = (pos-dpos)
                        dpos2 = dpos + Vec2(sp,sp)
                        dpos3 = dpos - Vec2(sp,sp)

                        #print("DPOS: "+str(pos.x)+" -> " +str(dpos.x) + ".." +str(dpos2.x))
                        if abs(dpos2.x-pos.x) < abs(dpos.x-pos.x):
                                dpos.x = dpos2.x           
                                s="r"
                                
                        if abs(dpos3.x-pos.x) < abs(dpos.x-pos.x):
                                dpos.x=dpos3.x        
                                s="l"
                        
                        if abs(dpos2.y-pos.y) < abs(dpos.y-pos.y):
                                dpos.y = dpos2.y           
                                s="r"
                                
                        if abs(dpos3.y-pos.y) < abs(dpos.y-pos.y):
                                dpos.y=dpos3.y        
                                s="l"
                                
                        r=sp/2.0
                        if r > abs(res[0]):
                                r=abs(res[0]) 
                        c=Circle(dpos.x,dpos.y, r*1) 
                        res2 = c.getValueAt(pos)
                        if -res2[0] < res[0]:
                                return [max(res[0],-res2[0]), pos, dpos, "i"]
                        return [max(res[0],-res2[0]), pos, dpos, "e"]
                                
               return [1.0, pos, Vec2(0,00), "s"]

               
               res[0]=res[0]
               s=0.1 #abs(res[0])/10.0
               q = Vec2.mod(pos+0.5,self.c) - (self.c*0.5)
               res2 = self.child.getValueAt(q.div(s))
               res2[0]=res2[0]*s
               return [min(res[0], res2[0]), pos, Vec2(0,0)]

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
                                
class Circle(Shape):
        def __init__(self, cx, cy, radius):
                self.center = Vec2(cx,cy)
                self.radius = radius
                        
        def getValueAt(self, pos):
                if not isinstance(pos, Vec2):
                        pos = Vec2(pos[0], pos[1])
                d=pos-self.center
                return [math.sqrt(d.x*d.x + d.y*d.y)-self.radius]

