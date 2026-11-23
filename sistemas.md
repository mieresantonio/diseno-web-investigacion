# Sistemas de color y tipografía usados de verdad

Los sistemas 2–5 usan la misma pila tipográfica del sistema
(`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`), títulos
con `letter-spacing` negativo (-0.01 a -0.02em) y tamaños fluidos con
`clamp()`. La diferencia entre sistemas es la paleta y el carácter,
no la tipografía. Excepción: Block Ethos (sistema nº 1) usa fuentes
web propias (Space Grotesk, Inter, JetBrains Mono); ver su sección.

## 1. Block Ethos — oscuro web3 (producto serio, educación tech)
Uso: plataformas de aprendizaje, dashboards de producto, temas
tecnológicos donde el oscuro es la norma.
```css
:root {
  --bk-blue: #2563eb; --bk-violet: #7c3aed; --bk-cyan: #06b6d4;
  --bk-gold: #f5b942;
  --bk-bg: #070d1a; --bk-navy: #0b1120;
  --bk-panel: #0e1730; --bk-panel-2: #111d3a;
  --bk-line: rgba(148, 163, 184, 0.14);
  --bk-line-2: rgba(148, 163, 184, 0.26);
  --bk-text: #e9eefb; --bk-muted: #97a3bd; --bk-muted-2: #6b7794;
  --bk-grad: linear-gradient(92deg, #2563eb 0%, #7c3aed 55%, #06b6d4 110%);
  --bk-radius: 18px;
  /* Bootstrap 5.3 re-tematizado con los tokens propios */
  --bs-body-bg: var(--bk-bg); --bs-body-color: var(--bk-text);
  --bs-primary: var(--bk-blue); --bs-card-bg: var(--bk-panel);
}
```
Tipografía: Space Grotesk (titulares) · Inter (texto) ·
JetBrains Mono (código y datos). Es la excepción a la pila del
sistema que comparten los demás sistemas de este archivo.
Notas: un solo set de iconos (Lucide). Fondo con patrón de nodos
en la landing (`landing-decor`, SVG en línea) y resplandores
radiales tenues sobre el fondo navy. Los botones principales usan
el degradado de marca; el botón deshabilitado pierde el degradado
y la sombra para parecer deshabilitado de verdad (Bootstrap solo
baja la opacidad y el gradiente seguía viéndose activo). Rompe a
conciencia la regla de una sola familia de acento del sistema de
vitrina (§3): el degradado tricolor es la marca del producto, no
un acento funcional. Sirve para productos con identidad técnica;
no usar para negocios de barrio (demasiado frío) ni para
contenido editorial.

## 2. Barbería — oscuro + dorado (negocio local con carácter)
Uso: negocios locales, servicios con cita, marcas que quieren verse
premium sin parecer corporativas.
```css
:root {
  --bg: #12100e; --panel: #1d1a17; --panel2: #26211c;
  --gold: #d9a441; --gold2: #f2c572;
  --text: #f5efe6; --muted: #b8ab98; --line: #3a322a;
  --green: #4caf7d; --red: #d9534f;
}
```
Notas: ancho máximo 1080 px; hero `clamp(2rem, 5vw, 3.2rem)`; tarjetas
con elevación al hover (`translateY(-3px)` + borde dorado); anillo de
foco dorado en todo lo interactivo; estados de celda libre/ocupado/
almuerzo con colores distintos (verde/rojo/tachado). El dorado funciona
porque el fondo es casi negro cálido, no gris.

## 3. Segundo Yo — violeta + ámbar sobre claro (herramienta amable)
Uso: herramientas de productividad personal, apps de aprendizaje,
contenido que debe sentirse cercano y no técnico.
```css
:root {
  --ink: #1e1b2e; --muted: #6b6780;
  --violet: #6d28d9; --violet-soft: #ede9fe;
  --amber: #d97706; --amber-soft: #fef3c7;
  --bg: #faf9fc; --card: #ffffff; --border: #e5e1f0;
  --radius: 14px;
  /* Escala de espaciado, base 4px */
  --space-xs: 4px; --space-sm: 8px; --space-md: 16px;
  --space-lg: 24px; --space-xl: 32px; --space-2xl: 48px;
}
```
Notas: hero centrado; pestañas en píldora; foco ámbar de 3 px;
transiciones desactivadas con `prefers-reduced-motion`; tarjetas con
`auto-fill, minmax(260px, 1fr)` en vez de columnas fijas. La escala de
espaciado con nombre es la práctica que las demás apps deberían copiar.

## 4. Biblioteca de prompts — índigo claro (contenido y búsqueda)
Uso: bibliotecas, catálogos, apps donde el contenido y los filtros son
el producto.
```css
body { background: #f5f4f0; color: #1f2430; }
.hero {
  background: linear-gradient(120deg, #312e81, #4f46e5 55%, #0e7490);
}
:focus-visible { outline: 3px solid #f59e0b; outline-offset: 2px; }
```
Notas: hero con degradado y pestañas que se invierten al color de
fondo al activarse; tarjetas blancas con sombra suave y elevación al
hover; panel lateral del constructor fijo (`position: sticky`); bloque
de texto ensamblado en oscuro (`#1f2430`) para distinguir «salida» de
«entrada». Foco ámbar visible también sobre el hero oscuro (cambia a
`#fde68a` dentro del hero).

## 5. Interfaz del rag-demo — teal claro (herramienta de consulta)
Uso: herramientas de pregunta-respuesta, consulta de documentos,
utilidades de una sola tarea donde la respuesta es el producto.
```css
:root {
  --fondo: #fafaf7; --superficie: #ffffff; --elevado: #f3f3ee;
  --texto: #1c1c1a; --atenuado: #6f6f68; --borde: #e3e3db;
  --acento: #0f766e; --acento-suave: #e6f5f3;
  --aviso: #92400e; --aviso-suave: #fef3c7;
  --error: #b91c1c; --error-suave: #fee2e2;
  --radio-s: 4px; --radio-m: 8px; --radio-l: 12px; --radio-xl: 16px;
}
```
Notas: una sola columna fluida (máximo 720 px), sin puntos de corte
de layout; botón de 44 px de alto mínimo; cifras con
`tabular-nums`; guardas de `prefers-reduced-motion`. El estado «ok»
reusa el acento teal: no hay verde de éxito separado. Aviso y error
van en tintas pálidas (`--aviso-suave`, `--error-suave`), nunca
saturados. Primera interfaz construida con el sistema
diseno_vitrina tras el portafolio (16 nov 2026).

## Cuándo usar cada uno
| Sistema | Úsalo para | No lo uses para |
|---|---|---|
| Block Ethos web3 | Producto tech, dashboards | Negocios locales, editorial |
| Barbería dorado | Servicios con cita, marca premium | Herramientas de texto, datos |
| Segundo Yo violeta | Productividad, aprendizaje | Marcas que necesitan sobriedad |
| Biblioteca índigo | Catálogos, búsqueda, filtros | Landing de un solo mensaje |
| Interfaz rag-demo teal | Consulta de documentos, utilidades de una tarea | Marcas que necesitan calidez, editorial |

Regla común: fondo, panel, texto, texto atenuado, línea, acento y
acento suave, más un color de éxito y uno de error. Nada más.
