#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
"""test for the jrectangle class"""


class testRectangle(unittest.TestCase):

    def setUp(self):
        print("SetUp")
        Base._Base__nb_objects = 0

    def tearDown(self):
        print("tearDown")
        del self.rectangle
