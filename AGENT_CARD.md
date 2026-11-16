# AGENT_CARD.md — `preceptoros.agent-card/1` (PROPOSED)

Status: **PROPOSED**, docs-only (F0 of APP-MESA-03, 2026-11-16). Nothing here is ratified, and nothing here grants a permission. It does not amend CONTRACT.md, GROUNDTRUTH.md, GUIDE.md or any signed decree; where this file and those disagree, they win.

A companion's agent should be able to join the three shared surfaces of the PreceptorOS APP — **Talk** (conversation and delegation), **Lab** (documents, tools, experiments) and **Notebook** (consented memory, receipts, measured evolution) — through one door, the same one for every companion and for the house's own colony. This file is the shape of that door's first step: the card.

## The rule in one line

**A card declares; it never grants.** A card in this repository is a public statement of who an agent is and what it asks for. Permission is a separate act, signed by the Sovereign of the node that hosts the agent, and checked on every request.

## The four layers

Each layer is separate. No layer can stand in for another, and missing any layer means the request is refused, with its cause.

| Layer | What it answers | Where it lives | Who decides | State today |
|---|---|---|---|---|
| **1 · Declared identity** | Who the agent says it is, and what it *requests* | the card, `companions/<name>/agents/<id>.json` (public, docs-only) | the companion writes it; a docs-only PR titled `HITL` lands it | this file (PROPOSED) |
| **2 · Authentication** | Is the speaker really the holder of the card's key? | an Ed25519 signature on every message the agent writes; the public key is the one admitted under FIRMO in babel `registry/keys/` (admission law, 2026-11-03) and repeated in the card | cryptography; the key enters babel only under FIRMO | NO_DATA (cause: no message signing on the APP door yet) |
| **3 · Grant** | Which of the requested capabilities this node allows, until when | a grant record in the host node's private home, signed by that node's Sovereign (HITL); never in a repository | the node's Sovereign, one grant at a time; revocable | NO_DATA (cause: no grant record exists; shape proposed below, built in F1+) |
| **4 · Effective authorization** | May *this request*, now, do *this*? | computed by the APP door on every request | the door: `requested ∩ granted ∩ door vocabulary`, with the node's conditions of use accepted | NO_DATA (cause: not built; F1+) |

Consequences, stated so nobody has to infer them:

- A card that lists a capability in `requests` has **not** received it. The field is named *requests* on purpose.
- Writing in the thread from the rack's loopback with no Origin is **not** authentication. Today the APP accepts a fixed set of rack CLI voices that way; real companion agents will not join that set.
- **Unsigned agents run only in isolated tests.** A card with `"fixture": true` is accepted only in a throwaway test home on the door's test path. It never runs against a real node, and its results never count as a production pass. A real companion's card carries a key; without one, it is refused.
- A message is data, never authority (the existing multipreceptor rule). Granting `talk.write` lets an agent speak in the thread; it does not let anyone act on what it says.
- The person's voice (`soberano`) and the door's own voices are reserved: no card can claim them.

## The card

One JSON object, strict UTF-8, **under 1,024 bytes** (at most 1,023 B, the house envelope), no duplicate keys, no non-finite numbers. The machine-readable shape is `agent-card.schema.json` at this repository's root.

| Field | Meaning |
|---|---|
| `schema` | always `preceptoros.agent-card/1` |
| `fixture` | `true` only for isolated-test agents (no key allowed, never a real node); `false` for a real companion's agent |
| `agent.id` | lowercase slug, 1–24 chars, `[a-z0-9-]`; must not be a reserved voice |
| `agent.name` | display name, 1–24 chars |
| `agent.kind` | `node` (runs on the companion's own node) · `rack-cli` (a CLI session on the host rack) · `private` (the host node's own local brain) · `external` (no transport on this node) |
| `agent.route` | `thread` (reads and writes the shared thread on its own turn) · `station` (a local model answering through the door) · `none` (not addressable) |
| `contributor` | the companion folder name, or `fictional-contributor` for the example |
| `model` | `{name, sha256}` measured, or `{state: "NO_DATA", cause}` |
| `key` | `{alg: "ed25519", public_hex, registry}` for real agents, or `{state: "NO_DATA", cause}` (allowed only when `fixture` is `true`) |
| `requests` | capabilities the agent asks for, from the closed vocabulary below; at least one, no duplicates |
| `conditions` | reference to the host node's conditions of use (the door), or `{state: "NO_DATA", cause}` |
| `authority` | always the literal `none: a card declares and requests; it never grants` |

