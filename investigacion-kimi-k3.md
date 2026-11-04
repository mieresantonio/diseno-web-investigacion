# Investigación: cómo diseña Kimi K3 y qué toma Dirsi

Resumen corto del estudio del 23 de octubre de 2026. El informe
completo (viabilidad técnica y legal de destilar K3) vive en
`research_notes/kimi-k3-distillation-viability-20261023-0638/`.

## Lo que se sabe

- Kimi K3 (Moonshot AI, julio 2026) es un MoE de 2,8 billones de
  parámetros (104.000 millones activos), contexto de 1 millón de
  tokens, con visión nativa (MoonViT-V2, 401 millones de parámetros).
- En 2026 lideraba el ranking de código frontend de Arena (1.679 Elo),
  por encima de sus rivales de frontera. Esa es la base empírica para
  tomarlo como referencia de diseño, no una preferencia.
- **No existe ningún mecanismo de diseño en los pesos.** Nada en la
  arquitectura dice «así se diseña». El talento de diseño es emergente
  y viene de cuatro cosas:
  1. **Visión nativa + bucle:** genera, renderiza, mira el resultado y
     corrige. El ojo (propio o del modelo) cierra el bucle.
  2. **Contexto de 1 millón de tokens + pensamiento siempre activo:**
     cabe el brief, el código, el render y la corrección en una sola
     pasada larga.
  3. **Escala MoE sobre un corpus enorme de código y web:** ha visto
     tantos layouts que sus valores por defecto ya son buenos.
  4. **La receta de entrenamiento, no publicada:** no se puede copiar
     lo que no se conoce.
- La vía viable para heredar algo de K3 no es extraer logits (el
  checkpoint pesa 1,56 TB y exige un clúster) sino SFT sobre sus
  salidas: ejemplos de diseño, no pesos. Y lo que el SFT transfiere
  bien es el *estilo de casa* (patrones de layout, convenciones,
  fiabilidad de formato), no el razonamiento de largo alcance.
- Cautela legal real: la licencia de los pesos no prohíbe entrenar con
  salidas, pero los términos de algunos intermediarios sí (Databricks
  lo prohíbe expresamente). Verificar el canal antes de generar.

## Qué toma Dirsi (y qué no)

Toma:
- **El bucle como método.** Generar → renderizar → mirar → corregir
  es el principio 5 de este repo. No hace falta un modelo gigante
  para aplicarlo: hace falta renderizar de verdad y mirar de verdad.
- **Evaluar por render, no por código.** Un diseño se juzga por cómo
  se ve y cómo se usa, no por lo limpio que parece su JSX.
- **El estilo se aprende con ejemplos.** Igual que un estudiante SFT
  absorbe el estilo de sus ejemplos, Dirsi mejora guardando patrones
  reales (este repo) en vez de reglas abstractas.
- **La casa importa.** K3 gana porque sus valores por defecto son
  buenos. Los sistemas de `sistemas.md` son el equivalente de Dirsi:
  valores por defecto buenos, listos para usar.

No toma:
- No copia el «mecanismo» de K3 porque no existe.
- No afirma ninguna relación con K3: Dirsi es otro modelo; la
  convergencia de estilo viene de corpus públicos compartidos, no de
  parentesco.
- No promete que un estudiante pequeño herede el talento completo:
  hereda estilo y formato, no razonamiento largo ni contexto de 1M.

## Actualización K3.1 Pro (4 nov 2026): la mejora no estaba en el esqueleto

Auditoría por ciclos del repo oficial `moonshotai/Kimi-K3.1-Pro`, con
el mismo método de la de K3 (índice + encabezados por rangos +
muestreo + código; ~142 MB leídos de 1,56 TB; 96/96 shards
reconciliados al byte, 0 errores). Informe completo en la auditoría
local de Dirsi (`auditoria-kimi-k3/k31/ANATOMIA-K31.md`).

- **Estructuralmente, K3.1 = K3 + 120 tensores.** Son los del
  «indexer» de su atención dispersa (Gated DSA): una cabecera ligera
  que elige los 2.048 tokens más relevantes y la atención principal
  solo mira esos, en las mismas 24 capas donde K3 hacía atención
  completa. Todo lo demás — expertos, embeddings, torre de visión,
  formatos — es byte a byte idéntico en tamaño a K3.
- **El muestreo cierra la historia:** los pesos compartidos tienen
  valores distintos de los de K3, con distribuciones casi iguales.
  La ganancia de capacidad de K3.1 no viene de arquitectura nueva:
  viene del post-entrenamiento sobre el mismo esqueleto.
- **Licencia de los pesos leída:** no restringe entrenar con salidas
  (puerta solo para negocio «modelo como servicio» >US$20M/año). Los
  términos de la API directa de Moonshot, en cambio, quedaron
  clasificados como zona de riesgo para destilar: el canal importa
  tanto como la licencia, como ya advertía la nota de Databricks.

Qué toma Dirsi de esto, para diseño y rediseño:

- **La confirmación del bucle, ahora con el caso del competidor.**
  Ni siquiera Moonshot mejoró rediseñando el esqueleto: mejoró
  iterando sobre lo que ya tenía, con retroalimentación medible.
  Para Dirsi el equivalente sigue siendo generar → renderizar →
  mirar → corregir, con criterios escritos y verificación por
  captura. La mejora vive en el bucle, no en un salto de motor.
- **Selección antes que exhaustividad (la lección del indexer).**
  El DSA no mira todo el contexto: elige lo relevante con un
  mecanismo barato y dedica el esfuerzo ahí. Traducción honesta a
  rediseños: primero diagnóstico por síntomas y corrección dirigida
  a lo que falla, en vez de rehacer la página entera «por si acaso».
- **Lo que NO cambia:** leer la anatomía de K3.1 no mejora los pesos
  de Dirsi ni su gusto. Lo que mejora el diseño en este sistema es
  lo de siempre: el ojo (capturas reales), los criterios de este
  repo y patrones guardados de trabajos verificados.
