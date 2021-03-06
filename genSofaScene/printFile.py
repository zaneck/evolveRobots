#!/usr/bin/python3 -O
########################################################################################################
#
# This file is part of evolveRobot.
#
# Contributors:
#	- created by Valentin Owczarek
########################################################################################################

import sys
sys.path.insert(0,"..")
from geometry import *
from canvas import Canvas


from sofaObject import *
from sofaObjectUsable import *

class printFileSimulation(object):

    def __init__(self, bag, wdPath):
        self.bag =  bag
        self.wdPath = wdPath
        
    def printFile(self):
        pass


class printPyscnFile(printFileSimulation):
    def printFile(self):
        f = open(self.wdPath + "/simulation.pyscn", "w")

        head = Head({})
        f.write(head.__str__())
        
        alpha = self.bag.getDataSofa("Canvas")[0]
        f.write(alpha.__str__())

        fem = FEM({})
        f.write(fem.__str__())

        #user Object
        bagKey = self.bag.getKeysSofa()

        for k in bagKey:
            if k != "Canvas":
                for alpha in self.bag.getDataSofa(k):
                    f.write(alpha.__str__())
        
        #end user Object

        tail = Tail({})
        f.write(tail.__str__())
        f.close()

class printMintopoFile(printFileSimulation):
    def binarybin(values):
        """This binning function is using the first value at [0]. If < 0 it return 1.0 (there is matter at
        this location. Otherwise it return 0 (no matter)"""
        if values[0] < 0:
                return 1
        return 0
        
    def printFile(self):
        #load shape into a canvas
        canvasData = self.bag.getDataSofa("Canvas")[0]
        #set dim and res vars
        dim = (1.0, 1.0)
        res = (canvasData.divX, canvasData.divY)

        theCanvas = Canvas(dim, res)

        union = Union()
        #user Object
        bagKey = self.bag.getKeysSofa()

        for k in bagKey:
            if k != "Canvas":
                for alpha in self.bag.getDataSofa(k):
                    theShape = alpha.minTopoAdd()
                    if theShape != None:
                        union.addShape(theShape)
        
        #write the canvas
        f = open(self.wdPath + "/minTopo.py", "w")
        f.write("topology = [\n")

        imgTest = theCanvas.toMatrice(union, printMintopoFile.binarybin)
        
        for j in range(res[1]):
            f.write("[")
            f.write("{0}".format(imgTest[0][j]))
            for i in range(1, res[0]):
                f.write(",{0}".format(imgTest[i][j]))
            if j == res[1]-1:
                f.write("]\n")
            else:                              
                f.write("],\n")

        f.write("]")
        f.close()
