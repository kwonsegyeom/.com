"""Core calculator module providing arithmetic and scientific operations."""

import math
from typing import Union

Number = Union[int, float]


class CalculatorError(Exception):
    """Raised when an invalid operation is attempted."""


class Calculator:
    """A stateful calculator that keeps a running history of operations."""

    def __init__(self) -> None:
        self._result: float = 0.0
        self._history: list[str] = []

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def result(self) -> float:
        """The current accumulated result."""
        return self._result

    @property
    def history(self) -> list[str]:
        """A read-only copy of the operation history."""
        return list(self._history)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _record(self, expression: str, result: float) -> None:
        self._result = result
        self._history.append(f"{expression} = {result}")

    # ------------------------------------------------------------------
    # Basic arithmetic
    # ------------------------------------------------------------------

    def add(self, a: Number, b: Number) -> float:
        """Return the sum of *a* and *b*."""
        result = float(a + b)
        self._record(f"{a} + {b}", result)
        return result

    def subtract(self, a: Number, b: Number) -> float:
        """Return the difference *a* - *b*."""
        result = float(a - b)
        self._record(f"{a} - {b}", result)
        return result

    def multiply(self, a: Number, b: Number) -> float:
        """Return the product of *a* and *b*."""
        result = float(a * b)
        self._record(f"{a} * {b}", result)
        return result

    def divide(self, a: Number, b: Number) -> float:
        """Return the quotient *a* / *b*.

        Raises:
            CalculatorError: if *b* is zero.
        """
        if b == 0:
            raise CalculatorError("Division by zero is undefined.")
        result = float(a / b)
        self._record(f"{a} / {b}", result)
        return result

    def modulo(self, a: Number, b: Number) -> float:
        """Return *a* mod *b*.

        Raises:
            CalculatorError: if *b* is zero.
        """
        if b == 0:
            raise CalculatorError("Modulo by zero is undefined.")
        result = float(a % b)
        self._record(f"{a} % {b}", result)
        return result

    def power(self, base: Number, exponent: Number) -> float:
        """Return *base* raised to the power of *exponent*."""
        result = float(base ** exponent)
        self._record(f"{base} ** {exponent}", result)
        return result

    # ------------------------------------------------------------------
    # Scientific / advanced operations
    # ------------------------------------------------------------------

    def sqrt(self, a: Number) -> float:
        """Return the square root of *a*.

        Raises:
            CalculatorError: if *a* is negative.
        """
        if a < 0:
            raise CalculatorError("Square root of a negative number is not real.")
        result = math.sqrt(float(a))
        self._record(f"sqrt({a})", result)
        return result

    def log(self, a: Number, base: Number = math.e) -> float:
        """Return the logarithm of *a* with the given *base* (default: natural log).

        Raises:
            CalculatorError: if *a* is non-positive or *base* is invalid.
        """
        if a <= 0:
            raise CalculatorError("Logarithm is only defined for positive numbers.")
        if base <= 0 or base == 1:
            raise CalculatorError("Logarithm base must be positive and not equal to 1.")
        result = math.log(float(a), float(base))
        base_label = "e" if base == math.e else str(base)
        self._record(f"log_{base_label}({a})", result)
        return result

    def sin(self, angle_degrees: Number) -> float:
        """Return the sine of *angle_degrees* (in degrees)."""
        result = math.sin(math.radians(float(angle_degrees)))
        self._record(f"sin({angle_degrees}°)", result)
        return result

    def cos(self, angle_degrees: Number) -> float:
        """Return the cosine of *angle_degrees* (in degrees)."""
        result = math.cos(math.radians(float(angle_degrees)))
        self._record(f"cos({angle_degrees}°)", result)
        return result

    def tan(self, angle_degrees: Number) -> float:
        """Return the tangent of *angle_degrees* (in degrees).

        Raises:
            CalculatorError: if the angle is 90° or 270° (undefined).
        """
        if float(angle_degrees) % 180 == 90:
            raise CalculatorError(f"tan({angle_degrees}°) is undefined.")
        result = math.tan(math.radians(float(angle_degrees)))
        self._record(f"tan({angle_degrees}°)", result)
        return result

    def factorial(self, n: int) -> int:
        """Return *n*! (n factorial).

        Raises:
            CalculatorError: if *n* is negative or not an integer.
        """
        if not isinstance(n, int) or isinstance(n, bool):
            raise CalculatorError("Factorial is only defined for non-negative integers.")
        if n < 0:
            raise CalculatorError("Factorial is not defined for negative integers.")
        result = math.factorial(n)
        self._record(f"{n}!", result)
        return result

    def absolute(self, a: Number) -> float:
        """Return the absolute value of *a*."""
        result = float(abs(a))
        self._record(f"|{a}|", result)
        return result

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def clear(self) -> None:
        """Reset the result and clear the history."""
        self._result = 0.0
        self._history.clear()

    def clear_history(self) -> None:
        """Clear the history without resetting the current result."""
        self._history.clear()

    def __repr__(self) -> str:
        return f"Calculator(result={self._result})"
