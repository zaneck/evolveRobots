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

def absBinning(value):
        return abs(value[0])

def binaryBinning(value):
        if value[0] < 0:
                return 1
        return 0

class TestFitnessFake(unittest.TestCase):
    def setUp(self):
        pass
 
    def test_basic(self):
        print("\nSymmetric shape along X axis")
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        fitness = FitnessFake("A fake fitness", canvas)
        
        candidate = Indi()
        candidate.addShape(Rectangle(0.2,0.3,0.1,0.2))       
        candidate.addShape(Circle(0.2,-0.2,0.2))  
        printMatrix( fitness.toMatrice(candidate) )

    def test_rectangle(self):
        print("Testing Rectangle")
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        
        union = Union()
        union.addShape(Rectangle(0.5,0.5,0.25,0.25))
        
        candidate = Indi(withSymmetry=False)
        candidate.addShape(union)      
        printMatrix( canvas.toMatrice(candidate, binaryBinning) )
        matriceToGrayImage(canvas.toMatrice(candidate,absBinning), "rectangleTest.png")
        
    def test_substract(self):
        print("Testing Substraction Shape Operator")
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        
        difference = Difference()
        difference.addShape(Rectangle(0.25,0.25,0.25,0.25))
        difference.addShape(Circle(-0.1,0.0,0.10))
        difference.addShape(Circle(0.1,0.0,0.10))
        
        candidate = Indi(withSymmetry=False)
        candidate.addShape(difference)      
        printMatrix( canvas.toMatrice(candidate, binaryBinning) )
        matriceToGrayImage(canvas.toMatrice(candidate,absBinning), "rectangleTest.png")
        
    def test_repeat(self):
        print("Testing Repeat Shape Operator (FIXME: the behavior is not what I expect.")
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))

        #repeater = Repeat(Rectangle(0.0,0.0, 0.1, 0.1), Vec2(0.1,0.1))
        repeater = Repeat(Circle(0.0,0.0,0.05), Vec2(0.13,0.13))
        
        candidate = Indi(withSymmetry=False)
        candidate.addShape(repeater)      
        printMatrix( canvas.toMatrice(candidate, binaryBinning) )
        matriceToGrayImage(canvas.toMatrice(candidate,absBinning), "repeatTest.png")    
        assertEqual(True, False)

    def test_microstructure(self):
        print("Testing MicroStructure Shape Operator (FIXME: the behavior is not what I expect.")
        canvas = Canvas(dim=(1.0,1.0), res=(128,128))

        #repeater = Repeat(Rectangle(0.0,0.0, 0.1, 0.1), Vec2(0.1,0.1))
        repeater = MicroStructure(Circle(0.0,0.0,0.5))
        
        candidate = Indi(withSymmetry=False)
        candidate.addShape(repeater)      
        printMatrix( canvas.toMatrice(candidate, binaryBinning) )
        matriceToGrayImage(canvas.toMatrice(candidate,absBinning), "microStructureTest.png")    
        assertEqual(True, False)

       
    def test_inverse(self):
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        fitness = FitnessFake("A fake fitness", canvas)
        
        union = Union()
        union.addShape(Rectangle(0.2,0.3,0.1,0.2))
        union.addShape(Circle(0.2,-0.2,0.2))  

        print("\nUnion of two shapes")        
        candidate = Indi(withSymmetry=False)
        candidate.addShape(union)      
        printMatrix( fitness.toMatrice(candidate) )

        print("\nInverse of the Union of two shapes")        
        candidate = Indi(withSymmetry=False)
        candidate.addShape(Inverse(union))    
        printMatrix( fitness.toMatrice(candidate) )

    def test_offset(self):
        """Offset a shape along its normal"""
        canvas = Canvas(dim=(1.0,1.0), res=(32,32))
        fitness = FitnessFake("A fake fitness", canvas)
        
        union = Union()
        union.addShape(Rectangle(0.2,0.3,0.1,0.2))
        union.addShape(Circle(0.2,-0.2,0.2))  
      
        print("\nOffset of the Union of two shapes")        
        candidate = Indi(withSymmetry=False)
        candidate.addShape(Offset(union, offset=+0.1))    
        printMatrix( fitness.toMatrice(candidate) )
        
        
if __name__ == '__main__':
    unittest.main()

