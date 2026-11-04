from gameforge.physics.body import RigidBody, PhysicsWorld
from gameforge.script.sandbox import ScriptSandbox
from gameforge.cinema.timeline import Timeline
from gameforge.worlds.persistence import WorldVault
from gameforge.fabric.builder import WorldBuilder
from gameforge.core.worldspec import WorldSpec

def test_physics_collision():
    w = PhysicsWorld()
    a = RigidBody(id="a", x=0, y=0, vx=1, radius=1)
    b = RigidBody(id="b", x=1.5, y=0, vx=-1, radius=1)
    w.add(a); w.add(b)
    w.step(0.1)
    assert a.x != 0 or b.x != 1.5  # positions changed or collision resolved

def test_script_sandbox():
    s = ScriptSandbox()
    assert s.evaluate("2 + 3 * 4") == 14
    assert s.evaluate("x > 5", {"x": 7}) is True

def test_timeline_sample():
    t = Timeline()
    t.add_keyframe(0, "x", 0)
    t.add_keyframe(1, "x", 10)
    assert abs(t.sample(0.5)["x"] - 5) < 0.1

def test_world_vault():
    v = WorldVault()
    h = v.save({"title": "test"}, note="initial")
    assert v.load(h)["title"] == "test"
    assert len(v.history()) == 1

def test_builder():
    spec = WorldSpec(title="BuildTest")
    m = WorldBuilder().build(spec)
    assert m.title == "BuildTest"
    assert len(m.world_hash) == 64
