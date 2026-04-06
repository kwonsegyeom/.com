import unittest

from calculator import Calculator


class CalculatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self) -> None:
        self.assertEqual(self.calculator.add(4, 5), 9)

    def test_subtract(self) -> None:
        self.assertEqual(self.calculator.subtract(10, 3), 7)

    def test_multiply(self) -> None:
        self.assertEqual(self.calculator.multiply(6, 7), 42)

    def test_divide(self) -> None:
        self.assertAlmostEqual(self.calculator.divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)

    def test_power(self) -> None:
        self.assertEqual(self.calculator.power(2, 5), 32)

    def test_modulo(self) -> None:
        self.assertEqual(self.calculator.modulo(10, 4), 2)

    def test_modulo_by_zero_raises(self) -> None:
        with self.assertRaises(ZeroDivisionError):
            self.calculator.modulo(5, 0)

    def test_evaluate_expression(self) -> None:
        self.assertEqual(self.calculator.evaluate("2 + 3 * 4"), 14)

    def test_evaluate_expression_with_parentheses(self) -> None:
        self.assertEqual(self.calculator.evaluate("(2 + 3) * 4"), 20)

    def test_evaluate_expression_with_power_and_unary(self) -> None:
        self.assertEqual(self.calculator.evaluate("-2 ** 3"), -8)

    def test_evaluate_invalid_expression_raises(self) -> None:
        with self.assertRaises(ValueError):
            self.calculator.evaluate("__import__('os').system('echo bad')")


if __name__ == "__main__":
    unittest.main()
