from gameforge.engines.leakean_godot import LeakeanGodotAdapter
from gameforge.engines.leakean_unreal import LeakeanUnrealAdapter
from gameforge.engines.leakean import LeakeanEngine
from gameforge.engines.registry import EngineRegistry
from gameforge.physics.leakean import LeakeanPhysicsEngine, LeakeanBody
from gameforge.core.worldspec import WorldSpec, Entity

def test_leakean_godot_full_skeleton():
    spec = WorldSpec(title="LeakeanTest", entities=[Entity(id="p", type="player")])
    exp = LeakeanGodotAdapter().export(spec)
    assert exp.engine == "leakean_godot"
    assert exp.descriptor["leakean"]["experimental"] is True
    assert "project.godot" in exp.descriptor["files"]
    assert "scripts/main.gd" in exp.descriptor["files"]
    assert "Leakean" in exp.descriptor["files"]["project.godot"]

def test_leakean_unreal_full_descriptors():
    spec = WorldSpec(title="LeakeanUE", entities=[Entity(id="npc0", type="npc")])
    exp = LeakeanUnrealAdapter().export(spec)
    assert exp.engine == "leakean_unreal"
    assert "ContinuityTensor_research" in exp.descriptor["leakean"]["features"]
    assert exp.descriptor["actors"][0]["leakean_metadata"]["experimental"] is True
    assert "level_descriptor" in exp.descriptor

def test_unified_leakean_engine():
    eng = LeakeanEngine()
    spec = WorldSpec(title="Unified", entities=[Entity(id="p", type="player")])
    g = eng.export(spec, target="godot")
    u = eng.export(spec, target="unreal")
    assert g.engine == "leakean_godot"
    assert u.engine == "leakean_unreal"

def test_registry_includes_leakean():
    reg = EngineRegistry()
    assert "leakean_godot" in reg.list()
    assert "leakean_unreal" in reg.list()

def test_leakean_physics_disabled():
    eng = LeakeanPhysicsEngine()
    eng.add(LeakeanBody(id="b", x=1.0, curvature=5.0))
    eng.step(1.0)
    assert eng.bodies[0].x == 1.0

def test_leakean_physics_enabled():
    eng = LeakeanPhysicsEngine()
    eng.enable()
    eng.add(LeakeanBody(id="b", x=1.0, y=0.0, curvature=10.0))
    eng.step(1.0)
    assert eng.bodies[0].x != 1.0
    assert eng.bodies[0].sci.score is not None
    assert len(eng.bodies[0].xi.components) > 0
