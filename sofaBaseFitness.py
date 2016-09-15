# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
import threading
import os
import hashlib

from subprocess import Popen, PIPE, call

from fitness import Fitness
from indi import *

from config import Config

from agregator import *


def binarybin(values):
        """This binning function is using the first value at [0]. If < 0 it return 1.0 (there is matter at
           this location. Otherwise it return 0 (no matter)"""
        if values[0] < 0:
                return 1
        return 0

def computeKey(m):
        res = ""
        for i in range(len(m)):
                for j in range(len(m[0])):
                        res+="{0}".format(m[i][j])
        m= hashlib.md5()
        m.update(res.encode())
        hashcode = m.hexdigest()
        return hashcode
                        
def addCache(k, s, raw, table):
        if k in table:
                testRaw = table[k][1]

                for i in range(len(testRaw)):
                        for j in range(len(testRaw[0])):
                                if testRaw[i][j] != raw[i][j]:
                                        print("ERROR")
                                        raise NotImplementedError
        else:
                table[k]=(s,raw)
        
        return 1


class FitnessSofa(Fitness):
        def __init__(self, name, theCanvas,
                     sofaScene="test1.pyscn", topologyMinFile="minTopoTest1"):
                Fitness.__init__(self)
                self.name=name
                
                self.canvas = theCanvas        
                self.sofaScene = sofaScene
                
                sys.path.insert(0, Config.fitnessSofaSceneFolder)
        
                exec("import {0}".format(topologyMinFile)) 
                self.topologyMin = sys.modules[topologyMinFile].topology

                #building working directory for the threads
                allThread = threading.enumerate()
                mainThread = threading.main_thread()

                for t in allThread:
                        if t != mainThread:
                                Popen(["mkdir", "-p", "/tmp/evolveRobots/{0}".format(t.ident)])
                                Popen(["cp", Config.fitnessSofaSceneFolder + "/controller.py", Config.fitnessSofaSceneFolder + "/"+sofaScene, Config.fitnessSofaSceneFolder + "/tools.py", "/tmp/evolveRobots/{0}".format(t.ident)]) #copy object

                ##############
                # CACHE INIT #
                ##############
                self.cacheLock = threading.Lock()
                self.cache = {}
                
                
        def toMatrice(self, candidate):
                return self.canvas.toMatrice(candidate, binarybin)

        """
        Create the Candidate matrix representation.
        return the matrix and the number of voxel
        The function use the minTopo.py file,
        where the 1 value code for materials and
        2 for no materials
        """
        def makeCandidateMatrix(self, candidate):
                #imgTest = self.canvas.toMatrice(candidate, binarybin)
                imgTest = self.toMatrice(candidate)
                cptVoxel = 0
                for i in range(self.canvas.resolution[0]):
                        for j in range(self.canvas.resolution[1]):
                                if self.topologyMin[i][j] == 2:
                                        imgTest[i][j] = 0
                                if self.topologyMin[i][j] == 1:
                                        imgTest[i][j] = 1
                                if imgTest[i][j] == 1:
                                        cptVoxel += 1
                                

                return (imgTest, cptVoxel)
        """
        Parse the result of the simulation, stdout from Sofa create by controller.py
        """
        def parseResult(self, astdout):
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
                                        if posUnit >= 70:
                                                return [sys.maxsize]
                                        pos.append(posUnit)
                                except ValueError:
                                        pass
                return pos

        def writeCandidateMatrix(self, basedir, candidate, imgTest):
                #clean up
                if os.path.exists(basedir+"topo.pyc"):
                        rm = Popen(["rm",basedir+"topo.pyc"]) 
                        rm.wait()

                #write the candidate shape into a file. This file is then read by the python script used to 
                # load the sofa scene.
                topo = open(basedir+"topo.py","w") 
                topo.write("#Topology for candidate #{0} score={1}\n".format(candidate.myId, candidate.fitness))
                topo.write("topology = [\n")

                # Into the shape description file we are writing the image generated from the 
                # candidate using the canvas and the provided binning function.
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

        def writeBestResult(self, filename):
                imgTest, cptVoxel = self.makeCandidateMatrix(self.bestOverAll)
                self.writeCandidateMatrix(filename, self.bestOverAll, imgTest)
                
        def simulate(self, candidate):
                idThread = threading.get_ident()
                imgTest, cptVoxel = self.makeCandidateMatrix(candidate)
            
                basedir = "/tmp/evolveRobots/{0}/".format(idThread)

                #########
                # CACHE #
                #########
                key = computeKey(imgTest)
                fitScore = None
                with self.cacheLock:
                        if key in self.cache:
                                fitScore = self.cache[key]
        
                if fitScore != None:
                        #     for i in range(len(imgTest)):
                        #             for j in range(len(imgTest[0])):
                        #                     if imgTest[i][j] != fitScore[1][i][j]:
                        #                             print("ERROR")
                        #                            raise NotImplementedError
                        return fitScore[0]
            
                # In order to score the candidate we need to benchmark it using a sofa simulation
                # the following line is starting sofa as an external application. Sofa is started 
                # in batch mode (-g batch) and will do Config.fitnessTimeStep iterations (-n).  
                # At each iteration step the score will be printed to the standard output 
                self.writeCandidateMatrix(basedir, candidate, imgTest)
                a = Popen(["runSofa", "-g", "batch", "-n", "{0}".format(Config.fitnessTimeStep), "/tmp/evolveRobots/{0}/{1}".format(idThread, self.sofaScene)], stdout=PIPE, universal_newlines=True) #add /tmp/thread.ident
                astdout, _ = a.communicate()
                a.stdout.close()

                pos = self.parseResult(astdout)

                #print(pos)
            
                if Config.fitnessAgregator == "max":
                        res = maxAgregator(pos)
                elif Config.fitnessAgregator == "min":
                        res = minAgregator(pos)
                elif Config.fitnessAgregator == "average":
                        res = averageAgregator(pos)
                else:
                        raise ValueError

                final = (res * Config.fitnessRateScore) + (cptVoxel * Config.fitnessRateVoxel)
                #########
                # CACHE #
                #########
                with self.cacheLock:
                        addCache(key, final, imgTest, self.cache)
                    
                #TODO valentin : moyenne des carré
                return final
