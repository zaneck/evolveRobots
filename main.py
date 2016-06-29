#!/usr/bin/python3 -O
#############################################################################
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
import sys
import argparse

from config import Config
from indi import *
from genetic import *
from fitness import *

parser = argparse.ArgumentParser(description='try to create a shape by genetic algorithm')
parser.add_argument('metric', metavar='M', type=int, nargs='+',
                                       help='the metric to use [0..4]')

parser.add_argument('shape', metavar='S', type=int, nargs='+',
                                       help='the shape to match [0..4]')

args = parser.parse_args()

sizex, sizey = 16, 16

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


shape = args.shape[0]
shapeName = imageDict[shape][0]
shapeMatrix = imageDict[shape][1]

metric = args.metric[0]

f = FitnessImage(shapeName, shapeMatrix, metric, sizex, sizey)

p = Population()

for _ in range(Config.evolveFirstGen):
    a = Indi(sizex, sizey)
    a.addRandomSquare()
    f.computeValue(a)
    p.addIndi(a)

g = GeneticAlgo(f, p)


for alpha in range(Config.evolveNbCycle):
    print("evolve {0}/{1}\r".format(alpha, Config.evolveNbCycle), end="")
    g.evolve()
print("")

best = f.bestOverAll

print("")
imgTest = best.toMatrice()
printMatrix(imgTest, sizex, sizey)
