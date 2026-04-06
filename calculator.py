"""Basic arithmetic calculator: functions and a simple command-line interface."""

from __future__ import annotations

import argparse
import sys
from typing import Callable


def add(a: float, b: float) -> float:
    """Return a + b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a - b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a * b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a / b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


_OPERATORS: dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def apply(op: str, a: float, b: float) -> float:
    """Apply a binary operator by name: +, -, *, /."""
    if op not in _OPERATORS:
        raise ValueError(f"unsupported operator: {op!r}")
    return _OPERATORS[op](a, b)


def _parse_float(s: str) -> float:
    try:
        return float(s)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"not a valid number: {s!r}") from e


def main(argv: list[str] | None = None) -> int:
    """CLI: `calculator A OP B` where OP is +, -, *, /."""
    parser = argparse.ArgumentParser(
        description="Evaluate A OP B with floating-point numbers.",
    )
    parser.add_argument("a", type=_parse_float, help="first operand")
    parser.add_argument(
        "op",
        choices=["+", "-", "*", "/"],
        help="operator",
    )
    parser.add_argument("b", type=_parse_float, help="second operand")
    args = parser.parse_args(argv)

    try:
        result = apply(args.op, args.a, args.b)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 2

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
