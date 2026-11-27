[← Laboratorios](../README.md)

# Guía de los laboratorios

> ¿Primer laboratorio? Lee antes [Antes de empezar](antes-de-empezar.md): cómo trabajar con un chat y con las hojas de cálculo, y cómo se lee un laboratorio. Esta guía es la técnica: sirve sobre todo para el camino con código.

## 1. Cómo funcionan

- No hay nada que entregar y los laboratorios no se evalúan. El guiado (A) de cada módulo y el proyecto final forman parte de las 30 horas del curso; el abierto (B) es opcional. El objetivo es practicar, equivocarse sin consecuencias y comprobar con datos reales lo que explican los módulos.
- Los módulos se numeran del 01 al 13 y se agrupan en cinco partes. Cada módulo tiene dos laboratorios, que llevan el número del módulo y una letra: la A es la guiada (consolida los conceptos con una tarea paso a paso) y la B la abierta (aplica los conceptos a un caso con más margen). Los módulos 10, 11 y 12 tienen además un tercero, el C, opcional y complementario. El último, el [laboratorio 14](../14/README.md), es el proyecto integrador y reúne todo el curso.
- Todos usan el mismo caso: Altanoria Software S.L., empresa ficticia de soluciones de software con IA generativa (véase [su perfil](empresa/altanoria.md)). Sus clientes, tickets, facturas y documentos son sintéticos; no hay datos reales.
- Cada laboratorio es un único documento (`README.md`) con siete apartados: título, ficha «De un vistazo», justificación del laboratorio, objetivos, recursos necesarios, pasos de ejecución y conclusiones. Los pasos están explicados al detalle para perfiles no técnicos y, en los laboratorios que usan scripts, cada paso incluye también la alternativa con código, plegada dentro del propio paso.
- Los pasos indican su duración (entre 45 y 100 minutos por laboratorio, siempre en múltiplos de 5, según el caso) y terminan con una comprobación.
- Las conclusiones incluyen un resumen de lo conseguido, la referencia de qué esperar, las preguntas de reflexión con su respuesta plegada, una autoevaluación y la solución de referencia. Conviene abrir la solución solo tras haber intentado el laboratorio: la mayor parte del aprendizaje está en el intento, también cuando no sale bien.
- **No hay nada que entregar**: los laboratorios no los corrige ni los evalúa nadie. Las tablas, informes y ficheros que piden las tareas son material de trabajo propio; conviene guardarlos (por ejemplo, en una carpeta local) para comparar versiones y repasar.

## 2. Qué se necesita

| Tipo de laboratorio | Qué hace falta |
|---|---|
| Solo chat (01B, 02A, 02B, 03A, 05A, 08A, 10A, 10B, 10C, 11C y 12B) | Un asistente de chat cualquiera (de pago o gratuito) y un editor de texto. El 11C trae además un comprobador que se abre en el navegador. |
| Con scripts opcionales (01A, 03B, 04, 05B, 06, 07, 08B, 09, 11, 12, 13 y el proyecto 14) | Python 3.9 o superior, una terminal y acceso a un modelo por API (o un modelo local). Los scripts no necesitan instalar paquetes. |

Los laboratorios con scripts tienen una alternativa sin API: usar un chat, el modo manual de los scripts, un modelo local o un plan gratuito. La [guía para trabajar sin API](sin-api.md) explica cada camino y cuál conviene a cada laboratorio.

Si algo no funciona al ejecutar un script, la guía [Si algo falla](si-algo-falla.md) explica los problemas más frecuentes (respuestas vacías, tiempos de espera, contexto truncado) y cómo arreglarlos.

### Cómo copiar un fichero del repositorio

Algunos pasos piden copiar el contenido de un fichero (un prompt, una especificación, un acta) y pegarlo en un chat. Se abre el enlace, se pulsa «Raw» si se muestra con formato, se selecciona todo (Ctrl+A en Windows, Cmd+A en Mac) y se copia (Ctrl+C o Cmd+C). Quien haya descargado el repositorio puede abrir el fichero con el Bloc de notas o con TextEdit y copiar de la misma manera.

### Preparar el entorno para el camino con código

