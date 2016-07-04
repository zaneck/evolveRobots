class Config(object):
    #general
    generalX, generalY = 10, 10 #size of the grid

    #Indi
    indiSizeMax = 1024 #maximum size of x, y, where x * y is the size of the canvas
    indiSquareMaxSize = 1 #maximum distance between the center of a square and his side
    
    #Population
    PopulationPopMax = 10

    #Genetic Algo
    geneticBest = 10 #number of champions which survive to the new generation 

    genticNbAugmentation = 10
    genticAddRate = 0.25
    genticCrossRate = 0.50
    genticCleanRate = 0.25
    

    #evolve
    evolveFirstGen = 10
    evolveNbCycle = 5
    
