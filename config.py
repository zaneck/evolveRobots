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
class Config(object):
    #general
    generalX, generalY = 20, 20 #size of the grid
    nbThread = 1 #number of thread use during the evolving cycle
    
    #Indi
    indiSizeMax = 1024 #maximum size of x, y, where x * y is the size of the grid
    indiSquareMaxSize = 4 #maximum distance between the center of a square and his side
    
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
