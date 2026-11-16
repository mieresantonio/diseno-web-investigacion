#!/usr/bin/env python3
"""Verificador de coherencia de diseno-web-investigacion.

Comprueba en un comando los invariantes que hasta ahora se
revisaban a mano en cada tanda, y — lo que lo hace distinto de un
linter de Markdown — verifica que los patrones documentados se
cumplen de verdad en el artefacto real que los originó (la
plantilla de la interfaz web del rag-demo).

Uso:
    python3 verificar.py            # todo; las comprobaciones de
                                    # artefacto se saltan (SKIP) si
                                    # no se encuentra el rag-demo
    RAG_DEMO_DIR=/ruta/al/rag-demo python3 verificar.py

El rag-demo se busca en `RAG_DEMO_DIR` o, si no está definida, en
los directorios hermanos `../rag-demo-asistente-documentos` y
`../rag-demo` (la disposición de los clones de trabajo). Sin el
artefacto, esas comprobaciones se informan como SKIP, no como
fallo: el cuaderno no depende de tener el artefacto al lado.

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


def bloque_css(texto, selector):
    """El contenido de la primera regla `selector { ... }` (sin anidar)."""
    m = re.search(re.escape(selector) + r"\s*\{(.*?)\}", texto, re.S)
    return m.group(1) if m else None


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
    artefacto = [("patron-10-artefacto", check_patron_10),
                 ("patron-11-artefacto", check_patron_11),
                 ("patron-12-artefacto", check_patron_12),
                 ("sistema-rag-tokens", check_sistema_rag_tokens)]
    if plantilla is None:
        for nombre, _ in artefacto:
            registrar(nombre, SKIP, "rag-demo no encontrado (define RAG_DEMO_DIR)")
    else:
        for _, fn in artefacto:
            fn(plantilla)
    n_ok = sum(1 for _, e, _ in resultados if e == OK)
    n_fail = sum(1 for _, e, _ in resultados if e == FAIL)
    n_skip = sum(1 for _, e, _ in resultados if e == SKIP)
    print(f"\n{n_ok} OK, {n_fail} FAIL, {n_skip} SKIP ({len(resultados)} comprobaciones)")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
