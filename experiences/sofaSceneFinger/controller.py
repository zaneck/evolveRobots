import math

class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

        self.pos =[]
        #20 45 0 30 50 20
        #find the box
        self.tetras=node.getObject('tetras').position

        box = node.getObject('GOAL').pointsInROI 
        
        for i in range(len(self.tetras)):
            if self.tetras[i] in box:
                    self.pos.append(i)
            

    #print distance from init position
    def onEndAnimationStep(self,deltaTime):
        inputvalue = self.node.getObject('cable/aCable').findData('value')

        #condition contre deplacement
        if inputvalue.value[0][0] < 20:
            displacement = inputvalue.value[0][0] + 0.5
            inputvalue.value = str(displacement)

        
        tetras = self.node.getObject('tetras').position

        print("animation"),
        for i in self.pos:
            dist = math.sqrt( math.pow(tetras[i][0], 2) + math.pow(tetras[i][1] - 28.5, 2))
            print("{0},".format(dist)),
