[← Laboratorios](../README.md) · [Guía de los laboratorios](README.md)

# Hacer los laboratorios sin acceso a una API

Muchos laboratorios se pueden hacer con un simple chat. Los que incluyen scripts están pensados para automatizar mediciones con una API, pero no es imprescindible tenerla. Hay cuatro caminos, de menos a más esfuerzo de instalación.

## Camino 1 · Chat web (gratuito o de pago)

Sirve para todos los laboratorios de la columna «Chat» de la tabla del final y, con lotes pequeños, para los de scripts.

- Abrir una conversación nueva para cada prueba (el contexto previo contamina los resultados).
- Para evaluar muchos casos con un solo mensaje, pegar lotes de 8 a 10 casos numerados y pedir una lista JSON con un objeto por caso. Es más rápido que caso a caso, aunque la calidad puede bajar un poco con lotes grandes.
- Los scripts que no llaman al modelo funcionan igual sin API: `validar_json.py`, `evaluar_extraccion.py`, `comprobar.py` (11A), los `unittest` de 11B, `comprobar.js` y `comprobar.html` (11C), `contar_tokens.py`, `detectar_pii.py` y `evaluar_integrador.py`. Basta guardar las respuestas del chat en el formato JSONL que cada script indica en su cabecera.
- Los chats no permiten fijar la temperatura ni el top-p. Para 06B hay que medir solo la variabilidad natural (repetir la misma petición 10 veces) o usar el Camino 3.

## Camino 2 · Modo manual de los scripts (sin API, con terminal)

Los scripts de los laboratorios admiten un proveedor `manual`: muestran cada prompt, se pega en el chat y se devuelve la respuesta por teclado.

```bash
export LLM_PROVIDER=manual
python ../comun/ejecutar_suite.py --prompt prompts/prompt_v0.txt --datos datos/reclamaciones_dev.csv \
       --campos categoria prioridad --etiqueta v0 --n 15
```

Para cada caso aparece un bloque entre líneas: copiarlo completo, pegarlo en una conversación nueva del chat, copiar la respuesta, pegarla en la terminal y terminar con una línea que solo contenga `FIN`.

- Las respuestas se guardan en `respuestas_manuales/` (o en la carpeta de `LLM_MANUAL_DIR`). Si se repite el mismo prompt, se reutiliza la respuesta guardada y no hay que volver a pegar nada. Así se puede interrumpir y continuar.
- Es lento: usar `--n 10` a `--n 20`. Con 15 casos ya se ven las tendencias.
- Si el script llama al modelo con una conversación de varios turnos, el bloque muestra cada mensaje con su etiqueta.
- No sirve para los laboratorios que requieren cientos de llamadas (13A, 13B y el 14 completos): para ellos, usar el Camino 3 o reducir a 3–5 casos.

## Camino 3 · Modelo local (gratuito, sin conexión)

Un modelo pequeño ejecutado en el propio ordenador permite usar todos los scripts, la temperatura y el top-p, sin coste por llamada.

1. Instalar una herramienta de ejecución local (por ejemplo, Ollama o LM Studio). Ambas ofrecen una API compatible con la de OpenAI.
2. Descargar un modelo «instruct» pequeño de una familia abierta (Llama, Qwen, Gemma, Mistral…). Orientación por memoria disponible:

| Memoria libre (RAM o VRAM) | Tamaño de modelo razonable |
|---|---|
| 8 GB | 3–4 mil millones de parámetros |
| 16 GB | 7–9 mil millones |
| 32 GB o más | 12–32 mil millones |

3. Configurar los scripts (ejemplo con Ollama):

```bash
export LLM_PROVIDER=openai
export LLM_BASE_URL="http://localhost:11434/v1"
export LLM_MODEL="nombre-del-modelo-descargado"
python llm.py "Responde solo con la palabra: listo"
```

