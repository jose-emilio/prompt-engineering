#!/usr/bin/env python3
"""Seudonimiza los identificadores estructurados (DNI, IBAN, correo y teléfono) de los expedientes.

    python seudonimizar.py                       # todos los expedientes
    python seudonimizar.py --ids EXP-01 EXP-02 EXP-03

Escribe expedientes_tratados.json (textos con marcadores como [DNI_1]) y tabla_correspondencia.json
(que debe guardarse APARTE del texto tratado). Los NOMBRES, DIRECCIONES, FECHAS DE NACIMIENTO y DATOS DE SALUD
no se detectan con expresiones regulares: hay que revisarlos y tratarlos a mano (esa es la parte del ejercicio).
"""
import json, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from utiles import crear_parser

PATRONES = {
    "DNI": r"\b\d{8}[A-HJ-NP-TV-Z]\b",
    "IBAN": r"\bES\d{2}(?:\s?\d{4}){5}\b",
    "EMAIL": r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b",
    "TEL": r"(?<!\d)(?:\+34\s?)?[6-9]\d{2}[\s.-]?\d{3}[\s.-]?\d{3}(?!\d)",
}


def seudonimizar(texto, nombres_conocidos=()):
    tabla, contadores = {}, {}

    def reemplazo(tipo):
        def f(m):
            contadores[tipo] = contadores.get(tipo, 0) + 1
            marca = f"[{tipo}_{contadores[tipo]}]"
            tabla[marca] = m.group(0)
            return marca
        return f
    for tipo, pat in PATRONES.items():
        texto = re.sub(pat, reemplazo(tipo), texto)
    for i, nombre in enumerate(nombres_conocidos, 1):
        marca = f"[PERSONA_{i}]"
        if nombre in texto:
            tabla[marca] = nombre
            texto = texto.replace(nombre, marca)
    return texto, tabla


if __name__ == "__main__":
    ap = crear_parser(__doc__)
    ap.add_argument("--ids", nargs="*", help="identificadores de los expedientes que se tratan (si se omite, todos)")
    a = ap.parse_args()
    aqui = os.path.dirname(os.path.abspath(__file__))
    exps = json.load(open(os.path.join(aqui, "datos", "expedientes.json"), encoding="utf-8"))
    if a.ids:
        exps = [e for e in exps if e["id"] in a.ids]
    tratados, tablas = [], {}
    for e in exps:
        texto, tabla = seudonimizar(e["texto"])
        tratados.append({"id": e["id"], "texto": texto, "tarea_posterior": e["tarea_posterior"]})
        tablas[e["id"]] = tabla
        print(f"{e['id']}: {len(tabla)} datos sustituidos")
    json.dump(tratados, open("expedientes_tratados.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump(tablas, open("tabla_correspondencia.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Revisar a mano nombres, direcciones, fechas de nacimiento y datos de salud; después: python detectar_pii.py --json expedientes_tratados.json")
