# Sistemas de color y tipografía usados de verdad

Todos usan la misma pila tipográfica del sistema
(`system-ui, -apple-system, "Segoe UI", Roboto, sans-serif`), títulos
con `letter-spacing` negativo (-0.01 a -0.02em) y tamaños fluidos con
`clamp()`. La diferencia entre sistemas es la paleta y el carácter, no
la tipografía.

## 1. Blockali — oscuro web3 (producto serio, educación tech)
Uso: plataformas de aprendizaje, dashboards de producto, temas
tecnológicos donde el oscuro es la norma.
```css
:root {
  --bk-primary: #2563eb;
  --bk-violet: #7c3aed;
  --bk-cyan: #06b6d4;
}
.hero {
  background: linear-gradient(92deg, #2563eb, #7c3aed 55%, #06b6d4);
}
```
Notas: un solo set de iconos (Lucide). Fondo con patrón de nodos en
la landing. Sirve para productos con identidad técnica; no usar para
negocios de barrio (demasiado frío) ni para contenido editorial.

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

## Cuándo usar cada uno
| Sistema | Úsalo para | No lo uses para |
|---|---|---|
| Blockali web3 | Producto tech, dashboards | Negocios locales, editorial |
| Barbería dorado | Servicios con cita, marca premium | Herramientas de texto, datos |
| Segundo Yo violeta | Productividad, aprendizaje | Marcas que necesitan sobriedad |
| Biblioteca índigo | Catálogos, búsqueda, filtros | Landing de un solo mensaje |

Regla común: fondo, panel, texto, texto atenuado, línea, acento y
acento suave, más un color de éxito y uno de error. Nada más.
