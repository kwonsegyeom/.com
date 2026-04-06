"""Unit tests for the Calculator class."""

import math
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ── Basic arithmetic ────────────────────────────────────────────────


class TestAdd:
    def test_positive_numbers(self, calc):
        assert calc.add(2, 3) == 5

    def test_negative_numbers(self, calc):
        assert calc.add(-1, -2) == -3

    def test_mixed_sign(self, calc):
        assert calc.add(-1, 3) == 2

    def test_floats(self, calc):
        assert calc.add(0.1, 0.2) == pytest.approx(0.3)

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
    def test_basic(self, calc):
        assert calc.multiply(3, 4) == 12

    def test_by_zero(self, calc):
        assert calc.multiply(5, 0) == 0

    def test_negative(self, calc):
        assert calc.multiply(-3, 4) == -12

    def test_both_negative(self, calc):
        assert calc.multiply(-3, -4) == 12


class TestDivide:
    def test_basic(self, calc):
        assert calc.divide(10, 2) == 5

    def test_float_result(self, calc):
        assert calc.divide(7, 2) == 3.5

    def test_divide_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.divide(5, 0)


class TestModulo:
    def test_basic(self, calc):
        assert calc.modulo(10, 3) == 1

    def test_even_division(self, calc):
        assert calc.modulo(9, 3) == 0

    def test_modulo_by_zero(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.modulo(5, 0)


# ── Power & roots ──────────────────────────────────────────────────


class TestPower:
    def test_basic(self, calc):
        assert calc.power(2, 3) == 8

    def test_zero_exponent(self, calc):
        assert calc.power(5, 0) == 1

    def test_negative_exponent(self, calc):
        assert calc.power(2, -1) == 0.5

    def test_fractional_exponent(self, calc):
        assert calc.power(4, 0.5) == pytest.approx(2.0)


class TestSquareRoot:
    def test_perfect_square(self, calc):
        assert calc.square_root(9) == 3.0

    def test_non_perfect(self, calc):
        assert calc.square_root(2) == pytest.approx(math.sqrt(2))

    def test_zero(self, calc):
        assert calc.square_root(0) == 0.0

    def test_negative_raises(self, calc):
        with pytest.raises(ValueError, match="negative"):
            calc.square_root(-4)


# ── Logarithmic ────────────────────────────────────────────────────


class TestLog:
    def test_base_10(self, calc):
        assert calc.log(100, 10) == pytest.approx(2.0)

    def test_base_2(self, calc):
        assert calc.log(8, 2) == pytest.approx(3.0)

    def test_non_positive_raises(self, calc):
        with pytest.raises(ValueError, match="non-positive"):
            calc.log(0)

    def test_bad_base_raises(self, calc):
        with pytest.raises(ValueError, match="base"):
            calc.log(10, 1)


class TestLn:
    def test_e(self, calc):
        assert calc.ln(math.e) == pytest.approx(1.0)

    def test_one(self, calc):
        assert calc.ln(1) == pytest.approx(0.0)

    def test_non_positive_raises(self, calc):
        with pytest.raises(ValueError, match="non-positive"):
            calc.ln(-1)


# ── Trigonometric ──────────────────────────────────────────────────


class TestTrig:
    def test_sin_zero(self, calc):
        assert calc.sin(0) == pytest.approx(0.0)

    def test_sin_pi_half(self, calc):
        assert calc.sin(math.pi / 2) == pytest.approx(1.0)

    def test_cos_zero(self, calc):
        assert calc.cos(0) == pytest.approx(1.0)

    def test_cos_pi(self, calc):
        assert calc.cos(math.pi) == pytest.approx(-1.0)

    def test_tan_zero(self, calc):
        assert calc.tan(0) == pytest.approx(0.0)


# ── Factorial ──────────────────────────────────────────────────────


class TestFactorial:
    def test_zero(self, calc):
        assert calc.factorial(0) == 1

    def test_basic(self, calc):
        assert calc.factorial(5) == 120

    def test_one(self, calc):
        assert calc.factorial(1) == 1

    def test_negative_raises(self, calc):
        with pytest.raises(ValueError, match="non-negative"):
            calc.factorial(-1)


# ── Utility ────────────────────────────────────────────────────────


class TestAbsolute:
    def test_positive(self, calc):
        assert calc.absolute(5) == 5

    def test_negative(self, calc):
        assert calc.absolute(-5) == 5

    def test_zero(self, calc):
        assert calc.absolute(0) == 0


class TestNegate:
    def test_positive(self, calc):
        assert calc.negate(5) == -5

    def test_negative(self, calc):
        assert calc.negate(-5) == 5


# ── History ────────────────────────────────────────────────────────


class TestHistory:
    def test_empty_initially(self, calc):
        assert calc.history == []

    def test_records_operations(self, calc):
        calc.add(1, 2)
        calc.multiply(3, 4)
        assert len(calc.history) == 2
        assert "1 + 2 = 3" in calc.history[0]

    def test_clear(self, calc):
        calc.add(1, 2)
        calc.clear_history()
        assert calc.history == []

    def test_history_is_copy(self, calc):
        calc.add(1, 2)
        hist = calc.history
        hist.clear()
        assert len(calc.history) == 1
