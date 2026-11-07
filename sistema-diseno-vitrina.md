# Sistema de diseño de vitrina — destilación del sistema de Grok Build

**Origen.** El 7 de noviembre de 2026 Antonio exportó el workspace completo de una app construida con Grok Build (la app «Factory · Estudio · Currículum») y Dirsi lo inspeccionó archivo por archivo. Dentro venía el sistema de diseño que la plataforma precarga a su constructor: una skill de diseño de interfaz con cinco referencias (UI refinada, tipografía, superficies, animación, rendimiento), una referencia de control de calidad en navegador y el CSS real de la app construida.

**Método.** Destilación con redacción propia: se extraen principios, parámetros y recetas —que son método, no obra— y se reescriben en el lenguaje de este repositorio. Nada de texto literal del original vive aquí. Nivel de evidencia: A (leído de primera mano en la exportación).

**Relación con lo existente.** `criterios-diseno-centeia.md` recoge los criterios que Dirsi ya usaba. Este documento los complementa con algo que faltaba: un sistema **cuantificado** (escalas cerradas, fórmulas y recetas de movimiento con números). Cuando ambos discrepen, manda el checklist final de la sección 11.

---

## 1. Principio rector: el sistema antes que el estilo

Ningún valor suelto llega a un componente. Antes de estilar cualquier pantalla se define, en un solo lugar (en Tailwind v4, el bloque `@theme` del CSS; en otro stack, las variables raíz):

- paleta semántica (fondo, superficie, elevado, texto, texto atenuado, borde, acento),
- escala de radios, escala de espaciado, escala tipográfica,
- tokens de movimiento (duraciones, curvas, distancias, escalas).

Si un valor no existe como token ni como paso de escala, no se usa: se crea el token o se rediseña el elemento. Corolario práctico en Tailwind v4: su preflight deja los botones con cursor por defecto; se corrige una vez en la base para que todo elemento pulsable muestre puntero de mano.

Componentes: si el stack es React + Tailwind, se parte de primitivas accesibles tipo shadcn/Radix y se visten con los tokens, en vez de fabricar botones e inputs a mano. La estructura de un componente conocido (variantes, estados, foco) es parte del acabado.

## 2. Parámetros base del sistema

**Espaciado** — escala de pasos de 4: 4, 8, 12, 16, 24, 32, 48, 64 px. Nada fuera de la escala.

**Radios** — 4, 8, 12, 16, 24 px, y pastilla completa (9999) solo para chips y botones pequeños.

**Tipografía fluida** — tamaños con `clamp()` para que escalen con la ventana sin saltos:
- XS ≈ 0,75–0,81 rem · S ≈ 0,875–0,94 · base ≈ 1–1,06 · L ≈ 1,125–1,25 · XL ≈ 1,5–2 · 2XL ≈ 2–3 · 3XL ≈ 2,5–4.
- Interlineado: 1,1 titulares grandes, 1,25 títulos, 1,5 cuerpo.
- Tracking: −0,02 em en texto grande, −0,03 em en titulares de portada.

**Movimiento** — duraciones por rol: micro 80 ms · cierre y cambios en sitio 150 ms · aperturas principales 250 ms · salida de paneles 350 ms · revelado de contenido 400 ms · énfasis raro 500 ms · desfase entre elementos de una lista 40 ms. Curva principal de salida suave: `cubic-bezier(0.22, 1, 0.36, 1)`. Distancias de entrada: 4–12 px. Escalas de apertura: modales desde 0,96, menús desde 0,97, tooltips desde 0,98 — **nunca desde 0**. Desenfoque auxiliar en cruces: 2–3 px.

## 3. Disciplina de color

