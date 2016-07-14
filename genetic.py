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
from distancefct import sorensenDice

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
        
    def evolve(self, historyLog=False):
        print("========================= generation {0} ================================".format(self.nbCycle))
        self.population.reducePopulation()
        newCandidates = []
        newBest = []
        events = {}
        
        for i in range(self.best):
            newBest.append(self.population.members[i])
        
        for alpha in range(self.nbAdd):
            # Among 4 random choice select the one with the smallest fitness score and select it 
            # as a parent for candidate that will be generated.
            s1 = random.choice(self.population.members)
            s2 = random.choice(self.population.members)
            s3 = random.choice(self.population.members)
            s4 = random.choice(self.population.members)

            if s1.fitness < s2.fitness:
                best1 = s1
            else:
                best1 = s2

            if s3.fitness < s4.fitness:
                best2 = s3
            else:
                best2 = s4

            if best1.fitness < best2.fitness:
                best = best1
            else:
                best = best2

            child = best.copy()
            child.addRandomShape()
            newCandidates.append(child)
            if historyLog:
                events[child] = [child, ["A", best, None], self.nbCycle, -1]
        
        for alpha in range(self.nbClean):
            # todo(valentin): pourquoi tu ne prend pas 4 éléments comme pour le add ou le cross ?
            s1 = random.choice(self.population.members)
            child = best.copy()
            res = child.removeRandomSquare()
            if res == 1:
                newCandidates.append(child)
            
            if historyLog:
                events[child] = [child, ["D", best, None], self.nbCycle, -1]
            
        for alpha in range(self.nbCross):
            samples = random.sample(self.population.members, 2)
            
            child1, child2 = samples[0].crossOver(samples[1])
            newCandidates.append(child1)
            newCandidates.append(child2)
            
            events[child1] = [child1, ["X", best1, best2], self.nbCycle, -1]
            events[child2] = [child2, ["X", best1, best2], self.nbCycle, -1]
            

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
