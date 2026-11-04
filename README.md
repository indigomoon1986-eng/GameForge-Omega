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
| **ForgeCore** | World state, ECS, events, deterministic simulation | `gameforge/core/` |
| **ForgeGeometry** | LOCS topology, spatial reasoning, procedural terrain | `gameforge/geometry/` |
| **ForgeRender** | Browser graphics, materials, lighting | `alpha/forge3d.html` |
| **ForgeMind** | SENTIUM NPCs, goals, memory | `gameforge/mind/` |
| **ForgePhysics** | Rigid-body, collision | `gameforge/physics/` |
| **ForgeStudio** | Editor, scripting, graph, cinematic authoring | `alpha/` + `gameforge/script/`, `gameforge/cinema/` |
| **ForgeFabric** | Compilation, builds, versioning, distribution | `gameforge/fabric/` |

MR7 cartridge architecture: each world declares the cartridges it needs.

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

Builds the Carolina Valley WorldSpec, instantiates a SENTIUM NPC, and produces a Fabric build manifest.

## Integration

Builds on earlier SophiaL-ToE-GameForge, monoreality orchestration, CIA-1 continuity concepts, Young Realms of Becoming, and SENTIUM/Sophia systems.

See `docs/` for architecture, integration notes, and roadmap.

## Current Maturity

All seven native systems have runnable modules. Two browser prototypes and a reference world exist. Tests cover core systems.

Full production features (connected Sophia model, multiplayer, marketplace, WebGPU path, Godot/Unreal export) remain future work.

## License

Monarch Open Sovereignty License v1.0. See `LICENSE`.

---

**The world is the source of truth.**

© 2025–2026 Steven Craig Leake Jr. · Monarch Sovereign Systems
