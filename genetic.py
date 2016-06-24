from indi import *

class Population():
    def __init__(self, popMax=100, popAugmentation=100):
        self.numberOfIndi = 0
        self.popMax = popMax
        self.pop =[]

    def addIndi(self, i):
        #incr numberOfNetwork
        self.numberOfIndi += 1
        self.pop.append(i)

    def reducePopulation(self):
        self.pop = sorted(self.pop, key = lambda x : x.fitness)
        self.pop = self.pop[:self.popMax]

    def cleanPop(self):
        self.pop = []
        self.numberOfIndi = 0


class GeneticAlgo():

    def __init__(self, fitnessFun, population):
        self.pop = population
        self.fitnessFun = fitnessFun

        self.nbCycle = 0

        self.best = 25
        
        self.nbAugmentation = 200
        self.ratioAdd = 0.33
        self.ratioCross = 0.33
        self.ratioClean = 0.33

        self.nbAdd = int(self.nbAugmentation * self.ratioAdd) 
        self.nbCross = int(self.nbAugmentation * self.ratioCross) 
        self.nbClean = int(self.nbAugmentation * self.ratioClean) 
        
    def evolve(self):
        self.nbCycle += 1

        self.pop.reducePopulation()
        newIndi = []

        for i in range(self.best):
            newIndi.append(self.pop.pop[i])
        
        for alpha in range(self.nbAdd):
#            print("add {0}".format(alpha))
            s1 = random.choice(self.pop.pop)
            s2 = random.choice(self.pop.pop)
            s3 = random.choice(self.pop.pop)
            s4 = random.choice(self.pop.pop)

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
            child.addRandomSquare()
            newIndi.append(child)

        for alpha in range(self.nbAdd):
#            print("add {0}".format(alpha))
            s1 = random.choice(self.pop.pop)
            child = best.copy()
            child.removeRandomSquare()
            newIndi.append(child)

            
            
        for alpha in range(self.nbCross):
#            print("cross {0}".format(alpha))
            s1 = random.choice(self.pop.pop)
            s2 = random.choice(self.pop.pop)
            s3 = random.choice(self.pop.pop)
            s4 = random.choice(self.pop.pop)

            if s1.fitness < s2.fitness:
                best1 = s1
            else:
                best1 = s2

            if s3.fitness < s4.fitness:
                best2 = s3
            else:
                best2 = s4

            child1, child2 = best1.crossOver(best2)
            newIndi.append(child1)
            newIndi.append(child2)

        self.pop.cleanPop()
        
        for i in newIndi:
            self.fitnessFun.computeValue(i)
            self.pop.addIndi(i)
