"""A calculator module supporting basic and scientific operations."""

import math
from typing import List, Union

Number = Union[int, float]


class Calculator:
    """A calculator with memory and history tracking."""

    def __init__(self) -> None:
        self.memory: float = 0.0
        self.history: List[str] = []

    def _record(self, expression: str, result: Number) -> Number:
        self.history.append(f"{expression} = {result}")
        return result

    def add(self, a: Number, b: Number) -> Number:
        return self._record(f"{a} + {b}", a + b)

    def subtract(self, a: Number, b: Number) -> Number:
        return self._record(f"{a} - {b}", a - b)

    def multiply(self, a: Number, b: Number) -> Number:
        return self._record(f"{a} * {b}", a * b)

    def divide(self, a: Number, b: Number) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        return self._record(f"{a} / {b}", result)

    def power(self, base: Number, exponent: Number) -> Number:
        result = base ** exponent
        return self._record(f"{base} ^ {exponent}", result)

    def sqrt(self, n: Number) -> float:
        if n < 0:
            raise ValueError("Cannot take square root of a negative number")
        result = math.sqrt(n)
        return self._record(f"sqrt({n})", result)

    def modulo(self, a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo by zero")
        return self._record(f"{a} % {b}", a % b)

    def factorial(self, n: int) -> int:
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial requires a non-negative integer")
        result = math.factorial(n)
        return self._record(f"{n}!", result)

    def absolute(self, n: Number) -> Number:
        return self._record(f"|{n}|", abs(n))

    def negate(self, n: Number) -> Number:
        return self._record(f"-({n})", -n)

    def memory_store(self, value: Number) -> None:
        self.memory = float(value)

    def memory_recall(self) -> float:
        return self.memory

    def memory_clear(self) -> None:
        self.memory = 0.0

    def memory_add(self, value: Number) -> None:
        self.memory += value

    def clear_history(self) -> None:
        self.history.clear()

    def get_history(self) -> List[str]:
        return list(self.history)


def evaluate(expression: str) -> float:
    """Safely evaluate a mathematical expression string.

    Supports: +, -, *, /, **, (), and numeric literals.
    Raises ValueError for disallowed expressions.
    """
    allowed = set("0123456789+-*/().% ")
    if not all(ch in allowed for ch in expression):
        raise ValueError(f"Disallowed characters in expression: {expression!r}")
    try:
        result = eval(expression, {"__builtins__": {}}, {})  # noqa: S307
    except Exception as exc:
        raise ValueError(f"Invalid expression: {expression!r}") from exc
    if not isinstance(result, (int, float)):
        raise ValueError(f"Expression did not produce a number: {expression!r}")
    return result
