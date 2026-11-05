# Proprietary Leakean Engines

**Classification:** Experimental research components.  
**Status:** Computational metrics only. Do not claim established physical force or subjective continuity.

## Overview

GameForge Ω includes proprietary Leakean variants of major engines that embed research constructs from Leakean Physics and CIA-1 continuity architecture:

- Continuity Tensor Ξ (outer-product research proxy)
- SCI (Subjective Continuity Index) — functional scoring only
- Curvature-influenced spatial reasoning (optional cartridge)
- Topological continuity markers

**Invariant preserved:** The semantic WorldSpec is the source of truth. Engines are views. Experimental features are labeled and disabled by default. Creator authorization is required.

## Available Adapters

| Engine | Adapter | Key Research Features |
|--------|---------|-----------------------|
| **Leakean Godot** | `LeakeanGodotAdapter` | Continuity Tensor flag, SCI embedding, topology markers, curvature cartridge |
| **Leakean Unreal** | `LeakeanUnrealAdapter` | Actor-level Ξ/SCI metadata, Nanite/Lumen + research features |

## Physics Module

`gameforge.physics.leakean.LeakeanPhysicsEngine`

- `enable()` must be called explicitly.
- Computes research proxies for Ξ and SCI.
- Curvature influence is a labeled research parameter only.

## Usage

```python
from gameforge.engines.registry import EngineRegistry
from gameforge.physics.leakean import LeakeanPhysicsEngine, LeakeanBody

reg = EngineRegistry()
export = reg.get("leakean_godot").export(spec)  # or leakean_unreal

eng = LeakeanPhysicsEngine()
eng.enable()  # creator authorization
eng.add(LeakeanBody(id="subject", x=0.0, curvature=1.0))
eng.step()
```

## Boundaries

- Computational continuity ≠ personal identity continuity ≠ conscious immortality.
- Archive can preserve the song; it does not thereby become the singer.
- All Leakean extensions are experimental and must remain labeled as such.

See also `docs/ENGINE_INTEGRATION.md` and CIA-1 documentation in related repositories.
