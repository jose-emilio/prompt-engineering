#!/usr/bin/env python3
"""Calcula los seis indicadores de referencia del laboratorio 12C a partir de `datos/incidencias_2026.csv` (solo biblioteca estándar).

    python calcular_referencia.py
    python calcular_referencia.py --salida datos/referencia_indicadores.json

Aplica las cuatro correcciones que el análisis necesita: quita las filas duplicadas (mismo `id`), unifica las tres formas de escribir cada
producto, convierte todas las duraciones a minutos y trata los `usuarios_afectados` vacíos como «no consta» (no como 0).
Con `--ingenuo` calcula los mismos indicadores sin una de ellas: son los errores típicos del código generado (`comparar_indicadores.py`
los usa para explicar de dónde sale un valor equivocado).
"""
import csv, json, os, statistics, sys
from collections import Counter
from datetime import datetime

aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from utiles import crear_parser

PRODUCTOS = {"altanoria copilot": "Altanoria Copilot", "copilot": "Altanoria Copilot", "documind": "DocuMind", "docu mind": "DocuMind",
             "agenthub": "AgentHub", "agent hub": "AgentHub"}
FALLOS = ("sin_deduplicar", "producto_sin_unificar", "horas_sin_convertir", "vacios_como_cero", "media_en_vez_de_mediana")


def leer(ruta=None):
    with open(ruta or os.path.join(aqui, "datos", "incidencias_2026.csv"), encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def fecha(texto):
    texto = texto.strip()
    for formato in ("%Y-%m-%d", "%d/%m/%Y"):
        try: return datetime.strptime(texto, formato).date()
        except ValueError: pass
    raise ValueError(f"fecha no válida: {texto!r}")


def indicadores(filas, fallo=None):
    """Los seis indicadores. `fallo` (uno de FALLOS) desactiva una corrección para reproducir un error típico."""
    if fallo != "sin_deduplicar":
        vistos, unicas = set(), []
        for r in filas:
            if r["id"] in vistos: continue
            vistos.add(r["id"]); unicas.append(r)
        filas = unicas
    def producto(r):
        return r["producto"].strip() if fallo == "producto_sin_unificar" else PRODUCTOS[r["producto"].strip().lower()]
    def minutos(r):
        x = float(r["duracion"])
        return x if fallo == "horas_sin_convertir" else (x * 60 if r["unidad"].strip() == "h" else x)
    por_producto = Counter(producto(r) for r in filas)
    sumas = {}
    for r in filas: sumas.setdefault(producto(r), []).append(minutos(r))
    usuarios = [int(r["usuarios_afectados"]) if r["usuarios_afectados"].strip() else (0 if fallo == "vacios_como_cero" else None) for r in filas]
    usuarios = [u for u in usuarios if u is not None]
    resumen = statistics.mean(usuarios) if fallo == "media_en_vez_de_mediana" else statistics.median(usuarios)
    por_mes = Counter(fecha(r["abierta"]).strftime("%Y-%m") for r in filas)
    causas = Counter(r["causa"].strip() for r in filas)
    causa, n = causas.most_common(1)[0]
    return {
        "incidencias_por_producto": dict(sorted(por_producto.items())),
        "duracion_media_min_por_producto": {k: round(statistics.mean(v), 1) for k, v in sorted(sumas.items())},
        "porcentaje_p1": round(100 * sum(r["prioridad"] == "P1" for r in filas) / len(filas), 2),
        "incidencias_por_mes": dict(sorted(por_mes.items())),
        "mediana_usuarios_afectados": round(float(resumen), 1),
        "causa_mas_frecuente": {"causa": causa, "porcentaje": round(100 * n / len(filas), 1)},
    }


def main():
    ap = crear_parser(__doc__, ["python calcular_referencia.py", "python calcular_referencia.py --ingenuo sin_deduplicar"])
    ap.add_argument("--salida", help="fichero JSON donde guardar los indicadores (si se omite, se imprimen)")
    ap.add_argument("--ingenuo", choices=FALLOS, help="calcular sin una de las correcciones, para ver el error típico que produce")
    ap.add_argument("--datos", help="fichero CSV de entrada (por defecto, datos/incidencias_2026.csv)")
    a = ap.parse_args()
    res = indicadores(leer(a.datos), a.ingenuo)
    txt = json.dumps(res, ensure_ascii=False, indent=2)
    if a.salida:
        with open(a.salida, "w", encoding="utf-8") as f: f.write(txt + "\n")
        print(f"Indicadores guardados en {a.salida}")
    else: print(txt)


if __name__ == "__main__":
    main()
