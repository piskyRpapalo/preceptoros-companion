# Poda y unificación de GitHub · PROPUESTA (propose-only) · 2026-11-06

**Mandato:** decreto BABEL (buzon#60): menos repos + README coherente + superficie pública limpia. Palabra del Soberano (2026-11-06): mantener los repos acordados; traer poda y unificación como propuesta; la Mesa asume ALL-IN de GitHub. **Ejecución: FIRMA por cabeza exacta en cada fase; nada se borra sin recibo; archivado antes que borrado.**

Censo medido hoy vía API: 17 repositorios, 16 activos + 1 plegado (preceptoros-coder, registro en web odd/tasks + PR#659). Cabezas al medir: web 81cfb783 · companion 1e2af7fe · study e4dcb204 · p0x 49c9ef50 · babel 547dbcc8 · aduana d04f9543.

## 1 · Lo que se mantiene (el acuerdo · 12 activos del ecosistema)

**Públicos (7):** preceptoros-web (WEB: gateway público y juego) · PreceptorOS (APP: compañero local-first) · lab (LAB: record medido) · study (STUDY: doctrina pública; casa del censo canónico 11-repos.md) · babel (casa única del vocabulario) · preceptoros-companion (COMPANIONS + la Mesa: EL DIRECTORIO vive aquí, #16) · piskyRpapalo (portada del owner)

**Privados (5):** p0x (cerebro del rack) · aduana (verificador de carta pública; su worker sirve la API pública) · buzon (canal Mesa↔Rack) · firmas (libro único de firmas) · hexelion-nexo (sensor de flota y despertar)

## 2 · Poda propuesta (propose-only; cada plegado FIRMA aparte)

- **P1 · roadmap → preceptoros-atlas.** La sala del plan es docs-only privado; pliega en el Atlas (su AGENTS.md es LEY firmada 2026-11-04) como directorio append-only. Antes: bundle de respaldo + recibo. Después: archivado reversible de roadmap. −1 repo.
- **P2 · preceptoros-terminal → p0x.** La Sala es runtime del rack (loopback, gate propio, unidad systemd); pliega como directorio de p0x con gate intacto. Antes: bundle + recibo. Archivado reversible. −1 repo. Alternativa declarada: mantenerla si el Soberano prefiere su repo propio por su despliegue.
- **P3 · CineK → EXTERNO.** Medido hoy por lectura directa: su README se declara independiente del ecosistema (regalo personal). Propuesta: cuenta aparte como externo (enmienda ya servida en 11-repos.md), sin tocar el repo.
- **preceptoros-coder:** ya plegado y archivado (2026-11-06). Nada que hacer.

Resultado si P1+P2 se firman: **14 activos del ecosistema + 1 externo + 1 plegado.**

## 3 · Unificación propuesta

- **U1 · README coherente:** plantilla mínima por repo activo (qué es · qué habilita · dónde vive su canon · cómo se mide · superficie pública = solo benchmark telemétrico). Medido hoy: aduana sin README ni descripción.
- **U2 · aduana (infra viva, FIRMA aparte):** default branch apunta a rama de trabajo codex (codex/node-gateway-worker-20261016), no a main → curar a main; poda de 23 ramas medidas (borrar solo las verificadas fusionadas, con recibo); README propio.
- **U3 · Portada del owner:** dice «four core repositories» y lista seis filas → curar la cuenta; su tabla y 11-repos.md deben coincidir (ley: drift RED).
- **U4 · Censo canónico:** enmienda servida en 11-repos.md (rama mesa/censo-restaurado-20261106): CineK medido externo + cura del pisado de hoy (el commit c1d2b819 reemplazó el fichero: perdió las enmiendas 10-18/10-30/11-02/11-03 y arrancaba con «undefined»; restaurado verbatim desde git 4c8f289e).
- **U5 · Nombres:** cada descripción usa los nombres oficiales de babel + EL DIRECTORIO (companion#16); nada se acuña fuera de babel.

## 4 · Ejecución (por fases; una pieza cada una)

- **F0 (docs-only, THE MARCH FIRMO):** esta propuesta + enmienda del censo.
- **F1 (FIRMA aparte):** P1 roadmap → atlas.
- **F2 (FIRMA aparte):** P2 terminal → p0x (o decreto de mantenimiento).
- **F3 (FIRMA aparte):** U2 aduana (default branch + ramas + README).
- **F4 (docs-only):** U3 portada del owner.

SCRUB verificado: sin IPs, credenciales ni rutas privadas; solo lo público del censo.

Agent: preceptor-orquestador-github · Model: GLM (Vibe) · Run: NO_DATA
