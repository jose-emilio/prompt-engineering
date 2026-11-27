"""Utilidades compartidas por los laboratorios (solo biblioteca estándar)."""
import argparse
import csv
import json
import math
import os
import re
from collections import Counter, defaultdict


# ---------- Ayuda de línea de comandos ----------
class _FormatoAyuda(argparse.RawDescriptionHelpFormatter):
    """Ayuda en español: «uso:», valores por defecto y descripciones sin reajustar."""

    def add_usage(self, usage, actions, groups, prefix=None):
        super().add_usage(usage, actions, groups, prefix or "uso: ")

    def _get_help_string(self, action):
        ayuda = action.help or ""
        if "%(default)" in ayuda or action.default in (None, argparse.SUPPRESS, False, "") or action.option_strings == ["-h", "--help"]:
            return ayuda
        if isinstance(action.default, (list, tuple)) and all(x is None for x in action.default): return ayuda
        if isinstance(action.default, (list, tuple)): return ayuda + " (por defecto: " + " ".join(str(x) for x in action.default) + ")"
        return ayuda + " (por defecto: %(default)s)"


def crear_parser(descripcion, ejemplos=(), **kw):
    """ArgumentParser de los laboratorios: `python script.py --help` explica qué hace el script, cada opción (con su valor por defecto) y
    muestra ejemplos. Cada `add_argument` debe llevar `help=`."""
    epilogo = ("Ejemplos:\n" + "\n".join("  " + e for e in ejemplos)) if ejemplos else None
    p = argparse.ArgumentParser(description=descripcion, epilog=epilogo, formatter_class=_FormatoAyuda, add_help=False, **kw)
    p.add_argument("-h", "--help", action="help", help="muestra esta ayuda y termina")
    p._positionals.title = "argumentos"; p._optionals.title = "opciones"
    return p


# ---------- Entrada y salida ----------
def leer_csv(ruta, delimitador=","):
    with open(ruta, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=delimitador))


def escribir_csv(ruta, filas, campos=None):
    campos = campos or list(filas[0].keys())
    os.makedirs(os.path.dirname(os.path.abspath(ruta)), exist_ok=True)
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        w.writerows(filas)


