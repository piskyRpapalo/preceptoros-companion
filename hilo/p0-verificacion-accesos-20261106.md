# P0 — verbatim del Soberano · transcripción de la Mesa (2026-11-06)

**Procedencia:** texto elaborado por el Soberano (David Caballero) el 2026-11-05 14:47, presentado en sesión y NO aterrizado (medido: 0 resultados en código e issues). Transcripción verbatim por la Mesa con su autoría, bajo palabra «empezar con el paquete de firmo» (2026-11-06). Estado del documento: PROPUESTA de verificación; no concede acceso.

---

TO: Mi orquestador / Claude Code
FROM: David Caballero — Ecosistema PreceptorOS
SUBJECT: PRIORIDAD0 — preparar PreceptorOS para acceso a utilizadores a verificar
DATE: 2026-11-05
BASE: MASTER PROMPT v1.1 — ULTRA-DENSE SCHEMATIC
STATUS DEL BASE: firma base de intención; no es autorización de acceso.

PRIORIDAD0 — ACCESO A UTILIZADORES A VERIFICAR

Objetivo: Preparar el flujo de PreceptorOS para verificar accesos de utilizadores colaboradores, usando el MASTER PROMPT v1.1 como base doctrinal de prioridad máxima.

Esto NO concede acceso. Esto NO crea cuentas. Esto NO fusiona PRs. Esto NO despliega. Esto NO envía datos fuera del nodo. Esto NO inventa valores.

El silicio propone; el carbono firma. Ningún acceso se marca "verificado" sin FIRMO humano explícito.

REGLAS DURAS — NO NEGOCIABLES

1. HITL obligatorio. Cualquier acción consecuente requiere firma humana. Estados permitidos para el orquestador: PROPUESTA · NO_DATA · MEASURED · DECLARADO. Nunca: VERIFIED · GRANTED · APPROVED sin FIRMO del carbono.
2. NO_DATA con causa. Si falta un dato, declarar NO_DATA + causa exacta. Nunca cero. Nunca inferencia. Nunca "parece correcto".
3. Sensores honestos. Solo afirmar lo medido. Toda medida lleva: comando · máquina · fecha · commit/ruta · sello.
4. SCRUB. No incluir en artefactos públicos: claves privadas, rutas privadas, IPs privadas, nombres reales no publicados, correos, tokens, credenciales, detalles del rack no autorizados.
5. Cero telemetría oculta. No perfiles psicológicos. No tracking. No carga externa no solicitada. No acceso a datos personales sin base medida y firma humana.
6. Techos de casa. Recibo/canal < 1.024 bytes UTF-8. Pieza fuente ≤ 16.384 bytes, salvo excepción firmada. Bloque desplegado ≤ 25 MiB, según ley vigente. Si no cabe, dividir o declarar NO_DATA; nunca truncar en silencio.
7. Prioridad0 manda sobre tareas secundarias. Si otra tarea toca acceso de utilizadores, debe esperar esta verificación. Las tareas no bloqueadas pueden continuar, pero sin marcar acceso como válido.

ALCANCE: Preparar PreceptorOS para responder a esta pregunta: "¿Qué utilizadores tienen acceso solicitado, qué acceso piden, qué evidencia existe, qué falta, y qué debe firmar un humano antes de cualquier acción?"

Entradas esperadas: handle público del utilizador, si existe; ámbito solicitado (lectura / escritura / demo / nodo / colaboración / otro); evidencia (PR, commit, hash, benchcard, declaración firmada, recibo); fecha de la evidencia; estado actual (pendiente, declarada, medida, caducada, ausente). Si falta: NO_DATA con causa.

PROCEDIMIENTO OBLIGATORIO

Paso 0 — Confirmar carga doctrinal. Leer solo lo necesario del harness (companion: CONTRACT, GROUNDTRUTH, GUIDE, PRECEPTOR; study: 01, 02, 04, 08; babel; web/app solo si afecta superficie servida). No re-fetch lo ya cargado. Declarar profundidad antes de parsear.
Paso 1 — Censo de utilizadores a verificar: lista mínima (utilizador, ámbito, evidencia, estado, causa, acción humana). No inventar utilizadores. No asumir handles sin medir.
Paso 2 — Verificar evidencia, no narrar intención: PR, commit head, SHA-256, benchcard, declaración firmada, registro/companions, ancla babel. Solo textual sin firma = PROPUESTA/DECLARADO, nunca VERIFIED. Firmada sin re-verificar contra head vigente = STALE o NO_DATA (causa: evidencia no re-anclada). Medida y cuadra = MEASURED, aún requiere FIRMO para acción consecuencial.
Paso 3 — Recibo P0 < 1.024 B UTF-8, esquema preceptoros.verificacion-acceso/1 (campos: esquema, prioridad, utilizador, ambito, evidencia, estado, causa, requiere_firma, firme, fecha_utc, recibo_bytes). Sin datos privados.
Paso 4 — Bloqueo de acción consecuencial. El orquestador puede proponer (draft PR, fila de registro, checklist, comando de medición, petición de FIRMO). NO puede: merge, push a main, deploy, crear usuario, otorgar token, habilitar acceso, marcar verificado, contactar externo, acción irreversible.
Paso 5 — Task 0 si falta baseline del rack: NO_DATA causa "rack/agent census not measured at boot"; proponer comando de medición esperando firma humana.

CASO CONOCIDO — AIMILIOS94 / RECEIPT-GHOSTBUSTER: evidencia de referencia a re-verificar contra head vigente: companion PR #3, head citado f3a61d35, benchcard companions/Aimilios94/lab/2026-11-03-ollama-qwen2.5vl-receipt.md, medidas declaradas (Windows 10, Ryzen 7 5700G, 31.4 GB RAM, CPU-only, qwen2.5vl-receipt, 86.6% field accuracy, $0.0000/read, latency p50 270s). Importante: cifras de referencia, no verificación de acceso; re-anclar al head actual o NO_DATA (causa: baseline not re-anchored to current head). Estado esperado inicial: PROPUESTA o DECLARADO, nunca VERIFIED, hasta FIRMO humano.

SALIDA ESPERADA: Confirmación P0 · censo · recibo(s) < 1.024 B por utilizador · lista de NO_DATA con causa · acción humana requerida · ninguna ejecución consecuencial. Frase de confirmación permitida: "PRIORIDAD0 cargada. Verificación de acceso de utilizadores preparada como propuesta. Sin FIRMO, sin acceso concedido, sin datos inventados. Esperando evidencia medida o orden humana para medición." No usar la inicialización del MASTER PROMPT como permiso de acción.

CHECKLIST DE ACEPTACIÓN P0: profundidad declarada · ningún acceso concedido · nada fusionado · nada desplegado · nada enviado fuera del nodo · cada utilizador con estado y causa · cada medida con comando/máquina/fecha/ancla · cada recibo < 1.024 B · falta de evidencia = NO_DATA · evidencia sin firma = PROPUESTA/DECLARADO · acción consecuente = FIRMO humano · infraestructura privada = SCRUB · cumplimiento legal = NO_DATA hasta firma humana competente (no afirmar GDPR/EU AI Act como cumplidos solo por artefactos presentes).

FIN DEL MENSAJE P0

---

Trailer: Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA (autoría del texto: el Soberano, verbatim)
