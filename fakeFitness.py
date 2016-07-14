# coding: utf8 
#############################################################################
# A fake fitness function to test the algorithm without actually running sofa. 
# 
# Contributors:
#	- created by damien.marchal@univ-lille1.fr
#############################################################################
import random

from canvas import Canvas, printMatrix 
from fitness import Fitness
from indi import *

from config import Config

def binarybin(values):
        """This binning function is using the first value at [0]. If < 0 it return 1.0 (there is matter at
           this location. Otherwise it return 0 (no matter)"""
        if values[0] < 0:
                return 1.0
        return 0.0

class FitnessFake(Fitness):
    def __init__(self, name, theCanvas):
        Fitness.__init__(self)
        self.name=name
        self.canvas = theCanvas
        self.width = self.canvas.res[0]
        self.height = self.canvas.res[1]

    def toMatrice(self, candidate):
        return self.canvas.toMatrice(candidate, binarybin)
            
    def simulate(self, candidate):
        imgTest = self.toMatrice(candidate)
        print("")
        printMatrix(imgTest)
        cptVoxel = 0
        for i in range(self.width):
            for j in range(self.height):
                if imgTest[i][j] == 1:
                    cptVoxel += 1
                    
        return 1.0/(cptVoxel+1)
