# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
from canvasBrutus import CanvasReflectionSymetryBrutus
import random

from config import Config

from imgTools import *

class IndiBrutus(object):
    idIndi = 0
    
    def __init__(self, x, y):        
        self.idIndi = IndiBrutus.idIndi
        IndiBrutus.idIndi +=1
        
        self.draw = "{0:b}".format(self.idIndi)
        self.lenDraw = 0
        
        self.fitness = 0

        self.canvas = CanvasReflectionSymetryBrutus(self, x, y)
        #self.canvas = Canvas(self,x,y)

    @property
    def myId(self):
        return self.idIndi

    def toMatrice(self):
        return self.canvas.toMatrice()

def printMatrix(m,w,h):
    print(m)
