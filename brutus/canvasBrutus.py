# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot.
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################

import sys
sys.path.insert(0,"..")
from canvas import Canvas

import math

class CanvasReflectionSymetryBrutus(Canvas):
    def __init__(self, indi, x, y):
        Canvas.__init__(self, indi, x, y)

        self.xMin = int(self.x / 2) 
        self.yMin = int(self.y / 2)
        

    def toMatrice(self):
        res =[[0 for _ in range(self.y)] for _ in range(self.x)]

        cpt = 0
        for i in range(len(self.indi.draw)-1, -1, -1):
            if self.indi.draw[i] == '1':
                res[math.floor(cpt/self.x)][cpt % self.y] = 1
                res[self.x - math.floor(cpt/self.x)-1][cpt % self.y] = 1
            cpt += 1

        return res

    def getMaxXY(self):
        return (self.xMin, self.yMin)
