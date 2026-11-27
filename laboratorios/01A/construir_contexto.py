#!/usr/bin/env python3
"""Construye un documento largo (el «pajar») con tres «agujas» (datos únicos) para el experimento de la aguja en el pajar, que prueba la memoria del contexto.

    python construir_contexto.py --tokens 25000            # genera contexto_largo.md
    python construir_contexto.py --tokens 120000 --salida contexto_120k.md

El documento es un registro de cambios sintético. En tres posiciones (inicio,
mitad y final) se inserta una entrada con una referencia única. Después se
pregunta al modelo por cada una; las respuestas correctas están en
preguntas_aguja.md (sin las respuestas) y en la sección de solución del laboratorio.
"""
import os, random, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "comun"))
from utiles import contar_tokens, crear_parser

AREAS = ["autocompletado", "revisión de pull requests", "conector de SharePoint", "búsqueda semántica", "editor de flujos",
         "puertas de validación", "registro de ejecuciones", "panel de administración", "webhooks", "permisos por documento"]
FRASES = ["mejora el rendimiento de {x}", "corrige un error intermitente en {x}", "añade opciones de configuración a {x}",
          "refuerza la validación de entradas en {x}", "mejora los mensajes de error de {x}", "ajusta los límites de {x}"]
AGUJAS = [  # (posición relativa, texto, pregunta, respuesta)
    (0.03, "Se añade el modo «Cometa verde» a AgentHub 9.9.1 con la referencia interna ZX-4471.", "¿Qué referencia interna tiene el modo «Cometa verde»?", "ZX-4471"),
    (0.50, "DocuMind 9.9.2 incorpora el conector «Lince» con la referencia interna QW-8820.", "¿Qué referencia interna tiene el conector «Lince»?", "QW-8820"),
    (0.97, "Altanoria Copilot 9.9.3 activa la función «Brújula» con la referencia interna MP-1359.", "¿Qué referencia interna tiene la función «Brújula»?", "MP-1359"),
]

ap = crear_parser(__doc__)
ap.add_argument("--tokens", type=int, default=25000, help="tamaño aproximado del documento, en tokens según la estimación del script (los tokens reales pueden ser un 10 %% a un 35 %% más)")
ap.add_argument("--salida", default="contexto_largo.md", help="fichero del documento que se crea")
ap.add_argument("--semilla", type=int, default=3, help="semilla del generador: la misma semilla da el mismo documento")
a = ap.parse_args()
R = random.Random(a.semilla)
lineas, i = ["# Registro de cambios (sintético)\n"], 0
total_est = 0
aguja_idx = 0
while total_est < a.tokens:
    i += 1
    x = R.choice(AREAS)
    texto = f"## Entrada {i} — 2026-{R.randint(1,10):02d}-{R.randint(1,28):02d}\n\n- Cambio: {R.choice(FRASES).format(x=x)}. Referencia interna: AL-{R.randint(1000,9999)}.\n"
    if aguja_idx < len(AGUJAS) and total_est >= AGUJAS[aguja_idx][0] * a.tokens:
        texto = f"## Entrada {i} — 2026-10-30\n\n- Cambio: {AGUJAS[aguja_idx][1]}\n"
        aguja_idx += 1
    lineas.append(texto); total_est += contar_tokens(texto)
while aguja_idx < len(AGUJAS):   # por si faltó alguna
    lineas.append(f"## Entrada final — 2026-10-30\n\n- Cambio: {AGUJAS[aguja_idx][1]}\n"); aguja_idx += 1
doc = "\n".join(lineas)
open(a.salida, "w", encoding="utf-8").write(doc)
with open("preguntas_aguja.md", "w", encoding="utf-8") as f:
    f.write("# Preguntas sobre el documento largo\n\n(Pegar el documento completo y después formular cada pregunta por separado.)\n\n")
    for k, (_, _, q, _) in enumerate(AGUJAS, 1):
        f.write(f"{k}. {q}\n")
print(f"Documento: {a.salida} · {len(doc)} caracteres · ~{contar_tokens(doc)} tokens · {i} entradas")
