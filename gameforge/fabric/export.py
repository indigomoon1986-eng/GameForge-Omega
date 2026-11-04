"""Export adapters for GameForge worlds.

Produces descriptors suitable for browser, Godot, or other targets.
Does not generate full engine projects; provides structured hand-off.
"""

from __future__ import annotations
from typing import Dict, Any
from gameforge.core.worldspec import WorldSpec
import json


class ExportAdapter:
    def to_web(self, spec: WorldSpec) -> Dict[str, Any]:
        return {
            "engine": "web",
            "title": spec.title,
            "entities": [e.model_dump() for e in spec.entities],
            "objectives": spec.objectives,
            "win": spec.win_condition,
            "cartridges": spec.cartridges,
        }

    def to_godot_descriptor(self, spec: WorldSpec) -> str:
        """Minimal Godot project descriptor (not a full .godot file)."""
        lines = [
            f"; GameForge Ω export for {spec.title}",
            "[application]",
            f'config/name="{spec.title}"',
            "run/main_scene=\"res://main.tscn\"",
            "",
            "; Entities",
        ]
        for e in spec.entities:
            lines.append(f"; {e.type}:{e.id} @ {e.position}")
        return "\n".join(lines)

    def to_json(self, spec: WorldSpec, target: str = "web") -> str:
        if target == "web":
            return json.dumps(self.to_web(spec), indent=2)
        return json.dumps({"godot_descriptor": self.to_godot_descriptor(spec)}, indent=2)
