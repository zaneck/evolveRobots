class controller(Sofa.PythonScriptController):
    def initGraph(self, node):
        self.node = node

    def onEndAnimationStep(self,deltaTime):
        node = self.node.getChild('subTopo').findData('test')
        print(node)

