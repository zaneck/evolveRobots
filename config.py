# coding: utf8 
#############################################################################
#
# This file is part of evolveRobot. Use this file to configure the 
# behavior of the genetic algorithm. 
#
# Contributors:
#	- created by Valentin Owczarek
#       - damien.marchal@univ.lille1.fr
#############################################################################
import json
import inspect

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj


class Config(object):
    #general
    generalX, generalY = 20, 20 #size of the grid
    nbThread = 1 #number of thread use during the evolving cycle
    
    #Indi
    indiSizeMax = 1024 #maximum size of x, y, where x * y is the size of the grid
    indiSquareMaxSize = 0.2 #maximum distance between the center of a square and his side
    indiSquareMinSize = 0.1 #maximum distance between the center of a square and his side
    centerMinValue = -0.5
    centerMaxValue =  0.5
    
    #Population
    PopulationPopMax = 100

    #Genetic Algo
    geneticBest = 10 #number of champions which survive to the new generation 
    genticNbAugmentation = 100
    genticAddRate = 0.30
    genticCrossRate = 0.50
    genticCleanRate = 0.20
    
    #evolve
    evolveFirstGen = 100
    evolveNbCycle = 10
    
    #fitness
    # use this to select the fitness function between ["fake", "sofa"]
    fitnessFunction = "fake"   
    fitnessRateScore = 1
    fitnessRateVoxel = 0.1
    
    def save(filename):
        f = open(filename, "w+t")
        res = json.dump(Config, f, cls=ObjectEncoder, indent=2, sort_keys=True)
        f.close()
    
    def load(filename):
        fp = open(filename)
        res = json.load(fp)
        for entry in res:
                setattr(Config, entry, res[entry])
        fp.close()
