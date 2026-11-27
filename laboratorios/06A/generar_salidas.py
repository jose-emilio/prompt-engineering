#!/usr/bin/env python3
"""Ejecuta un prompt sobre las 30 notas de incidencia y guarda las respuestas en bruto.

    python generar_salidas.py --prompt prompt_json.txt --salida salidas.jsonl
    python generar_salidas.py --prompt prompt_json.txt --n 10 --temperatura 0.7

El prompt usa {{nota}} y {{esquema}} (se sustituye por datos/esquema_incidencia.json).
Formato del fichero: sistema opcional, línea ---USUARIO---, usuario.
Después: python validar_json.py salidas.jsonl
"""
import os, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from llm import llamar
from utiles import leer_jsonl, escribir_jsonl, crear_parser

ap = crear_parser(__doc__)
ap.add_argument("--prompt", required=True, help="fichero del prompt (usa {{nota}} y {{esquema}})")
ap.add_argument("--salida", default="salidas.jsonl", help="fichero .jsonl donde se guardan las respuestas")
ap.add_argument("--n", type=int, default=0, help="usar solo las n primeras notas (0 = todas)")
ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura del modelo")
a = ap.parse_args()
txt = open(a.prompt, encoding="utf-8").read()
sistema, usuario = (txt.split("---USUARIO---", 1) if "---USUARIO---" in txt else ("", txt))
esquema = open(os.path.join(aqui, "datos", "esquema_incidencia.json"), encoding="utf-8").read()
notas = leer_jsonl(os.path.join(aqui, "datos", "notas_incidencia.jsonl"))
if a.n: notas = notas[:a.n]
out = []
for n in notas:
    m = usuario.replace("{{nota}}", n["nota"]).replace("{{esquema}}", esquema)
    r = llamar(sistema.strip(), m.strip(), temperature=a.temperatura, max_tokens=600)
    out.append({"id": n["id"], "respuesta": r["texto"]}); print(n["id"], len(r["texto"]), "caracteres")
escribir_jsonl(a.salida, out)
print(f"\n{len(out)} respuestas en {a.salida}. Validar con: python validar_json.py {a.salida}")
