from gameforge.runtime.loop import WorldRuntime
from gameforge.core.worldspec import WorldSpec
from gameforge.cartridges.registry import CartridgeRegistry
from gameforge.sophia.planner import SophiaPlanner
from gameforge.render.xr import XRAdapter, XRSessionConfig
from gameforge.assets.pipeline import AssetPipeline

def test_runtime_steps():
    spec = WorldSpec(title="RuntimeTest")
    rt = WorldRuntime(spec)
    results = rt.run(5)
    assert len(results) == 5
    assert results[-1].tick == 5

def test_cartridges():
    reg = CartridgeRegistry()
    reg.defaults()
    resolved = reg.resolve(["npc", "physics"])
    names = [c.name for c in resolved]
    assert "npc" in names
    assert "physics" in names

def test_sophia_planner():
    planner = SophiaPlanner()
    prop = planner.propose("Add a portal and two collectibles")
    assert not prop.authorized
    authorized = planner.authorize(prop)
    assert any(e.type == "portal" for e in authorized.entities)

def test_xr():
    xr = XRAdapter()
    ok = xr.request(XRSessionConfig(mode="immersive-vr"))
    assert ok
    assert xr.is_active()
    xr.end()
    assert not xr.is_active()

def test_assets():
    pipe = AssetPipeline()
    a = pipe.register("mesh1", "mesh", "res://mesh.glb", b"fake")
    assert a.hash
    assert pipe.get("mesh1") is not None
