#!/usr/bin/python3 -O
########################################################################################################
#
# This application is generating a complete trial for the evolveRobots application from a simplified
# configuration file that provides a high level view of the experiment.   
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ-lille1.fr
########################################################################################################
import json
import sys
import argparse
import os 
import shutil 
import sofaObjectUsable
import sofaObject

from jsonParser import JsonParser

from bagOfObject import *
from printFile import *

parser = argparse.ArgumentParser(description="""This application creates an evolveRobots trials from a trial file. """)

parser.add_argument('--source', metavar='file', 
                     default='defaulttrial.json', type=argparse.FileType('r'),
                     help='file with the description of the trial to do (defaults to defaulttrials.json)')
parser.add_argument('--dest', metavar='file', 
                     default='Trial1', action='store',
                     help='output directory where the trial data files are generated (Trial1)')
parser.add_argument('--force', default=False, action='store_true',
                     help='automatically remove the output directory before to create a new trial.')
                     
args = parser.parse_args()

args.dest = os.path.abspath(args.dest)

if os.path.exists(args.dest):
        if args.force:
                shutil.rmtree(args.dest, ignore_errors=True)
        else:
                print(
"""The directory {0} already exists. 
Please remove it before to use this software or use the --force option for their automatic removal.""".format(args.dest))
                sys.exit(-1)
                
if not os.path.exists(args.dest):
        os.mkdir(args.dest)

parser = JsonParser(args.source.name) 
parser.checkValidJson()
bag=parser.genBagOfObject()


pyscn = printPyscnFile(bag, args.dest)
minTopo = printMintopoFile(bag, args.dest)

pyscn.printFile()
minTopo.printFile()
 
