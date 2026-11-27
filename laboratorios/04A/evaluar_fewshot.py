#!/usr/bin/env python3
"""Compara zero-shot, one-shot y few-shot sobre la clasificación de tickets.

    python evaluar_fewshot.py --k 0 1 3 8 --repeticiones 3   # media y rango entre 3 selecciones de ejemplos
    python evaluar_fewshot.py --k 6 --orden agrupado        # efecto del orden
    python evaluar_fewshot.py --k 6 --sesgo acceso          # ejemplos sesgados
    python evaluar_fewshot.py --k 3 --n 40                  # prueba rápida
    python evaluar_fewshot.py --k 8 --matriz                # qué categorías se confunden entre sí
    python evaluar_fewshot.py --listar-ejemplos             # ids y texto de los ejemplos (o --listar-ejemplos integracion)
    python evaluar_fewshot.py --ids E-int-1 E-err-1 E-fun-3 # ejemplos elegidos a mano (en lugar de --k)
    python evaluar_fewshot.py --k 0 --instruccion datos/instruccion_con_definiciones.txt   # otra instrucción (con las categorías definidas)
    python evaluar_fewshot.py --k 0 --n 10 --max-tokens 4000 # modelo que razona mucho antes de responder

Los ejemplos salen de datos/tickets_ejemplos.csv; la evaluación, de
datos/tickets_prueba.csv (nunca se mezclan).
"""
import os, random, re, sys, unicodedata
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from llm import llamar
from utiles import leer_csv, exactitud, informe_clasificacion, matriz_confusion, crear_parser

CATS = ["facturacion","acceso","rendimiento","integracion","error","funcionalidad","seguridad","cancelacion","consulta"]
INSTR = ("Clasifica el ticket de soporte en UNA de estas categorías: " + ", ".join(CATS) + ". "
         "Si el ticket menciona varios temas, elige la categoría del PRIMER problema que describe. "
         "Responde únicamente con el nombre de la categoría, en minúsculas, sin negritas, sin puntuación y sin explicación.")


def primera_categoria(texto):
    """Devuelve la categoría de la respuesta (tolera tildes, negritas, comillas y puntuación).
    Si el texto menciona UNA sola categoría, esa es. Si menciona varias («No es facturación, es acceso»),
    la respuesta es ambigua y se devuelve «ambigua»: no se adivina cuál eligió el modelo. Si no hay ninguna,
    devuelve el primer token, que cuenta como categoría no válida."""
    limpio = "".join(c for c in unicodedata.normalize("NFD", texto.lower()) if unicodedata.category(c) != "Mn")     # «facturación» cuenta como «facturacion»
    limpio = limpio.replace("*", " ").replace("`", " ")
    palabras = set(re.findall(r"[a-z]+", limpio))
    halladas = [c for c in CATS if c in palabras]
    if len(halladas) == 1:
        return halladas[0]
    if len(halladas) > 1:
        return "ambigua"
    partes = limpio.split()
    return partes[0].strip(".,;:\"'") if partes else ""


def elegir(ejemplos, k, orden, sesgo, semilla):
    R = random.Random(semilla)
    if k == 0: return []
    if sesgo:
        pool = [e for e in ejemplos if e["categoria"] == sesgo]
        return R.sample(pool, min(k, len(pool)))
    # selección equilibrada: una por categoría, después al azar
    por_cat = {c: [e for e in ejemplos if e["categoria"] == c] for c in CATS}
    for c in por_cat: R.shuffle(por_cat[c])
    sel = []
    ronda = 0
    while len(sel) < k:
        for c in CATS:
            if len(sel) < k and ronda < len(por_cat[c]):
                sel.append(por_cat[c][ronda])
        ronda += 1
    if orden == "aleatorio": R.shuffle(sel)
    elif orden == "agrupado": sel.sort(key=lambda e: e["categoria"])
    elif orden == "inverso": sel = sel[::-1]
    return sel