4. **Ampliar la ventana de contexto.** Ollama carga los modelos con solo 4.096 tokens y, si el prompt es más largo, lo trunca sin avisar: el modelo no ve parte de las instrucciones y las respuestas salen mal sin ningún error. Los laboratorios con documentos largos (05B, 08B, 09B, 13B y 14) lo sufren. Se amplía definiendo `OLLAMA_CONTEXT_LENGTH=16384` antes de arrancar el servidor, o con un modelo derivado (véase la [guía](README.md#opción-d--modelo-local-ollama-lm-studio-vllm)). `python comun/comprobar_entorno.py` avisa si la ventana es de 4.096 tokens.
5. Con un modelo de razonamiento (por ejemplo, Gemma 4), añadir `LLM_MIN_TOKENS=2000` y, si hay tiempos de espera, `LLM_TIMEOUT=600`. Si algo falla, véase [Si algo falla](si-algo-falla.md).

Los modelos pequeños son menos precisos que los modelos de uso general: fallarán más en JSON, razonamiento y seguimiento de reglas, y las cifras de las soluciones no se reproducirán. No es un inconveniente del laboratorio: es material de análisis (¿qué instrucciones lo corrigen?, ¿qué tareas no son aptas para un modelo pequeño?). En máquinas modestas, una consulta puede tardar varios segundos; reducir con `--n`.

## Camino 4 · Planes gratuitos de proveedores en la nube

Algunos proveedores ofrecen un nivel gratuito con límites de uso y una API compatible con la de OpenAI. Las condiciones, los modelos y los límites cambian con frecuencia (hay servicios que han retirado su nivel gratuito, como GitHub Models, y otros que han retirado modelos concretos): comprobar siempre su documentación oficial actual antes de usarlos. Cloudflare Workers AI y NVIDIA NIM también ofrecen uso gratuito limitado, pero su dirección depende de la cuenta.

| Servicio | Clave gratuita | Dirección base habitual |
|---|---|---|
| Google AI Studio (Gemini) | Sí; las comparativas indican que no pide tarjeta | `https://generativelanguage.googleapis.com/v1beta/openai/` |
| Groq | Sí; las comparativas indican que no pide tarjeta | `https://api.groq.com/openai/v1` |
| NVIDIA (catálogo build.nvidia.com) | Sí; comprobado, con limitaciones (ver abajo) | `https://integrate.api.nvidia.com/v1` |
| OpenRouter (modelos con sufijo `:free`) | Sí, sin tarjeta, pero con un límite de 50 peticiones al día (comprobado) | `https://openrouter.ai/api/v1` |

No sirven para este fin los servicios que solo dan un crédito de prueba de pago único (por ejemplo, la consola de Anthropic) ni los que han retirado su nivel gratuito (GitHub Models) o exigen un pago para obtener la clave (Cerebras) o crédito para poder usarla (Mistral: según la prueba con una cuenta nueva, la clave no se activa sin crédito) o saldo (DeepSeek: una cuenta nueva comprobada el 9 de noviembre de 2026 tenía saldo 0 y las llamadas devolvían el error 402 «Insufficient Balance»). Cloudflare Workers AI y NVIDIA NIM también ofrecen uso gratuito, pero su dirección depende de la cuenta y los requisitos de registro varían.

Ejemplo comprobado el 9 de noviembre de 2026 con una clave gratuita de Google AI Studio: el laboratorio 07A con 30 casos devolvió JSON válido en los 30 y tardó unos 5 segundos por llamada.

```bash
export LLM_PROVIDER=openai
export LLM_BASE_URL="https://generativelanguage.googleapis.com/v1beta/openai"
export LLM_API_KEY="<clave de AI Studio>"
export LLM_MODEL="gemini-3.1-flash-lite"   # los modelos cambian: ver la lista abajo
```

Lista de modelos disponibles para la clave (los proveedores retiran los modelos antiguos y los nombres cambian, así que conviene copiar uno de esta lista y no uno visto en un ejemplo):

```bash
curl -s -H "Authorization: Bearer $LLM_API_KEY" "$LLM_BASE_URL/models"
```

Ejemplo comprobado con una clave gratuita de OpenRouter: funcionan modelos como `nvidia/nemotron-3-ultra-550b-a55b:free`, pero hay tres limitaciones. El límite gratuito es de 50 peticiones al día (a la petición 51 devuelve «Rate limit exceeded: free-models-per-day» y para subirlo a 1.000 pide comprar créditos), de modo que una sola tanda de 30 casos consume más de la mitad. Los modelos de razonamiento gastan parte de `max_tokens` en pensar y pueden devolver la respuesta vacía: usar `--max-tokens 1500` o más. En la prueba con 30 casos del laboratorio 07A, 6 respuestas salieron vacías o truncadas con el límite por defecto. Y algunos modelos gratuitos están temporalmente limitados desde el proveedor (error 429) o devuelven un formato sin el campo `choices`.

Ejemplo comprobado con una clave del catálogo de NVIDIA: la lista de modelos devolvió 84, pero la mayoría de los probados fallaron (error 410 «end of life» en modelos retirados, como `meta/llama-3.1-8b-instruct`, y 404 «Function not found for account» en modelos no habilitados para la cuenta). Funcionó `mistralai/mistral-large-4-1t-a52b`, un modelo de razonamiento: tardó unos 12 segundos en una petición mínima y con `max_tokens` bajos devuelve el contenido vacío (el razonamiento se gasta antes), así que hay que usar `--max-tokens 1500` o más. Otro modelo (`deepseek-ai/deepseek-v4.1-flash`) no respondió en 100 segundos. Es una opción posible, pero lenta y poco fiable para tandas largas; probar primero el modelo con una llamada suelta.

Los modelos Gemma devuelven su razonamiento interno dentro de la respuesta (etiquetas `<thought>`), lo que rompe los extractores de JSON: preferir un modelo Gemini.

Configuración genérica para otros servicios:

```bash
export LLM_PROVIDER=openai
export LLM_BASE_URL="<dirección base del servicio>"
export LLM_API_KEY="<clave del servicio>"
export LLM_MODEL="<modelo disponible en el nivel gratuito>"
```

Los niveles gratuitos suelen limitar las peticiones por minuto: el cliente reintenta automáticamente ante errores de limitación, y `ejecutar_suite.py` admite `--pausa 2` (segundos entre llamadas). **No enviar datos personales reales** a ningún servicio; los datos de los laboratorios son ficticios.

## Qué camino conviene a cada laboratorio

| Laboratorio | Chat | Modo manual | Modelo local / API gratuita |
|---|---|---|---|
| 01A, 01B, 02A, 02B, 03A, 05A, 08A, 09A, 10A, 10B, 12B | Completo | — | — |
| 03B, 06A, 08B, 12A, 12C | Con lotes de 10 casos y los scripts de evaluación sin API | Con `--n 15` | Completo |
| 04A, 04B, 07A, 07B | Con 15–20 casos | Con `--n 15` | Completo (más fiable) |
| 05B | Conversación de 14 turnos pegando mensaje a mensaje | Sí | Completo |
| 06B | Solo variabilidad natural, sin temperatura | No recomendable | Recomendado (permite temperatura y top-p) |
| 09B | Ataques uno a uno con el prompt del asistente | Con 5 ataques | Completo |
| 11A, 11B | Completo (código y pruebas se ejecutan en local) | — | — |
| 11C | Completo (la traducción se pide en el chat y se comprueba en el navegador con `comprobar.html`) | — | — |
| 13A, 13B, 14 | Etapa por etapa, con 3–5 casos | Con `--n 3` | Recomendado |

## Consejos para trabajar sin API

- Empezar siempre por una prueba pequeña (5 casos) para detectar errores de formato antes de lanzar el lote.
- Guardar las respuestas del chat tal cual, con su identificador de caso. Sirven como registro de experimentos.
- Anotar el modelo y la fecha de cada prueba: los chats cambian de modelo sin avisar.
- Si los resultados difieren de los de las soluciones, no es un fallo: compararlos y explicar la diferencia es parte del aprendizaje.
