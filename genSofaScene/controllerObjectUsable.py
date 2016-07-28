# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#
#############################################################################

from controllerObject import ControllerObject
from sofaObject import BoxROI

class DistanceFromOrigin(ControllerObject):
    unique = False
    def __init__(self, context):
        self.key = "DistanceFromOrigin"
        self.haveBoxROI = True
        self.boxOne = BoxROI(context["box"])
        self.distanceName = context["distanceName"]
        
    def initObject(self):
        """
        return the init object part for the initGraph fun
        """

        return ""

    def inLoopComputation(self):
        """
        return what it need to be compute during the simulation loop.
        Instruction for the onEndAnimationStep function
        """

        return ""
        
    def getBoxROI(self):
        return [self.box]

class DistanceBetweenTwoBox(ControllerObject):
    unique = False
    def __init__(self, context):
        self.key = "DistanceBetweenTwoBox"
        self.haveBoxROI = True
        
        self.boxOne = BoxROI(context["boxOne"])
        self.boxTwo = BoxROI(context["boxTwo"])
        self.distanceName = context["distanceName"]
        
    def initObject(self):
        return """
        self.leftBox = []
        self.rightBox = []

        leftBox = node.getObject('ROI{0}').pointsInROI
        rightBox = node.getObject('ROI{1}').pointsInROI

        for i in range(len(tetras)):
            if tetras[i] in leftBox:
                self.leftBox.append(i)
                
            if tetras[i] in rightBox:
                self.rightBox.append(i)
""".format(self.boxOne.idBox, self.boxTwo.idBox)
    
    def inLoopComputation(self):
        return """        leftCentroidX = 0
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


        {0} = math.sqrt(math.pow(rightCentroidX - leftCentroidX, 2) + math.pow(rightCentroidY - leftCentroidY, 2))
""".format(self.distanceName)

    def getBoxROI(self):
        return [self.boxOne, self.boxTwo]
    
class SimpleResult(ControllerObject):
    def __init__(self, context):
        self.key = "SimpleResult"
        self.haveBoxROI = False
        self.distanceName = context["distanceName"]
        
    def initObject(self):
        return ""

    def inLoopComputation(self):
        return "        res = {0}".format(self.distanceName)
