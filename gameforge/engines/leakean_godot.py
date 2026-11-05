"""Proprietary Leakean Godot adapter.

Extends Godot 4 with experimental Leakean physics features:
- Continuity Tensor Ξ (research)
- SCI score embedding
- Curvature-influenced spatial reasoning
- Topological continuity markers

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
        base_export = self._base.export(spec)
        descriptor = base_export.descriptor.copy()
        descriptor["engine"] = "leakean_godot"
        descriptor["leakean"] = {
            "experimental": True,
            "continuity_tensor_enabled": False,
            "sci_embedding": "optional",
            "curvature_cartridge": "experimental_physics",
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
        descriptor["main_gd_snippet"] = self._leakean_snippet(spec)
        return EngineExport(
            engine=self.name,
            title=spec.title,
            descriptor=descriptor,
            notes="Proprietary Leakean Godot. Experimental physics labeled and disabled by default.",
        )

    def _leakean_snippet(self, spec: WorldSpec) -> str:
        return f'''extends Node2D
# GameForge Ω Leakean Godot — experimental
# Title: {spec.title}
# Entities: {len(spec.entities)}
# Continuity Tensor Ξ and SCI are research metrics only.

var continuity_xi := 0.0  # research proxy

func _ready() -> void:
    print("Leakean world loaded (experimental): {spec.title}")
    # Experimental cartridge must be explicitly enabled by creator
'''
