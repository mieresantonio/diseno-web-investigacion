# Patrones de componentes reutilizables

Esqueletos cortos, no componentes terminados. Cada patrón indica de
qué app viene y qué no hay que olvidar.

## 1. Hero de landing
De: barbería, biblioteca, Segundo Yo.
```jsx
<header className="hero">
  <p className="eyebrow">PARA QUIÉN ES ESTO</p>
  <h1>Título en una frase, verbo primero</h1>
  <p className="subtitle">Una línea de beneficio, sin jerga.</p>
  <div className="hero-actions">
    <a className="btn primary" href="#accion">Empezar</a>
    <a className="btn secondary" href="#saber-mas">Saber más</a>
  </div>
</header>
```
No olvidar: `clamp()` en el `h1`, subtítulo con ancho máximo (~640–
720 px) para que no se estire, acciones que en móvil pasan a ancho
completo.

## 2. Tarjetas de servicios o precios
De: barbería.
```css
.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.card { background: var(--panel); border: 1px solid var(--line);
  border-radius: 14px; padding: 22px; transition: transform .15s, box-shadow .15s; }
.card:hover { transform: translateY(-3px); border-color: var(--accent); }
@media (max-width: 900px) { .cards { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 700px) { .cards { grid-template-columns: 1fr; } }
```
No olvidar: el precio grande va en el acento, el detalle en texto
atenuado; la elevación al hover es sutil (3 px), no un salto.

## 3. Agenda de día por profesional
De: barbería. El patrón más valioso del repo: una regla de negocio
visible (sin solapes, almuerzo bloqueado, día de descanso) convertida
en interfaz.
```jsx
<section>
  <input type="date" value={date} onChange={e => setDate(e.target.value)} />
  {professionals.map(p => (
    <div key={p.id}>
      <h3>{p.name}</h3>
      <div className="grid">
        {slots[p.id].map(s => (
          <button key={s.time} className={`cell ${s.state}`}
            disabled={s.state !== 'free'} onClick={() => pick(s)}>
            {s.time}
          </button>
        ))}
      </div>
    </div>
  ))}
</section>
```
Estados obligatorios: libre, ocupado, almuerzo (tachado), día cerrado.
La API devuelve solo huecos libres; el cliente nunca calcula la regla.

## 4. Widget de chat con opciones
De: barbería (panel fijo + FAB). Lección incorporada: las opciones de
respuesta deben tener una forma única y estable (ver `lecciones.md`).
```jsx
{open ? (
  <div className="chat-panel">
    <div className="chat-head"><span>Asistente</span><button onClick={close}>✕</button></div>
    <div className="chat-body">
      {messages.map((m, i) => (
        <div key={i} className={`msg ${m.from}`}>
          <p>{m.text}</p>
          {m.options && <div className="msg-opts">
            {m.options.map(o => <button key={o} onClick={() => send(o)}>{o}</button>)}
          </div>}
        </div>
      ))}
    </div>
    <form className="chat-input" onSubmit={submit}>
      <input value={text} onChange={e => setText(e.target.value)} placeholder="Escribe…" />
      <button>Enviar</button>
    </form>
  </div>
) : <button className="chat-fab" onClick={open}>💬</button>}
```
No olvidar: panel con `max-height: calc(100vh - 40px)` y ancho
`min(380px, calc(100vw - 32px))`; burbujas propias en acento, ajenas
en panel; foco visible en todos los botones.

## 5. Constructor con campos y vista previa en vivo
De: biblioteca de prompts (6 campos: acción, pasos, persona, contexto,
restricciones, plantilla).
```jsx
<div className="builder-grid">
  <div className="builder-fields">
    {FIELDS.map(f => (
      <label key={f.key}>{f.label}
        <textarea value={values[f.key]} onChange={e => set(f.key, e.target.value)} />
      </label>
    ))}
  </div>
  <aside className="builder-side">
    <h3>Resultado</h3>
    <pre className="assembled">{assembled}</pre>
    <button onClick={copy}>Copiar</button>
  </aside>
</div>
```
No olvidar: los campos vacíos se omiten en el ensamblado; el panel
lateral es `sticky` en escritorio y estático en móvil; copiar con
fallback si el portapapeles no está disponible.

## 6. Tarjeta resumen copiable (ficha)
De: Segundo Yo.
```jsx
<div className="card summary-card">
  <p className="card-label">TU FICHA</p>
  <p className="summary-text">{summary}</p>
  <button onClick={copy}>Copiar ficha</button>
</div>
```
No olvidar: el texto con `white-space: pre-line` para respetar los
saltos; fondo con degradado suave del acento hacia blanco; ejemplos
cargables en chips para empezar sin la página en blanco.

