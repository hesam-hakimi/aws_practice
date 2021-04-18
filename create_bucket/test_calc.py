import unittest
import calendar
import time


class TestSample(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2+2, 4)
        self.assertEqual(5, 5)

    def test_add2(self):
        self.assertEqual(2+2, 4)
        self.assertEqual(5, 5)

    def test_add3(self):
        self.assertEqual(2+2, 4)
        self.assertEqual(6, 5)
