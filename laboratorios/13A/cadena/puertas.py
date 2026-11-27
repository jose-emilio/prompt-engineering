"""Puertas de validación entre etapas.

Cada puerta recibe la salida de una etapa y devuelve (ok, motivos):
    ok      True si puede pasar a la etapa siguiente
    motivos lista de textos que explican por qué se rechaza (vacía si ok)

Las comprobaciones de FORMATO y ESQUEMA ya están hechas. Lo que falta son las
comprobaciones SEMÁNTICAS marcadas con TODO: son las que de verdad frenan los
errores que «parecen» correctos.
"""
import re
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "comun"))
from utiles import extraer_json, validar_esquema
from contratos import *


def puerta_1(texto_modelo, parte):
    """Valida la salida de la etapa 1 (extracción). Devuelve (ok, motivos, objeto)."""
    obj, err = extraer_json(texto_modelo)
    if obj is None:
        return False, [f"formato: {err}"], None
    if err:  # JSON rodeado de texto: se acepta, pero se anota
        pass
    motivos = validar_esquema(obj, ESQUEMA_ETAPA1)
    if motivos:
        return False, ["esquema: " + m for m in motivos], obj

    # TODO 1 (semántica): cada fragmento de `fragmentos_fuente` debe aparecer
    #   LITERALMENTE en parte["texto"]. Si alguno no aparece, rechazar:
    #   motivos.append(f"fragmento inventado: {frag!r}")

    # TODO 2 (semántica): si datos.importe_eur no es null, ese importe debe
    #   aparecer en el texto del parte (con formato 599, 599,00 o 1.194,00).
    #   Pista: normalizar el texto quitando puntos de millar y cambiando la coma
    #   decimal por un punto antes de buscar el número.

    # (Ya resuelto) Un estado «ok» exige al menos un fragmento fuente.
    if obj["estado"] == "ok" and not obj["fragmentos_fuente"] and obj["categoria"] not in ("necesita_aclaracion", "no_soporte"):
        motivos.append("estado ok sin fragmentos fuente")

    return (len(motivos) == 0), motivos, obj


def puerta_2(texto_modelo, extraccion):
    """Valida la salida de la etapa 2 (análisis)."""
    obj, err = extraer_json(texto_modelo)
    if obj is None:
        return False, [f"formato: {err}"], None
    motivos = validar_esquema(obj, ESQUEMA_ETAPA2)
    if motivos:
        return False, ["esquema: " + m for m in motivos], obj

    # (Ya resueltas) Reglas de negocio de la etapa 2.
    if extraccion["categoria"] == "seguridad" and obj["accion"] != "escalar_humano":
        motivos.append("regla: una incidencia de seguridad siempre se escala a una persona")
    if obj["accion"] == "revision_reembolso" and obj["norma"] not in ("CS-5.3", "CS-5.4"):
        motivos.append("regla: un reembolso exige citar CS-5.3 o CS-5.4")


    return (len(motivos) == 0), motivos, obj


def puerta_3(texto_modelo, extraccion, analisis):
    """Valida el borrador de respuesta al cliente."""
    motivos = []
    palabras = len(texto_modelo.split())
    if not (PALABRAS_MIN <= palabras <= PALABRAS_MAX):
        motivos.append(f"longitud: {palabras} palabras (debe estar entre {PALABRAS_MIN} y {PALABRAS_MAX})")

    # (Ya resueltas) Promesas prohibidas y datos personales.
    bajo = texto_modelo.lower()
    for p in PROMESAS_PROHIBIDAS:
        if p in bajo:
            motivos.append(f"promesa prohibida: «{p}»")
    if re.search(r"\bES\d{2}(?:\s?\d{4}){5}\b", texto_modelo) or re.search(r"\b\d{8}[A-Z]\b", texto_modelo):
        motivos.append("datos personales sensibles (IBAN o DNI) en la respuesta")


    return (len(motivos) == 0), motivos
