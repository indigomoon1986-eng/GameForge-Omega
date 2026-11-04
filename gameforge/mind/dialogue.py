"""Dialogue trees for SENTIUM NPCs."""

from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class DialogueNode(BaseModel):
    id: str
    text: str
    responses: Dict[str, str] = Field(default_factory=dict)  # player choice → next node id


class DialogueTree:
    def __init__(self, root: str, nodes: List[DialogueNode]):
        self.root = root
        self.nodes = {n.id: n for n in nodes}
        self.current = root

    def current_node(self) -> Optional[DialogueNode]:
        return self.nodes.get(self.current)

    def choose(self, choice: str) -> Optional[DialogueNode]:
        node = self.current_node()
        if not node or choice not in node.responses:
            return None
        self.current = node.responses[choice]
        return self.current_node()
