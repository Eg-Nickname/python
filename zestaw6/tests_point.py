import unittest
import math
from point import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(0, 0)
        self.p2 = Point(1, 2)
        self.p3 = Point(3, 4)
        self.p4 = Point(-1, -2)
        self.p5 = Point(1, 0)
        self.p6 = Point(0, 1)

    def test_str(self):
        self.assertEqual(str(self.p1), "(0, 0)")
        self.assertEqual(str(self.p2), "(1, 2)")
        self.assertEqual(str(self.p3), "(3, 4)")
        self.assertEqual(str(self.p4), "(-1, -2)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(0, 0)")
        self.assertEqual(repr(self.p2), "Point(1, 2)")
        self.assertEqual(repr(self.p3), "Point(3, 4)")

    def test_eq(self):
        self.assertTrue(self.p1 == Point(0, 0))
        self.assertTrue(self.p2 == Point(1, 2))
        self.assertFalse(self.p2 == Point(1, 3))
        self.assertFalse(self.p2 == Point(2, 2))

    def test_ne(self):
        self.assertTrue(Point(1, 2) != Point(1, 3))
        self.assertFalse(Point(1, 2) != Point(1, 2))

    def test_add(self):
        self.assertEqual(self.p2 + self.p3, Point(4, 6))
        self.assertEqual(self.p2 + self.p4, Point(0, 0))
        self.assertEqual(self.p1 + self.p2, self.p2)

    def test_sub(self):
        self.assertEqual(self.p3 - self.p2, Point(2, 2))
        self.assertEqual(self.p2 - self.p2, Point(0, 0))
        self.assertEqual(self.p2 - self.p1, self.p2)

    def test_mul(self):
        self.assertEqual(self.p2 * self.p3, 11)
        self.assertEqual(self.p5 * self.p6, 0)
        self.assertEqual(self.p2 * self.p4, -5)
        self.assertEqual(self.p1 * self.p2, 0)

    def test_cross(self):
        self.assertEqual(self.p2.cross(self.p3), -2)
        self.assertEqual(self.p5.cross(self.p6), 1)
        self.assertEqual(self.p2.cross(self.p2), 0)

    def test_length(self):
        self.assertEqual(self.p1.length(), 0)
        self.assertEqual(self.p5.length(), 1)
        self.assertEqual(self.p6.length(), 1)
        self.assertAlmostEqual(self.p3.length(), 5.0)
        self.assertAlmostEqual(self.p2.length(), math.sqrt(5))

    def test_hash(self):
        self.assertEqual(hash(Point(1, 2)), hash(Point(1, 2)))
        s = {Point(1, 2), Point(1, 2), Point(3, 4)}
        self.assertEqual(len(s), 2)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
