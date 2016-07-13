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
        print("\nSymmetric shape along X axis")
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        fitness = FitnessFake("A fake fitness", canvas)
        
        candidate = Indi(32, 32)
        candidate.addShape(Rectangle(0.2,0.3,0.1,0.2))       
        candidate.addShape(Circle(0.2,-0.2,0.2))  
        printMatrix( fitness.toMatrice(candidate) )

    def test_inverse(self):
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        fitness = FitnessFake("A fake fitness", canvas)
        
        union = Union()
        union.addShape(Rectangle(0.2,0.3,0.1,0.2))
        union.addShape(Circle(0.2,-0.2,0.2))  

        print("\nUnion of two shapes")        
        candidate = Indi(32, 32, withSymmetry=False)
        candidate.addShape(union)      
        printMatrix( fitness.toMatrice(candidate) )

        print("\nInverse of the Union of two shapes")        
        candidate = Indi(32, 32, withSymmetry=False)
        candidate.addShape(Inverse(union))    
        printMatrix( fitness.toMatrice(candidate) )

    def test_offset(self):
        """The Offset if not working for rectangles shapes FIXME"""
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        fitness = FitnessFake("A fake fitness", canvas)
        
        union = Union()
        union.addShape(Rectangle(0.2,0.3,0.1,0.2))
        union.addShape(Circle(0.2,-0.2,0.2))  
      
        print("\nOffset of the Union of two shapes")        
        candidate = Indi(32, 32, withSymmetry=False)
        candidate.addShape(Offset(union, offset=+0.1))    
        printMatrix( fitness.toMatrice(candidate) )
        self.assertEqual(1, 0)

        
if __name__ == '__main__':
    unittest.main()

