#!/usr/bin/python3 -O
#############################################################################
#
# 
# 
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
        a = Indi(16, 16)

        # Should work 
        a = Indi(0, 0)
        
        # Should throw an exception        
        with self.assertRaises(TypeError):
                a = Indi(-1, -1)
                a = Indi("toto", 10)
                a = Indi(10, "tata")
        
        # Should throw an exception        
        with self.assertRaises(MemoryError):
               a = Indi(100000000, 1000000000) 
                
    def test_basic_behavior(self):
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

    def test_atLeastOneSquareKO(self):
        a = Indi(16, 16)
        res = a.removeRandomSquare()
        self.assertEqual(res, 0)

        a = Indi(16, 16)
        a.addRandomSquare()
        res = a.removeRandomSquare()
        self.assertEqual(res, 0)
        
    def test_atLeastOneSquareOK(self):
        a = Indi(16, 16)
        a.addRandomSquare()
        a.addRandomSquare()
        res = a.removeRandomSquare()
        self.assertEqual(res, 1)
   
        
if __name__ == '__main__':
    unittest.main()