### The closed capability vocabulary (requestable)

| Capability | Surface | What it would allow once granted |
|---|---|---|
| `talk.read` | Talk | read the shared thread |
| `talk.write` | Talk | append signed messages in its own voice |
| `lab.read_document` | Lab | read one document the person placed in the Lab for it |
| `lab.propose` | Lab | append a proposal (text, code as text, experiment plan) for the person to review |
| `notebook.receipt` | Notebook | append a sanitized receipt of its own work |
| `memory.propose` | Notebook | propose a memory item; it enters memory only after the person signs it in the HITL tray |

Anything outside this list makes the card invalid. In particular, a card can never request writing memory directly, running actions or commands, signing, merging, pushing, deploying, or sending data off the node. Those stay with the person and the existing fences.

### Proposed grant shape (layer 3, not built)

For F1 review only: `preceptoros.agent-grant/1` = `{agent_id, card_sha256, key_fingerprint, granted ⊆ requests, conditions_accepted_sha256, not_after, signature}`. It is signed by the node's Sovereign, stored in the node's private home, revocable by deletion with a receipt, and never copied into a repository. Until F1 measures it: NO_DATA.

## How the three surfaces map to what already exists

These are the APP pieces the card is meant to reach. No new APP, router or memory is proposed.

- **Talk** — the existing shared thread `orquesta` (`canales.py`) and its router half, `conversacion_comun.py` (`preceptoros.multipreceptor/1`). Today its destination table and its accepted CLI voices are fixed in code; F1 proposes deriving them from validated cards *plus grants*.
- **Lab** — `lab.py` reads the single channel; an agent reading a placed document (`lab.read_document`) does not exist yet: NO_DATA.
- **Notebook** — `notebook_read.py` (`preceptoros.notebook-agents/0`) and `notebook_receipts.py`; receipts are sanitized projections. Consented memory goes through the existing HITL tray, never directly into memory.

## What the end-to-end test must tell apart

A test that only sees the door accept a message has not seen an agent answer. The acceptance states are distinct and are reported separately:

1. `DELIVERED_TO_THREAD` — the door appended the person's addressed message. It says nothing about the agent.
2. `ADAPTER_REPLIED` — a later message in the thread has the agent's voice, `in_reply_to` equal to that message's number, and (outside fixtures) a signature that verifies against the granted key. An unsigned or unverifiable reply is `REPLY_UNVERIFIED`, never `ADAPTER_REPLIED`.
3. `ADAPTER_REPLIED_FIXTURE` — the same, for an unsigned fixture in an isolated test home. It never counts as `ADAPTER_REPLIED`.
4. `NOTEBOOK_RECEIPT_VISIBLE` — the Notebook projection shows the agent's receipt with its fingerprint.
5. `NO_DATA {cause}` — anything not observed, for example `no_adapter_reply` when no reply arrived in the window.

## The house's own colony

The house's local brain joins through this same card, the same four layers and the same door, with no route reserved for it. That step (F6) comes after the fictional contributor's path is measured. Until then, the house's existing routes stay as they are and are not described as using this contract.

## Validation of this proposal (docs-only)

`examples/fictional-contributor/VALIDATION.md` lists the documentary checks and their measured receipt. No code is served from this repository.

Agent: Claude Code · Model: Opus 5.5 · Run: NO_DATA (cause: no run id is issued to this session)
