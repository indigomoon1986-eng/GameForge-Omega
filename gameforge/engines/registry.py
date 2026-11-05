"""Registry of available engine adapters.

Includes proprietary Leakean variants (experimental).
"""

from __future__ import annotations
from typing import Dict
from .base import EngineAdapter
from .godot import GodotAdapter
from .unreal import UnrealAdapter
from .leakean_godot import LeakeanGodotAdapter
from .leakean_unreal import LeakeanUnrealAdapter


class EngineRegistry:
    def __init__(self):
        self.adapters: Dict[str, EngineAdapter] = {
            "godot": GodotAdapter(),
            "unreal": UnrealAdapter(),
            "leakean_godot": LeakeanGodotAdapter(),
            "leakean_unreal": LeakeanUnrealAdapter(),
        }

    def get(self, name: str) -> EngineAdapter:
        if name not in self.adapters:
            raise ValueError(f"Unknown engine: {name}. Available: {list(self.adapters)}")
        return self.adapters[name]

    def list(self) -> list[str]:
        return list(self.adapters.keys())
