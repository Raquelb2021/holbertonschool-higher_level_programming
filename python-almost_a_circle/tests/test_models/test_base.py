#!/usr/bin/python3

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        print("setUp")
        Base._Base__nb_objects = 0

    def tearDown(self):
        print("tearDown")
        Base._Base__nb_objects = 0
        del self.Base

    def test_id_auto_assignment(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_manual_assignment(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string_none(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_dict(self):
        json_str = Base.to_json_string([{'id': 12}])
        self.assertEqual(json_str, '[{"id": 12}]')

if __name__ == '__main__':
    unittest.main()

