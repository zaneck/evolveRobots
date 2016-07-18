# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. 
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
from config import Config
from indi import *
import dump 

class Population(object):
    def __init__(self):
        self.numberOfIndi = 0
        self.popMax = Config.PopulationPopMax
        self.pop =[]

    def __len__(self):
        return len(self.pop)

    def addIndi(self, i):
        #incr numberOfNetwork
        self.numberOfIndi += 1
        self.pop.append(i)

    def reducePopulation(self):
        """Reduce the population to keep it below self.popMax. The Candidates that are 
           removed are the one with the highest fitness function """
        self.pop = sorted(self.pop, key = lambda x : x.fitness)
        self.pop = self.pop[:self.popMax]

    def cleanPop(self):
        self.pop = []
        self.numberOfIndi = 0

    def tournament(self, nbCandidate=4):
        s = random.choice(self.pop) 

        for _ in range(nbCandidate):
            sCandidate = random.choice(self.pop)
            if s.fitness > sCandidate.fitness:
                s = sCandidate
            
        return s
        
class GeneticAlgo(object):
    def __init__(self, fitnessFun, population):
        self.pop = population
        self.fitnessFun = fitnessFun

        self.nbCycle = 0

        self.best = Config.geneticBest
        
        self.nbAugmentation = Config.genticNbAugmentation
        self.addRate = Config.genticAddRate
        self.crossRate = Config.genticCrossRate
        self.cleanRate = Config.genticCleanRate

        self.nbAdd = int(self.nbAugmentation * self.addRate) 
        self.nbCross = int(self.nbAugmentation * self.crossRate) 
        self.nbClean = int(self.nbAugmentation * self.cleanRate) 
        
    def evolve(self, historyLog=False):
        self.pop.reducePopulation()
        newCandidates = []
        newBest = []
        
        for i in range(self.best):
            newBest.append(self.pop.pop[i])
        
        for alpha in range(self.nbAdd):
            best = self.pop.tournament()
            
            child = best.copy()
            child.addRandomSquare()
            newCandidates.append(child)
            if historyLog:
                historyLog.addEvent(child, ["A", best, None], self.nbCycle)    
        
        for alpha in range(self.nbClean):
            best = self.pop.tournament()
            child = best.copy()
            res = child.removeRandomSquare()
            if res == 1:
                newCandidates.append(child)           
                if historyLog:
                    historyLog.addEvent(child, ["D", best, None], self.nbCycle)    
            
        for alpha in range(self.nbCross):
            best1 = self.pop.tournament()
            best2 = self.pop.tournament()
            
            child1, child2 = best1.crossOver(best2)
            newCandidates.append(child1)
            newCandidates.append(child2)

            if historyLog:
                historyLog.addEvent(child1, ["X", best1, best2], self.nbCycle)    
                historyLog.addEvent(child2, ["X", best1, best2], self.nbCycle)    


        self.pop.cleanPop()

        # Evaluates all the candidates. 
        self.fitnessFun.computeValues(newCandidates)
        
        for i in newCandidates:
            self.pop.addIndi(i)

        for i in newBest:
            self.pop.addIndi(i)
            
        if dump.activated():
                dump.addGeneration(newCandidates) 
        self.nbCycle += 1
