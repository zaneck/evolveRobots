from subprocess import Popen, PIPE

from fitness import Fitness
from indi import *

class FitnessSofa(Fitness):
    def __init__(self, name, sofaScene="test1.pyscn", topologyMinFile="minTopoTest1", x=10, y=10):
        Fitness.__init__(self)
        self.name=name
        
        self.x = x
        self.y = y

        self.sofaScene = sofaScene

        exec("import {0}".format(topologyMinFile)) 
        self.topologyMin = sys.modules[topologyMinFile].topology
        
    def simulate(self, n):
        imgTest = n.toMatrice()

        for i in range(self.x):
            for j in range(self.y):
                if self.topologyMin[i][j] == 1:
                    imgTest[i][j] = 1
        
        #write the topo
        topo = open("topo.py","w")

        topo.write("topology = [")

        for i in range(self.x):
            if i != self.x - 1:
                topo.write("{0},".format(imgTest[i]))
            else:
                topo.write("{0}".format(imgTest[i]))
                
        topo.write("]")

        topo.close()
        
        #Popen
        a = Popen(["runSofa", "-g", "batch", "-n", "50", "test1.pyscn"], stdout=PIPE)
        a.wait()
        
        #Parse
        print(a.stdout)
        
        #return
                    
        return 1#cptOk
