import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        rez = area(10)
        self.assertEqual(rez, 100)

    def test_square_area_zero(self):
        with self.assertRaises(ValueError):
            area(0)

    def test_square_area_invalid_type(self):
        with self.assertRaises(ValueError):
            area("10")

    def test_square_perimetr(self):
        rez = perimeter(10)
        self.assertEqual(rez, 40)

    def test_square_perimeter_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_square_perimeter_invalid_type(self):
        with self.assertRaises(ValueError):
            perimeter("10")