def construir(sel, texto):
    p = INSTR + "\n\n"
    for e in sel:
        p += f"Ticket: {e['texto']}\nCategoría: {e['categoria']}\n\n"
    p += f"Ticket: {texto}\nCategoría:"
    return p


def imprimir_matriz(reales, pred):
    """Filas: categoría real. Columnas: categoría que ha dicho el modelo. La diagonal son los aciertos."""
    m = matriz_confusion(reales, pred)
    cols = CATS + [c for c in sorted({p for p in pred}) if c not in CATS]       # «» = respuesta sin categoría
    print("\nMatriz de confusión (filas: categoría real; columnas: respuesta del modelo):")
    cab = "real \\ modelo"        # (sin barra invertida dentro de la f-string: Python 3.9 a 3.11 no la admiten)
    print(f"{cab:<16}" + "".join(f"{(c[:5] or '(vac)'):>6}" for c in cols))
    for r in CATS:
        print(f"{r:<16}" + "".join(f"{m[r][c]:>6}" if m[r][c] else f"{'.':>6}" for c in cols))
    fallos = sorted(((n, r, p) for r in m for p, n in m[r].items() if r != p), reverse=True)[:5]
    print("\nConfusiones más frecuentes (real → respuesta del modelo):")
    for n, r, p in fallos: print(f"  {n:>3} × {r} → {p or '(sin categoría)'}")


