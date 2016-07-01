#!/bin/python -O
#############################################################################
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
import sys
import argparse


from config import Config
from indi import *
from genetic import *
from sofaBaseFitness import *

parser = argparse.ArgumentParser(description='try to create a softRobot by genetic algorithm')

#toDo(valentin) add scene and mintopo var

args = parser.parse_args()

sizex, sizey = Config.generalX, Config.generalY

f = FitnessSofa("sofa")

p = Population()

for alpha in range(Config.evolveFirstGen):
    print("init {0}/{1}\r".format(alpha+1, Config.evolveFirstGen), end="")
    a = Indi(sizex, sizey)
    a.addRandomSquare()
    f.computeValue(a)
    p.addIndi(a)

g = GeneticAlgo(f, p)

print("")

for alpha in range(Config.evolveNbCycle):
    print("evolve {0}/{1}\r".format(alpha+1, Config.evolveNbCycle), end="")
    g.evolve()
print("")

best = f.bestOverAll

print("")
imgTest = best.toMatrice()
printMatrix(imgTest, sizex, sizey)