Hace falta Python 3.9 o superior y acceso a un modelo por API (véase más abajo la configuración). Antes de empezar un laboratorio con scripts se comprueba el entorno con `python ../comun/comprobar_entorno.py`, ejecutado desde la carpeta del laboratorio. Si el modelo es de razonamiento y las respuestas llegan vacías, la sección «Modelos de razonamiento» explica cómo darle margen con `LLM_MIN_TOKENS`.

## 3. Configurar el acceso a un modelo

Los scripts usan el cliente [`llm.py`](llm.py), que solo depende de la biblioteca estándar de Python. Se configura con variables de entorno.

### Opción A · Cualquier proveedor compatible con la API de OpenAI

```bash
export LLM_PROVIDER=openai
export LLM_API_KEY="tu-clave"
export LLM_MODEL="nombre-del-modelo"
# opcional, para otros servidores compatibles:
# export LLM_BASE_URL="https://tu-servidor/v1"
```

### Opción B · Anthropic

```bash
export LLM_PROVIDER=anthropic
export LLM_API_KEY="tu-clave"
export LLM_MODEL="nombre-del-modelo"
```

### Opción C · Amazon Bedrock

```bash
pip install boto3                      # única dependencia opcional del curso
export LLM_PROVIDER=bedrock
export LLM_MODEL="us.amazon.nova-2-lite-v1:0"   # ejemplo; usar un identificador o perfil de inferencia disponible en la región
export LLM_REGION="us-east-1"                   # opcional
```

Usa la API Converse con las credenciales de AWS que haya configuradas (`aws configure` o variables de entorno). Las soluciones de los laboratorios incluyen resultados medidos con este modelo.

### Opción D · Modelo local (Ollama, LM Studio, vLLM…)

```bash
export LLM_PROVIDER=openai
export LLM_BASE_URL="http://localhost:11434/v1"   # ejemplo con Ollama
export LLM_MODEL="nombre-del-modelo-local"
# no hace falta clave
```

**Con Ollama, ampliar la ventana de contexto.** Ollama carga los modelos con una ventana de solo 4.096 tokens y, si el prompt es más largo, **lo trunca sin avisar**: el modelo no ve parte de las instrucciones y las respuestas salen mal sin ningún error. Lo sufren los laboratorios con documentos largos (por ejemplo, el 05B, con el catálogo, el SLA y las condiciones dentro del prompt de sistema, que ocupan unos 4.600 tokens). Para detectarlo, `python comun/llm.py` imprime los tokens de entrada: si coinciden con 4096, el prompt se ha cortado. La solución es ampliar la ventana, con una de estas dos opciones:

- Definir la variable de entorno del servidor antes de arrancarlo: `OLLAMA_CONTEXT_LENGTH=16384` (en Windows, como variable de entorno del sistema y reiniciando Ollama).
- Crear un modelo derivado con una ventana mayor. Con un fichero `Modelfile` que contenga `FROM nombre-del-modelo` y `PARAMETER num_ctx 16384`, ejecutar `ollama create nombre-16k -f Modelfile` y usar `LLM_MODEL=nombre-16k`.

Una ventana de 16.384 tokens basta para todos los laboratorios salvo el 01A con los documentos largos.

En Windows (PowerShell) se usa `$env:LLM_API_KEY="tu-clave"` en lugar de `export`.

### Comprobar que funciona

```bash
python comun/comprobar_entorno.py
```

Revisa la versión de Python, las variables de entorno del proveedor elegido y hace una llamada mínima al modelo (una fracción de céntimo), con la latencia medida y pistas si algo falla. Con `--sin-llamada` solo revisa lo local. También se puede llamar directamente al cliente:

```bash
python comun/llm.py "Responde solo con la palabra: listo"
```

Debe mostrar el texto de la respuesta y, debajo, el número de tokens de entrada y salida. `python comun/llm.py --help` explica todas las opciones, incluidas las que separan las instrucciones y el contexto de la pregunta (`--system`, `--contexto-archivo`) y las variables de entorno.

### Modelos de razonamiento: respuestas vacías

