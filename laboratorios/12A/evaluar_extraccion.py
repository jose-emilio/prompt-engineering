#!/usr/bin/env python3
"""Evalúa predicciones de extracción contra el gold, campo a campo.

    python evaluar_extraccion.py predicciones.jsonl
    python evaluar_extraccion.py predicciones.jsonl --detalle

Métricas por campo:
  · correcto        valor igual al gold (incluido null = null)
  · inventado       el gold es null y la predicción NO lo es   ← el error más grave
  · omitido         el gold tiene valor y la predicción es null
  · equivocado      ambos tienen valor pero distinto
Además valida cada objeto contra el esquema y cuenta los JSON inválidos.
"""
import collections, json, os, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from utiles import leer_jsonl, validar_esquema, crear_parser

ap = crear_parser(__doc__)
ap.add_argument("predicciones", help="fichero .jsonl con las predicciones (lo genera extraer.py)")
ap.add_argument("--detalle", action="store_true", help="mostrar cada campo equivocado, omitido o inventado")
a = ap.parse_args()
gold = {g["id"]: g for g in leer_jsonl(os.path.join(aqui, "datos", "correos_gold.jsonl"))}
esquema = json.load(open(os.path.join(aqui, "datos", "esquema_extraccion.json"), encoding="utf-8"))
pred = {p["id"]: p for p in leer_jsonl(a.predicciones)}
campos = [k for k in esquema["required"] if k != "id"]
c = {k: collections.Counter() for k in campos}
invalidos = incumple = 0
for i, g in gold.items():
    p = pred.get(i)
    if p is None or "_error" in p:
        invalidos += 1; continue
    if validar_esquema(p, esquema): incumple += 1
    for k in campos:
        gv, pv = g[k], p.get(k)
        if isinstance(gv, float) and isinstance(pv, (int, float)) and abs(gv - pv) < 0.005: pv = gv
        if gv == pv: c[k]["correcto"] += 1
        elif gv is None: c[k]["inventado"] += 1; a.detalle and print(f"INVENTADO {i}.{k}: pred={pv!r}")
        elif pv is None: c[k]["omitido"] += 1; a.detalle and print(f"OMITIDO   {i}.{k}: gold={gv!r}")
        else: c[k]["equivocado"] += 1; a.detalle and print(f"MAL       {i}.{k}: gold={gv!r} pred={pv!r}")
n = len(gold) - invalidos
print(f"\nCorreos: {len(gold)} · JSON inválido o ausente: {invalidos} · no cumplen el esquema: {incumple}\n")
print(f"{'campo':<24}{'correcto':>9}{'inventado':>10}{'omitido':>9}{'equivocado':>11}")
tot = collections.Counter()
for k in campos:
    r = c[k]; tot.update(r)
    print(f"{k:<24}{r['correcto']:>9}{r['inventado']:>10}{r['omitido']:>9}{r['equivocado']:>11}")
suma = sum(tot.values()) or 1
print(f"\nAciertos totales: {tot['correcto']}/{suma} = {tot['correcto']/suma:.1%}   Valores INVENTADOS: {tot['inventado']}")
