from imgTools import *
from network import *
from population import *
from neat import *
from noveltySearch import *

import sys

def resXor(n):
        cptOk = 0
        testSuite = [[0,0],[0,1],[1,0],[1,1]]
        
        for t in testSuite:        
            test = (t[0] != t[1])
            val = n.computeNetwork([t[0],t[1],1])[0]

            print([t, test,val])
            
def createNeat(nbIn, nbOut, fun, name):
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

    n = Neat(p,f, name=name)
    return (n,f)
    
#n, f = createNeat(2,1, NoveltyFitnessXor)

if __name__ == '__main__':
        fitnessDict ={
                1:NoveltyFitnessCircle,
                2:NoveltyFitnessCross,
                3:NoveltyFitnessSquare,
                4:NoveltyFitnessFourSquare,

                }
        
        n, f = createNeat(2,1, fitnessDict[int(sys.argv[1])], name=sys.argv[2])


        for ticks in range(100):
                print("evolve {0}".format(ticks))
                n.evolve()

        #print([f.bestOverAll.behavior,f.bestOverAll.fitness, f.bestOverAll.fitnessReal])

        (f.bestOverAll).printNetwork()

        #resXor(f.bestOverAll)

        # img = makeImg(f.bestOverAll, 32,32)
        # matriceToImage(img, 32,32, "testOne.png")
        # printPict(img, 32, 32)