## 7. Explorador con buscador (glosario, catálogo)
De: Segundo Yo, biblioteca de prompts.
```jsx
<input className="search" value={q} onChange={e => setQ(e.target.value)}
  placeholder="Buscar…" />
<div className="cards">
  {filtered.length ? filtered.map(item => <article key={item.id} className="card">…</article>)
    : <p className="empty">Sin resultados. Prueba otra palabra.</p>}
</div>
```
No olvidar: el estado vacío es un diseño, no un hueco (borde
discontinuo, texto centrado); la búsqueda filtra por título y
descripción, no solo por título.

## 8. Formulario con estados de validación
De: barbería (reserva), biblioteca (añadir prompt).
```css
.form input, .form select { border: 1px solid var(--line); border-radius: 8px; padding: 11px 12px; }
.form input:focus, .form select:focus { border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(0, 0, 0, 0.12); outline: none; }
.btn:disabled { opacity: 0.5; cursor: not-allowed; }
.notice { border: 1px solid var(--accent); border-radius: 10px; padding: 12px 16px; }
```
No olvidar: etiqueta encima del campo, no solo placeholder; el botón
deshabilitado explica por qué (falta un campo); el aviso de error dice
qué hacer, no solo qué falló («ese hueco choca con el almuerzo»).

## 9. Favoritos con localStorage
De: biblioteca de prompts.
```js
const [favs, setFavs] = useState(() =>
  JSON.parse(localStorage.getItem('favs') || '[]'));
function toggleFav(id) {
  const next = favs.includes(id) ? favs.filter(f => f !== id) : [...favs, id];
  setFavs(next);
  localStorage.setItem('favs', JSON.stringify(next));
}
```
No olvidar: leer con `try/catch` o valor por defecto (el almacenamiento
puede fallar); el favorito es un corazón o estrella con estado
«on» en acento; ofrecer vista «solo favoritos».

## 10. Punto de estado + texto largo en flex
De: interfaz web del rag-demo (16 nov 2026).
```css
.estado { display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }
.punto { flex: none; width: 10px; height: 10px; border-radius: 50%;
  transform: translateY(1px); }
#estado-texto { flex: 1; min-width: 0; overflow-wrap: anywhere; }
```
No olvidar: sin `flex: 1; min-width: 0` en el texto, un texto largo
(nombre de modelo) empuja al punto a su propia línea en
pantallas estrechas: el span debe ocupar el ancho restante y
partirse, no saltar entero. El punto lleva `flex: none` para que
no se comprima y `translateY(1px)` para asentarse sobre la línea
base del texto.

## 11. Formulario deshabilitado entero cuando el servicio no está
De: interfaz web del rag-demo (16 nov 2026).
```js
// Rama "sin índice": el campo se deshabilita, no solo el botón.
campo.disabled = true;
// El botón además se apaga cuando el campo está vacío.
boton.disabled = !indiceListo || texto.length === 0;
```
```css
textarea:disabled { background: var(--elevado); color: var(--atenuado); }
button:disabled { opacity: 0.45; cursor: not-allowed; }
```
No olvidar: si solo se deshabilita el botón, el usuario escribe la
pregunta y se encuentra un botón muerto; el campo debe quedar
deshabilitado y con aspecto de tal (fondo distinto, texto atenuado).
La regla general: el estado de «no disponible» se aplica a todo el
formulario, no a su botón. Y el botón no debe parecer activo con el
campo vacío: se deshabilita también entonces, con el aviso visible
de por qué no se puede preguntar.

## 12. Lista de fuentes con evidencia (cita verificable)
De: interfaz web del rag-demo (16 nov 2026).
```css
.fuente { padding: 12px 0; border-top: 1px solid var(--borde); }
.fuente:first-of-type { border-top: 0; padding-top: 4px; }
.fuente-cabecera { display: flex; gap: 8px; flex-wrap: wrap; align-items: baseline; }
.fuente-sim { margin-left: auto; font-variant-numeric: tabular-nums; }
.fuente-texto { margin: 8px 0 0; color: var(--atenuado); white-space: pre-wrap; }
```
No olvidar: cada fuente lleva número, archivo y sección en la
cabecera y la similitud a la derecha con `margin-left: auto` y
`tabular-nums` para que las cifras no bailen; el fragmento va con
`pre-wrap` para respetar sus saltos; la primera fuente no lleva
borde superior (es el inicio de la lista, no una separación). Todo
contenido recuperado se escapa antes de inyectarlo con `innerHTML`:
el texto de una fuente nunca se confía tal cual.

