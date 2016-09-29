import math

class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

        self.pos =[]
        #20 45 0 30 50 20
        #find the box
        self.tetras=node.getObject('tetras').position

        box = node.getObject('FORCE1').pointsInROI 
        box2 = node.getObject('FORCE2').pointsInROI 
        box3 = node.getObject('FORCE3').pointsInROI 
        
        for i in range(len(self.tetras)):
            if self.tetras[i] in box or self.tetras[i] in box2 or self.tetras[i] in box3:
                    self.pos.append(i)
            

    #print distance from init position
    def onEndAnimationStep(self,deltaTime):
        tetras = self.node.getObject('tetras').position
        
        print("animation"),
        for i in self.pos:
            print("{0},".format(self.tetras[i][1] - tetras[i][1])),
