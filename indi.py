from config import Config

from imgTools import *
from canvas import CanvasReflectionSymetry
import random


class Indi(object):
    idIndi = 0
    
    def __init__(self, x, y):
        #test params
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError

        if x > Config.indiSizeMax or y > Config.indiSizeMax:
            raise MemoryError
        
        self.idIndi = Indi.idIndi
        Indi.idIndi +=1
        
        self.x =x
        self.y =y

        self.draw = [] #(centX, centY, radius)
        self.lenDraw = 0
        
        self.fitness = 0

        self.canvas = CanvasReflectionSymetry(self, x, y)

    def copy(self):
        res = Indi(self.x, self.y)

        for d in self.draw :
            res.draw.append(d)

        res.lenDraw = self.lenDraw
        
        return res
            
    def addRandomSquare(self):
        x, y = self.canvas.getMaxXY()
        centX = random.randint(0,self.x-1)
        centY = random.randint(0,self.y-1)
        radius = random.randint(0, Config.indiSquareMaxSize)
        
        self.draw.append((centX,centY,radius))
        self.lenDraw +=1

    def removeRandomSquare(self):
        if self.lenDraw >=2:
            s = random.choice(self.draw)
            self.draw.remove(s)
            self.lenDraw -= 1
            return 1
        else:
            return 0
            
            
    def crossOver(self, i):
        res1 = Indi(self.x, self.y)
        res2 = Indi(self.x, self.y)
        
        borneMax = min(self.lenDraw, i.lenDraw)
        borne = random.randint(0,borneMax)

        for s in range(0,borneMax):
            res1.draw.append(self.draw[s])
            res2.draw.append(i.draw[s])
            res1.lenDraw +=1
            res2.lenDraw +=1
            
        for s in range(borneMax, self.lenDraw):
            res2.draw.append(self.draw[s])
            res2.lenDraw +=1
            
        for s in range(borneMax, i.lenDraw):
            res1.draw.append(i.draw[s])
            res1.lenDraw +=1
            
        return (res1,res2)

    def toMatrice(self):
        return self.canvas.toMatrice()


def printMatrix(m, x, y):
    for i in range(x):
        print("{0},".format(m[i]))
