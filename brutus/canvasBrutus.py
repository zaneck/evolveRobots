# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot.
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
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
        for a in self.indi.draw:
            if a == '1':
                res[math.floor(cpt/self.xMin)][cpt % self.yMin] = 1
                res[math.floor(cpt/self.xMin)][self.y - (cpt % self.yMin) - 1] = 1
            cpt += 1

                # for d in self.indi.draw:
                #     centX, centY, radius = d
                #     for i in range(centX - radius, centX + radius+1):
                #         for j in range(centY - radius, centY + radius+1):
                #             if i >=0 and i< self.x and j >=0 and j< self.y:
                #                 res[i][j]=1

                #     for i in range((self.x-centX) - radius, (self.x-centX) + radius+1):
                #         for j in range(centY - radius, centY + radius+1):
                #             if i >=0 and i< self.x and j >=0 and j< self.y:
                #                 res[i][j]=1

        return res

    def getMaxXY(self):
        return (self.xMin, self.yMin)
