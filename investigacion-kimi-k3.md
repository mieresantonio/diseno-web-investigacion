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
