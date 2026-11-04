"""World persistence and branching for long-horizon worlds.

Append-only history with optional branching. Creator retains ownership.
"""

from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import hashlib
import json
import time


class Branch(BaseModel):
    id: str
    parent: Optional[str] = None
    timestamp: float = Field(default_factory=time.time)
    world_hash: str = ""
    note: str = ""


class WorldVault:
    """Local-first vault for world snapshots and branches."""

    def __init__(self):
        self.snapshots: Dict[str, dict] = {}
        self.branches: List[Branch] = []

    def save(self, world: dict, note: str = "", parent: Optional[str] = None) -> str:
        payload = json.dumps(world, sort_keys=True).encode()
        h = hashlib.sha256(payload).hexdigest()
        self.snapshots[h] = world
        branch = Branch(id=h[:12], parent=parent, world_hash=h, note=note)
        self.branches.append(branch)
        return h

    def load(self, world_hash: str) -> Optional[dict]:
        return self.snapshots.get(world_hash)

    def history(self) -> List[Branch]:
        return list(self.branches)
