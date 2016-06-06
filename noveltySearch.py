from fitnessFun import Fitness
from scipy.spatial import distance

class NoveltySearch(Fitness):
    
    def __init__(self, rho=0.5 ,k=15):
        Fitness.__init__(self)

        self.name = "Novelty Search base fitness function"

        self.cptInsert = 0
        self.cptReject = 0

        self.archive=[] # elder

        self.k = k # k nearest neighbor
        self.rho = rho # initial archive threshold

    #load value into behavior var, use simulation
    def computeValue(self, n):
        #compute fitness and behavior
        simula = self.simulate(n)
        n.behavior = simula[0]
        n.fitnessReal = simula[1]

        if self.bestOverAll == None:
            self.archive.append(n)
            self.bestOverAll = n
            self.cptInsert += 1
            n.fitness = 0
            return
            
        #save the best
        if self.bestOverAll.fitnessReal < n.fitnessReal:
            self.bestOverAll = n

        s = self.sparness(n)
        
        #si s > seuil add to archive
        if s >= self.rho:
            self.cptInsert += 1
            self.archive.append(n)
            
            if self.cptInsert == 4:
                self.cptInsert = 0
                self.cptReject = 0
                self.rho *= 1.20
                print("rho {0}".format(self.rho))
        else:
            self.cptReject += 1

            if self.cptReject == 2500:
                self.cptInsert = 0
                self.cptReject = 0
                self.rho /= 1.05
        n.fitness = s

#        return s

    def sparness(self, n):
        neighbor = []
        sumDist = 0

        for a in self.archive:
            d = distance.euclidean(a.behavior, n.behavior)
            neighbor.append(d)
            
        neighbor = sorted(neighbor)
        
        for l in range(min(len(neighbor),self.k)):
            sumDist += neighbor[l]

        return sumDist /(min(len(neighbor),self.k)+1)

    #need to define this, return ((b0,b1,..,bn), fitness)
    def simulate(self, n):
        raise NotImplementedError


class NoveltyFitnessXor(NoveltySearch):
    def __init__(self):
        NoveltySearch.__init__(self)
        self.name="Novelty Xor fitness fun"

    def simulate(self, n):
        cptOk = 0
        testSuite = [[0,0],[0,1],[1,0],[1,1]]
        
        b=[]

        for t in testSuite:        
            test = (t[0] != t[1])
            val = n.computeNetwork([t[0],t[1],1])[0]
            if (val>=0.0 and test == True) or (val<0.0 and test == False):
                cptOk += 1
            
            if val>=0.0:
                b.append(1)
            else:
                b.append(0)

        return (b,cptOk)
