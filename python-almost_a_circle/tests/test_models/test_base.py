#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

if __name__ == '__main__':
    unittest.main()
