# HITL · LISTA COMPRIMIDA v3 · PROTOCOLO DE TRASPASO + LÍNEA FINAL

Madre: lista-v3-20261104 (fisión declarada por tier). Transcripción fiel de la Mesa, 2026-11-04.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROTOCOLO DE TRASPASO — cómo the Arm lleva estas filas a hilo/tasks/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BUSCAR (cláusula 10): antes de crear cada tarea, corre los cinco lugares (main · PRs abiertas · ramas · mesa · retirados/). Si la tarea ya existe como PR o rama, la CITA y la enriquece, no la re-crea. Lo no verificado = NO_DATA con causa.
RECLAMO (cláusula 10): fila {id, campo: claim, dueño: the Arm, causa, origen} ANTES de la primera línea. Un dueño por pieza. El segundo cede con causa.
VARA: corre la vara de la fila contra HEAD. Si confirma: MEASURED con recibo (comando+fecha+máquina). Si no: NO_DATA con causa y se cierra la fila. Las varas de T-14..T-19, T-24, T-25 corren EN LA CASA (the Codex lane), no desde fuera.
PIEZA: docs-only PR bajo THE MARCH si es texto; pieza de valor espera FIRMO por cabeza exacta. Una pieza por PR. OJO T-18: si altera el denominador de pruebas, es Code/Harness PR, no docs-only.
SCRUB: ningún nombre de placa, ninguna ruta privada, ningún ps raw. Machine star o pseudónimo del censo. Solo clave, conteo y tarea cruzan; jamás valor.
FAMILIA CRUZADA: the Codex lane confirma T-01..T-13 contra el metal (tiene el grep de la casa que the Arm no ve) antes de que the Arm las traspase. Si confirma una NO_DATA como MEASURED, la fila se actualiza con su recibo. Si la desmiente, se cierra con causa.
CENSO: cada cierre superseded o reclamo-chocado-resuelto se registra en hilo/tasks/duplication-census.md. Vara: duplicaciones/semana → 0.
FISSIÓN DECLARADA: si este merge excede 16.384 B al traspasar, se fisiona por tier (TIER 0..TIER 5 como piezas separadas, cada una ≤ 16.384 B, citando la pieza madre). Precedente vivo: «Budget of every doc: < 16,384 B (house ceiling) or declared fission».

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LÍNEA FINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
El Soberano dijo «enfocado a lo que tenemos hoy, olvida instalar cosas nuevas». Este merge no trae OpenRig, ni Hermes, ni router: trae lo que HEAD sirve hoy y lo que la casa guarda. La vara vectorial manda: T-01 (el ancla null) bloquea todo lo demás; sin ceremonia no hay flota, sin flota no hay mapa. T-05 (el tablero stale) y T-06 (la cola #641) son la puerta que ya funcionó y el triaje que debe verla antes de tocar OpenWorld. T-20..T-25 son higiene de web corregida contra HEAD en vivo — tres filas se recortaron o encogieron porque el metal las movió esta mañana, y una subió a MEASURED total porque el bug quedó delimitado. Las CIERRAN se citan, no se re-crean; C-07 celebra que el carril de babel está limpio. Las LIQUIDADAS ya no son hueco. Y la voz del analista sigue «otra» hasta tu FIRMO.
Silicio propone la fila, la vara, el cruce y el scrub. Carbono firma la ceremonia, las dirimencias (T-04, T-13, T-26, T-27), la voz, y cada merge. Lo que ya existe, se cita; lo que está reclamado, se cede; lo que es ambiguo, se pregunta; lo que es null servido, se ejecuta; lo que el metal ya movió, se recorta y se dice.

Agent: otra (voz en dirimencia §F) · Model: NO_DATA (cause: provider not evidenced on this surface) · Run: NO_DATA (cause: run identity absent)
