"""Prompt translator for GameForge Ω.

Converts natural-language descriptions into typed WorldSpec.
Creator authorizes the result.
"""

from __future__ import annotations
import re
from typing import List
from .worldspec import WorldSpec, Entity, Rule


class PromptTranslator:
    """Lightweight deterministic prompt → WorldSpec."""

    def translate(self, prompt: str, title: str | None = None) -> WorldSpec:
        text = (prompt or "").strip()
        if not text:
            raise ValueError("Prompt must not be empty")

        entities: List[Entity] = []
        rules: List[Rule] = []
        objectives: List[str] = []

        # Always include a player
        entities.append(Entity(id="player", type="player", position=[0.0, 0.0]))

        # Collectibles
        m = re.search(r"(\d+)\s*collectible", text, re.I)
        count = int(m.group(1)) if m else (3 if "collectible" in text.lower() else 0)
        for i in range(count):
            entities.append(Entity(id=f"c{i}", type="collectible", position=[float(i*2), 2.0]))

        # Enemy
        if re.search(r"enemy|enemies", text, re.I):
            entities.append(Entity(id="enemy", type="enemy", position=[4.0, 4.0]))

        # Portal
        if re.search(r"portal", text, re.I):
            entities.append(Entity(id="portal", type="portal", position=[8.0, 0.0]))
            objectives.append("Reach the portal")

        # NPC
        if re.search(r"npc|guide|character", text, re.I):
            entities.append(Entity(id="npc0", type="npc", position=[2.0, 2.0], properties={"name": "Guide"}))
            objectives.append("Speak with the guide")

        if count:
            objectives.append(f"Collect {count} items")

        win = "portal reached" if any(e.type == "portal" for e in entities) else "objectives complete"

        return WorldSpec(
            title=title or "Generated World",
            entities=entities,
            rules=rules,
            objectives=objectives,
            win_condition=win,
            cartridges=["render", "movement", "objectives"],
        )