## 13. Revelado al hacer scroll como mejora progresiva
De: portafolio (el mecanismo existe desde el rediseño del 7 nov 2026;
verificado en `portfolio/index.html`, 23 nov 2026).
```html
<!-- En <head>, antes del CSS: solo si hay JS la página se marca como tal -->
<script>document.documentElement.classList.add('js');</script>
```
```css
/* Sin JS no hay clase .js: el contenido se ve siempre. Con JS, oculto hasta revelar. */
.js .rev { opacity: 0; transform: translateY(10px); }
.js .rev.in { opacity: 1; transform: none;
  transition: opacity 500ms var(--ease), transform 500ms var(--ease);
  transition-delay: calc(var(--i, 0) * 40ms); }
@media (prefers-reduced-motion: reduce) {
  .js .rev { opacity: 1; transform: none; }
  .js .rev.in { transition: none; }
}
@media print { .js .rev { opacity: 1; transform: none; } }
```
```js
// Solo elementos fuera del hero; escalonado por grupo con --i.
var els = document.querySelectorAll('.rev');
if (!('IntersectionObserver' in window)) {
  els.forEach(function (el) { el.classList.add('in'); });
} else {
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.05 });
  els.forEach(function (el) { io.observe(el); });
}
// Red de seguridad: nada queda oculto si el observador no dispara.
setTimeout(function () {
  els.forEach(function (el) { el.classList.add('in'); });
}, 2500);
```
No olvidar: la puerta es la clase `.js` en `<html>` — sin JavaScript
no hay nada oculto que revelar, así que el contenido nunca depende
del script; la transición vive en `.in`, no en `.rev`: solo se anima
la entrada. El observador se da de baja (`unobserve`) tras revelar
cada elemento, y la red de seguridad de 2,5 s cubre el caso en que
no dispare (pestaña en segundo plano, elemento ya visible al cargar).
El hero no se revela: es lo primero que se ve, no necesita entrar.
El escalonado usa el token de desfase de 40 ms del sistema de vitrina
(§2) y la duración de 500 ms es su token de énfasis raro; el revelado
de contenido estándar es 400 ms.

## 14. Esqueleto de carga con la silueta exacta de la tarjeta real
De: Block Ethos, `PathCardSkeleton` + `.bk-skeleton` en `index.css`
(2ª tanda, 16 nov 2026; verificado en el clon de esta sesión).
```jsx
// Misma silueta que la tarjeta real (imagen de 160 px, badge, título,
// descripción y pie) para que la carga no mueva el layout.
// aria-hidden: el esqueleto no es contenido.
<div className="card h-100 overflow-hidden" aria-hidden="true">
  <div className="bk-skeleton bk-skeleton-img" />
  <div className="card-body d-flex flex-column">
    <div className="bk-skeleton mb-2" style={{ width: "92px", height: "20px" }} />
    <div className="bk-skeleton mb-2" style={{ width: "80%", height: "22px" }} />
    <div className="bk-skeleton mb-2" style={{ width: "100%", height: "14px" }} />
    <div className="bk-skeleton mb-3" style={{ width: "65%", height: "14px" }} />
    <div className="d-flex justify-content-between align-items-center mt-auto">
      <div className="bk-skeleton" style={{ width: "70px", height: "14px" }} />
      <div className="bk-skeleton" style={{ width: "96px", height: "31px", borderRadius: "50rem" }} />
    </div>
  </div>
</div>
```
```css
/* Brillo casi invisible (banda al 8 %, diseno_vitrina §3): panel de base. */
.bk-skeleton {
  background-color: var(--bk-panel-2);
  background-image: linear-gradient(100deg, transparent 40%,
    rgba(233, 238, 251, 0.08) 50%, transparent 60%);
  background-size: 200% 100%;
  animation: bk-shimmer 1.4s ease-in-out infinite;
  border-radius: 8px;
}
/* La imagen del esqueleto mide 160 px como la de la tarjeta real,
   sin radio (la tarjeta recorta con overflow). */
.bk-skeleton-img { height: 160px; border-radius: 0; }
@keyframes bk-shimmer {
  from { background-position: 120% 0; }
  to { background-position: -120% 0; }
}
@media (prefers-reduced-motion: reduce) { .bk-skeleton { animation: none; } }
```
No olvidar: la rejilla de esqueletos usa la misma distribución
responsive que la rejilla real (1 / 2 / 3 columnas) — si no, el
layout salta al llegar los datos aunque cada tarjeta mida igual;
cada banda del esqueleto reproduce una pieza real (badge, título,
líneas, pie) con sus medidas, no un rectángulo genérico; el brillo
es una banda móvil sobre el color de panel, no un cambio de fondo
entero; con movimiento reducido el esqueleto queda fijo, sin
animación. Instancia la receta «Esqueleto → contenido» de
`sistema-diseno-vitrina.md` §7 con números concretos (1,4 s,
banda al 8 %).

