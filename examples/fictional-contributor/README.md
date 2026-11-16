# examples/fictional-contributor — FICTIONAL

**This contributor does not exist.** It is the house's worked example for `AGENT_CARD.md` (`preceptoros.agent-card/1`, PROPOSED). It is not a companion, is not listed in COMPANIONS.md, and must never be registered on a real node.

## The story it tests

A contributor runs a small local agent, **Lantern**, on their own node. The first deliverable of APP-MESA-03 is that Lantern can, in an isolated test home:

1. **register** — its card is validated and a test-only grant is issued in the throwaway home;
2. **converse** — the person addresses Lantern in Talk; the door reports `DELIVERED_TO_THREAD`; Lantern's adapter replies in its own voice (`ADAPTER_REPLIED_FIXTURE`, because it is unsigned);
3. **examine a document** — the person places `lab/sample-document.md` in the Lab for Lantern (`lab.read_document`); Lantern reads that one file and nothing else;
4. **leave a receipt** — Lantern appends a sanitized receipt (`notebook.receipt`) that the Notebook shows as `NOTEBOOK_RECEIPT_VISIBLE`.

Lantern requests no memory capability: its example shows that an agent can be useful without touching the person's memory.

## Files

| File | What |
|---|---|
| `agents/lantern.json` | the card: `fixture: true`, no key, so it is valid only in isolated tests |
| `lab/sample-document.md` | the document Lantern is asked to examine |
| `ACCEPTANCE.md` | the end-to-end states the APP test must report, separately |
| `VALIDATION.md` | the documentary checks of this proposal and their receipt |

Agent: Claude Code · Model: Opus 5.5 · Run: NO_DATA (cause: no run id is issued to this session)
