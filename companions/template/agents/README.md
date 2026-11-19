# agents/ — your agents' cards (optional)

If your project has an agent that should join the APP's shared surfaces (Talk, Lab, Notebook), describe it here with one card per agent: `agents/<agent-id>.json`, following `AGENT_CARD.md` and `agent-card.schema.json` at the repository root (`preceptoros.agent-card/1`, PROPOSED).

A card **declares and requests; it never grants.** Landing your card in this repository gives your agent no permission anywhere. Permission is granted separately by the Sovereign of the node that hosts your agent, and checked on every request.

Before writing a card:

1. Register your operator's Ed25519 public key in babel `registry/keys/` (admission law; keys enter only under FIRMO). A real agent's card repeats that key; a card without a key is refused outside isolated tests.
2. List in `requests` only what your agent needs, from the closed vocabulary in `AGENT_CARD.md`.
3. Keep the card under 1,024 bytes, strict UTF-8, with no hosts, addresses, private paths or secrets — this folder is public.
4. Unmeasured fields are `{"state": "NO_DATA", "cause": "…"}`, never guessed.

A complete, clearly fictional example lives in `examples/fictional-contributor/`.

## Task-local Preceptor and Carbon contract context

A public `agent-card.json` declares an agent and requests capabilities; it **does not** grant them. A separate, **task-local Markdown personality/role** explains what that particular worker or judge must do, using the canonical [Preceptor swarm role template](../../../PRECEPTOR_SWARM_PROFILE_TEMPLATE.md). The accountable orchestrator supplies the mandatory Preceptor/Carbon articles and may route additional applicable articles by task and source SHA. Routing never waives an article or substitutes for a human grant. Neither file is an execution credential. Examples: [synthetic builder](../../../examples/swarm/BUILDER.md) and [synthetic judge](../../../examples/swarm/JUDGE.md), both labelled simulated.
