"""Simple calculator module with safe expression evaluation."""

from __future__ import annotations

import ast


class Calculator:
    """Perform arithmetic operations and safely evaluate expressions."""

    def add(self, left: float, right: float) -> float:
        return left + right

    def subtract(self, left: float, right: float) -> float:
        return left - right

    def multiply(self, left: float, right: float) -> float:
        return left * right

    def divide(self, left: float, right: float) -> float:
        if right == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return left / right

    def power(self, base: float, exponent: float) -> float:
        return base**exponent

    def evaluate(self, expression: str) -> float:
        """Safely evaluate an arithmetic expression.

        Supported operators:
          - Addition (+), subtraction (-), multiplication (*), division (/)
          - Exponentiation (**)
          - Parentheses and unary +/-
        """

        expression = expression.strip()
        if not expression:
            raise ValueError("Expression cannot be empty.")

        try:
            parsed = ast.parse(expression, mode="eval")
        except SyntaxError as exc:
            raise ValueError("Invalid expression syntax.") from exc

        return float(self._eval_node(parsed.body))

    def _eval_node(self, node: ast.AST) -> float:
        if isinstance(node, ast.BinOp):
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)

            if isinstance(node.op, ast.Add):
                return self.add(left, right)
            if isinstance(node.op, ast.Sub):
                return self.subtract(left, right)
            if isinstance(node.op, ast.Mult):
                return self.multiply(left, right)
            if isinstance(node.op, ast.Div):
                return self.divide(left, right)
            if isinstance(node.op, ast.Pow):
                return self.power(left, right)
            raise ValueError("Unsupported binary operator.")

        if isinstance(node, ast.UnaryOp):
            operand = self._eval_node(node.operand)
            if isinstance(node.op, ast.UAdd):
                return operand
            if isinstance(node.op, ast.USub):
                return -operand
            raise ValueError("Unsupported unary operator.")

        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.Num):  # pragma: no cover - for older Python AST nodes
            return float(node.n)

        raise ValueError("Unsupported expression.")
