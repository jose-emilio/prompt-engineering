#!/usr/bin/env python3
"""Evalúa un prompt de respuestas fundamentadas en documentos y la prueba de sesgo.

    # 1. Respuestas con fuentes
    python evaluar_fundamentada.py --prompt mi_prompt.txt
    python evaluar_fundamentada.py --prompt mi_prompt.txt --n 10

    # 2. Prueba contrafactual de sesgo
    python evaluar_fundamentada.py --modo sesgo --prompt prompt_sesgo.txt --repeticiones 5 --temperatura 0.7

Formato del prompt (modo respuestas): sistema, línea ---USUARIO---, usuario con
{{documentos}} y {{pregunta}}. El modelo debe devolver un JSON:
    {"estado": "respondida" | "no_consta" | "aclaracion",
     "respuesta": "<texto>",
     "citas": ["<cita LITERAL de los documentos>", ...]}

El script comprueba, sin intervención humana:
  · estado correcto según el tipo de pregunta (respondible / no_consta / ambigua)
  · que cada cita exista literalmente en los documentos (detecta citas inventadas)
  · que las preguntas «no_consta» no reciban una respuesta con datos
La corrección del CONTENIDO de la respuesta debe revisarse a mano con respuesta_esperada.
"""
import collections, os, re, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from llm import llamar
from utiles import leer_csv, extraer_json, escribir_csv, crear_parser

DOCS = ["catalogo_planes.md", "sla.md", "condiciones_servicio.md", "politica_privacidad.md"]


def norm(t):
    return re.sub(r"\s+", " ", re.sub(r"[*_`>#|]", " ", t)).strip().lower()


def cargar_docs():
    partes = []
    for f in DOCS:
        partes.append(f"<documento nombre=\"{f}\">\n" + open(os.path.join(aqui, "..", "comun", "empresa", f), encoding="utf-8").read() + "\n</documento>")
    return "\n".join(partes)


def leer_prompt(ruta):
    t = open(ruta, encoding="utf-8").read()
    return (t.split("---USUARIO---", 1) if "---USUARIO---" in t else ("", t))


def modo_respuestas(a):
    sistema, usuario = leer_prompt(a.prompt)
    docs = cargar_docs(); docs_n = norm(docs)
    preguntas = leer_csv(os.path.join(aqui, "datos", "preguntas_condiciones.csv"))
    if a.n: preguntas = preguntas[::max(1, len(preguntas) // a.n)][:a.n]
    esperado = {"respondible": "respondida", "no_consta": "no_consta", "ambigua": "aclaracion"}
    res, citas_total, citas_malas = [], 0, 0
    for q in preguntas:
        m = usuario.replace("{{documentos}}", docs).replace("{{pregunta}}", q["pregunta"])
        r = llamar(sistema.strip(), m.strip(), temperature=a.temperatura, max_tokens=500)
        obj, err = extraer_json(r["texto"])
        if not isinstance(obj, dict):
            res.append(dict(id=q["id"], tipo=q["tipo"], estado="(json inválido)", ok_estado=0, citas=0, citas_inventadas=0, respuesta=r["texto"][:200])); continue
        estado = obj.get("estado", ""); citas = obj.get("citas") or []
        malas = [c for c in citas if norm(str(c)) not in docs_n]
        citas_total += len(citas); citas_malas += len(malas)
        ok = int(estado == esperado[q["tipo"]])
        res.append(dict(id=q["id"], tipo=q["tipo"], estado=estado, ok_estado=ok, citas=len(citas), citas_inventadas=len(malas),
                        respuesta=str(obj.get("respuesta", ""))[:200], esperada=q["respuesta_esperada"]))
        print(f"{q['id']} {q['tipo']:<11} estado={estado:<11} {'OK' if ok else 'NO'}  citas={len(citas)} inventadas={len(malas)}")
    por = collections.defaultdict(list)
    for x in res: por[x["tipo"]].append(x["ok_estado"])
    print("\nEstado correcto por tipo de pregunta:")
    for k, v in por.items(): print(f"  {k:<12}{sum(v)}/{len(v)}")
    print(f"Citas: {citas_total} · inventadas (no existen en los documentos): {citas_malas}")
    inventan = [x for x in res if x["tipo"] == "no_consta" and x["estado"] == "respondida"]
    print(f"Preguntas sin respuesta en los documentos que el sistema respondió igualmente: {len(inventan)}")
    escribir_csv(os.path.join(aqui, "resultados_fundamentada.csv"), res)
    print("Detalle en resultados_fundamentada.csv (revisar a mano el contenido de las respuestas).")


def modo_sesgo(a):
    sistema, usuario = leer_prompt(a.prompt)
    casos = leer_csv(os.path.join(aqui, "datos", "casos_sesgo.csv"))
    cuenta = collections.defaultdict(collections.Counter); texto = {}
    for c in casos:
        for _ in range(a.repeticiones):
            r = llamar(sistema.strip(), usuario.replace("{{caso}}", c["prompt_caso"]).strip(), temperature=a.temperatura, max_tokens=120)
            t = r["texto"].lower()
            v = "alta" if re.search(r"\balta\b", t) else "baja" if re.search(r"\bbaja\b", t) else "normal" if re.search(r"\bnormal\b", t) else "?"
            cuenta[c["id"]][v] += 1; texto[c["id"]] = c
    print(f"{'caso':<6}{'grupo':<6}{'atributo':<46}{'alta':>5}{'normal':>7}{'baja':>6}")
    for i, cs in cuenta.items():
        print(f"{i:<6}{texto[i]['grupo']:<6}{texto[i]['atributo'][:44]:<46}{cs['alta']:>5}{cs['normal']:>7}{cs['baja']:>6}")
    print("\nSi los casos de un mismo grupo (misma petición, distinto atributo) reciben prioridades distintas, hay indicios de sesgo.")


ap = crear_parser(__doc__)
ap.add_argument("--modo", choices=["respuestas", "sesgo"], default="respuestas", help="respuestas: evalúa las preguntas con documentos; sesgo: prueba contrafactual con los casos de datos/casos_sesgo.csv")
ap.add_argument("--prompt", required=True, help="fichero del prompt que se prueba")
ap.add_argument("--n", type=int, default=0, help="usar solo los n primeros casos (0 = todos)")
ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura del modelo (en la prueba de sesgo, mayor que 0 para que haya variación)")
ap.add_argument("--repeticiones", type=int, default=1, help="veces que se repite cada caso (en la prueba de sesgo)")
a = ap.parse_args()
(modo_respuestas if a.modo == "respuestas" else modo_sesgo)(a)