Los modelos de razonamiento gastan parte del límite de tokens «pensando» antes de contestar. Si el límite que fija un script es bajo (por ejemplo, 80 o 500), el modelo puede agotarlo sin escribir nada y la respuesta llega **vacía**: en los laboratorios se nota porque el JSON no se puede leer, las métricas salen a cero o la exactitud baja al añadir ejemplos.

- `python comun/comprobar_entorno.py` lo detecta: si la respuesta de prueba llega vacía, lo avisa y comprueba si con más margen responde.
- La solución, sin tocar ningún script, es fijar un mínimo para el límite de todas las llamadas:

```bash
export LLM_MIN_TOKENS=2000      # en Windows: set LLM_MIN_TOKENS=2000
```

- Si aun así llegan respuestas vacías, subir el valor (4000) o usar un modelo sin razonamiento, que además es más barato para estas tareas.
- Con un modelo local lento o con respuestas largas puede saltar `TimeoutError: timed out`, porque el cliente espera 120 segundos como máximo por respuesta. Se amplía con `export LLM_TIMEOUT=600` (en Windows, `set LLM_TIMEOUT=600`).
- Con un modelo sin razonamiento no hace falta nada: el límite es solo un tope y no cambia lo que responde ni lo que cuesta.
- Algunos modelos de razonamiento permiten desactivar el razonamiento (por ejemplo, Gemma 4 en Ollama). Con `LLM_RAZONAMIENTO=no` el cliente envía `reasoning_effort: none` y el modelo contesta sin pensar antes (solo con `LLM_PROVIDER=openai`). Es lo que hace falta en el laboratorio 04B para que «responder directamente» y «razonar paso a paso» se puedan comparar:

```bash
export LLM_RAZONAMIENTO=no      # en Windows: set LLM_RAZONAMIENTO=no
```

### Cuánto tardan los scripts

El tiempo depende sobre todo del modelo. Un modelo local de razonamiento tarda mucho más que una API rápida sin razonamiento: con Gemma 4 de 8 B en local, los 45 mensajes del proyecto final tardan cerca de una hora y la curva completa del laboratorio 04A, unos 40 minutos. Cada laboratorio con código indica en «Recursos necesarios» el tiempo orientativo de sus ejecuciones. Para probar sin esperar, casi todos los scripts aceptan `--n` (usar solo los n primeros casos), y los que repiten medidas, `--repeticiones`.

### Cuántos tokens se gastan

El coste de un laboratorio es `tokens de entrada × precio de entrada + tokens de salida × precio de salida`, con los precios de cada proveedor (cambian: consultarlos en su página). Estos volúmenes se midieron con los datos de los laboratorios y sirven para estimar el gasto:

| Ejecución | Tokens aproximados |
|---|---|
| 07A/L2: una versión del prompt sobre los 60 casos de desarrollo | de 8.000 (v0) a 43.000 (v3) de entrada y unos 1.600 de salida |
| 07B: evaluación final sobre los 120 casos de prueba | unos 86.000 de entrada y 3.200 de salida |
| 04A: una serie sobre los 132 tickets de prueba | 24.000 (0 ejemplos), 75.000 (8) y 133.000 (16) de entrada; con `--repeticiones 3`, el triple |
| 04B: autoconsistencia con 5 muestras sobre 30 problemas | unos 52.000 de salida |
| 13A: cadena completa sobre los 25 partes | unos 39.000 en total |

Con un modelo pequeño, cualquiera de estas ejecuciones cuesta pocos céntimos. Para gastar menos: limitar los casos con `--n`, probar primero con pocos casos y no repetir ejecuciones idénticas. Si el proveedor es gratuito, el límite suele ser el número de peticiones por minuto, no el dinero (véase `--pausa`).

### Reglas de seguridad al usar claves

- **Nunca escribir la clave** en un fichero que se vaya a compartir ni subirla a ningún repositorio.
- Usar variables de entorno o un gestor de secretos.
- Establecer un **límite de gasto** en el panel del proveedor antes de lanzar series de llamadas.
- Los laboratorios están pensados para costar poco: los conjuntos de datos son pequeños y la mayoría de las ejecuciones se pueden reducir con `--n 10`. Aun así, conviene revisar el coste después de cada ejecución larga.

### Probar el código sin gastar nada

