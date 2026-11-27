#!/usr/bin/env python3
"""Pide a un modelo el código de análisis a partir de TU prompt y lo guarda en un fichero .py (no lo ejecuta).

    python generar_codigo.py --prompt prompts/prompt_codigo_v1.txt --salida codigo_v1.py
    python generar_codigo.py --prompt mi_prompt.txt --salida codigo_v2.py --muestra 8

Formato del prompt: igual que en los demás laboratorios (una sola parte, o «sistema» y «usuario» separados por ---USUARIO---).
Variables disponibles: {{columnas}} (descripción de las columnas de datos/columnas.md) y {{muestra}} (las primeras filas del CSV).
Del texto que devuelve el modelo se guarda solo el primer bloque de código Python. REVISA el código antes de ejecutarlo.
"""
import os, re, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from llm import llamar
from utiles import crear_parser

ap = crear_parser(__doc__)
ap.add_argument("--prompt", required=True, help="fichero del prompt (usa {{columnas}} y {{muestra}})")
ap.add_argument("--salida", default="codigo.py", help="fichero .py donde se guarda el código")
ap.add_argument("--muestra", type=int, default=5, help="número de filas del CSV que se incluyen en {{muestra}}")
ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura del modelo")
a = ap.parse_args()
txt = open(a.prompt, encoding="utf-8").read()
sistema, usuario = (txt.split("---USUARIO---", 1) + [""])[:2] if "---USUARIO---" in txt else ("", txt)
columnas = open(os.path.join(aqui, "datos", "columnas.md"), encoding="utf-8").read().strip()
with open(os.path.join(aqui, "datos", "incidencias_2026.csv"), encoding="utf-8") as f:
    muestra = "".join(next(f) for _ in range(a.muestra + 1))
usuario = usuario.strip().replace("{{columnas}}", columnas).replace("{{muestra}}", muestra.strip())
r = llamar(sistema.strip(), usuario, temperature=a.temperatura, max_tokens=4000)
bloques = re.findall(r"```(?:python|py)?\n(.*?)```", r["texto"], re.S)
if not bloques:
    print("La respuesta no contiene un bloque de código. Respuesta (primeros 400 caracteres):\n", r["texto"][:400]); sys.exit(1)
with open(a.salida, "w", encoding="utf-8") as f: f.write(bloques[0].rstrip() + "\n")
print(f"Código guardado en {a.salida} ({len(bloques[0].splitlines())} líneas, {r['salida_tokens']} tokens de salida).")
print(f"Revísalo antes de ejecutarlo. Para compararlo con la referencia:  python comparar_indicadores.py {a.salida}")
