# GameForge Ω Roadmap

| Release | Deliverable | Status |
|---------|-------------|--------|
| **0.1 — Alpha** | Standalone browser Studio: prompt → playable, four panes, JSON import/export | **Done** |
| **0.2 — Forge3D** | Three.js viewport, camera, meshes, lighting, terrain proxy | **Done** (`alpha/forge3d.html`) |
| **0.3 — ForgeMind** | SENTIUM NPC state machines, memory, dialogue, goals | **Scaffolded** (`gameforge/mind/`) |
| **0.4 — ForgePhysics** | Rigid-body, collision | **Done** (`gameforge/physics/`) |
| **0.5 — ForgeScript** | Typed scripting, sandboxed execution | **Done** (`gameforge/script/`) |
| **0.6 — ForgeCinema** | Timeline, keyframes | **Done** (`gameforge/cinema/`) |
| **0.7 — ForgeWorlds** | Persistent worlds, branching histories | **Done** (`gameforge/worlds/`) |
| **1.0 — Creator Platform** | Asset pipeline, builds, publishing descriptors, creator ownership | **Scaffolded** (`gameforge/fabric/`) |

## Reference Demonstration

**Carolina Valley** — `examples/carolina_valley.py`  
Explorable environment with interactive objects, intelligent NPCs, a quest, and persistent state.

Serves as reference for Young Realms of Becoming, GameForge creator SaaS, and MonoReality scientific sandboxes.

## Architectural Invariant

**GameForge owns the semantic world, not the renderer.**

Graphics can improve independently. Worlds compile to other engines. Sophia remains a co-architect under creator authorization.

## Maturity

Current state is a coherent E2-level creator platform foundation: all seven native systems have runnable modules, two browser prototypes exist, and the reference world builds cleanly.

Full production features (multiplayer, marketplace, WebGPU path, Godot/Unreal export, connected Sophia model) remain future work.
