#!/usr/bin/python3 -O
#############################################################################
#
# This application creates soft-robot designs that match a given specification. 
# To generates the designs a genetic algorithm is implemented. You can change 
# the parameters of the genetic algorithm by editting the file [config.py].
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
import sys
import argparse

from config import Config
from indi import *
from genetic import *
from sofaBaseFitness import *

parser = argparse.ArgumentParser(description="""
This application creates soft-robot designs that match a given specification. To generates the designs a genetic algorithm
is implemented. To change the parameters of the genetic algorithm you need to edit the file [config.py]
""")

#toDo(valentin) add scene and mintopo var
args = parser.parse_args()

######################## Read the configuration file an initialize the algorithm ###########################
sizex, sizey = Config.generalX, Config.generalY

f = FitnessSofa("sofa", x=sizex, y=sizey)
p = Population()

#### Randomly creates an initial population composed of 'Config.evolveFirstGen' candidates. 
firstIndi = []
for alpha in range(Config.evolveFirstGen):
    print("init {0}/{1}\r".format(alpha+1, Config.evolveFirstGen), end="")
    a = Indi(sizex, sizey)
    a.addRandomSquare()
    firstIndi.append(a)
    
f.computeValues(firstIndi)

for a in firstIndi:
    p.addIndi(a)

#### Create the algorithm and do the iterations 
g = GeneticAlgo(f, p)
print("")
for alpha in range(Config.evolveNbCycle):
    print("evolve {0}/{1}\r".format(alpha+1, Config.evolveNbCycle), end="")
    g.evolve()
print("")

#### Dup the results.
best = f.bestOverAll

print("")
imgTest = best.toMatrice()
printMatrix(imgTest, sizex, sizey)
