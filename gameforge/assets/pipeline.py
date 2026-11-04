"""Simple asset registry and pipeline.

Tracks meshes, materials, audio, and other resources by hash and provenance.
"""

from __future__ import annotations
from typing import Dict, Optional
from pydantic import BaseModel, Field
import hashlib


class Asset(BaseModel):
    id: str
    type: str  # mesh, material, audio, texture, script
    uri: str
    hash: str = ""
    provenance: Optional[str] = None


class AssetPipeline:
    def __init__(self):
        self.assets: Dict[str, Asset] = {}

    def register(self, asset_id: str, asset_type: str, uri: str, content: bytes | None = None) -> Asset:
        h = hashlib.sha256(content).hexdigest() if content else ""
        asset = Asset(id=asset_id, type=asset_type, uri=uri, hash=h)
        self.assets[asset_id] = asset
        return asset

    def get(self, asset_id: str) -> Optional[Asset]:
        return self.assets.get(asset_id)

    def list_by_type(self, asset_type: str) -> list[Asset]:
        return [a for a in self.assets.values() if a.type == asset_type]
