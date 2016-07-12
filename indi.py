# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ.lille1.fr
#############################################################################
import math
from config import Config

from imgTools import *
from canvas import Canvas
import random

def circledistance(center, radius, pos):
        dx=pos[0]-center[0] 
        dy=pos[1]-center[1] 
        return math.sqrt(dx*dx + dy*dy)-radius


class Indi(object):
    idIndi = 0
    
    def __init__(self, width, height):
        #test params
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError

        if width > Config.indiSizeMax or height> Config.indiSizeMax:
            raise MemoryError
        
        self.idIndi = Indi.idIndi
        Indi.idIndi +=1
        
        self.width=width
        self.height=height

        self.draw = [] 
        self.lenDraw = 0
       
        self.fitness = 0

    def copy(self):
        res = Indi(self.width, self.height)
        for d in self.draw :
            res.draw.append(d)

        res.lenDraw = self.lenDraw
        return res
    
    def addSquare(self):
        centX = 0.2
        centY = 0.3
        radiusW = 0.2
        radiusH = 0.2
        
        self.draw.append((centX,centY,radiusW, radiusH))
        self.lenDraw += 1

    def addRandomSquare(self):
        centX = random.uniform(Config.centerMinValue, Config.centerMaxValue)
        centY = random.uniform(Config.centerMinValue, Config.centerMaxValue)
        halfW = random.uniform(0.1, Config.indiSquareMaxSize)
        halfH = random.uniform(0.1, Config.indiSquareMaxSize)
        
        self.draw.append((centX,centY,halfW,halfH))
        self.lenDraw += 1

    def removeRandomSquare(self):
        if self.lenDraw >=2:
            s = random.choice(self.draw)
            self.draw.remove(s)
            self.lenDraw -= 1
            return 1
        else:
            return 0
            
    def crossOver(self, i):
        res1 = Indi(self.width, self.height)
        res2 = Indi(self.width, self.height)
        
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

    def getValueAt(self, pos):
        """ Returns a list of float value between  indicating the data content """
        res=[]
        for f in self.draw:
                if pos[0] >= f[0]-f[2] and pos[0] <= f[0]+f[2] and pos[1] >= f[1]-f[3] and pos[1] <= f[1]+f[3]:
                        return [-1.0]
        return [1.0]         
        #return [circledistance((0,0), 0.4, pos)]

    @property
    def myId(self):
        return self.idIndi

