# ACCEPTANCE.md — what the APP end-to-end test must report (PROPOSED)

These are the acceptance states for the fictional contributor's path. They are written before any APP code exists, so the test cannot be bent to fit the code. Each state is reported on its own line; one state never stands in for another.

| # | Step | Pass state | Not a pass |
|---|---|---|---|
| A1 | Card validation | `CARD_VALID` (schema, under 1,024 B, no duplicate keys, closed vocabulary) | any schema failure → `CARD_INVALID {cause}` |
| A2 | Fixture fence | the unsigned card is accepted **only** in a throwaway test home on the door's test path | accepted against a real home → **failure of the test itself** |
| A3 | Grant | a test-only grant ⊆ requests exists in the throwaway home | card present without grant → every request refused `no_grant` (this refusal is also asserted) |
| A4 | Talk delivery | `DELIVERED_TO_THREAD` with the thread number `n` | — |
| A5 | Agent reply | `ADAPTER_REPLIED_FIXTURE`: a later thread message in voice `lantern` with `in_reply_to = n` | no reply in the window → `NO_DATA {no_adapter_reply}`; A4 alone is never reported as a reply |
| A6 | Document | Lantern's reply quotes `lab/sample-document.md` exactly and answers the gate question with NO_DATA | quotes from any other file → failure (`read_outside_placed_document`) |
| A7 | Receipt | `NOTEBOOK_RECEIPT_VISIBLE`: the Notebook projection lists Lantern's receipt with its sha256 | receipt written but not projected → `NO_DATA {receipt_not_projected}` |
| A8 | Refusals | `memory.propose` (not requested) refused; a message claiming voice `soberano` refused; a card requesting an unknown capability refused | any of these accepted → failure |
| A9 | No egress | no request leaves the loopback during the run | any outside request → failure |
| A10 | Production line | a reply signed with a key admitted in babel `registry/keys/` → `ADAPTER_REPLIED`; unsigned or wrong key → `REPLY_UNVERIFIED` | NO_DATA until authentication (layer 2) is built |

The same table, with `lantern` replaced by the house's local brain and `fixture: false`, is the acceptance for connecting the house's colony (F6): same door, same states, no reserved route.
