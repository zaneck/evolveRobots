class Config(object):
    #general
    generalX, generalY = 20, 20 #size of the grid
    nbThread = 6 #number of thread use during the evolving cycle
    
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
    evolveNbCycle = 30
    

    #fitness
    fitnessRateScore = 1
    fitnessRateVoxel = 0.1
