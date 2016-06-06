from network import *

class Fitness:
    def __init__(self):
        self.name="Abstract fitness fun"
        self.bestOverAll = None
        
    def computeValue(self, n):
        fit = self.simulate(n)

        #save the best
        if self.bestOverAll == None or self.bestOverAll.fitness < fit:
            self.bestOverAll = n

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
