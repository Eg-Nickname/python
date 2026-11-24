import unittest
from polys import Poly


class TestPoly(unittest.TestCase):
    def setUp(self):
        self.p1 = Poly(1, 1)
        self.p2 = Poly(1, 2)
        self.p3 = Poly.from_list([2, 1])
        self.p4 = Poly.from_list([2, 1, 0])
        self.p5 = Poly.from_list([-3, 0, 1])
        self.p6 = Poly(3, 0)
        self.p8 = Poly.from_list([0, 0, 0])
        self.zero = Poly(0, 0)

    def assert_normalized(self, poly):
        if len(poly.a) > 1:
            self.assertNotEqual(poly.a[-1], 0)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Poly.from_list([0, 1, 1]))
        self.assertEqual(self.p3 + self.p5, Poly.from_list([-1, 1, 1]))
        self.assertEqual(self.p4 + self.p6, Poly.from_list([5, 1]))
        self.assertEqual(Poly.from_list([1, 2]) + Poly.from_list([-1, -2]), self.zero)
        self.assertEqual(self.zero + self.p8, self.zero)
        self.assert_normalized(self.p3 + Poly.from_list([-2, -1, 0, 0]))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Poly.from_list([0, 1, -1]))
        self.assertEqual(self.p2 - self.p1, Poly.from_list([0, -1, 1]))
        self.assertEqual(self.p3 - self.p3, self.zero)
        self.assertEqual(self.p4 - self.p3, self.zero)
        self.assertEqual(self.p5 - self.p6, Poly.from_list([-6, 0, 1]))
        self.assert_normalized(Poly.from_list([1, 2, 3]) - Poly.from_list([0, 0, 3]))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, Poly.from_list([0, 0, 0, 1]))
        self.assertEqual(self.p3 * self.p3, Poly.from_list([4, 4, 1]))
        self.assertEqual(self.p3 * self.p5, Poly.from_list([-6, -3, 2, 1]))
        self.assertEqual(self.zero * self.p3, self.zero)
        self.assertEqual(self.p6 * self.p3, Poly.from_list([6, 3]))
        self.assert_normalized(self.p8 * self.p5)

    def test_is_zero(self):
        self.assertTrue(self.zero.is_zero())
        self.assertTrue(self.p8.is_zero())
        self.assertFalse(self.p1.is_zero())
        self.assertFalse(self.p2.is_zero())
        self.assertFalse(self.p3.is_zero())
        self.assertFalse(self.p6.is_zero())

    def test_eq(self):
        self.assertTrue(self.p3 == self.p3)
        self.assertTrue(self.p3 == self.p4)
        self.assertTrue(self.p4 == self.p3)
        self.assertTrue(self.zero == self.p8)
        self.assertFalse(self.p1 == self.p2)
        self.assertFalse(self.p3 == self.p5)
        self.assertFalse(Poly.from_list([2, 1]) == Poly.from_list([2, 2]))

    def test_eval(self):
        self.assertEqual(self.p1.eval(0), 0)
        self.assertEqual(self.p1.eval(5), 5)
        self.assertEqual(self.p2.eval(3), 9)
        self.assertEqual(self.p3.eval(3), 5)
        self.assertEqual(self.p5.eval(2), 1)
        self.assertEqual(self.p5.eval(0), -3)
        self.assertEqual(self.p6.eval(10), 3)
        self.assertEqual(self.p8.eval(4), 0)

    def test_combine(self):
        self.assertEqual(self.p1.combine(self.p2), Poly(1, 2))
        self.assertEqual(self.p2.combine(self.p1), Poly(1, 2))
        self.assertEqual(self.p3.combine(self.p2), Poly.from_list([2, 0, 1]))
        self.assertEqual(self.p2.combine(self.p3), Poly.from_list([4, 4, 1]))
        self.assertEqual(self.p6.combine(self.p1), Poly(3, 0))
        self.assertEqual(self.p3.combine(self.p6), Poly(5, 0))
        self.assertEqual(self.zero.combine(self.p3), self.zero)
        self.assertEqual(self.p3.combine(self.zero), Poly(2, 0))
        self.assert_normalized(self.zero.combine(self.p3))

    def test_pow(self):
        self.assertEqual(self.p1 ** 0, Poly(1, 0))
        self.assertEqual(self.p1 ** 1, Poly.from_list([0, 1]))
        self.assertEqual(self.p1 ** 2, Poly.from_list([0, 0, 1]))
        self.assertEqual(self.p1 ** 3, Poly.from_list([0, 0, 0, 1]))
        self.assertEqual(self.p3 ** 0, Poly(1, 0))
        self.assertEqual(self.p3 ** 2, Poly.from_list([4, 4, 1]))
        self.assertEqual(self.p5 ** 2, Poly.from_list([9, 0, -6, 0, 1]))
        self.assertEqual(self.zero ** 3, self.zero)
        with self.assertRaises(ValueError):
            self.p1 ** -1
        self.assert_normalized(self.p8 ** 2)

    def test_diff(self):
        self.assertEqual(self.p1.diff(), Poly(1, 0))
        self.assertEqual(self.p2.diff(), Poly.from_list([0, 2]))
        self.assertEqual(self.p3.diff(), Poly(1, 0))
        self.assertEqual(self.p4.diff(), Poly(1, 0))
        self.assertEqual(self.p5.diff(), Poly.from_list([0, 2]))
        self.assertEqual(Poly.from_list([4, 4, 1]).diff(), Poly.from_list([4, 2]))
        self.assertEqual(self.p6.diff(), self.zero)
        self.assertEqual(self.zero.diff(),  self.zero)
        self.assertEqual(self.p8.diff(),  self.zero)
        self.assert_normalized(Poly(1, 3).diff())

    def test_pos_neg(self):
        self.assertEqual(+self.p3, self.p3)
        self.assertEqual(-self.p3, Poly.from_list([-2, -1]))
        self.assertEqual(self.p3 + (-self.p3), self.zero)

    def test_integrate(self):
        self.assertEqual(self.p1.integrate(), Poly.from_list([0, 0, 0.5]))
        self.assertEqual(self.p6.integrate(), Poly.from_list([0, 3]))
        self.assertEqual(self.zero.integrate(), self.zero)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
