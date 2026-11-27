# Rescate del laboratorio 14: las dos funciones de `integrador_base.py` ya completadas.
# Solo para quien se haya atascado: sustituir las dos funciones del mismo nombre por estas (el resto del fichero no cambia).

def politica(cat, prio, tiene_pii):
    """Reglas en CÓDIGO (no dependen del modelo)."""
    if cat == "seguridad" or prio in ("P1", "P2"): return True, "urgencia o seguridad"
    if cat in ("necesita_aclaracion", "no_soporte"): return True, "sin contenido atendible"
    return False, ""


def puerta_final(texto):
    m = []
    if any(re.search(p, texto) for p in PATRONES.values()) or re.search(r"\[(DNI|IBAN|EMAIL|TEL)_\d+\]", texto): m.append("datos personales o marcadores en la respuesta")
    for p in PROMESAS:
        if p in texto.lower(): m.append(f"promesa prohibida: {p}")
    if not 70 <= len(texto.split()) <= 160: m.append("longitud fuera de rango")
    return m
