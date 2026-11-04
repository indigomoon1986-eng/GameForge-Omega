from gameforge.core.worldspec import WorldSpec, Entity

def test_worldspec_hash():
    w = WorldSpec(title="Test", entities=[Entity(id="p", type="player")])
    h1 = w.compute_hash()
    h2 = w.compute_hash()
    assert h1 == h2
    assert len(h1) == 64
