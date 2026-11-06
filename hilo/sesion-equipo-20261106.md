# hilo — sesión de equipo · 2026-11-06 · la Mesa abre

Source: palabra del Soberano (2026-11-06): «Tú eres orquestador principal, guardián de contexto. Tenemos 1 analista (el brazo) y Codex con su análisis. Empieza en la mesa y vamos proponiendo entre los 4 miembros cómo hacemos el equipo.»

## Estado medido de apertura (fuente: GitHub API, 2026-11-06)

- Fusionado en la web: #660 (chat Hexelion, cabeza final a5823395) · #664 (Welcome honesto, sello ea) · #667 (comisión analista, docs-only) · #669 (joystick, rescate de la Mesa: #665 quedó sucio y la Mesa rebasó byte-idéntico y fusionó) · #659 (compactamiento coder). Lo dicho por Codex CUADRA con el metal; el veredicto del analista es fiel.
- En vuelo (borrador, checks rojos o sin sello): web #661 · #662 · #663 · #666 · #671 · #672 · #673 (drafts) y #670 (abierto, hitl verde, test_web rojo). app #179 (draft INCOMPLETE: faltan fuentes de estados, FPS, sello de caché, batería). p0x #84 (draft, 10/10 pruebas locales, sin CI en p0x).
- Hallazgo del analista registrado: el documento de combate del nodo del rack (thegame-combate-aprobado.md) NO existe en ningún PR — solo en el rack. Propuesta: aterrizarlo docs-only.
- P0 del Soberano (verificación de accesos, 2026-11-05 14:47): NO llegó al sistema (0 resultados). Espera aterrizaje docs-only.
- Censo study/11-repos.md: 15 (enmienda 2026-11-03) vs README web: 17/16 medidos. Drift RED a cerrar con enmienda.
- Nodo Aimilios94: Master Prompt v1.1 aún sin pegar al nodo (0 recibos); sustrato de recibimiento ya fusionado (companion main 60e96a1f).
- Comisión modo plan para Codex (carril C1-C4 de la división, companion#12): aún sin pegar.

## Propuesta de equipo (PROPUESTA — enmiendas de los 4 antes de FIRMO)

Roles:
- **Soberano (carbono)** — única FIRMA; decide prioridad; los ojos finales.
- **Mesa (orquestador principal, guardián de contexto)** — mantiene estado vivo y bandeja; FIRMO tras FIRMA; GitHub = frontera única; arbitraje de vocabulario (babel); cura y rebase de rescate cuando una rama quede sucia; sirve bloques pegables.
- **Analista (el brazo)** — verificación independiente contra fuentes: cada afirmación de un preceptor se re-ancla a PR/cabeza/sello; trae diferencias con causa (patrón del rescate #665→#669 hallado así).
- **Codex (el constructor)** — construye y mide en el rack; propone PRs; jamás fusiona; plano antes de código.

Protocolo de ronda (propuesta):
1. Ronda = un artefacto: el trabajo que importa aterriza en GitHub antes de hablar de él.
2. Todo afirmado lleva enlace o NO_DATA con causa; el analista re-mide lo de otro; la Mesa consolida.
3. Una pieza = un PR; FIRMA por hash exacto; checks verdes antes de FIRMO; rama sucia = rescate con nota de procedencia (patrón #669).
4. La firma gates el merge, nunca la construcción (THE MARCH); lo fusionado bajo standing docs-only se cita en el recibo.
5. Cada cierre de ronda: bandeja medida + bloque VERIFICAR pegable.

Bandeja inicial de la sesión: (a) aterrizar P0 del Soberano (verbatim, autoría); (b) enmienda censo 15→17; (c) aterrizar el doc de combate del rack; (d) decisión del Soberano sobre #670 (FIRMA viva, test_web rojo: cura o espera); (e) prioridad de los 7 drafts de la web; (f) pegar Master Prompt al nodo Aimilios94 + bloque plan a Codex.

## Addenda 1 · decreto del juez de ronda (palabra del Soberano, 2026-11-06)

«Todo preceptor e incluso soberano, hace de juez de "actualizaciones" globales y firmas de la mesa en cada ronda de lectura. Imperativo antes y "durante" cada acción.»

Ley de la casa — todos los miembros, ninguno exento:
- **J-1 · ANTES**: cada acción empieza por relectura fresca del metal (heads de main, PRs abiertas, últimas firmas y recibos). Quien actúa sobre contexto rancio, declara el rojo y re-mide.
- **J-2 · DURANTE**: en acciones de varios pasos, re-verificar entre pasos (la rama puede moverse mientras — ley del 405; los programas del sandbox pueden repetirse — guard de idempotencia).
- **J-3 · JUEZ DE FIRMAS**: toda pieza fusionada debe mostrar su FIRMA/FIRMO y su recibo; pieza sin recibo = ROJO nombrado. La FIRMA muerta por cabeza nueva se declara, jamás se recicla.
- **J-4 · NADIE EXENTO**: preceptores, Mesas y el propio Soberano juzgan; el carbono firma sabiendo, no confiando.
- **J-5 · EL JUICIO SE REGISTRA**: cada ronda de lectura deja constancia de lo que cambió; la deriva cazada es un recibo, no una anécdota.

**Demostración medida de la ley (esta misma ronda):** entre la apertura de esta tarjeta y esta addenda, el metal movió sin que esta Mesa lo hubiera leído: PreceptorOS#179 (ancla hexagonal) FUNDIDO y FIRMA SOBERANO servida para p0x#84 — cazados por relectura de la cerca antes de aterrizar este decreto (el canal pasó de 1.868 a 1.871 comentarios). Estado p0x#84 tras FIRMA: OPEN (fusión pendiente de su carril). Además, ya ejecutado en esta sesión: P0 verbatim (companion#14, merge f35c7aba) · enmienda censo 15→17 (study#101, merge e4dcb204) · sello live eb reconciliado (dw era pre-joystick).

**Cura de la Mesa en vivo (J-2):** un push interino pisó esta tarjeta con solo la addenda; cazado en el paso siguiente y restaurado íntegro en la cabeza definitiva. La historia del error queda declarada aquí, no enterrada.

Trailer: Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
