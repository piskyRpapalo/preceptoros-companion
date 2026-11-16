# VALIDATION.md — documentary checks of `preceptoros.agent-card/1` (F0)

Measured 2026-11-16 ~12:27Z · x86_64 · Python 3.14.4 · jsonschema 4.19.2 (Draft 2020-12) · run twice, same result. The checking script is a scratch tool of the session and is not committed: this repository serves no code. Re-run the checks below with any Draft 2020-12 validator.

| # | Check | Result |
|---|---|---|
| V1 | `agent-card.schema.json` is itself a valid Draft 2020-12 schema | PASS |
| V2 | `agents/lantern.json` validates; 559 B (< 1,024 B), strict UTF-8, no duplicate keys | PASS |
| V3 | sabotage `fixture: false` with no key → rejected | PASS |
| V4 | sabotage agent id `soberano` (reserved voice) → rejected | PASS |
| V5 | sabotage request `memory.write` (outside the closed vocabulary) → rejected | PASS |
| V6 | sabotage `authority` changed to a grant claim → rejected | PASS |
| V7 | sabotage extra `grants` field → rejected (a card cannot carry grants) | PASS |
| V8 | sabotage duplicate request / empty requests → rejected | PASS ×2 |
| V9 | sabotage padded to 1,024 B → rejected by size | PASS |
| V10 | sabotage fixture carrying a key → rejected (fixtures are unsigned by definition) | PASS |
| V11 | sabotage duplicate JSON key → rejected at parse | PASS |
| V12 | forbidden vocabulary (AGENTS.md list) in the new files → none found | PASS |
| V13 | scrub in the new files: no IP addresses, home paths, mail addresses, private device or host names → none found | PASS |

Total: 11 card cases + 2 text scans, all PASS, ×2.

Not measured here (NO_DATA): any APP behaviour — registration, Talk delivery, agent reply, Lab document reading, Notebook receipt (cause: F0 is docs-only; the APP side is F1+, claimed by Codex CLI); authentication by signature (cause: not built); the babel entry for the term "agent card" (cause: not proposed to babel yet; the term stays PROPOSED here).
