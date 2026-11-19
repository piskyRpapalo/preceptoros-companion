# PreceptorOS · First Four Companions
## Sovereign AI co-working · Field guide and invitation · 19 November 2026

**Audience:** four initial independent collaborators and their chosen AI assistants.
**Founder and governance author:** David Pecero Caballero.
**Drafting preceptor:** Codex GPT-6.
**Status:** public onboarding **proposal**; not a grant, deployment approval, legal certification or proof of a live service.

PreceptorOS is an open-source AI co-working ecosystem: independent people develop their own projects, models, services and evidence, while making selected parts available to a community governed by human consent. Its long-term direction is a federated, open-source AI governance network, potentially with DAO-like or another human-agreed governance structure. **No DAO or automatic member authority is established by this invitation.**

The first four companions are invited to experiment, help shape the community and propose improvements. Each is sovereign over their own devices, data, models, permissions, budget and project. Joining a public conversation does not surrender any of these.

## 1 · What you received on WhatsApp

You received two separate files:

| File | What it is | What it does not do |
| --- | --- | --- |
| `PreceptorOS-android-0.3.0-v7.apk` (155,998,639 bytes, about 156 MB) | The native Android PreceptorOS APP, with six MVP panels, a deterministic Mini router and an embedded ARM64 GGUF inference engine. | It does not create an approved or LIVE public node merely by opening. |
| `base-web-q4km.gguf` (105,454,144 bytes, about 100.6 MiB) | An independent copy of **SmolLM2-135M-Instruct, Q4_K_M**, for experiments with a compatible local runtime. | It is **not** an installable Android app or an importable model in the current APP model selector. |

**The APK already contains the same SmolLM2-135M model** as `assets/offline-mini.gguf` and `lib/arm64-v8a/libmini_llama.so`. Do not install Ollama, duplicate the GGUF in Android private storage, or rebuild the app just to complete the initial test.

