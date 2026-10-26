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
