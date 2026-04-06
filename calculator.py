"""Simple calculator utilities and CLI."""

from __future__ import annotations

import ast
import operator
import sys
from typing import Callable

Number = int | float


class Calculator:
    """Perform basic arithmetic and evaluate safe math expressions."""

    _binary_operators: dict[type[ast.operator], Callable[[Number, Number], Number]] = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    _unary_operators: dict[type[ast.unaryop], Callable[[Number], Number]] = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

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

    def evaluate(self, expression: str) -> Number:
        """Safely evaluate an arithmetic expression."""
        parsed_expression = ast.parse(expression, mode="eval")
        return self._evaluate_node(parsed_expression.body)

    def _evaluate_node(self, node: ast.AST) -> Number:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return node.value

        if isinstance(node, ast.BinOp):
            operation = self._binary_operators.get(type(node.op))
            if operation is None:
                raise ValueError(f"Unsupported operator: {ast.dump(node.op)}")
            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)
            if isinstance(node.op, ast.Div) and right == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return operation(left, right)

        if isinstance(node, ast.UnaryOp):
            operation = self._unary_operators.get(type(node.op))
            if operation is None:
                raise ValueError(f"Unsupported unary operator: {ast.dump(node.op)}")
            return operation(self._evaluate_node(node.operand))

        raise ValueError(f"Unsupported expression: {ast.dump(node)}")


def main(argv: list[str] | None = None) -> int:
    arguments = argv if argv is not None else sys.argv[1:]
    expression = " ".join(arguments).strip()
    if not expression:
        expression = input("Enter an arithmetic expression: ").strip()

    calculator = Calculator()
    try:
        result = calculator.evaluate(expression)
    except (SyntaxError, ValueError, ZeroDivisionError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
