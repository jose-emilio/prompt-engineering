#!/usr/bin/env python3
"""Mide la variabilidad de las respuestas según la temperatura (y top-p).

    python experimento_parametros.py --tarea T1 --temps 0 0.3 0.7 1.0 --repeticiones 10
    python experimento_parametros.py --tarea T2 --temps 0 1.0 --top-p 0.5 1.0

Para cada configuración repite la misma petición N veces y calcula:
  · respuestas distintas (de N)
  · similitud media entre pares (difflib, 0-1; 1 = idénticas)
  · longitud media y desviación (en caracteres)
Guarda todas las salidas en resultados_parametros.csv para su análisis.
"""
import difflib, itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from llm import llamar
from utiles import leer_csv, escribir_csv, desviacion, crear_parser

aqui = os.path.dirname(os.path.abspath(__file__))
ap = crear_parser(__doc__)
ap.add_argument("--tarea", default="T1", help="tarea del experimento: T1 (extracción), T2 (eslogan) o T3 (resumen)")
ap.add_argument("--temps", type=float, nargs="+", default=[0, 0.5, 1.0], help="temperaturas que se comparan")
ap.add_argument("--top-p", type=float, nargs="+", default=[None], help="valores de top-p que se comparan (si se omite, se usa el del modelo)")
ap.add_argument("--repeticiones", type=int, default=10, help="veces que se repite cada petición")
ap.add_argument("--max-tokens", type=int, default=None, help="tope de tokens de cada respuesta (si no se indica, 200). Si se indica, se respeta tal cual aunque esté definida LLM_MIN_TOKENS, para poder ver cómo trunca un límite bajo")
a = ap.parse_args()
tarea = next(t for t in leer_csv(os.path.join(aqui, "datos", "tareas_parametros.csv")) if t["id"] == a.tarea)
sistema = "Eres un asistente de Altanoria. Sigue la instrucción con precisión y no añadas explicaciones."
usuario = f"{tarea['descripcion']}\n\n<entrada>\n{tarea['entrada']}\n</entrada>"
filas = []
print(f"Tarea {tarea['id']} ({tarea['nombre']})\n")
print(f"{'temp':>5} {'top_p':>6} {'distintas':>10} {'similitud':>10} {'long.media':>11} {'desv.':>7}")
for t, tp in itertools.product(a.temps, a.top_p):
    salidas = []
    for i in range(a.repeticiones):
        r = llamar(sistema, usuario, temperature=t, top_p=tp, max_tokens=a.max_tokens or 200, exacto=a.max_tokens is not None)
        salidas.append(r["texto"].strip())
        filas.append(dict(tarea=tarea["id"], temperatura=t, top_p=tp if tp is not None else "", n=i + 1, salida=salidas[-1]))
    pares = list(itertools.combinations(salidas, 2))
    sim = sum(difflib.SequenceMatcher(None, x, y).ratio() for x, y in pares) / len(pares)
    longs = [len(s) for s in salidas]
    print(f"{t:>5} {str(tp or '-'):>6} {len(set(salidas)):>7}/{a.repeticiones:<2} {sim:>10.2f} {sum(longs)/len(longs):>11.0f} {desviacion(longs):>7.1f}")
escribir_csv(os.path.join(aqui, "resultados_parametros.csv"), filas)
print("\nSalidas completas en resultados_parametros.csv")
