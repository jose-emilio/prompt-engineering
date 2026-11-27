#!/usr/bin/env python3
"""Aplica TU prompt de extracción a los correos y guarda las predicciones.

    python extraer.py --prompt mi_prompt.txt --salida predicciones.jsonl
    python extraer.py --prompt mi_prompt.txt --n 10        # prueba rápida

Formato del prompt: igual que en ejecutar_suite.py. Variables disponibles:
{{id}}, {{fecha_correo}}, {{de}}, {{asunto}}, {{cuerpo}} y {{esquema}}
(el esquema JSON de datos/esquema_extraccion.json).
"""
import os, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from llm import llamar
from utiles import leer_jsonl, escribir_jsonl, extraer_json, crear_parser

ap = crear_parser(__doc__)
ap.add_argument("--prompt", required=True, help="fichero del prompt (usa {{id}}, {{fecha_correo}}, {{de}}, {{asunto}}, {{cuerpo}} y {{esquema}})")
ap.add_argument("--salida", default="predicciones.jsonl", help="fichero .jsonl donde se guardan las predicciones")
ap.add_argument("--n", type=int, default=0, help="usar solo los n primeros correos (0 = todos)")
ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura del modelo")
a = ap.parse_args()
txt = open(a.prompt, encoding="utf-8").read()
sistema, usuario = (txt.split("---USUARIO---", 1) + [""])[:2] if "---USUARIO---" in txt else ("", txt)
sistema, usuario = sistema.strip(), usuario.strip()
esquema = open(os.path.join(aqui, "datos", "esquema_extraccion.json"), encoding="utf-8").read()
correos = leer_jsonl(os.path.join(aqui, "datos", "correos_clientes.jsonl"))
if a.n: correos = correos[:a.n]
out = []
for c in correos:
    m = usuario.replace("{{esquema}}", esquema)
    for k, v in c.items(): m = m.replace("{{" + k + "}}", str(v))
    r = llamar(sistema, m, temperature=a.temperatura, max_tokens=500)
    obj, err = extraer_json(r["texto"])
    if obj is None: obj = {"id": c["id"], "_error": err, "_bruto": r["texto"][:300]}
    obj.setdefault("id", c["id"])
    out.append(obj); print(c["id"], "ok" if "_error" not in obj else "ERROR")
escribir_jsonl(a.salida, out)
print(f"\n{len(out)} predicciones guardadas en {a.salida}. Evalúalas con:  python evaluar_extraccion.py {a.salida}")
