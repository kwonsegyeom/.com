"""Unit tests for the calculator module."""

import math
import pytest
from calculator import Calculator, evaluate


@pytest.fixture
def calc():
    return Calculator()


class TestBasicOperations:
    def test_add_positive(self, calc):
        assert calc.add(2, 3) == 5

    def test_add_negative(self, calc):
        assert calc.add(-2, -3) == -5

    def test_add_floats(self, calc):
        assert calc.add(1.5, 2.5) == 4.0

    def test_subtract(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_subtract_negative_result(self, calc):
        assert calc.subtract(3, 7) == -4

    def test_multiply(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_multiply_by_zero(self, calc):
        assert calc.multiply(5, 0) == 0

    def test_multiply_floats(self, calc):
        assert calc.multiply(2.5, 4) == 10.0

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5.0

    def test_divide_float_result(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.divide(5, 0)


class TestScientificOperations:
    def test_power(self, calc):
        assert calc.power(2, 3) == 8

    def test_power_zero_exponent(self, calc):
        assert calc.power(5, 0) == 1

    def test_power_negative_exponent(self, calc):
        assert calc.power(2, -1) == 0.5

    def test_sqrt(self, calc):
        assert calc.sqrt(9) == 3.0

    def test_sqrt_zero(self, calc):
        assert calc.sqrt(0) == 0.0

    def test_sqrt_negative(self, calc):
        with pytest.raises(ValueError, match="negative"):
            calc.sqrt(-4)

    def test_modulo(self, calc):
        assert calc.modulo(10, 3) == 1

    def test_modulo_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.modulo(10, 0)

    def test_factorial(self, calc):
        assert calc.factorial(5) == 120

    def test_factorial_zero(self, calc):
        assert calc.factorial(0) == 1

    def test_factorial_negative(self, calc):
        with pytest.raises(ValueError, match="non-negative integer"):
            calc.factorial(-1)

    def test_absolute_positive(self, calc):
        assert calc.absolute(5) == 5

    def test_absolute_negative(self, calc):
        assert calc.absolute(-5) == 5

    def test_negate(self, calc):
        assert calc.negate(5) == -5

    def test_negate_negative(self, calc):
        assert calc.negate(-3) == 3


class TestMemory:
    def test_memory_default(self, calc):
        assert calc.memory_recall() == 0.0

    def test_memory_store_and_recall(self, calc):
        calc.memory_store(42)
        assert calc.memory_recall() == 42.0

    def test_memory_add(self, calc):
        calc.memory_store(10)
        calc.memory_add(5)
        assert calc.memory_recall() == 15.0

    def test_memory_clear(self, calc):
        calc.memory_store(100)
        calc.memory_clear()
        assert calc.memory_recall() == 0.0


class TestHistory:
    def test_history_empty(self, calc):
        assert calc.get_history() == []

    def test_history_tracks_operations(self, calc):
        calc.add(1, 2)
        calc.multiply(3, 4)
        history = calc.get_history()
        assert len(history) == 2
        assert "1 + 2 = 3" in history[0]
        assert "3 * 4 = 12" in history[1]

    def test_clear_history(self, calc):
        calc.add(1, 2)
        calc.clear_history()
        assert calc.get_history() == []

    def test_history_returns_copy(self, calc):
        calc.add(1, 2)
        history = calc.get_history()
        history.clear()
        assert len(calc.get_history()) == 1


class TestEvaluate:
    def test_simple_addition(self):
        assert evaluate("2 + 3") == 5

    def test_complex_expression(self):
        assert evaluate("(2 + 3) * 4") == 20

    def test_division(self):
        assert evaluate("10 / 4") == 2.5

    def test_modulo(self):
        assert evaluate("10 % 3") == 1

    def test_disallowed_characters(self):
        with pytest.raises(ValueError, match="Disallowed"):
            evaluate("import os")

    def test_invalid_expression(self):
        with pytest.raises(ValueError, match="Invalid"):
            evaluate("2 +")
