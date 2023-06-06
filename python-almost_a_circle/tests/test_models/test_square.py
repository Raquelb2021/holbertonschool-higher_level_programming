#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        print("setUp")
        Base._Base__nb_objects = 0

    def tearDown(self):
        print("tearDown")
        del self.square
