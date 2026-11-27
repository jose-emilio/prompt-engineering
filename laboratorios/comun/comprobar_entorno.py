#!/usr/bin/env python3
"""Comprueba, antes de empezar un laboratorio con scripts, que el entorno está listo.

    python ../comun/comprobar_entorno.py              # revisa Python, variables y hace UNA llamada mínima
    python ../comun/comprobar_entorno.py --sin-llamada  # solo revisa Python y variables

Qué comprueba:
  1. Versión de Python (3.9 o superior).
  2. Variables de entorno del proveedor elegido (LLM_PROVIDER, LLM_API_KEY, LLM_MODEL...).
  3. Una llamada de prueba al modelo (cuesta una fracción de céntimo) y su latencia.
No imprime nunca la clave de API."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utiles import crear_parser

PROVEEDORES = {
    "openai": ("LLM_MODEL", "LLM_API_KEY"),     # LLM_API_KEY no hace falta con servidores locales (Ollama, LM Studio)
    "anthropic": ("LLM_MODEL", "LLM_API_KEY"),
    "bedrock": ("LLM_MODEL",),                  # usa las credenciales de AWS ya configuradas
    "manual": (),
    "mock": (),
}
estado = {"ok": True}


def ventana_ollama(base, modelo):
    """Ventana de contexto con la que Ollama tiene cargado el modelo (None si el servidor no es Ollama o no se puede saber)."""
    import json, urllib.request
    raiz = base.rstrip("/")
    raiz = raiz[:-3] if raiz.endswith("/v1") else raiz
    try:
        with urllib.request.urlopen(raiz + "/api/ps", timeout=5) as r: cargados = json.loads(r.read().decode("utf-8")).get("models", [])
    except Exception:
        return None
    for m in cargados:
        if modelo in (m.get("name"), m.get("model")): return m.get("context_length")
    return cargados[0].get("context_length") if len(cargados) == 1 else None


def ok(msg): print(f"  OK     {msg}")
def aviso(msg): print(f"  AVISO  {msg}")
def error(msg): estado["ok"] = False; print(f"  ERROR  {msg}")


def main():
    ap = crear_parser(__doc__)
    ap.add_argument("--sin-llamada", action="store_true", help="no llamar al modelo: solo comprobar Python y las variables")
    a = ap.parse_args()

    print("1. Python")
    if sys.version_info >= (3, 9): ok(f"Python {sys.version.split()[0]}")
    else: error(f"Python {sys.version.split()[0]}: se necesita 3.9 o superior")

    print("2. Variables de entorno")
    proveedor = os.environ.get("LLM_PROVIDER", "openai").lower()
    if proveedor not in PROVEEDORES:
        error(f"LLM_PROVIDER={proveedor!r} no es válido. Opciones: {', '.join(PROVEEDORES)}")
        return fin()
    ok(f"LLM_PROVIDER={proveedor}" + ("" if "LLM_PROVIDER" in os.environ else " (valor por defecto)"))
    for v in PROVEEDORES[proveedor]:
        if os.environ.get(v):
            ok(f"{v} definida" + ("" if v == "LLM_API_KEY" else f" = {os.environ[v]}"))
        elif v == "LLM_API_KEY" and os.environ.get("LLM_BASE_URL", "").startswith(("http://localhost", "http://127.")):
            ok("LLM_API_KEY vacía, pero LLM_BASE_URL apunta a un servidor local")
        else:
            error(f"{v} sin definir")
    if proveedor == "bedrock":
        try:
            import boto3  # noqa: F401
            ok("boto3 instalado")
        except ImportError:
            error("falta boto3 (pip install boto3), necesario solo con el proveedor bedrock")
    if proveedor == "manual":
        ok("modo manual: los scripts mostrarán cada prompt para pegarlo en un chat (ver comun/sin-api.md)")
    if proveedor == "mock":
        aviso("proveedor de prueba: no hay modelo real")

    if a.sin_llamada or proveedor in ("manual", "mock") or not estado["ok"]:
        if not a.sin_llamada and not estado["ok"]: aviso("no se hace la llamada de prueba hasta corregir los errores")
        return fin()

    print("3. Llamada de prueba")
    from llm import llamar
    t0 = time.time()
    try:
        r = llamar("Responde de forma muy breve.", "Responde solo con la palabra: listo", temperature=0, max_tokens=20)
    except Exception as e:
        error(f"la llamada falló: {str(e)[:300]}")
        aviso("Causas habituales: clave incorrecta o caducada, modelo mal escrito, región sin acceso al modelo, "
              "límite de peticiones del plan gratuito, o sin crédito en la cuenta.")
        return fin()
    seg = time.time() - t0
    ok(f"respuesta: {r['texto'].strip()[:60]!r}  ({r['entrada_tokens']}+{r['salida_tokens']} tokens, {seg:.1f} s)")
    base = os.environ.get("LLM_BASE_URL", "")
    if any(x in base for x in ("localhost", "127.0.0.1", ":11434")):
        ventana = ventana_ollama(base, os.environ.get("LLM_MODEL", ""))
        if ventana is not None and ventana <= 4096:
            aviso(f"Ollama tiene cargado el modelo con una ventana de contexto de solo {ventana} tokens: los prompts más largos se TRUNCAN sin error y el modelo no ve parte de "
                  "las instrucciones (afecta, por ejemplo, a los laboratorios 05B, 08B, 09B, 13B y 14). Ampliarla con OLLAMA_CONTEXT_LENGTH=16384 antes de arrancar el servidor, "
                  "o con un modelo derivado (PARAMETER num_ctx 16384). Véase laboratorios/comun/README.md, «Opción D».")
        elif ventana is not None: ok(f"ventana de contexto de Ollama: {ventana} tokens")
    if seg > 15: aviso("la latencia es alta: las suites largas tardarán; conviene usar --n para limitar los casos")
    if not r["texto"].strip() and r["salida_tokens"] >= 20:
        aviso("la respuesta ha llegado VACÍA tras gastar el límite de 20 tokens: el modelo parece de razonamiento (piensa antes de contestar). Probando con más margen…")
        os.environ["LLM_MIN_TOKENS"] = "2000"
        r = llamar("Responde de forma muy breve.", "Responde solo con la palabra: listo", temperature=0, max_tokens=20)
        if r["texto"].strip():
            aviso(f"con 2000 tokens responde ({r['salida_tokens']} tokens usados). Antes de ejecutar los laboratorios, ejecutar: export LLM_MIN_TOKENS=2000 "
                  "(en Windows: set LLM_MIN_TOKENS=2000). Si algún script sigue dando respuestas vacías, subir el valor.")
        else:
            error("el modelo sigue devolviendo respuestas vacías con 2000 tokens: probar con un valor mayor (LLM_MIN_TOKENS=4000) o con un modelo sin razonamiento.")
    if "listo" not in r["texto"].lower(): aviso("el modelo no obedeció la instrucción mínima; revisar LLM_MODEL")
    fin()


def fin():
    print("\nTodo listo: se puede empezar el laboratorio." if estado["ok"] else "\nHay errores: corregirlos antes de empezar.")
    sys.exit(0 if estado["ok"] else 1)


if __name__ == "__main__":
    main()
