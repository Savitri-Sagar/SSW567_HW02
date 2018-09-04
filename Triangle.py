# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

# This file was created by me to be able to run the Test file for HW02a.

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return "InvalidInput"
     
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput';
    
    # This information was not in the requirements spec but is important for correctness
    # The sum of any two sides must be greater than the third side
    if ((a+b) < c) or ((a+c) < b) or ((c+b) < a):
        return 'NotATriangle'
    
    # now we know that we have a valid triangle
    # Add this to ensure we can use the Pythag Theorem to check for right Triangles
    orig_a = a
    orig_b = b
    orig_c = c
    sides_list = [orig_a, orig_b, orig_c]
    c = max(orig_a, orig_b, orig_c)
    sides_list.remove(c)
    a = sides_list[0]
    b = sides_list[1]
    if a == b and b == c:
        return 'Equilateral'
    elif (((a ** 2) + (b ** 2)) == (c ** 2)) and ((a!=b) and (b!=c) and (a!=c)):
        return 'Scalene Right'
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'