"""Cliente mínimo y neutral para llamar a un modelo de lenguaje.

Solo usa la biblioteca estándar de Python (sin instalar nada).

Configuración mediante variables de entorno:

    LLM_PROVIDER   anthropic | openai | bedrock | manual | mock   (por defecto: openai)
    LLM_API_KEY    clave de la API (no necesaria con servidores locales)
    LLM_MODEL      nombre del modelo, tal como lo llama el proveedor
    LLM_REGION     (solo bedrock) región de AWS; por defecto, la configurada en AWS
    LLM_BASE_URL   (opcional) URL base. Con 'openai' sirve para cualquier
                   servidor compatible: OpenAI, Azure, Ollama
                   (http://localhost:11434/v1), LM Studio, vLLM, etc.
    LLM_MIN_TOKENS (opcional) mínimo del límite de tokens de salida de todas las llamadas. Los modelos de razonamiento gastan
                   el límite pensando y, si es bajo, devuelven la respuesta vacía: con 2000 suelen bastar.
    LLM_TIMEOUT    (opcional) segundos de espera máxima por respuesta (por defecto, 120). Con modelos locales o de razonamiento y
                   respuestas largas puede hacer falta más (por ejemplo, 600).
    LLM_RAZONAMIENTO (opcional, solo con 'openai') esfuerzo de razonamiento: no | low | medium | high. Con «no» se desactiva el
                   razonamiento en los modelos que lo permiten (por ejemplo, Gemma 4 en Ollama); es lo que hace falta para comparar
                   responder directamente con razonar paso a paso (lab. 04B).

Uso:

    from llm import llamar
    r = llamar("Eres un asistente conciso.", "Hola", temperature=0.2)
    print(r["texto"], r["entrada_tokens"], r["salida_tokens"])

El proveedor 'manual' no necesita API: muestra cada prompt, el usuario lo pega en un chat y pega aquí la respuesta
(termina con una línea que solo contenga FIN). Las respuestas se guardan en una carpeta (LLM_MANUAL_DIR, por defecto
./respuestas_manuales) y se reutilizan si se repite el mismo prompt. Véase comun/sin-api.md.

El proveedor 'mock' no hace ninguna llamada de red: devuelve lo que
indique la función registrada con `registrar_mock`. Sirve para probar el
código de los laboratorios sin gastar dinero.
"""
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

_MOCK = None


def registrar_mock(funcion):
    """Registra `funcion(system, user, **kw) -> str` para el proveedor mock."""
    global _MOCK
    _MOCK = funcion


def _post(url, cabeceras, cuerpo, reintentos=3):
    datos = json.dumps(cuerpo).encode("utf-8")
    for intento in range(reintentos):
        req = urllib.request.Request(url, data=datos, headers=cabeceras, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=float(os.environ.get("LLM_TIMEOUT", "120") or 120)) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and intento < reintentos - 1:
                time.sleep(2 ** (intento + 1))  # espera creciente
                continue
            raise RuntimeError(f"Error HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}")
        except urllib.error.URLError as e:
            if intento < reintentos - 1:
                time.sleep(2 ** (intento + 1))
                continue
            raise RuntimeError(f"Error de red: {e}")


def _manual(system, conv, temperature):
    """Modo sin API: el usuario pega el prompt en un chat y devuelve la respuesta por teclado."""
    carpeta = os.environ.get("LLM_MANUAL_DIR", "respuestas_manuales")
    os.makedirs(carpeta, exist_ok=True)
    huella = hashlib.sha1(json.dumps([system, conv], ensure_ascii=False).encode("utf-8")).hexdigest()[:16]
    ruta = os.path.join(carpeta, huella + ".txt")
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as f:
            return f.read()
    if not sys.stdin.isatty():
        raise RuntimeError("El modo manual necesita una terminal interactiva (o respuestas guardadas en " + carpeta + ").")
    print("\n" + "=" * 78)
    print("COPIAR todo lo que hay entre las líneas, PEGARLO en una conversación NUEVA del chat,")
    print("y PEGAR aquí la respuesta completa. Terminar con una línea que solo contenga FIN.")
    print("-" * 78)
    if system:
        print("[Instrucciones]\n" + system + "\n")
    for i, m in enumerate(conv):
        etiqueta = "" if len(conv) == 1 else ("[Usuario] " if m["role"] == "user" else "[Asistente] ")
        print(etiqueta + m["content"])
    print("-" * 78)
    lineas = []
    while True:
        try:
            linea = input()
        except EOFError:
            break
        if linea.strip() == "FIN":
            break
        lineas.append(linea)
    texto = "\n".join(lineas).strip()
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(texto)
    return texto


