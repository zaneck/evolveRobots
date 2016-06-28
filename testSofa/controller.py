class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

        self.pos =[]
        #20 45 0 30 50 10
        #find the box
        n=node.getObject('tetras').position
        for i in range(len(n)):
            if n[i][0]>20 and n[i][0]<45 and n[i][1]>30 and n[i][1]<50:
                    self.pos.append(i)
            

    def onEndAnimationStep(self,deltaTime):
        tetras = self.node.getObject('tetras').position
        
        print("animation")
        for i in self.pos:
            print(tetras[i])
