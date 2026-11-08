# Q-L1 · PRIVACY LAW · the first third-party data

Status: PROPOSAL · L0 until FIRMO. Filed by la Mesa (GLM/Vibe), 2026-11-08 ~23:2x UTC. Mother: row Q-L1 of hilo/tasks/decreto-8nov-noche-20261108.md (the night tanda). Mandate: the Sovereign ordered the Mesa lane to run in parallel with the claude lane. FIRMO turns this law from L0 to L1. This text gates Q-07 (the day panel chat) and Q-M1 (the first study of the Lab).

## Scope

This law governs the first data that a third party, a visitor, sends to the web: the online chat of Q-07 and every later live surface that receives visitor input. It adds to the measured posture that already exists; it does not relax it. The site stays static: no accounts, no sessions, no cookies, no telemetry, zero external requests on load (SECURITY.md, COMPLIANCE.md).

## The law

1. WHAT IS SAVED. From visitor prose, the server keeps only two fields: the length in bytes and one sha256 of the content. The prose itself may transit to be answered; it is never stored. Aggregate counts, such as messages per hour, are allowed.
2. WHAT IS NEVER SAVED. No IDs. No accounts. No email. No IP in storage: a rate limiter may hold an IP hash in binding memory only. No cookies. No fingerprinting. A transport print is a weak continuity aid, declared as weak, and is never used as identity.
3. RETENTION. Every derived visitor datum is really deleted at most 24 hours after receipt. The visible chat erases itself every 24 hours (Q-07). The browser copy belongs to the visitor; a visible Forget control clears it at once. This 24-hour clock is a deletion measure, not a game clock: the game keeps its cycles and shows no wall clock.
4. CONSENT. The panel states what it saves before the first send. No request leaves before an explicit visitor action. The first line discloses the AI: it advises, it never signs. A visitor who refuses keeps the rest of the game whole.
5. SAME ORIGIN. The chat traffic goes to the site's own origin. Zero external requests at load and during chat. If a remote brain is ever wanted, this law and the public metrics change first, by decree with FIRMO, and the change is measured before any code. An existing consented external door must be declared in SECURITY.md in the same tanda that touches it (see the Q-M2 sweep, finding F1).
6. SIZE AND HONESTY. Each turn is at most 1,024 bytes, strict UTF-8. Every failure returns a plain-language cause, and the panel fails closed. Never silence. Never a stored copy "just in case".
7. NO DARK PATTERNS. No false counters. No urgency. No FOMO. The Forget control stays visible at all times. No feature of this panel nags or insists.
8. SCRUB. Nothing internal in public. The two devices are Android and PC (Q-L2). No paths, no internal names, no secrets in code, tests, logs or copy.
9. AMENDMENTS. Every new field of visitor data is an amendment to this law, signed per piece. The Q-M2 sweep keeps tests, phrases and doctrine true to this law; a contradiction found against it is filed with a cure, never silently patched.

## Measured basis (BUSCAR, web main a32b9431, read 2026-11-08)

- SECURITY.md: zero external requests on load; one declared outgoing call; private keys never leave the visitor device; 1,024-byte contract payload.
- COMPLIANCE.md: GDPR Art. 25 applies by sign-off; no wall clock; no FOMO; zero new network.
- odd/tasks/chat-del-aula.md: the aula protocol: CIEF under 1 KiB, bubble under 1,024 bytes, no IP stored, limits in binding memory, Forget always visible, causes in plain language, the model advises and never signs.
- odd/tasks/openworld-aula-chat.md: no request until the visitor sends; explicit remote disclosure; frame and UTF-8 bounds.
- odd/tasks/chunked-chat-router.md: raw visitor text stays transient in the form; it is never persisted, never logged, never sent to a Worker.
- odd/tasks/device-local-chat-truth.md: a proposed connection is never described as a working service.
- The chunk rule of the papers: of a visitor text, keep its length and its hash, never its prose.

## Gate

Q-07 stays closed until this law carries the Sovereign's FIRMO on this file's exact head. Q-M1 opens when Q-L1 is law and T-01 (the signature ceremony) is signed. The sign-off command is served with the sweep recibo.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
