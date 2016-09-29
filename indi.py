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

from geometry import * 
from imgTools import *
import random

class Indi(object):
    idIndi = 0
    
    def __init__(self, withSymmetry=True):       
        self.idIndi = Indi.idIndi
        Indi.idIndi +=1
        
        #self.width=width
        #self.height=height

        self.draw = [] 
        self.lenDraw = 0
       
        self.fitness = 0
        
        self.rootunion = Union()
        self.symmetry = self.rootunion 
        if withSymmetry:
                self.symmetry = Symmetry(self.rootunion, axis="x")

    def copy(self):
        res = Indi()
        for s in self.rootunion.children :
            res.rootunion.addShape(s)
        return res
    
    def addShape(self, shape):
        """Add a new shape into the candidate primitive list
           Example:
                ind = Indi()
                ind.addShape(Rectangle(1,1,4,2))
        """
        self.rootunion.addShape(shape)
                
    def addRandomShape(self):
        # todo(dmarchal): use a configuration paramter to specify the percentage of 
        # square/circle to generate. 
        if random.random() < 0.5:
                self.addRandomSquare()
        else:
                self.addRandomCircle()    
    
    def addRandomCircle(self):
        centX = random.uniform(Config.centerMinValue, Config.centerMaxValue)
        centY = random.uniform(Config.centerMinValue, Config.centerMaxValue)
        w = random.uniform(Config.indiSquareMinSize, Config.indiSquareMaxSize)
        self.addShape(Circle(centX, centY, w))   
        
    def addRandomSquare(self):
        centX = random.uniform(Config.centerMinValue, Config.centerMaxValue)
        centY = random.uniform(Config.centerMinValue, Config.centerMaxValue)
        halfW = random.uniform(Config.indiSquareMinSize, Config.indiSquareMaxSize)
        halfH = random.uniform(Config.indiSquareMinSize, Config.indiSquareMaxSize)
        self.addShape(Rectangle(centX,centY,halfW,halfH))

        
    def removeShapeAtRandom(self):
        if len(self.rootunion) >=2:
            s = random.choice(self.rootunion.children)
            self.rootunion.remove(s)
            return 1
        else:
            return 0

    # #find the first splitable square, remove from the list
    # #and add 4 new square at the end of the drawing list
    # def splitSquare(self):
    #     cpt=0

    #     while cpt < len(self.draw) and self.draw[cpt][2] < 1 :
    #         cpt += 1

    #     if cpt == len(self.draw):
    #         return 0

    #     s = self.draw[cpt]
    #     self.draw.remove(s)

    #     rad = math.ceil(s[2] / 2)
        
    #     self.draw.append((s[0] - rad, s[1] - rad, rad))
    #     self.draw.append((s[0] - rad, s[1] + rad, rad))
    #     self.draw.append((s[0] + rad, s[1] - rad, rad))
    #     self.draw.append((s[0] + rad, s[1] + rad, rad))

    #     return 1
        
    def crossOver(self, i):
        res1 = Indi()
        res2 = Indi()
        
        borneMax = min(len(self.rootunion), len(i.rootunion))
        borne = random.randint(0,borneMax)

        for s in range(0,borneMax):
            res1.addShape( self.rootunion[s] )
            res2.addShape( i.rootunion[s] )
            
        for s in range(borneMax, len(self.rootunion)):
            res2.addShape( self.rootunion[s] )
            
        for s in range(borneMax, len(i.rootunion)):
            res1.addShape(i.rootunion[s])
            
        return (res1,res2)

    def getValueAt(self, pos):
        """ Returns a list of float value indicating the data content 
            first value is the distance to the border of the object
            second value is the primitive that emit this distance
        """
        return self.symmetry.getValueAt(pos)

    @property
    def myId(self):
        return self.idIndi

