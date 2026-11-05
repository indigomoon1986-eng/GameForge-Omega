"""Proprietary Leakean Godot Engine.

Full research-oriented Godot 4 adapter with:
- Complete project skeleton (project.godot, main.tscn, main.gd)
- Continuity Tensor Ξ research proxy
- SCI score embedding
- Curvature cartridge hook
- Topological continuity markers
- Optional LeakeanPhysicsEngine integration points

Explicitly labeled experimental. Does not claim established physical force
or subjective continuity. Semantic WorldSpec remains authoritative.
"""

from __future__ import annotations
from typing import Dict, Any
from gameforge.core.worldspec import WorldSpec
from .base import EngineAdapter, EngineExport
from .godot import GodotAdapter


class LeakeanGodotAdapter(EngineAdapter):
    name = "leakean_godot"

    def __init__(self):
        self._base = GodotAdapter()

    def export(self, spec: WorldSpec) -> EngineExport:
        base = self._base.export(spec)
        descriptor = base.descriptor.copy()
        descriptor["engine"] = "leakean_godot"
        descriptor["version"] = "4.x-leakean"
        descriptor["leakean"] = {
            "experimental": True,
            "continuity_tensor_enabled": False,
            "sci_embedding": "optional",
            "curvature_cartridge": "experimental_physics",
            "physics_module": "gameforge.physics.leakean.LeakeanPhysicsEngine",
            "notes": (
                "Leakean extensions are research-only. Continuity Tensor Ξ and SCI "
                "are computational metrics, not claims of subjective survival or "
                "established physical force. Creator must authorize experimental cartridges."
            ),
            "topology_markers": [
                {"entity": e.id, "knot_class": "S1_embed" if e.type == "portal" else "trivial"}
                for e in spec.entities
            ],
        }
        descriptor["files"] = {
            "project.godot": self._project_file(spec),
            "main.tscn": self._scene_file(),
            "scripts/main.gd": self._main_script(spec),
        }
        return EngineExport(
            engine=self.name,
            title=spec.title,
            descriptor=descriptor,
            notes="Proprietary Leakean Godot. Full skeleton generated. Experimental physics labeled and disabled by default.",
        )

    def _project_file(self, spec: WorldSpec) -> str:
        title = spec.title.replace('"', '\\"')
        return f'''config_version=5

[application]

config/name="{title} (Leakean)"
run/main_scene="res://main.tscn"
config/features=PackedStringArray("Forward Plus")

[display]

window/size/viewport_width=1024
window/size/viewport_height=600

[leakean]

experimental=true
continuity_tensor=false
'''

    def _scene_file(self) -> str:
        return '''[gd_scene load_steps=2 format=3]

[ext_resource type="Script" path="res://scripts/main.gd" id="1_main"]

[node name="Main" type="Node2D"]
script = ExtResource("1_main")
'''

    def _main_script(self, spec: WorldSpec) -> str:
        entity_count = len(spec.entities)
        return f'''extends Node2D
# GameForge Ω Proprietary Leakean Godot
# Title: {spec.title}
# Entities: {entity_count}
# Continuity Tensor Ξ and SCI are research metrics only.

var continuity_xi := 0.0
var sci_score := 0.0

func _ready() -> void:
    print("Leakean Godot world loaded (experimental): {spec.title}")
    # Experimental cartridge must be explicitly enabled by creator
    # Integrate with LeakeanPhysicsEngine when authorized

func _process(delta: float) -> void:
    # Research proxy update (disabled until authorized)
    pass
'''
