"""Small calculator module with a safe expression evaluator."""

from __future__ import annotations

import argparse
import ast
from typing import Iterable


class CalculatorError(ValueError):
    """Raised when the calculator receives invalid input."""


class Calculator:
    """Collection of basic calculator operations."""

    @staticmethod
    def add(left: float, right: float) -> float:
        return left + right

    @staticmethod
    def subtract(left: float, right: float) -> float:
        return left - right

    @staticmethod
    def multiply(left: float, right: float) -> float:
        return left * right

    @staticmethod
    def divide(left: float, right: float) -> float:
        if right == 0:
            raise CalculatorError("Cannot divide by zero.")
        return left / right

    @staticmethod
    def power(base: float, exponent: float) -> float:
        return base**exponent

    @staticmethod
    def average(values: Iterable[float]) -> float:
        numbers = list(values)
        if not numbers:
            raise CalculatorError("Average requires at least one value.")
        return sum(numbers) / len(numbers)


def evaluate(expression: str) -> float:
    """Safely evaluate a simple arithmetic expression."""

    if not expression or not expression.strip():
        raise CalculatorError("Expression must not be empty.")

    try:
        parsed = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise CalculatorError("Invalid arithmetic expression.") from exc

    return float(_evaluate_node(parsed.body))


def _evaluate_node(node: ast.AST) -> float:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _evaluate_node(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value

    if isinstance(node, ast.BinOp):
        left = _evaluate_node(node.left)
        right = _evaluate_node(node.right)

        if isinstance(node.op, ast.Add):
            return Calculator.add(left, right)
        if isinstance(node.op, ast.Sub):
            return Calculator.subtract(left, right)
        if isinstance(node.op, ast.Mult):
            return Calculator.multiply(left, right)
        if isinstance(node.op, ast.Div):
            return Calculator.divide(left, right)
        if isinstance(node.op, ast.Pow):
            return Calculator.power(left, right)

    raise CalculatorError(
        "Only numbers, parentheses, and +, -, *, /, ** operators are supported."
    )


def _format_result(value: float) -> str:
    return str(int(value)) if value.is_integer() else str(value)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Evaluate a simple arithmetic expression."
    )
    parser.add_argument(
        "expression",
        help='Arithmetic expression to evaluate, for example: "2 * (3 + 4)"',
    )
    args = parser.parse_args()

    try:
        result = evaluate(args.expression)
    except CalculatorError as exc:
        parser.exit(status=1, message=f"error: {exc}\n")

    print(_format_result(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
