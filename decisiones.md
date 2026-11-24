# Índice de decisiones

Cada decisión lleva su fecha, qué se descartó y su motivo, con
enlace a la fuente. Si una decisión no tiene fecha ni motivo
escrito, es un hábito: no entra.

Empieza con las 6 decisiones de arquitectura del caso de estudio
de Block Ethos, publicado el 23 nov 2026: el caso ya las deja
escritas con su porqué, así que este índice no investiga de cero,
las ordena y les pone fecha y alternativas. Cada app nueva añade
las suyas con la misma forma. Las decisiones no se borran: si una
deja de ser cierta, se corrige con fecha, como las lecciones.

Fuente general: [caso de estudio de Block
Ethos](https://github.com/mieresantonio/block-ethos/blob/main/docs/CASO-ESTUDIO.md#decisiones-de-arquitectura).
Los enlaces por decisión apuntan al commit `c52f86b` (23 nov
2026), el que creó el caso, para que las líneas no se muevan; las
citas de código vivo llevan su HEAD y su fecha de verificación.

## 1. Una app completa en un solo repositorio
Fecha: 6 ago 2026 (inicio del proyecto; viene de la plantilla).
De: Block Ethos.
Decisión: frontend React con Vite y backend Flask en el mismo
repositorio, desplegados como un solo servicio en PythonAnywhere
que sirve la API y el frontend compilado.
Descartado: el caso no nombra alternativas: la forma venía dada
por la plantilla react-flask de 4Geeks del proyecto final.
Motivo: un solo servicio que desplegar y mantener; la plantilla ya
traía esa forma y el proyecto la conservó.
Fuente: [caso de estudio,
L55-L61](https://github.com/mieresantonio/block-ethos/blob/c52f86b/docs/CASO-ESTUDIO.md#L55-L61);
el servicio único se ve en el código vivo: `src/app.py` sirve la
SPA compilada desde el mismo proceso (L117-L136, HEAD 6377d55,
verificado 23 nov 2026).

## 2. SQLite en producción, por decisión, no por defecto
Fecha: ago 2026, desde el inicio del proyecto (el caso no le pone
fecha propia; la documenta como decisión explícita al publicarse,
el 23 nov 2026).
De: Block Ethos.
Decisión: SQLite en producción y desarrollo, accedida siempre a
través de SQLAlchemy 2 con migraciones Alembic.
Descartado: un servidor de base de datos. El caso lo nombra tal
cual («SQLite en vez de un servidor de base de datos»); el repo
aún guarda esa alternativa en su configuración de Render
(`render.yaml`: base PostgreSQL).
Motivo: con un solo proceso, SQLite elimina una pieza de
infraestructura sin coste real; el día que el volumen lo pida, el
cambio es la URL de conexión, no el código.
Fuente: [caso de estudio,
L63-L71](https://github.com/mieresantonio/block-ethos/blob/c52f86b/docs/CASO-ESTUDIO.md#L63-L71)
y [«Decisiones con criterio de
coste»](https://github.com/mieresantonio/block-ethos/blob/c52f86b/docs/CASO-ESTUDIO.md#L261-L263);
en el código vivo: `src/app.py` L62-L67 (URL de entorno o SQLite
de reserva) y `render.yaml` L24-L30 (PostgreSQL en Render), HEAD
6377d55, verificado 23 nov 2026.

## 3. El tutor no usa ningún modelo de lenguaje
Fecha: 2 nov 2026 (tutor integrado); el caché del índice, 23 nov
2026.
De: Block Ethos.
Decisión: el tutor (`POST /api/tutor`) responde con búsqueda
TF-IDF escrita con solo la librería estándar de Python sobre los
fragmentos de las lecciones; respuesta extractiva que cita la
lección de origen, y si ningún fragmento supera el umbral (0,08)
lo dice en vez de inventar.
Descartado: un modelo de lenguaje externo (una API de pago). El
caso lo nombra tal cual («TF-IDF sin dependencias en vez de un
modelo externo»).
Motivo: sin servicios externos, sin claves de API, sin coste por
pregunta; y una respuesta extractiva con cita no puede inventar
contenido del curso.
Fuente: [caso de estudio,
L73-L89](https://github.com/mieresantonio/block-ethos/blob/c52f86b/docs/CASO-ESTUDIO.md#L73-L89);
en el código vivo: `src/api/routes.py` L1187 (comentario TF-IDF,
solo estándar), L1210 (umbral 0,08) y L1289-L1298 (índice
cacheado), HEAD 6377d55, verificado 23 nov 2026.

## 4. Rate limiting sin dependencias
Fecha: 16 nov 2026; la corrección ProxyFix, 23 nov 2026.
De: Block Ethos.
Decisión: el limitador de autenticación es memoria del proceso
con ventana deslizante por (IP, endpoint): 10 logins y 5
registros/recuperaciones por minuto, con 429 JSON y cabecera
`Retry-After`.
Descartado: Redis o un servicio externo de rate limiting. El caso
lo nombra tal cual («Sin Redis ni servicios»).
Motivo: en PythonAnywhere corre un solo proceso, así que el estado
en memoria basta; el propio código documenta ese límite.
Fuente: [caso de estudio,
L91-L98](https://github.com/mieresantonio/block-ethos/blob/c52f86b/docs/CASO-ESTUDIO.md#L91-L98);
en el código vivo: `src/api/rate_limit.py` L1-L27 (docstring: solo
librería estándar, límites conocidos), HEAD 6377d55, verificado
23 nov 2026.

## 5. Certificados verificables, no PDFs decorativos
Fecha: 23 oct 2026 (certificados); la unicidad en la base de
datos, 16 nov 2026.
De: Block Ethos.
Decisión: al completar una ruta al 100% con todos los quizzes
aprobados (≥ 70%), el estudiante reclama un certificado con
código único `BK-XXXXX-XXXXX-XXXXX`, comprobable por cualquiera
en `/verificar/:code`, sin cuenta.
Descartado: un PDF decorativo sin verificación; y la unicidad
garantizada solo en el código de la aplicación, sin la base de
datos.
Motivo: un certificado que cualquiera puede comprobar tiene valor;
uno bonito que no se verifica, no. La unicidad en la base de datos
es la que no se puede saltar.
Fuente: [caso de estudio,
L100-L105](https://github.com/mieresantonio/block-ethos/blob/c52f86b/docs/CASO-ESTUDIO.md#L100-L105);
en el código vivo: `src/api/models.py` L141-L142 (código
`unique=True`), HEAD 6377d55, verificado 23 nov 2026.

## 6. Gamificación sobre el progreso real
Fecha: 23 oct 2026.
De: Block Ethos.
Decisión: XP (100 por lección completada, más los puntos de los
quizzes), 6 niveles (Explorador → Arquitecto Web3) y rachas de
días consecutivos, todo derivado del progreso ya registrado, sin
tablas nuevas. La fecha de finalización de cada lección se sella
solo la primera vez que se completa.
Descartado: puntos decorativos, sin atar al progreso registrado:
es el contraste que marca el propio título («sobre el progreso
real»).
Motivo: la XP y las rachas valen porque miden lo hecho de verdad;
sin la fecha sellada una sola vez, las rachas no serían fiables.
Fuente: [caso de estudio,
L107-L112](https://github.com/mieresantonio/block-ethos/blob/c52f86b/docs/CASO-ESTUDIO.md#L107-L112);
en el código vivo: `src/api/routes.py` L814-L815 (la XP y las
rachas se derivan del progreso guardado), L792-L793 (la fecha se
sella solo la primera vez) y L822-L829 (los 6 niveles), HEAD
6377d55, verificado 23 nov 2026.
