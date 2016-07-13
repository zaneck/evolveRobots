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

def aTestFct(d):
        return "hello"
        
class TestFitnessFake(unittest.TestCase):
    def setUp(self):
        pass

    def test_basic_init(self):
        canvas = Canvas(dim=(-1.0,1.0), res=(32,32))
        
        self.assertEqual(hasattr(canvas, "dim"), True)
        self.assertEqual(hasattr(canvas, "res"), True)
        
        self.assertEqual(canvas.dim, (-1.0,1.0))
        self.assertEqual(canvas.res, (32,32))
        
          
    def test_invalid_init(self):
        with self.assertRaises(ValueError):
                canvas = Canvas(dim=(1.0,-1.0), res=(-32,32))

        with self.assertRaises(ValueError):
                canvas = Canvas(dim=(1.0,1.0), res=(-32,-32))
        
        with self.assertRaises(ValueError):
                canvas = Canvas(dim=(1.0,1.0), res=(32,1000000))

    def test_basic_print(self):
        canvas = Canvas(dim=(-1.0,1.0), res=(19,15))
        matrice = canvas.toMatrice(Indi(), aTestFct)
        
        self.assertEqual( len(matrice), 19 )
        self.assertEqual( len(matrice[0]), 15 )
        self.assertEqual( matrice[0][0], "hello" )
        
        
    def test_invalid_print(self):
        canvas = Canvas(dim=(-1.0,1.0), res=(32,32))
        
        with self.assertRaises(TypeError):
                canvas.toMatrice("damien", aTestFct)

        with self.assertRaises(TypeError):
                canvas.toMatrice(Indi(), "damien")
            
if __name__ == '__main__':
    unittest.main()

