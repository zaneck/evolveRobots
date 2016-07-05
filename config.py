class Config(object):
    #general
    generalX, generalY = 10, 10 #size of the grid
    nbThread = 8 #number of thread use during the evolving cycle
    
    #Indi
    indiSizeMax = 1024 #maximum size of x, y, where x * y is the size of the grid
    indiSquareMaxSize = 1 #maximum distance between the center of a square and his side
    
    #Population
    PopulationPopMax = 100

    #Genetic Algo
    geneticBest = 10 #number of champions which survive to the new generation 
    genticNbAugmentation = 100
    genticAddRate = 0.25
    genticCrossRate = 0.50
    genticCleanRate = 0.25
    
    #evolve
    evolveFirstGen = 100
    evolveNbCycle = 20
    
