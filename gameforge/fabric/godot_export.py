"""Enhanced Godot export descriptor for GameForge worlds.

Produces a structured project skeleton description suitable for later compilation.
Not a full Godot project generator.
"""

from __future__ import annotations
from typing import Dict, Any
from gameforge.core.worldspec import WorldSpec
import json


def to_godot_skeleton(spec: WorldSpec) -> Dict[str, Any]:
    """Return a skeleton description of a Godot project."""
    return {
        "engine": "godot",
        "version": "4.x",
        "title": spec.title,
        "main_scene": "res://main.tscn",
        "entities": [
            {
                "id": e.id,
                "type": e.type,
                "position": e.position,
                "properties": e.properties,
            }
            for e in spec.entities
        ],
        "objectives": spec.objectives,
        "win_condition": spec.win_condition,
        "cartridges": spec.cartridges,
        "notes": "Semantic world preserved. Full project generation is future work.",
    }


def to_godot_json(spec: WorldSpec) -> str:
    return json.dumps(to_godot_skeleton(spec), indent=2)
