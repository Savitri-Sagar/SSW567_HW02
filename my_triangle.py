# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

# This file was created by me to be able to run the Test file for HW02a.

def classify_triangle(side_a, side_b, side_c):
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
    side_too_big = side_a > 200 or side_b > 200 or side_c > 200
    side_too_small = side_a <= 0 or side_b <= 0 or side_c <= 0
    side_not_int = not(isinstance(side_a, int) and isinstance(side_b, int)\
                       and isinstance(side_c, int))
    if (side_too_big or side_too_small or side_not_int):
        return "InvalidInput"
#     if side_a <= 0 or side_b <= 0 or side_c <= 0:
#         return 'InvalidInput'
#     # verify that all 3 inputs are integers
#     # Python's "isinstance(object,type) returns True if the object is of the specified type
#     if not(isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)):
#         return 'InvalidInput'
    # This information was not in the requirements spec but is important for correctness
    # The sum of any two sides must be greater than the third side
    if ((side_a+side_b) < side_c) or ((side_a+side_c) < side_b) or ((side_c+side_b) < side_a):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    # Add this to ensure we can use the Pythag Theorem to check for right Triangles
    orig_a = side_a
    orig_b = side_b
    orig_c = side_c
    sides_list = [orig_a, orig_b, orig_c]
    side_c = max(orig_a, orig_b, orig_c)
    sides_list.remove(side_c)
    side_a = sides_list[0]
    side_b = sides_list[1]
    if side_a == side_b and side_b == side_c:
        return 'Equilateral'
    if (((side_a ** 2) + (side_b ** 2)) == (side_c ** 2)) and \
    ((side_a != side_b) and (side_b != side_c) and (side_a != side_c)):
        return 'Scalene Right'
    if (side_a != side_b) and  (side_b != side_c) and (side_a != side_c):
        return 'Scalene'
    return 'Isosceles'
# I pledge on my honor
# that I have not given or received
# any unauthorized assistance on this assignment/examination.
# I further pledge that I have not copied
# any material from a book, article, the Internet
# or any other source except where I have expressly cited the source.
# Kristen Tan
