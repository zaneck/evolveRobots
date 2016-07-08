#############################################################################
#
# A fake fitness function to test the algorithm without actually running sofa. 
# 
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
import random

from fitness import Fitness
from indi import *

from config import Config

class FitnessFake(Fitness):
    def __init__(self, name, sofaScene="test1.pyscn", topologyMinFile="minTopoTest1", 
                x=10, y=10):
        Fitness.__init__(self)
        self.name=name
        
        self.x = x
        self.y = y

            
    def simulate(self, n):
        imgTest = n.toMatrice()
        cptVoxel = 0
        for i in range(self.x):
            for j in range(self.y):
                if imgTest[i][j] == 1:
                    cptVoxel += 1
                    
        return 1.0/cptVoxel
