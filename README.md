# GameForge Ω — Sovereign World Engine

**Monarch Sovereign Systems · Game Engine & Programmable Reality Platform**

**Project:** GameForge Ω — Sovereign World Engine  
**Architect:** Steven Craig Leake Jr.  
**AI co-architect:** Sophia  
**Mission:** Build a sovereign, AI-native alternative to Unreal Engine, capable of creating games, persistent worlds, cinematic experiences, intelligent NPCs, XR environments, and scientific simulations.

> The world is the source of truth. The graphics engine is only one way of viewing it.

## Product Positioning

| Target | Differentiator |
|--------|----------------|
| **Unreal Engine 5** | High-fidelity rendering, professional editing, physics, animation, cinematics, shipping pipelines. |
| **GameForge Ω** | Semantic world graphs, natural-language authoring, programmable reality, persistent SENTIUM agents, reproducible simulation, and sovereign ownership. |

Usable creator platform foundation. Not a claim of feature parity with Unreal.

## Core Principle

GameForge owns the **semantic world**, not the renderer. This lets graphics improve independently, worlds compile to other engines, and Sophia act as a genuine world-building co-architect under creator authorization.

## Unified Architecture

```
GameForge Studio
  ↓
WorldSpec + LOCS Semantic World Graph
  ↓
Sophia + LUCA · PrimeUniScript · SENTIUM · LOCS
  ↓
Deterministic World Runtime
  ↓
WebGPU/Three.js · MR7/LeakXR · Godot/Unreal export
  ↓
Monarch Sovereign Fabric (ExaForge · Vault · Veritas Mesh · XTAX · PBA · DID)
```

### Seven Native Systems (Implemented)

| System | Responsibility | Module |
|--------|----------------|--------|
| **ForgeCore** | World state, ECS, events, prompt translator, validation | `gameforge/core/` |
| **ForgeGeometry** | LOCS topology, spatial reasoning, procedural terrain | `gameforge/geometry/` |
| **ForgeRender** | Browser graphics, materials, lighting, XR adapter | `alpha/forge3d.html`, `gameforge/render/` |
| **ForgeMind** | SENTIUM NPCs, goals, memory, dialogue trees | `gameforge/mind/` |
| **ForgePhysics** | Rigid-body, collision + experimental adapter (labeled) | `gameforge/physics/` |
| **ForgeStudio** | Editor, scripting, graph, cinematic authoring, Sophia planner | `alpha/`, `gameforge/script/`, `gameforge/cinema/`, `gameforge/sophia/` |
| **ForgeFabric** | Compilation, builds, export, multiplayer stub, publishing, assets | `gameforge/fabric/`, `gameforge/assets/` |

Additional: Deterministic runtime (`gameforge/runtime/`), MR7 cartridges (`gameforge/cartridges/`), CLI (`gameforge/cli.py`), **engine integration** (`gameforge/engines/`).

## Game Engine Integration

Semantic WorldSpec is authoritative. Engines are views:

- **Godot 4** — `GodotAdapter` produces project skeleton + main.gd snippet.
- **Unreal Engine 5** — `UnrealAdapter` produces actor descriptors (Nanite/Lumen noted).

```python
from gameforge.engines.registry import EngineRegistry
reg = EngineRegistry()
export = reg.get("godot").export(spec)  # or "unreal"
```

See `docs/ENGINE_INTEGRATION.md`.

## Creation Pipeline

Describe → Sophia Game Planner → Typed WorldSpec → Validation/XTAX → LUCA/LOCS Compiler → Runtime → Render/Play/Simulate → Observe/Decide/Act → Persist + Export.

Operating loop: **Describe → Generate → Inspect → Play → Modify → Save → Export.**

## Prototypes

- `alpha/index.html` — Studio Alpha 0.1 (top-down, prompt parser, four panes, JSON import/export).
- `alpha/forge3d.html` — Forge3D Three.js viewport with orbit controls, terrain proxy, player, collectibles, portal, NPC.

Both are local-first and require no installation.

## Reference World

```bash
python examples/carolina_valley.py
```

## CLI

```bash
python -m gameforge.cli prompt "Add a player and three collectibles and a portal"
python -m gameforge.cli validate worldspec.json
```

## Additional Capabilities

- Prompt → WorldSpec translator and Sophia planner (creator authorization required)
- WorldSpec validation with policy warnings
- Deterministic World Runtime with event handlers
- MR7 cartridge registry with dependency resolution
- Export adapters (web, Godot skeleton, Unreal actor descriptors)
- Multiplayer session stub
- Publishing / marketplace catalog
- NPC dialogue trees
- XR adapter stub
- Asset pipeline with content hashing
- Experimental physics adapter (explicitly labeled, disabled by default)
- CI workflow

See `docs/RUNTIME.md`, `docs/EXPORT_AND_PUBLISH.md`, `docs/ENGINE_INTEGRATION.md`, and `docs/ROADMAP.md`.

## Integration

Builds on earlier SophiaL-ToE-GameForge, monoreality orchestration, CIA-1 continuity concepts, Young Realms of Becoming, and SENTIUM/Sophia systems.

## Current Maturity

Coherent **E2-level creator platform foundation**. All seven native systems plus runtime, cartridges, Sophia planner, validation, CLI, experimental physics adapter, XR stub, asset pipeline, export adapters, multiplayer stub, publishing catalog, and **Godot/Unreal engine adapters** are implemented. Two browser prototypes and a reference world exist. Tests and CI are in place.

Full production features (connected external Sophia model, production networking, marketplace UI, full WebXR, complete Godot/Unreal project file generation, WebGPU path) remain future work.

## License

Monarch Open Sovereignty License v1.0. See `LICENSE`.

---

**The world is the source of truth.**

© 2025–2026 Steven Craig Leake Jr. · Monarch Sovereign Systems
