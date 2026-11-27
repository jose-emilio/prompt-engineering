#!/usr/bin/env python3
"""Ejecuta un prompt sobre un conjunto de casos y calcula métricas.

Pensado para los laboratorios 07A y 07B (suites de prueba), 04A (few-shot), 12A y 13A.

Ejemplo:
    python ../comun/ejecutar_suite.py \
        --prompt prompt_v0.txt --datos datos/reclamaciones_dev.csv \
        --campos categoria prioridad --etiqueta v0

Formato del fichero de prompt (texto plano):

    Instrucciones del sistema (opcional)
    ---USUARIO---
    Mensaje de usuario con {{texto}} donde irá la entrada de cada caso.

Si no aparece la línea ---USUARIO---, todo el fichero es el mensaje de usuario.
En el mensaje se puede usar cualquier columna del CSV como {{columna}}.

El modelo debe devolver un objeto JSON con las claves de --campos.
La comparación con el valor correcto es literal (mayúsculas y tildes incluidas), salvo en los campos de tipo sí/no (todos los valores correctos son sí o no):
ahí «sí», «si», «Sí», «SI.» o true cuentan como la misma respuesta.
Salida: tabla de métricas por pantalla y un JSON detallado en ./resultados/.

Con --repeticiones N se repite toda la ejecución N veces y se informa de la media y el rango
(mínimo–máximo) de cada métrica. Con temperatura 0 las repeticiones suelen coincidir; sirven
sobre todo con --temperatura mayor que 0 o con modelos que no son totalmente deterministas.
"""
import json, os, sys, time, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from llm import llamar
from utiles import leer_csv, extraer_json, exactitud, informe_clasificacion, normalizar_si_no, crear_parser


def cargar_prompt(ruta):
    t = open(ruta, encoding="utf-8").read()
    if "---USUARIO---" in t:
        s, u = t.split("---USUARIO---", 1)
        return s.strip(), u.strip()
    return "", t.strip()


def rellenar(plantilla, fila):
    for k, v in fila.items():
        plantilla = plantilla.replace("{{" + k + "}}", str(v))
    return plantilla


def ejecutar(a, filas, sistema, usuario, etiqueta):
    """Una ejecución completa: llama al modelo con cada caso, imprime el informe y devuelve el resumen."""
    resultados, t_in, t_out, invalidos = [], 0, 0, 0
    for i, f in enumerate(filas, 1):
        msg = rellenar(usuario, f)
        try:
            r = llamar(sistema, msg, temperature=a.temperatura, max_tokens=a.max_tokens)
        except Exception as e:
            print(f"[{i}/{len(filas)}] {f.get('id','?')}: ERROR {e}")
            resultados.append(dict(id=f.get("id"), error=str(e))); invalidos += 1
            continue
        obj, err = extraer_json(r["texto"])
        t_in += r["entrada_tokens"]; t_out += r["salida_tokens"]
        valido = isinstance(obj, dict) and err is None
        if not valido: invalidos += 1
        res = dict(id=f.get("id"), tipo=f.get("tipo", ""), json_valido=valido, aviso=err, respuesta=r["texto"][:500],
                   salida_tokens=r["salida_tokens"], truncada=r["salida_tokens"] >= a.max_tokens)
        for c in a.campos:
            res["real_" + c] = f.get(c)
            res["pred_" + c] = (obj or {}).get(c) if isinstance(obj, dict) else None
        resultados.append(res)
        if a.pausa: time.sleep(a.pausa)
        if i % 10 == 0: print(f"  {i}/{len(filas)} casos…", flush=True)

    ok = [r for r in resultados if "error" not in r]
    print(f"\n=== {etiqueta}: {len(filas)} casos · JSON válido {sum(r['json_valido'] for r in ok)}/{len(filas)} · tokens {t_in}+{t_out} ===\n")
    resumen = {"json_valido": sum(r["json_valido"] for r in ok) / max(1, len(filas))}
    truncadas = sum(1 for r in ok if r.get("truncada"))
    if truncadas:
        print(f"AVISO: {truncadas} de {len(ok)} respuestas llegaron al límite de {a.max_tokens} tokens de salida (--max-tokens) y pueden estar cortadas"
              f"{'; por eso no se pudo leer el JSON' if resumen['json_valido'] < 0.5 else ''}.")
        print(f"       Repetir con un límite mayor, por ejemplo --max-tokens {max(1000, a.max_tokens * 4)}. Los modelos de razonamiento gastan parte del límite en «pensar» antes de contestar.\n")
    elif resumen["json_valido"] < 0.5 and ok:
        print("AVISO: menos de la mitad de las respuestas contienen un JSON legible. Revisar el campo «respuesta» del fichero de resultados para ver qué devuelve el modelo.\n")
    comparables = {}      # por campo: (reales, predichas); en los campos sí/no, «sí» y «si» cuentan como la misma respuesta
    sin_columna = [c for c in a.campos if all(r["real_" + c] is None for r in ok)]
    for c in a.campos:
        if c in sin_columna:
            print(f"--- Campo: {c} ---\nEl CSV no tiene una columna «{c}»: no hay valor correcto con el que comparar, así que no se calculan métricas de este campo.\n")
            continue
        reales = [str(r["real_" + c]) for r in ok]; pred = [str(r["pred_" + c]) for r in ok]
        comparables[c] = normalizar_si_no(reales, pred)
        reales, pred = comparables[c]
        print(f"--- Campo: {c} ---"); print(informe_clasificacion(reales, pred)); print()
        resumen["exactitud_" + c] = exactitud(reales, pred)
    if comparables:
        todos = [all(comparables[c][0][i] == comparables[c][1][i] for c in comparables) for i in range(len(ok))]
        resumen["exactitud_conjunta"] = sum(todos) / max(1, len(filas))
        print(f"Exactitud conjunta (todos los campos correctos): {resumen['exactitud_conjunta']:.1%}")
    else:
        todos = [True] * len(ok)
        print("Ningún campo tiene valor correcto en el CSV: las respuestas se evalúan aparte, aplicándoles una regla.")
    por_tipo = {}
    for r, t in zip(ok, todos):
        por_tipo.setdefault(r["tipo"] or "-", []).append(t)
    if comparables and len(por_tipo) > 1:
        print("\nExactitud conjunta por tipo de caso:")
        for k, v in sorted(por_tipo.items()): print(f"  {k:<28}{sum(v)}/{len(v)}  ({sum(v)/len(v):.0%})")
    if comparables:
        print("\nErrores (primeros 10):")
        n = 0
        for r, t in zip(ok, todos):
            if not t and n < 10:
                n += 1
                print(f"  {r['id']} [{r['tipo']}] " + "; ".join(f"{c}: real={r['real_'+c]} pred={r['pred_'+c]}" for c in comparables))
    os.makedirs("resultados", exist_ok=True)
    ruta = f"resultados/{etiqueta}_{datetime.datetime.now():%Y%m%d_%H%M%S}.json"
    with open(ruta, "w", encoding="utf-8") as fh:
        json.dump(dict(etiqueta=etiqueta, prompt=a.prompt, datos=a.datos, temperatura=a.temperatura,
                       resumen=resumen, tokens_entrada=t_in, tokens_salida=t_out, resultados=resultados),
                  fh, ensure_ascii=False, indent=2)
    print(f"\nDetalle guardado en {ruta}")
    if not comparables and os.path.exists("evaluar_urgencia.py"):       # laboratorio 03B, enfoque B: la regla decide a partir de las señales
        print(f'Siguiente paso: aplicar la regla con  python evaluar_urgencia.py "{ruta}" --regla')

    return resumen