## 15. Error de carga humano con reintento
De: Block Ethos, `LoadError` + `BACKEND_DORMIDO` en
`src/front/components/LoadError.jsx`, usado en `Courses.jsx` y
`LearningPaths.jsx` (verificado 23 nov 2026).
```js
// Mensaje compartido: la causa real, en lenguaje humano, no el error técnico.
export const BACKEND_DORMIDO = {
  title: "El servidor está despertando",
  message: "Nuestro servidor duerme cuando nadie lo usa y tarda unos segundos en arrancar. Pulsa «Reintentar» y el contenido aparecerá."
};
```
```jsx
<div className="card border-0 shadow-sm p-4 text-center my-4" role="alert">
  {/* align-self-center: .card es flex-column en Bootstrap, así que
      text-center no centra el icono; sin esto quedaba a la izquierda. */}
  <span className="icon-chip align-self-center mb-3"><WifiOff size={22} /></span>
  <h5 className="fw-bold">{title}</h5>
  <p className="text-muted small mx-auto mb-3" style={{ maxWidth: "480px" }}>
    {message}
  </p>
  <button type="button" className="btn btn-primary rounded-pill px-4" onClick={onRetry}>
    Reintentar
  </button>
</div>
```
No olvidar: nunca mostrar el mensaje técnico crudo al visitante
(antes se veía literalmente «Failed to fetch» en inglés); el
detalle técnico va a la consola (`console.error` en quien llama),
donde lo ve quien desarrolla. El mensaje explica la causa en
lenguaje humano y dice qué hacer: reintentar. El botón de
reintento es obligatorio, no opcional: un error sin salida es un
callejón. `role="alert"` para que el lector de pantalla lo
anuncie; el texto con ancho máximo (~480 px) centrado para que no
se estire en pantallas anchas; el icono lleva `align-self-center`
porque `.card` es flex-column en Bootstrap y `text-center` no lo
centra. El mensaje se comparte como constante (`BACKEND_DORMIDO`):
la misma causa, el mismo texto en todas las pantallas.

## 16. Historial de sesión solo-DOM
De: interfaz web del rag-demo (verificado en
`templates/index.html`, 23 nov 2026).
```html
<section class="tarjeta" id="historial" aria-label="Historial de la sesión" hidden>
  <h2>Historial de la sesión</h2>
  <ol class="historial-lista" id="historial-lista"></ol>
  <p class="historial-nota">Solo vive en esta página: al recargar se
  borra. La más reciente queda arriba.</p>
</section>
```
```css
.historial-lista { margin: 0; padding: 0; list-style: none; }
.historial-entrada { display: flex; gap: 12px; flex-wrap: wrap;
  align-items: baseline; justify-content: space-between;
  padding: 10px 0; border-top: 1px solid var(--borde); font-size: 14px; }
.historial-entrada:first-child { border-top: 0; padding-top: 4px; }
.historial-pregunta { font-weight: 600; }
.historial-meta { color: var(--atenuado);
  font-variant-numeric: tabular-nums; white-space: nowrap; }
```
```js
function agregarHistorial(pregunta, confianza, similitudMaxima) {
  // Solo DOM, sin persistencia: al recargar la página se borra.
  // Se construye con nodos (textContent), nunca con innerHTML, para
  // que una pregunta con <script> no pueda inyectar nada.
  var entrada = document.createElement("li");
  entrada.className = "historial-entrada";
  var preguntaSpan = document.createElement("span");
  preguntaSpan.className = "historial-pregunta";
  preguntaSpan.textContent = pregunta;
  var metaSpan = document.createElement("span");
  metaSpan.className = "historial-meta";
  metaSpan.textContent =
    (confianza === "alta" ? "Confianza alta" : "Confianza baja") +
    " · sim. " + (typeof similitudMaxima === "number"
      ? similitudMaxima.toFixed(3) : "—");
  entrada.appendChild(preguntaSpan);
  entrada.appendChild(metaSpan);
  historialLista.insertBefore(entrada, historialLista.firstChild);
  // Tope de 20 entradas: la sesión no debe crecer sin límite.
  while (historialLista.children.length > 20) {
    historialLista.removeChild(historialLista.lastChild);
  }
  historial.hidden = false;
}
```
No olvidar: la sección nace oculta (`hidden`) y solo aparece con
la primera entrada — sin historial no hay tarjeta vacía; cada
entrada se construye con nodos y `textContent`, nunca con
`innerHTML`, para que una pregunta con `<script>` no pueda
inyectar nada; la más reciente queda arriba (`insertBefore(…,
firstChild)`); tope de 20 entradas, se descarta la más antigua;
la nota visible lo dice sin rodeos («Solo vive en esta página:
al recargar se borra»); la meta (confianza + similitud) va con
`tabular-nums` y `white-space: nowrap` para que las cifras no
bailen ni se partan. Si el historial debe sobrevivir a la
recarga, no es este patrón: es el 9 (persistencia local)
adaptado a entradas en vez de a favoritos.

