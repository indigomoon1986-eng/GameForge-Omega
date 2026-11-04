# Export, Multiplayer, and Publishing

## Export Adapters

`gameforge.fabric.export.ExportAdapter` produces structured hand-offs:

- `to_web(spec)` — JSON-ready browser package.
- `to_godot_descriptor(spec)` — Minimal Godot project descriptor (not a full engine project).
- `to_json(spec, target)` — Serialized form.

Full Godot/Unreal project generation remains future work; the descriptor preserves the semantic world for later compilation.

## Multiplayer Stub

`gameforge.fabric.multiplayer.Session` holds an authoritative world hash and client replicas with position updates and join/leave events. Not a full networking stack; suitable for local-first or future authoritative server designs.

## Publishing

`gameforge.fabric.publish.Marketplace` stores PublishRecords with creator ownership, optional public listing, and tags. Worlds remain under creator control; no coercive extraction.

## Prompt Translator

`gameforge.core.prompt.PromptTranslator` converts natural-language prompts into typed WorldSpec (player, collectibles, enemies, portals, NPCs). Deterministic and local.

## Dialogue

`gameforge.mind.dialogue.DialogueTree` supports simple NPC conversation graphs for ForgeMind.

All components preserve the invariant: the world is the source of truth; renderers and networks are views.