1. Los neutros ocupan el 90 % o más de la superficie: fondos casi blancos o casi negros, grises quietos, bordes translúcidos derivados del color de texto (así se adaptan solos a claro y oscuro).
2. **Una sola familia de acento**, reservada a acción principal y foco. Prohibidos como acento de marca salvo encargo expreso: púrpura, violeta, magenta, amarillo, dorado, naranja.
3. Gradientes: solo si son casi invisibles (lavado lineal con salto de luminosidad ≤ 8 %). Nada de auroras, mallas de color ni fondos «IA púrpura».
4. Iconos en monocromo o `currentColor`; el color no viene de emojis.
5. Estados semánticos (éxito, aviso, peligro) con verde, ámbar y rojo **contenidos**: solo en insignias e iconos pequeños, nunca paneles enteros.
6. Contraste AA en texto de cuerpo; el texto atenuado es solo para etiquetas secundarias.

## 4. Tipografía

- Una familia con contraste de pesos, o una pareja sobria (titular + cuerpo). Nunca más de dos familias; mono solo para código, cifras e identificadores.
- Pesos por rol: titulares 500–600, cuerpo 400, etiquetas 500, botones 500–600. Nada de negros 900 en texto grande.
- Máximo tres tamaños efectivos por pantalla (sin contar microtexto legal).
- Titulares y bloques cortos con `text-wrap: balance`; cuerpo largo con `text-wrap: pretty` (evita huérfanos sin coste en textos largos).
- Suavizado de fuente activado una sola vez en la raíz (`antialiased`).
- Cifras vivas (contadores, precios, tiempos, tablas) con `tabular-nums` para que no baile el layout al cambiar el valor.
- Ancho de lectura 60–75 caracteres; el titular de portada puede romperlo con intención.

## 5. Superficies y detalle fino

- **Radios concéntricos, obligatorios:** radio exterior = radio interior + relleno entre ambos. Cada nivel de anidación baja un paso de la escala. El mismo radio en padre e hijo es el defecto silencioso más común.
- **Sombra en vez de borde** en tarjetas, botones y contenedores con profundidad: la sombra se adapta a cualquier fondo; el borde sólido, no. Receta clara: anillo de 1 px al 6 % de negro + sombra suave de 1–2 px al 6 % + ambiente de 4 px al 4 % (en hover, subir a 8/8/6 %). En oscuro basta el anillo blanco al 8 % (13 % en hover). Los divisores y límites de tabla **siguen siendo bordes**: separan, no elevan.
- Imágenes con contorno interior de 1 px al 10 % (outline con offset −1, no suma layout).
- **Alineación óptica:** en botones con texto + icono, el lado del icono lleva ~2 px menos de relleno; el triángulo de «play» se desplaza ~2 px a la derecha; los iconos asimétricos se corrigen en el propio SVG.
- **Área de toque mínima 44 × 44 px** (40 como suelo): si el elemento visible es menor, se extiende el área con un pseudo-elemento, sin invadir el área de otro elemento interactivo.
- Profundidad con mesura: bordes finos y una sola receta de sombra suave; panel elevado = un paso más claro que el fondo, no una losa gris.

## 6. Anti-slop: lo que delata diseño genérico

| Prohibido | En su lugar |
| --- | --- |
| Emojis como iconos o en titulares y estados vacíos | Tipografía sobria o iconos SVG de un set real (Lucide) |
| Masas de gradiente y resplandores como relleno | Superficies planas o casi planas con jerarquía |
| Ilustraciones SVG dibujadas a mano | Librerías reales (gráficos con Recharts) o imágenes reales/generadas |
| Cajas grises «placeholder» en el producto final | Contenido real desde el primer pase |
| La misma fuente por defecto sin jerarquía | Pareja deliberada y pasos de peso |
| Cristal esmerilado en cadena, bordes arcoíris, brillos neón | Bordes finos neutros, sombras de una capa |
| Valores mágicos (13 px, 27 px) | La escala de espaciado |
| Rebote en cada control | Movimiento corto con tokens; overshoot solo en micro-momentos raros (una insignia) |

Cada elemento gana su sitio o se corta. Los estados vacío, cargando y error son parte del diseño, no una sorpresa posterior. Al editar una app existente se respeta su lenguaje visual: no se introduce un segundo sistema.

## 7. Movimiento: catálogo de recetas

Reglas universales:

