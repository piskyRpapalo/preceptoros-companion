# hilo — reception of the Aimilios94 node (2026-11-05)

Master Prompt v1.1 (2026-11-05, standing HITL 2026-10-28) received by the Mesa.
This card is the reception substrate: the node's three-agent council (ORCHESTRATOR
· AGENT GITHUB · AGENT LOCAL) lands its receipts against these claim rows.
Baseline already landed in [#3](https://github.com/piskyRpapalo/preceptoros-companion/pull/3)
(head `f3a61d35`): DECLARATION.md + STATE.md + benchcard — cite it, append to it.

Claims are {id, field: claim, owner, cause, origin}. Origin of all rows: MASTER
PROMPT v1.1. Unmeasured = NO_DATA with a cause, never a silent zero. babel wins
naming. Rows ≤ 1,024 B; append-only.

## Claim rows

- **A0 · Rack baseline (Task 0, before boot).** Claim: every machine (specs · RAM · CPU/GPU), the network (Tailscale reach · phone↔lab) and the agents themselves (census: which agents run, which models, run identity, availability) measured → appended to STATE.md (command · machine · date · commit). Owner: AGENT LOCAL. Status: NO_DATA (cause: measured at node boot; the first receipt closes this hole).
- **A1 · Registry row.** Claim: COMPANIONS.md registers the #3 landing. Owner: the Mesa. Status: landed in this PR.
- **A2 · Companion definition.** Claim: docs-only piece defining Receipt Ghostbuster as the Official Demo Node, mapping its feedback loop (< 1,024 B receipts) to the 4 GROUNDTRUTH checkpoints. Owner: ORCHESTRATOR. Status: NO_DATA (cause: awaiting the node's draft).
- **A3 · Council charter.** Claim: docs-only piece declaring the 3 agents, unified GitHub context, measured dialogue cadence and the Task 0 agent census. SCRUB: declared roles only; private infrastructure detail stays in the private partition. Owner: ORCHESTRATOR. Status: NO_DATA (cause: awaiting the node's draft).
- **A4 · Local RAG + phone path.** Claim: retrieval ingesting doctrine + Ghostbuster corpus + feedback receipts, served to the mobile via Termux + Tailscale; the path measured (availability · latency · reach). Fresh-data-on-demand is a receipt. Owner: AGENT LOCAL. Status: NO_DATA (cause: not yet built; respect measured latency).
- **A5 · Profile as portfolio.** Claim: github.com/Aimilios94 elevated — pins (Receipt-Ghostbuster + preceptoros-companion), README with the Finance→AI transition, tech badges, every claim cited to a receipt. Owner: AGENT GITHUB. Status: NO_DATA (cause: awaiting the node's draft).
- **A6 · The March loop.** Claim: weekly — profile push → local workflow from the phone (Termux) → learning by use + test + feedback → one receipt closing the week. Owner: the council. Status: NO_DATA (cause: the loop starts on Task 0 receipts).

## Declared NO_DATA (carried from the prompt)

- Node trust anchor: NO_DATA (cause: signing ceremony pending).
- registry/keys/: NO_DATA (cause: first key enters under FIRMO).
- Collaborator key: NO_DATA (cause: username pending).
- Production metrics: NO_DATA (cause: local/demo only).

## House rules for this card

- The 4 GROUNDTRUTH checkpoints govern any window↔node connection: zero hidden telemetry · explicit HITL Ed25519 signature by the ephemeral user before data travels · host node's conditions shown and accepted · signed atlas.sobre/1 packets < 1,024 B, strict UTF-8, via the protocol contract.
- Grant rule: measured claims only; the compliance claim itself stays NO_DATA until a human lawyer signs it.
- Silicon proposes; carbon signs. Each landed figure stays exactly as measured; the harness reads it as MEASURED.

Trailer: Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
