# STATE.md — Aimilios94 / Receipt Ghostbuster

Figures exactly as measured. Each carries its command, machine, date, and commit.
What is not measured is declared `NO_DATA` with a cause. Append-only; the operator
owns these figures and the house never re-measures them.

**Machine M1 (dev workstation):** Windows 10 (build 19045) · AMD Ryzen 7 5700G, 8C/16T · 31.4 GB RAM · no discrete GPU (CPU-only inference). Cloud-model figures are orchestrated from M1 over the provider API; local-model figures run entirely on M1, CPU-bound.

**Fleet / rack identity (all figures below):** `NO_DATA` — cause: outside machine, no rack identity. M1 is a developer workstation, not a PreceptorOS rack.

---

## MEASURED

### 1. Receipt extraction — production model accuracy
- **Figure:** overall field accuracy **99.3%** (141/142); receipts fully correct **96.2%** (25/26); n = 26 hand-labelled real receipts.
- **Per field:** vendor 100% (25/25) · date 96% (24/25) · total 100% (26/26) · vat_amount 100% (21/21) · vat_rate 100% (21/21) · category 100% (24/24).
- **Model:** `gpt-5-mini` (OpenAI, cloud API). **Command:** `python backend/scripts/eval_extraction.py`. **Machine:** M1. **Date:** 2026-10-22. **Commit:** `3a7c0fe`. **Artifact:** `backend/eval/RESULTS.md`, `backend/eval/metrics.json`.
- Note: scored on the user-facing fields after the deterministic VAT/amount/category logic — not the raw model JSON (the AI never does the math).

### 2. Model matrix — same pipeline, five models, same 26 receipts
- **Figures (overall field accuracy):** `gpt-5-mini` **98.6%** · `gpt-4o` 92.3% · `claude-haiku-4-5` 86.6% · `qwen2.5vl-receipt` (local, Ollama) **89.4%** at **$0.0000/read** · `claude-opus-4-8` 98.2% (n = 20, frozen).
- **Command:** `python backend/scripts/eval_models.py`. **Machine:** M1. **Date:** 2026-10-22. **Commit:** `de4b282`. **Artifact:** `backend/eval/MODELS.md`.
- Note: n = 26 is small — read as direction, not a leaderboard. `gpt-5-mini` is the production pick; the local model is the private/$0 option.

### 3. Ask chatbot — NL Q&A quality (live)
- **Figures:** tool-selection **18/18** · answer-correctness **18/18** · refusal **5/5** · prose faithfulness **18/18** (calibrated LLM-as-judge → **TRUSTED**) · overall **100%** (41/41).
- **Model:** `gpt-5-mini` (live, cached). **Command:** `python backend/scripts/eval_chatbot.py --live --judge`. **Machine:** M1. **Date:** 2026-10-25 (eval reference date 2026-10-31). **Commit:** `59a6457`. **Artifact:** `backend/eval/chatbot/RESULTS.md`, `metrics.json`, `CALIBRATION.md`.
- Note: answer-correctness is graded in **code** (the tool is dispatched over a committed synthetic ledger and its structured result compared to the expected figure — no LLM judge). The judge grades only prose faithfulness, and only after it was calibrated to 100%/100%/100% against 14 human-confirmed examples. Set is small (18 Q) by design — reproducible and public-safe.

### 4. Test suite
- **Figure:** **302 passed.** **Command:** `python -m pytest` (in `backend/`). **Machine:** M1. **Date:** 2026-11-03. **Commit:** `2309342`. (Was 287 at commit `9e39cab`; +15 from the fix in the lab note below.)

### 5. Local on-device model — full BENCHCARD
- **Headline:** `qwen2.5vl-receipt` (Ollama, Q4_K_M, num_ctx 16384) = **86.6%** field accuracy (123/142) over n = **25**, **$0.0000/read**, latency p50 270s / p95 978s, prompt-injection slice 100%. **Date:** 2026-11-03. **Commit:** `9e39cab`. **Machine:** M1 (CPU-only).
- **Full card + the dropped-receipt case:** see `companions/Aimilios94/lab/2026-11-03-ollama-qwen2.5vl-receipt.md`.

---

## NO_DATA (declared gaps)

- **Production / real-user metrics** (uptime, latency under load, real-user accuracy): `NO_DATA` — cause: not yet deployed to real users; local + demo only.
- **Payslip reader (v0.6)**: `NO_DATA` — cause: designed, not yet built.
- **Fleet identity on every benchmark**: `NO_DATA` — cause: outside machine, no rack identity (see header).

---

★ **Note — on the measurement discipline itself.** This project adopted PreceptorOS's measurement discipline: every public number carries a state label and a measurement receipt (command · machine · date · commit · artifact). Applied to our local-model eval on 2026-11-03, the rule *"unmeasured = NO_DATA with a cause, never a silent zero"* immediately earned its keep — it surfaced a real bug that a conventional "just report the accuracy" harness would have hidden: one receipt did not quietly become a *miss*, it **crashed out of scoring entirely** (the model transcribed a VAT amount with a European comma, `'32,95'`, which our float parser rejected), silently shrinking the denominator from 26 to 25. The discipline forced the drop into the open; we fixed the parser and hardened the pipeline so a receipt can never silently drop again, with a regression test (tests 287 → 302). Credit to David / PreceptorOS — the method graded our harness, not just the model, and the harness lost. The full worked example is in `lab/`.
