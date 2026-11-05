"""WorldSpec validation and policy checks.

Enforces basic integrity, sovereignty constraints, and cartridge compatibility.
"""

from __future__ import annotations
from typing import List
from pydantic import BaseModel
from .worldspec import WorldSpec


class ValidationResult(BaseModel):
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


def validate_worldspec(spec: WorldSpec) -> ValidationResult:
    errors: List[str] = []
    warnings: List[str] = []

    if not spec.title or not spec.title.strip():
        errors.append("Title is required")

    ids = [e.id for e in spec.entities]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate entity ids")

    if not any(e.type == "player" for e in spec.entities):
        warnings.append("No player entity defined")

    if "experimental_physics" in spec.cartridges:
        warnings.append("Experimental physics cartridge is labeled and does not claim established physical force")

    if not spec.objectives and not spec.win_condition:
        warnings.append("No objectives or win condition")

    return ValidationResult(valid=len(errors) == 0, errors=errors, warnings=warnings)
