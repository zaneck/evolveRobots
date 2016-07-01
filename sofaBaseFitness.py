import numpy as np
from subprocess import Popen, PIPE, call

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

        cptVoxel = 0
        for i in range(self.x):
            for j in range(self.y):
                if imgTest[i][j] == 1:
                    cptVoxel += 1
                if self.topologyMin[i][j] == 1:
                    imgTest[i][j] = 1

        #clean up
        rm = Popen(["rm","topo.pyc"])
        rm.wait()

        #write the new topo
        topo = open("topo.py","w")
        topo.write("topology = [")

        for i in range(self.x):
            topo.write("{0},".format(imgTest[i]))
    
        topo.write("]")
        topo.close()

        #Popen sofa
        a = Popen(["runSofa", "-g", "batch", "-n", "10", "test1.pyscn"], stdout=PIPE, universal_newlines=True)
        astdout, _ = a.communicate()

        a.stdout.close()
        
        #Parse
        temp = astdout.split("animation")
        temp = temp[2:]
        temp = temp[:len(temp)-1] 
        
        pos = []
        for t in temp: #for all step
            tSplit = t.split(",")
            
            for i in tSplit:#for all value
                try:
                    posUnit = float(i)
                    
                    if posUnit >= 40:
                        return sys.maxsize
                    pos.append(posUnit)
                except ValueError:
                    pass
                    
        
        res = max(pos)
        #TODO valentin : moyenne des carré
        
        return res + (cptVoxel * 0.1)
