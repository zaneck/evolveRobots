from network import *
from population import *
from neat import *
from noveltySearch import *


def createNeat(nbIn, nbOut):
    inNodes = []
    outNodes = []

    f = NoveltyFitnessXor()
    p = Population()
    
    for _ in range(nbIn):
        inNodes.append(Node(inout="in"))

    for _ in range(nbOut):
        outNodes.append(Node(inout="out"))

    firstGen = []
    for _ in range(150):
        n = Network(inNodes, outNodes)
        n.linkInputOutput()
        f.computeValue(n)
        p.addNetwork(n)

    p.setAdjustFitness()

    n = Neat(p,f)
    return (n,f)
    
n, f = createNeat(2,1)


for _ in range(200):
    n.evolve()


print([f.bestOverAll.behavior,f.bestOverAll.fitness, f.bestOverAll.fitnessReal])
