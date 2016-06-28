class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

        self.pos =[]
        #20 45 0 30 50 10
        #find the box
        self.tetras=node.getObject('tetras').position

        for i in range(len(self.tetras)):
            if self.tetras[i][0]>=20 and self.tetras[i][0]<=30 and  self.tetras[i][1]>=45 and self.tetras[i][1]<=50:
                    self.pos.append(i)
            

    #print distance from init position
    def onEndAnimationStep(self,deltaTime):
        tetras = self.node.getObject('tetras').position
        
        print("animation")
        for i in self.pos:
            print(self.tetras[i][1] - tetras[i][1])
