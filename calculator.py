"""Calculator module with basic arithmetic and expression evaluation."""

from __future__ import annotations

import ast
import operator
from typing import Union

Number = Union[int, float]


class Calculator:
    """Simple calculator with basic operations."""

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

    def power(self, left: Number, right: Number) -> Number:
        return left**right

    def modulo(self, left: Number, right: Number) -> Number:
        if right == 0:
            raise ZeroDivisionError("Cannot take modulo by zero.")
        return left % right

    def evaluate(self, expression: str) -> Number:
        """Safely evaluate a numeric expression using +, -, *, /, %, and **."""
        parsed = ast.parse(expression, mode="eval")
        return _evaluate_ast(parsed.body)


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _evaluate_ast(node: ast.AST) -> Number:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Expression contains non-numeric constant.")

    if isinstance(node, ast.BinOp):
        operator_type = type(node.op)
        if operator_type not in _BINARY_OPERATORS:
            raise ValueError("Expression uses an unsupported operator.")
        left = _evaluate_ast(node.left)
        right = _evaluate_ast(node.right)
        if operator_type in (ast.Div, ast.Mod) and right == 0:
            raise ZeroDivisionError("Division or modulo by zero is not allowed.")
        return _BINARY_OPERATORS[operator_type](left, right)

    if isinstance(node, ast.UnaryOp):
        operator_type = type(node.op)
        if operator_type not in _UNARY_OPERATORS:
            raise ValueError("Expression uses an unsupported unary operator.")
        operand = _evaluate_ast(node.operand)
        return _UNARY_OPERATORS[operator_type](operand)

    raise ValueError("Expression contains unsupported syntax.")
