"""Carolina Valley — Reference demonstration world for GameForge Ω.

Explorable environment with interactive objects, intelligent NPCs, a quest,
and persistent state. Serves Young Realms, creator SaaS, and scientific sandboxes.
"""

from gameforge.core.worldspec import WorldSpec, Entity, Rule
from gameforge.mind.npc import NPCState, Goal
from gameforge.fabric.builder import WorldBuilder


def build_carolina_valley() -> WorldSpec:
    return WorldSpec(
        title="Carolina Valley",
        author="Steven Craig Leake Jr.",
        entities=[
            Entity(id="player", type="player", position=[0, 0, 0]),
            Entity(id="guide", type="npc", position=[5, 0, 3], properties={"name": "Valley Guide"}),
            Entity(id="well", type="interactive", position=[-2, 0, 4]),
            Entity(id="portal", type="portal", position=[12, 0, -6]),
            Entity(id="tree_grove", type="terrain", position=[0, 0, 8]),
        ],
        rules=[
            Rule(id="quest_start", condition="near guide", action="offer_quest"),
            Rule(id="win", condition="reach portal after quest", action="complete"),
        ],
        objectives=["Speak with the Valley Guide", "Gather water from the well", "Reach the portal"],
        win_condition="portal reached with quest items",
        cartridges=["render", "movement", "objectives", "npc", "physics"],
        provenance="reference-implementation",
    )


def main():
    spec = build_carolina_valley()
    print("Carolina Valley WorldSpec:")
    print(spec.to_json())
    print("\nHash:", spec.compute_hash()[:16], "...")

    npc = NPCState(id="guide", name="Valley Guide", goal=Goal.INTERACT)
    npc.remember("Player approached")
    print("\nNPC step:", npc.step({}))

    manifest = WorldBuilder().build(spec)
    print("\nBuild manifest:")
    print(manifest.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
