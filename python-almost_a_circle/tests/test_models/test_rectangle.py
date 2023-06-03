#!/usr/bin/python3


import unittest
import sys
from io import StringIO
from models.rectangle import Rectangle
"""Test for the Rectangle class"""


class TestRectangle(unittest.TestCase):
    """initialize tests"""

    def test_width(self):
        """test the width of the rectangle"""
    r = Rectangle(10, 20)
    self.assertEqual(r.width, 10)

    def test_height(self):
        """test the height of the rectangle"""
    r = Rectangle(10, 20)
    self.assertEqual(r.height, 20)

    def test_area(self):
        """test for the rectangle area"""
    r = Rectangle(10, 20)
    self.assertEqual(r.area, 200)

    def test_display(self):
        r = Rectangle(4, 6)
        captureOutput = StringIO()
        sys.stdout = sys.__stdout__
        expected_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(captureOutput.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
