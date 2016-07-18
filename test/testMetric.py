#!/usr/bin/python3 -O
#############################################################################
# Contributors:
#	- created by Valentin Oczwarek
#############################################################################
import sys

sys.path.insert(0,"..")
from indi import *
from genetic import *
from fitness import *

sizex, sizey = 16, 16

print(sys.argv[0]+" IS DEPRECATED---SHOULD BE REMOVED----")
sys.exit(-1)
p = Population()

imageDict = {
    1:("circle", circle(sizex, sizey)),
    2:("square",square(sizex, sizey, int(sizex/2), int(sizey/2))),
    3:("fourSquare",fourSquare(sizex, sizey)),
    4:("cross",cross(sizex, sizey, int(sizex/2), int(sizey/2))),
}

metricDict = {
    1:("hausdorff"),
    2:("hausdorffAverage"),
    3:("SorensenDice"),
    4:("maxRessemblance"),
}

for forme in range(1,5):
    print(imageDict[forme][0])
    print("     ", end="")
    for i in range(4,5):
        print(metricDict[i], end=" ")

    print("")
    for metric in range(1,5):
        print(metricDict[i], end=" ")
        f = FitnessImage(imageDict[forme][0],imageDict[forme][1], metric,sizex,sizey)

        for _ in range(100):
            a = Indi(sizex,sizey)
            a.addRandomSquare()
            f.computeValue(a)
            p.addIndi(a)

        g = GeneticAlgo(f, p)

        for alpha in range(100):
            g.evolve()

        best = f.bestOverAll
        for metric in range(1,5):
            f = FitnessImage(imageDict[forme][0],imageDict[forme][1], metric,sizex,sizey)
            f.simulate(best)
