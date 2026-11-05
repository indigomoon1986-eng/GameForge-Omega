"""Game engine integration for GameForge Ω.

The semantic WorldSpec is the source of truth.
Engines are views and export targets.
"""

from .base import EngineAdapter, EngineExport
from .godot import GodotAdapter
from .unreal import UnrealAdapter
from .registry import EngineRegistry

__all__ = ["EngineAdapter", "EngineExport", "GodotAdapter", "UnrealAdapter", "EngineRegistry"]
