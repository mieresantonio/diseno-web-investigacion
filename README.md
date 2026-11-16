# Diseño web — investigación de Dirsi

Repositorio especial de investigación pura sobre diseño web. No es un
producto, no se despliega y no es un portafolio: es el cuaderno donde
Dirsi acumula lo que aprende construyendo apps reales, para que cada
app nueva empiece mejor que la anterior.

## Regla de crecimiento

Cada app que se construye deja aquí su lección. Al terminar una app:

1. Añadir una entrada en `log.md` (fecha, app, una línea de lo aprendido).
2. Si apareció un patrón reutilizable, documentarlo en `patrones.md`.
3. Si apareció un sistema de color o tipografía nuevo, registrarlo en
   `sistemas.md`.
4. Si algo falló o decepcionó, escribirlo en `lecciones.md` antes de
   olvidarlo. Las lecciones no se borran: se corrigen con fecha cuando
   dejan de ser ciertas.
5. Si el ojo visual produjo capturas, curar las que demuestran algo
   en `capturas/` con su entrada en el índice; y antes de dar la
   tanda por cerrada, correr `python3 verificar.py` (debe quedar en
   verde: coherencia del cuaderno y patrones contra el artefacto
   real).

## Contenido

- `principios.md` — Las reglas de diseño de Dirsi, cada una con su porqué
  y un ejemplo real de una app construida.
- `sistemas.md` — Los sistemas de color y tipografía usados de verdad
  (Block Ethos, barbería, Segundo Yo, biblioteca de prompts, interfaz
  del rag-demo) y cuándo usar cada uno.
- `sistema-diseno-vitrina.md` — El sistema de diseño cuantificado
  destilado del sistema precargado de Grok Build (tokens, disciplina
  de color, radios concéntricos, recetas de movimiento, anti-slop y
  checklist de cierre); su skill operativa es `diseno_vitrina`.
- `patrones.md` — Patrones de componentes reutilizables con esqueletos
  de código: hero, tarjetas, agenda, chat, constructor, ficha, glosario,
  formularios, favoritos, punto de estado, formulario deshabilitado,
  fuentes citadas.
- `lecciones.md` — Lo que falló o decepcionó y qué enseñó.
- `investigacion-kimi-k3.md` — Qué se sabe de cómo diseña Kimi K3 y qué
  toma Dirsi de eso (un método, no un mecanismo).
- `criterios-diseno-centeia.md` — Criterios aplicables destilados de
  la guía de diseño de CenteIA: diagnóstico de lo genérico, brief
  mínimo, trabajo por secciones, verificación y pasada final, con
  checklist de salida.
- `aplicacion-criterios-centeia.md` — Los criterios en la práctica:
  cómo se aplicaron en los rediseños de los Ciclos 2 y 4, con el
  mapeo intervención → criterio y el límite de verificación
  declarado (por código, bundles y checklist, sin captura).
- `log.md` — Bitácora viva de casos de estudio.
- `capturas/` — Galería de capturas verificadas del ojo visual,
  indexadas por fecha, caso y patrón que demuestran
  (`capturas/README.md`).
- `verificar.py` — Verificador ejecutable (sin dependencias):
  comprueba la coherencia interna del cuaderno y que los patrones
  10, 11 y 12 y los tokens del sistema rag-demo se cumplen en la
  plantilla real del rag-demo (`python3 verificar.py`).

## Origen

Síntesis original a partir de: las 4 apps construidas en octubre de 2026
(demo de barbería, biblioteca de prompts, Segundo Yo, API Segundo Yo),
el rediseño de Block Ethos, la revisión ModelBattle de 4 plataformas de
aprendizaje blockchain, el estudio de distilación de Kimi K3, los
materiales CenteIA «Tu segundo yo 24/7», la destilación del sistema
de diseño precargado de Grok Build y el método de clonación limpia
(observar → especificar → reconstruir → comparar paridad).

Nada de lo aquí escrito es texto copiado de esos materiales: son ideas
y estructuras redactadas con palabras propias.

Nota de nombre (16 nov 2026): el proyecto de aprendizaje blockchain
se llamó «Blockali» hasta el 16 de noviembre de 2026; desde entonces
es «Block Ethos» (eslogan «Web3 Space»). Las entradas anteriores a
esa fecha hablan del mismo proyecto con su nombre actual.