- Preferir **transiciones CSS** (interrumpibles: si la persona cambia de idea a mitad, la animación se redirige sin saltos). Keyframes solo para secuencias escenificadas de una sola vez.
- Enumerar propiedades (`opacity, transform` y blur solo si hace falta). **`transition: all` está prohibido** (ver también §8).
- Entrar más lento que salir: la apertura usa el token de 250 ms; el cierre, el de 150 ms.
- Nada entra desde escala 0; menús y popovers crecen **desde su disparador**; modales, desde el centro.
- Todo respeta `prefers-reduced-motion` (solo opacidad o instantáneo).
- Las duraciones viven en variables CSS para que el JS que orquesta lea los mismos valores y no se desincronice.
- Al cerrar con clase de salida, retirarla tras el timeout: si no, la próxima apertura salta desde la escala equivocada.

Recetas por patrón visible:

- **Menú desde disparador:** escala 0,97→1 + opacidad, 250 ms al abrir, 150 ms al cerrar.
- **Modal centrado:** escala 0,96→1, 250/150 ms; el velo solo cambia opacidad.
- **Panel lateral:** traslación en su eje + blur ligero opcional; 400 ms al abrir, 350 ms al cerrar.
- **Lista ↔ detalle:** traslaciones opuestas de 8 px + blur 2–3 px, 250 ms.
- **Cifra que cambia:** cada dígito re-entra con desplazamiento de 4 px y blur de 2 px, desfase de 40 ms, siempre con `tabular-nums`.
- **Intercambio de icono en un control** (play/pausa, silencio/sonido): ambos iconos conviven en el DOM y se cruzan con escala, opacidad y blur de 4 px, ~300 ms sin rebote.
- **Texto que cambia en un hueco:** el saliente se va en una dirección, el entrante llega de la contraria, 150 ms.
- **Entrada de pantalla:** revelar por grupos semánticos (título, descripción, acciones) con desfase de ~100 ms entre grupos; entradas con opacidad + 12 px + blur 4 px. Salidas más cortas y suaves que las entradas (150 ms, −12 px).
- **Pulsación de botón:** escala 0,96 al presionar (nunca menos de 0,95), con prop de escape para botones donde distraiga.
- **Esqueleto → contenido:** pulso lineal del placeholder y cruce con blur ligero, 400 ms.
- **Error en un campo:** sacudida corta segmentada, con la clase de «error» separada de la clase de «sacudida» para poder repetirla sin re-render.
- **No animar en la carga inicial** lo que ya nace en su estado por defecto (interruptores, iconos de estado): animar solo cambios posteriores.

## 8. Rendimiento de la interfaz

- Transicionar **solo** las propiedades que cambian. La shorthand genérica obliga al navegador a vigilarlo todo y produce transiciones no deseadas.
- `will-change` con criterio quirúrgico: solo en propiedades componibles por GPU (transform, opacity, filter, clip-path) y solo cuando se observa tartamudeo en el primer frame. Cada capa extra cuesta memoria; nada de aplicarlo «por si acaso» ni sobre color, padding o dimensiones.

## 9. Control de calidad visual y de marca

El constructor no declara «terminado» sin mirar su propio trabajo:

1. **Pase de humo en dos ventanas** (escritorio 1280×800 y móvil 390×844) con veredicto estructurado: estado HTTP, errores de consola y de página, desbordamiento horizontal y longitud del texto. Las capturas **se leen con ojos**, no se archivan sin mirar.
2. **Pase contra el build**: servir la versión construida y comparar con la línea base del pase en desarrollo; solo se re-revisan las capturas si el veredicto marca divergencia.
3. **Pase interactivo** cuando la app tiene algo que manejar: ejecutar el flujo que haría una persona y afirmar el resultado con una comprobación que **falle en voz alta** (una aserción que lanza), no con una marca de «ok» — una página de error también devuelve «ok». Las referencias a elementos de una captura de accesibilidad caducan con cada cambio del DOM: re-capturar tras navegar o clicar. La profundidad del pase se ajusta a la app: una landing se agota en el pase de humo; un control invertido (izquierda/derecha) no se despacha jamás sin probar.
4. **Identidad al compartir:** toda app que se publica lleva su tarjeta de enlace (1200×630, custom por defecto salvo utilidades puras, donde vale la genérica), favicon SVG nítido a 16 px y —solo si se pide instalable— iconos PWA. La pasada de marca corre en paralelo y no bloquea la entrega; si la tarjeta llega tras publicar, se republica.