## 17. Desglose de relevancia visible
De: interfaz web del rag-demo (verificado en
`templates/index.html`, 23 nov 2026).
```js
// Desglose del ranking híbrido: la relevancia (lo que ordena las
// fuentes) es la similitud semántica más la bonificación léxica.
// Sin el desglose, una fuente con similitud menor por encima de
// otra parecía un error de ordenación; con él, se ve el porqué.
function desgloseRelevancia(f) {
  var sim = (typeof f.similitud === "number")
    ? f.similitud.toFixed(3) : "—";
  if (typeof f.relevancia !== "number" ||
      typeof f.bonificacion_lexica !== "number") {
    return "sim. " + sim;
  }
  return "sim. " + sim + " + léx. " +
    f.bonificacion_lexica.toFixed(3) + " → relev. " +
    f.relevancia.toFixed(3);
}
```
Uso: en la cabecera de cada fuente (patrón 12), en el hueco de
`.fuente-sim`, sin añadir ninguna línea nueva:
```js
'<span class="fuente-sim">' + escapar(desgloseRelevancia(f)) + "</span>"
```
No olvidar: el desglose vive en el mismo hueco que la cifra
simple (`.fuente-sim`, a la derecha con `margin-left: auto` y
`tabular-nums`) — no añade una línea nueva a la cabecera; si la
API no trae los campos del desglose, cae a «sim. X» sin romperse
(los `typeof` antes de formatear); se escapa antes de inyectar,
como todo contenido recuperado (patrón 12). La regla general:
cuando el orden de una lista no se explica por la cifra que se
muestra, enseñar el desglose que lo ordena en vez de dejar que
parezca un error de ordenación.

