# WELCOME.md — for `<companion-name>` and your agent

From the house to the companion. This is the handoff: read it, then act.

## What the house decided about you

You are not a PR contributor to the core repositories. You are a **companion**: a human with their own project who works under the PreceptorOS doctrine. The door for that is this repository. Your folder is `companions/<your-name>/`.

## The ground truth

Before anything you build touches the ecosystem, read `GROUNDTRUTH.md` at the root of this repository (decree 2026-11-02): the window (the static web, zero external requests on load), the door (the app and its conditions of use), the node territory (yours — the house never touches your internal code, only how you connect), and the ephemeral account flow (every interaction of an ephemeral user is signed — HITL, Ed25519 — under the host node's conditions, travelling in `atlas.sobre/1` packets under 1024 bytes). Every integration proposal is reviewed against its four doctrinal checkpoints.

## Your first move (the only one that matters now)

Write, in your own words, from your own measurements:
- `DECLARATION.md` — what your project is, what it solves, for whom, stack, current state.
- `STATE.md` — your measured figures exactly as measured: accuracy, tests, cost, **run date, machine**. What you have not measured: declare `NO_DATA` with a cause. Never invent.

Then open the PR (`contrib/<your-name>/declaration`, docs-only, `REQUIERE_FIRMA`). The house does not write these files for you and never re-measures your figures.

Welcome to the door. — The house, by order of the Sovereign, 2026-11-02.
