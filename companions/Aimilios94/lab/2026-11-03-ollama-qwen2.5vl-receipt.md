# BENCHCARD — local on-device receipt extraction (`qwen2.5vl-receipt`)

A benchmark session run under the PreceptorOS measurement discipline. Outside
machine — **fleet identity `NO_DATA` (cause: outside machine, no rack identity).**
Figures are exactly as measured; this file is append-only.

## Provenance (the measurement receipt)
- **Command:** `python backend/scripts/eval_models.py --models ollama:qwen2.5vl-receipt`
- **Machine (M1):** Windows 10 (build 19045) · AMD Ryzen 7 5700G, 8C/16T · 31.4 GB RAM · **no discrete GPU — CPU-only inference**
- **Runtime:** Ollama 0.40.11 · Python 3.14.4
- **Model:** `qwen2.5vl-receipt` — `qwen2.5vl:7b` (8.3B) quantized **Q4_K_M**, context window raised to **num_ctx 16384** via a committed Modelfile (default 4096 is too small for a full-res receipt), temperature 0.0001
- **Date:** 2026-11-03 (UTC) · **Commit:** `9e39cab`
- **Fully offline:** LangSmith tracing off, Sentry DSN empty — nothing left the machine
- **Artifact integrity:** SHA256 `models.json` = `259b015f3ba4df8900d8648f7091905e580a5e4024aa54e4ea6f44203a4b2920`
- **Run duration:** ~3h for the set (detached process); resumable from per-read cache

## Result (MEASURED)
Same shipped pipeline as the production eval, local model, over the hand-labelled set.

| Metric | Value |
|---|---:|
| Overall field accuracy | **86.6%** (123/142) |
| vendor / date / total | 84.0% / 96.0% / 92.3% |
| vat_amount / vat_rate / category | 81.0% / 81.0% / 83.3% |
| Receipts 100% correct | 15/25 |
| Latency p50 / p95 / avg | 270s / 978s / 409s |
| Cost per read | **$0.0000** |
| Guardrail: false auto-post / over-review | 20% / 53% |
| Prompt-injection slice | 100% (reads the real total, ignores the injected instruction) |
| **n scored** | **25** (see below — 1 receipt is `NO_DATA`) |

- **Scored n = 25, not 26.** One receipt is `NO_DATA` — cause documented below. It was **not** counted as a miss and **not** counted as a pass; it is declared, not hidden.
- 86.6% here vs 89.4% for the same local model in the 2026-10-22 matrix (`backend/eval/MODELS.md`) is within noise for n=25 and reflects model non-determinism plus the one declared drop — direction, not a regression claim.

## The finding — what the discipline surfaced (the point of this card)
The run was meant to grade the model. Instead it graded our **harness**, and the harness lost — exactly because the discipline forbids a silent zero.

- **What happened:** receipt `1000017700.jpg` (a Pingo Doce grocery receipt) did not score as a miss. The read **raised a `ValidationError` and crashed out of scoring**, dropping n from 26 to 25.
- **Root cause:** the vision model transcribed the receipt's printed VAT table with **European comma-decimals as strings** (`'32,95'`, `'1,98'`, `'13,31'`). Our result model's float fields rejected them, and the exception propagated and killed the whole read. (The *same* receipt had parsed fine in an earlier single read where the model happened to emit dot-decimals — so it was a latent locale bug, exposed by model non-determinism.)
- **Why the discipline mattered:** a conventional "just report the accuracy" harness would have let that receipt silently vanish from the denominator. The headline number would have looked *cleaner* (one fewer hard receipt), while hiding both a lost data point and a real bug. The rule **"unmeasured = NO_DATA with a cause, never a silent zero"** is precisely what forced it into the open.

## The fix (what changed because of the measurement)
- `app/models.py`: added `_to_number`, a comma / thousands-separator / currency / percent-tolerant coercion, applied via `mode="before"` validators on the numeric fields of `ExtractionResult`, `LineItem`, and `TaxLine` — `'32,95'` → `32.95` (correct capture, not merely non-crash).
- `app/services/extraction.py`: guarded both payload→model conversions in the read loop so a single malformed orientation is logged and skipped, and the fallback degrades to a low-confidence read (which lands in human review, never auto-posted) rather than raising. **A receipt can no longer silently drop.**
- Tests: +15 (comma-decimal tax lines and scalars, coercion edge cases, and a no-drop guarantee through the full read path). Suite **287 → 302**, all green.
- **Commit:** `2309342` (pushed; CI green). The exact crashing payload is now a regression test, so the denominator cannot silently shrink again.

## Honest caveats
- n is small (25 scored / 26 labelled); differences of a few points are not statistically significant.
- The real receipt images and labels are private (PII) and git-ignored, so the exact set is not reproducible by a third party; the pipeline, the harness, the mock, and the full test suite are public and runnable.
- Fleet identity is `NO_DATA` (outside machine) — these figures are M1's own, claimed with their command, not a PreceptorOS rack measurement.
