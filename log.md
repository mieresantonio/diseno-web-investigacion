# Bitácora viva

Entradas cortas: fecha, app, una línea de lo aprendido. La bitácora no
se reescribe: se añade.

## 2026-10-26 — Creación del repositorio
Se crea este repo de investigación para acumular lo aprendido
construyendo apps reales, con 4 casos de estudio iniciales.

## 2026-10-26 — Caso: demo local de barbería
Landing + agenda + chat de WhatsApp simulado; lo que la define es su
flujo (reservar → cancelar → hueco libre), no su landing. Sistema
oscuro + dorado.

## 2026-10-26 — Caso: biblioteca de prompts
Catálogo con filtros + constructor de 6 campos + copiar + favoritos en
localStorage; el panel lateral fijo y el bloque oscuro de «salida» son
sus dos decisiones de diseño más imitables. Sistema índigo claro.

## 2026-10-26 — Caso: Diseña tu Segundo Yo
Ficha copiable + 25 tareas en 5 grupos + checklist de 5 pasos +
glosario con buscador; su lección es la escala de espaciado con nombre
y el estado vacío diseñado. Sistema violeta + ámbar claro.

## 2026-10-26 — Caso: API Segundo Yo
Backend Flask + SQLite con los mismos 3 dominios que los frontends;
su lección es de proceso, no de pantalla: verificar termina matando el
servidor y comprobando el puerto libre.

## 2026-11-01 — Criterios de diseño desde la guía CenteIA
Se vuelca en `criterios-diseno-centeia.md` el criterio destilado de
la guía de diseño evaluada en octubre (no su instalación): diagnóstico
de lo genérico, brief de 6 puntos, trabajo por secciones con
comparación, verificación en móvil y con capturas, y pasada final
crítica → auditoría → pulido con checklist de salida.

## 2026-11-02 — Los criterios, aplicados: pasada de rediseño en 3 apps
Se aplican los criterios de `criterios-diseno-centeia.md` a
biblioteca-prompts, segundo-yo y la demo de barbería, solo en el
frontend y con cambios puntuales donde el diagnóstico lo pedía:
biblioteca pierde el degradado morado (tinta sólida + textura de
puntos, Fraunces, acentos por bloque); segundo-yo pierde el título en
degradado (tinta sólida + barra ámbar, Sora); barbería solo gana su
fuente de marca (Oswald) — el resto ya cumplía. Cada app guarda su
`redesign-log.md`. Verificación: build y dist servido en local con los
cambios confirmados en el CSS compilado; sin capturas visuales (la VM
no tiene navegador), la mirada final en pantalla queda de Antonio.

## 2026-11-02 — Lección de despliegue (Blockali en producción)
Dos builds seguidos salieron mal por empaquetar sin mirar dentro.
Regla que queda, ya escrita en el runbook de despliegue: compilar
SIEMPRE con `VITE_BACKEND_URL=https://BC123.pythonanywhere.com` y
verificar el bundle POR SU CONTENIDO (cadenas decisivas dentro,
conteo de la URL del backend) contra el último bundle conocido-bueno
antes de subirlo. Nunca por nombre ni por fecha.
