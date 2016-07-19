import math

class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node
        self.leftBox = []
        self.rightBox = []

        #get all tetras
        tetras = node.getObject('tetras').position
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

        rightCentroidX = 0
        rightCentroidY = 0
        for a in self.rightBox:
            rightCentroidX += tetras[a][0]
            rightCentroidY += tetras[a][1]            
            
        print("animation"),
        # for i in self.pos:
        print("{0},".format(1-math.sqrt(math.pow(rightCentroidX - leftCentroidX,2) + math.pow(rightCentroidY - leftCentroidY,2)))),
