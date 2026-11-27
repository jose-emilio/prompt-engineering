#!/usr/bin/env python3
"""Ejecuta el código de análisis (o lee su salida JSON) y compara los seis indicadores con la referencia.

    python comparar_indicadores.py codigo_v1.py
    python comparar_indicadores.py salida.json

Si el argumento es un .py, se ejecuta con el mismo Python en una carpeta temporal que contiene una COPIA de `datos/` (límite de tiempo:
120 s; RECUERDA: es código generado por un modelo, revísalo antes) y se toma como resultado el último objeto JSON que imprima. Si el
código escribe o modifica ficheros de datos, lo avisa: los datos originales no se tocan. Para cada indicador muestra el valor esperado, el
obtenido y si coincide; si no coincide, avisa de si el valor es el que daría uno de los errores típicos (duplicados sin quitar, productos
sin unificar, horas sin convertir, vacíos como 0, media en lugar de mediana).
"""
import hashlib, json, os, shutil, subprocess, sys, tempfile
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun")); sys.path.insert(0, aqui)
from utiles import crear_parser
import calcular_referencia as ref

TOL = {"duracion_media_min_por_producto": 0.5, "porcentaje_p1": 0.1, "mediana_usuarios_afectados": 0.5}
NOMBRES = {"incidencias_por_producto": "Incidencias por producto", "duracion_media_min_por_producto": "Duración media (min) por producto",
           "porcentaje_p1": "Porcentaje de P1", "incidencias_por_mes": "Incidencias por mes",
           "mediana_usuarios_afectados": "Mediana de usuarios afectados", "causa_mas_frecuente": "Causa más frecuente"}


def ultimo_json(texto):
    dec = json.JSONDecoder(); mejor = None; i = 0
    while i < len(texto):
        if texto[i] == "{":
            try: obj, fin = dec.raw_decode(texto, i); mejor = obj; i = fin; continue
            except ValueError: pass
        i += 1
    return mejor


def huellas(carpeta):
    return {f: hashlib.md5(open(os.path.join(carpeta, f), "rb").read()).hexdigest() for f in sorted(os.listdir(carpeta))}


def iguales(clave, esperado, obtenido):
    try:
        if isinstance(esperado, dict):
            if set(esperado) != set(obtenido): return False
            return all(iguales(clave, esperado[k], obtenido[k]) if clave in TOL or isinstance(esperado[k], dict) else esperado[k] == obtenido[k] for k in esperado)
        if clave == "causa_mas_frecuente": return esperado["causa"] == obtenido["causa"] and abs(esperado["porcentaje"] - obtenido["porcentaje"]) <= 0.1
        return abs(float(esperado) - float(obtenido)) <= TOL.get(clave, 0)
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


def main():
    ap = crear_parser(__doc__, ["python comparar_indicadores.py codigo_v1.py", "python comparar_indicadores.py salida.json"])
    ap.add_argument("entrada", help="fichero .py con el código (se ejecuta) o .json con los indicadores")
    ap.add_argument("--timeout", type=int, default=120, help="segundos máximos de ejecución del código")
    a = ap.parse_args()
    if a.entrada.endswith(".py"):
        codigo = os.path.abspath(a.entrada)
        with tempfile.TemporaryDirectory() as tmp:
            shutil.copytree(os.path.join(aqui, "datos"), os.path.join(tmp, "datos"))
            antes = huellas(os.path.join(tmp, "datos"))
            try:
                p = subprocess.run([sys.executable, codigo], cwd=tmp, capture_output=True, text=True, timeout=a.timeout)
            except subprocess.TimeoutExpired:
                print(f"El código tardó más de {a.timeout} s y se detuvo."); return 1
            cambiados = [f for f, h in huellas(os.path.join(tmp, "datos")).items() if antes.get(f) != h]
        if cambiados:
            print("⚠ El código ha escrito o modificado ficheros de datos (" + ", ".join(cambiados) + "). Se ejecutó sobre una copia: los datos originales están intactos.\n"
                  "  Un análisis no debe escribir sobre sus datos de origen: es un defecto grave del código aunque los indicadores salgan bien.\n")
        if p.returncode != 0:
            print("El código falló al ejecutarse. Últimas líneas del error:\n" + "\n".join(p.stderr.strip().splitlines()[-6:])); return 1
        obtenido = ultimo_json(p.stdout)
    else:
        obtenido = ultimo_json(open(a.entrada, encoding="utf-8").read())
    if not isinstance(obtenido, dict):
        print("No se encontró ningún objeto JSON en la salida del código."); return 1
    filas = ref.leer(); esperado = ref.indicadores(filas)
    variantes = {f: ref.indicadores(filas, f) for f in ref.FALLOS}
    ok = 0
    for clave, nombre in NOMBRES.items():
        if clave not in obtenido:
            print(f"✗ {nombre}: falta la clave «{clave}» en la salida"); continue
        if iguales(clave, esperado[clave], obtenido[clave]):
            ok += 1; print(f"✓ {nombre}"); continue
        pista = next((f for f, v in variantes.items() if iguales(clave, v[clave], obtenido[clave])), None)
        print(f"✗ {nombre}\n    esperado: {json.dumps(esperado[clave], ensure_ascii=False)}\n    obtenido: {json.dumps(obtenido[clave], ensure_ascii=False)}"
              + (f"\n    pista: coincide con el cálculo «{pista}»" if pista else ""))
    print(f"\nIndicadores correctos: {ok}/6")
    return 0


if __name__ == "__main__":
    sys.exit(main())
