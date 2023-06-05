import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_auto_assignment(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_manual_assignment(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

if __name__ == '__main__':
    unittest.main()

