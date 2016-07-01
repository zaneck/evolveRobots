class Config(object):
    #general
    generalX, generalY = 16, 16 #size of the grid

    #Indi

    #todo(valentin): il faut expliquer c'est quoi ? est ce que size == le nombre ?  
    indiSizeMax = 1024

    #todo(valentin): je ne comprend pas ce que c'est
    indiSquareMaxSize = 1#int(max(generalX, generalX) / 5)
    
    #Population
    PopulationPopMax = 100

    #Genetic Algo
    #todo(valentin): ici expliquer c'est quoi ce param. 
    geneticBest = 10

    #todo(valentin): french vs english.  
    genticNbAugmentation = 100
    genticRatioAdd = 0.10
    genticRatioCross = 0.80
    genticRatioClean = 0.10
    

    #evolve
    evolveFirstGen = 100
    evolveNbCycle = 50
    
