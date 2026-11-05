from gameforge.core.validation import validate_worldspec
from gameforge.core.worldspec import WorldSpec, Entity
from gameforge.physics.experimental import ExperimentalPhysics, ExperimentalBody
from gameforge.fabric.godot_export import to_godot_skeleton

def test_validation_good():
    spec = WorldSpec(title="Valid", entities=[Entity(id="p", type="player")])
    r = validate_worldspec(spec)
    assert r.valid

def test_validation_duplicate():
    spec = WorldSpec(
        title="Dup",
        entities=[Entity(id="a", type="player"), Entity(id="a", type="npc")],
    )
    r = validate_worldspec(spec)
    assert not r.valid
    assert any("Duplicate" in e for e in r.errors)

def test_experimental_disabled_by_default():
    ep = ExperimentalPhysics()
    ep.add(ExperimentalBody(id="b", x=1, y=1, curvature=1.0))
    ep.step(1.0)
    # no change when disabled
    assert ep.bodies[0].x == 1.0

def test_experimental_enabled():
    ep = ExperimentalPhysics()
    ep.enable()
    ep.add(ExperimentalBody(id="b", x=1, y=0, curvature=10.0))
    ep.step(1.0)
    assert ep.bodies[0].x != 1.0

def test_godot_skeleton():
    spec = WorldSpec(title="GodotTest", entities=[Entity(id="p", type="player")])
    skel = to_godot_skeleton(spec)
    assert skel["engine"] == "godot"
    assert skel["title"] == "GodotTest"
    assert len(skel["entities"]) == 1
