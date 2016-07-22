import json
import sys

import sofaObjectUsable
import sofaObject
from organisor import *

f = open("test1.json")

res = json.load(f)
f.close()

orga = Organisor()

for a in res.keys():
    cls = getattr(sofaObjectUsable, a)

    if cls.unique == False:
        for context in res[a]:
            a = cls(context)
            orga.addToStock(a)
    else:
        a=cls(res[a])
        orga.addToStock(a)

pyscn = printPyscnFile(orga, ".")
minTopo = printMintopoFile(orga, ".")

pyscn.printFile()
minTopo.printFile()

# head = Head()
# canvas = Canvas(50,50,5,20,20,1)
# fem = FEM()
# partialConstraint = PartialFixedConstraint(0,0,1)
# fixedConstraint1 = FixedConstraint(0,0,0,2,1,1)
# fixedConstraint2 = FixedConstraint(18,0,0,20,1,1)
# constantForceField = ConstantForceField(10,19,0,11,20,1,0,-100,0)

# tail = Tail()

# print(head)

#print(canvas)

# print(fem)

# print(partialConstraint)
# print(fixedConstraint1)
# print(fixedConstraint2)
# print(constantForceField)

# print(tail)

# a=["x":50, "y":50, "z":5, "divX":20, "divY":20, "divZ":1]
# c1 = Canvas(a)
# print(c1)
 
