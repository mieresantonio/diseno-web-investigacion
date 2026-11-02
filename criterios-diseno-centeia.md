# Criterios de diseño aplicables (desde la guía CenteIA)

Origen: la evaluación que Dirsi hizo en octubre de 2026 de una guía
externa de diseño web con IA (materiales CenteIA). De esa guía lo que
sirve aquí no es su parte de instalación —pensada para otro entorno—
sino su criterio: cómo reconocer el diseño genérico, cómo encargar un
diseño con datos concretos y cómo revisarlo antes de darlo por bueno.
Todo está reformulado con palabras propias; nada es texto de la guía.

Advertencia de evidencia: la guía citaba repositorios de terceros
(skills de diseño y animación, librerías de componentes) que Dirsi no
ha verificado de primera mano. Aquí no se recomienda instalar nada:
solo se destila el criterio, que es aplicable a cualquier build.

## 1. Diagnóstico: señales de diseño genérico

Una página «hecha por IA sin criterio» se reconoce por estos síntomas.
Si una build acumula tres o más, no está lista:

- Tipografía por defecto, sin personalidad ni jerarquía clara entre
  título, subtítulo y cuerpo.
- El degradado morado-azul de siempre como único recurso visual.
- Rejilla de tarjetas todas iguales, mismo peso, mismo tamaño.
- Todo centrado: cada sección con el mismo eje y el mismo ritmo.
- Espaciado uniforme en todas partes, sin zonas de respiro ni zonas
  densas que marquen importancia.
- Texto de relleno intercambiable: podría ser la web de cualquier
  negocio sin cambiar una palabra.
- Botones y llamadas a la acción idénticos en secciones con objetivos
  distintos.

La causa no es la herramienta: es falta de decisiones previas (para
quién, para qué, con qué tono) y falta de piezas buenas de referencia.

## 2. Antes de construir: el brief mínimo

Ninguna build empieza sin estas seis respuestas por escrito:

1. **Negocio**: qué es y qué ofrece, en una frase.
2. **Público**: quién entra y qué viene a resolver.
3. **Objetivo**: la única acción que la página debe provocar.
4. **Secciones**: lista cerrada, en orden de importancia.
5. **Estilo**: tres adjetivos de tono (ej.: sobrio, cálido, técnico).
6. **Colores**: paleta decidida antes, no descubierta sobre la marcha.

Sin brief, el resultado cae en el diagnóstico de la sección 1.

## 3. Reglas anti-genérico

- **Una decisión visual por sección**: cada sección tiene un recurso
  principal (una imagen, un dato, una interacción); no compiten tres.
- **Romper la rejilla al menos una vez**: una sección asimétrica, un
  elemento que se sale del margen o un cambio de ritmo, para que la
  página no sea un catálogo uniforme.
- **Jerarquía por contraste real**: tamaño, peso y espacio deben
  decir qué importa; si todo grita, nada se escucha.
- **Contenido específico o nada**: textos con datos del negocio real
  (precios, nombres, horarios) o huecos marcados como pendientes;
  nunca relleno que suene profesional y no diga nada.
- **Color con sistema, no con ocurrencias**: la paleta del brief se
  convierte en tokens (ver `sistemas.md`) y no aparecen colores
  nuevos a mitad de página.
- **Componentes con referencia**: antes de inventar un componente,
  mirar cómo lo resuelven librerías de componentes curadas; copiar la
  estructura, no el aspecto de otra marca.

## 4. Trabajo por secciones, con comparación

- Nunca se juzga la página entera de una vez: se construye y se
  evalúa **sección por sección**, y cada sección se compara contra su
  versión anterior antes de seguir.
- Hay tres modos de trabajo, y conviene decir cuál se está usando:
  crear desde cero, rediseñar algo existente o mejorar una sola
  sección. Mezclarlos sin decirlo produce cambios sin criterio.
- Una mejora cuenta solo si se puede decir en qué mejoró (más claro,
  más rápido de escanear, objetivo más visible). «Se ve mejor» no es
  un criterio.

## 5. Movimiento con criterio

- La animación explica, no decora: sirve para mostrar que algo
  cambió, llegó o se puede tocar.
- Duraciones cortas y consistentes en toda la app; una interfaz que
  tarda en reaccionar se siente rota aunque sea bonita.
- Entradas suaves, salidas rápidas: lo que aparece puede tomarse su
  tiempo; lo que desaparece, no.
- Si el sistema pide reducir movimiento, la app lo respeta; ninguna
  animación es imprescindible para usar la app.

## 6. Verificación obligatoria

- **Móvil siempre**: cada sección se revisa en ancho de teléfono
  antes de darse por buena (ver principio 2 de `principios.md`).
- **Capturas en dos anchos**: escritorio y móvil lado a lado; los
  desajustes que no se ven en el código aparecen en la captura.
- **Formularios y enlaces probados de verdad**: enviar el formulario,
  pulsar cada enlace y cada botón; un diseño con un enlace roto no
  está terminado.
- **Todos los estados**: vacío, cargando, error y confirmación
  existen y se ven bien (ver principio 8 de `principios.md`).

## 7. Pasada final en tres tiempos

Antes de cerrar cualquier build, en este orden:

1. **Crítica**: recorrer la página con el diagnóstico de la sección 1
   y anotar cada síntoma presente, sin corregir todavía.
2. **Auditoría**: comprobar brief contra resultado (¿está el
   objetivo? ¿sobra alguna sección?) y correr la verificación de la
   sección 6.
3. **Pulido**: corregir solo lo anotado, en pasadas cortas, y volver
   a capturar para comparar. Si una corrección empeora otra sección,
   se anota en `lecciones.md`.

## Checklist rápida (la puerta de salida)

- [ ] Brief de 6 puntos escrito antes de construir.
- [ ] Diagnóstico de genérico: menos de 3 síntomas.
- [ ] Una decisión visual principal por sección.
- [ ] Al menos un quiebre de ritmo en la página.
- [ ] Textos específicos del negocio, sin relleno.
- [ ] Revisión en móvil hecha sección por sección.
- [ ] Capturas de escritorio y móvil comparadas.
- [ ] Formulario enviado y enlaces pulsados en la prueba.
- [ ] Estados vacío, carga, error y confirmación presentes.
- [ ] Pasada crítica → auditoría → pulido completada.
