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
        candidate.addSquare()
        printMatrix( fitness.toMatrice(candidate) )
        
if __name__ == '__main__':
    unittest.main()

