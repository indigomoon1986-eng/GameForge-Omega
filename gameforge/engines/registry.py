"""Registry of available engine adapters."""

from __future__ import annotations
from typing import Dict
from .base import EngineAdapter
from .godot import GodotAdapter
from .unreal import UnrealAdapter


class EngineRegistry:
    def __init__(self):
        self.adapters: Dict[str, EngineAdapter] = {
            "godot": GodotAdapter(),
            "unreal": UnrealAdapter(),
        }

    def get(self, name: str) -> EngineAdapter:
        if name not in self.adapters:
            raise ValueError(f"Unknown engine: {name}. Available: {list(self.adapters)}")
        return self.adapters[name]

    def list(self) -> list[str]:
        return list(self.adapters.keys())
