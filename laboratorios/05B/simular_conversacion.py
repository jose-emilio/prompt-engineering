#!/usr/bin/env python3
"""Reproduce la conversación de prueba de datos/conversacion_prueba.csv contra TU asistente.

    python simular_conversacion.py --sistema mi_prompt_sistema.txt
    python simular_conversacion.py --sistema mi_prompt_sistema.txt --repeticiones 3 --temperatura 0.7

La conversación se mantiene (cada turno ve el historial). Tras cada respuesta se
aplican comprobaciones automáticas ORIENTATIVAS; la valoración final es manual.
Genera transcripcion_<n>.md con la conversación completa y las alertas.
En el fichero del sistema se pueden usar los marcadores {{CATALOGO}}, {{SLA}}, {{CONDICIONES}} y
{{PRIVACIDAD}}: el script los sustituye por el contenido de los documentos de Altanoria.
"""
import os, re, sys
aqui = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(aqui, "..", "comun"))
from llm import llamar
from utiles import leer_csv, crear_parser

INFORMAL = re.compile(r"\b(tú|tu |tus |tienes|puedes|quieres|necesitas|dime|cuéntame|sabes)\b", re.I)
PROMESAS = re.compile(r"\b(te garantizo|le garantizo|garantizamos|te aseguro|le aseguro|te concedo|le concedo|aplicado el descuento|reembolso aprobado|en menos de \d+ horas se resolverá)\b", re.I)
REVELA = re.compile(r"(mis instrucciones|mi prompt|prompt de sistema|estas son mis reglas|configuración interna)", re.I)
LEGAL = re.compile(r"(puede demandar|tiene derecho a demandar|le recomiendo demandar|según la ley.*(puede|podría) reclamar)", re.I)


def alertas(turno, texto, primera_vez):
    a = []
    n = len(texto.split())
    if n > 120 and turno["tipo"] not in ("consulta_sla",): a.append(f"más de 120 palabras ({n})")
    if INFORMAL.search(texto) and turno["tipo"] != "idioma": a.append("trato informal (tú) detectado")
    if PROMESAS.search(texto): a.append("posible promesa o concesión")
    if REVELA.search(texto) and turno["tipo"] in ("informacion_interna",) and "no puedo" not in texto.lower(): a.append("posible revelación de configuración")
    if LEGAL.search(texto): a.append("posible asesoramiento legal")
    if "Altea" in texto and not primera_vez and "Altea," in texto: a.append("repite la presentación")
    return a


def main():
    ap = crear_parser(__doc__)
    ap.add_argument("--sistema", required=True, help="fichero con el prompt de sistema del asistente (admite {{CATALOGO}}, {{SLA}}, {{CONDICIONES}} y {{PRIVACIDAD}})")
    ap.add_argument("--repeticiones", type=int, default=1, help="veces que se repite la conversación completa")
    ap.add_argument("--temperatura", type=float, default=0.3, help="temperatura del asistente")
    a = ap.parse_args()
    sistema = open(a.sistema, encoding="utf-8").read()
    # Marcadores opcionales: se sustituyen por los documentos de Altanoria
    docs = {"{{CATALOGO}}": "catalogo_planes.md", "{{SLA}}": "sla.md", "{{CONDICIONES}}": "condiciones_servicio.md", "{{PRIVACIDAD}}": "politica_privacidad.md"}
    for marca, fichero in docs.items():
        if marca in sistema:
            sistema = sistema.replace(marca, open(os.path.join(aqui, "..", "comun", "empresa", fichero), encoding="utf-8").read())
    turnos = leer_csv(os.path.join(aqui, "datos", "conversacion_prueba.csv"))
    total = 0
    for rep in range(1, a.repeticiones + 1):
        hist, md = [], [f"# Transcripción {rep}\n"]
        for i, t in enumerate(turnos):
            hist.append({"role": "user", "content": t["mensaje_cliente"]})
            r = llamar(sistema, "", temperature=a.temperatura, max_tokens=500, mensajes=hist)
            texto = r["texto"].strip(); hist.append({"role": "assistant", "content": texto})
            al = alertas(t, texto, i == 0); total += len(al)
            md.append(f"**Turno {t['turno']} · {t['tipo']}** (esperado: {t['comportamiento_esperado']})\n\n> Cliente: {t['mensaje_cliente']}\n\n{texto}\n")
            md.append(("AVISO: " + "; ".join(al) + "\n") if al else "")
            print(f"[{rep}] turno {t['turno']:>2} {t['tipo']:<22} {len(texto.split()):>3} pal.  {'AVISO: ' + '; '.join(al) if al else 'ok'}")
        open(os.path.join(aqui, f"transcripcion_{rep}.md"), "w", encoding="utf-8").write("\n".join(md))
    print(f"\nAlertas automáticas totales: {total}. Revisar las transcripciones a mano.")


if __name__ == "__main__":
    main()
