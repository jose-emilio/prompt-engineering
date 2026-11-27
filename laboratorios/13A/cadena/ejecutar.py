#!/usr/bin/env python3
"""Orquestador de la cadena: extracción → análisis → respuesta, con puertas.

    python ejecutar.py                       # los 25 partes
    python ejecutar.py --n 5                 # los 5 primeros
    python ejecutar.py --id P-023            # un solo parte
    python ejecutar.py --inyectar-fallo etapa1 --tipo-fallo campo_ausente
    python ejecutar.py --inyectar-fallo etapa2 --tipo-fallo json_roto --prob 0.5

Cada decisión se anota en registro.jsonl (una línea por intento de etapa).
"""
import json, os, random, sys, datetime
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, aqui); sys.path.insert(0, os.path.join(aqui, "..", "..", "comun"))
from utiles import leer_jsonl, extraer_json, crear_parser
import etapas, puertas

MAX_REINTENTOS = 2
FALLOS = ["json_roto", "campo_ausente", "valor_fuera_de_rango", "texto_extra"]


def corromper(texto, tipo, R):
    """Simula un fallo del modelo en la respuesta de una etapa."""
    if tipo == "json_roto": return texto[: max(5, len(texto) // 2)]
    if tipo == "texto_extra": return "Claro, aquí tienes el resultado:\n" + texto + "\nEspero que te sirva."
    obj, _ = extraer_json(texto)          # tolera bloques ```json y texto alrededor
    if not isinstance(obj, dict): return texto
    if tipo == "campo_ausente":
        k = R.choice([x for x in obj if x != "version"]); obj.pop(k)
    elif tipo == "valor_fuera_de_rango":
        if "prioridad" in obj: obj["prioridad"] = "P9"
        elif "accion" in obj: obj["accion"] = "aprobar_todo"
    return json.dumps(obj, ensure_ascii=False)


def registrar(f, **kw):
    kw["ts"] = datetime.datetime.now().isoformat(timespec="seconds")
    f.write(json.dumps(kw, ensure_ascii=False) + "\n"); f.flush()


def intentar(nombre, funcion_etapa, funcion_puerta, parte, log, fallo, R, args_extra=()):
    """Ejecuta una etapa con reintentos y puerta. Devuelve (objeto_o_texto, ok)."""
    correccion = ""
    for intento in range(1, MAX_REINTENTOS + 2):
        r = funcion_etapa(*args_extra, correccion=correccion) if args_extra else funcion_etapa(correccion=correccion)
        texto = r["texto"]
        if fallo and fallo["etapa"] == nombre and intento == 1 and R.random() < fallo["prob"]:
            texto = corromper(texto, fallo["tipo"], R)
        res = funcion_puerta(texto)
        ok, motivos, obj = (res[0], res[1], res[2] if len(res) > 2 else texto)
        registrar(log, parte=parte["id"], etapa=nombre, intento=intento, puerta="ok" if ok else "rechazada",
                  motivos=motivos, tokens_entrada=r["entrada_tokens"], tokens_salida=r["salida_tokens"], latencia_s=r["latencia_s"])
        if ok:
            return obj, True
        correccion = "\n".join(f"- {m}" for m in motivos)
    return None, False


def procesar(parte, log, fallo, R):
    salida = dict(id=parte["id"], estado="completado", respuesta=None, motivo=None)
    ext, ok = intentar("etapa1", lambda correccion="": etapas.etapa1_extraer(parte, correccion),
                       lambda t: puertas.puerta_1(t, parte), parte, log, fallo, R)
    if not ok:
        salida.update(estado="escalado", motivo="etapa1 no superó la puerta"); return salida
    if ext["estado"] == "revisar" or ext["categoria"] in ("necesita_aclaracion",):
        salida.update(estado="escalado", motivo=f"extracción marcada como {ext['estado']} / {ext['categoria']}"); return salida
    ana, ok = intentar("etapa2", lambda correccion="": etapas.etapa2_analizar(ext, parte, correccion),
                       lambda t: puertas.puerta_2(t, ext), parte, log, fallo, R)
    if not ok:
        salida.update(estado="escalado", motivo="etapa2 no superó la puerta"); return salida
    if ana["accion"] in ("escalar_humano", "rechazar", "pedir_datos"):
        salida.update(estado="escalado", motivo=f"acción {ana['accion']}", analisis=ana); return salida
    resp, ok = intentar("etapa3", lambda correccion="": etapas.etapa3_responder(ext, ana, parte, correccion),
                        lambda t: puertas.puerta_3(t, ext, ana) + (t,), parte, log, fallo, R)
    if not ok:
        salida.update(estado="escalado", motivo="etapa3 no superó la puerta", analisis=ana); return salida
    salida.update(respuesta=resp, analisis=ana, extraccion=ext)
    return salida


def main():
    ap = crear_parser(__doc__)
    ap.add_argument("--n", type=int, default=0, help="usar solo los n primeros partes (0 = todos)")
    ap.add_argument("--id", default="", help="ejecutar solo el parte con este identificador (por ejemplo, P-004)")
    ap.add_argument("--inyectar-fallo", choices=["etapa1", "etapa2", "etapa3"], default="", help="etapa en la que se corrompe el primer intento, para probar las puertas")
    ap.add_argument("--tipo-fallo", choices=FALLOS, default="campo_ausente", help="cómo se corrompe la respuesta")
    ap.add_argument("--prob", type=float, default=1.0, help="probabilidad de corromper el primer intento")
    ap.add_argument("--semilla", type=int, default=7, help="semilla que decide qué partes se corrompen")
    a = ap.parse_args()
    partes = leer_jsonl(os.path.join(aqui, "..", "datos", "partes_reclamacion.jsonl"))
    if a.id: partes = [p for p in partes if p["id"] == a.id]
    if a.n: partes = partes[:a.n]
    R = random.Random(a.semilla)
    fallo = {"etapa": a.inyectar_fallo, "tipo": a.tipo_fallo, "prob": a.prob} if a.inyectar_fallo else None
    resultados = []
    with open(os.path.join(aqui, "registro.jsonl"), "w", encoding="utf-8") as log:
        for p in partes:
            r = procesar(p, log, fallo, R); resultados.append(r)
            print(f"{p['id']}  {r['estado']:<10} {r['motivo'] or ''}")
    with open(os.path.join(aqui, "salidas.jsonl"), "w", encoding="utf-8") as f:
        for r in resultados: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    c = {}
    for r in resultados: c[r["estado"]] = c.get(r["estado"], 0) + 1
    print("\nResumen:", c, "· detalle en registro.jsonl y salidas.jsonl")


if __name__ == "__main__":
    main()
