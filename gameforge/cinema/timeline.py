"""Simple timeline and keyframe system for cinematic authoring."""

from __future__ import annotations
from typing import Any, Dict, List
from pydantic import BaseModel, Field


class Keyframe(BaseModel):
    time: float
    property: str
    value: Any


class Timeline(BaseModel):
    name: str = "main"
    keyframes: List[Keyframe] = Field(default_factory=list)
    duration: float = 10.0

    def add_keyframe(self, time: float, prop: str, value: Any) -> None:
        self.keyframes.append(Keyframe(time=time, property=prop, value=value))
        self.keyframes.sort(key=lambda k: k.time)

    def sample(self, t: float) -> Dict[str, Any]:
        """Return interpolated property values at time t (linear between keys)."""
        result: Dict[str, Any] = {}
        props = {k.property for k in self.keyframes}
        for prop in props:
            keys = [k for k in self.keyframes if k.property == prop]
            if not keys:
                continue
            if t <= keys[0].time:
                result[prop] = keys[0].value
                continue
            if t >= keys[-1].time:
                result[prop] = keys[-1].value
                continue
            for i in range(len(keys)-1):
                if keys[i].time <= t <= keys[i+1].time:
                    # linear if numeric
                    a, b = keys[i].value, keys[i+1].value
                    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                        alpha = (t - keys[i].time) / (keys[i+1].time - keys[i].time)
                        result[prop] = a + (b - a) * alpha
                    else:
                        result[prop] = a
                    break
        return result
