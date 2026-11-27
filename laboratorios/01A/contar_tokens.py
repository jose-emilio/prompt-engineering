#!/usr/bin/env python3
"""Cuenta tokens y palabras de textos y estima costes.

Usos:
    python contar_tokens.py --csv datos/corpus_tokenizacion.csv --col texto
    python contar_tokens.py --archivo ../comun/empresa/condiciones_servicio.md
    python contar_tokens.py --texto "Hola, ¿qué tal?"

Si está instalado `tiktoken` (pip install tiktoken) se usa su codificación
o200k_base. Si no, se usa una ESTIMACIÓN (caracteres / 3,6). Las dos son
aproximaciones: cada proveedor tiene su propio tokenizador y el recuento
exacto es el que informa la API en el campo `usage`.
"""
import csv, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from utiles import contar_tokens, crear_parser

try:
    import tiktoken  # noqa: F401
    METODO = "tiktoken (o200k_base)"
except Exception:
    METODO = "estimación (caracteres / 3,6)"


def fila(nombre, texto):
    pal = len(texto.split())
    tok = contar_tokens(texto)
    return nombre, len(texto), pal, tok, (tok / pal if pal else 0), (len(texto) / tok if tok else 0)


def imprimir(filas):
    print(f"Método: {METODO}\n")
    print(f"{'texto':<34}{'caract.':>8}{'palabras':>9}{'tokens':>8}{'tok/pal.':>9}{'car/tok.':>9}")
    for n, c, p, t, r, k in filas:
        print(f"{n[:33]:<34}{c:>8}{p:>9}{t:>8}{r:>9.2f}{k:>9.1f}")


if __name__ == "__main__":
    ap = crear_parser(__doc__)
    ap.add_argument("--texto", help="texto que se cuenta, escrito entre comillas")
    ap.add_argument("--archivo", help="fichero de texto que se cuenta")
    ap.add_argument("--csv", help="fichero CSV cuyos textos se cuentan, uno por fila")
    ap.add_argument("--col", default="texto", help="columna del CSV que contiene el texto")
    a = ap.parse_args()
    filas = []
    if a.texto:
        filas.append(fila(a.texto[:30], a.texto))
    if a.archivo:
        filas.append(fila(os.path.basename(a.archivo), open(a.archivo, encoding="utf-8").read()))
    if a.csv:
        with open(a.csv, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                filas.append(fila(f"{r.get('id','')}-{r.get('tipo','')}-{r.get('idioma','')}", r[a.col]))
    if not filas:
        ap.error("indique --texto, --archivo o --csv")
    imprimir(filas)
