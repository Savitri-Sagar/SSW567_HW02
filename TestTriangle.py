# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

# This file was created by me to be able to run the Test file for HW02a.

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testIsoscelesRightTriangleA(self):
        """Isosceles Right. Test all integer inputs in a, b, c order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(1, 1, 2**0.5),'Isosceles Right','1, 1, 2**0.5 is an Isosceles Right triangle')
    def testIsoscelesRightTriangleB(self):
        """Isosceles Right. Test all integer inputs in a, c, b order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(1, 2**0.5, 1),'Isosceles Right','1, 2**0.5, 1 is an Isosceles Right triangle')
    def testIsoscelesRightTriangleC(self):
        """Isosceles Right. Test all integer inputs in c, a, b (also c, b, a) order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(2**0.5, 1, 1),'Isosceles Right','2**0.5, 1, 1 is an Isosceles Right triangle')


    def testScaleneRightTriangleA(self): 
        """Scalene Right. Test all integer inputs in a, b, c order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(3, 4, 5),'Scalene Right','3, 4, 5 is a Scalene Right triangle')
    def testScaleneRightTriangleB(self):
        """Scalene Right. Test all integer inputs in a, c, b order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(3, 5, 4),'Scalene Right','3, 5, 4 is a Scalene Right triangle')
    def testScaleneRightTriangleC(self):
        """Scalene Right. Test all integer inputs in b, a, c order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(4, 3, 5),'Scalene Right','4, 3, 5 is a Scalene Right triangle')
    def testScaleneRightTriangleD(self):
        """Scalene Right. Test all integer inputs in b, c, a order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(4, 5, 3),'Scalene Right','4, 5, 3 is a Scalene Right triangle')
    def testScaleneRightTriangleE(self):
        """Scalene Right. Test all integer inputs in c, a, b order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(5, 3, 4),'Scalene Right','5, 3, 4 is a Scalene Right triangle')
    def testScaleneRightTriangleF(self):
        """Scalene Right. Test all integer inputs in c, b, a order where a and b are legs and c is the hypotensue."""
        self.assertEqual(classifyTriangle(5, 4, 3),'Scalene Right','5, 4, 3 is a Scalene Right triangle')
        
        
    def testEquilateralTriangleA(self): 
        """Equilateral. Test all integer inputs."""
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
        
    # Test triangles that can only be classified as isosceles.
    def testIsoscelesTriangleA(self):
        """Strictly isosceles. Test side order A"""
        self.assertEqual(classifyTriangle(10, 10, 25), 'Isosceles', '10, 10, 25 should be an Isosceles triangle')
    def testIsoscelesTriangleB(self): #new
        """Strictly isosceles. Test side order B."""
        self.assertEqual(classifyTriangle(10, 25, 10), 'Isosceles', '10, 25, 10 should be an Isosceles triangle')
    def testIsoscelesTriangleC(self): #new
        """Strictly isosceles. Test side order C."""
        self.assertEqual(classifyTriangle(25, 10, 10), 'Isosceles', '25, 10, 10 should be an Isosceles triangle')
        
        
    def testScaleneTriangleA(self):
        """Strictly scalene. Test side order A."""
        self.assertEqual(classifyTriangle(89, 112, 114),'Scalene', '89, 112, 114 should be a Scalene triangle')
    def testScaleneTriangleB(self):
        """Strictly scalene. Test side order B."""
        self.assertEqual(classifyTriangle(89, 114, 112),'Scalene', '89, 114, 112 should be a Scalene triangle')
    def testScaleneTriangleC(self):
        """Strictly scalene. Test side order C."""
        self.assertEqual(classifyTriangle(112, 89, 114),'Scalene', '112, 89, 114 should be a Scalene triangle')
    def testScaleneTriangleD(self):
        """Strictly scalene. Test side order D."""
        self.assertEqual(classifyTriangle(112, 114, 89),'Scalene', '112, 114, 89 should be a Scalene triangle')
    def testScaleneTriangleE(self):
        """Strictly scalene. Test side order E."""
        self.assertEqual(classifyTriangle(114, 89, 112),'Scalene', '114, 89, 112 should be a Scalene triangle')
    def testScaleneTriangleF(self):
        """Strictly scalene. Test side order F."""
        self.assertEqual(classifyTriangle(114, 112, 89),'Scalene', '114, 112, 89 should be a Scalene triangle')
        
        
    def testBadTriangleA(self):
        """Test inputs that do not satisfy the Triangle Inequality Theorem. Test side order A."""
        self.assertEqual(classifyTriangle(1, 2, 5), "NotATriangle", "1, 2, 5 side lengths cannot form a triangle")
    def testBadTriangleB(self):
        """Test inputs that do not satisfy the Triangle Inequality Theorem. Test side order B."""
        self.assertEqual(classifyTriangle(1, 5, 2), "NotATriangle", "1, 5, 2 side lengths cannot form a triangle")
    def testBadTriangleC(self):
        """Test inputs that do not satisfy the Triangle Inequality Theorem. Test side order C."""
        self.assertEqual(classifyTriangle(2, 1, 5), "NotATriangle", "2, 1, 5 side lengths cannot form a triangle")
    def testBadTriangleD(self):
        """Test inputs that do not satisfy the Triangle Inequality Theorem. Test side order D."""
        self.assertEqual(classifyTriangle(2, 5, 1), "NotATriangle", "2, 5, 1 side lengths cannot form a triangle")
    def testBadTriangleE(self):
        """Test inputs that do not satisfy the Triangle Inequality Theorem. Test side order E."""
        self.assertEqual(classifyTriangle(5, 1, 2), "NotATriangle", "5, 1, 2 side lengths cannot form a triangle")
    def testBadTriangleF(self):
        """Test inputs that do not satisfy the Triangle Inequality Theorem. Test side order F."""
        self.assertEqual(classifyTriangle(5, 2, 1), "NotATriangle", "5, 2, 1 side lengths cannot form a triangle")
        
        
    def testInvalInputA(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. One invalid input > 200."""
        self.assertEqual(classifyTriangle(201, 100, 120), "InvalidInput", "201 is an invalid input")
    def testInvalInputB(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. Two invalid inputs > 200."""
        # 'InvalidInput' is the expected output of the below test because the input check comes before the triangle validity check
        self.assertEqual(classifyTriangle(205, 300, 100), "InvalidInput", "204.98 and 300 are invalid inputs")
    def testInvalInputC(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. Three invalid inputs > 200."""
        self.assertEqual(classifyTriangle(201, 204, 400), "InvalidInput", "201, 204, and 400 are invalid inputs")
    def testInvalInputD(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. One invalid input <= 0."""
        self.assertEqual(classifyTriangle(0, 4, 5), "InvalidInput", "0 is an invalid input")
    def testInvalInputE(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. Two invalid inputs <= 0."""
        self.assertEqual(classifyTriangle(-10, -7, 10), "InvalidInput", "-10 and -7 are invalid inputs")
    def testInvalInputF(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. Three invalid inputs <= 0."""
        self.assertEqual(classifyTriangle(0, -100, -50), "InvalidInput", "0, -100, and -50 are invalid inputs")
    def testInvalInputG(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. Combination of invalid inputs > 200 and <= 0."""
        self.assertEqual(classifyTriangle(-12, 400, 0), "InvalidInput", "-12, 400, and 0 are invalid inputs")
    def testInvalInputH(self):
        """Test inputs that do not satisfy the bounds placed on the inputs. Combination of invalid inputs > 200 and <= 0 and one valid input."""
        self.assertEqual(classifyTriangle(-4, 17, 201), "InvalidInput", "-4 and 201 are invalid inputs")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()