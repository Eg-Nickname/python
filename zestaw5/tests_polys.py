import unittest
from polys import *

class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p1 = [0, 1]
        self.p2 = [0, 0, 1]
        self.p3 = [2, 1]
        self.p4 = [2, 1, 0]
        self.p5 = [-3, 0, 1]
        self.p6 = [3]
        self.p7 = [0]
        self.p8 = [0, 0, 0]

    def assert_normalized(self, poly):
        if len(poly) > 1:
            self.assertNotEqual(poly[-1], 0)

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly(self.p3, self.p5), [-1, 1, 1])
        self.assertEqual(add_poly(self.p4, self.p6), [5, 1])
        self.assertEqual(add_poly([1, 2], [-1, -2]), [0])
        self.assertEqual(add_poly(self.p7, self.p8), [0])
        self.assert_normalized(add_poly(self.p3, [-2, -1, 0, 0]))

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])
        self.assertEqual(sub_poly(self.p3, self.p3), [0])
        self.assertEqual(sub_poly(self.p4, self.p3), [0])
        self.assertEqual(sub_poly(self.p5, self.p6), [-6, 0, 1])
        self.assert_normalized(sub_poly([1, 2, 3], [0, 0, 3]))

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])
        self.assertEqual(mul_poly(self.p3, self.p3), [4, 4, 1])
        self.assertEqual(mul_poly(self.p3, self.p5), [-6, -3, 2, 1])
        self.assertEqual(mul_poly(self.p7, self.p3), [0])
        self.assertEqual(mul_poly(self.p6, self.p3), [6, 3])
        self.assert_normalized(mul_poly(self.p8, self.p5))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.p7))
        self.assertTrue(is_zero(self.p8))
        self.assertFalse(is_zero(self.p1))
        self.assertFalse(is_zero(self.p2))
        self.assertFalse(is_zero(self.p3))
        self.assertFalse(is_zero(self.p6))

    def test_eq_poly(self):
        self.assertTrue(eq_poly(self.p3, self.p3))
        self.assertTrue(eq_poly(self.p3, self.p4))
        self.assertTrue(eq_poly(self.p4, self.p3))
        self.assertTrue(eq_poly(self.p7, self.p8))
        self.assertFalse(eq_poly(self.p1, self.p2))
        self.assertFalse(eq_poly(self.p3, self.p5))
        self.assertFalse(eq_poly([2, 1], [2, 2]))

    def test_eval_poly(self):
        self.assertEqual(eval_poly(self.p1, 0), 0)
        self.assertEqual(eval_poly(self.p1, 5), 5)
        self.assertEqual(eval_poly(self.p2, 3), 9)
        self.assertEqual(eval_poly(self.p3, 3), 5)
        self.assertEqual(eval_poly(self.p5, 2), 1)
        self.assertEqual(eval_poly(self.p5, 0), -3)
        self.assertEqual(eval_poly(self.p6, 10), 3)
        self.assertEqual(eval_poly(self.p8, 4), 0)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p1, self.p2), [0, 0, 1])
        self.assertEqual(combine_poly(self.p2, self.p1), [0, 0, 1])
        self.assertEqual(combine_poly(self.p3, self.p2), [2, 0, 1])
        self.assertEqual(combine_poly(self.p2, self.p3), [4, 4, 1])
        self.assertEqual(combine_poly(self.p6, self.p1), [3])
        self.assertEqual(combine_poly(self.p3, self.p6), [5])
        self.assertEqual(combine_poly(self.p7, self.p3), [0])
        self.assertEqual(combine_poly(self.p3, self.p7), [2])
        self.assert_normalized(combine_poly(self.p7, self.p3))

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p1, 0), [1])
        self.assertEqual(pow_poly(self.p1, 1), [0, 1])
        self.assertEqual(pow_poly(self.p1, 2), [0, 0, 1])
        self.assertEqual(pow_poly(self.p1, 3), [0, 0, 0, 1])
        self.assertEqual(pow_poly(self.p3, 0), [1])
        self.assertEqual(pow_poly(self.p3, 2), [4, 4, 1])
        self.assertEqual(pow_poly(self.p5, 2), [9, 0, -6, 0, 1])
        self.assertEqual(pow_poly(self.p7, 3), [0])        
        with self.assertRaises(ValueError):
            pow_poly(self.p1, -1)
        self.assert_normalized(pow_poly(self.p8, 2))

    def test_diff_poly(self):
        self.assertEqual(diff_poly(self.p1), [1])
        self.assertEqual(diff_poly(self.p2), [0, 2])
        self.assertEqual(diff_poly(self.p3), [1])
        self.assertEqual(diff_poly(self.p4), [1])
        self.assertEqual(diff_poly(self.p5), [0, 2])
        self.assertEqual(diff_poly([4, 4, 1]), [4, 2])
        self.assertEqual(diff_poly(self.p6), [0])
        self.assertEqual(diff_poly(self.p7), [0])
        self.assertEqual(diff_poly(self.p8), [0])
        self.assert_normalized(diff_poly([1, 0, 0, 0]))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
