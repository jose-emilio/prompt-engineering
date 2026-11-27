#!/usr/bin/env python3
"""Detector sencillo de datos personales (DNI, IBAN, correo, teléfono).

Sirve para comprobar que, tras anonimizar, no ha quedado nada evidente.
NO es una herramienta de producción: no detecta nombres, direcciones ni datos
de salud, que requieren revisión humana o modelos de reconocimiento de entidades.

    python detectar_pii.py texto_anonimizado.txt
    python detectar_pii.py --json expedientes_anonimizados.json
"""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from utiles import crear_parser

PATRONES = {
    "dni": r"\b\d{8}[A-HJ-NP-TV-Z]\b",
    "nie": r"\b[XYZ]\d{7}[A-HJ-NP-TV-Z]\b",
    "iban": r"\bES\d{2}(?:\s?\d{4}){5}\b",
    "email": r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b",
    "telefono": r"(?<!\d)(?:\+34\s?)?[6-9]\d{2}[\s.-]?\d{3}[\s.-]?\d{3}(?!\d)",
    "fecha_larga": r"\b\d{1,2} de (?:enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre) de \d{4}\b",
    "codigo_postal": r"\b(?:0[1-9]|[1-4]\d|5[0-2])\d{3}\b",
}

def detectar(texto):
    hallazgos = []
    for tipo, pat in PATRONES.items():
        for m in re.finditer(pat, texto):
            hallazgos.append((tipo, m.group(0)))
    return hallazgos

if __name__ == "__main__":
    ap = crear_parser(__doc__)
    ap.add_argument("archivo", help="fichero de texto que se revisa (o un JSON de expedientes si se usa --json)")
    ap.add_argument("--json", action="store_true", help="el fichero es un JSON de expedientes: se revisa el texto de cada uno")
    a = ap.parse_args()
    if a.json:
        datos = json.load(open(a.archivo, encoding="utf-8"))
        textos = [(d.get("id", "?"), d["texto"]) for d in datos]
    else:
        textos = [("documento", open(a.archivo, encoding="utf-8").read())]
    total = 0
    for id_, t in textos:
        h = detectar(t)
        total += len(h)
        for tipo, v in h: print(f"{id_}: {tipo:<14} {v}")
    print(f"\n{total} coincidencias" + ("" if total else " — ningún patrón evidente (sigue siendo necesaria la revisión humana)"))
    sys.exit(1 if total else 0)
