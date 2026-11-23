#!/usr/bin/env python3
"""Verificador de coherencia de diseno-web-investigacion.

Comprueba en un comando los invariantes que hasta ahora se
revisaban a mano en cada tanda, y — lo que lo hace distinto de un
linter de Markdown — verifica que los patrones documentados se
cumplen de verdad en los artefactos reales que los originaron:
la plantilla de la interfaz web del rag-demo, el portafolio y
Block Ethos. 18 comprobaciones en total: 8 de coherencia interna
y 10 contra los artefactos.

Uso:
    python3 verificar.py            # todo; las comprobaciones de
                                    # artefacto se saltan (SKIP) si
                                    # no se encuentra el artefacto
    RAG_DEMO_DIR=/ruta/al/rag-demo python3 verificar.py
    PORTFOLIO_DIR=/ruta/al/portfolio python3 verificar.py
    BLOCK_ETHOS_DIR=/ruta/a/block-ethos python3 verificar.py

Cada artefacto se busca en su variable de entorno o, si no está
definida, en el directorio hermano de los clones de trabajo
(`../rag-demo-asistente-documentos` o `../rag-demo`,
`../portfolio`, `../block-ethos`). Sin el artefacto, sus
comprobaciones se informan como SKIP, no como fallo: el cuaderno
no depende de tener los artefactos al lado.

Salida: una línea OK/FAIL/SKIP por comprobación y un resumen.
Código de salida 0 si todo lo ejecutado pasa; 1 si algo falla.
Sin dependencias y sin escribir nada; solo toca la red para la
comprobación de enlaces (con timeout corto; sin red, SKIP).
"""

import os
import re
import sys
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
OK, FAIL, SKIP = "OK", "FAIL", "SKIP"

resultados = []


def registrar(nombre, estado, detalle=""):
    resultados.append((nombre, estado, detalle))
    linea = f"[{estado}] {nombre}"
    if detalle:
        linea += f" — {detalle}"
    print(linea)


def leer(rel):
    return (RAIZ / rel).read_text(encoding="utf-8")


# ---------------------------------------------------------------- coherencia

def check_patrones_readme():
    """Nº de patrones en patrones.md == nombres listados en el README."""
    patrones = leer("patrones.md")
    n_patrones = len(re.findall(r"^## \d+\. ", patrones, re.M))
    readme = leer("README.md")
    m = re.search(
        r"- `patrones\.md` — Patrones de componentes reutilizables con "
        r"esqueletos\n  de código: ([^\n]+(?:\n  [^\n-]+)*)",
        readme,
    )
    if not m:
        registrar("patrones-readme", FAIL, "no se encontró la lista en el README")
        return
    nombres = [n.strip() for n in m.group(1).replace("\n  ", " ").split(",")]
    nombres = [n for n in nombres if n]
    if n_patrones == len(nombres):
        registrar("patrones-readme", OK, f"{n_patrones} patrones, {len(nombres)} en el README")
    else:
        registrar("patrones-readme", FAIL,
                  f"patrones.md tiene {n_patrones}, el README lista {len(nombres)}")


def check_contenido_readme():
    """Todos los .md de la raíz aparecen en Contenido del README."""
    readme = leer("README.md")
    faltan = [p.name for p in sorted(RAIZ.glob("*.md"))
              if p.name != "README.md" and p.name not in readme]
    if "capturas/" not in readme:
        faltan.append("capturas/")
    if not faltan:
        registrar("contenido-readme", OK, "todos los archivos listados")
    else:
        registrar("contenido-readme", FAIL, "faltan en Contenido: " + ", ".join(faltan))


def check_log_cronologico():
    """Las entradas de log.md van en orden cronológico (no decreciente)."""
    fechas = re.findall(r"^## (\d{4}-\d{2}-\d{2})", leer("log.md"), re.M)
    if fechas == sorted(fechas):
        registrar("log-cronologico", OK, f"{len(fechas)} entradas en orden")
    else:
        registrar("log-cronologico", FAIL, f"fuera de orden: {fechas}")


