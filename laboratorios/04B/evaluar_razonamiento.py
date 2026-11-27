#!/usr/bin/env python3
"""Compara respuesta directa, paso a paso y autoconsistencia en problemas de cálculo.

    python evaluar_razonamiento.py --modo directo
    python evaluar_razonamiento.py --modo paso_a_paso
    python evaluar_razonamiento.py --modo autoconsistencia --muestras 5 --temperatura 0.7
    python evaluar_razonamiento.py --modo directo --tipo trampa

El modelo debe terminar con la línea:  RESPUESTA: <valor>
"""
import collections, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from llm import llamar
from utiles import leer_csv, escribir_csv, crear_parser

REGLAS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun", "empresa", "catalogo_planes.md"), encoding="utf-8").read()
SLA = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun", "empresa", "sla.md"), encoding="utf-8").read()
CONTEXTO = f"<catalogo_planes>\n{REGLAS}\n</catalogo_planes>\n<sla>\n{SLA}\n</sla>"
FINAL = "Termina con una última línea con el formato exacto:  RESPUESTA: <valor>  (solo el número con punto decimal, o la respuesta breve)."
PROMPTS = {
    "directo": "Responde sin explicar el razonamiento.\n" + FINAL,
    "paso_a_paso": "Resuelve el problema paso a paso, mostrando los cálculos intermedios y comprobando cada regla aplicable del catálogo y del SLA antes de concluir.\n" + FINAL,
    "autoconsistencia": "Resuelve el problema paso a paso, mostrando los cálculos intermedios.\n" + FINAL,
}


def extraer(texto):
    m = re.findall(r"RESPUESTA:\s*(.+)", texto)
    return m[-1].strip() if m else ""


def igual(pred, real):
    pn = re.sub(r"[^\d.,-]", "", pred).replace(",", ".")
    rn = re.sub(r"[^\d.,-]", "", real).replace(",", ".")
    try:
        return abs(float(pn) - float(rn)) < 0.011
    except ValueError:
        return pred.strip().lower().startswith(real.strip().lower()[:12])


def main():
    ap = crear_parser(__doc__)
    ap.add_argument("--modo", choices=list(PROMPTS), default="directo", help="estrategia: directo (sin razonar), paso_a_paso o autoconsistencia (varias muestras y voto)")
    ap.add_argument("--muestras", type=int, default=5, help="muestras por problema en el modo autoconsistencia")
    ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura (en autoconsistencia debe ser mayor que 0, por ejemplo 0.7)")
    ap.add_argument("--tipo", default="", help="usar solo los problemas de este tipo (por ejemplo, trampa)")
    ap.add_argument("--n", type=int, default=0, help="usar solo los n primeros problemas (0 = todos)")
    a = ap.parse_args()
    aqui = os.path.dirname(os.path.abspath(__file__))
    probs = leer_csv(os.path.join(aqui, "datos", "problemas_calculo.csv"))
    if a.tipo: probs = [p for p in probs if p["tipo"] == a.tipo]
    if a.n: probs = probs[:a.n]
    sistema = "Eres un asistente de facturación de Altanoria. Usa SOLO las reglas de los documentos.\n" + CONTEXTO
    n_muestras = a.muestras if a.modo == "autoconsistencia" else 1
    temp = a.temperatura if a.modo == "autoconsistencia" else 0.0
    salida, ok, tok = [], 0, 0
    for p in probs:
        votos = []
        for _ in range(n_muestras):
            r = llamar(sistema, PROMPTS[a.modo] + "\n\nProblema: " + p["enunciado"], temperature=temp, max_tokens=1200)
            votos.append(extraer(r["texto"])); tok += r["salida_tokens"]
        elegido = collections.Counter(votos).most_common(1)[0][0]
        bien = igual(elegido, p["respuesta_correcta"]); ok += bien
        salida.append(dict(id=p["id"], tipo=p["tipo"], trampa=p["trampa"], correcta=p["respuesta_correcta"], obtenida=elegido, votos="|".join(votos), acierto=int(bien)))
        print(f"{p['id']} {p['tipo']:<16} {'OK' if bien else 'NO'} esperado={p['respuesta_correcta']:<10} obtenido={elegido}")
    print(f"\nModo {a.modo}: {ok}/{len(probs)} = {ok/len(probs):.1%}   tokens de salida: {tok}")
    for t in ("si", "no"):
        s = [x for x in salida if x["trampa"] == t]
        if s: print(f"  trampa={t}: {sum(x['acierto'] for x in s)}/{len(s)}")
    escribir_csv(os.path.join(aqui, f"resultados_{a.modo}.csv"), salida)


if __name__ == "__main__":
    main()
