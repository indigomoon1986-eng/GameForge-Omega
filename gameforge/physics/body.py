"""Simple rigid-body and collision for GameForge runtime.

Experimental Leakean simulation is optional and must be explicitly enabled.
"""

from __future__ import annotations
from typing import List
from pydantic import BaseModel
import math


class RigidBody(BaseModel):
    id: str
    x: float = 0.0
    y: float = 0.0
    vx: float = 0.0
    vy: float = 0.0
    radius: float = 1.0
    mass: float = 1.0

    def step(self, dt: float = 0.016) -> None:
        self.x += self.vx * dt
        self.y += self.vy * dt


class PhysicsWorld:
    def __init__(self):
        self.bodies: List[RigidBody] = []

    def add(self, body: RigidBody) -> None:
        self.bodies.append(body)

    def step(self, dt: float = 0.016) -> None:
        for b in self.bodies:
            b.step(dt)
        # simple pairwise collision (elastic bounce proxy)
        for i, a in enumerate(self.bodies):
            for b in self.bodies[i+1:]:
                dx = b.x - a.x
                dy = b.y - a.y
                dist = math.hypot(dx, dy)
                min_dist = a.radius + b.radius
                if dist < min_dist and dist > 1e-6:
                    # push apart
                    overlap = min_dist - dist
                    nx, ny = dx/dist, dy/dist
                    a.x -= nx * overlap * 0.5
                    a.y -= ny * overlap * 0.5
                    b.x += nx * overlap * 0.5
                    b.y += ny * overlap * 0.5
                    # reverse velocities roughly
                    a.vx, b.vx = -a.vx * 0.8, -b.vx * 0.8
                    a.vy, b.vy = -a.vy * 0.8, -b.vy * 0.8
