"""Las tres etapas de la cadena. Cada una usa un prompt de la carpeta prompts/."""
import json, os, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "..", "comun"))
from llm import llamar
from contratos import NORMAS


def _prompt(nombre):
    t = open(os.path.join(aqui, "prompts", nombre), encoding="utf-8").read()
    s, u = (t.split("---USUARIO---", 1) + [""])[:2] if "---USUARIO---" in t else ("", t)
    return s.strip(), u.strip()


def _normas_texto():
    return "\n".join(f"- {k}: {v}" for k, v in NORMAS.items())


def etapa1_extraer(parte, correccion=""):
    s, u = _prompt("etapa1.txt")
    u = u.replace("{{texto}}", parte["texto"]).replace("{{producto}}", parte["producto"]).replace("{{plan}}", parte["plan"])
    if correccion:
        u += "\n\nLa salida anterior fue rechazada por estos motivos; corrígelos:\n" + correccion
    return llamar(s, u, temperature=0, max_tokens=600)


def etapa2_analizar(extraccion, parte, correccion=""):
    s, u = _prompt("etapa2.txt")
    u = (u.replace("{{extraccion}}", json.dumps(extraccion, ensure_ascii=False, indent=2))
          .replace("{{normas}}", _normas_texto()).replace("{{plan}}", parte["plan"]))
    if correccion:
        u += "\n\nLa salida anterior fue rechazada por estos motivos; corrígelos:\n" + correccion
    return llamar(s, u, temperature=0, max_tokens=500)


def etapa3_responder(extraccion, analisis, parte, correccion=""):
    s, u = _prompt("etapa3.txt")
    u = (u.replace("{{extraccion}}", json.dumps(extraccion, ensure_ascii=False, indent=2))
          .replace("{{analisis}}", json.dumps(analisis, ensure_ascii=False, indent=2))
          .replace("{{norma_texto}}", NORMAS.get(analisis["norma"], ""))
          .replace("{{cliente}}", parte["cliente"]))
    if correccion:
        u += "\n\nEl borrador anterior fue rechazado por estos motivos; corrígelos:\n" + correccion
    return llamar(s, u, temperature=0.2, max_tokens=500)