def _llamar(system, user, temperature=0.0, top_p=None, max_tokens=1024,
            mensajes=None, modelo=None, proveedor=None):
    """Llama al modelo y devuelve un diccionario:

    {"texto": str, "entrada_tokens": int, "salida_tokens": int,
     "latencia_s": float, "modelo": str}

    `mensajes` permite pasar una conversación completa como lista de
    {"role": "user"|"assistant", "content": str}; si se indica, `user` se
    ignora.
    """
    proveedor = (proveedor or os.environ.get("LLM_PROVIDER", "openai")).lower()
    modelo = modelo or os.environ.get("LLM_MODEL", "")
    clave = os.environ.get("LLM_API_KEY", "")
    base = os.environ.get("LLM_BASE_URL", "")
    conv = mensajes if mensajes is not None else [{"role": "user", "content": user}]
    t0 = time.time()

    if proveedor == "manual":
        texto = _manual(system, conv, temperature)
        return {"texto": texto, "entrada_tokens": len(system + str(conv)) // 4,
                "salida_tokens": len(texto) // 4, "latencia_s": 0.0, "modelo": "manual"}

    if proveedor == "mock":
        if _MOCK is None:
            raise RuntimeError("Proveedor mock sin función registrada (registrar_mock).")
        texto = _MOCK(system, conv[-1]["content"], mensajes=conv, temperature=temperature)
        return {"texto": texto, "entrada_tokens": len(system + str(conv)) // 4,
                "salida_tokens": len(texto) // 4, "latencia_s": 0.0, "modelo": "mock"}

    if not modelo:
        raise RuntimeError("Falta LLM_MODEL (nombre del modelo).")

    if proveedor == "anthropic":
        url = (base or "https://api.anthropic.com") + "/v1/messages"
        cab = {"content-type": "application/json", "x-api-key": clave,
               "anthropic-version": "2023-06-01"}
        cuerpo = {"model": modelo, "max_tokens": max_tokens, "system": system,
                  "messages": conv, "temperature": temperature}
        if top_p is not None:
            cuerpo["top_p"] = top_p
        r = _post(url, cab, cuerpo)
        texto = "".join(b.get("text", "") for b in r.get("content", []))
        uso = r.get("usage", {})
        return {"texto": texto, "entrada_tokens": uso.get("input_tokens", 0),
                "salida_tokens": uso.get("output_tokens", 0),
                "latencia_s": round(time.time() - t0, 2), "modelo": modelo}

    if proveedor == "openai":
        url = (base or "https://api.openai.com/v1").rstrip("/") + "/chat/completions"
        cab = {"content-type": "application/json"}
        if clave:
            cab["authorization"] = f"Bearer {clave}"
        msgs = ([{"role": "system", "content": system}] if system else []) + conv
        cuerpo = {"model": modelo, "messages": msgs, "temperature": temperature,
                  "max_tokens": max_tokens}
        if top_p is not None:
            cuerpo["top_p"] = top_p
        razon = os.environ.get("LLM_RAZONAMIENTO", "").strip().lower()
        if razon:
            cuerpo["reasoning_effort"] = "none" if razon in ("no", "none", "off", "0", "false") else razon
        r = _post(url, cab, cuerpo)
        texto = r["choices"][0]["message"]["content"] or ""
        uso = r.get("usage", {})
        return {"texto": texto, "entrada_tokens": uso.get("prompt_tokens", 0),
                "salida_tokens": uso.get("completion_tokens", 0),
                "latencia_s": round(time.time() - t0, 2), "modelo": modelo}

    if proveedor == "bedrock":
        # Amazon Bedrock mediante la API Converse. Requiere `pip install boto3` y credenciales de AWS.
        try:
            import boto3
        except ImportError:
            raise RuntimeError("El proveedor bedrock necesita boto3 (pip install boto3).")
        cliente = boto3.client("bedrock-runtime", region_name=os.environ.get("LLM_REGION") or None)
        cfg = {"temperature": temperature, "maxTokens": max_tokens}
        if top_p is not None:
            cfg["topP"] = top_p
        args = {"modelId": modelo, "messages": [{"role": m["role"], "content": [{"text": m["content"] or " "}]} for m in conv],
                "inferenceConfig": cfg}
        if system:
            args["system"] = [{"text": system}]
        for intento in range(4):
            try:
                r = cliente.converse(**args)
                break
            except Exception as e:  # limitación de ritmo o fallo transitorio
                if intento < 3 and any(x in str(e) for x in ("Throttling", "ServiceUnavailable", "ModelTimeout", "InternalServer")):
                    time.sleep(2 ** (intento + 1)); continue
                raise RuntimeError(f"Error de Bedrock: {e}")
        texto = "".join(b.get("text", "") for b in r["output"]["message"]["content"])
        uso = r.get("usage", {})
        return {"texto": texto, "entrada_tokens": uso.get("inputTokens", 0), "salida_tokens": uso.get("outputTokens", 0),
                "latencia_s": round(time.time() - t0, 2), "modelo": modelo}

    raise RuntimeError(f"Proveedor desconocido: {proveedor}")


_AVISADO = False
_AVISADO_VENTANA = False


def llamar(system, user, temperature=0.0, top_p=None, max_tokens=1024,
           mensajes=None, modelo=None, proveedor=None, exacto=False):
    """Llama al modelo y devuelve un diccionario:

    {"texto": str, "entrada_tokens": int, "salida_tokens": int,
     "latencia_s": float, "modelo": str}

    `mensajes` permite pasar una conversación completa como lista de
    {"role": "user"|"assistant", "content": str}; si se indica, `user` se
    ignora.

    Modelos de razonamiento: gastan parte del límite de tokens «pensando» antes de contestar, y con un límite bajo la respuesta
    llega vacía. La variable de entorno LLM_MIN_TOKENS fija un mínimo para el límite de todas las llamadas (por ejemplo,
    export LLM_MIN_TOKENS=2000) sin tocar los scripts. Si una respuesta llega vacía porque ha agotado el límite, se avisa una vez.
    Con `exacto=True` el límite se respeta tal cual, sin aplicar ese mínimo (para experimentos que varían el límite a propósito).

    Si el servidor es local y los tokens de entrada coinciden con una ventana típica (2048 o 4096), se avisa una vez: es la señal de que el
    prompt ha podido truncarse (véase comun/README.md, «Opción D»).
    """
    global _AVISADO, _AVISADO_VENTANA
    try:
        piso = int(os.environ.get("LLM_MIN_TOKENS", "0") or 0)
    except ValueError:
        piso = 0
    limite = max_tokens if exacto else max(max_tokens, piso)
    r = _llamar(system, user, temperature, top_p, limite, mensajes, modelo, proveedor)
    base = os.environ.get("LLM_BASE_URL", "")
    if (not _AVISADO_VENTANA and r.get("entrada_tokens") in (2048, 4096) and (proveedor or os.environ.get("LLM_PROVIDER", "openai")).lower() == "openai"
            and any(x in base for x in ("localhost", "127.0.0.1", ":11434"))):
        _AVISADO_VENTANA = True
        print(f"AVISO: el prompt ha ocupado exactamente {r['entrada_tokens']} tokens de entrada, el tamaño de la ventana de contexto por defecto de muchos servidores "
              "locales (Ollama usa 4096): lo más probable es que el servidor haya TRUNCADO el prompt sin avisar y el modelo no vea parte de las instrucciones. "
              "Ampliar la ventana (OLLAMA_CONTEXT_LENGTH=16384 o un modelo derivado con num_ctx; véase laboratorios/comun/README.md, «Opción D»).", file=sys.stderr)
    if not _AVISADO and not str(r.get("texto", "")).strip() and r.get("salida_tokens", 0) >= limite > 0:
        _AVISADO = True
        sugerido = 2000 if limite < 2000 else limite * 2
        print(f"AVISO: el modelo ha devuelto una respuesta VACÍA tras agotar el límite de {limite} tokens de salida. Es lo que ocurre con los modelos de "
              "razonamiento: gastan el límite pensando y no llegan a escribir la respuesta. Subir el límite para todos los scripts con "
              f"export LLM_MIN_TOKENS={sugerido} (en Windows, set LLM_MIN_TOKENS={sugerido}) o usar un modelo sin razonamiento.", file=sys.stderr)
    return r


AYUDA = """\
Cliente mínimo para llamar a un modelo de lenguaje desde la terminal o desde otro script de Python.

Sin opciones, envía la pregunta tal cual. Para separar las instrucciones y el contexto de la pregunta:
  --system / --system-archivo   instrucciones (y contexto de referencia) que van aparte del mensaje del usuario
  --contexto-archivo            fichero cuyo contenido se pega antes de la pregunta, entre <contexto> y </contexto>

Configuración (variables de entorno):
  LLM_PROVIDER   anthropic | openai | bedrock | manual | mock   (por defecto: openai)
  LLM_API_KEY    clave de la API (no hace falta con servidores locales)
  LLM_MODEL      nombre del modelo, tal como lo llama el proveedor
  LLM_REGION     (solo bedrock) región de AWS
  LLM_BASE_URL   (opcional) URL base; con 'openai' sirve para Ollama, LM Studio, vLLM, Azure, etc.
  LLM_MANUAL_DIR (solo manual) carpeta donde se guardan las respuestas pegadas a mano
  LLM_MIN_TOKENS (opcional) mínimo del límite de tokens de salida; útil con modelos de razonamiento (por ejemplo, 2000)
  LLM_TIMEOUT    (opcional) segundos de espera máxima por respuesta (por defecto, 120); subirlo con modelos locales lentos
  LLM_RAZONAMIENTO (opcional, solo 'openai') no | low | medium | high: esfuerzo de razonamiento; «no» lo desactiva si el modelo lo permite

Ejemplos:
  python llm.py "Responde solo con la palabra: listo"
  python llm.py --system "Eres un asistente conciso." "¿Qué es un token?"
  python llm.py --contexto-archivo datos/registro_de_cambios.md "¿Cuál es la referencia de la entrada 3.5.1?"
  python llm.py --proveedor manual "Resume en una frase qué es la temperatura"
  python llm.py --json --temperatura 0.7 "Dame un eslogan"

Desde Python (la misma función que usan los laboratorios):
  from llm import llamar
  r = llamar(system, user, temperature=0.0, top_p=None, max_tokens=1024, mensajes=None)
  # r = {"texto", "entrada_tokens", "salida_tokens", "latencia_s", "modelo"}
  # `mensajes` es una conversación completa, [{"role": "user"|"assistant", "content": "..."}, ...];
  # si se indica, `user` se ignora y `system` se sigue enviando aparte.

Si la pregunta empieza por un guion, escribirla después de «--». Más información: comun/README.md y comun/sin-api.md.
"""


def _main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(prog="python llm.py", description="Llama a un modelo de lenguaje y muestra la respuesta.",
                                 epilog=AYUDA, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pregunta", nargs="*", help="texto de la pregunta (por defecto, una prueba mínima)")
    ap.add_argument("--system", default="Responde de forma breve.", help="instrucciones del sistema (por defecto: «Responde de forma breve.»)")
    ap.add_argument("--system-archivo", metavar="FICHERO", help="leer las instrucciones del sistema de un fichero (sustituye a --system)")
    ap.add_argument("--contexto-archivo", metavar="FICHERO", help="pegar el contenido del fichero antes de la pregunta, entre <contexto> y </contexto>")
    ap.add_argument("--temperatura", type=float, default=0.0, help="temperatura (por defecto 0)")
    ap.add_argument("--top-p", type=float, default=None, help="top-p (por defecto, el del proveedor)")
    ap.add_argument("--max-tokens", type=int, default=1024, help="máximo de tokens de salida (por defecto 1024)")
    ap.add_argument("--proveedor", help="anthropic, openai, bedrock, manual o mock (sustituye a LLM_PROVIDER)")
    ap.add_argument("--modelo", help="modelo (sustituye a LLM_MODEL)")
    ap.add_argument("--json", action="store_true", help="mostrar el diccionario completo en lugar de solo el texto")
    a = ap.parse_args(argv)
    system = open(a.system_archivo, encoding="utf-8").read() if a.system_archivo else a.system
    pregunta = " ".join(a.pregunta) or "Responde solo con la palabra: listo"
    if a.contexto_archivo:
        pregunta = "<contexto>\n" + open(a.contexto_archivo, encoding="utf-8").read().strip() + "\n</contexto>\n\n" + pregunta
    r = llamar(system, pregunta, temperature=a.temperatura, top_p=a.top_p, max_tokens=a.max_tokens, modelo=a.modelo, proveedor=a.proveedor)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        print(r["texto"])
        print(f"\n[tokens de entrada: {r['entrada_tokens']} · de salida: {r['salida_tokens']} · {r['latencia_s']} s · {r['modelo']}]", file=sys.stderr)


if __name__ == "__main__":
    _main()
