import sys

from indi import *
from genetic import *
from fitness import *

x, y = 64, 64

p = Population()

fitness = {
    "1":FitnessCircle,
    "2":FitnessSquare,
    "3":FitnessCross,
    "4":FitnessFourSquare,
}


f = fitness[sys.argv[1]]()

for _ in range(100):
    a = Indi(x,y)
    a.addRandomSquare()
    f.computeValue(a)
    p.addIndi(a)

print(p.numberOfIndi)

g = GeneticAlgo(f, p)

print(g.__dict__)

for alpha in range(100):
    print("evolve {0}".format(alpha))
    g.evolve()


best = f.bestOverAll

print("")
imgTest = best.toMatrice()
printMatrix(imgTest, x, y)
