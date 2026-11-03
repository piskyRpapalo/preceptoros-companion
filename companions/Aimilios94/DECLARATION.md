# DECLARATION.md — Aimilios94 / Receipt Ghostbuster

**What it is.** A personal money assistant that turns a messy expense into a clean, categorized, reconciled record, with a human confirm gate and model evaluations for better performance.

**What it solves.** People lose track of what they spent, how much they spend, and what they buy — including what their most common expense is. It flags unused subscriptions so you stop paying for things you don't need, and gives advice on your expenses for better management and tracking.

**For whom.** Free for everyone ,open-source, whoever needs it can use it.

**Stack.** React + Vite · Python/FastAPI · Supabase · n8n · vision-LLM (gpt-5-mini default) · local Ollama qwen2.5vl option for private on-device reads (still testing more models) · LangSmith (tracing, experiments) · Sentry (error handling and debugging).

**Current state.** Phase 1 shipped through v0.5: extraction + review gate, bank reconciliation, spending breakdown, Ask chatbot, rule-based Advice. The AI never does the math. Both extraction and chatbot ship with measured eval. Next: demo visuals, then a payslip reader (v0.6).
