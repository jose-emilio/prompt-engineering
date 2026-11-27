#!/usr/bin/env python3
"""Valida salidas JSON de un modelo contra un esquema y compara con la solución.

Entrada: un fichero .jsonl con una línea por respuesta del modelo, con las
claves {"id": "INC-4001", "respuesta": "<texto tal cual devolvió el modelo>"}.

    python validar_json.py salidas.jsonl
    python validar_json.py salidas.jsonl --sin-gold          # solo validar formato

Clasifica cada respuesta en: JSON inválido · JSON con texto alrededor ·
no cumple el esquema · cumple el esquema (y si coincide con el gold).
"""
import collections, os, sys, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from utiles import extraer_json, validar_esquema, leer_jsonl, crear_parser

aqui = os.path.dirname(os.path.abspath(__file__))
ap = crear_parser(__doc__)
ap.add_argument("salidas", help="fichero .jsonl con las respuestas del modelo (lo genera generar_salidas.py)")
ap.add_argument("--sin-gold", action="store_true", help="solo validar el formato, sin comparar con la solución")
a = ap.parse_args()
esquema = json.load(open(os.path.join(aqui, "datos", "esquema_incidencia.json"), encoding="utf-8"))
gold = {g["id"]: g for g in leer_jsonl(os.path.join(aqui, "datos", "incidencias_gold.jsonl"))}
cuenta = collections.Counter(); campos_mal = collections.Counter()
for s in leer_jsonl(a.salidas):
    obj, err = extraer_json(s["respuesta"])
    if obj is None:
        cuenta["json_invalido"] += 1; print(f"FALLO {s['id']}: {err}"); continue
    if err: cuenta["json_con_texto_alrededor"] += 1; print(f"! {s['id']}: {err}")
    errores = validar_esquema(obj, esquema)
    if errores:
        cuenta["no_cumple_esquema"] += 1; print(f"FALLO {s['id']}: " + " | ".join(errores[:3])); continue
    cuenta["cumple_esquema"] += 1
    if not a.sin_gold and s["id"] in gold:
        g = gold[s["id"]]; mal = [k for k in g if obj.get(k) != g[k]]
        if mal:
            for k in mal: campos_mal[k] += 1
            print(f"~ {s['id']}: valores distintos al gold en {mal}")
        else: cuenta["coincide_con_gold"] += 1
print("\nResumen:", dict(cuenta))
if campos_mal: print("Campos con más discrepancias:", campos_mal.most_common())
