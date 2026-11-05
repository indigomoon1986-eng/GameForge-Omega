# Game Engine Integration

GameForge Ω owns the **semantic WorldSpec**. Engines are views and export targets.

## Available Adapters

| Engine | Adapter | Output |
|--------|---------|--------|
| **Godot 4** | `GodotAdapter` | Project skeleton + main.gd snippet + entity mapping |
| **Unreal Engine 5** | `UnrealAdapter` | Actor descriptors (Nanite/Lumen noted), type mapping |
| **Leakean Godot** (experimental) | `LeakeanGodotAdapter` | Godot skeleton + Continuity Tensor / SCI / topology research metadata |
| **Leakean Unreal** (experimental) | `LeakeanUnrealAdapter` | UE5 actor descriptors + Ξ/SCI research metadata |

## Usage

```python
from gameforge.engines.registry import EngineRegistry
from gameforge.core.worldspec import WorldSpec, Entity

spec = WorldSpec(title="Test", entities=[Entity(id="p", type="player")])
reg = EngineRegistry()

godot_export = reg.get("godot").export(spec)
leakean_export = reg.get("leakean_godot").export(spec)  # or leakean_unreal
print(leakean_export.descriptor["leakean"])
```

## Design Notes

- Semantic world remains authoritative.
- Adapters produce structured descriptors suitable for later full project generation or editor import.
- Experimental features (including all Leakean extensions) stay labeled and disabled by default.
- Creator authorization is required to enable research physics.
- Earlier private GameForge Godot compiler and monoreality UE5 patterns informed these adapters.

Full .uproject / complete Godot project file emission and live editor sync remain future work.

See `docs/LEAKEAN_ENGINES.md` for proprietary Leakean details.
