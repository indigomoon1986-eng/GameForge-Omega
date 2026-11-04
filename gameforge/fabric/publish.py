"""Publishing and marketplace descriptors for creator-owned worlds.

Creator retains ownership. No coercive extraction.
"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from gameforge.core.worldspec import WorldSpec
import hashlib
import json


class PublishRecord(BaseModel):
    title: str
    author: str
    world_hash: str
    version: str = "0.1.0"
    tags: List[str] = Field(default_factory=list)
    license: str = "creator-owned"
    public: bool = False


class Marketplace:
    """Local catalog of published worlds."""

    def __init__(self):
        self.records: Dict[str, PublishRecord] = {}

    def publish(self, spec: WorldSpec, public: bool = False, tags: Optional[List[str]] = None) -> PublishRecord:
        payload = json.dumps(spec.model_dump(), sort_keys=True).encode()
        h = hashlib.sha256(payload).hexdigest()
        rec = PublishRecord(
            title=spec.title,
            author=spec.author,
            world_hash=h,
            tags=tags or [],
            public=public,
        )
        self.records[h] = rec
        return rec

    def list_public(self) -> List[PublishRecord]:
        return [r for r in self.records.values() if r.public]
