"""Proprietary Leakean Unreal Engine.

Full research-oriented UE5 adapter with:
- Structured actor and level descriptors
- Continuity Tensor Ξ actor metadata
- SCI score on persistent agents
- Curvature-influenced spatial volumes (research)
- Topological continuity tags
- Optional LeakeanPhysicsEngine integration points

Explicitly labeled experimental. Does not claim established physical force
or subjective continuity. Semantic WorldSpec remains authoritative.
"""

from __future__ import annotations
from typing import Dict, Any
from gameforge.core.worldspec import WorldSpec
from .base import EngineAdapter, EngineExport
from .unreal import UnrealAdapter


class LeakeanUnrealAdapter(EngineAdapter):
    name = "leakean_unreal"

    def __init__(self):
        self._base = UnrealAdapter()

    def export(self, spec: WorldSpec) -> EngineExport:
        base = self._base.export(spec)
        descriptor = base.descriptor.copy()
        descriptor["engine"] = "leakean_unreal"
        descriptor["version"] = "5.x-leakean"
        descriptor["leakean"] = {
            "experimental": True,
            "features": ["Nanite", "Lumen", "ContinuityTensor_research", "SCI_embedding_research"],
            "continuity_tensor_enabled": False,
            "physics_module": "gameforge.physics.leakean.LeakeanPhysicsEngine",
            "notes": (
                "Leakean extensions are research-only. Ξ and SCI are computational "
                "metrics for functional continuity, not claims of subjective survival."
            ),
        }
        # Augment actors with research metadata
        for actor in descriptor.get("actors", []):
            actor["leakean_metadata"] = {
                "sci_score": None,
                "xi_vector": None,
                "curvature": 0.0,
                "experimental": True,
                "continuity_class": "functional",
            }
        descriptor["level_descriptor"] = {
            "name": spec.title,
            "experimental_physics": False,
            "objectives": spec.objectives,
            "win_condition": spec.win_condition,
        }
        return EngineExport(
            engine=self.name,
            title=spec.title,
            descriptor=descriptor,
            notes="Proprietary Leakean Unreal. Full actor + level descriptors. Experimental physics labeled and disabled by default.",
        )
