"""Godot 4 adapter.

Produces a structured project skeleton and optional minimal playable files.
Adapted from earlier GameForge MVP compiler patterns.
"""

from __future__ import annotations
from typing import Dict, Any
from gameforge.core.worldspec import WorldSpec
from .base import EngineAdapter, EngineExport
import json


class GodotAdapter(EngineAdapter):
    name = "godot"

    def export(self, spec: WorldSpec) -> EngineExport:
        descriptor = {
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
            "project_godot": self._project_file(spec),
            "main_gd_snippet": self._main_snippet(spec),
        }
        return EngineExport(
            engine=self.name,
            title=spec.title,
            descriptor=descriptor,
            notes="Godot 4 skeleton. Full project files can be written from this descriptor.",
        )

    def _project_file(self, spec: WorldSpec) -> str:
        title = spec.title.replace('"', '\\"')
        return f'''config_version=5

[application]

config/name="{title}"
run/main_scene="res://main.tscn"
config/features=PackedStringArray("Forward Plus")

[display]

window/size/viewport_width=1024
window/size/viewport_height=600
'''

    def _main_snippet(self, spec: WorldSpec) -> str:
        return f'''extends Node2D
# GameForge Ω generated for {spec.title}
# Entities: {len(spec.entities)}
# Objectives: {spec.objectives}

func _ready() -> void:
    print("World loaded: {spec.title}")
'''
