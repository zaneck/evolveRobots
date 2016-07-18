import threading
import os

#import numpy as np
from subprocess import Popen, PIPE, call

from fitness import Fitness
from indi import *

from config import Config

def binarybin(values):
        """This binning function is using the first value at [0]. If < 0 it return 1.0 (there is matter at
           this location. Otherwise it return 0 (no matter)"""
        if values[0] < 0:
                return 1
        return 0

class FitnessSofa(Fitness):
    def __init__(self, name, theCanvas, sofaScene="test1.pyscn", topologyMinFile="minTopoTest1"):
        Fitness.__init__(self)
        self.name=name

        self.canvas = theCanvas        
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
    
    def toMatrice(self, candidate):
        return self.canvas.toMatrice(candidate, binarybin)
            
    def simulate(self, candidate):
        idThread = threading.get_ident()

        imgTest = self.canvas.toMatrice(candidate, binarybin)
        cptVoxel = 0
        for i in range(self.canvas.resolution[0]):
            for j in range(self.canvas.resolution[1]):
                if imgTest[i][j] == 1:
                    cptVoxel += 1
                if self.topologyMin[i][j] == 1:
                    imgTest[i][j] = 1
        
        #clean up
        basedir = "/tmp/evolveRobots/{0}/".format(idThread)
        if os.path.exists(basedir+"topo.pyc"):
                rm = Popen(["rm",basedir+"topo.pyc".format(idThread)]) 
                rm.wait()

        #write the candidate shape into a file. This file is then read by the python script used to 
        # load the sofa scene.
        topo = open(basedir+"topo.py","w") 
        topo.write("#Topology for candidate #{0}\n".format(candidate.myId))
        topo.write("topology = [\n")

        # Into the shape description file we are writing the image generated from the 
        # candidate using the canvas and the provided binning function. The matrix
        # is written in column row mode
        for j in range(self.canvas.resolution[1]):
                topo.write("[")
                topo.write("{0}".format(imgTest[0][j]))
                for i in range(1, self.canvas.resolution[0]):
                    topo.write(",{0}".format(imgTest[i][j]))
                if j == self.canvas.resolution[1]-1:
                        topo.write("]\n")
                else:                              
                        topo.write("],\n")
        topo.write("]")
        topo.close()

        
        # In order to score the candidate we need to benchmark it using a sofa simulation
        # the following line is starting sofa as an external application. Sofa is started 
        # in batch mode (-g batch) and will do 50 iterations (-n).  
        # At each iteration step the score will be printed to the standard output 
        a = Popen(["runSofa", "-g", "batch", "-n", "50", "/tmp/evolveRobots/{0}/{1}".format(idThread, self.sofaScene)], stdout=PIPE, universal_newlines=True) #add /tmp/thread.ident
        astdout, _ = a.communicate()

        a.stdout.close()
        
        #Parse the sofa output searching for the score. 
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
