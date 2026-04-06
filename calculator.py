#!/usr/bin/env python3
"""A small calculator module with a safe expression evaluator."""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from typing import Union

Number = Union[int, float]


@dataclass
class Calculator:
    """Simple calculator with basic arithmetic operations."""

    last_result: float = 0.0

    def add(self, left: Number, right: Number) -> Number:
        return left + right

    def subtract(self, left: Number, right: Number) -> Number:
        return left - right

    def multiply(self, left: Number, right: Number) -> Number:
        return left * right

    def divide(self, left: Number, right: Number) -> float:
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return left / right

    def evaluate(self, expression: str) -> float:
        """Evaluate a numeric expression using a restricted AST."""
        if not expression or not expression.strip():
            raise ValueError("Expression cannot be empty.")

        try:
            parsed = ast.parse(expression, mode="eval")
        except SyntaxError as exc:
            raise ValueError(f"Invalid expression: {expression!r}") from exc

        result = float(self._eval_node(parsed.body))
        self.last_result = result
        return result

    def _eval_node(self, node: ast.AST) -> Number:
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Only numeric literals are allowed.")

        if isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            if isinstance(node.op, ast.UAdd):
                return +operand
            if isinstance(node.op, ast.USub):
                return -operand
            raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")

        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)

            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return left / right
            if isinstance(node.op, ast.FloorDiv):
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return left // right
            if isinstance(node.op, ast.Mod):
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return left % right
            if isinstance(node.op, ast.Pow):
                return left**right

            raise ValueError(f"Unsupported binary operator: {type(node.op).__name__}")

        raise ValueError(f"Unsupported expression element: {type(node).__name__}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run simple calculator expressions.")
    parser.add_argument(
        "expression",
        nargs="?",
        help='Expression to evaluate, e.g. "2 + 3 * 4". If omitted, runs interactively.',
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()
    calculator = Calculator()

    if args.expression:
        print(calculator.evaluate(args.expression))
        return

    print("Calculator interactive mode. Type 'quit' to exit.")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"quit", "exit"}:
            break
        try:
            print(calculator.evaluate(user_input))
        except Exception as error:  # pragma: no cover - CLI guard
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