## 18. Perfil público verificable
De: Block Ethos, `GET /api/profile/<handle>` y `PUT /profile/me` en
`src/api/routes.py`, página `/u/<handle>` en
`src/front/pages/PublicProfile.jsx` (verificado 23 nov 2026).
```py
# Dos columnas en users (models.py): handle único elegido por el
# estudiante y marca de opt-in, False por defecto. El handle es
# columna aparte del username a propósito: el registro nunca impuso
# unicidad de username, así que no sirve como identificador público.
public_handle: Mapped[str] = mapped_column(
    String(30), unique=True, nullable=True, index=True)
is_profile_public: Mapped[bool] = mapped_column(
    Boolean(), default=False, nullable=False)
```
```py
# La lectura pública: el mismo 404 para «no existe», «no es
# público» y «no es estudiante» — la respuesta no debe decir cuál
# de las tres es, para no convertir el endpoint en un oráculo.
@api.route('/profile/<string:handle>', methods=['GET'])
@rate_limit(max_attempts=30)
def get_public_profile(handle):
    user = db.session.execute(
        db.select(User).filter_by(
            public_handle=handle.strip().lower())
    ).scalars().one_or_none()
    if not user or not user.is_profile_public \
            or user.role != UserType.student:
        return jsonify({"error": "Perfil no encontrado"}), 404
    return jsonify(_perfil_publico_serialize(user)), 200
```
```py
# El serializador público es una lista cerrada: nombre, nivel, XP,
# antigüedad en mes (YYYY-MM, nunca la fecha exacta) y rutas con su
# avance y sus certificados. Sin correo, sin id interno, sin notas
# de quiz, sin rachas.
return {
    "handle": user.public_handle,
    "display_name": user.username or user.public_handle,
    "level_name": nombre_nivel,
    "xp": xp,
    "member_since": user.created_at.strftime("%Y-%m")
    if user.created_at else None,
    "paths": rutas,  # cada ruta: avance + certificado (código, fecha)
    "certificates_count": len(certs),
}
```
```jsx
// La página no deshace la ambigüedad del 404: el visitante lee que
// el perfil «puede que no exista o que su dueño lo tenga privado».
// Cada certificado enlaza a su verificación independiente.
<h3>Perfil no encontrado</h3>
<p>No hay ningún perfil público de Block Ethos con el handle
  @{handle}. Puede que no exista o que su dueño lo tenga privado.</p>
<Link to={`/verificar/${ruta.certificate.code}`}>
  {ruta.certificate.code}
</Link>
```
No olvidar: el 404 debe ser idéntico en los tres casos, mismo
estado y mismo cuerpo: hay un test que compara la respuesta JSON
de «privado» e «inexistente» y exige que sean iguales
(`tests/test_perfil_publico.py`). La página tampoco debe filtrar
el caso: si el backend es ambiguo pero la interfaz dice «este
usuario lo tiene privado», el oráculo vuelve por la pantalla.
El opt-in nace en falso: nada se ve hasta que el estudiante lo
activa, y al desactivarlo el perfil desaparece con el mismo 404.
Publicar exige handle primero (sin handle, 400); el handle se
valida (3–30 caracteres, minúsculas, sin palabras reservadas) y
el duplicado responde 409. El perfil es solo para estudiantes:
el admin recibe 403 al configurarlo y el endpoint público lo
trata como 404. La verificación no la afirma la propia página:
cada certificado enlaza a `/verificar/<código>`, donde
cualquiera lo comprueba por su cuenta. El rate limit es por IP
de cliente y exige ProxyFix detrás del proxy; sin él, todos los
visitantes comparten un cubo. Y cambiar el handle mueve la URL:
la vieja pasa a 404, así que hay que avisar al estudiante si ya
la enlazó desde su CV.

## 19. Sello «en vivo» con fecha en build-time
De: portafolio, sello en `index.html` (2ª tanda, 23 nov 2026;
verificado en `portfolio/index.html`, 23 nov 2026).
```html
<!-- La afirmación lleva su fecha: «verificada el», no «en vivo» a
     secas. datetime para la máquina, texto legible para la persona;
     data-dato marca el valor como dato vivo del portafolio. -->
<p class="live-seal"><span class="live-seal-dot" aria-hidden="true"></span>
  Demo en línea · verificada el
  <time datetime="2026-11-23" data-dato="be-en-vivo-fecha">23 nov 2026</time></p>
```
```css
/* Píldora con sombra-como-borde, solo tokens del sistema: sigue al
   modo oscuro sin una regla extra. El punto es estático, no parpadea. */
.live-seal{
  display:inline-flex; align-items:center; gap:8px; margin:16px 0 0;
  background:var(--paper); box-shadow:inset 0 0 0 1px var(--line);
  border-radius:999px; padding:6px 14px 6px 10px;
  font-size:.82rem; font-weight:500; color:var(--muted);
}
.live-seal-dot{ width:8px; height:8px; border-radius:50%; background:var(--ok); flex:none; }
.live-seal time{ font-family:var(--font-mono); font-size:.78rem; color:var(--faint); }
```
No olvidar: la fecha ES la afirmación: «verificada el 23 nov
2026» dice cuándo se comprobó la demo por última vez, no que
esté en vivo siempre; una fecha vieja es peor que no tener fecha,
porque demuestra que nadie ha vuelto a comprobarlo. La fecha se
fija en el momento de publicar (build-time), nunca la calcula el
navegador: ningún script de la página toca el sello. Al
actualizarla hay que cambiar juntos el `datetime` y el texto
visible: si discrepan, la máquina y la persona leen fechas
distintas. Hoy la fecha se escribe a mano en cada publicación:
el script `tools/actualizar-datos.py` no la cubre (su motor solo
reemplaza grupos de dígitos), así que es un paso manual de la
lista de publicación. El punto es decorativo (`aria-hidden`): el
texto lleva el significado. Y el sello va junto a la afirmación
que fecha — dentro de la tarjeta del proyecto, no en el pie.
