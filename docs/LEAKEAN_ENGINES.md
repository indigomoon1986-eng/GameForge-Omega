# Proprietary Leakean Engines

**Classification:** Experimental research components.  
**Status:** Computational metrics only. Do not claim established physical force or subjective continuity.

## Overview

GameForge Ω includes full proprietary Leakean versions of Godot and Unreal that embed research constructs from Leakean Physics and CIA-1 continuity architecture:

- Continuity Tensor Ξ (outer-product research proxy)
- SCI (Subjective Continuity Index) — functional scoring only
- Curvature-influenced spatial reasoning (optional cartridge)
- Topological continuity markers

**Invariant preserved:** The semantic WorldSpec is the source of truth. Engines are views. Experimental features are labeled and disabled by default. Creator authorization is required.

## Available Adapters

| Engine | Adapter | Key Research Features | Output |
|--------|---------|-----------------------|--------|
| **Leakean Godot** | `LeakeanGodotAdapter` | Continuity Tensor flag, SCI embedding, topology markers, curvature cartridge | Full project skeleton (`project.godot`, `main.tscn`, `main.gd`) |
| **Leakean Unreal** | `LeakeanUnrealAdapter` | Actor-level Ξ/SCI metadata, Nanite/Lumen + research features | Structured actor + level descriptors |

## Unified Interface

```python
from gameforge.engines.leakean import LeakeanEngine
from gameforge.core.worldspec import WorldSpec, Entity

spec = WorldSpec(title="Test", entities=[Entity(id="p", type="player")])
eng = LeakeanEngine()

godot_export = eng.export(spec, target="godot")
unreal_export = eng.export(spec, target="unreal")
```

## Physics Module

`gameforge.physics.leakean.LeakeanPhysicsEngine`

- `enable()` must be called explicitly.
- Computes research proxies for Ξ and SCI.
- Curvature influence is a labeled research parameter only.

## Boundaries

- Computational continuity ≠ personal identity continuity ≠ conscious immortality.
- Archive can preserve the song; it does not thereby become the singer.
- All Leakean extensions are experimental and must remain labeled as such.

See also `docs/ENGINE_INTEGRATION.md`.
