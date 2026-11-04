"""Cartridge registry for modular world loading.

Worlds declare required cartridges instead of loading the full ecosystem.
"""

from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Cartridge(BaseModel):
    name: str
    description: str = ""
    dependencies: List[str] = Field(default_factory=list)
    experimental: bool = False


class CartridgeRegistry:
    def __init__(self):
        self.available: Dict[str, Cartridge] = {}

    def register(self, cart: Cartridge) -> None:
        self.available[cart.name] = cart

    def resolve(self, requested: List[str]) -> List[Cartridge]:
        """Return ordered list of cartridges including dependencies."""
        resolved: Dict[str, Cartridge] = {}

        def add(name: str):
            if name in resolved or name not in self.available:
                return
            cart = self.available[name]
            for dep in cart.dependencies:
                add(dep)
            resolved[name] = cart

        for name in requested:
            add(name)
        return list(resolved.values())

    def defaults(self) -> None:
        """Register common cartridges."""
        for name, desc in [
            ("render", "Browser rendering"),
            ("movement", "Player and NPC movement"),
            ("objectives", "Win/loss and quest tracking"),
            ("npc", "SENTIUM agent support"),
            ("physics", "Rigid-body collision"),
            ("cinema", "Timeline and keyframes"),
            ("experimental_physics", "Optional Leakean simulation"),
        ]:
            self.register(Cartridge(
                name=name,
                description=desc,
                experimental=(name == "experimental_physics"),
            ))
