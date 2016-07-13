#!/usr/bin/python3 -O
#############################################################################
#
# This application brute force all possible soft-robot and return the best one.
#
# Contributors:
#	- created by Valentin Owczarek
#############################################################################
#import sys
import argparse

from indiBrutus import *

from sofaBaseFitness import *
from config import Config

parser = argparse.ArgumentParser(description='Brute force way')

parser.add_argument('--config', metavar='file', 
                     default='config.json', type=argparse.FileType('r'),
                     help='file to process (defaults to config.json)')

args = parser.parse_args()
Config.load(args.config.name)

sizex, sizey = Config.generalX, Config.generalY

f = FitnessSofa("sofa", x=sizex, y=sizey)

indiToTest=[]

for _ in range(int(math.pow(2,18))):
    a = IndiBrutus(sizex, sizey)
    indiToTest.append(a)
    
f.computeValues(indiToTest)

print(f.bestOverAll.idIndi)

#fitness
