"""World compilation and build manifest for GameForge Fabric.

Produces browser-ready or export-ready packages from WorldSpec.
"""

from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel, Field
from gameforge.core.worldspec import WorldSpec
import hashlib
import json


class BuildManifest(BaseModel):
    title: str
    world_hash: str
    cartridges: List[str] = Field(default_factory=list)
    target: str = "web"
    version: str = "0.1.0-alpha"
    provenance: Optional[str] = None


class WorldBuilder:
    """Compile a WorldSpec into a buildable package descriptor."""

    def build(self, spec: WorldSpec, target: str = "web") -> BuildManifest:
        payload = json.dumps(spec.model_dump(), sort_keys=True).encode()
        h = hashlib.sha256(payload).hexdigest()
        return BuildManifest(
            title=spec.title,
            world_hash=h,
            cartridges=spec.cartridges,
            target=target,
            provenance=spec.provenance,
        )

    def export_json(self, manifest: BuildManifest) -> str:
        return manifest.model_dump_json(indent=2)
