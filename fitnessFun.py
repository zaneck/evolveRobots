from network import *
from imgTools import *

class Fitness:
    def __init__(self):
        self.name="Abstract fitness fun"
        self.bestOverAll = None
        self.bestNumber = 0
        
    def computeValue(self, n):
        fit = self.simulate(n)

        n.fitness = fit

        #Save the man
        img = makeImg(n, self.x, self.y)
        fileName = "{0}/folks/{1}.png".format(self.name, n.idNetwork)
        matriceToImage(img, self.x, self.y, fileName)

        self.networkSet.write("{2} {0} {1}\n".format(n.idNetwork, n.fitness, n.philogenie))
        
        #end save
        
        if self.bestOverAll == None:
            self.bestOverAll = n
            return
        
        #save the best
        if self.bestOverAll.fitness < fit:
            self.bestOverAll = n

            print("New record {0}".format(self.bestOverAll.fitness))

            fileName = "{0}/best/{1}-{2}-{3}.png".format(self.name,self.bestNumber, n.idNetwork, n.fitness)
            matriceToImage(img, self.x, self.y, fileName)
            self.bestNumber +=1
            
        return fit

    def simulate(self, n):
        raise NotImplementedError

# for a 2 input one output network
class FitnessXor(Fitness):
    def __init__(self):
        Fitness.__init__(self)
        self.name="Xor fitness fun"

    def simulate(self, n):
        cptOk = 0
        testSuite = [[0,0],[0,1],[1,0],[1,1]]

        for t in testSuite:        
            test = (t[0] != t[1])
            val = n.computeNetwork([t[0],t[1]])[0]
            if (val>=0.0 and test == True) or (val<0.0 and test == False):
                cptOk += 1

        return cptOk



class FitnessCircle(Fitness):
    def __init__(self):
        Fitness.__init__(self)
        self.name="images/circleSimple/"

        self.networkSet = open(self.name+"networkSet.txt", "w")
        
        self.x = 64
        self.y = 64

        self.img = circle(self.x, self.y, color=1)
        printPict(self.img, self.x, self.y)
        
        
    def simulate(self, n):
        imgTest = makeImg(n, self.x, self.y)
        cptOk = fitnessP(imgTest, self.img, self.x, self.y)
        
        return cptOk

    

