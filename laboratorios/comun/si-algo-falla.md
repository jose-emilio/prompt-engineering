[← Laboratorios](../README.md) · [Guía de los laboratorios](README.md)

# Si algo falla

Esta guía reúne los problemas que aparecen de verdad al hacer los laboratorios con código, ordenados por lo que se ve en pantalla. Cada uno indica qué significa y cómo arreglarlo. Los laboratorios que se hacen solo con un chat y una hoja de cálculo no necesitan nada de esto: solo el apartado final.

Antes de buscar el síntoma, conviene ejecutar `python comun/comprobar_entorno.py` desde la carpeta de laboratorios: detecta los fallos más frecuentes (sin conexión, clave incorrecta, respuestas vacías) y dice qué variable ajustar.

## El script no consigue conectar con el modelo

Se ve `URLError`, `Connection refused`, `Error HTTP 401` o `Error HTTP 404`.

- `Connection refused`: el servidor no está en marcha (por ejemplo, Ollama no está abierto) o `LLM_BASE_URL` apunta a otra dirección. Con Ollama, la URL es `http://localhost:11434/v1`.
- `Error HTTP 401`: la clave de `LLM_API_KEY` falta o es incorrecta. Con un servidor local basta una clave cualquiera.
- `Error HTTP 404`: el nombre de `LLM_MODEL` no existe en ese servidor. Con Ollama, `ollama list` muestra los nombres exactos.
- Con `LLM_PROVIDER=bedrock` hace falta `pip install boto3` y credenciales de AWS configuradas.

## La respuesta llega vacía

Se ve un aviso del cliente («respuesta vacía»), el JSON no se puede leer o las métricas salen a cero.

Los modelos de razonamiento gastan el límite de tokens «pensando» antes de contestar. Si el script fija un límite bajo, se agota sin escribir nada.

```bash
export LLM_MIN_TOKENS=2000      # en Windows: set LLM_MIN_TOKENS=2000
```

Si aun así llegan vacías, subir el valor a 4000 o usar un modelo sin razonamiento.

## `TimeoutError: timed out`

El cliente espera como máximo 120 segundos por respuesta. Con un modelo local lento o con respuestas largas puede quedarse corto:

```bash
export LLM_TIMEOUT=600          # en Windows: set LLM_TIMEOUT=600
```

## El modelo local ignora las instrucciones o responde cosas sin sentido con prompts largos

Ollama carga los modelos con una ventana de solo 4.096 tokens y, si el prompt es más largo, **lo trunca sin avisar**: el modelo no ve parte de las instrucciones. Se nota porque `python comun/llm.py` muestra **4096 tokens de entrada**, justo el tamaño de la ventana.

- Definir `OLLAMA_CONTEXT_LENGTH=16384` antes de arrancar el servidor, o
- crear un modelo derivado con `PARAMETER num_ctx 16384` (véase la [guía](README.md#opción-d--modelo-local-ollama-lm-studio-vllm)).

Con documentos muy largos (laboratorio 01A) hay que comprobar además que el texto cabe en la ventana del modelo: si no cabe, el servidor lo corta y el modelo falla sin decir por qué.

## La comparación entre «responder directamente» y «razonar paso a paso» sale igual

Pasa en el laboratorio 04B con un modelo de razonamiento: piensa antes de contestar aunque se le pida «sin explicar». Si el modelo lo permite, hay que desactivar ese razonamiento para ver el contraste:

```bash
export LLM_RAZONAMIENTO=no      # en Windows: set LLM_RAZONAMIENTO=no
```

## `Error HTTP 429` o `503`

El proveedor limita las peticiones o está saturado. El cliente reintenta tres veces con espera creciente. Si persiste, añadir una pausa entre llamadas con `--pausa 2` (en los scripts que la admiten, como `ejecutar_suite.py`) o repetir pasado un rato.

## El JSON no es válido o hay muchas respuestas «truncadas»

- La respuesta llega envuelta en un bloque de código o con texto alrededor: es un fallo del prompt (falta «responde únicamente con el JSON»), no del script.
- El script avisa de las respuestas truncadas: el modelo se quedó sin tokens antes de terminar. Subir `--max-tokens` o `LLM_MIN_TOKENS`.

## Mis resultados no se parecen a los de la solución

Es normal y forma parte del laboratorio:

- Los modelos no son deterministas ni siquiera con temperatura 0, y los de razonamiento menos.
- Cada solución indica con qué modelo se midió. Otro modelo da otros números.
- Una diferencia de pocos puntos con pocos casos es ruido. Se repite con `--repeticiones 3` y se compara el rango, no un punto.
- Lo que se valora no es acercarse a la cifra, sino explicar por qué difiere.

## Python y el terminal

- La versión mínima es Python 3.9. En algunos sistemas el comando es `python3` en lugar de `python`.
- Las variables de entorno se definen con `export NOMBRE=valor` en macOS y Linux, y con `set NOMBRE=valor` (cmd) o `$env:NOMBRE="valor"` (PowerShell) en Windows. Duran lo que dura la ventana del terminal.
- Los scripts se ejecutan desde la carpeta del laboratorio, no desde la raíz del repositorio.

## No tengo acceso a una API o no puedo usar Python

Hay un camino sin API ([guía](sin-api.md)) y otro sin Python ([guía](sin-python.md)). Todos los laboratorios se pueden hacer con un chat y la hoja de cálculo.

## La hoja de cálculo

- Las columnas con las respuestas correctas están ocultas y agrupadas a propósito. Se muestran solo en el paso que lo indica, con el botón de grupo (+) de la cabecera.
- Si una fórmula no calcula, comprobar que el archivo se ha abierto con una hoja de cálculo completa (Excel o LibreOffice) y no con una vista previa.
