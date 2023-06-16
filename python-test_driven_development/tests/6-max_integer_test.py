#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class for tests
    """

    def test_positive_list(self):
        """ Tests the function on a list of positives """
        self.assertEqual(max_integer([10, 5, 90, 45, 35]), 90)

    def test_negative_list(self):
        """ Tests the function on a list of negatives """
        self.assertEqual(max_integer([-22, -17, -15, -13, -6]), -6)

    def test_error(self):
        """ Tests the function on a error case """
        with self.assertRaises(TypeError):
            max_integer(['n', 8, 10])

    def test_none(self):
        """ Tests the function with None parameter """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty_list(self):
        """ Tests the function on a empty list case """
        self.assertEqual(max_integer([]), None)

    def test_unique_int(self):
        """ Tests the function on a list with a single value """
        self.assertEqual(max_integer([51]), 51)


if __name__ == "__main__":
    unittest.main()
