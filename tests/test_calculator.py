"""Tests for the calculator module."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from calculator import Calculator, CalculatorError, evaluate


REPO_ROOT = Path(__file__).resolve().parents[1]


class CalculatorOperationTests(unittest.TestCase):
    def test_basic_operations(self) -> None:
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.subtract(10, 4), 6)
        self.assertEqual(Calculator.multiply(6, 7), 42)
        self.assertEqual(Calculator.power(2, 5), 32)

    def test_average(self) -> None:
        self.assertEqual(Calculator.average([2, 4, 6, 8]), 5)

    def test_divide_by_zero_raises(self) -> None:
        with self.assertRaises(CalculatorError):
            Calculator.divide(5, 0)

    def test_average_requires_values(self) -> None:
        with self.assertRaises(CalculatorError):
            Calculator.average([])


class CalculatorEvaluateTests(unittest.TestCase):
    def test_evaluate_expression(self) -> None:
        self.assertEqual(evaluate("2 * (3 + 4)"), 14.0)

    def test_evaluate_power_and_unary_values(self) -> None:
        self.assertEqual(evaluate("-2 ** 3 + 10"), 2.0)

    def test_invalid_expression_rejected(self) -> None:
        with self.assertRaises(CalculatorError):
            evaluate("sum([1, 2, 3])")

    def test_empty_expression_rejected(self) -> None:
        with self.assertRaises(CalculatorError):
            evaluate("  ")


class CalculatorCliTests(unittest.TestCase):
    def test_cli_prints_result(self) -> None:
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "calculator.py"), "8 / 2 + 1"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "5")

    def test_cli_reports_errors(self) -> None:
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "calculator.py"), "10 / 0"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 1)
        self.assertIn("Cannot divide by zero.", result.stderr)


if __name__ == "__main__":
    unittest.main()
