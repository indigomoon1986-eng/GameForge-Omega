"""Unreal Engine 5 adapter.

Contract-first descriptor for UE5 projects.
Does not generate full .uproject files; preserves semantic world for later plugin or editor import.
Adapted from earlier monoreality UE5 adapter patterns.
"""

from __future__ import annotations
from typing import Dict, Any
from gameforge.core.worldspec import WorldSpec
from .base import EngineAdapter, EngineExport


class UnrealAdapter(EngineAdapter):
    name = "unreal"

    def export(self, spec: WorldSpec) -> EngineExport:
        descriptor = {
            "engine": "unreal",
            "version": "5.x",
            "title": spec.title,
            "features": ["Nanite", "Lumen"],
            "actors": [
                {
                    "name": e.id,
                    "class": self._map_type(e.type),
                    "location": e.position,
                    "properties": e.properties,
                }
                for e in spec.entities
            ],
            "objectives": spec.objectives,
            "win_condition": spec.win_condition,
            "cartridges": spec.cartridges,
            "notes": "UE5 actor mapping. Full .uproject / Blueprint generation is future work.",
        }
        return EngineExport(
            engine=self.name,
            title=spec.title,
            descriptor=descriptor,
        )

    def _map_type(self, entity_type: str) -> str:
        mapping = {
            "player": "Character",
            "npc": "AIController + Character",
            "collectible": "StaticMeshActor",
            "portal": "TriggerVolume",
            "enemy": "AICharacter",
        }
        return mapping.get(entity_type, "Actor")
