"""this file contains unit test to test testing_functions.py"""

import unittest

from testing_functions import square, cube, addition
class TestTime(unittest.TestCase):
    """this class contain unit tests functions to test the imported functions"""
    def test_square(self):
        """this function tests the square() function"""
        self.assertEqual(square(5),25)

    def test_cube(self):
        """this function tests the cube() function"""
        self.assertEqual(cube(9),729)

    def test_addition(self):
        """this function tests the addition() function"""
        self.assertEqual(addition(9,9),18)
