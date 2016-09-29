import math
from math import fmod        

class Vec2(object):
        def __init__(self,x=0.0,y=0.0):
                self.x = x
                self.y = y
        
        def __sub__(a, b):
                if isinstance(b, (float,int)):
                        return Vec2(a.x-b, a.y-b)

                v=Vec2()
                v.x = a.x-b.x
                v.y = a.y-b.y
                return v
                
        def __add__(a, b):
                if isinstance(b, (float,int)):
                        return Vec2(a.x+b, a.y+b)
                v=Vec2()
                v.x = a.x+b.x
                v.y = a.y+b.y
                return v

        def __mul__(a,aScalar):
                v = Vec2()
                v.x = a.x * aScalar                
                v.y = a.y * aScalar                
                return v
        
        def div(a,aScalar):
                v = Vec2()
                v.x = a.x / aScalar                
                v.y = a.y / aScalar                
                return v

        @staticmethod
        def mod(a,b):
                return Vec2(fmod(a.x, b.x), fmod(a.y, b.y))

        @staticmethod
        def min(a, b):
                v=Vec2(min(a.x, b.x, min(a.y,b.y)))
                return v 
                
        @staticmethod        
        def max(a, b):
                v=Vec2(max(a.x, b.x, max(a.y,b.y)))
                return v 

        @staticmethod                
        def length(a):
                return math.sqrt(a.x*a.x + a.y*a.y)        
        
        def abs(self):
                v=Vec2(abs(self.x), abs(self.y))
                return v
