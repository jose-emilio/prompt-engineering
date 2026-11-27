#!/usr/bin/env python3
"""Pide a un modelo la traducción de facturacion.py a JavaScript a partir de TU prompt y la guarda en un fichero .js (no la ejecuta).

    python generar_traduccion.py --prompt prompts/prompt_traduccion_v1.txt --salida traduccion_v1.js
    python generar_traduccion.py --prompt mi_prompt_v2.txt --salida traduccion_v2.js

Formato del prompt: igual que en los demás laboratorios (una sola parte, o «sistema» y «usuario» separados por ---USUARIO---).
Variable disponible: {{codigo}} (el contenido de facturacion.py). Del texto que devuelve el modelo se guarda solo el primer bloque de código.
REVISA la traducción antes de comprobarla.
"""
import os, re, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from llm import llamar
from utiles import crear_parser

ap = crear_parser(__doc__, ["python generar_traduccion.py --prompt prompts/prompt_traduccion_v1.txt --salida traduccion_v1.js"])
ap.add_argument("--prompt", required=True, help="fichero del prompt (usa {{codigo}})")
ap.add_argument("--salida", default="traduccion.js", help="fichero .js donde se guarda la traducción")
ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura del modelo")
a = ap.parse_args()
txt = open(a.prompt, encoding="utf-8").read()
sistema, usuario = (txt.split("---USUARIO---", 1) + [""])[:2] if "---USUARIO---" in txt else ("", txt)
codigo = open(os.path.join(aqui, "facturacion.py"), encoding="utf-8").read().strip()
usuario = usuario.strip().replace("{{codigo}}", codigo)
r = llamar(sistema.strip(), usuario, temperature=a.temperatura, max_tokens=4000)
bloques = re.findall(r"```(?:javascript|js|node)?\n(.*?)```", r["texto"], re.S)
if not bloques:
    print("La respuesta no contiene un bloque de código. Respuesta (primeros 400 caracteres):\n", r["texto"][:400]); sys.exit(1)
with open(a.salida, "w", encoding="utf-8") as f: f.write(bloques[0].rstrip() + "\n")
print(f"Traducción guardada en {a.salida} ({len(bloques[0].splitlines())} líneas, {r['salida_tokens']} tokens de salida).")
print(f"Revísala antes de comprobarla. Para comprobarla:  node comprobar.js {a.salida}  (o pégala en comprobar.html)")
