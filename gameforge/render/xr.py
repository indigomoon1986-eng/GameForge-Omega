"""XR adapter stub for WebXR / LeakXR paths.

Research scaffolding. Does not implement full WebXR session management.
"""

from __future__ import annotations
from typing import Optional
from pydantic import BaseModel


class XRSessionConfig(BaseModel):
    mode: str = "immersive-vr"  # immersive-vr, immersive-ar, inline
    reference_space: str = "local-floor"
    optional_features: list[str] = []


class XRAdapter:
    """Placeholder for XR session and frame rendering."""

    def __init__(self):
        self.active: Optional[XRSessionConfig] = None

    def request(self, config: XRSessionConfig) -> bool:
        """Simulate session request. Returns True if accepted."""
        if config.mode in ("immersive-vr", "immersive-ar", "inline"):
            self.active = config
            return True
        return False

    def end(self) -> None:
        self.active = None

    def is_active(self) -> bool:
        return self.active is not None
