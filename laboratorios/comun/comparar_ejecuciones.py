#!/usr/bin/env python3
"""Compara dos ficheros de resultados de ejecutar_suite.py y señala regresiones.

    python ../comun/comparar_ejecuciones.py resultados/v0_*.json resultados/v1_*.json
"""
import glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utiles import crear_parser

def resolver(p):
    """Expande comodines (en Windows el intérprete de órdenes no lo hace) y elige el fichero más reciente."""
    m = sorted(glob.glob(p))
    return m[-1] if m else p

def cargar(p):
    d = json.load(open(p, encoding="utf-8"))
    return d, {r["id"]: r for r in d["resultados"] if "error" not in r}

def correcto(r):
    campos = [k[5:] for k in r if k.startswith("real_")]
    return all(str(r["real_" + c]) == str(r["pred_" + c]) for c in campos)

ap = crear_parser(__doc__)
ap.add_argument("antes", help="fichero (o patrón entre comillas) de resultados de la ejecución de partida; si el patrón da varios ficheros, se usa el más reciente")
ap.add_argument("despues", help="fichero (o patrón entre comillas) de resultados de la ejecución que se compara con la anterior")
p = ap.parse_args()
a, ra = cargar(resolver(p.antes)); b, rb = cargar(resolver(p.despues))
print(f"A = {a['etiqueta']}   B = {b['etiqueta']}\n")
for k in sorted(set(a["resumen"]) | set(b["resumen"])):
    va, vb = a["resumen"].get(k), b["resumen"].get(k)
    if va is None or vb is None: continue
    print(f"{k:<26}{va:>8.1%}{vb:>8.1%}   ({vb-va:+.1%})")
mejoras = [i for i in ra if i in rb and not correcto(ra[i]) and correcto(rb[i])]
regresiones = [i for i in ra if i in rb and correcto(ra[i]) and not correcto(rb[i])]
print(f"\nCasos que mejoran ({len(mejoras)}): {', '.join(mejoras) or '-'}")
print(f"REGRESIONES ({len(regresiones)}): {', '.join(regresiones) or '-'}")
for i in regresiones:
    r = rb[i]
    print(f"  {i} [{r['tipo']}] " + "; ".join(f"{k[5:]}: real={r[k]} pred={r['pred_'+k[5:]]}" for k in r if k.startswith('real_')))
