import math

class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

        self.pos =[]
        #20 45 0 30 50 20
        #find the box
        self.tetras=node.getObject('tetras').position

        for i in range(len(self.tetras)):
            if self.tetras[i][0]>=20 and self.tetras[i][0]<=30 and  self.tetras[i][1]>=45 and self.tetras[i][1]<=50:
                    self.pos.append(i)
            

    #print distance from init position
    def onEndAnimationStep(self,deltaTime):
        tetras = self.node.getObject('tetras').position
        
        print("animation"),
        for i in self.pos:
            #issue with fall over the map
            #dist = math.sqrt(math.pow(self.tetras[i][0]-tetras[i][0],2) + math.pow(self.tetras[i][1]-tetras[i][1],2)) 
            #print("{0},".format(dist)),
            print("{0},".format(self.tetras[i][1] - tetras[i][1])),
