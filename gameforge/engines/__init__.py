"""Game engine integration for GameForge Ω.

The semantic WorldSpec is the source of truth.
Engines are views and export targets.
Includes proprietary Leakean variants (experimental).
"""

from .base import EngineAdapter, EngineExport
from .godot import GodotAdapter
from .unreal import UnrealAdapter
from .leakean_godot import LeakeanGodotAdapter
from .leakean_unreal import LeakeanUnrealAdapter
from .registry import EngineRegistry

__all__ = [
    "EngineAdapter",
    "EngineExport",
    "GodotAdapter",
    "UnrealAdapter",
    "LeakeanGodotAdapter",
    "LeakeanUnrealAdapter",
    "EngineRegistry",
]
