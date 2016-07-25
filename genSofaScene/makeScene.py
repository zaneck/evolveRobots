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
import sofaObjectUsable
import sofaObject
import os 
from organisor import *

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
                os.rmdir(args.dest)
        else:
                print(
"""The directory {0} already exists. 
Please remove it before to use this software or use the --force option for their automatic removal.""".format(args.dest))
                sys.exit(-1)
                
if not os.path.exists(args.dest):
        os.mkdir(args.dest)

f = open(args.source.name)

res = json.load(f)
f.close()

orga = Organisor()

for k in res.keys():
    cls = getattr(sofaObjectUsable, k)

    if cls.unique == False:
        for context in res[k]:
            a = cls(context)
            orga.addToStock(a)
    else:
        a=cls(res[k])
        orga.addToStock(a)

pyscn = printPyscnFile(orga, args.dest)
minTopo = printMintopoFile(orga, args.dest)

pyscn.printFile()
minTopo.printFile()
 
