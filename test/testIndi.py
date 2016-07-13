#!/usr/bin/python3 -O
#############################################################################
# Contributors:
#	- created by Valentin Oczwarek
#############################################################################
import unittest
import sys

sys.path.insert(0,"..")

from fitness import *
from indi import *
from imgTools import *


class TestIndie(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_basic_constructor_behavior(self):
        # Should work 
        a = Indi()
        
        # Should throw an exception        
        with self.assertRaises(TypeError):
                a = Indi()
                a = Indi("toto", 10)
                a = Indi(10, "tata")
       
    def test_basic_behavior(self):
        a = Indi()
        b = Indi()

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

    def test_atLeastOneSquareKO(self):
        a = Indi()
        res = a.removeRandomSquare()
        self.assertEqual(res, 0)

        a = Indi()
        a.addRandomSquare()
        res = a.removeRandomSquare()
        self.assertEqual(res, 0)
        
    def test_atLeastOneSquareOK(self):
        a = Indi()
        a.addRandomSquare()
        a.addRandomSquare()
        res = a.removeRandomSquare()
        self.assertEqual(res, 1)   
        
if __name__ == '__main__':
    unittest.main()

