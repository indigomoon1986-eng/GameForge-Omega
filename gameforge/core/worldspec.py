"""Typed WorldSpec — the semantic source of truth for a GameForge world."""

from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
import hashlib
import json


class Entity(BaseModel):
    id: str
    type: str  # player, npc, collectible, portal, obstacle, etc.
    position: List[float] = Field(default_factory=lambda: [0.0, 0.0])
    properties: Dict[str, Any] = Field(default_factory=dict)


class Rule(BaseModel):
    id: str
    condition: str
    action: str
    priority: int = 0


class WorldSpec(BaseModel):
    """Canonical description of a programmable world."""
    title: str = "Untitled World"
    author: str = "creator"
    entities: List[Entity] = Field(default_factory=list)
    rules: List[Rule] = Field(default_factory=list)
    objectives: List[str] = Field(default_factory=list)
    win_condition: Optional[str] = None
    lose_condition: Optional[str] = None
    cartridges: List[str] = Field(default_factory=lambda: ["render", "movement", "objectives"])
    provenance: Optional[str] = None

    def compute_hash(self) -> str:
        payload = json.dumps(self.model_dump(), sort_keys=True).encode()
        return hashlib.sha256(payload).hexdigest()

    def to_json(self) -> str:
        return self.model_dump_json(indent=2)