## 10. La muestra real: tokens de la app exportada

La app «Factory · Estudio · Currículum» instanció el sistema con identidad propia:

- **Paleta marina:** fondo `#0e2744`, superficie `#16365c`, espuma `#e8f1fb`, tinta `#10233b`, acento cielo `#3d7adf`, niebla `#b7cbe3`; línea como mezcla translúcida al 20 %.
- **Tipografía:** serif editorial (Newsreader) para nombres y titulares + Public Sans para el cuerpo; titular de portada con `clamp(2,8rem, 6,4vw, 5,1rem)`, interlineado 0,96 y tracking −0,03.
- **Hábitos visibles en su CSS:** objetivos de toque de 44 px (2,75 rem) en toda la navegación, foco visible con contorno de 2 px, guardas de `prefers-reduced-motion`, regla de impresión, y la corrección de cursor de Tailwind v4 aplicada en la base.

**Observación honesta (de la inspección, no del sistema):** la app concreta no cumple el sistema al 100 % — usa resplandores radiales y una rejilla en perspectiva con brillo que las referencias documentales desaconsejan. Conclusión útil: el *sistema escrito* es más disciplinado que esta *salida concreta*; lo que aquí se adopta es el sistema y lo que la muestra demuestra hacer bien (tokens, fluidez, accesibilidad básica), no cada decisión de esa app.

## 11. Qué no transfiere esta destilación

- **El prior generativo del modelo:** el gusto entrenado que ubica bien el primer borrador cuando ninguna plantilla encaja. Vive en los pesos; no viaja en documentos (misma lección que la anatomía de Kimi K3: leer la receta no hornea el pan).
- **Sus herramientas de imagen integradas** (generación de arte, tarjeta e iconos dentro del mismo flujo).
- **Su bucle interno de vista previa:** él captura y corrige dentro de la sesión de generación; Dirsi verifica con su ojo visual local, fuera de ese bucle y más despacio. La velocidad, aquí, es iteraciones: más iteraciones visuales por sesión = más pulido final.

Consecuencia práctica: este sistema cubre el diseño «de molde» (la gran mayoría: paneles, landings, CRUD, portafolios). La dirección de arte desde cero —identidad visual nueva, ilustración— sigue siendo el territorio donde Grok conserva ventaja, y se alquila con sus tokens cuando un proyecto lo pida.

## 12. Checklist de cierre (antes de declarar una interfaz terminada)

- [ ] Tokens definidos en un solo lugar; ningún hex suelto ni valor arbitrario en componentes
- [ ] ≤ 5 colores, ≤ 2 familias, escala de espaciado consistente
- [ ] Radios concéntricos en todo anidamiento
- [ ] Contraste AA; donde cambia el fondo, cambia también el texto
- [ ] Móvil ~390 px sin desbordamiento; áreas de toque ≥ 44 px
- [ ] Iconos e imágenes reales; cero señales anti-slop de la §6
- [ ] Estados vacío, cargando y error diseñados
- [ ] Movimiento con tokens, abrir/cerrar asimétrico, sin `transition: all`, con guarda de movimiento reducido
- [ ] Cifras vivas con `tabular-nums`; titulares con `balance`, cuerpo con `pretty`
- [ ] Verificado con capturas reales (escritorio y móvil) leídas por quien construye
- [ ] Tarjeta de enlace y favicon resueltos si la app se publica

---

*Destilado por Dirsi el 2026-11-07 desde la exportación del workspace de Grok Build aportada por Antonio. Documento de método: parámetros y principios reescritos, sin texto literal de la fuente.*
