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

## 2026-11-02 — Los criterios CenteIA en la práctica: Ciclos 2 y 4
Se documenta en `aplicacion-criterios-centeia.md` cómo se aplicaron
los criterios en la práctica: en el Ciclo 2, segundo-yo bajó los
síntomas de diseño genérico de 1 a 0 y las tres apps ganaron
tipografía propia; en el Ciclo 4, cada app web3 ganó un gesto de
cabecera propio (dao-vote no, por identidad suficiente), solo en
presentación. Verificación por código, bundles y checklist, sin
captura: la mirada visual de Antonio queda pendiente.

## 2026-11-07 — Destilación del sistema de diseño de Grok Build
Antonio exportó el workspace completo de la app que construyó con Grok
Build («Factory · Estudio · Currículum») y se inspeccionó archivo por
archivo. Dentro venía el sistema de diseño precargado de la plataforma
(skill de diseño con cinco referencias, referencia de QA en navegador y
el CSS real de la app). Se destiló a `sistema-diseno-vitrina.md` con
redacción propia: tokens cuantificados, disciplina de color, radios
concéntricos, sombra-como-borde, catálogo de recetas de movimiento,
lista anti-slop, QA visual con veredicto y checklist de cierre. Queda
registrado también lo que la destilación NO transfiere: el prior
generativo del modelo, sus herramientas de imagen integradas y su bucle
interno de vista previa. La skill propia `diseno_vitrina` lo convierte
en procedimiento operativo de Dirsi.

## 2026-11-07 (noche) — Revisión de los 47 repos y primer uso del sistema

A petición de Antonio se revisaron con el ojo visual las superficies con
cara pública de sus 47 repos de GitHub (9 capturas: Blockali, portafolio,
Biblioteca de Prompts, Segundo Yo, Barbería, Hash Lab, DAO Vote, NFT
Studio y el visor de mundo-vida-ia). Veredicto: las apps web3 y las de
CenteIA están presentables; el visor de mundo-vida-ia es plano pero
funcional; la superficie urgente era el PORTAFOLIO.

Hallazgo verificado en el archivo: el borrador del 21 oct 2026 cargaba
Tailwind desde un CDN externo — un único punto de fallo: sin ese CDN la
página se renderiza ilegible (texto negro sobre fondo casi negro) — y
traía enlaces de proyecto de relleno y un LinkedIn incorrecto.

Rediseño ejecutado el mismo día con la skill `diseno_vitrina`, primera
aplicación real del sistema destilado por la mañana: un solo archivo
HTML+CSS sin dependencias, tema claro editorial (papel, tinta, un acento
marino), tipografía serif de vitrina, sombra-como-borde, datos reales
(Blockali destacado con sus cifras verificadas) y LinkedIn correcto.
Verificación con el ojo en escritorio y móvil, incluido scroll real: la
composición no necesitó correcciones; se corrigieron dos cosas técnicas
(el revelado por scroll ahora es mejora progresiva — sin JS el contenido
se ve siempre — y un enlace que se partía en móvil). El juicio de Antonio
resuelve la entrada de calibración C-006 en mundo-dirsi.
