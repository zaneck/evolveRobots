import sys

from neat import *
from network import *
from fitnessFun import *

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
        1:FitnessCircle,
#        2:FitnessCross,
 #       3:FitnessSquare,
  #      4:FitnessFourSquare,    
    }

    n, f = createNeat(2,1, fitnessDict[int(sys.argv[1])], name=sys.argv[2])


    for ticks in range(100):
        print("evolve {0}".format(ticks))
        n.evolve()

    f.networkSet.close()
    #print([f.bestOverAll.behavior,f.bestOverAll.fitness, f.bestOverAll.fitnessReal])
    
    (f.bestOverAll).printNetwork()
    
    #resXor(f.bestOverAll)

    img = makeImg(f.bestOverAll, 16,16)
    matriceToImage(img, 16,16, "best1616.png")
    

    img = makeImg(f.bestOverAll, 32,32)
    matriceToImage(img, 32,32, "best3232.png")

    
    img = makeImg(f.bestOverAll, 64,64)
    matriceToImage(img, 64,64, "best6464.png")
