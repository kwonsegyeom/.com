"""Unit tests for calculator functionality."""

import unittest

from calculator import Calculator


class CalculatorOperationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self) -> None:
        self.assertEqual(self.calculator.add(2, 3), 5)

    def test_subtract(self) -> None:
        self.assertEqual(self.calculator.subtract(9, 4), 5)

    def test_multiply(self) -> None:
        self.assertEqual(self.calculator.multiply(6, 7), 42)

    def test_divide(self) -> None:
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(1, 0)

    def test_power(self) -> None:
        self.assertEqual(self.calculator.power(2, 5), 32)


class CalculatorExpressionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_evaluate_expression(self) -> None:
        self.assertEqual(self.calculator.evaluate("2 + 3 * 4"), 14)

    def test_evaluate_parentheses(self) -> None:
        self.assertEqual(self.calculator.evaluate("(2 + 3) * 4"), 20)

    def test_evaluate_unary(self) -> None:
        self.assertEqual(self.calculator.evaluate("-5 + +2"), -3)

    def test_evaluate_power(self) -> None:
        self.assertEqual(self.calculator.evaluate("2 ** 3"), 8)

    def test_evaluate_empty_expression_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("   ")

    def test_evaluate_invalid_syntax_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("2 +")

    def test_evaluate_disallowed_expression_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("__import__('os').system('echo nope')")


if __name__ == "__main__":
    unittest.main()