def check_blockali_solo_historico():
    """«Blockali» aparece solo en la nota histórica del README."""
    apariciones = []
    for p in sorted(RAIZ.rglob("*.md")):
        for i, linea in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if "Blockali" in linea:
                apariciones.append((str(p.relative_to(RAIZ)), i, linea.strip()))
    readme = leer("README.md")
    nota = "Nota de nombre" in readme
    solo_en_readme = all(rel == "README.md" for rel, _, _ in apariciones)
    if len(apariciones) == 1 and solo_en_readme and nota:
        registrar("blockali-solo-historico", OK, "solo la nota histórica del README")
    else:
        registrar("blockali-solo-historico", FAIL,
                  f"apariciones: {apariciones} (nota histórica presente: {nota})")


def check_cercas_y_llaves():
    """Cercas de código balanceadas y llaves equilibradas en bloques css/js."""
    problemas = []
    for p in sorted(RAIZ.rglob("*.md")):
        texto = p.read_text(encoding="utf-8")
        if texto.count("```") % 2:
            problemas.append(f"{p.relative_to(RAIZ)}: cercas impares")
        for m in re.finditer(r"```(css|js)\n(.*?)```", texto, re.S):
            bloque = m.group(2)
            if bloque.count("{") != bloque.count("}"):
                problemas.append(
                    f"{p.relative_to(RAIZ)}: llaves {bloque.count('{')} vs "
                    f"{bloque.count('}')} en bloque {m.group(1)}")
    if not problemas:
        registrar("cercas-y-llaves", OK, "cercas pares, llaves equilibradas")
    else:
        registrar("cercas-y-llaves", FAIL, "; ".join(problemas))


def check_sistemas_tabla():
    """Cada sistema de sistemas.md tiene fila en «Cuándo usar cada uno»."""
    texto = leer("sistemas.md")
    n_sistemas = len(re.findall(r"^## \d+\. ", texto, re.M))
    tabla = texto.split("## Cuándo usar cada uno", 1)[1]
    filas = [l for l in tabla.splitlines()
             if l.startswith("|") and "---" not in l and "Sistema" not in l]
    if len(filas) == n_sistemas:
        registrar("sistemas-tabla", OK, f"{n_sistemas} sistemas, {len(filas)} filas")
    else:
        registrar("sistemas-tabla", FAIL,
                  f"{n_sistemas} sistemas, {len(filas)} filas en la tabla")


def check_capturas_indice():
    """Cada PNG de capturas/ está en el índice y cada PNG del índice existe."""
    indice = leer("capturas/README.md")
    en_disco = {p.name for p in (RAIZ / "capturas").glob("*.png")}
    en_indice = set(re.findall(r"`(rag-[a-z0-9-]+\.png)`", indice))
    problemas = []
    for nombre in sorted(en_disco - en_indice):
        problemas.append(f"{nombre} sin indexar")
    for nombre in sorted(en_indice - en_disco):
        problemas.append(f"{nombre} indexado pero ausente")
    for p in sorted((RAIZ / "capturas").glob("*.png")):
        if p.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
            problemas.append(f"{p.name} no es un PNG válido")
    if not problemas:
        registrar("capturas-indice", OK, f"{len(en_disco)} PNG indexadas y válidas")
    else:
        registrar("capturas-indice", FAIL, "; ".join(problemas))


def check_enlaces():
    """Los enlaces externos del repo devuelven 200 (sin red: SKIP)."""
    urls = set()
    for p in sorted(RAIZ.rglob("*.md")):
        urls.update(re.findall(r"https?://[^\s\)\"'<>`]+", p.read_text(encoding="utf-8")))
    urls = sorted(u.rstrip(".,") for u in urls)
    fallos, saltos = [], []
    for url in urls:
        try:
            req = urllib.request.Request(url, method="HEAD",
                                         headers={"User-Agent": "verificar.py"})
            with urllib.request.urlopen(req, timeout=8) as r:
                if r.status != 200:
                    fallos.append(f"{url} → {r.status}")
        except Exception as e:  # noqa: BLE001 - sin red o bloqueo: SKIP honesto
            saltos.append(f"{url} ({type(e).__name__})")
    if fallos:
        registrar("enlaces", FAIL, "; ".join(fallos))
    elif saltos and len(saltos) == len(urls):
        registrar("enlaces", SKIP, "sin acceso a la red: " + "; ".join(saltos))
    else:
        detalle = f"{len(urls) - len(saltos)}/{len(urls)} con 200"
        if saltos:
            detalle += "; sin comprobar: " + "; ".join(saltos)
        registrar("enlaces", OK, detalle)


