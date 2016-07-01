class Config(object):
    #general
    generalX, generalY = 16, 16 #size of the grid

    #indi
    indiSquareMaxSize = 1#int(max(generalX, generalX) / 5)
    
    
    #Indi
    indiSizeMax = 1024
    
    #Population
    PopulationPopMax = 100

    #Genetic Algo
    geneticBest = 10

    genticNbAugmentation = 100
    genticRatioAdd = 0.10
    genticRatioCross = 0.80
    genticRatioClean = 0.10
    

    #evolve
    evolveFirstGen = 100
    evolveNbCycle = 50
    
