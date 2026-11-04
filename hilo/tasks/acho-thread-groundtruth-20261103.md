# HITL · Acho frame and the conversation

Status: PROPOSED · 2026-11-03 · depth 3. The Sovereign's commission asks to
recover the conversation idea using existing pieces and evidence from the
local machine. This is a translation into an inspectable proposal, not a
claim that a signed conversation chain already exists. One branch, one piece,
no merge. The companion contract cites the permanent FIRMO of the thread
(decree 2026-10-28); the signing book was consulted, but the precise original
record for that standing coverage was not located in this reading: NO_DATA.

## 1. Verified anchors

Scope: local Linux x86_64, 2026-11-03 UTC. App sources at
[7e40181e](https://github.com/piskyRpapalo/PreceptorOS/tree/7e40181ecc7bb3737ae9ca4fb679c299ad8c0f4c),
web at [97c5d644](https://github.com/piskyRpapalo/preceptoros-web/tree/97c5d644dae5ab932a4dc174dbbd46fda516fd5b),
study at [4c8f289e](https://github.com/piskyRpapalo/study/tree/4c8f289e5d17eac07c335a36593be1ade397a907),
babel at [433ef33d](https://github.com/piskyRpapalo/babel/tree/433ef33dfaacb718c97db2286b1a014a1529e12e),
and companion at e6f86e9c.

| Command and source | Result and limit |
| --- | --- |
| `rg -n 'FASES|GUIA|motor_llama' conversacion.py` (app) | Four guide phases and a child-process adapter exist; this does not prove a signed per-turn chain. |
| `rg -n 'VOCES|motor_llama|NO_DATA' lab.py` (app) | Closed voice list and no-invented-answer path exist in source; the Lab channel and the person's conversation remain distinct. |
| `rg -n 'mode=ro|sqlite|registro' canales.py` (app) | Read paths use read-only mode; source also has a write adapter. Read-only reading does not prove the whole adapter is read-only. |
| `rg -n 'hash|texto|largo' captura.py estado.py conversacion.py` (app) | Capture has privacy-scoped metadata and correction paths; a blanket claim that all response text is always absent from every store is NO_DATA. |
| `rg -n 'NO_DATA|YES|WHEN|def ' clasificador_cuaternario.py` (app) | Parser source exists; the literal accepted output is SI/NO/CUANDO or cause-bearing NO_DATA. Equivalence to English labels needs its existing translation contract, not an assumed rename. |
| `rg -n 'RACK_ESQUEMA|RACK_RANCIA_S|RACK_FUTURO_S|CAUSA_RESIDENTE' consola.py` (app) | The source declares a 15-minute age limit and a two-minute future tolerance. A fresh rack snapshot and model residency were not read. |
| `rg -n 'charla_sin_|CAUSA_' textos.py consola.py` (app) | Three fallback text keys and three model causes exist in source; they are not evidence that they are present inside the requested fixture. |
| `rg -n 'NO_DATA|edad' interface/compass.js` (app) | Source contains age display; live rendering on a physical device was not exercised. |
| `rg -n 'sha256|chunk' public/game/chunk_router.js odd/tasks/chunked-chat-router.md` (web) | This router checks model-file chunks; its reuse for conversation context is a proposal, not measured behavior. |
| `rg -n 'hash32|prev|verifica' atlas/puros/sala_log.js` (web) | A local conversation-log prototype chains using a 32-bit hash, not the requested SHA-256. It does not prove a signed local conversation chain. |
| `rg -n 'preceptoros.acho/1' public/game/acho_language.js atlas/puros/acho.js` (web) | Frame format and pure validator exist. The validator's scope is frame fields and bounds, not a signature or prior-turn chain. |
| `rg -n 'sha256|tabla_semantica' test_face.py` (app) | This checks fixed file hashes, including the semantic table; it does not check a previous-turn hash. |
| `rg --files -g 'memoria.py' -g 'cerebros.json' -g 'servicios.json'` (app tracked tree) | NO_DATA: these exact paths were not found in this checkout; absence here does not prove ecosystem-wide absence. |
| `rg -n 'snapshot|ttl_s|firma' data/*.json` (app) | NO_DATA for the claimed signed snapshot contract in this scoped search; a reference elsewhere is not evidence of a local implementation. |
| `rg --files -g '12-schema.md' -g '13-rosetta.md' -g '08-ai-fluency.md'` (study) | The files exist. Current `12-schema.md` describes rename statuses, not the four observation statuses asserted in the commission: preserve the discrepancy. |
| `rg -n 'Acho|frame|NO_DATA|HITL|heartbeat' registry/*.md` (babel) | The registry anchors these terms; a hit is not proof that every field name is an admitted term. |
| `rg -n 'duda|propuesta|evidencia|nodo.genesis' canales.py data/canal_event.schema.json` (app) | NO_DATA for those four exact type names in these two files; no new type is inferred. |
| `systemctl --user is-active preceptoros-pwa` | `active`; this measures the unit only, not the interface, storage behavior or a signed turn. |
| `python3 test_face.py` (app, two separate runs) | 7 tests passed in each run; this is the face suite, not an Acho chain verifier. |
| `node --test atlas/puros/acho_casos.mjs` (web, two separate runs) | 48 tests passed in each run; this is the pure frame suite, not browser or device parity. |
| `rg -n 'FIRMO|2026-10-28' LIBRO_DE_FIRMAS.md` (signing book) | NO_DATA: this search did not locate the precise standing-coverage record. No signature is transcribed. |

Other commission anchors, including the envelope and packet runtime, full
faro, timeline identity across repositories, current board and model catalogue:
NO_DATA in this run, cause: not individually exercised. Their historical
claims remain citations to investigate, not current measurements.

## 2. Frame fixture and proposed turn

The following synthetic frame was serialized as compact UTF-8 JSON and passed
`Acho.valida` from web `atlas/puros/acho.js` with the web's declared band set:
241 bytes, SHA-256
`af5296fbb759255c5c78d5ce5b60c9ba58148b3b088689814e36d287f3826930`.
The hash is of the compact JSON bytes shown below, with no trailing newline.
Sound is explicitly NO_DATA. This is a frame test, not a signed turn.

```json
{"v":"preceptoros.acho/1","id":"proposal","t":0,"atoms":[{"k":"status","r":"NO_DATA: signed state and previous hash not measured.","i":[]}],"bands":[],"change":["proposal"],"sound":"NO_DATA","soundCause":"no sound measured","seal":"NO_DATA"}
```

A turn-shaped sketch follows. It is **PROPOSED**, not a valid signed frame or
a member of a real chain; the unknown predecessor is not replaced with a
synthetic genesis. Field names are provisional identifiers pending vocabulary
review.

```json
{"origen":"orquestador","st":{"estado":"NO_DATA","causa":"signature not measured","max_bytes":150},"no_data_heredados":[],"no_data_resueltos":[],"puertas_abiertas":[],"solution_propuesta":null,"hash_previo":{"estado":"NO_DATA","causa":"genesis not measured"}}
```

The desired turn carries origin, signed state, inherited unknowns, resolutions
with source measurement, dependent questions, proposed action and previous
hash. That relationship is PROPOSED. Genesis bytes, canonical serialization,
the previous SHA-256, a verified signature, the three fallback texts inside
the turn and the mapping between turn data and frame are NO_DATA: no such
fixture was located or verified. No zero hash is asserted as a real genesis.
A future test must prove reject-on-tamper, signature verification, causal
inheritance, strict UTF-8 byte size including any trailer, and both positive
and negative cases. Never truncate an oversized turn.

## 3. Phase table

| Piece | Phase | Evidence / unresolved condition |
| --- | --- | --- |
| Guide phases, local voice source, read path, bounded frame validator | A: source available to study | Anchors above; A does not claim a deployed end-to-end conversation. |
| Synthetic frame | A: local test only | 241 bytes and validator result above; unsigned and not linked to a real preceding turn. |
| Per-turn state signature and SHA-256 chain | B | NO_DATA: schema, signing, genesis and verifier not demonstrated together. |
| External contribution becoming a local turn | B | NO_DATA: opt-in signature and explicit authorization boundary not exercised. A PR remains evidence, not an external voice. |
| Multiple signatures, app/web pixel parity, live frame on device | B | NO_DATA: no paired signing or device measurement in this run. |
| Solar seal and energy value | B | NO_DATA: contract and measurement not supplied in this run. |

## 4. Vocabulary and discrepancies

`rg -n -i 'Acho|frame|NO_DATA|HITL|heartbeat|sign-off|yardstick' registry/*.md`
and `docs/lexicon.md` found those entries at the pinned sources. The registry
is the later vocabulary authority; the web lexicon is its historical seed.
Other proposed field identifiers, including inherited unknowns, resolution,
dependent questions and previous hash, are **NO_DATA as admitted vocabulary**:
the search did not establish registry admission or run the Alphabet test for
each identifier. They describe requirements, not newly admitted names.

Preserve these differences for review: Study's four term statuses differ from
the proposed four observation states; the app parser's literal verdicts differ
from their English gloss; the existing log's 32-bit hash differs from a
cryptographic SHA-256 chain; and the model-file router is not measured as a
conversation router. A signed name and a proposed name are not equivalent.

## 5. SCRUB receipt

Before publication, inspect the staged diff for private network addresses,
local home paths, internal ports and private identifiers. Pattern checks only
cover known patterns and cannot prove the absence of every secret. This
proposal uses repository-relative public source references and no local data
values. A configured private-identifier scan is NO_DATA if its environment is
not supplied; do not print or manufacture its contents.

## 6. Boundaries and receipt

| Surface | Measures / inherits | Freshness and owner |
| --- | --- | --- |
| GitHub | Published commits, PRs and receipts | A commit is historical; current rack state is NO_DATA without a dated rack observation. Human signs each head. |
| Web | A frame when a browser actually renders it | Browser, live worker and physical-device behavior: NO_DATA in this run; node owner governs its conditions. |
| App | Local source and, when exercised, its local runtime | Unit active was measured; signed turn and rendered output are NO_DATA. The person owns the local decision. |
| Rack | The commands and files actually inspected here | Source checks are timestamped; model residence, live sensor and external-device behavior are NO_DATA. |
| External reader | Published evidence at a declared depth | No local write authorization is inferred from ability to read. |

The four architectural checkpoints remain review questions for any later
connection: no hidden telemetry; explicit human signature; the node owner's
conditions; and the existing signed-packet contract. This docs-only proposal
introduces no connection and does not prove those checkpoints for future code.

Three review improvements: (1) distinguish frame validity from chain and
signature validity; (2) fix canonical bytes and genesis before claiming SHA-256
continuity; (3) require independent scoped evidence for privacy and freshness.
The deterministic claim applies only to measured form and verification; model
responses are not guaranteed deterministic. Human review and exact-head FIRMO
remain pending.
