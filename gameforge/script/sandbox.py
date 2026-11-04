"""Restricted script execution for GameForge behaviors.

Generated scripts run in a limited environment. Creator authorizes changes.
"""

from __future__ import annotations
from typing import Any, Dict
import ast


class ScriptSandbox:
    """Very restricted evaluator for simple expressions and safe builtins."""

    SAFE_NAMES = {
        "abs": abs, "min": min, "max": max, "round": round,
        "True": True, "False": False, "None": None,
    }

    def evaluate(self, expression: str, context: Dict[str, Any] | None = None) -> Any:
        """Evaluate a simple arithmetic or comparison expression."""
        tree = ast.parse(expression, mode="eval")
        return self._eval(tree.body, context or {})

    def _eval(self, node: ast.AST, ctx: Dict[str, Any]) -> Any:
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            if node.id in ctx:
                return ctx[node.id]
            if node.id in self.SAFE_NAMES:
                return self.SAFE_NAMES[node.id]
            raise ValueError(f"Name not allowed: {node.id}")
        if isinstance(node, ast.BinOp):
            left = self._eval(node.left, ctx)
            right = self._eval(node.right, ctx)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                return left / right
        if isinstance(node, ast.Compare):
            left = self._eval(node.left, ctx)
            for op, comparator in zip(node.ops, node.comparators):
                right = self._eval(comparator, ctx)
                if isinstance(op, ast.Gt) and not (left > right):
                    return False
                if isinstance(op, ast.Lt) and not (left < right):
                    return False
                if isinstance(op, ast.Eq) and not (left == right):
                    return False
                left = right
            return True
        raise ValueError("Expression not allowed in sandbox")
