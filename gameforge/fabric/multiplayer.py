"""Multiplayer session stub for GameForge worlds.

Local-first, authoritative world with optional client replicas.
Not a full networking stack.
"""

from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
import time


class ClientReplica(BaseModel):
    client_id: str
    last_seen: float = Field(default_factory=time.time)
    position: List[float] = Field(default_factory=lambda: [0.0, 0.0])


class Session:
    """Authoritative session holding world state and client replicas."""

    def __init__(self, world_hash: str):
        self.world_hash = world_hash
        self.clients: Dict[str, ClientReplica] = {}
        self.events: List[dict] = []

    def join(self, client_id: str) -> ClientReplica:
        replica = ClientReplica(client_id=client_id)
        self.clients[client_id] = replica
        self.events.append({"type": "join", "client": client_id, "t": time.time()})
        return replica

    def leave(self, client_id: str) -> None:
        self.clients.pop(client_id, None)
        self.events.append({"type": "leave", "client": client_id, "t": time.time()})

    def update_position(self, client_id: str, pos: List[float]) -> None:
        if client_id in self.clients:
            self.clients[client_id].position = pos
            self.clients[client_id].last_seen = time.time()

    def snapshot(self) -> dict:
        return {
            "world_hash": self.world_hash,
            "clients": {cid: c.model_dump() for cid, c in self.clients.items()},
            "event_count": len(self.events),
        }
