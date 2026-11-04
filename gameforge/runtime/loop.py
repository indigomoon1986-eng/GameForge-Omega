"""Deterministic simulation loop for GameForge worlds.

Fixed timestep, event queue, action resolution.
"""

from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional
from pydantic import BaseModel
from gameforge.core.worldspec import WorldSpec
import time


class TickResult(BaseModel):
    tick: int
    dt: float
    events: List[dict] = []
    state_hash: Optional[str] = None


class WorldRuntime:
    """Authoritative deterministic runtime."""

    def __init__(self, spec: WorldSpec, tick_rate: float = 60.0):
        self.spec = spec
        self.tick_rate = tick_rate
        self.tick = 0
        self.events: List[dict] = []
        self.handlers: Dict[str, Callable] = {}
        self.start_time = time.time()

    def on(self, event_type: str, handler: Callable) -> None:
        self.handlers[event_type] = handler

    def emit(self, event_type: str, payload: dict) -> None:
        ev = {"type": event_type, "tick": self.tick, **payload}
        self.events.append(ev)
        if event_type in self.handlers:
            self.handlers[event_type](ev)

    def step(self, dt: Optional[float] = None) -> TickResult:
        if dt is None:
            dt = 1.0 / self.tick_rate
        self.tick += 1
        # simple objective check proxy
        if self.spec.win_condition and self.tick > 100:
            self.emit("objective", {"status": "check"})
        return TickResult(tick=self.tick, dt=dt, events=self.events[-5:])

    def run(self, steps: int = 10) -> List[TickResult]:
        return [self.step() for _ in range(steps)]
