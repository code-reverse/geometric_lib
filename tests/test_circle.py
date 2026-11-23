import unittest
from circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        rez = area(10)
        self.assertEqual(rez, 100*math.pi)

    def test_circle_area_zero(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_circle_area_invalid_type(self):
        with self.assertRaises(ValueError):
            area("10")

    def test_circle_perimeter(self):
        rez = perimeter(10)
        self.assertEqual(rez, 20*math.pi)

    def test_circle_perimeter_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_circle_perimeter_invalid_type(self):
        with self.assertRaises(ValueError):
            perimeter("10")
