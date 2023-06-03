#!/usr/bin/python3

import unittest
from models.base import Base
"""Test for the Base class"""


class TestBase(unittest.TestCase):
    """initialize tests"""

    def test_no_id(self):
        """Testing with no id"""
        b = Base()
        self.assertEqual(Base._Base__nb_objects, 1)

    def test_with_id(self):
        """testing with id value"""
        b = Base(100)
        self.assertEqual(b.id, 100)
        self.assertEqual(Base._Base__nb_objects, 1)


if __name__ == '__main__':
    unittest.main()
