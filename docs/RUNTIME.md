# Runtime, Cartridges, Sophia, XR, Assets

## Deterministic World Runtime

`gameforge.runtime.WorldRuntime` provides a fixed-timestep simulation loop with event emission and handler registration. Worlds remain the source of truth; the runtime advances state under deterministic rules.

## MR7 Cartridges

`gameforge.cartridges.CartridgeRegistry` lets worlds declare required capabilities (render, movement, objectives, npc, physics, cinema, experimental_physics). Dependencies are resolved automatically. Experimental cartridges are labeled.

## Sophia Planner

`gameforge.sophia.SophiaPlanner` proposes WorldSpec changes from natural-language prompts. The creator must call `authorize()` before the proposal becomes the active world. Deterministic scaffolding; no external model required.

## XR Adapter

`gameforge.render.XRAdapter` is a stub for WebXR / LeakXR session requests (immersive-vr, immersive-ar, inline). Full session management is future work.

## Asset Pipeline

`gameforge.assets.AssetPipeline` registers meshes, materials, audio, and other resources by id, type, URI, and content hash for provenance.

All components preserve creator authorization and the semantic-world invariant.