# ---------------------------------------------------------------- artefacto

def localizar_rag_demo():
    """Devuelve la plantilla del rag-demo o None si no se encuentra."""
    candidatos = []
    if os.environ.get("RAG_DEMO_DIR"):
        candidatos.append(Path(os.environ["RAG_DEMO_DIR"]))
    candidatos += [RAIZ.parent / "rag-demo-asistente-documentos",
                   RAIZ.parent / "rag-demo"]
    for base in candidatos:
        plantilla = base / "templates" / "index.html"
        if plantilla.is_file():
            return plantilla
    return None


def localizar_portfolio():
    """Devuelve el index.html del portafolio o None si no se encuentra."""
    candidatos = []
    if os.environ.get("PORTFOLIO_DIR"):
        candidatos.append(Path(os.environ["PORTFOLIO_DIR"]))
    candidatos.append(RAIZ.parent / "portfolio")
    for base in candidatos:
        indice = base / "index.html"
        if indice.is_file():
            return indice
    return None


def localizar_block_ethos():
    """Devuelve la raíz de Block Ethos o None si no se encuentra."""
    candidatos = []
    if os.environ.get("BLOCK_ETHOS_DIR"):
        candidatos.append(Path(os.environ["BLOCK_ETHOS_DIR"]))
    candidatos.append(RAIZ.parent / "block-ethos")
    for base in candidatos:
        if (base / "src" / "front" / "index.css").is_file():
            return base
    return None


def bloque_css(texto, selector):
    """El contenido de la primera regla `selector { ... }` (sin anidar)."""
    m = re.search(re.escape(selector) + r"\s*\{(.*?)\}", texto, re.S)
    return m.group(1) if m else None


def bloques_anidados(texto, cabecera):
    """El contenido de cada bloque `cabecera { ... }`, con llaves
    anidadas contadas (para @media y funciones, donde bloque_css
    se detendría en la primera llave interior)."""
    bloques = []
    inicio = 0
    while True:
        i = texto.find(cabecera, inicio)
        if i < 0:
            return bloques
        j = texto.find("{", i)
        if j < 0:
            return bloques
        profundidad = 0
        for k in range(j, len(texto)):
            if texto[k] == "{":
                profundidad += 1
            elif texto[k] == "}":
                profundidad -= 1
                if profundidad == 0:
                    bloques.append(texto[j + 1:k])
                    inicio = k + 1
                    break
        else:
            return bloques


def check_artefacto(nombre, plantilla, comprobaciones):
    """Cada comprobación: (etiqueta, texto_que_debe_existir) o
    (etiqueta, selector_css, [declaraciones que debe contener])."""
    texto = plantilla.read_text(encoding="utf-8")
    faltan = []
    for comp in comprobaciones:
        if len(comp) == 2:
            etiqueta, literal = comp
            if literal not in texto:
                faltan.append(etiqueta)
        else:
            etiqueta, selector, declaraciones = comp
            bloque = bloque_css(texto, selector)
            if bloque is None:
                faltan.append(f"{etiqueta} (sin regla {selector})")
            else:
                for d in declaraciones:
                    if d not in bloque:
                        faltan.append(f"{etiqueta}: falta «{d}»")
    if not faltan:
        registrar(nombre, OK, f"{len(comprobaciones)} comprobaciones contra {plantilla}")
    else:
        registrar(nombre, FAIL, "; ".join(faltan))


def check_patron_10(plantilla):
    check_artefacto("patron-10-artefacto", plantilla, [
        ("estado", ".estado",
         ["display: flex", "align-items: baseline", "gap: 8px", "flex-wrap: wrap"]),
        ("punto", ".punto",
         ["flex: none", "width: 10px", "height: 10px", "border-radius: 50%",
          "transform: translateY(1px)"]),
        ("estado-texto", "#estado-texto",
         ["flex: 1", "min-width: 0", "overflow-wrap: anywhere"]),
    ])


