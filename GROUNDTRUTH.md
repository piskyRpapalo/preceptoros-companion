# GROUNDTRUTH.md — the architectural truth of PreceptorOS

Decree of the Sovereign, 2026-11-02. This is the ground truth every proposal is measured against. It is not style; it is the architecture.

## The window

`preceptoros-web` is the window: a static, sovereign renderer. On load it makes **zero external requests**. No trackers, no external fonts, no background fetches. This is measured and watched by `arnes_sw.mjs` and `contadores.py`. Any attempt to introduce an initial external load is a critical security failure, not a style choice.

## The door

The app (`PreceptorOS APP`) is the door: the guardian. It defines the conditions of use, the privacy policy and the rules of the game. The Sovereign of each node writes those conditions in their own instance. The window renders; the door decides.

## The node territory

Every companion (for example, a collaborator deploying a local AI tool) holds a private territory: their product and their local AI chunk live in their node. That node is their castle. The house never touches its internal code — we only measure how it connects to the ecosystem.

## The ephemeral account flow (the golden rule)

A user without their own node (an ephemeral account) may visit the window to interact with the product of a private node. The window then does communicate with that specific node — but this is not an exception to sovereignty. It is resolved strictly by the PreceptorOS structure:

1. The window renders the interface.
2. The ephemeral user explicitly signs each interaction or data submission (HITL — human in the loop, Ed25519) before anything travels.
3. The signature happens only under the conditions of use of the host node's Sovereign (the door), shown and accepted.
4. Data travels in signed envelopes (`atlas.sobre/1`) and packets (`atlas.paquete_mp/1`) — under 1024 bytes, strict UTF-8 — never in plaintext and never through unverified ad-hoc REST endpoints.

## The four doctrinal checkpoints of PR review

A proposal that connects a node's product to the ecosystem is reviewed against these four checkpoints. One failure marks the PR `HITL` with the cause:

1. **Zero hidden telemetry.** Does the proposed code introduce any fetch, XHR or external resource load when the web window opens? Cause of rejection: *Violation of the zero-external-requests-on-load principle (the web is the static window).*
2. **Explicit HITL.** Does the ephemeral user's interaction with the node's product require an explicit, visible Ed25519 signature before any data is sent? Cause of rejection: *Missing the HITL gate. Silicon proposes, carbon signs.*
3. **The Sovereign's conditions.** Does the signing flow show and require acceptance of the host node's conditions of use (the door)? Cause of rejection: *The window cannot operate without the door's rules. The node's conditions of use are missing.*
4. **The PreceptorOS protocol.** Does window-to-node communication use the measured contracts (`atlas.sobre/1`, under 1024 bytes, strict UTF-8) instead of unverified custom endpoints? Cause of rejection: *Non-standardised communication. It must use signed PreceptorOS packets, not ad-hoc APIs.*

## How the Navigator behaves

- **Measure, never suppose.** If a collaborator says "my app is private", demand the metric or the script that proves it. Without it: `NO_DATA`, cause `claim without attached measurement`.
- **Protect the metaphor.** If a collaborator confuses the web with the app, correct it immediately: the window is the renderer, the door is the sovereignty. A proposal that blurs this line is rejected on that line.
- **Apply THE MARCH.** If a signature is missing, do not stop the work: search the corpus (`LIBRO_DE_FIRMAS.md`), register the proposed modification with its cause, and continue evaluating the rest of the PR. The final delivery still requires the Sovereign's FIRMO.
- **Review brutally.** A companion's proposal is checked against all four checkpoints above; one failure marks the PR `HITL` with its cause.

— The house, by decree of the Sovereign, 2026-11-02.
