# GameForge Ω Roadmap

| Release | Deliverable | Status |
|---------|-------------|--------|
| **0.1 — Alpha** | Standalone browser Studio: prompt → playable, four panes, JSON import/export | **Done** |
| **0.2 — Forge3D** | Three.js viewport, camera, meshes, lighting, terrain proxy | **Done** |
| **0.3 — ForgeMind** | SENTIUM NPCs, memory, dialogue, goals | **Done** |
| **0.4 — ForgePhysics** | Rigid-body, collision + experimental adapter (labeled) | **Done** |
| **0.5 — ForgeScript** | Typed scripting, sandboxed execution | **Done** |
| **0.6 — ForgeCinema** | Timeline, keyframes | **Done** |
| **0.7 — ForgeWorlds** | Persistent worlds, branching histories | **Done** |
| **1.0 — Creator Platform** | Asset pipeline, builds, publishing, validation, CLI, cartridges, runtime, Sophia planner, XR stub, export | **Scaffolded / E2** |

## Reference Demonstration

**Carolina Valley** — `examples/carolina_valley.py`  
Explorable environment with interactive objects, intelligent NPCs, a quest, and persistent state.

## Architectural Invariant

**GameForge owns the semantic world, not the renderer.**

Graphics can improve independently. Worlds compile to other engines. Sophia remains a co-architect under creator authorization. Experimental physics is explicitly labeled.

## Maturity

Current state is a coherent **E2-level creator platform foundation**:

- All seven native systems have runnable modules.
- Deterministic runtime, MR7 cartridges, Sophia planner (authorization required), validation, CLI, asset pipeline, export adapters (web + Godot skeleton), multiplayer stub, publishing catalog, XR stub, and dialogue trees exist.
- Two browser prototypes and a reference world build cleanly.
- Tests and CI are in place.

Full production features (connected external Sophia model, production networking, marketplace UI, full WebXR, complete Godot/Unreal project generation, WebGPU path) remain future work.
