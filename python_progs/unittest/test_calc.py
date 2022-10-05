#!/usr/bin/python3
import unittest
from calc import Calc


class TestCalc(unittest.TestCase):

    a = Calc(99, 6)
    b = Calc(-1, 1)
    c = Calc(-1, -2)

    def test_add(self):
        self.assertEqual(TestCalc.a.add(), 105)
        self.assertEqual(TestCalc.b.add(), 0)
        self.assertEqual(TestCalc.c.add(), -3)

    def test_sub(self):
        self.assertEqual(TestCalc.a.sub(), 93)
        self.assertEqual(TestCalc.b.sub(), -2)
        self.assertEqual(TestCalc.c.sub(), 1)

    def test_div(self):
        self.assertEqual(TestCalc.a.div(), 16.5)
        self.assertEqual(TestCalc.b.div(), -1)
        self.assertEqual(TestCalc.c.div(), 0.5)

    def test_mul(self):
        self.assertEqual(TestCalc.a.mul(), 594)
        self.assertEqual(TestCalc.b.mul(), -1)
        self.assertEqual(TestCalc.c.mul(), 2)


if __name__ == '__main__':
    unittest.main()
