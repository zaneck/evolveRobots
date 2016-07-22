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
        self.populationMax = Config.PopulationPopMax
        self.members =[]

    def __len__(self):
        return len(self.members)

    def addIndi(self, i):
        self.numberOfIndi += 1
        self.members.append(i)

    def reducePopulation(self):
        """Reduce the population to keep it below self.populationMax. The Candidates that are 
           removed are the one with the highest fitness function """
        self.members = sorted(self.members, key = lambda x : x.fitness)
        self.members = self.members[:self.populationMax]

    def cleanPop(self):
        self.members = []
        self.numberOfIndi = 0

    def tournament(self, nbCandidate=4):
        s = random.choice(self.members) 

        for _ in range(nbCandidate):
            sCandidate = random.choice(self.members)
            if s.fitness > sCandidate.fitness:
                s = sCandidate
            
        return s
        
class GeneticAlgo(object):
    def __init__(self, fitnessFun, population):
        self.population = population
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

#        self.nbSplit = 30
        
    def evolve(self, historyLog=False):
        print("========================= generation {0} ================================".format(self.nbCycle))
        self.population.reducePopulation()
        newCandidates = []
        newBest = []
        events = {}
        
        for i in range(self.best):
            newBest.append(self.population.members[i])
        
        for _ in range(self.nbAdd):
            best = self.population.tournament()
            child = best.copy()
            child.addRandomShape()
            newCandidates.append(child)
            if historyLog:
                events[child] = [child, ["A", best, None], self.nbCycle, -1]
        
        for _ in range(self.nbClean):
            best = self.population.tournament()
            child = best.copy()
            res = child.removeShapeAtRandom()
            if res == 1:
                newCandidates.append(child)           

                if historyLog:
                    events[child] = [child, ["D", best, None], self.nbCycle, -1]
                    
        for _ in range(self.nbCross):
            best1 = self.population.tournament()
            best2 = self.population.tournament()
            
            child1, child2 = best1.crossOver(best2)
            newCandidates.append(child1)
            newCandidates.append(child2)

            if historyLog:
                events[child1] = [child1, ["X", best1, best2], self.nbCycle, -1]
                events[child2] = [child2, ["X", best1, best2], self.nbCycle, -1]
            

        # for _ in range(self.nbSplit):
        #     best = self.population.tournament()
        #     child = best.copy()
        #     res = child.splitSquare()
            
        #     if res == 1:
        #         newCandidates.append(child)           
        #         if historyLog:
        #             historyLog.addEvent(child, ["S", best, None], self.nbCycle)    

        self.population.cleanPop()

        # Evaluates all the candidates. 
        self.fitnessFun.computeValues(newCandidates)
        if historyLog:
                for c in newCandidates:
                        evt = events[c]
                        evt[3] = c.fitness
                        historyLog.addEvent(evt[0], evt[1], evt[2], 1.0/evt[3])    
                        
        for i in newCandidates:
            self.population.addIndi(i)

        for i in newBest:
            self.population.addIndi(i)
            
        if dump.activated():
                dump.addGeneration(newCandidates, self.fitnessFun) 
        self.nbCycle += 1