def main():
    ap = crear_parser(__doc__)
    ap.add_argument("--prompt", required=True, help="fichero del prompt (con {{texto}} u otros marcadores de las columnas del CSV)")
    ap.add_argument("--datos", required=True, help="CSV con los casos y las respuestas correctas")
    ap.add_argument("--campos", nargs="+", default=["categoria"], help="claves JSON a evaluar (columnas del CSV con el mismo nombre = respuesta correcta)")
    ap.add_argument("--etiqueta", default="ejecucion", help="nombre de la ejecución: va en el fichero de resultados")
    ap.add_argument("--n", type=int, default=0, help="limitar a los n primeros casos (0 = todos)")
    ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura del modelo")
    ap.add_argument("--max-tokens", type=int, default=1000, help="máximo de tokens de salida por respuesta (los modelos de razonamiento gastan parte en pensar: si el JSON sale cortado, subirlo)")
    ap.add_argument("--filtro-tipo", default="", help="ejecutar solo los casos cuyo 'tipo' contiene este texto")
    ap.add_argument("--repeticiones", type=int, default=1, help="repetir la ejecución completa y resumir la variación")
    ap.add_argument("--pausa", type=float, default=0.0, help="segundos de pausa entre llamadas")
    a = ap.parse_args()

    sistema, usuario = cargar_prompt(a.prompt)
    filas = leer_csv(a.datos)
    if a.filtro_tipo:
        filas = [f for f in filas if a.filtro_tipo in f.get("tipo", "")]
    if a.n:
        filas = filas[:a.n]

    if a.repeticiones <= 1:
        ejecutar(a, filas, sistema, usuario, a.etiqueta)
        return
    resumenes = []
    for rep in range(1, a.repeticiones + 1):
        print(f"\n##### Repetición {rep}/{a.repeticiones} #####")
        resumenes.append(ejecutar(a, filas, sistema, usuario, f"{a.etiqueta}_r{rep}"))
    print(f"\n=== Resumen de {a.repeticiones} repeticiones de «{a.etiqueta}» (media y rango) ===")
    for m in resumenes[0]:
        v = [r[m] for r in resumenes]
        print(f"  {m:<26}{sum(v)/len(v):6.1%}   ({min(v):.1%} – {max(v):.1%})")
    print("Una diferencia entre versiones menor que este rango no es evidencia de mejora.")


if __name__ == "__main__":
    main()
