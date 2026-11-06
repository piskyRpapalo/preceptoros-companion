# EL DIRECTORIO · v1.2 · el registro pro-máquina: 118 huérfanos y el contrato de la instantánea · 2026-11-06

Continuación de la enmienda de coherencia (v1.1, companion#18). Todo medido por el Soberano en el rack el 2026-11-06; servido por la Mesa en Buzón ·6683921773.

## El contrato medido de la instantánea

rack_instantanea.py, restaurado de git 3f81a14 (21.330 B) tras la cura; service VERDE (status=0/SUCCESS):

- La APP promete funcionar SIN RED: lee UN fichero, ~/.preceptoros/laboratorio/rack.json, esquema hexelion.rack-instantanea/1; si tiene más de 15 min lo pinta NO_DATA.
- El ESCRITOR solo toca loopback de lectura: el Nexo (8765, /api/nodos y /api/soberania) y Ollama (11434, /api/ps), más el Registro Único, que VERIFICA cada firma y la cadena al leer (enmienda 2026-10-04: sección registro). El escritor no se fía ni de eso: vuelve a descartar lo caducado o sin zona antes de copiar.
- Las CUATRO REGLAS, cada una con su prueba Y su sabotaje. La primera: Saneado · nada de IPs, nombres de la tailnet ni /home/<usuario>; cada texto se mira al entrar y el fichero entero se mira otra vez antes de escribir.

Continuidad con v1.1: el Saneado es el SCRUB de hoy; la pareja prueba+sabotaje es la misma disciplina que cazó el sabotaje pintado de verde (lección 2026-10-30). La disciplina no es nueva: es la misma desde el principio.

## El registro pro-máquina: 118 huérfanos

Fuente muerta (.py borrado), bytecode vivo (.pyc en __pycache__). Censo medido por cementerio:

- laboratorio (88): aduana_juego · aduana_nodos · apuntador_hwmon · audicion · auditor · banco_adversarial · buscar · calibrar_simulador · choice_model_duel · clasifica_feedback · compara_superviviente · compass · dataset_d39 · decisor_ref · destilar · destilar_reglas · duelo_mini · enjambre · enrutador · estudio_torre · etiquetar · etiquetar_seeds · evolutionary_lab_runner · fabrica_eu · forja_canario · forja_dificiles · forja_superviviente · forjar · gate_failure_cycle · gc_loras · hexelion_busca · hexelion_mockup · ingesta · jav · jev · juez · juez_de_contexto · mapa_hexelion · mcp_ai_act_article14_state · mcp_ai_act_article50_a2a_lexical_fluency · mcp_eaa_article12_projection · mcp_eu_generico · mcp_gdpr_article25_access · mcp_nis2_article21_loader · medir_modelo · mide_atajo · mide_d39 · mide_libro · mide_pisos · objective_anchor_hints · objetivos_registry_build · personajes_torre · problemas_juego · promocion · rack_instantanea · reescrituras · reflexion · ruteo_capas · sabotaje_juez_web · servidor · shared_lab_telemetry · simulador · sonda_web · sueno · sintesis · territory_inbox · timeline_build · traduce_familia · tramo · tramo2 · tramo2_eu · tramo14_eu · tramo17_agente_backup · tramo19_eu · turnos · vectores · y sus test_*.
- bin (24): aceptados_fragua · agora_portada · bandeja_fragua · censo_juego · censo_remoto · coherencia-publica · doctor · inventario_js_muerto · inyeccion_dataset · libro_de_pruebas · mcp_preceptor · mcp_rack · mock_api_granero · optimizaciones · panel_estudio · paquete_estudio · rag_estudio · rama_publica · release_publica · responder_quipu · sw-huella · test_lint_datetime · test_mock_api_granero · vista_soberano.
- scripts (1): revisor_ia · bench-fluency (3): resumen · runner · test_bench · m10-autopsia (2): autopsia · medir.

Fechas del pycache del laboratorio: última foto viva el 15-oct. El fichero restaurado (rack_instantanea.py) está aún SIN commit en el p0x del rack: propose-only + FIRMA por cabeza, pendiente.

## Joyas nuevas del censo (nombre-proto -> qué es hoy)

| nombre-proto | cementerio | hoy |
|---|---|---|
| bandeja_fragua · aceptados_fragua | bin | la bandeja de la forja: el feedback aceptado entra al dataset |
| censo_remoto | bin | censo_remoto_latest.json, hoy en mente/telemetria |
| doctor | bin | el diagnostico del rack (hoy: la cerca de git que cura) |
| vista_soberano | bin | el panel del Soberano |
| coherencia-publica | bin | la ley del drift (hoy: 11-repos.md y esta serie) |
| libro_de_pruebas | bin | el libro de casos (hoy: bateria del gate, 1147/1147) |
| responder_quipu | bin | los quipus (hoy: mensajes.jsonl y el Buzon) |
| sw-huella | bin | la huella de software (hoy: el sello preceptoros-AAAA-MM-DD) |
| sueno · reflexion | laboratorio | los bucles del Director (hoy: afinador/curador del director.timer) |
| forja_canario · forja_dificiles · forja_superviviente · forjar | laboratorio | la familia de la forja de datos |
| juez · juez_de_contexto | laboratorio | el ensamble de dos capas (hoy: juez del dataset y del contexto) |
| mcp_gdpr · mcp_nis2 · mcp_ai_act · mcp_eaa | laboratorio | los MCP regulatorios (hoy: la familia mcp_* del p0x) |
| enrutador · ruteo_capas | laboratorio | el ruteo de modelos (hoy: decisor de niveles) |

## Deriva de citas medida (honesto, con causa)

- mesa/matematica-nativa-tanda2-20261105.md y espacios/lab-pupilo/progreso/2026-10-03_ficha_rack-instantanea_qwen2.5-14b.md NO existen en el p0x del rack en sus rutas citadas (PS de codex ·6683239121).
- La ficha VIVE en historial git (git log la lista). Causa: cita de otro entorno o purgado del arbol. Cura: restauracion desde git, jamas reescritura.

## Veredicto

La cura del rack repite el patron del Ojo: lo que sirve esta en git; lo perdido se restaura por hash, no se reinventa. Y el contrato de la instantanea es la foto mas clara de la serie: la app no habla con nadie, el escritor no se fia de nadie, y cada regla trae su prueba y su sabotaje. ESO es el ecosistema.
