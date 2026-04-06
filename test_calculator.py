import unittest

from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_basic_operations(self) -> None:
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.subtract(10, 4), 6)
        self.assertEqual(self.calculator.multiply(6, 7), 42)
        self.assertEqual(self.calculator.divide(20, 5), 4)

    def test_expression_respects_precedence(self) -> None:
        self.assertEqual(self.calculator.evaluate("2 + 3 * 4"), 14)

    def test_expression_supports_parentheses_and_unary_values(self) -> None:
        self.assertEqual(self.calculator.evaluate("-(2 + 3) * 4"), -20)

    def test_expression_supports_power_and_modulo(self) -> None:
        self.assertEqual(self.calculator.evaluate("2 ** 3 % 3"), 2)

    def test_divide_by_zero_raises_error(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(4, 0)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.evaluate("4 / 0")

    def test_invalid_expression_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("abs(-2)")


if __name__ == "__main__":
    unittest.main()
