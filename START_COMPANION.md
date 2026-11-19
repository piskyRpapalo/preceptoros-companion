# Start as a Companion — with your own external agent

**Status: public guide to the existing docs-only door.** This is not permission to connect a node, grant agent capabilities or appear live in OpenWorld. The signed [CONTRACT.md](CONTRACT.md), [GROUNDTRUTH.md](GROUNDTRUTH.md), [GUIDE.md](GUIDE.md) and [CONTRIBUTING.md](CONTRIBUTING.md) take precedence.

A Companion is a **person with their own project and tools**. The house reads only what that person chooses to declare and measure, never the project's private code or signing keys. External agents may help prepare proposals, but never sign or publish on a person's behalf.

## Step 1 · Get the app or use the manual door

Open [Get the app](https://preceptoros.org/get-the-app/) and choose your device, but verify the file and product before installing. A published download is not proof of an independent person's complete installation.

- **Linux:** an installer is offered; the APP's isolated-home source smoke was measured, but not an independent collaborator's complete install.
- **Windows:** an installer is offered; **NO_DATA(windows_installer_E2E_unverified)**.
- **Android · native MINI (verified release, 2026-11-19):** use the [official Android v7 release](https://github.com/piskyRpapalo/preceptoros-app/releases/tag/android-mvp-v7-20261119), not the legacy OpenWorld wrapper. The native APK is `PreceptorOS-android-0.3.0-v7.apk` (155,998,639 bytes; SHA-256 `9c4d227db2ba395cdb232bdd3eb6a52f83d344f3386a99bb5274d42837eebe6b`; `org.preceptoros.app`, versionCode 7). It includes the six-panel APP, local Mini routing and an embedded SmolLM2-135M GGUF / ARM64 inference engine. Physical S110 inference was observed; do not assume another phone passed the same tests. As checked on 2026-11-19, the public `/get-the-app/` page **still linked to legacy Android 1.0.1 TWA**, so the release URL above is the verified native choice until a fresh web check demonstrates otherwise.
- **Your model and tools:** you may use your own agent, local model or external provider. **Hexelion is not required**. Do not provide the house with private endpoint addresses or credentials.

If your installed APP has **My node → Node identity** (or the corresponding Settings entry in an older build), save your local Companion draft there. A local draft, public declaration or downloaded APK is **not** an approved or LIVE node. If this feature is absent, follow the same steps manually. Public node admission and signed provisioning remain separately gated. For the first four collaborators, read the [dated Companion field guide](FIRST_FOUR_COMPANIONS_20261119.md), including why a separate WhatsApp GGUF does not need to be imported into Android v7.

## Step 2 · Prepare only public facts

Choose your companion folder slug (1–24 lowercase letters, digits or hyphens, beginning with a letter or digit). Prepare the project name, who it serves, what it solves, its stack and what you can demonstrate. Every reported measurement needs **a command, a date, and a machine**. An unmeasured result must be **NO_DATA(cause)**, never a fabricated PASS.

Keep secrets, private memory, access tokens, passwords, internal addresses and private Ed25519 keys out of the handoff, the agent's transcript and GitHub.

## Step 3 · Give the external agent a bounded brief

Copy this prompt into an agent you choose, substituting your own companion slug and *public* project facts:

> **Companion onboarding · proposal only.** Read the public preceptoros-companion repository's GROUNDTRUTH.md, GUIDE.md, CONTRIBUTING.md, CONTRACT.md and AGENT_CARD.md before editing. Help me prepare **only one building**, in companions/MY-SLUG/DECLARATION.md, STATE.md, BUILDING.md, and KNOWLEDGE_INDEX.md based on the project facts that I provide. Use the existing companions/template examples. Do not invent measurements, dates, hardware, signatures or identity; say NO_DATA with a concrete cause. Do not copy secrets, request access to private repositories, authorize actions, open network connections, sign, merge, deploy, provision keys or submit a PR in my name. Show me the complete diff and evidence first. I will review and submit a docs-only PR titled HITL from my fork on branch contrib/MY-SLUG/declaration. A declared agent card is **not** authentication, permission or a working connector. Acceptance of this PR is **not** automatic OpenWorld publication.

The human may refuse or revise the draft. An external agent may suggest measurements but must not present unexecuted tests as completed.

## Step 4 · Human-reviewed declaration

1. Fork [preceptoros-companion](https://github.com/piskyRpapalo/preceptoros-companion) using your own GitHub account. The house does **not** need your account token.
2. Create a branch in your fork called **contrib/MY-SLUG/declaration**. Replace MY-SLUG with your slug.
3. Copy [DECLARATION.md](companions/template/DECLARATION.md), [STATE.md](companions/template/STATE.md), [BUILDING.md](companions/template/BUILDING.md), and [KNOWLEDGE_INDEX.md](companions/template/KNOWLEDGE_INDEX.md) into your own **companions/MY-SLUG/** directory. The folder proposes exactly **one** building; its knowledge sources remain in your own node. Keep them human-authored.
4. Review the diff, measurements, dates and machine descriptions. For hardware outside the rack, explicitly record **NO_DATA(outside_machine_no_rack_identity)** rather than invent a fleet identity.
5. Open a **docs-only pull request** into this repository, titled **HITL · Companion MY-SLUG declaration**. You can do this in GitHub's browser without sharing credentials with an AI.

**Request review (explicit human action):** after opening the docs-only PR, use
[One building · architect review](https://github.com/piskyRpapalo/preceptoros-companion/issues/new?template=one-building-review.md)
to notify the architect of the PR and public building documents. GitHub requires you
to sign in and press **Submit new issue**; the APP cannot send or publish for you.
The maintainer's repository subscription is configured, but delivery to a device is
**NO_DATA(notification_delivery_not_tested)**. The issue is a review request only.
It does not replace PR review, host consent, Ed25519 signatures, or an accepted node.

If you later propose a companion agent, read [AGENT_CARD.md](AGENT_CARD.md) and [agent-card.schema.json](agent-card.schema.json). **F0 remains PROPOSED**. A card requests capabilities but **does not authenticate the agent or grant Talk, Lab or Notebook access**. No real agent can join without a separate key and the hosting node's human-approved, revocable grant.

## One-building proposal · Nexo (17 November 2026)

The scope is deliberately simple: **one Companion → one Nexo building**. The previous multi-building layout of Node 0 is not the collaborator's deployment template. A human may choose any local or external agent; only their approved **public** sources belong in the proposed knowledge file. This does not authorize retrieval of a private repository or a network port.

Copy DECLARATION.md and STATE.md, and additionally fill in knowledge.md and defense.md using the templates under companions/template/. The proposed BUILDING.json is a machine-readable declaration with count 1, never a live deployment ticket. Your agent may prepare the files in your own Companion folder, but the human reviews all public content.

After preparing your fork's docs-only PR, you may open the [architect review request](https://github.com/piskyRpapalo/preceptoros-companion/issues/new) and mention @piskyRpapalo. This is a public GitHub Issue, and it is NOT sent until you confirm Submit. GitHub account access, notification delivery, owner review, identity approval and Web deployment are separate: NO_DATA(external_submit_or_notification_not_verified) until measured.

A future Deploy one Nexo button may request a signed deployment only after the architect accepts the declaration and validates the node identity, source references and revocable permissions. No implementation or deployment is asserted by this template. The expiry of a visitor's temporary occupation must return control to NPC; it never transfers permanent ownership.

## Step 5 · Distinguish the three states

| State | Measured fact | Not implied |
| --- | --- | --- |
| **DRAFT_ONLY** | The human can inspect a local declaration draft | No PR, grant or public listing |
| **DECLARATION_IN_REVIEW** | A docs-only PR has been submitted by the person | No trusted agent, territory or listing |
| **DECLARED** | Maintainers have accepted a declaration under the proper human sign-off | No live node or automatically published OpenWorld project |

**OpenWorld has another gate:** the host's terms of use must be accepted; node identity and messages require real Ed25519 authentication; network data must follow the signed **atlas.sobre/1** packet contract (strict UTF-8, fewer than 1,024 bytes). The web remains a static renderer with zero hidden requests on load. Until independently measured, the honest state is **NO_DATA(world_publication_not_verified)**.

Acho, the visual status and the machine-readable receipt must report the **same state and cause**. An agent's self-reported completion without a verified receipt is never a completed operation.

## Optional collaboration and data exchange (proposed, not live)

An agent's public card declares requested capabilities; it never grants permission. The node owner must authorize a separate, revocable grant. Public GitHub declarations must contain no private corpus, credentials, model memory, device addresses or signing keys.

**Control and data are different:** an Acho / `atlas.sobre/1` control message must occupy **fewer than 1,024 UTF-8 bytes** (at most 1,023). A future owner-consented file exchange may carry up to **25 MiB** using a separate transport, a SHA-256 digest, a named recipient, an expiry and an independently verified receipt. This limit does **not** mean the current APP or website can already send private 25 MiB packages. The responsible gateway is private Aduana, not the public WEB renderer.

The sender must review the exact destination and contents before emission; the receiver must approve acceptance under its own conditions. An external MCP, AI-generated document, GitHub fork or draft PR never bypasses either owner's human decision. The node's kill switch and explicit revocation remain authoritative, including when network services are unavailable.

**State today:** `NO_DATA(private_companion_25MiB_exchange_E2E_not_implemented)`; `NO_DATA(effective_external_agent_grants_not_measured)`. Do not advertise completed remote transfer, model connectivity or LIVE status from a declaration alone.

## Acceptance still outstanding

The independent **download → install → draft with external agent → human PR → accepted declaration → verified OpenWorld project** chain remains **NO_DATA(external_companion_end_to_end_not_exercised)**. The next true acceptance run must use a collaborator's fresh HOME, no Hexelion dependency, a real docs-only PR under that person's control, and a separately authenticated public projection. A simulated PR or signed project cannot replace those observations.
