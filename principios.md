# Principios de diseño de Dirsi

Cada principio lleva su porqué en una línea y un ejemplo real de una
app construida. Si un principio no tiene ejemplo, es teoría: no entra.

## 1. El flujo completo manda sobre la landing bonita
Porqué: una landing sin flujo que funcione no se puede usar ni vender.
Ejemplo: en el demo de barbería, el criterio de «listo» no fue que la
landing se viera bien, sino que un visitante pudiera reservar, cancelar
y ver el hueco liberado en la agenda.

## 2. Móvil primero, porque el usuario es phone-first
Porqué: Antonio revisa y aprueba todo desde el teléfono; si en móvil se
rompe, el diseño está roto.
Ejemplo: en las 4 apps, los puntos de corte bajan a 700/560/480 px, las
tarjetas pasan de 3 columnas a 1 y los botones de acción pasan a ancho
completo en móvil.

## 3. Un solo set de iconos, siempre
Porqué: mezclar librerías produce inconsistencia visual y peso muerto.
Ejemplo: Blockali llegó con tres librerías a la vez (Font Awesome por
CDN, bootstrap-icons y lucide-react); el rediseño unificó todo a Lucide.

## 4. Los datos de ejemplo van siempre etiquetados
Porqué: un demo que parece real engaña al cliente y al propio autor.
Ejemplo: el demo de barbería lleva la etiqueta «datos de ejemplo» en
cabecera, secciones, agenda y pie de página, no solo en un aviso legal.

## 5. Verificar diseñando: renderizar, mirar, corregir
Porqué: el ojo detecta desajustes que leyendo código no se ven.
Ejemplo: es el bucle que hace bueno a Kimi K3 (generar → renderizar →
mirar → corregir) y el que usó Dirsi: el bug de render del chat de la
barbería se detectó escribiendo el componente, no leyendo el plan.

## 6. La tarea antes que la herramienta
Porqué: elegir la herramienta primero produce apps que nadie necesita.
Ejemplo: la app Segundo Yo no empieza por un modelo ni una API, sino
por la ficha «Cuando ____, me gustaría que mi segundo yo ____, para
obtener ____»: primero la tarea que se repite, luego el resto.

## 7. Primera versión de la máquina, criterio de la persona
Porqué: la IA propone rápido y la persona decide lo que importa.
Ejemplo: las apps CenteIA preparan borradores (fichas, prompts, listas)
y dejan la edición, el guardado y el envío en manos del usuario; nunca
se publica nada solo.

## 8. Todos los estados existen: carga, vacío, error, confirmación
Porqué: una app que solo diseña el caso feliz se rompe en el primer uso
real.
Ejemplo: la app Segundo Yo tiene estado vacío con borde discontinuo
para búsquedas sin resultados; la barbería muestra confirmación verde,
errores 409 con mensaje claro («ese hueco choca con el almuerzo») y
celdas distintas para libre, ocupado y almuerzo.

## 9. Un sistema de tokens, nunca colores sueltos
Porqué: sin tokens, cada pantalla inventa su propio gris y el producto
se deshilacha.
Ejemplo: las 4 apps definen sus colores en `:root` (`--bg`, `--panel`,
`--gold`, `--violet`, `--border`…) y ningún componente usa un color
hexadecimal directo salvo el token.

## 10. Contenido propio, nunca copia
Porqué: el portafolio debe mostrar trabajo del autor, no material ajeno
republicado.
Ejemplo: las apps CenteIA usan las estructuras del curso (ficha,
6 campos del prompt, 5 grupos de tareas) con redacción propia; y el
método de clonación limpia exige construir desde una especificación,
nunca desde el material original.

## 11. Una pantalla o un flujo por vez, completo y verificado
Porqué: avanzar por rebanadas verticales evita el «casi todo hecho y
nada funciona».
Ejemplo: el método de clonación limpia y la construcción de la barbería
(landing → agenda → chat → enlace) dejan cada pieza verificada antes
de pasar a la siguiente.
