"""A full-featured calculator supporting basic and advanced operations."""

import math
from typing import List


class Calculator:
    """Calculator with history tracking and support for basic & advanced math."""

    def __init__(self) -> None:
        self._history: List[str] = []

    @property
    def history(self) -> List[str]:
        """Return a copy of the calculation history."""
        return list(self._history)

    def clear_history(self) -> None:
        """Clear all stored history."""
        self._history.clear()

    def _record(self, expression: str, result: float) -> float:
        self._history.append(f"{expression} = {result}")
        return result

    # ── Basic arithmetic ─────────────────────────────────────────────

    def add(self, a: float, b: float) -> float:
        return self._record(f"{a} + {b}", a + b)

    def subtract(self, a: float, b: float) -> float:
        return self._record(f"{a} - {b}", a - b)

    def multiply(self, a: float, b: float) -> float:
        return self._record(f"{a} * {b}", a * b)

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self._record(f"{a} / {b}", a / b)

    def modulo(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero")
        return self._record(f"{a} % {b}", a % b)

    # ── Power & roots ────────────────────────────────────────────────

    def power(self, base: float, exponent: float) -> float:
        return self._record(f"{base} ^ {exponent}", base ** exponent)

    def square_root(self, a: float) -> float:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return self._record(f"sqrt({a})", math.sqrt(a))

    # ── Logarithmic ──────────────────────────────────────────────────

    def log(self, a: float, base: float = 10) -> float:
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        return self._record(f"log_{base}({a})", math.log(a, base))

    def ln(self, a: float) -> float:
        if a <= 0:
            raise ValueError("Natural logarithm undefined for non-positive values")
        return self._record(f"ln({a})", math.log(a))

    # ── Trigonometric (input in radians) ─────────────────────────────

    def sin(self, a: float) -> float:
        return self._record(f"sin({a})", math.sin(a))

    def cos(self, a: float) -> float:
        return self._record(f"cos({a})", math.cos(a))

    def tan(self, a: float) -> float:
        return self._record(f"tan({a})", math.tan(a))

    # ── Factorial ────────────────────────────────────────────────────

    def factorial(self, n: int) -> int:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers")
        result = math.factorial(n)
        return self._record(f"{n}!", result)

    # ── Utility ──────────────────────────────────────────────────────

    def absolute(self, a: float) -> float:
        return self._record(f"|{a}|", abs(a))

    def negate(self, a: float) -> float:
        return self._record(f"-({a})", -a)
