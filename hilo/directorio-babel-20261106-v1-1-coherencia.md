# EL DIRECTORIO · v1.1 · enmienda de coherencia: los escritos antiguos ya hablaban · 2026-11-06

**Mandato del Soberano:** revisar los escritos más antiguos por coherencia con lo que hoy la Mesa habla como ground truth, y actualizar. Revisado con lectura directa: DISCURSO_FUNDACIONAL_P0X.md (mente/doctrina/, 2026-07-04), arranque.json «las reglas» (2026-09-07, commit f50f1f0), acta.js (padre de f91ddb5), las cadenas del bytecode del Ojo (medición del Soberano 2026-11-06) y el registro de 88 huérfanos del laboratorio (buzon#53 ·6683794007/·6683821579/·6683844195).

## Veredicto: HOY ES COHERENTE CON LO MÁS ANTIGUO

Lo que la Mesa habla hoy no es drift: es la continuación de lo ya escrito. Cada pieza con su cita medida:

1. **IronClaw**: «el silicio estudia, propone y optimiza; el carbono supervisa y firma toda salida» (Discurso §1, 2026-07-04) = la ley de FIRMA de hoy.
2. **«sin dato»** (Sínodo, 2026-07-04) = NO_DATA de hoy; y arranque.json ya exigía la causa: «la respuesta trae NO_DATA con su nombre en vez de callarse».
3. **«el guardián tiene un suelo duro que ninguna firma exime»** (arranque.json) = la cerca hitl de hoy.
4. **«git push SOLO con la firma explícita del Soberano» · «ninguna unidad systemd sin firma explícita»** (arranque.json, 2026-09-07) = FIRMO/FIRMA por cabeza exacta y FIRMA por unidad de hoy. La restauración del Ojo de HOY sigue exactamente esa regla antigua (propose-only, unidad disabled hasta FIRMA).
5. **«un acta que no verifica no vale como acta»** (acta.js, con cadena_sana/CADENA ROTA y badge firma_requerida) = los recibos con sha256 y el HITL de hoy.
6. **La Fragua · La Torre · El Vigía** (Discurso §4, 2026-07-04: RK3588, Jetson Orin, RPi) = tres filas de EL DIRECTORIO v1. El decreto BABEL no inventó nombres de hardware: VOLVIÓ a los del discurso fundacional.
7. **«El sistema se cita a sí mismo»** (Discurso §2) = la disciplina de fuentes de hoy.
8. **«SE PARTE, NO SE RECORTA» + tope 16.384 B por fichero** (arranque.json, corregido el 2026-09-07 desde el tope viejo de 10.240) = canon vivo de la web hoy: test_web lo exige.
9. **El flujo de forja del bytecode del Ojo**: «cinco turnos sobre el feedback FIRMADO que llega de la web: extrae, analiza, pasa el Guardian, forja el dataset y lo juzga con el ensamble de dos capas. Deja un dataset.jsonl candidato con su sha256 y su nota. Y el carril del JUEGO: las partidas que la Aduana verificó pasan a dataset» (strings de ojo.pyc, medido 2026-11-06) = Aduana + forja + guardianes + sellos sha256 de HOY.
10. **El Sínodo de seis voces con contrato de datos** (El Monje · El Vocero · El Berserker · El Escriba · El Alquimista · El Enlace, Discurso §3) = los proto-preceptores de hoy: proponen, jamás deciden.

**El único cambio medido** (evolución firmada, no incoherencia): «CERO nombres propios» en los README públicos (2026-09-07) → decreto BABEL (hardware real, 2026-11-06). Cambio decretado por el carbono; queda registrado como evolución.

## Joyas nuevas (primera mención medida → qué es hoy)

| nombre-proto | fuente | qué es hoy |
|---|---|---|
| IronClaw | Discurso §1 · 2026-07-04 | la ley de firma: silicio propone, carbono firma |
| El Sínodo (6 voces) | Discurso §3 · 2026-07-04 | la Mesa y sus preceptores (contratos de datos) |
| El Faro (Ed25519, cadena) | Discurso §2 · 2026-07-04 | faro de producción (151/151) y sellos encadenados |
| cargar partida (save game) | arranque.json + commit 0893d57 · 2026-09-02 | el estado que sobrevive a la sesión fría |
| El Acta (cadena, firma_requerida) | acta.js · f91ddb5^ | buzon (canal Mesa↔Rack) y HITL |
| La Necrópolis | arranque.json · 2026-09-07 | lo retirado con su porqué (hoy: plegados con recibo) |
| El Ojo-Vivo, refugio del Soberano | vivo.html · f91ddb5^ | restaurado HOY: SIRVE · 17 piezas (loopback 200) |
| Los cuatro pilares (Caza-Nido, 3 Capas, Verdad del Silicio, Bug LoRA) | arranque.json | doctrina fundacional viva |
| 88 huérfanos del laboratorio | pycache 13-sep→15-oct · ·6683821579 | registro fósil pro-máquina (aduana_juego, forja_canario, juez, enjambre…) |

## Topología medida del Ojo (ground truth de la restauración)

**17 piezas que sirve:** acta.js · arranque.js · automata.js · bunker.css · bunker.html · bunker.js · digesto.js · glosario.js · grafo.js · letras.js · ojo.css · ojo.html · ojo.js · partida.js · vivo.css · vivo.html · vivo.js.
**8 fuentes que lee:** estado.json · fases.json · glosario.json · identidad_publica.json · mensajes.jsonl · arranque.json · recursos.json · grafo.json.
Recibo del Soberano: SHA-RECIBO con 16 sha256 verificados idénticos entre /tmp y el directorio vivo. Pendiente de medir: el cableado de las telemetrías que el bytecode nombra (censo_remoto_latest, espejo_latest, cerebro_local.jsonl — existen en mente/telemetria, con altura_bloque 221.879.809 y ciclos 747).

## Filas pendientes de EL DIRECTORIO v1

- **«los HP x86»** (Discurso §4: toolchain de entrenamiento) — NO_DATA hoy: ¿es fedora? A medir antes de fila.
- **CineK Studio**: unidad viva en 9000 «hasta la migración del 4-Nov» — migración PENDIENTE, pregunta abierta al Soberano.

SCRUB: sin IPs, credenciales ni rutas privadas; solo lo público del censo y las citas doctrinales.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
