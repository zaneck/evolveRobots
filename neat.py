import math

from network import *
from population import *


class Neat():

    def __init__(self, population, fitnessFun):
        self.population = population
        self.fitnessFun = fitnessFun

        self.nbCycle = 0

        self.nodeEdgeRate = 0.20
        self.addNodeRate = 0.35
        self.addEdgeRate = 0.65

        self.retry = 10
        
    #do not generate the first gen
    def evolve(self):
        self.nbCycle += 1
        
        #Select the best
        self.population.reducePopulation()
        
        #Calcul species ratio
        nbAugmentation = self.population.numberOfAugmentation()
        
        #gen new network
        #addNode addEdge
        newNetwork = []
        cpt = 0
        for k in self.population.species.keys():
            for n in range(math.ceil(nbAugmentation[cpt] * self.nodeEdgeRate)):
                child = self.newChildAddNodeEdge(self.population.species[k])
                if child != None:
                    newNetwork.append(child)

        #weight mut
        for k in self.population.species.keys():
            for n in self.population.species[k]:
                child = self.newChildWeight(n)
                if child != None:
                    newNetwork.append(child)

        #CrossOver
                    
        #clean old Population
        self.population.cleanSpecies()

        #compute fitness and behavior
        for n in newNetwork:
            self.fitnessFun.computeValue(n)
        
        #add new network to Population
        for n in newNetwork:
            self.population.addNetwork(n)
        
        #adjust Fitness
        self.population.setAdjustFitness()

    def newChildWeight(self, n):
        test = random.random()
        if test <= 0.1 :
            return None

        child = n.copy()
        uniformPerturb = random.random()

        for e in child.edges:
            wheel = random.random()
            if wheel <=0.1:
                e.weight = Edge.randomWeight()
            else:
                e.weight *= uniformPerturb

        return child
        
    def newChildAddNodeEdge(self, species):
        #select a child between 4 indi
        c1 = random.choice(species)
        c2 = random.choice(species)
        c3 = random.choice(species)
        c4 = random.choice(species)

        if c1.fitnessAdjust > c2.fitnessAdjust:
            bestC1C2 = c1
        else:
            bestC1C2 = c2

        if c3.fitnessAdjust > c4.fitnessAdjust:
            bestC3C4 = c3
        else:
            bestC3C4 = c4
            
        if bestC1C2.fitnessAdjust > bestC3C4.fitnessAdjust:
            best = bestC1C2
        else:
            best = bestC3C4

        #clone
        child = best.copy()
        #add Edge or node
        choice = random.random()
        nodes = list(set(child.inputNodes) | set(child.hiddenNodes) | set(child.outputNodes))
        flag = False
        
        if choice <= self.addNodeRate:
            #addNode
            for _ in range(self.retry):
                t = child.addNode((random.choice(nodes)).idNode, (random.choice(nodes)).idNode)
                if t == True:
                    return child
                
        else:
            #addEdge
            for _ in range(self.retry):
                t = child.addEdge((random.choice(nodes)).idNode, (random.choice(nodes)).idNode)
                if t == True:
                    return child
