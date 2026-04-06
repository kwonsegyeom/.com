"""Unit tests for the Calculator class."""

import math
import pytest

from calculator import Calculator
from calculator.calculator import CalculatorError


@pytest.fixture()
def calc() -> Calculator:
    return Calculator()


# ---------------------------------------------------------------------------
# Basic arithmetic
# ---------------------------------------------------------------------------


class TestAdd:
    def test_positive_numbers(self, calc):
        assert calc.add(3, 4) == 7

    def test_negative_numbers(self, calc):
        assert calc.add(-5, -3) == -8

    def test_mixed_signs(self, calc):
        assert calc.add(-10, 4) == -6

    def test_floats(self, calc):
        assert calc.add(1.5, 2.5) == pytest.approx(4.0)

    def test_zero(self, calc):
        assert calc.add(0, 0) == 0


class TestSubtract:
    def test_basic(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_negative_result(self, calc):
        assert calc.subtract(3, 7) == -4

    def test_floats(self, calc):
        assert calc.subtract(5.5, 2.2) == pytest.approx(3.3)


class TestMultiply:
    def test_positive(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_by_zero(self, calc):
        assert calc.multiply(100, 0) == 0

    def test_negatives(self, calc):
        assert calc.multiply(-3, -4) == 12

    def test_mixed(self, calc):
        assert calc.multiply(-3, 4) == -12

    def test_floats(self, calc):
        assert calc.multiply(2.5, 4) == pytest.approx(10.0)


class TestDivide:
    def test_basic(self, calc):
        assert calc.divide(10, 2) == 5

    def test_float_result(self, calc):
        assert calc.divide(7, 2) == pytest.approx(3.5)

    def test_negative(self, calc):
        assert calc.divide(-9, 3) == -3

    def test_divide_by_zero(self, calc):
        with pytest.raises(CalculatorError, match="Division by zero"):
            calc.divide(5, 0)


class TestModulo:
    def test_basic(self, calc):
        assert calc.modulo(10, 3) == 1

    def test_zero_remainder(self, calc):
        assert calc.modulo(9, 3) == 0

    def test_modulo_by_zero(self, calc):
        with pytest.raises(CalculatorError, match="Modulo by zero"):
            calc.modulo(5, 0)


class TestPower:
    def test_square(self, calc):
        assert calc.power(2, 10) == 1024

    def test_zero_exponent(self, calc):
        assert calc.power(999, 0) == 1

    def test_fractional_exponent(self, calc):
        assert calc.power(9, 0.5) == pytest.approx(3.0)

    def test_negative_base(self, calc):
        assert calc.power(-2, 3) == -8


# ---------------------------------------------------------------------------
# Scientific operations
# ---------------------------------------------------------------------------


class TestSqrt:
    def test_perfect_square(self, calc):
        assert calc.sqrt(25) == 5

    def test_float(self, calc):
        assert calc.sqrt(2) == pytest.approx(math.sqrt(2))

    def test_zero(self, calc):
        assert calc.sqrt(0) == 0

    def test_negative(self, calc):
        with pytest.raises(CalculatorError, match="negative"):
            calc.sqrt(-1)


class TestLog:
    def test_natural_log(self, calc):
        assert calc.log(math.e) == pytest.approx(1.0)

    def test_log_base_10(self, calc):
        assert calc.log(1000, 10) == pytest.approx(3.0)

    def test_log_base_2(self, calc):
        assert calc.log(8, 2) == pytest.approx(3.0)

    def test_log_of_one(self, calc):
        assert calc.log(1) == pytest.approx(0.0)

    def test_non_positive_argument(self, calc):
        with pytest.raises(CalculatorError, match="positive"):
            calc.log(0)

    def test_invalid_base(self, calc):
        with pytest.raises(CalculatorError, match="base"):
            calc.log(5, 1)


class TestTrig:
    def test_sin_zero(self, calc):
        assert calc.sin(0) == pytest.approx(0.0)

    def test_sin_90(self, calc):
        assert calc.sin(90) == pytest.approx(1.0)

    def test_cos_zero(self, calc):
        assert calc.cos(0) == pytest.approx(1.0)

    def test_cos_90(self, calc):
        assert calc.cos(90) == pytest.approx(0.0, abs=1e-10)

    def test_tan_45(self, calc):
        assert calc.tan(45) == pytest.approx(1.0)

    def test_tan_90_undefined(self, calc):
        with pytest.raises(CalculatorError, match="undefined"):
            calc.tan(90)

    def test_tan_270_undefined(self, calc):
        with pytest.raises(CalculatorError, match="undefined"):
            calc.tan(270)


class TestFactorial:
    def test_zero(self, calc):
        assert calc.factorial(0) == 1

    def test_one(self, calc):
        assert calc.factorial(1) == 1

    def test_five(self, calc):
        assert calc.factorial(5) == 120

    def test_negative(self, calc):
        with pytest.raises(CalculatorError, match="negative"):
            calc.factorial(-1)

    def test_float_rejected(self, calc):
        with pytest.raises(CalculatorError):
            calc.factorial(3.5)  # type: ignore[arg-type]


class TestAbsolute:
    def test_negative(self, calc):
        assert calc.absolute(-7) == 7

    def test_positive(self, calc):
        assert calc.absolute(7) == 7

    def test_zero(self, calc):
        assert calc.absolute(0) == 0


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------


class TestHistory:
    def test_history_records_operations(self, calc):
        calc.add(1, 2)
        calc.multiply(3, 4)
        assert len(calc.history) == 2

    def test_history_is_copy(self, calc):
        calc.add(1, 1)
        h = calc.history
        h.append("tampered")
        assert len(calc.history) == 1

    def test_clear_resets_history_and_result(self, calc):
        calc.add(5, 5)
        calc.clear()
        assert calc.history == []
        assert calc.result == 0.0

    def test_clear_history_only(self, calc):
        calc.add(5, 5)
        calc.clear_history()
        assert calc.history == []
        assert calc.result == 10.0


class TestResult:
    def test_result_tracks_last_operation(self, calc):
        calc.add(3, 7)
        assert calc.result == 10.0
        calc.multiply(2, 6)
        assert calc.result == 12.0