def check_patron_11(plantilla):
    check_artefacto("patron-11-artefacto", plantilla, [
        ("campo-deshabilitado", "campo.disabled = true;"),
        ("boton-deshabilitado", "boton.disabled = !indiceListo || texto.length === 0;"),
        ("textarea-disabled",
         "textarea:disabled { background: var(--elevado); color: var(--atenuado); }"),
        ("button-disabled", "button:disabled { opacity: 0.45; cursor: not-allowed; }"),
    ])


def check_patron_12(plantilla):
    check_artefacto("patron-12-artefacto", plantilla, [
        ("fuente", ".fuente", ["padding: 12px 0", "border-top: 1px solid var(--borde)"]),
        ("fuente-cabecera", ".fuente-cabecera",
         ["display: flex", "gap: 8px", "flex-wrap: wrap", "align-items: baseline"]),
        ("fuente-sim", ".fuente-sim", ["margin-left: auto",
                                       "font-variant-numeric: tabular-nums"]),
        ("fuente-texto", ".fuente-texto", ["margin: 8px 0 0", "white-space: pre-wrap"]),
        ("escapa-numero", "escapar(f.n)"),
        ("escapa-archivo", "escapar(f.archivo)"),
        ("escapa-seccion", "escapar(f.seccion)"),
        ("escapa-fragmento", "escapar(f.fragmento)"),
    ])


def tokens_de(bloque):
    return dict(re.findall(r"(--[\w-]+):\s*([^;]+);", bloque))


def check_sistema_rag_tokens(plantilla):
    """Los 16 tokens del sistema nº 5 coinciden con el :root real."""
    sistemas = leer("sistemas.md")
    seccion5 = sistemas.split("## 5. ", 1)[1].split("## Cuándo usar", 1)[0]
    m = re.search(r"```css\n(.*?)```", seccion5, re.S)
    doc = tokens_de(m.group(1)) if m else {}
    texto = plantilla.read_text(encoding="utf-8")
    raiz_real = tokens_de(bloque_css(texto, ":root") or "")
    diferencias = [f"{k}: doc {doc.get(k)} vs real {raiz_real.get(k)}"
                   for k in sorted(set(doc) | set(raiz_real))
                   if doc.get(k) != raiz_real.get(k)]
    if not diferencias and doc:
        registrar("sistema-rag-tokens", OK, f"{len(doc)} tokens idénticos al :root real")
    else:
        registrar("sistema-rag-tokens", FAIL, "; ".join(diferencias or ["sin tokens"]))


def check_sistema_block_ethos_tokens(css):
    """Los 15 tokens --bk-* del sistema nº 1 coinciden con el :root real.
    Las variables --bs-* de re-tematizado de Bootstrap no entran: son
    derivadas, no tokens del sistema."""
    sistemas = leer("sistemas.md")
    seccion1 = sistemas.split("## 1. ", 1)[1].split("## 2. ", 1)[0]
    m = re.search(r"```css\n(.*?)```", seccion1, re.S)
    doc = {k: v for k, v in tokens_de(m.group(1)).items()
           if k.startswith("--bk-")} if m else {}
    texto = css.read_text(encoding="utf-8")
    raiz_real = {k: v for k, v in tokens_de(bloque_css(texto, ":root") or "").items()
                 if k.startswith("--bk-")}
    diferencias = [f"{k}: doc {doc.get(k)} vs real {raiz_real.get(k)}"
                   for k in sorted(set(doc) | set(raiz_real))
                   if doc.get(k) != raiz_real.get(k)]
    if not diferencias and len(doc) == 15:
        registrar("sistema-block-ethos-tokens", OK,
                  f"{len(doc)} tokens idénticos al :root real")
    else:
        registrar("sistema-block-ethos-tokens", FAIL,
                  "; ".join(diferencias or ["sin tokens"]))


