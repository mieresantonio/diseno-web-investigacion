# Los criterios CenteIA en la práctica: Ciclos 2 y 4

Nota de aplicación, 2 de noviembre de 2026. Los criterios están en
`criterios-diseno-centeia.md`; esta nota no añade criterio nuevo:
registra cómo se usaron de verdad en dos rediseños, qué punto
concreto de ese archivo motivó cada intervención y hasta dónde
llegó la verificación. Si una decisión no está en el archivo de criterios, se
dice que es decisión de Dirsi, no de CenteIA.

## Ciclo 2: segundo-yo a fondo y pasadas tipográficas en 3 apps

### Segundo-yo: rediseño contra el diagnóstico hasta 0 síntomas

Segundo-yo se rediseñó recorriendo la página con el diagnóstico de
la sección 1 de `criterios-diseno-centeia.md` («Diagnóstico: señales
de diseño genérico») y corrigiendo lo anotado. El conteo de síntomas
presentes, medido con ese diagnóstico y con la checklist de salida
del mismo archivo, bajó de 1 a 0.

Mapeo intervención → criterio:

| Intervención | Punto del archivo que la motivó |
|---|---|
| Recorrer la app buscando síntomas antes de corregir | §7 «Pasada final en tres tiempos», paso 1 (Crítica): recorrer la página con el diagnóstico de la sección 1 y anotar cada síntoma presente, sin corregir todavía |
| Usar el conteo de síntomas como medida de cierre | §1: si una build acumula tres o más síntomas, no está lista; y checklist de salida: «Diagnóstico de genérico: menos de 3 síntomas». Llegar a 0 es cumplir esa puerta con margen, no una exigencia distinta del archivo |
| Tratar el trabajo como rediseño declarado, no como mezcla de modos | §4 «Trabajo por secciones, con comparación»: hay tres modos (crear, rediseñar, mejorar una sección) y conviene decir cuál se está usando |
| Poder decir en qué mejoró el resultado | §4: una mejora cuenta solo si se puede decir en qué mejoró. Aquí la mejora es enunciable en una cifra: síntomas del diagnóstico, 1 → 0 |

### Biblioteca-prompts, segundo-yo y barbería: identidad tipográfica propia

Cada una de las tres apps recibió una pasada de identidad
tipográfica con una fuente de marca propia: Fraunces en
biblioteca-prompts, Sora en segundo-yo y Oswald en la demo de
barbería.

Mapeo intervención → criterio:

| Intervención | Punto del archivo que la motivó |
|---|---|
| Sustituir la tipografía sin personalidad por una fuente propia por app | §1, primer síntoma: «Tipografía por defecto, sin personalidad ni jerarquía clara entre título, subtítulo y cuerpo» |
| Que la fuente elegida sostenga la jerarquía título / subtítulo / cuerpo de cada app | §3 «Reglas anti-genérico», regla «Jerarquía por contraste real»: tamaño, peso y espacio deben decir qué importa |

Precisión de atribución: el archivo de criterios diagnostica la
tipografía por defecto como síntoma; no nombra Fraunces, Sora ni
Oswald ni prescribe una fuente por app. Esas tres elecciones son la
respuesta concreta de Dirsi a ese diagnóstico, no contenido de la
guía ni del archivo de criterios.

## Ciclo 4: un gesto de cabecera por app en el conjunto web3

El conjunto web3 compartía una sola plantilla. La intervención fue
dar a la cabecera de cada app un gesto visual propio, como capa de
presentación, sin tocar lógica ni datos. Los gestos aplicados
fueron: línea de hash, curva de gas, fila de bloques, velas, barra
de editor, marcos de galería, ruta, cinta de advertencia y chip de
tarjeta. Esta nota no asigna cada gesto a una app concreta: el
registro verificado es el conjunto de gestos, no su correspondencia
una a una.

Una app, dao-vote, quedó intencionalmente sin gesto, por tener
identidad suficiente ya.

Mapeo intervención → criterio:

| Intervención | Punto del archivo que la motivó |
|---|---|
| Dar a cada cabecera un recurso visual principal y distinto | §3, regla «Una decisión visual por sección»: cada sección tiene un recurso principal; no compiten tres. Aquí la sección intervenida es la cabecera |
| Diferenciar apps que compartían plantilla con un gesto ligado a lo que cada una hace (hash, gas, bloques, velas…) | §1, síntomas «Rejilla de tarjetas todas iguales, mismo peso, mismo tamaño» y «Texto de relleno intercambiable: podría ser la web de cualquier negocio sin cambiar una palabra», llevados a escala de conjunto: sin gesto propio, cada app podría ser cualquiera de las demás |
| Romper la uniformidad del conjunto al menos en la cabecera de cada app | §3, regla «Romper la rejilla al menos una vez»: un cambio de ritmo para que la página no sea un catálogo uniforme. Aplicada aquí entre apps, no solo dentro de una página |
| Limitar el cambio a la capa de presentación, sin tocar lógica ni datos | §4: el modo de trabajo se declara y el alcance se respeta. El modo fue mejorar la presentación de una sección (la cabecera), no rediseñar el funcionamiento |
| Dejar dao-vote sin gesto por tener identidad suficiente | §7, paso 3 (Pulido): corregir solo lo anotado. Y §4: una mejora cuenta solo si se puede decir en qué mejoró; donde el diagnóstico no anotó falta de identidad, añadir un gesto no era una mejora enunciable |

Precisión de atribución, igual que en el Ciclo 2: ningún gesto de
esta lista aparece en el archivo de criterios. Lo que el archivo
aporta es el diagnóstico de lo intercambiable y las reglas de la
sección 3; los gestos concretos son decisiones de Dirsi para este
conjunto.

## Límite de verificación (declarado, no disimulado)

La VM donde se hizo el trabajo no tiene navegador visual. Por tanto:

- La conformidad con los criterios se verificó por código, por
  bundles y contra la checklist de salida de
  `criterios-diseno-centeia.md`. No se verificó por captura.
- Eso deja sin cumplir, tal como están redactados, dos puntos del
  propio archivo: §6 «Verificación obligatoria» pide «Capturas en
  dos anchos» (escritorio y móvil lado a lado), y la checklist de
  salida incluye «Capturas de escritorio y móvil comparadas».
  En esta nota esos ítems quedan pendientes, no marcados como
  hechos.
- La verificación visual queda pendiente de la mirada de Antonio
  en su laptop. Hasta que esa mirada ocurra, lo afirmado aquí es
  conformidad por código, bundle y checklist — no conformidad
  vista en pantalla. Es la misma salvedad que ya quedó registrada
  para la pasada del Ciclo 2 en `log.md`.

## Qué deja esta nota

- El diagnóstico de la sección 1 sirve como instrumento de medida,
  no solo como lista de advertencias: permite cerrar un rediseño
  con un conteo (1 → 0 en segundo-yo).
- Las reglas de la sección 3 escalan de una página a un conjunto:
  aplicadas a las cabeceras hermanas del conjunto web3, producen
  diferenciación sin tocar lógica ni datos.
- La pasada final de la sección 7 también protege lo que ya está
  bien: dao-vote demuestra que «corregir solo lo anotado» incluye
  no intervenir.
