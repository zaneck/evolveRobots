from imgTools import *
from network import *
from population import *
from neat import *
from noveltySearch import *

from circleFitness import *

def resXor(n):
        cptOk = 0
        testSuite = [[0,0],[0,1],[1,0],[1,1]]
        
        for t in testSuite:        
            test = (t[0] != t[1])
            val = n.computeNetwork([t[0],t[1],1])[0]

            print([t, test,val])
            
def createNeat(nbIn, nbOut, fun):
    inNodes = []
    outNodes = []

    f = fun()
    p = Population()
    
    for _ in range(nbIn):
        inNodes.append(Node(inout="in"))

    for _ in range(nbOut):
        outNodes.append(Node(inout="out"))

    firstGen = []
    for _ in range(100):
        n = Network(inNodes, outNodes)
        n.linkInputOutput()
        f.computeValue(n)
        p.addNetwork(n)

    p.setAdjustFitness()

    n = Neat(p,f)
    return (n,f)
    
#n, f = createNeat(2,1, NoveltyFitnessXor)

n, f = createNeat(2,1, NoveltyFitnessCircle)


for ticks in range(25):
        print("evolve {0}".format(ticks))
        n.evolve()

#print([f.bestOverAll.behavior,f.bestOverAll.fitness, f.bestOverAll.fitnessReal])

(f.bestOverAll).printNetwork()

#resXor(f.bestOverAll)

img = makeImg(f.bestOverAll, 32,32)
printPict(img, 32, 32)