def check_patron_13(indice):
    """El patrón 13 (revelado por scroll) se cumple en el portafolio."""
    texto = indice.read_text(encoding="utf-8")
    faltan = []
    for etiqueta, literal in [
        ("puerta-js", "document.documentElement.classList.add('js');"),
        ("rev-oculto", ".js .rev { opacity: 0; transform: translateY(10px); }"),
        ("observador", "IntersectionObserver"),
        ("unobserve", "io.unobserve(e.target);"),
        ("red-seguridad", "}, 2500);"),
    ]:
        if literal not in texto:
            faltan.append(etiqueta)
    visible = ".js .rev { opacity: 1; transform: none; }"
    for etiqueta, cabecera in [
        ("movimiento-reducido", "@media (prefers-reduced-motion: reduce)"),
        ("impresion", "@media print"),
    ]:
        bloques = bloques_anidados(texto, cabecera)
        if not bloques:
            faltan.append(f"{etiqueta} (sin bloque {cabecera})")
        elif not any(visible in b for b in bloques):
            faltan.append(f"{etiqueta}: falta «{visible}»")
    if not faltan:
        registrar("patron-13-artefacto", OK, f"7 comprobaciones contra {indice}")
    else:
        registrar("patron-13-artefacto", FAIL, "; ".join(faltan))


def check_patron_14(base):
    """El patrón 14 (esqueleto con la silueta real) se cumple en Block Ethos."""
    faltan = []
    jsx = base / "src" / "front" / "components" / "PathCardSkeleton.jsx"
    if not jsx.is_file():
        faltan.append("falta PathCardSkeleton.jsx")
        texto_jsx = ""
    else:
        texto_jsx = jsx.read_text(encoding="utf-8")
    for etiqueta, literal in [
        ("aria-hidden", 'aria-hidden="true"'),
        ("skeleton-img", "bk-skeleton-img"),
        ("rejilla", "col-12 col-md-6 col-lg-4"),
    ]:
        if literal not in texto_jsx:
            faltan.append(f"PathCardSkeleton.jsx: {etiqueta}")
    css = base / "src" / "front" / "index.css"
    texto_css = css.read_text(encoding="utf-8") if css.is_file() else ""
    esqueleto = bloque_css(texto_css, ".bk-skeleton")
    if esqueleto is None:
        faltan.append("sin regla .bk-skeleton")
    else:
        for d in ["background-color: var(--bk-panel-2);",
                  "rgba(233, 238, 251, 0.08)",
                  "animation: bk-shimmer 1.4s ease-in-out infinite;"]:
            if d not in esqueleto:
                faltan.append(f".bk-skeleton: falta «{d}»")
    imagen = bloque_css(texto_css, ".bk-skeleton-img")
    if imagen is None:
        faltan.append("sin regla .bk-skeleton-img")
    elif "height: 160px;" not in imagen:
        faltan.append(".bk-skeleton-img: falta «height: 160px;»")
    if not faltan:
        registrar("patron-14-artefacto", OK, "7 comprobaciones contra Block Ethos")
    else:
        registrar("patron-14-artefacto", FAIL, "; ".join(faltan))


def check_patron_15(base):
    """El patrón 15 (error humano con reintento) se cumple en Block Ethos."""
    faltan = []
    load_error = base / "src" / "front" / "components" / "LoadError.jsx"
    if not load_error.is_file():
        faltan.append("falta LoadError.jsx")
        texto_le = ""
    else:
        texto_le = load_error.read_text(encoding="utf-8")
    for etiqueta, literal in [
        ("constante", "BACKEND_DORMIDO"),
        ("titulo", 'title: "El servidor está despertando"'),
        ("role-alert", 'role="alert"'),
        ("centrado-icono", "align-self-center"),
        ("onretry", "onRetry: PropTypes.func.isRequired"),
    ]:
        if literal not in texto_le:
            faltan.append(f"LoadError.jsx: {etiqueta}")
    for rel in ["src/front/pages/Courses.jsx",
                "src/front/components/LearningPaths.jsx"]:
        ruta = base / rel
        if not ruta.is_file():
            faltan.append(f"falta {rel}")
            continue
        texto = ruta.read_text(encoding="utf-8")
        for etiqueta, literal in [
            ("import", "import { LoadError, BACKEND_DORMIDO }"),
            ("console-error", 'console.error("No se pudieron cargar las rutas:", err)'),
            ("titulo-uso", "title={BACKEND_DORMIDO.title}"),
        ]:
            if literal not in texto:
                faltan.append(f"{rel}: {etiqueta}")
    if not faltan:
        registrar("patron-15-artefacto", OK, "11 comprobaciones contra Block Ethos")
    else:
        registrar("patron-15-artefacto", FAIL, "; ".join(faltan))


