# DEPRECATED LEDGER · the old parts behind each new thing

Status: LIVING LEDGER, append-only. Filed by la Mesa (GLM/Vibe), 2026-11-08. Mother: the Sovereign's decree «cuando claude haga algo nuevo, busca las partes antiguas y escribe deprecated».

Rule: when the builder lane merges a new piece, la Mesa sweeps for the old parts it leaves behind and appends one row here. The row names the old part with file and line, its cause, and the marker text. The in-repo marker (a DEPRECATED comment at the old part) is written by the builder lane: edits under public/ carry the seal. This ledger is the public record that the marker cites. History stays append-only; nothing is deleted; an archive row never takes the marker.

Measured at web main abfb5bc6 (seal gq) on 2026-11-08.

## Rows

D-01 · New: Q-04. The visible leaf of the terminal reads Help (public/game/terminal_panel.js:79, labels = { Welcome: 'Help' }; the leaf's icon is the question mark). Old: the word Welcome as the load-bearing key. Measured: public/game/terminal_panel.js:64,66,74,79; public/game/gamepad.js:64; public/game/world_feed.js:81; public/game/welcome_card.js:1,10; public/game/talk.css:46,51,72 (data-cat=Welcome); public/openworld/index.html:33-34 (speaker key, sheet-welcome, welcome-h, the first-run heading); the precache path welcome_card.js (public/sw-listas.js:28; public/openworld/index.html:125). Cause: the label is new, the key is old. Marker text: DEPRECATED NAME · the visible word is Help (Q-04); this key is an alias. The file welcome_card.js stays live: it is the first-run card. What is deprecated is the old name, not the file.

D-02 · New: Q-03. The visible button and sheet title read Node (public/game/building_sheet.js:88 button with name Node, id gp-town; :94 heading Node). Old: the word Town in ids and comments. Measured: public/game/building_sheet.js:2,83; public/game/town_actions.js:1 (file name and header); public/game/gamepad.js:108; public/game/map_aura.js:2,58,68; public/game/panel_x.js:2; public/game/visitor_battle_ui.js:7; public/game/talk.css:44 (#gamepad #gp-town); docs/reparto-paneles-20261108.md section 2, cited by the code. Cause: the visible rename landed; the ids and comments keep the old word. Marker text: DEPRECATED NAME · the visible word is Node (Q-03); this id and comment are aliases. The id rename is its own piece with its own seal.

D-03 · Q-06 (no sign-for-adoption step). Measured: zero occurrences of the old step in code and docs at this head. Clean removal. No orphan to mark.

D-04 · Q-02 (ghost guardians patrol inside their hexagon). Measured: no orphan code. The two remaining patrol lines describe the new deterministic patrol (public/game/visitor_battle.js:14; public/game/visitor_play.js:71). No marker needed.

D-05 · Q-09 (the crab's bubble rests minimized). Measured: the change lives inside the bubble's own code; no orphan file found. No marker needed.

D-06 · Archive rule. Ten task files and one canon doc still carry the old words (Town, Welcome), measured under odd/tasks and docs/canon-map-details-20261107.md. History is append-only. History is not deprecated; it is history. The marker never lands on archive rows.

D-07 · Standing note. PR #781 (open at this filing, click-trail) announces a DEPRECATED.json pattern of its own. When it merges, its deprecations append here as new rows. PR #780 (Rust workspace) stays a lane ruling for the Sovereign, not a deprecation row.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
