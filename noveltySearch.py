from imgTools import *
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

        self.bestNumber = 0
        
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
            print("New record {0}".format(self.bestOverAll.fitnessReal))

            img = makeImg(n, self.x, self.y)
            fileName = "{0}{1}-{2}.png".format(self.name,self.bestNumber, n.idNetwork)
            matriceToImage(img, self.x, self.y, fileName)
            self.bestNumber +=1
            
        s = self.sparness(n)
        
        #si s > seuil add to archive
        if s >= self.rho:
            self.cptInsert += 1
            self.archive.append(n)
            
            if self.cptInsert == 4:
                self.cptInsert = 0
                self.cptReject = 0
                self.rho *= 1.20
#                print("rho {0}".format(self.rho))
        else:
            self.cptReject += 1

            if self.cptReject == 2500:
                self.cptInsert = 0
                self.cptReject = 0
                self.rho /= 1.05
                
        n.fitness = s+1
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

class NoveltyFitnessCross(NoveltySearch):
    def __init__(self):
        NoveltySearch.__init__(self)
        self.name="images/cross/"

        self.x = 64
        self.y = 64
        
        self.img = cross(self.x, self.y, int(self.x/2),int(self.y/2))
        printPict(self.img, self.x, self.y)
        
        
    def simulate(self, n):
        imgTest = makeImg(n, self.x, self.y)

        cptOk = fitnessP(imgTest, self.img, self.x, self.y)

        behavior = blockBehavior(imgTest, self.img, self.x, self.y)
        
        return (behavior, cptOk)


class NoveltyFitnessCircle(NoveltySearch):
    def __init__(self):
        NoveltySearch.__init__(self)
        self.name="images/circle/"

        self.x = 64
        self.y = 64

        self.img = circle(self.x, self.y, color=1)
        printPict(self.img, self.x, self.y)
        
        
    def simulate(self, n):
        imgTest = makeImg(n, self.x, self.y)

        cptOk = fitnessP(imgTest, self.img, self.x, self.y)

        behavior = blockBehavior(imgTest, self.img, self.x, self.y)
        
        return (behavior, cptOk)


class NoveltyFitnessSquare(NoveltySearch):
    def __init__(self):
        NoveltySearch.__init__(self)
        self.name="images/square/"

        self.x = 64
        self.y = 64

        self.img = square(self.x, self.y, int(self.x/2),int(self.y/2))
        printPict(self.img, self.x, self.y)
        
        
    def simulate(self, n):
        imgTest = makeImg(n, self.x, self.y)

        cptOk = fitnessP(imgTest, self.img, self.x, self.y)

        behavior = blockBehavior(imgTest, self.img, self.x, self.y)
        
        return (behavior, cptOk)


class NoveltyFitnessFourSquare(NoveltySearch):
    def __init__(self):
        NoveltySearch.__init__(self)
        self.name="images/foursquare/"

        self.x = 64
        self.y = 64
        
        self.img = fourSquare(self.x, self.y, color=1, Rradius=15)
        printPict(self.img, self.x, self.y)
        
        
    def simulate(self, n):
        imgTest = makeImg(n, self.x, self.y)

        cptOk = fitnessP(imgTest, self.img, self.x, self.y)

        behavior = blockBehavior(imgTest, self.img, self.x, self.y)
        
        return (behavior, cptOk)
    
