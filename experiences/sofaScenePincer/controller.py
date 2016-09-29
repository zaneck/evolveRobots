import math
import topo
from tools import *

class controller(Sofa.PythonScriptController):
    def bwdInitGraph(self, node):
        x , y , z = 21, 21, 2
        grid = node.getObject('grid')
        hexa = grid.findData('hexahedra').value
        position = grid.findData('position').value
        
        ##########################################
        # Contact                                #
        ##########################################
        maskLeft = halfPart(topo.topology, x-1, y-1, "L")
        leftHexa = selectHexa(hexa, maskLeft)
        
        reduceLeftPosition, reduceLeftHexa = reducePositionOverHexa(position, leftHexa)
        
        leftContact = node.createChild('contact')        
        leftContact.createObject('Mesh', position=reduceLeftPosition, hexahedra=reduceLeftHexa)
        leftContact.createObject('MechanicalObject')
        leftContact.createObject('TTriangleModel', group="3", selfCollision="1")
        leftContact.createObject('TLineModel', group="3", selfCollision="1")
        leftContact.createObject('TPointModel', group="3", selfCollision="1")
        leftContact.createObject('BarycentricMapping')

        maskRight = halfPart(topo.topology, x-1, y-1, "R")
        rightHexa = selectHexa(hexa, maskRight)
        
        reduceRightPosition, reduceRightHexa = reducePositionOverHexa(position, rightHexa)
        
        rightContact = node.createChild('contact')        
        rightContact.createObject('Mesh', position=reduceRightPosition, hexahedra=reduceRightHexa)
        rightContact.createObject('MechanicalObject')
        rightContact.createObject('TTriangleModel', group="4", selfCollision="1")
        rightContact.createObject('TLineModel', group="4", selfCollision="1")
        rightContact.createObject('TPointModel', group="4", selfCollision="1")
        rightContact.createObject('BarycentricMapping')

        # mask = halfPart(topo.topology, x-1, y-1, "ALL")
        # allHexa = selectHexa(hexa, mask)
        # reducePosition, reduceHexa = reducePositionOverHexa(position, allHexa)

        # contact = node.createChild('contact')        
        # contact.createObject('Mesh', position=reducePosition, hexahedra=reduceHexa)
        # contact.createObject('MechanicalObject')
        # contact.createObject('TTriangleModel', group="4", selfCollision="1")
        # contact.createObject('TLineModel', group="4", selfCollision="1")
        # contact.createObject('TPointModel', group="4", selfCollision="1")
        # contact.createObject('BarycentricMapping')

        
    def initGraph(self, node):
        self.node = node
        #get all tetras
        tetras = node.getObject('tetras').position


        self.leftBox = []
        self.rightBox = []
        #and 2 boxes to watch

        leftBox = node.getObject('LEFTBOX').pointsInROI
        rightBox = node.getObject('RIGHTBOX').pointsInROI

        #get indices of the 2 boxs tetras
        for i in range(len(tetras)):
            if tetras[i] in leftBox:
                self.leftBox.append(i)
                
            if tetras[i] in rightBox:
                self.rightBox.append(i)
        
    #print distance from init position
    def onEndAnimationStep(self,deltaTime):
        tetras = self.node.getObject('tetras').position

        #get centroid of 2 box

        leftCentroidX = 0
        leftCentroidY = 0
        for a in self.leftBox:
            leftCentroidX += tetras[a][0]
            leftCentroidY += tetras[a][1]

        leftCentroidX /= len(self.leftBox)
        leftCentroidY /= len(self.leftBox)

        rightCentroidX = 0
        rightCentroidY = 0
        for a in self.rightBox:
            rightCentroidX += tetras[a][0]
            rightCentroidY += tetras[a][1]            

        
        rightCentroidX /= len(self.rightBox)
        rightCentroidY /= len(self.rightBox)


        res = math.sqrt(math.pow(rightCentroidX - leftCentroidX, 2) + math.pow(rightCentroidY - leftCentroidY, 2))
        
        print("animation"),
        # for i in self.pos:
        print("{0},".format(res)),
