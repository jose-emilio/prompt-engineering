"""Comprueba tu implementación contra los casos de aceptación.

Uso:  python comprobar.py            (desde esta carpeta)
Lee casos_aceptacion.csv, llama a facturacion.calcular_factura_copilot y
muestra los casos que fallan.
"""
import csv, importlib, math, os, sys

aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, aqui)
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from utiles import crear_parser
crear_parser(__doc__).parse_args()          # sin argumentos: solo ofrece --help
modulo = importlib.import_module("facturacion")
f = modulo.calcular_factura_copilot

def convertir(valor, columna):
    if columna == "usuarios":
        try: return int(valor)
        except ValueError: return valor            # p. ej. "10" como texto
    if columna == "educativo": return valor == "True"
    return valor

ok = fallos = 0
with open(os.path.join(aqui, "datos", "casos_aceptacion.csv"), encoding="utf-8") as fh:
    for i, fila in enumerate(csv.DictReader(fh), 2):
        usuarios = convertir(fila["usuarios"], "usuarios")
        # casos especiales de tipo: booleano y decimal
        if fila["usuarios"].startswith("str:"): usuarios = fila["usuarios"][4:]   # texto, no número
        elif fila["usuarios"] == "True": usuarios = True
        elif fila["usuarios"] == "5.0": usuarios = 5.0
        args = (fila["plan"], usuarios, fila["periodo"], fila["educativo"] == "True")
        try:
            r = f(*args)
            if fila["error"]:
                fallos += 1; print(f"FALLO línea {i} {args}: debía lanzar {fila['error']} y devolvió {r}")
                continue
            malo = [k for k in ("base","descuento_pct","descuento","subtotal","iva","total")
                    if not math.isclose(float(r[k]), float(fila[k]), abs_tol=0.005)]
            if malo:
                fallos += 1; print(f"FALLO línea {i} {args}: difieren {malo}; esperado "
                                   + ", ".join(f"{k}={fila[k]}" for k in malo) + "; obtenido "
                                   + ", ".join(f"{k}={r[k]}" for k in malo))
            else: ok += 1
        except ValueError as e:
            if fila["error"] == "ValueError": ok += 1
            else: fallos += 1; print(f"FALLO línea {i} {args}: ValueError inesperado: {e}")
        except Exception as e:
            fallos += 1; print(f"FALLO línea {i} {args}: {type(e).__name__}: {e}")
print(f"\nCorrectos: {ok}   Fallos: {fallos}")
sys.exit(1 if fallos else 0)
