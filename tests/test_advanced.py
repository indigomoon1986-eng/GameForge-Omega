from gameforge.core.prompt import PromptTranslator
from gameforge.fabric.export import ExportAdapter
from gameforge.fabric.multiplayer import Session
from gameforge.fabric.publish import Marketplace
from gameforge.core.worldspec import WorldSpec
from gameforge.mind.dialogue import DialogueTree, DialogueNode

def test_prompt_translator():
    t = PromptTranslator()
    spec = t.translate("Add 2 collectibles and a portal and an npc")
    assert any(e.type == "collectible" for e in spec.entities)
    assert any(e.type == "portal" for e in spec.entities)
    assert any(e.type == "npc" for e in spec.entities)

def test_export():
    spec = WorldSpec(title="ExportTest")
    adapter = ExportAdapter()
    web = adapter.to_web(spec)
    assert web["title"] == "ExportTest"
    godot = adapter.to_godot_descriptor(spec)
    assert "ExportTest" in godot

def test_session():
    s = Session("abc123")
    s.join("client1")
    s.update_position("client1", [1.0, 2.0])
    snap = s.snapshot()
    assert "client1" in snap["clients"]

def test_marketplace():
    m = Marketplace()
    spec = WorldSpec(title="PubTest", author="creator")
    rec = m.publish(spec, public=True, tags=["demo"])
    assert rec.public
    assert len(m.list_public()) == 1

def test_dialogue():
    nodes = [
        DialogueNode(id="start", text="Hello", responses={"hi": "end"}),
        DialogueNode(id="end", text="Goodbye"),
    ]
    tree = DialogueTree("start", nodes)
    assert tree.current_node().text == "Hello"
    tree.choose("hi")
    assert tree.current_node().text == "Goodbye"
