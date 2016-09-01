import math

class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

        self.pos =[]
        #20 45 0 30 50 20
        #find the box
        self.tetras=node.getObject('tetras').position

        box = node.getObject('ROIForce').pointsInROI 
        
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