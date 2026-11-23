import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        rez = area(10, 10)
        self.assertEqual(rez, 50)

    def test_triangle_area_zero(self):
        with self.assertRaises(ValueError):
            area(0, 0)

    def test_triangle_area_invalid_type(self):
        with self.assertRaises(ValueError):
            area("10", "10")

    def test_triangle_perimeter(self):
        rez = perimeter(10, 10, 10)
        self.assertEqual(rez, 30)

    def test_triangle_perimeter_zero(self):
        with self.assertRaises(ValueError):
            perimeter(0,0,10)

    def test_triangle_perimeter_invalid(self):
        with self.assertRaises(ValueError):
            perimeter(1,1,10)

    def test_triangle_perimeter_invalid_equals(self):
        with self.assertRaises(ValueError):
            perimeter(5,5,10)
            
    def test_triangle_perimeter_invalid_type(self):
        with self.assertRaises(ValueError):
            perimeter("10", 10, 10)
        