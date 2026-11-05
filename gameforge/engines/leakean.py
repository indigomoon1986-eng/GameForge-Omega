"""Unified proprietary Leakean engine interface.

Provides a single entry point for Leakean Godot and Leakean Unreal.
Experimental research components only.
"""

from __future__ import annotations
from typing import Literal
from gameforge.core.worldspec import WorldSpec
from .base import EngineExport
from .leakean_godot import LeakeanGodotAdapter
from .leakean_unreal import LeakeanUnrealAdapter


class LeakeanEngine:
    """Proprietary Leakean engine selector."""

    def __init__(self):
        self.godot = LeakeanGodotAdapter()
        self.unreal = LeakeanUnrealAdapter()

    def export(
        self,
        spec: WorldSpec,
        target: Literal["godot", "unreal"] = "godot",
    ) -> EngineExport:
        if target == "godot":
            return self.godot.export(spec)
        if target == "unreal":
            return self.unreal.export(spec)
        raise ValueError(f"Unknown Leakean target: {target}")
