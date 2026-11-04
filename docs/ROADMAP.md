# GameForge Ω Roadmap

| Release | Deliverable | Status |
|---------|-------------|--------|
| **0.1 — Alpha** | Standalone browser Studio: prompt → playable, four panes, JSON import/export | **Done** |
| 0.2 — Forge3D | Three.js/WebGPU viewport, camera, meshes, lighting, terrain | Planned |
| 0.3 — ForgeMind | SENTIUM NPC state machines, memory, dialogue, goals | Scaffolded |
| 0.4 — ForgePhysics | Rigid-body, collision, LOCS geometric adapter | Planned |
| 0.5 — ForgeScript | Typed scripting, hot reload, visual nodes, sandbox | Planned |
| 0.6 — ForgeCinema | Timeline, keyframes, cameras, sound, cinematic export | Planned |
| 0.7 — ForgeWorlds | Persistent worlds, branching histories, MR7 cartridges, multiplayer | Planned |
| **1.0 — Creator Platform** | Asset pipeline, builds, testing, publishing, marketplace, creator ownership | Planned |

## Reference Demonstration

**Carolina Valley** — visually rich, playable world with explorable environment, interactive objects, intelligent NPCs, a quest, dynamic weather, and persistent state.

Serves as reference for Young Realms of Becoming, GameForge creator SaaS, and MonoReality scientific sandboxes.

## Architectural Invariant

Protect throughout development: **GameForge owns the semantic world, not the renderer.**
