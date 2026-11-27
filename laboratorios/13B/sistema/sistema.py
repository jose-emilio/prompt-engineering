"""Sistema ramificado de atención: clasificador → (consulta | incidencia | excepción) → unificador.

    python sistema.py "¿Cuánto cuesta Copilot Team?"
"""
import json, os, sys, time
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, aqui); sys.path.insert(0, os.path.join(aqui, "..", "..", "comun"))
from llm import llamar
from utiles import extraer_json
from rag import recuperar

VERSION = "sistema-v0.1"
UMBRAL_CONFIANZA = 0.7       # por debajo, el mensaje va a la rama de excepciones
UMBRAL_RECUPERACION = 0.05   # puntuación mínima del mejor fragmento para intentar responder (ajustar en el laboratorio)
K = 3
PRECIO_ENTRADA, PRECIO_SALIDA = 2.50, 10.00   # € por millón de tokens (modelo ficticio medio)


def _prompt(nombre):
    t = open(os.path.join(aqui, "prompts", nombre), encoding="utf-8").read()
    s, u = t.split("---USUARIO---", 1)
    return s.strip(), u.strip()


class Traza:
    def __init__(self): self.etapas = []
    def llamar(self, nombre, sistema, usuario, **kw):
        t0 = time.time(); r = llamar(sistema, usuario, **kw)
        self.etapas.append(dict(etapa=nombre, latencia_s=round(time.time() - t0, 2), tokens_entrada=r["entrada_tokens"], tokens_salida=r["salida_tokens"]))
        return r
    def coste(self):
        return sum(e["tokens_entrada"] * PRECIO_ENTRADA + e["tokens_salida"] * PRECIO_SALIDA for e in self.etapas) / 1e6


def clasificar(mensaje, traza):
    s, u = _prompt("clasificador.txt")
    r = traza.llamar("clasificador", s, u.replace("{{mensaje}}", mensaje), temperature=0, max_tokens=80)
    obj, _ = extraer_json(r["texto"])
    if not isinstance(obj, dict) or obj.get("ruta") not in ("consulta", "incidencia", "adversarial", "fuera_de_ambito"):
        return "excepcion", 0.0
    return obj["ruta"], float(obj.get("confianza", 0) or 0)


def rama_consulta(mensaje, traza):
    frs = recuperar(mensaje, K)
    mejor = frs[0]["puntuacion"] if frs else 0
    if mejor < UMBRAL_RECUPERACION:
        return dict(respuesta="No he encontrado información suficiente en la documentación para responder. ¿Quiere que se lo traslade a una persona?", fuentes=[], escalar_humano=True, motivo="sin_evidencia")
    bloque = "\n\n".join(f"[{f['id']}] ({f['titulo']})\n{f['texto']}" for f in frs)
    s, u = _prompt("consulta.txt")
    r = traza.llamar("consulta", s, u.replace("{{fragmentos}}", bloque).replace("{{mensaje}}", mensaje), temperature=0, max_tokens=400)
    obj, _ = extraer_json(r["texto"])
    if not isinstance(obj, dict):
        return dict(respuesta="No he podido elaborar una respuesta fiable.", fuentes=[], escalar_humano=True, motivo="formato_invalido")
    ids = {f["id"] for f in frs}
    fuentes = [x for x in obj.get("fuentes", []) if x in ids]
    if obj.get("suficiente") is False or not fuentes:
        return dict(respuesta=obj.get("respuesta") or "No consta en la documentación.", fuentes=[], escalar_humano=True, motivo="sin_evidencia")
    return dict(respuesta=obj["respuesta"], fuentes=fuentes, escalar_humano=False, motivo="")


def rama_incidencia(mensaje, traza):
    s, u = _prompt("incidencia.txt")
    r = traza.llamar("incidencia", s, u.replace("{{mensaje}}", mensaje), temperature=0, max_tokens=300)
    obj, _ = extraer_json(r["texto"])
    if not isinstance(obj, dict) or obj.get("prioridad") not in ("P1", "P2", "P3", "P4"):
        return dict(respuesta="Hemos recibido su mensaje y lo revisará una persona.", fuentes=[], escalar_humano=True, motivo="formato_invalido")
    esc = bool(obj.get("escalar_humano")) or obj["prioridad"] in ("P1", "P2")
    return dict(respuesta=obj.get("respuesta_cliente", ""), fuentes=[], escalar_humano=esc, prioridad=obj["prioridad"], resumen=obj.get("resumen", ""), motivo="")


def rama_excepcion(motivo):
    return dict(respuesta="No puedo ayudar con esa petición. Si necesita asistencia con productos de Altanoria, indíqueme su consulta.", fuentes=[], escalar_humano=False, motivo=motivo)


def atender(mensaje):
    traza = Traza()
    ruta, conf = clasificar(mensaje, traza)
    if ruta in ("adversarial", "fuera_de_ambito"):
        res = rama_excepcion(ruta)
    elif conf < UMBRAL_CONFIANZA:
        res = dict(rama_excepcion("baja_confianza"), escalar_humano=True, respuesta="No he entendido bien su mensaje; lo revisará una persona.")
    elif ruta == "consulta":
        res = rama_consulta(mensaje, traza)
    else:
        res = rama_incidencia(mensaje, traza)
    res.update(version=VERSION, ruta=ruta, confianza=conf, coste_eur=round(traza.coste(), 6), traza=traza.etapas)
    return res


if __name__ == "__main__":
    from utiles import crear_parser
    ap = crear_parser(__doc__)
    ap.add_argument("mensaje", nargs="*", help="mensaje del cliente entre comillas; si se omite, se usa «¿Cuánto cuesta Copilot Team?»")
    a = ap.parse_args()
    print(json.dumps(atender(" ".join(a.mensaje) or "¿Cuánto cuesta Copilot Team?"), ensure_ascii=False, indent=2))
