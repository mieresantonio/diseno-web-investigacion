# Galería de capturas verificadas

Selección curada de las capturas que el ojo visual produjo al
verificar las apps de este cuaderno. Cada imagen se indexa con su
fecha, su caso y el patrón o la entrada de `log.md` que demuestra:
la galería es la evidencia visible de las afirmaciones de
verificación del resto del repo.

Regla de la galería: una captura entra aquí solo si alguien la vio
y comprobó que lo que muestra coincide con lo que la entrada que
la cita afirma. Si una captura no muestra lo que se esperaba, el
índice lo dice en vez de callarlo (ver la nota del par
antes/después, abajo).

## Interfaz web del rag-demo — 16 nov 2026

Caso: interfaz web mínima del rag-demo (`log.md`, entradas del
16 nov 2026). Capturas con el ojo visual en escritorio 1280×800 y
móvil 390×844.

### Antes de preguntar (estado inicial)

| Archivo | Vista | Qué muestra |
|---|---|---|
| `rag-ui-desktop-antes.png` | Escritorio 1280×800, solo viewport | Estado inicial: punto de estado verde junto a «27 documentos · 527 fragmentos · paragraph-multilingual-MiniLM-L12-v2» en una sola línea; campo de pregunta vacío con el botón «Preguntar» apagado. |
| `rag-ui-mobile-antes.png` | Móvil 390×844, solo viewport | Lo mismo en móvil: el texto de estado se parte en dos líneas y el nombre del modelo pasa a la segunda; el punto sigue en la primera línea, junto a «27 documentos · 527 fragmentos ·». |

Entrada de `log.md`: «2026-11-16 — Interfaz web mínima del
rag-demo».

### Después de preguntar (página completa con respuesta y fuentes)

| Archivo | Vista | Qué muestra |
|---|---|---|
| `rag-ui-desktop-despues.png` | Escritorio 1280×2886, página completa | La respuesta a «¿Qué es REA y para qué sirve?»: texto extractivo con citas [1]–[4], «Confianza alta», «Similitud máxima 0.526» y la lista de Fuentes con número, archivo, sección y similitud a la derecha (0.526, 0.364, 0.431, 0.337). |
| `rag-ui-mobile-despues.png` | Móvil 390×4776, página completa | Lo mismo en móvil: la respuesta, «Confianza alta», «Similitud máxima 0.526» y la lista de Fuentes con la similitud alineada a la derecha. |

Entradas de `log.md`: «2026-11-16 — Interfaz web mínima del
rag-demo» y «2026-11-16 — Estado sin índice de la interfaz del
rag-demo» (esta última cita el mismo estado — REA, confianza
alta 0,526, 4 fuentes — como comprobación de que el camino con
índice quedó intacto tras restaurar). Patrón demostrado: nº 12
«Lista de fuentes con evidencia» (`patrones.md`).

### Estado sin índice (formulario deshabilitado entero)

| Archivo | Vista | Qué muestra |
|---|---|---|
| `rag-ui-sin-indice-desktop.png` | Escritorio 1280×800, solo viewport | Punto rojo «Sin índice cargado.», aviso amarillo «Todavía no se ha ejecutado la ingesta: ejecuta «python ingest.py» y recarga la página para poder preguntar.», campo de pregunta con fondo gris deshabilitado y botón «Preguntar» apagado. |
| `rag-ui-sin-indice-mobile.png` | Móvil 390×844, solo viewport | Lo mismo en móvil: punto rojo, aviso, campo y botón deshabilitados. |

Entrada de `log.md`: «2026-11-16 — Estado sin índice de la
interfaz del rag-demo». Patrón demostrado: nº 11 «Formulario
deshabilitado entero cuando el servicio no está» (`patrones.md`):
el campo queda deshabilitado y con aspecto de tal, no solo el
botón.

## Nota honesta sobre el par antes/después y el patrón nº 10

El patrón nº 10 («Punto de estado + texto largo en flex») nació
de un defecto real de esta interfaz: en móvil, el punto de estado
saltaba a su propia línea. Pero estas capturas «antes» **no
muestran ese defecto**: comparando la tarjeta de estado del móvil
entre `rag-ui-mobile-antes.png` y `rag-ui-mobile-despues.png`,
la región es idéntica píxel a píxel (el punto comparte la
primera línea con el texto en ambas). El par antes/después
documenta el estado inicial frente a la página respondida — y
ahí sí demuestra el patrón nº 12 —, no el defecto del punto.
El patrón nº 10 sigue apoyado en la entrada de `log.md` y en el
código del rag-demo, no en una imagen de esta galería. Si algún
día se recaptura el defecto (p. ej. con la plantilla anterior al
arreglo), esa imagen debe añadirse aquí con su fecha.
