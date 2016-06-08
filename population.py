import math

from network import *

class Population():

    def __init__(self, popMax=100, popAugmentation=100, speciesSeparation=3.0):
        self.species=None
        self.speciesSeparation = speciesSeparation

        self.numberOfNetwork = 0
        self.popMax = popMax
        self.popAugmentation = popAugmentation
        

    def addNetwork(self, n):
        #incr numberOfNetwork
        self.numberOfNetwork += 1

        #find species
        if self.species == None: #firstNetworkCase
            self.species ={n:[n]}

        else:
            flagInsert = False
            for k in self.species.keys(): #add into first match
                #distance beetween n and k
                d = k.distance(n)

                if d < self.speciesSeparation:
                    self.species[k].append(n)
                    flagInsert = True
            
            if flagInsert == False: #New species
                self.species[n].append[n]

    def setAdjustFitness(self):
        for k in self.species.keys():
            for n in self.species[k]:
                n.fitnessAdjust = n.fitness / len(self.species[k])
            
    def reducePopulation(self):
        #case "do nothing because, nothing to do"
        if self.numberOfNetwork <= self.popMax:
            return

        #calcul reduce ratio
        reduceRatio = (self.numberOfNetwork - self.popMax) / self.numberOfNetwork

        #for all species
        for k in self.species.keys():
            #sort using fitness
            self.species[k] = sorted(self.species[k], key = lambda x : x.fitnessAdjust, reverse=True)
            #numberOfOut
            outNumber = math.floor(len(self.species[k]) * reduceRatio)
            self.species[k] = self.species[k][:outNumber]
            #update numberOfNetwork
            self.numberOfNetwork -= outNumber

    def cleanSpecies(self):
        newSpecies = {}
        #randomize key
        for k in self.species.keys():
            newKey = random.choice(self.species[k])
            newSpecies[newKey] = []
        
        self.species = newSpecies
        self.numberOfNetwork = 0
        
    def numberOfAugmentation(self):
        res = []
        
        sumTotal = 0
        for k in self.species.keys():
            sumFitness = 0
            for s in self.species[k]:
                sumFitness += s.fitnessAdjust

            res.append(sumFitness)
            sumTotal += sumFitness

        if sumTotal == 0:
            return 0
        else:
            res = list(map(lambda x : math.floor((x*self.popAugmentation)/sumTotal), res))

            return res
