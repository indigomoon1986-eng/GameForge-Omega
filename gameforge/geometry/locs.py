"""LOCS — Lightweight geometric and topological primitives for world compilation.

Research scaffolding. Does not claim physical force.
"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel
import math


class LOCSPoint(BaseModel):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    label: str = ""

    def distance_to(self, other: "LOCSPoint") -> float:
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2 + (self.z-other.z)**2)


class SpatialRelation(BaseModel):
    subject: str
    predicate: str  # near, contains, connects, etc.
    object: str
    strength: float = 1.0


def procedural_terrain_seed(seed: int, width: int = 64, height: int = 64) -> List[List[float]]:
    """Simple heightmap proxy for procedural terrain."""
    import random
    rng = random.Random(seed)
    return [[rng.random() for _ in range(width)] for _ in range(height)]
