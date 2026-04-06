"""Tests for calculator module."""

import unittest

from calculator import add, apply, divide, multiply, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self) -> None:
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 7), -7)

    def test_multiply(self) -> None:
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self) -> None:
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(1, 4), 0.25)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            divide(1, 0)
        self.assertIn("zero", str(ctx.exception).lower())

    def test_apply(self) -> None:
        self.assertEqual(apply("+", 1, 2), 3)
        self.assertEqual(apply("-", 5, 2), 3)
        self.assertEqual(apply("*", 3, 4), 12)
        self.assertEqual(apply("/", 8, 2), 4)

    def test_apply_bad_operator(self) -> None:
        with self.assertRaises(ValueError):
            apply("%", 1, 2)


if __name__ == "__main__":
    unittest.main()
