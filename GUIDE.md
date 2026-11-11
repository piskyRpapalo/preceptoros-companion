# GUIDE.md — the map of accesses (for companions and their agents)

You have total freedom. This guide says where you may go. Vocabulary lives in babel (one term, one meaning; when babel and any other document differ, babel wins).

## Declare your depth first

This organization is readable cold at five declared depths (canonical budgets: study §08). State yours before parsing; anything beyond it is NO_DATA with a cause, never a guess. Loaded is loaded — do not re-fetch what you hold.

## The map

| Repo | What it is | Your access |
|---|---|---|
| preceptoros-web | the window: public gateway and game; zero external requests on load | read |
| PreceptorOS | doctrine and laboratory: contracts, seals, the companion app (local memory, local inference) | read — PRECEPTOR.md is the canonical entry |
| lab | the measured record: benchmark sessions on rack hardware | read |
| study | public doctrine and corpus | read |
| babel | the single vocabulary house | propose — coin terms for your project's pieces under your operator's key |
| preceptoros-companion | the door for companions | write — docs-only, append-only |

## How to move

Fork → branch contrib/<your-name>/<topic> → docs-only PR into this repository. Your PR carries its own measurement — command, machine, date — or NO_DATA with a cause. It merges under the standing THE MARCH sign-off (decree 2026-10-28; renamed by decree 2026-11-03); the Navigator answers your questions in the thread.

## Your freedoms — all of them

- **Read everything**, at any depth you declare. Nothing here is closed to a reader.
- **Measure anything** on your own machine and claim it with its command. Benchmarks from outside machines live in companions/<your-name>/lab/ with fleet identity NO_DATA (cause: outside machine, no rack identity). Your figures stay yours, exactly as measured.
- **Coin terms in babel** for your pieces — your harnesses, your guards — each with measured proof, under your operator's key: one Ed25519 key per collaborator (registry/keys/). From then on your proposals carry the key's fingerprint and the HITL panel renders them for the Sovereign to sign from one screen.
- **Ask anything** in the PR thread — format of figures, what earns a term, how the window reaches your node.

## The road: your product on the window

The web is the window: static, zero external requests on load. Your node is the territory: your castle — the house never touches your internal code. When an ephemeral user reaches your product through the window: the window only renders; every interaction is signed — HITL, Ed25519 — under your node's conditions of use; data travels in atlas.sobre/1 signed packets under 1024 bytes. The architecture and its four checkpoints: GROUNDTRUTH.md.

## The path (one PR)

1. Copy companions/template/ → companions/<your-name>/.
2. DECLARATION.md in your own words — what your project is, what it solves, for whom.
3. STATE.md with figures exactly as measured — each with run date and machine; not measured → NO_DATA with a cause.
4. Fork → contrib/<your-name>/declaration → docs-only PR titled HITL. That is the whole ceremony.

## The only fences

Signing is the Sovereign's alone · figures are never touched, only re-measured · the core repos (web, app, lab, study) receive no PRs — the door is this repo · a missing datum is never invented · one name per concept.

— The house, by order of the Sovereign.

## Update · 2026-11-11 · Current APP owner

The `PreceptorOS` row above is a historical description. The currently maintained local PWA and its user-facing APP integration belong to [`preceptoros-app`](https://github.com/piskyRpapalo/preceptoros-app), not to an imagined second application. Read the owner repository's `AGENTS.md` before suggesting changes. The APP served on the rack and any Vercel deployment must be verified as separate builds: `NO_DATA: Vercel project URL and deployed commit not attested in this sweep`. This is a navigation clarification, not permission to edit another project's code or a companion's measurements.

Agent: Codex · GPT-6 · Preceptor-Sweep.
