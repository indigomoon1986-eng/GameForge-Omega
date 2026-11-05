# Game Engine Integration

GameForge Ω owns the **semantic WorldSpec**. Engines are views and export targets.

## Available Adapters

| Engine | Adapter | Output |
|--------|---------|--------|
| **Godot 4** | `GodotAdapter` | Project skeleton + main.gd snippet + entity mapping |
| **Unreal Engine 5** | `UnrealAdapter` | Actor descriptors (Nanite/Lumen noted), type mapping |

## Usage

```python
from gameforge.engines.registry import EngineRegistry
from gameforge.core.worldspec import WorldSpec, Entity

spec = WorldSpec(title="Test", entities=[Entity(id="p", type="player")])
reg = EngineRegistry()

godot_export = reg.get("godot").export(spec)
print(godot_export.descriptor["project_godot"])

unreal_export = reg.get("unreal").export(spec)
print(unreal_export.descriptor["actors"])
```

## Design Notes

- Semantic world remains authoritative.
- Adapters produce structured descriptors suitable for later full project generation or editor import.
- Experimental features stay labeled.
- Earlier private GameForge Godot compiler and monoreality UE5 patterns informed these adapters.

Full .uproject / complete Godot project file emission and live editor sync remain future work.