def main():
    ap = crear_parser(__doc__)
    ap.add_argument("--k", type=int, nargs="+", default=[0, 1, 3, 8], help="números de ejemplos que se comparan, por ejemplo --k 0 1 3 8")
    ap.add_argument("--orden", default="aleatorio", choices=["aleatorio", "agrupado", "inverso"], help="orden de los ejemplos en el prompt")
    ap.add_argument("--sesgo", default="", help="usar solo ejemplos de esta categoría")
    ap.add_argument("--n", type=int, default=0, help="usar solo los n primeros tickets de prueba (0 = todos), para ahorrar tiempo y coste")
    ap.add_argument("--semilla", type=int, default=1, help="semilla de la selección de ejemplos")
    ap.add_argument("--repeticiones", type=int, default=1, help="semillas distintas para los ejemplos")
    ap.add_argument("--ids", nargs="+", metavar="ID", help="usar exactamente estos ejemplos (ids de tickets_ejemplos.csv), en este orden; sustituye a --k")
    ap.add_argument("--listar-ejemplos", nargs="?", const="todas", metavar="CATEGORIA", help="mostrar los ids y el texto de los ejemplos (de una categoría o de todas) y terminar")
    ap.add_argument("--instruccion", metavar="FICHERO", help="usar la instrucción de este fichero en lugar de la instrucción base (por ejemplo, datos/instruccion_con_definiciones.txt)")
    ap.add_argument("--matriz", action="store_true", help="imprimir la matriz de confusión y las confusiones más frecuentes de la última serie")
    ap.add_argument("--max-tokens", type=int, default=2000, help="tope de tokens de la respuesta (un modelo normal usa 1 o 3; los modelos de razonamiento necesitan margen para pensar antes de contestar)")
    a = ap.parse_args()
    aqui = os.path.dirname(os.path.abspath(__file__))
    ej = leer_csv(os.path.join(aqui, "datos", "tickets_ejemplos.csv"))
    prueba = leer_csv(os.path.join(aqui, "datos", "tickets_prueba.csv"))
    global INSTR
    if a.instruccion:
        ruta = a.instruccion if os.path.isabs(a.instruccion) else os.path.join(os.getcwd(), a.instruccion)
        if not os.path.exists(ruta): sys.exit(f"No existe el fichero de instrucción: {a.instruccion}")
        INSTR = open(ruta, encoding="utf-8").read().strip()
    print(f"Instrucción: {a.instruccion or 'base (solo los nombres de las categorías)'}")
    if a.listar_ejemplos:
        for e in ej:
            if a.listar_ejemplos in ("todas", e["categoria"]): print(f"{e['id']:<9}{e['categoria']:<15}{' '.join(e['texto'].split())[:100]}")
        return
    por_id = {e["id"]: e for e in ej}
    if a.ids:
        faltan = [i for i in a.ids if i not in por_id]
        if faltan: sys.exit(f"Ids de ejemplo que no existen: {', '.join(faltan)}. Con --listar-ejemplos se ven los disponibles.")
        fija = [por_id[i] for i in a.ids]
        a.k = [len(fija)]
        if a.repeticiones > 1: print("Con ejemplos elegidos a mano la selección no cambia entre repeticiones (y la temperatura es 0): se hace una sola serie."); a.repeticiones = 1
    if a.n: prueba = prueba[:a.n]
    resumen = []
    for k in a.k:
        accs = []
        for rep in range(a.repeticiones):
            sel = fija if a.ids else elegir(ej, k, a.orden, a.sesgo, a.semilla + rep)
            reales, pred, tok, crudas = [], [], 0, []
            for t in prueba:
                r = llamar("", construir(sel, t["texto"]), temperature=0, max_tokens=a.max_tokens)
                p = primera_categoria(r["texto"])
                if p not in CATS: crudas.append((t["id"], r["texto"], r["salida_tokens"]))
                reales.append(t["categoria"]); pred.append(p); tok += r["entrada_tokens"]
            acc = exactitud(reales, pred); accs.append(acc)
            sin_cat = sum(1 for p_ in pred if p_ not in CATS)
            if sin_cat > len(pred) * 0.2 and rep == 0:
                vacias = [c for c in crudas if not c[1].strip() and c[2] >= a.max_tokens]
                print(f"AVISO: {sin_cat} de {len(pred)} respuestas no contienen una única categoría válida (vacías, sin categoría o con varias) (k={k}). Respuestas del modelo que no se han podido interpretar (las 5 primeras):")
                for idt, txt, ntok in crudas[:5]: print(f"   {idt}: {txt[:160]!r}  ({ntok} tokens de salida)")
                if len(vacias) > len(crudas) / 2:
                    print(f"   Casi todas están VACÍAS y han agotado el límite de {a.max_tokens} tokens: el modelo gasta todo el límite razonando y no llega a escribir la respuesta "
                          f"(ocurre con los modelos de razonamiento). Repetir con un límite mucho mayor, por ejemplo --max-tokens {max(4000, a.max_tokens * 2)}, o usar un modelo sin razonamiento.")
                else:
                    print("   Posibles causas: una explicación sin categoría, o un bloqueo del proveedor. Mirar las respuestas de arriba; si el modelo razona, probar con --max-tokens más alto "
                          f"(ahora {a.max_tokens}).")
            difi = [(r_ == p_) for r_, p_, t in zip(reales, pred, prueba) if t["dificil"] == "si"]
            print(f"k={k:<2} semilla={a.semilla+rep} exactitud={acc:.1%}  difíciles={sum(difi)}/{len(difi)}  tokens_entrada={tok}")
            if k == a.k[-1] and rep == a.repeticiones - 1:
                print(); print(informe_clasificacion(reales, pred))
                if a.matriz: imprimir_matriz(reales, pred)
        resumen.append((k, accs, tok))
    print("\nResumen (k, exactitud media y rango entre repeticiones, tokens de entrada de la última serie):")
    for k, accs, tok in resumen:
        rango = f"  ({min(accs):.1%} – {max(accs):.1%})" if len(accs) > 1 else ""
        print(f"  k={k:<2} {sum(accs)/len(accs):.1%}{rango}  {tok}")
    if a.ids:
        print("Ejemplos elegidos a mano: para compararlos con ejemplos al azar, ejecutar --k con el mismo número de ejemplos y --repeticiones 3.")
    elif a.repeticiones == 1:
        print("Una sola serie por condición: con pocos casos, diferencias de varios puntos pueden ser ruido. Usar --repeticiones 3.")
    else:
        print("Si los rangos de dos condiciones se solapan, no se puede afirmar que una sea mejor.")


if __name__ == "__main__":
    main()
