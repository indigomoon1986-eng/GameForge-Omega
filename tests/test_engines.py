from gameforge.engines.godot import GodotAdapter
from gameforge.engines.unreal import UnrealAdapter
from gameforge.engines.registry import EngineRegistry
from gameforge.core.worldspec import WorldSpec, Entity

def test_godot_export():
    spec = WorldSpec(title="GodotWorld", entities=[Entity(id="p", type="player")])
    exp = GodotAdapter().export(spec)
    assert exp.engine == "godot"
    assert "project_godot" in exp.descriptor
    assert exp.descriptor["title"] == "GodotWorld"

def test_unreal_export():
    spec = WorldSpec(title="UEWorld", entities=[Entity(id="npc0", type="npc")])
    exp = UnrealAdapter().export(spec)
    assert exp.engine == "unreal"
    assert exp.descriptor["features"] == ["Nanite", "Lumen"]
    assert exp.descriptor["actors"][0]["class"] == "AIController + Character"

def test_registry():
    reg = EngineRegistry()
    assert "godot" in reg.list()
    assert "unreal" in reg.list()
    adapter = reg.get("godot")
    assert adapter.name == "godot"