def leer_jsonl(ruta):
    with open(ruta, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def escribir_jsonl(ruta, filas):
    os.makedirs(os.path.dirname(os.path.abspath(ruta)), exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        for fila in filas:
            f.write(json.dumps(fila, ensure_ascii=False) + "\n")


def leer_texto(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


# ---------- Tokens (estimación) ----------
def contar_tokens(texto):
    """Cuenta tokens. Si está instalado `tiktoken` lo usa (codificación
    o200k_base); si no, aplica una estimación documentada en el laboratorio
    01A (aprox. 1 token por cada 3,6 caracteres en español)."""
    try:
        import tiktoken
        return len(tiktoken.get_encoding("o200k_base").encode(texto))
    except Exception:
        return max(1, round(len(texto) / 3.6))


# ---------- Extracción de JSON de una respuesta ----------
def extraer_json(texto):
    """Devuelve (objeto, error). Acepta JSON puro o dentro de ```json ... ```."""
    t = texto.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", t, re.S)
    if m:
        t = m.group(1).strip()
    try:
        return json.loads(t), None
    except json.JSONDecodeError as e:
        # intento: primer { ... último }
        i, j = t.find("{"), t.rfind("}")
        if i != -1 and j > i:
            try:
                return json.loads(t[i:j + 1]), "JSON rodeado de texto"
            except json.JSONDecodeError:
                pass
        return None, f"JSON inválido: {e}"


# ---------- Validación de esquema (subconjunto de JSON Schema) ----------
def validar_esquema(obj, esquema, ruta="$"):
    """Valida `obj` contra un subconjunto de JSON Schema: type, properties,
    required, enum, items, minimum, maximum, pattern, additionalProperties,
    minLength, maxLength, minItems, maxItems. Devuelve una lista de errores."""
    errores = []
    tipos = {"string": str, "integer": int, "number": (int, float), "boolean": bool,
             "array": list, "object": dict, "null": type(None)}
    t = esquema.get("type")
    if t:
        posibles = t if isinstance(t, list) else [t]
        ok = False
        for p in posibles:
            py = tipos[p]
            if p in ("integer", "number") and isinstance(obj, bool):
                continue
            if isinstance(obj, py):
                ok = True
        if not ok:
            return [f"{ruta}: se esperaba {t}, hay {type(obj).__name__}"]
    if "enum" in esquema and obj not in esquema["enum"]:
        errores.append(f"{ruta}: valor {obj!r} fuera de {esquema['enum']}")
    if isinstance(obj, (int, float)) and not isinstance(obj, bool):
        if "minimum" in esquema and obj < esquema["minimum"]:
            errores.append(f"{ruta}: {obj} < mínimo {esquema['minimum']}")
        if "maximum" in esquema and obj > esquema["maximum"]:
            errores.append(f"{ruta}: {obj} > máximo {esquema['maximum']}")
    if isinstance(obj, str):
        if "pattern" in esquema and not re.search(esquema["pattern"], obj):
            errores.append(f"{ruta}: {obj!r} no cumple el patrón {esquema['pattern']}")
        if "minLength" in esquema and len(obj) < esquema["minLength"]:
            errores.append(f"{ruta}: longitud menor que {esquema['minLength']}")
        if "maxLength" in esquema and len(obj) > esquema["maxLength"]:
            errores.append(f"{ruta}: longitud mayor que {esquema['maxLength']}")
    if isinstance(obj, dict):
        for r in esquema.get("required", []):
            if r not in obj:
                errores.append(f"{ruta}: falta el campo obligatorio '{r}'")
        props = esquema.get("properties", {})
        for k, v in obj.items():
            if k in props:
                errores += validar_esquema(v, props[k], f"{ruta}.{k}")
            elif esquema.get("additionalProperties") is False:
                errores.append(f"{ruta}: campo no permitido '{k}'")
    if isinstance(obj, list):
        if "minItems" in esquema and len(obj) < esquema["minItems"]:
            errores.append(f"{ruta}: menos de {esquema['minItems']} elementos")
        if "maxItems" in esquema and len(obj) > esquema["maxItems"]:
            errores.append(f"{ruta}: más de {esquema['maxItems']} elementos")
        if "items" in esquema:
            for i, el in enumerate(obj):
                errores += validar_esquema(el, esquema["items"], f"{ruta}[{i}]")
    return errores


# ---------- Métricas de clasificación ----------
_SI = {"si", "sí", "yes", "true", "verdadero", "1"}
_NO = {"no", "false", "falso", "0"}


def si_no(valor):
    """«sí» o «no» si el valor es una respuesta de tipo sí/no (con o sin tilde, mayúsculas, punto final, comillas o booleano); None en otro caso."""
    s = str(valor).strip().strip("\"'`").rstrip(".").strip().lower()
    return "si" if s in _SI else "no" if s in _NO else None


def normalizar_si_no(reales, predichas):
    """Si el campo es de tipo sí/no (todos los valores reales lo son), compara «sí», «si», «Sí», «SI.» o True como la misma respuesta.
    Un valor predicho que no es sí/no (o que falta) se deja como está y cuenta como error."""
    if reales and all(si_no(r) for r in reales):
        return [si_no(r) for r in reales], [si_no(p) or str(p) for p in predichas]
    return reales, predichas


def exactitud(reales, predichas):
    ok = sum(1 for r, p in zip(reales, predichas) if r == p)
    return ok / len(reales) if reales else 0.0


def matriz_confusion(reales, predichas):
    m = defaultdict(Counter)
    for r, p in zip(reales, predichas):
        m[r][p] += 1
    return m


def precision_recall_f1(reales, predichas):
    """Devuelve {clase: (precisión, exhaustividad, f1, soporte)} y la F1 macro."""
    clases = sorted(set(reales) | set(predichas))
    out, f1s = {}, []
    for c in clases:
        tp = sum(1 for r, p in zip(reales, predichas) if r == c and p == c)
        fp = sum(1 for r, p in zip(reales, predichas) if r != c and p == c)
        fn = sum(1 for r, p in zip(reales, predichas) if r == c and p != c)
        pr = tp / (tp + fp) if tp + fp else 0.0
        rc = tp / (tp + fn) if tp + fn else 0.0
        f1 = 2 * pr * rc / (pr + rc) if pr + rc else 0.0
        out[c] = (round(pr, 3), round(rc, 3), round(f1, 3), tp + fn)
        f1s.append(f1)
    return out, round(sum(f1s) / len(f1s), 3) if f1s else 0.0


def informe_clasificacion(reales, predichas):
    por_clase, macro = precision_recall_f1(reales, predichas)
    lineas = [f"Exactitud: {exactitud(reales, predichas):.1%}   F1 macro: {macro}", "",
              f"{'clase':<22}{'prec.':>7}{'exh.':>7}{'F1':>7}{'n':>5}"]
    for c, (p, r, f, n) in por_clase.items():
        lineas.append(f"{c:<22}{p:>7}{r:>7}{f:>7}{n:>5}")
    return "\n".join(lineas)


def desviacion(valores):
    if len(valores) < 2:
        return 0.0
    m = sum(valores) / len(valores)
    return math.sqrt(sum((v - m) ** 2 for v in valores) / (len(valores) - 1))
