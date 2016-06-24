#!/usr/bin/python3 -O
#############################################################################
# Contributors:
#	- created by Valentin Oczwarek
#############################################################################
import sys

from indi import *
from genetic import *
from fitness import *

sizex, sizey = 64, 64

imageDict = {
    "1":("circle", circle(sizex, sizey)),
    "2":("square",square(sizex, sizey, int(sizex/2), int(sizey/2))),
    "3":("fourSquare",fourSquare(sizex, sizey)),
    "4":("cross",cross(sizex, sizey, int(sizex/2), int(sizey/2))),
}

metricDict = {
    "1":("hausdorff"),
    "2":("hausdorffAverage"),
    "3":("SorensenDice"),
    "4":("maxRessemblance"),
}

# todo(damien): Il faut une vrai gestion des arguments et des messages d'erreurs. 

shape = sys.argv[1]
shapeName = imageDict[shape][0]
shapeMatrix = imageDict[shape][1]

metric = sys.argv[2]

f = FitnessImage(shapeName, shapeMatrix, metric, sizex, sizey)

#todo(valentin): Gerer tous les parametres de l'algo, population, cycleMax... 
p = Population()

for _ in range(100):
    a = Indi(sizex, sizey)
    a.addRandomSquare()
    f.computeValue(a)
    p.addIndi(a)

g = GeneticAlgo(f, p)


for alpha in range(100):
    print("evolve {0}/{1}\r".format(alpha, 100), end="")
    g.evolve()
print("")

best = f.bestOverAll

print("")
imgTest = best.toMatrice()
printMatrix(imgTest, sizex, sizey)
