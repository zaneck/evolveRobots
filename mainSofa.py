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
import dump

from config import Config
from indi import *
from genetic import *
from sofaBaseFitness import *
from fakeFitness import *
from history import History

parser = argparse.ArgumentParser(description="""
This application creates soft-robot designs that match a given specification. To generates the designs a genetic algorithm
is implemented. To change the parameters of the genetic algorithm you need to edit the config file [config.json]
""")

parser.add_argument('--config', metavar='file', 
                     default='config.json', type=argparse.FileType('r'),
                     help='file to process (defaults to config.json)')

#toDo(valentin) add scene and mintopo var
args = parser.parse_args()

Config.load(args.config.name)

######################## Read the configuration file an initialize the algorithm ###########################
sizex, sizey = Config.generalX, Config.generalY

if Config.fitnessFunction == "fake":
        f = FitnessFake("fake", x=sizex, y=sizey) #FitnessSofa("sofa", x=sizex, y=sizey)
else:
        f = FitnessSofa("sofa", x=sizex, y=sizey) 
p = Population()
historyLog = History() 

#### Randomly creates an initial population composed of 'Config.evolveFirstGen' candidates. 
firstIndi = []
for alpha in range(Config.evolveFirstGen):
    print("init {0}/{1}\r".format(alpha+1, Config.evolveFirstGen), end="")
    a = Indi(sizex, sizey)
    a.addRandomSquare()
    if historyLog:
        historyLog.addEvent(a, ["N", None, None], 0)
    firstIndi.append(a)
    
f.computeValues(firstIndi)

for a in firstIndi:
    p.addIndi(a)

if dump.activated():
        dump.newExperiment("log", f, p, Config.evolveNbCycle) 

#### Create the algorithm and do the iterations 
g = GeneticAlgo(f, p)
print("")
for alpha in range(Config.evolveNbCycle):
    print("evolve {0}/{1}\r".format(alpha+1, Config.evolveNbCycle), end="")
    g.evolve(historyLog)
print("")

#### Dup the results.
best = f.bestOverAll

print("")
imgTest = best.toMatrice()
printMatrix(imgTest, sizex, sizey)

if dump.activated():
        #dump.saveHistories(candidates) 
        dump.endExperiment()
        historyLog.saveToCSV("log/history/history.csv")
        
