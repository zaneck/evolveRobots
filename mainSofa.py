#!/usr/bin/python3 -O
########################################################################################################
#
# This application creates soft-robot designs that match a given specification. 
# To generates the designs a genetic algorithm is implemented. You can change 
# the parameters of the genetic algorithm by editting the file [config.py].
#
# Contributors:
#	- created by Valentin Owczarek
########################################################################################################
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

args = parser.parse_args()

Config.load(args.config.name)

######################## Read the configuration file an initialize the algorithm ###########################
sizex, sizey = Config.generalX, Config.generalY

canvas = Canvas(dim=(1.0,1.0),res=(Config.generalX, Config.generalY))

if Config.fitnessFunction == "fake":
        f = FitnessFake("fake", canvas)
else:
        f = FitnessSofa("sofa", canvas)
        
p = Population()
historyLog = False#History() 


#### Randomly creates an initial population composed of 'Config.evolveFirstGen' candidates. 
firstIndi = []
for alpha in range(Config.evolveFirstGen):
#    print("init {0}/{1}\r".format(alpha+1, Config.evolveFirstGen), end="")
    a = Indi()
    a.addRandomSquare()
    firstIndi.append(a)

f.computeValues(firstIndi)
for a in firstIndi:
    p.addIndi(a)

    if historyLog:
        historyLog.addEvent(a, ["N", None, None], 0, a.fitness)


if dump.activated():
        dump.newExperiment("log", f, p, Config.evolveNbCycle) 


#### Create the algorithm and do the iterations 
g = GeneticAlgo(f, p)
#print("======== START =======")
for alpha in range(Config.evolveNbCycle):
    g.evolve()#historyLog)
#print("")


#### Dump the results.
best = f.bestOverAll

#print("======= RESULT =======")
imgTest = f.toMatrice(best)
#printMatrix(imgTest)

if dump.activated():
        dump.endExperiment()
        historyLog.saveToCSV("log/history/history.csv")
        

f.writeBestResult("BEST")
print(best.fitness)