def check_patron_16(plantilla):
    """El patrón 16 (historial de sesión solo-DOM) se cumple en el rag-demo."""
    texto = plantilla.read_text(encoding="utf-8")
    faltan = []
    for etiqueta, literal in [
        ("funcion", "function agregarHistorial(pregunta, confianza, similitudMaxima)"),
        ("crea-li", 'document.createElement("li")'),
        ("pregunta-texto", "preguntaSpan.textContent = pregunta;"),
        ("mas-reciente-arriba",
         "historialLista.insertBefore(entrada, historialLista.firstChild);"),
        ("tope-20", "while (historialLista.children.length > 20) {"),
        ("muestra-seccion", "historial.hidden = false;"),
        ("nota-visible", "Solo vive en esta página: al recargar se"),
        ("regla-entrada", ".historial-entrada {"),
        ("regla-meta", ".historial-meta {"),
        ("seccion", 'id="historial" aria-label="Historial de la sesión" hidden'),
    ]:
        if literal not in texto:
            faltan.append(etiqueta)
    cuerpos = bloques_anidados(
        texto, "function agregarHistorial(pregunta, confianza, similitudMaxima)")
    if cuerpos and "innerHTML" in cuerpos[0]:
        faltan.append("innerHTML dentro de agregarHistorial (debe construir con nodos)")
    if not faltan:
        registrar("patron-16-artefacto", OK, f"11 comprobaciones contra {plantilla}")
    else:
        registrar("patron-16-artefacto", FAIL, "; ".join(faltan))


def check_patron_17(plantilla):
    check_artefacto("patron-17-artefacto", plantilla, [
        ("funcion", "function desgloseRelevancia(f) {"),
        ("caida-sim", 'return "sim. " + sim;'),
        ("formato-desglose", '"sim. " + sim + " + léx. "'),
        ("formato-relevancia", "→ relev. "),
        ("uso-escapado", "escapar(desgloseRelevancia(f))"),
    ])


def main():
    check_patrones_readme()
    check_contenido_readme()
    check_log_cronologico()
    check_blockali_solo_historico()
    check_cercas_y_llaves()
    check_sistemas_tabla()
    check_capturas_indice()
    check_enlaces()
    plantilla = localizar_rag_demo()
    artefacto_rag = [("patron-10-artefacto", check_patron_10),
                     ("patron-11-artefacto", check_patron_11),
                     ("patron-12-artefacto", check_patron_12),
                     ("sistema-rag-tokens", check_sistema_rag_tokens),
                     ("patron-16-artefacto", check_patron_16),
                     ("patron-17-artefacto", check_patron_17)]
    if plantilla is None:
        for nombre, _ in artefacto_rag:
            registrar(nombre, SKIP, "rag-demo no encontrado (define RAG_DEMO_DIR)")
    else:
        for _, fn in artefacto_rag:
            fn(plantilla)
    indice = localizar_portfolio()
    if indice is None:
        registrar("patron-13-artefacto", SKIP,
                  "portafolio no encontrado (define PORTFOLIO_DIR)")
    else:
        check_patron_13(indice)
    base_be = localizar_block_ethos()
    if base_be is None:
        for nombre in ["sistema-block-ethos-tokens", "patron-14-artefacto",
                       "patron-15-artefacto"]:
            registrar(nombre, SKIP, "Block Ethos no encontrado (define BLOCK_ETHOS_DIR)")
    else:
        check_sistema_block_ethos_tokens(base_be / "src" / "front" / "index.css")
        check_patron_14(base_be)
        check_patron_15(base_be)
    n_ok = sum(1 for _, e, _ in resultados if e == OK)
    n_fail = sum(1 for _, e, _ in resultados if e == FAIL)
    n_skip = sum(1 for _, e, _ in resultados if e == SKIP)
    print(f"\n{n_ok} OK, {n_fail} FAIL, {n_skip} SKIP ({len(resultados)} comprobaciones)")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