El proveedor `mock` no hace llamadas de red: ejecuta una función simulada que se registra con `llm.registrar_mock`. Sirve para ver cómo funciona un script antes de usar un modelo real, aunque los resultados no tienen ningún valor.

## 4. Datos y utilidades comunes

Todos los scripts de los laboratorios tienen ayuda en línea: `python nombre_del_script.py --help` explica qué hace, cada opción (con su valor por defecto) y muestra ejemplos.

| Fichero | Para qué sirve |
|---|---|
| [`llm.py`](llm.py) | Cliente mínimo y neutral de modelos de lenguaje. |
| [`utiles.py`](utiles.py) | Lectura de CSV/JSONL, validación de JSON contra un esquema, métricas de clasificación, recuento aproximado de tokens. |
| [`comprobar_entorno.py`](comprobar_entorno.py) | Comprueba Python, variables y una llamada mínima antes de empezar. |
| [`sin-api.md`](sin-api.md) | Cómo hacer los laboratorios sin acceso a una API. |
| [`si-algo-falla.md`](si-algo-falla.md) | Qué hacer ante los errores más frecuentes al ejecutar los scripts. |
| [`ejecutar_suite.py`](ejecutar_suite.py) | Ejecuta un prompt sobre un conjunto de casos y calcula métricas (módulo 07 y siguientes). Con `--repeticiones N` informa de la media y el rango. |
| [`comparar_ejecuciones.py`](comparar_ejecuciones.py) | Compara dos ejecuciones y detecta regresiones. |
| [`empresa/`](empresa/altanoria.md) | Documentos de Altanoria: planes, SLA, condiciones, privacidad, glosario. |

## 5. Buenas costumbres de trabajo

1. Anotar todo: versión del prompt, modelo, temperatura, fecha y resultado. Sin registro no se puede comparar.
2. Un cambio cada vez (módulo 07): si se cambian dos cosas a la vez no se sabe cuál produjo el efecto.
3. Separar desarrollo y prueba: los conjuntos «dev» sirven para ajustar; los «test» se usan al final y no se tocan.
4. Verificar con una fuente, no con la fluidez del texto (módulo 08).
5. **No pegar datos personales reales** en ningún modelo (módulo 09). Los datos de los laboratorios son ficticios; los propios, no.
6. Repetir antes de concluir: con pocos casos, una sola ejecución puede dar un resultado que no se repite. Usar `--repeticiones 3` y comparar rangos, no puntos sueltos.
7. Los modelos y sus interfaces cambian: si un nombre de parámetro o de modelo ha cambiado, consultar la documentación del proveedor.

## 6. Qué se ha comprobado con un modelo real

Los laboratorios con scripts se ejecutaron el 23 y el 24 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada a 16.384 tokens (131.072 en el 01A), y los resultados se incluyen, marcados como tales, en la sección de solución de cada uno: 01A, 01B, 02A, 02B, 03B, 04A, 04B, 05B, 06A, 06B, 07A, 07B, 08B, 09B, 11A, 11B, 12A, 13A, 13B y el integrador. Esa prueba detectó y permitió corregir varios defectos en los propios materiales y en el entorno: un extractor de respuestas demasiado frágil, un inyector de fallos que no inyectaba, una ventana de contexto de Ollama que truncaba los prompts largos sin avisar, respuestas vacías de un modelo de razonamiento con límites de tokens bajos, un contraste entre «directo» y «paso a paso» que desaparecía con un modelo de razonamiento (de ahí `LLM_RAZONAMIENTO`) y un tiempo de espera de 120 segundos que se quedaba corto con un modelo local (de ahí `LLM_TIMEOUT`). Los laboratorios 03A, 05A, 08A, 09A, 10A, 10B y 12B se basan en el chat y no se han medido de forma automática: sus soluciones son referencias razonadas.

## 7. Sobre los resultados

Los modelos de lenguaje no son deterministas y cada proveedor ofrece modelos distintos que evolucionan. Por eso las soluciones no dan cifras exactas de lo que debe salir en cada ejecución, sino rangos orientativos, criterios para valorar el resultado y los errores típicos. Si los resultados propios difieren, no es un fallo: es el material de análisis del laboratorio.
