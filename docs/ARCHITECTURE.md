# GameForge Ω Architecture

Reconstructed from August–September GameForge work, MR7 MonoReality, LUCA/LOCS, SENTIUM, and Sophia Co-Architect plans.

## Foundational Decision

**The world is the source of truth. The graphics engine is only one way of viewing it.**

## Seven Native Systems

1. **ForgeCore** — World state, ECS, events, deterministic simulation tick.
2. **ForgeGeometry** — LOCS topology, LUCA operators, spatial reasoning, procedural terrain.
3. **ForgeRender** — Browser (WebGPU/Three.js), materials, lighting, XR adapters. Export paths to Godot/Unreal.
4. **ForgeMind** — SENTIUM NPCs, goals, memory, dialogue, agent orchestration.
5. **ForgePhysics** — Conventional rigid-body + optional experimental Leakean simulation (explicitly labeled).
6. **ForgeStudio** — Sophia Composer, World Viewport, World Graph, Inspector, timeline, asset tools.
7. **ForgeFabric** — Compilation, builds, cloud execution, versioning, collaboration, distribution, marketplace.

## MR7 Cartridges

Worlds declare required cartridges instead of loading the entire Monarch ecosystem.

Example: simple platformer → render, movement, collisions, objectives.
Scientific simulation → geometric operators, experimental physics, instrumentation, ExaForge.

## Creation Pipeline

1. Creator describes a world.
2. Sophia Game Planner proposes Typed WorldSpec.
3. Validation and XTAX policy check.
4. LUCA/LOCS World Compiler.
5. Deterministic World Runtime.
6. Render / Play / Simulate.
7. Observe / Decide / Act.
8. Persist state and receipts.
9. Export / Publish / Branch.

Sophia proposes changes and shows previews. The creator authorizes them.

## Alpha Status

`alpha/index.html` implements the recovered September MVP: prompt → playable, with one environment, player, NPCs, objectives, win/loss, and JSON export.

## Integration Notes

- Earlier private repository: SophiaL-ToE-GameForge (monoreality adapters, Godot compiler, prompt translator, ExaForge).
- CIA-1 continuity concepts inform persistent agent memory and provenance.
- Young Realms of Becoming supplies monoreality and Sophia continuity patterns.

All experimental physics remains clearly labeled.
