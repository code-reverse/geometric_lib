import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):       
    def test_rectangle_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_rectangle_area_zero(self):
        with self.assertRaises(ValueError):
            area(10, 0)

    def test_rectangle_area_invalid_type(self):
        with self.assertRaises(ValueError):
            area("1", 1)

    def test_rectangle_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_rectangle_perimeter_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0, 10)

    def test_rectangle_perimeter_invalid_type(self):
        with self.assertRaises(ValueError):
            perimeter("1", 1)