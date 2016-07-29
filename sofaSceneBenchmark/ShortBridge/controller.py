import math

class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

        self.pos =[]
        #20 45 0 30 50 20
        #find the box
        self.tetras=node.getObject('tetras').position

        box0 = node.getObject('ROIForce0').pointsInROI
        box1 = node.getObject('ROIForce1').pointsInROI
        box2 = node.getObject('ROIForce2').pointsInROI
        box3 = node.getObject('ROIForce3').pointsInROI 

        boxes = [box0, box1, box2, box3]

        for box in boxes:
            for i in range(len(self.tetras)):
                if self.tetras[i] in box:
                    self.pos.append(i)
            

    #print distance from init position
    def onEndAnimationStep(self,deltaTime):
        tetras = self.node.getObject('tetras').position
        
        print("animation"),
        for i in self.pos:
            res = math.sqrt(math.pow(self.tetras[i][1] - tetras[i][1],2) + math.pow(self.tetras[i][0] - tetras[i][0],2))
            print("{0},".format(res)),