Official release and integrity reference: [PreceptorOS Android v7](https://github.com/piskyRpapalo/preceptoros-app/releases/tag/android-mvp-v7-20261119).
APK SHA-256: `9c4d227db2ba395cdb232bdd3eb6a52f83d344f3386a99bb5274d42837eebe6b`.
SmolLM2 GGUF SHA-256: `ed5fa30c487b282ec156c29062f1222e5c20875a944ac98289dbd242e947f747`.
WhatsApp is a delivery channel, not a cryptographic proof of provenance. Compare hashes where your device supports it; otherwise declare `NO_DATA(transfer_digest_not_checked)`.

**First experiment:** install the APK on a compatible Android ARM64 device, open Talk, close **Choose model** (that selector lists *external/personal* connections), and ask a free question. Test twice with different prompts and again offline if the owner agrees. A deterministic greeting or `NO_DATA(model_catalog_unavailable)` does not prove generative inference. Record an actual on-device reply and its source, or `NO_DATA(mini_inference_not_verified_on_this_phone)`. Preserve previous installs and local data: do not uninstall or clear storage to troubleshoot.

## 2 · Your chosen AI is your guide, not your owner

Use the web or local AI assistant you prefer: Claude, ChatGPT, Mistral, Gemini, a local model, or another agent. The individual chooses their provider, costs and permissions. An AI assistant may read public repositories, explain the system, draft an owner's project declaration, suggest a local model, review evidence, and prepare changes for human inspection.

**The assistant may not infer permission** to read private files, connect to devices, publish a private database, create a public node, transfer documents or deploy software. A consumer chat subscription does not automatically grant API, GitHub or device access. A connector/MCP has only the capabilities the individual explicitly authorizes. No founder or collaborator receives the other person's GitHub login, private signing keys, personal memory or device administrator credentials.

## 3 · The sovereignty contract

1. **Individual ownership.** Each person exclusively controls their own private data, device, node policy and project. Public material is published by deliberate choice.
2. **Human-in-the-loop (HITL).** Each person is responsible for approving their own actions. A SHA-256 hash proves byte integrity, **not identity or consent**. Ed25519 / the applicable signed-receipt contract proves specific cryptographic authorization when a verified key and scope are present. Neither a model's text nor a hash alone is a human signature.
3. **EU-oriented engineering.** Design and review software against applicable EU requirements, including data protection, security, accessibility and the EU AI Act as relevant to the specific use. A statement of intent is **not** a compliance assessment or certification.
4. **Declared telemetry.** State exactly what is measured or transmitted, by whom, for which purpose and for how long. Default to no unsolicited remote telemetry; no secret logging. An explicit per-service declaration does not itself authorize transmission.
5. **Acho accessibility.** The same status, action, cause and receipt must be available in readable text, speech/screen-reader form and machine-readable form. Make it usable by blind users and small local models, not merely visually attractive.
6. **Fail closed.** When a capability, connection, receipt or approval is missing, report `NO_DATA(cause)` or the correct pending state. Never advertise a pending node as LIVE.

## 4 · Who controls which door?

Think in three parts: **the Window, the Door, and the Node**.

**The Window — [preceptoros.org/#openworld](https://preceptoros.org/#openworld):** publicly readable OpenWorld. Anyone may visit without installing the APP. A visitor is an ephemeral visitor, not an authenticated node owner. Public visitors may interact only with services that a node owner has **actually enabled** under displayed conditions and verified permissions.

**The Door — PreceptorOS APP:** an owner's private consent and capability interface. **The intended only path for admitting a new owner node is an APP-originated, cryptographically authenticated request**, reviewed by the community gate and subject to both the owner's and the ecosystem's human approvals. A form, a GitHub PR, a copied APK, a browser User-Agent or an AI message is never sufficient evidence that a real APP owner has authorized a LIVE node.

**The Node — your hardware:** your selected local or server model, private knowledge, RAG/harness if independently wired, logs, streaming services, media tools and revocable network policy. The owner determines what is offered to visitors and other nodes. The public Window must not gain arbitrary access to this territory.

### Permission ladder — deny by default

| State or operation | Required authority | Never imply |
| --- | --- | --- |
| Read public guides, copy public templates, visit OpenWorld | Public read access | Identity, membership or admission |
| Draft an identity, project, prompt, local documents or a building | Individual's local action | Public visibility or data export |
| Let a local AI inspect private data or use an MCP/device | Owner's explicit, least-privilege and revocable authorization | Automatic access for other collaborators |
| Publish a public Companion declaration or a proposed mission | Owner-reviewed public content; PR and the repository's human review | A node certificate, services online or merge |
| Submit a node admission request | Owner consent in the APP, authenticated identity, anti-replay checks, gate acceptance | Approval or provisioning |
| Approve / provision a node | The proper human signers, signed credentials and verified server-side policy | A live heartbeat |
| Mark a node **LIVE** or offer a chatbot/stream | Fresh authenticated heartbeat **and** demonstrated reachable, authorized service | LIVE from an icon, declaration or cached stale reading |
| Send private data between peers | Both owners' consent, recipient/scope/expiry and a separate verified transfer | General-purpose access to the sender's memory |
| Revoke, stop or disconnect | Each owner's local kill switch and revoked permissions | Continued remote access after revocation |

**Door implementation requirements (target, not yet verified end-to-end):** individually generated and owner-held signing key; challenge/nonce to prevent replay; verified Ed25519/SSHSIG as appropriate; identity-to-key binding; explicit action scope, expiry and revocation; server-side signature and policy checks; per-node rate limits; no sensitive default logs; independent heartbeats; accessible consent and kill-switch state. The founder controls admission to the shared Window; **the owner controls their local Door and every service they offer**. Neither side should be able to grant itself the other side's authority.

## 5 · Acho: small control messages, larger consented files

Acho is the compact expression of shared state: a **mathematical screenshot** in the metaphor of an accessible, deterministic state representation. The existing `atlas.sobre/1` control envelope is **strict UTF-8 and smaller than 1,024 bytes** (at most 1,023 bytes). This is for concise signed A2A control, state, consent and receipts — **not** for sending a model, video or a 25 MiB knowledge pack inside a control message.

**Future separate data transport: up to 25 MiB per consented package.** The proposal allows a person's AI to prepare a private information package for a specifically named collaborator, with explicit sender review, independent recipient acceptance, SHA-256 digest, byte limit, purpose/scope, expiry, signed receipt, integrity validation and revocation. The data plane should use a protected, access-controlled, preferably end-to-end encrypted route; the tiny Acho envelope carries only a bounded reference and authorization metadata. Transport, scanning, retention, and receipts require separate security tests.

**Current truth:** `NO_DATA(private_companion_25MiB_exchange_E2E_not_implemented)`. WhatsApp can pass a user-selected file manually, but this is not the protocol's consented private transfer service. Neither an AI prompt nor a public PR activates that service today.

## 6 · Keep two kinds of private record separate

**Local owner store:** the APP and the person's own devices retain identity drafts, selected documents, model settings and private sources. Do not assume imported documents automatically become searchable RAG or that the Android Mini can retrieve them. Back up with the owner's consent and verify restores before relying on them.

**Owner-controlled online coordination store:** if helpful, create a **private GitHub repository under the collaborator's own account** for reviewed plans, public/private boundaries, signed proposal receipts and collaboration decisions. This is a reviewable coordination ledger, not a replacement for the local database, nor a guarantee that GitHub is the runtime database. Share only the metadata needed for a task; keep sensitive data and signing keys local. Cloud services and MCP tools must be scoped, authenticated and revocable.

The founder's `preceptoros-private-mesa` is **not automatically a database or shared private workspace for each participant**; access is restricted. Use the **public Mesa** to collaborate on public missions and a personally controlled private repository for private coordination. Do not copy private-Mesa content without permission.

## 7 · A stronger model on your own hardware

The phone Mini is a **small experimental starting point**, not the finished decision intelligence. When ready, the owner can run a more capable, legally usable model on their own laptop, desktop, GPU host or server, choosing a verified local engine and hardware-compatible weights. Their preferred cloud AI may help plan installation but does not gain control of the machine by default.

The sequence is: inventory your hardware → select a model and runtime → obtain and verify weights/licence → test offline generation → measure latency, memory, quality and energy on your device → configure a narrowly scoped connection in your APP **only where a working, authenticated adapter exists** → grant particular services to your Companion. Do not publicly expose a local inference endpoint or claim a production connector based on a saved model name.

A semi-deterministic LoRA decision model is a **research direction**. Deterministic validation and an owner-controlled database remain authoritative; an LLM or LoRA may recommend decisions but cannot become the signing authority or substitute for structured data and revocable permissions. An owner's public chatbot may eventually answer from an authorized harness/RAG, or instead offer their own audio stream, educational service, coding tool or media generator, each with its own conditions.

## 8 · One proposed Companion, one possible OpenWorld territory

A participant chooses a name and an individual project. The first public deliverable is a **docs-only declaration**, not a network port or a live machine. The public invitation describes a future territory/hexagonal tower; visual presence in OpenWorld must follow an approved identity and verifiable service state. A prepared building or accepted PR never implies automatic LIVE registration.

**As checked on 19 November 2026:** the official Android v7 APK is publicly released; physical S110 inference was previously observed. The current web `/get-the-app/` still advertises the legacy 1.34 MB OpenWorld wrapper rather than the native v7 APK. Public `POST /api/v1/deployment-requests` returned HTTP **404** / `ruta_ausente`; the public credential register lists zero entries; available heartbeat rows do not establish the four new Android nodes. Therefore `NO_DATA(first_four_public_node_admissions_and_live_heartbeat)`. Use the official [v7 Release](https://github.com/piskyRpapalo/preceptoros-app/releases/tag/android-mvp-v7-20261119) rather than the legacy web APK until the deployment is verified.

## 9 · Copy public patterns, not someone else's authority

These are **public sources**, readable without the founder's private repositories:

- [preceptoros-app](https://github.com/piskyRpapalo/preceptoros-app) — Android/APP source, local Mini and measured interface; inspect `AGENTS.md` before modifying.
- [preceptoros-web](https://github.com/piskyRpapalo/preceptoros-web) — the shared Window and public OpenWorld.
- [preceptoros-companion](https://github.com/piskyRpapalo/preceptoros-companion) — the existing public declaration door. Read [START_COMPANION.md](START_COMPANION.md), [GROUNDTRUTH.md](GROUNDTRUTH.md), [GUIDE.md](GUIDE.md) and [CONTRIBUTING.md](CONTRIBUTING.md). Copy `companions/template/` into a personal, human-reviewed `companions/<your-slug>/` proposal.
- [preceptoros-public-mesa](https://github.com/piskyRpapalo/preceptoros-public-mesa) — public, agent-readable missions and proposals; humans set priorities and approve their changes. Do not publish private memory or authorization material.
- [lab](https://github.com/piskyRpapalo/lab) — reproducible methods, benchmark templates and privacy-safe receipts. You can keep your own private results and submit chosen public measurements through the Companion channel.
- [study](https://github.com/piskyRpapalo/study) and [babel](https://github.com/piskyRpapalo/babel) — governance, contracts, terminology and provenance.

Your own private project may borrow the **structure** of a Mesa, Lab, Notebook and signed receipts, but do not copy the founder's private content or claim his signing authority. Public missions belong in the appropriate Mesa; tests and code belong in their owner repositories. External AI assistants should read public contracts before proposing work.

## 10 · A practical first session (no programming required)

1. Confirm the APK and GGUF names received in WhatsApp. Verify integrity if possible. Install and open the **native** APK without deleting another version.
2. In Talk, ask two different non-scripted questions. Record whether the response is deterministic, actual **on-device model output**, or `NO_DATA(cause)`. Test without connectivity only with device-owner consent.
3. In My node, choose a local Companion name, purpose and public prompt. Save locally; close and reopen. Do not put secrets in the public prompt.
4. Ask your preferred AI assistant to read the public Companion guide and draft one project declaration and a measured state card. You review all facts and choose what stays private.
5. Optionally fork the public Companion repo under **your own GitHub account** and submit a docs-only `HITL` PR. Human review, acceptance, node admission and LIVE provisioning remain different steps.
6. Describe one service you might eventually offer (chatbot, audio, educational tool, research, or media work), its audience, permitted data and kill switch. Measure before advertising availability.

### Prompt to paste into your preferred AI assistant

> I am one of the first independent PreceptorOS Companion experimenters. I received the native Android v7 APP (about 156 MB) and a separate SmolLM2-135M Q4_K_M GGUF (about 100 MB) through WhatsApp. Do not assume the file transfer proves the APK's checksum, and do not download or install another model first: the official APK already embeds this GGUF and a native inference engine.
>
> Act as my **proposal-only, privacy-first technical guide**. Start with public sources at https://github.com/piskyRpapalo/preceptoros-companion (START_COMPANION.md, GUIDE.md, GROUNDTRUTH.md, AGENTS.md), then preceptoros-app, study, lab and preceptoros-public-mesa as needed. Follow the repository's declared reading depth, existing templates and rules. Explain the APP's separate local Mini and external model selector. Guide me through two actual offline response tests, local identity/preferences and a restart test, without wiping data. If this phone cannot demonstrate inference, name the precise NO_DATA cause instead of improvising a second installation.
>
> Help me design **one unique project**, one optional public service and a precise private/public boundary. Prepare drafts of DECLARATION.md, STATE.md, BUILDING.md and KNOWLEDGE_INDEX.md from **facts I provide**, never invented figures. Suggest how a stronger local model might run on my own available hardware, but ask before accessing any device or using GitHub, MCP, cloud provider or billable service. Public Github work is via my own fork and my reviewed docs-only HITL PR.
>
> Explain what I can do today versus future services: Acho control envelopes below 1,024 UTF-8 bytes; a **proposed**, not yet operational, separately consented 25 MiB data plane; public visitors versus owner-authenticated nodes; grant scopes, two-sided permission, cryptographic signatures, expiry, revocation and kill switch. Never transmit private documents, credentials or hidden telemetry. A public declaration does not create a LIVE OpenWorld node.
>
> Report each outcome as **CODE_EXISTS / DEVICE_TESTED / PUBLIC_SERVICE_VERIFIED / NO_DATA(cause)**, with date, device class, evidence and next safe step. Keep me as final signer and owner.

---

**Invitation, not enrolment:** Participation in the community, hosted services, AI-to-AI exchange and any future DAO-like institution remains voluntary, independently reviewed and governed by the affected humans. The network can share methods without absorbing its members' private projects.

**Maintainer sign-off:** PENDING_HUMAN_REVIEW. This guide introduces no new authority, production service or change to existing signed contracts.
