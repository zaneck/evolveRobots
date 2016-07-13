# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot.
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ.lille1.fr
#############################################################################

class Canvas(object):
    def __init__(self, indi, x, y):
        self.indi = indi
        self.x = x
        self.y = y
        
    def toMatrice(self):
        res =[[0 for _ in range(self.y)] for _ in range(self.x)]

        for d in self.indi.draw:
            centX, centY, radius = d
            for i in range(centX - radius, centX + radius+1):
                for j in range(centY - radius, centY + radius+1):
                    if i >=0 and i< self.x and j >=0 and j< self.y:
                        res[i][j]=1
                    
        return res

    def getMaxXY(self):
        return (self.x,self.y)
