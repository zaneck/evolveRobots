# todo(damien): ajouter un shebang 
#############################################################################
# Contributors:
#	- created by Valentin Oczwarek
#############################################################################
from fitness import *
from indi import *
from imgTools import *

def fakeIndiCircle(x,y):
    a = Indi(16,16)

    circleMat = circle(16,16)

    for i in range(16):
        for j in range(16):
            if circleMat[i][j] == 1:
                a.draw.append((i,j,0))    
    return a
        
a = Indi(16, 16)
b = Indi(16, 16)

a.addRandomSquare()
a.addRandomSquare()

b.addRandomSquare()
b.addRandomSquare()
b.addRandomSquare()

print(a.__dict__)
print(b.__dict__)

c, d = a.crossOver(b)

print(c.__dict__)
print(d.__dict__)

mat = a.toMatrice()

f = FitnessCircle()

fakeOne = fakeIndiCircle(16,16)

mat = fakeOne.toMatrice()

printMatrix(mat, 16,16)

value = f.computeValue(fakeOne)
print(value)

assert value == 0
