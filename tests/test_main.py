import unittest

from src.main import Lisp


class TestLisp(unittest.TestCase):

    def test_flat(self):
        self.assertEqual(Lisp.parse("(+ 1 2)"), 3)
        self.assertEqual(Lisp.parse("(- 10 4)"), 6)
        self.assertEqual(Lisp.parse("(+ 0 0)"), 0)
        self.assertEqual(Lisp.parse("(- 3 7)"), -4)
        self.assertEqual(Lisp.parse("(* 8 7)"), 56)
        self.assertEqual(Lisp.parse("(/ 8 4)"), 2)

    def test_negative_literals(self):
        self.assertEqual(Lisp.parse("(+ -5 5)"), 0)
        self.assertEqual(Lisp.parse("(- -5 -3)"), -2)
        self.assertEqual(Lisp.parse("(+ -2 -3)"), -5)

    def test_single_nesting(self):
        self.assertEqual(Lisp.parse("(+ (+ 1 2) 3)"), 6)
        self.assertEqual(Lisp.parse("(+ 1 (+ 2 3))"), 6)
        self.assertEqual(Lisp.parse("(- (- 9 4) 2)"), 3)
        self.assertEqual(Lisp.parse("(- 100 (+ 20 30))"), 50)

    def test_both_args_nested(self):
        self.assertEqual(Lisp.parse("(+ (- 8 3) (- 10 6))"), 9)
        self.assertEqual(Lisp.parse("(- (+ 5 5) (+ 2 2))"), 6)

    def test_chains(self):
        self.assertEqual(Lisp.parse("(+ (+ (+ 1 1) 1) 1)"), 4)
        self.assertEqual(Lisp.parse("(- 20 (- 10 (- 5 2)))"), 13)

    def test_deep_mixed(self):
        self.assertEqual(Lisp.parse("(+ (- (+ 2 3) (- 8 4)) (+ (- 6 1) (+ 0 2)))"), 8)
        self.assertEqual(Lisp.parse("(- (+ (- 1 2) (+ 3 4)) (- (+ 5 6) (- 7 8)))"), -6)

    def test_bare_atoms(self):
        self.assertEqual(Lisp.parse("42"), 42)
        self.assertEqual(Lisp.parse("-7"), -7)

    def test_large_ints(self):
        self.assertEqual(Lisp.parse("(+ 999999999999 1)"), 1000000000000)

    def test_flat_mul_div(self):
        self.assertEqual(Lisp.parse("(* 3 4)"), 12)
        self.assertEqual(Lisp.parse("(* 0 99)"), 0)
        self.assertEqual(Lisp.parse("(* -3 4)"), -12)
        self.assertEqual(Lisp.parse("(* -6 -7)"), 42)
        self.assertEqual(Lisp.parse("(/ 10 2)"), 5)
        self.assertEqual(Lisp.parse("(/ 9 3)"), 3)
        self.assertEqual(Lisp.parse("(/ -12 4)"), -3)
        self.assertEqual(Lisp.parse("(/ 9 -3)"), -3)

    def test_mul_div_single_nesting(self):
        self.assertEqual(Lisp.parse("(* (+ 1 2) 4)"), 12)
        self.assertEqual(Lisp.parse("(* 2 (- 10 7))"), 6)
        self.assertEqual(Lisp.parse("(/ (+ 6 4) 5)"), 2)
        self.assertEqual(Lisp.parse("(/ 24 (+ 2 4))"), 4)

    def test_mul_div_both_args_nested(self):
        self.assertEqual(Lisp.parse("(/ (* 3 8) (+ 2 4))"), 4)
        self.assertEqual(Lisp.parse("(- (* 5 5) (/ 20 4))"), 20)
        self.assertEqual(Lisp.parse("(+ (/ 100 10) (* 2 3))"), 16)
        self.assertEqual(Lisp.parse("(* (/ 12 4) (- 10 6))"), 12)

    def test_mul_div_chains(self):
        self.assertEqual(Lisp.parse("(* (* 2 3) (* 4 5))"), 120)
        self.assertEqual(Lisp.parse("(/ (/ 64 4) 2)"), 8)
        self.assertEqual(Lisp.parse("(/ 64 (/ 8 2))"), 16)

    def test_mul_div_deep_mixed(self):
        self.assertEqual(Lisp.parse("(+ (* (- 8 5) (+ 2 2)) (/ (* 6 6) (+ 3 3)))"), 18)
        self.assertEqual(Lisp.parse("(- (/ (* 10 10) (+ 5 5)) (* (- 4 2) (+ 1 2)))"), 4)
        self.assertEqual(Lisp.parse("(* (+ (* 2 2) (- 5 1)) (- (/ 20 5) (+ 1 1)))"), 16)


if __name__ == '__main__':
    unittest.main()
