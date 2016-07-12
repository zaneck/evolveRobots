#!/usr/bin/python3 -O
#############################################################################
# Contributors:
#	- created by damien.marchal@univ-lille1.fr
#############################################################################
import unittest

import sys

sys.path.insert(0,"..")

from fakeFitness import *
from indi import *
from imgTools import *

class TestFitnessFake(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_basic(self):
        canvas = Canvas(dim=(1.0,1.0), res=(16,16))
        fitness = FitnessFake("A fake fitness", canvas)
        
        candidate = Indi(16, 16)
        
        candidate.addShape(Rectangle(0.2,0.3,0.2,0.2))       
        printMatrix( fitness.toMatrice(candidate) )

        candidate.addShape(Circle(-0.2,-0.2,0.2))       
        printMatrix( fitness.toMatrice(candidate) )

    def test_basic(self):
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        fitness = FitnessFake("A fake fitness", canvas)
        
        candidate = Indi(32, 32)
        
        candidate.addShape(Rectangle(0.2,0.3,0.1,0.2))       
        printMatrix( fitness.toMatrice(candidate) )

        candidate.addShape(Circle(0.2,-0.2,0.2))  
        print("")     
        printMatrix( fitness.toMatrice(candidate) )

        
if __name__ == '__main__':
    unittest.main()

