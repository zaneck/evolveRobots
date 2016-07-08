import threading

import numpy as np
from subprocess import Popen, PIPE, call

from fitness import Fitness
from indi import *

from config import Config

class FitnessSofa(Fitness):
    def __init__(self, name, sofaScene="test1.pyscn", topologyMinFile="minTopoTest1", x=10, y=10):
        Fitness.__init__(self)
        self.name=name
        
        self.x = x
        self.y = y

        self.sofaScene = sofaScene

        sys.path.insert(0,"sofaScene")
        
        exec("import {0}".format(topologyMinFile)) 
        self.topologyMin = sys.modules[topologyMinFile].topology

        #building working directory for the threads
        allThread = threading.enumerate()
        mainThread = threading.main_thread()

        for t in allThread:
            if t != mainThread:
                Popen(["mkdir", "-p", "/tmp/evolveRobots/{0}".format(t.ident)])
                Popen(["cp", "sofaScene/controller.py", "sofaScene/"+sofaScene, "sofaScene/tools.py", "/tmp/evolveRobots/{0}".format(t.ident)]) #copy object
            
    def simulate(self, n):
        idThread = threading.get_ident()

        imgTest = n.toMatrice()
        cptVoxel = 0
        for i in range(self.x):
            for j in range(self.y):
                if imgTest[i][j] == 1:
                    cptVoxel += 1
                if self.topologyMin[i][j] == 1:
                    imgTest[i][j] = 1
        
        #clean up
        rm = Popen(["rm","/tmp/evolveRobots/{0}/topo.pyc".format(idThread)]) #add /tmp/thread.ident
        rm.wait()

        #write the new topo
        topo = open("/tmp/evolveRobots/{0}/topo.py".format(idThread),"w") #add /tmp/thread.ident
        topo.write("topology = [")

        for i in range(self.x):
            topo.write("{0},".format(imgTest[i]))
    
        topo.write("]")
        topo.close()

        #Popen sofa
        a = Popen(["runSofa", "-g", "batch", "-n", "50", "/tmp/evolveRobots/{0}/{1}".format(idThread, self.sofaScene)], stdout=PIPE, universal_newlines=True) #add /tmp/thread.ident
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
        
        return (res * Config.fitnessRateScore) + (cptVoxel * Config.fitnessRateVoxel)
