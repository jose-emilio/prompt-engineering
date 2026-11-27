#!/usr/bin/env python3
"""Evalúa un enfoque de detección de urgencia contra el gold.

Entrada: un fichero resultados/*.json generado por ../comun/ejecutar_suite.py.

  · Enfoque A y C (la respuesta ya contiene «urgente»):
        python ../comun/ejecutar_suite.py --prompt enfoque_A.txt --datos datos/tickets_urgencia.csv --campos urgente --etiqueta A
        python evaluar_urgencia.py resultados/A_*.json

  · Enfoque B (el modelo extrae SEÑALES y el código decide con una regla):
        python ../comun/ejecutar_suite.py --prompt enfoque_B.txt --datos datos/tickets_urgencia.csv --campos produccion_parada riesgo_seguridad usuarios_afectados tiene_alternativa --etiqueta B
        python evaluar_urgencia.py resultados/B_*.json --regla

La regla del enfoque B se edita en la función `decidir` de este fichero.
Se informa de falsos negativos (urgente que se pasa por alto: el error más caro)
y de falsos positivos (no urgente marcado como urgente: coste de atención).
"""
import glob, json, os, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from utiles import leer_csv, crear_parser


def decidir(s):
    """REGLA DEL ENFOQUE B. Recibe un diccionario de señales y devuelve 'si' o 'no'.
    Editar para el laboratorio."""
    # Regla de partida (deliberadamente simple): solo la producción parada es urgente.
    return "si" if str(s.get("produccion_parada")).lower() in ("si", "sí") else "no"


def a_entero(v):
    try:
        return int(float(str(v).replace(",", ".")))
    except (ValueError, TypeError):
        return 0


ap = crear_parser(__doc__)
ap.add_argument("resultados", help="fichero (o patrón entre comillas) de resultados que genera ejecutar_suite.py, por ejemplo \"resultados/A_*.json\"")
ap.add_argument("--regla", action="store_true", help="las respuestas contienen señales (enfoque B) y la decisión la toma la función decidir() de este script")
a = ap.parse_args()
gold = {r["id"]: r for r in leer_csv(os.path.join(aqui, "datos", "tickets_urgencia.csv"))}
# En Windows el intérprete de órdenes no expande comodines: se hace aquí y se toma el fichero más reciente
fichero = (sorted(glob.glob(a.resultados)) or [a.resultados])[-1]
datos = json.load(open(fichero, encoding="utf-8"))
tp = fp = fn = tn = 0; fallos = []
for r in datos["resultados"]:
    if "error" in r: continue
    g = gold[r["id"]]
    if a.regla:
        s = {k[5:]: v for k, v in r.items() if k.startswith("pred_")}
        s["usuarios_afectados"] = a_entero(s.get("usuarios_afectados"))
        pred = decidir(s)
    else:
        pred = str(r.get("pred_urgente")).lower().replace("í", "i")
    real = g["urgente"]
    if real == "si" and pred == "si": tp += 1
    elif real == "no" and pred == "si": fp += 1; fallos.append(("FALSO POSITIVO", r["id"], g["prioridad_real"], g["texto"][:90]))
    elif real == "si" and pred != "si": fn += 1; fallos.append(("FALSO NEGATIVO", r["id"], g["prioridad_real"], g["texto"][:90]))
    else: tn += 1
n = tp + fp + fn + tn
print(f"Casos: {n}   Exactitud: {(tp+tn)/n:.1%}")
print(f"Urgentes detectados (TP): {tp}   Urgentes NO detectados (FN): {fn}   Falsas alarmas (FP): {fp}   Correctos no urgentes (TN): {tn}")
if tp + fn: print(f"Exhaustividad sobre urgentes: {tp/(tp+fn):.1%}")
if tp + fp: print(f"Precisión de las alertas:     {tp/(tp+fp):.1%}")
for f in fallos[:15]: print("  ", *f)
