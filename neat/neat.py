import math

from network import *
from population import *
from imgTools import *

class Neat():

    def __init__(self, population, fitnessFun, name="neat"):
        self.name = name

        self.population = population
        self.fitnessFun = fitnessFun

        self.nbCycle = 0

        self.nodeEdgeRate = 0.30
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
            if len(self.population.species[k]) > 0:
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
        for _ in range(30):
            s1 = random.choice(list(self.population.species.keys()))
            s2 = random.choice(list(self.population.species.keys()))

            if len(self.population.species[s1]) <= 0 or len(self.population.species[s2]) <= 0:
                break

            n1a = random.choice(list(self.population.species[s1]))
            n1b = random.choice(list(self.population.species[s1]))

            if n1a.fitness < n1a.fitness:
                n1 = n1a
            else:
                n1 = n1b

            n2a = random.choice(list(self.population.species[s2]))
            n2b = random.choice(list(self.population.species[s2]))

            if n2a.fitness < n2a.fitness:
                n2 = n2a
            else:
                n2 = n2b

            if n1 !=n2:
                child = n1.crossover(n2)
            else:
                break
            if child != None:
                newNetwork.append(child)
            
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

        # #DUMP IMG ALL NETWORK
        # os.mkdir(self.name+"/{0}".format(self.nbCycle))

        # for sk in self.population.species.keys():
        #     os.mkdir("{0}/{1}/{2}".format(self.name, self.nbCycle, sk.idNetwork))

        #     for n in self.population.species[sk]:
        #         img = makeImg(n, 64,64)
        #         matriceToImage(img, 64,64,
        #                        "{0}/{1}/{2}/{3}.png".format(self.name,self.nbCycle,sk.idNetwork,n.idNetwork))
        
    def newChildWeight(self, n):
        test = random.random()
        if test <= 0.1 :
            return None

        child = n.copy("w")
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
        #child = best.copy()
        #add Edge or node
        choice = random.random()
        flag = False
        
        if choice <= self.addNodeRate:
            child = best.copy("n")
            #addNode
            for _ in range(self.retry):
                nodes = list(set(child.inputNodes) | set(child.hiddenNodes) | set(child.outputNodes))
                t = child.addNode((random.choice(nodes)).idNode, (random.choice(nodes)).idNode)
                if t == True:
                    return child
                
        else:
            #addEdge
            child = best.copy("e")
            for _ in range(self.retry):
                nodes = list(set(child.inputNodes) | set(child.hiddenNodes) | set(child.outputNodes))
                t = child.addEdge((random.choice(nodes)).idNode, (random.choice(nodes)).idNode)
                if t == True:
                    return child
