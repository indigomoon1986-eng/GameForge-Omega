"""Experimental Leakean physics adapter.

Explicitly labeled research component. Does not claim established physical force.
Optional cartridge only.
"""

from __future__ import annotations
from typing import List
from pydantic import BaseModel
import math


class ExperimentalBody(BaseModel):
    id: str
    x: float = 0.0
    y: float = 0.0
    curvature: float = 0.0  # research parameter only


class ExperimentalPhysics:
    """Placeholder for optional geometric influence. Research only."""

    def __init__(self):
        self.bodies: List[ExperimentalBody] = []
        self.enabled: bool = False

    def enable(self) -> None:
        """Must be explicitly enabled."""
        self.enabled = True

    def add(self, body: ExperimentalBody) -> None:
        self.bodies.append(body)

    def step(self, dt: float = 0.016) -> None:
        if not self.enabled:
            return
        # simple research proxy: slight radial adjustment based on curvature label
        for b in self.bodies:
            r = math.hypot(b.x, b.y) or 1.0
            factor = 1.0 + b.curvature * 0.01 * dt
            b.x *= factor
            b.y *= factor
