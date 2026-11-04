"""Sophia Game Planner stub.

Proposes WorldSpec modifications. Creator must authorize before application.
Does not call an external model; uses deterministic rules for research scaffolding.
"""

from __future__ import annotations
from typing import List
from pydantic import BaseModel
from gameforge.core.worldspec import WorldSpec, Entity
from gameforge.core.prompt import PromptTranslator


class Proposal(BaseModel):
    description: str
    spec: WorldSpec
    authorized: bool = False


class SophiaPlanner:
    def __init__(self):
        self.translator = PromptTranslator()

    def propose(self, prompt: str, base: WorldSpec | None = None) -> Proposal:
        """Generate a proposed WorldSpec from a prompt."""
        proposed = self.translator.translate(prompt, title=(base.title if base else "Proposed World"))
        if base:
            # merge entities by id
            existing = {e.id: e for e in base.entities}
            for e in proposed.entities:
                existing[e.id] = e
            proposed.entities = list(existing.values())
            proposed.objectives = list(set(base.objectives + proposed.objectives))
        return Proposal(
            description=f"Proposed changes from: {prompt[:80]}",
            spec=proposed,
        )

    def authorize(self, proposal: Proposal) -> WorldSpec:
        """Creator authorizes the proposal."""
        proposal.authorized = True
        return proposal.spec
