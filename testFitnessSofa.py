from indi import *
from sofaBaseFitness import *

i = Indi(10,10)
i.addRandomSquare()
a = FitnessSofa("test")
a.simulate(i)
 
