# Lecciones: lo que falló o decepcionó

Cada lección lleva fecha y qué cambió después. No se borran.

## 2026-10-21 — Los modelos pequeños gratuitos diseñan flojo
Hecho: el modelo gratuito del teléfono (North Mini Code) construyó un
portafolio correcto pero visualmente pobre, y una pasada de mejora
apenas lo cambió. El usuario quedó decepcionado.
Lección: para diseño, el tamaño del modelo importa más que la
rapidez. El trabajo visual va a Dirsi o al portátil; el agente del
teléfono queda para aprendizaje y ediciones rápidas de texto o código.

## 2026-10-21 — Kimi Work: 6 usos al mes no son un plan de trabajo
Hecho: el tier gratuito de Kimi Work permite unos 6 usos de agente al
mes. No alcanza para diseñar una página completa.
Lección: reservar herramientas de un solo uso para UNA pasada final,
sobre una copia del proyecto, con alcance muy acotado y revisión antes
de aceptar. Nunca como base del trabajo.

## 2026-10-22 — Block Ethos: la plantilla se veía por todas partes
Hechos: README de plantilla, páginas Demo/Single de ejemplo, artefactos
de build versionados, `render.yaml` llamado «sample-service-name»,
favicon de 4Geeks, `lang="en"` en una app en español, mojibake
(«tÃ­tulo») visible para el usuario, y dos manifiestos de dependencias
en conflicto (requirements de 2021 contra Pipfile moderno).
Lección: la fase 0 de cualquier rediseño es higiene — quitar restos de
plantilla, unificar dependencias, idioma y metadatos — antes de tocar
un solo color. Lo que el usuario ve primero (README, favicon, idioma)
pesa más que cualquier degradado.

## 2026-10-22 — Block Ethos: tres librerías de iconos a la vez
Hecho: Font Awesome por CDN, bootstrap-icons y lucide-react conviviendo
en la misma app.
Lección: un solo set de iconos por proyecto (principio 3). La mezcla
no solo pesa: hace que la interfaz parezca armada con piezas de otros
productos.

## 2026-10-22 — Block Ethos: 239 líneas de CSS sobre Bootstrap
Hecho: todo el «sistema de diseño» eran sobrescrituras de Bootstrap.
Se veía decente, pero era nivel plantilla: sin modo oscuro (raro en
web3), sin imágenes propias, componentes stock sin pulir.
Lección: sobrescribir un framework tiene techo. Un sistema propio con
tokens (`--bk-*`) cuesta un día y se nota en cada pantalla.

## 2026-10-22 — ModelBattle: lo bonito sin contenido no gana
Hechos: la versión A («bloquea») tenía el dashboard más limpio y
moderno, pero el contenido más delgado (sin quizzes ni certificados).
La B tenía el currículo más completo y el certificado, pero era la
menos distintiva visualmente. La C era la más pulida pero con secciones
marcador («PRONTO») y la más lenta sin ventaja de contenido.
Lección: ni la belleza sin fondo ni el fondo sin identidad ganan. El
plano ganador combina: currículo de B, laboratorio de D, simulador de
C, rachas de A y juego anti-phishing de B. Y: el código no verificado
no cuenta (el código de B nunca se pudo abrir).

## 2026-10-22 — ModelBattle: un laboratorio vale más que mil palabras
Hecho: lo mejor valorado de las 4 versiones fueron los laboratorios:
hash SHA-256 en vivo, cadena que se rompe al alterar un bloque,
calculadora de gas, Solidity real copiable con enlace a Remix.
Lección: en apps educativas, el interactivo es el diferenciador. Por
eso Block Ethos ganó su laboratorio (`/laboratorio`) en la fase 1 y por
eso el demo de barbería se define por su flujo, no por su landing.

## 2026-10-26 — Bug de render en el chat: array contra objeto
Hecho: al escribir el widget de chat de la barbería, las opciones de
respuesta llegaron como array donde el componente esperaba un objeto
(y al revés). Se detectó escribiendo el componente y se corrigió antes
del build.
Lección: fijar UNA forma para cada dato que cruza componentes y
validarla en el borde (el patrón 4 documenta la forma elegida). Los
bugs de forma se cazan renderizando, no leyendo el plan.

## 2026-10-26 — Una landing sola nunca es «listo»
Hecho: el criterio de terminado del demo de barbería se escribió antes
de construir: reserva completa, cancelación y hueco liberado. Sin ese
criterio, la landing sola habría parecido terminada.
Lección: escribir el criterio de «listo» como un flujo observable
antes de construir. Si no se puede probar con un clic, no está hecho.

## 2026-10-26 — El servidor de prueba que quedó en marcha
Hecho: tras verificar el demo de barbería, el servidor de pruebas
quedó corriendo en el puerto 5000 y bloqueó la verificación de la API
al día siguiente (mismo puerto). Se detuvo a mano.
Lección: toda verificación termina matando su servidor y comprobando
el puerto libre. El «después» forma parte de la verificación.

## 2026-11-16 — Flask sirve la plantilla vieja sin modo debug
Hecho: tras corregir el punto de estado de la interfaz del
rag-demo, la primera re-captura salió idéntica a la anterior:
Flask, sin modo debug, cachea la plantilla y seguía sirviendo la
versión vieja.
Lección: reiniciar el servidor antes de re-verificar cualquier
cambio de plantilla; si la re-captura sale idéntica, sospechar
de la caché antes que del arreglo.

## 2026-11-23 — Las citas de código con líneas caducan
Hecho: el portafolio cita un fragmento de `routes.py` de Block
Ethos en las líneas 666–680; el código sigue ahí, idéntico, pero
ahora está en las líneas 724–740 y el enlace apunta a otra función.
Lección: una cita con líneas es una foto con fecha: al publicar
un fragmento, citar también la función o el ancla que lo identifica
y re-verificar el rango en cada pasada. El texto citado puede
seguir siendo cierto mientras su puntero ya miente.

## 2026-11-23 — Los números de contraste se etiquetan por tema y fondo
Hecho: el comentario de contraste del portafolio listaba los pares
del tema oscuro (sobre papel y sobre superficie) sin etiquetarlos;
leídos como «claro/oscuro», cada cifra parecía del tema contrario.
La conclusión (todo ≥ 4,5:1) era cierta en ambos temas; las cifras,
mal atribuidas.
Lección: cada cifra de contraste lleva su tema y su fondo. Un número
sin etiqueta es una afirmación a medias, aunque el veredicto sea
correcto.
