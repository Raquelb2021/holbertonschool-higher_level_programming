#!/usr/bin/python3


import unittest
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


if __name__ == '__main__':
    unittest.main()
