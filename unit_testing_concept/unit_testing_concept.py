"""this file contains unit test to test testing_functions.py"""

import unittest

from unit_testing_concept.testing_functions import square, cube, addition
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
        self.assertEqual(addition(2, 4), 6)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(2.3, 3.6), 5.9)
        self.assertEqual(addition("hello", "world"), "helloworld")
        self.assertEqual(addition(2.3000, 4.3000), 6.6)
        self.assertNotEqual(addition(-2, -2), 0)


if __name__ == '__main__':
    unittest.main()
