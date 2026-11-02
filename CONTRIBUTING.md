# CONTRIBUTING.md — preceptoros-companion

## For human companions

1. Create your folder: companions/<your-name>/.
2. Write DECLARATION.md: what your project is, what it solves, for whom, stack, current state.
3. Write STATE.md: your measured figures — accuracy, tests, cost, run date, machine. What you have not measured, declare as NO_DATA with a cause.
4. Open a docs-only PR titled REQUIERE_FIRMA. It is covered by the permanent ODD FIRMO (decree 2026-10-28). A text-only PR does not need piece-by-piece signatures; the Mesa merges citing the ODD FIRMO in the receipt.
5. Branch naming: contrib/<your-name>/<topic> from main of this repo.

## For outside machines

Benchmarks from machines outside the rack travel as they are: the fleet identity is NO_DATA with cause "outside machine, no rack identity". The session format supports self-preference sessions. Benchmarks live in companions/<your-name>/lab/, never in the core lab repository.

## For house agents

See AGENTS.md. You propose; the companion signs.

## Never

- No served code in this repo.
- No rewriting history: declarations and measurements are append-only.
- No figures without a date and a machine.
