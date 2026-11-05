"""Base types for engine integration."""

from __future__ import annotations
from typing import Any, Dict
from pydantic import BaseModel
from gameforge.core.worldspec import WorldSpec


class EngineExport(BaseModel):
    engine: str
    title: str
    descriptor: Dict[str, Any]
    notes: str = "Semantic world preserved. Full project generation is optional."


class EngineAdapter:
    """Abstract adapter. Subclasses implement export."""

    name: str = "base"

    def export(self, spec: WorldSpec) -> EngineExport:
        raise NotImplementedError
