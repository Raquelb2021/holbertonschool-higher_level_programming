#!/usr/bin/python3

import json
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        print("setUp")
        self.base = Base()
        Base._Base__nb_objects = 0

    def tearDown(self):
        print("tearDown")
        del self.base

    def test_id_auto_assignment(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

    def test_id_manual_assignment(self):
        base3 = Base(12)
        self.assertEqual(base3.id, 12)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_dict(self):
        json_str = (Base.to_json_string([{'id': 12}]))
        self.assertEqual(json_str, '[{"id": 12}]')

    def test_to_json_string_returns_string(self):
        json_str = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(json_str, str)

    def test_from_json_string_None(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
