"""SENTIUM-backed NPC agent for GameForge.

Research scaffolding. Does not claim machine consciousness.
"""

from __future__ import annotations
from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Goal(str, Enum):
    IDLE = "idle"
    PATROL = "patrol"
    PURSUE = "pursue"
    INTERACT = "interact"
    FLEE = "flee"


class NPCState(BaseModel):
    id: str
    name: str = "NPC"
    goal: Goal = Goal.IDLE
    memory: List[str] = Field(default_factory=list)
    position: List[float] = Field(default_factory=lambda: [0.0, 0.0])
    dialogue: Optional[str] = None

    def remember(self, event: str) -> None:
        self.memory.append(event)
        if len(self.memory) > 50:
            self.memory = self.memory[-50:]

    def step(self, world_context: Dict) -> str:
        """Simple behavior step. Returns action description."""
        if self.goal == Goal.PATROL:
            return "moving along path"
        if self.goal == Goal.PURSUE:
            return "pursuing target"
        return "idle"
