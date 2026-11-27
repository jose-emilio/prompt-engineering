[← Laboratorios](../README.md) · [Módulo 06](../../modulos/06-formato-de-salida-y-parametros/README.md) · [← 06A](../06A/README.md) · [07A →](../07A/README.md)

# Laboratorio 06B · Temperatura y top-p: un experimento controlado

Módulo 06 · Control del formato de salida y parámetros de generación · Duración estimada: 50 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Variar la temperatura en un experimento controlado y medir cuánto cambian la variabilidad y la calidad (el top-p, como ampliación). |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Del chat: no hace falta fijar la temperatura (el camino con chat mide la variabilidad natural al repetir la petición); fijar temperatura y top-p exige una API o un modelo local. Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Conocer las tres tareas y sus criterios (7 min)
- Paso 2 · Experimento de temperatura (19 min)
- Paso 3 · Mirar los criterios, no solo la variabilidad (6 min)
- Paso 4 · Reproducibilidad con temperatura 0 (5 min)
- Paso 5 · Entender los límites de salida (6 min)
- Paso 6 · Redactar la política de parámetros (7 min)

<details>
<summary>Secciones del módulo relacionadas (6)</summary>

- [§3.1 Parámetros de generación](../../modulos/06-formato-de-salida-y-parametros/03-parametros-de-generacion-y-cierre.md#31-parámetros-de-generación)
- [§3.2 Temperature: variabilidad en la selección de tokens](../../modulos/06-formato-de-salida-y-parametros/03-parametros-de-generacion-y-cierre.md#32-temperature-variabilidad-en-la-selección-de-tokens)
- [§3.3 Top-p: muestreo por núcleo](../../modulos/06-formato-de-salida-y-parametros/03-parametros-de-generacion-y-cierre.md#33-top-p-muestreo-por-núcleo)
- [§3.4 Max tokens y límites de generación](../../modulos/06-formato-de-salida-y-parametros/03-parametros-de-generacion-y-cierre.md#34-max-tokens-y-límites-de-generación)
- [§3.5 Stop sequences: terminación configurable](../../modulos/06-formato-de-salida-y-parametros/03-parametros-de-generacion-y-cierre.md#35-stop-sequences-terminación-configurable)
- [§3.6 Reproducibilidad y variabilidad](../../modulos/06-formato-de-salida-y-parametros/03-parametros-de-generacion-y-cierre.md#36-reproducibilidad-y-variabilidad)

</details>

## Justificación del laboratorio

Altanoria usa un mismo modelo para tareas muy distintas: extraer datos de incidencias, proponer eslóganes de campaña y resumir incidencias para la dirección. Un ingeniero propone «poner la temperatura a 1 para todo porque da respuestas más naturales». Otro propone ponerla a 0 en todas partes «por si acaso». Las dos propuestas se basan en intuiciones, y las dos tienen un punto ciego.

La temperatura y el parámetro top-p controlan cuánta libertad tiene el modelo al elegir cada palabra. Con valores bajos, el modelo elige casi siempre lo más probable y las respuestas se parecen mucho entre sí; con valores altos, explora alternativas y las respuestas varían. Eso es lo que se quiere para ideas creativas y justo lo que no se quiere para extraer un dato. Pero la relación no es mecánica: ni siquiera con temperatura 0 las respuestas son siempre idénticas, y mucha variabilidad no equivale a buena calidad.

Este laboratorio mide qué ocurre de verdad con tres tareas (extracción, eslogan y resumen) y deduce una política de parámetros para Altanoria.

## Objetivos

Observar y medir cómo los parámetros de decodificación (temperatura y top-p) afectan a la variabilidad y a la calidad de las respuestas según el tipo de tarea, y deducir una política de parámetros por tipo de tarea para Altanoria: qué valores usar para extraer datos, para generar ideas y para resumir.

Al terminar el laboratorio se habrá conseguido:

- Diferenciar lo que se controla con el prompt de lo que se controla con los parámetros ([§3.1 Parámetros de generación](../../modulos/06-formato-de-salida-y-parametros/03-parametros-de-generacion-y-cierre.md#31-parámetros-de-generación)).
- Medir variabilidad con métricas simples: respuestas distintas, similitud entre pares y desviación de la longitud.
- Relacionar temperatura baja con tareas de precisión y temperatura alta con tareas creativas.
- Entender que la reproducibilidad total no está garantizada ni con temperatura 0.
- Limitar la longitud y el final de la salida con `max_tokens` y secuencias de parada.

Conceptos que se usan:

- **Temperatura**. Controla cuánta aleatoriedad hay al elegir el siguiente token: con valores bajos el modelo elige casi siempre el más probable; con valores altos considera más alternativas. No cambia lo que el modelo «sabe», solo la dispersión de lo que dice.
- **Top-p (muestreo por núcleo)**. Limita la elección a los tokens más probables cuya probabilidad acumulada alcanza *p*. Con un *p* bajo, el conjunto de candidatos es pequeño. Se suelen ajustar uno u otro, no ambos a la vez.
- **Disponibilidad variable**. Algunos modelos (por ejemplo, ciertos modelos de razonamiento) no permiten fijar la temperatura o ignoran estos parámetros. Hay que consultar la documentación del modelo usado.
- **`max_tokens` y secuencias de parada**. Fijan el máximo de salida y cuándo se corta. Un máximo demasiado bajo trunca el texto (y puede romper un JSON); no sustituye a pedir una longitud en el prompt.

## Recursos necesarios

> Sin acceso a una API: Los chats no permiten fijar temperatura ni top-p: sin API solo se puede medir la variabilidad natural repitiendo la petición 10 veces. Con un modelo local sí se reproduce completo. Véase la [guía para trabajar sin API](../comun/sin-api.md).

- Un asistente de chat para medir la variabilidad natural; para cambiar la temperatura y el top-p hace falta Python 3.9 o superior y un modelo por API o local ([guía](../comun/README.md)). Verificar si el modelo elegido admite temperatura y top-p.
- Datos: [`datos/tareas_parametros.csv`](datos/tareas_parametros.csv): tres tareas (T1 extracción, T2 eslogan, T3 resumen).
- Hoja de cálculo: [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), para registrar las diez repeticiones de cada tarea y temperatura; calcula cuántas respuestas distintas salen.
- Script: [`experimento_parametros.py`](experimento_parametros.py).
- Alternativa manual (sin API): muchos chats no exponen los parámetros. Se puede medir la variabilidad natural repitiendo 10 veces cada tarea en conversaciones nuevas. Sirve para la parte de variabilidad, no para comparar temperaturas.

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

Tiempo de ejecución con código (orientativo, medido con Gemma 4 de 8 B en local; con una API rápida y sin razonamiento suele ser bastante menos): las tres tareas del experimento con cuatro temperaturas cada una, unos 3 minutos.

## Pasos de ejecución

Los pasos se hacen en orden. Atención al camino: casi ningún chat permite fijar la temperatura ni el top-p. Camino con chat: solo se puede medir la variabilidad natural, repitiendo la misma petición varias veces en conversaciones nuevas (y, si hay un playground web de un proveedor con control de temperatura, usarlo). Camino con código: el script cambia los parámetros y mide.

### Paso 1 · Conocer las tres tareas y sus criterios (7 minutos)
Las tres tareas están en [`datos/tareas_parametros.csv`](datos/tareas_parametros.csv) y son:

```text
TAREA T1 · extraccion

Eres un asistente de Altanoria. Sigue la instrucción con precisión y no añadas explicaciones.

Extraer producto, prioridad y número de usuarios de una nota

<entrada>
Ticket INC-4021 (P2). DocuMind. Afecta a unos 120 usuarios del equipo de Finanzas desde las 9:15.
</entrada>

----------
TAREA T2 · eslogan

Eres un asistente de Altanoria. Sigue la instrucción con precisión y no añadas explicaciones.

Proponer un eslogan para la campaña de lanzamiento de la revisión de pull requests de Copilot (máx. 8 palabras)

<entrada>
Producto: Altanoria Copilot. Novedad: revisión automática de pull requests. Público: equipos de desarrollo.
</entrada>

----------
TAREA T3 · resumen

Eres un asistente de Altanoria. Sigue la instrucción con precisión y no añadas explicaciones.

Resumir en dos frases una incidencia para un directivo

<entrada>
El lunes por la mañana el equipo de Soporte recibió 312 tickets, el doble que la media. El 60 % eran de acceso y se debían a un certificado SSO caducado. A las 11:40 se renovó y a las 12:10 el volumen volvía a la normalidad. Se aplicará una alerta de caducidad con 30 días de antelación.
</entrada>
```

Después, abrir la pestaña «Criterios» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): para cada tarea dice qué tres o cuatro cosas se comprueban en cada respuesta (por ejemplo, en T1, producto, prioridad y número de usuarios). Son sí o no, no hay que valorar nada «a ojo».

Comprobación: se puede decir, para T1, T2 y T3, qué criterios se comprueban en cada respuesta.

### Paso 2 · Experimento de temperatura (19 minutos)
Camino con chat:

1. Abrir una conversación nueva, pegar el prompt de la tarea T1 y enviar. En la primera fila libre de la pestaña «Experimento» de la hoja de resultados, contestar sí o no a los criterios de esa respuesta.
2. Repetir diez veces, cada una en una conversación nueva. En la columna «Grupo de respuesta» poner el mismo número a las respuestas que sean exactamente iguales (1 a la primera, 1 de nuevo si otra sale idéntica, 2 si es distinta, y así). La pestaña «Resultado» cuenta cuántas respuestas distintas hay de las diez.
3. Hacer lo mismo con T2 y con T3. La hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) tiene un bloque de diez filas para cada tarea y temperatura (pestaña «Experimento»); los resultados se leen en la pestaña «Resultado».
4. Si el chat o un playground permite fijar la temperatura, repetir T1 y T2 con temperatura 0 y con temperatura 1,0.

<details>
<summary>Con código: el experimento completo con el script</summary>

Abrir una terminal en la carpeta `laboratorios/06B` (antes, `python ../comun/comprobar_entorno.py`) y ejecutar para cada tarea:

```bash
python experimento_parametros.py --tarea T1 --temps 0 0.3 0.7 1.0 --repeticiones 10
python experimento_parametros.py --tarea T2 --temps 0 0.3 0.7 1.0 --repeticiones 10
python experimento_parametros.py --tarea T3 --temps 0 0.3 0.7 1.0 --repeticiones 10
```

Para una prueba más rápida: `--temps 0 1.0 --repeticiones 6`. El script imprime, por temperatura, las respuestas distintas (de las repeticiones), la similitud media entre pares, la longitud media y su desviación, y guarda todas las salidas en `resultados_parametros.csv`.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: la pestaña «Resultado» muestra las respuestas distintas por tarea (y por temperatura, si se pudo fijar).

### Paso 3 · Mirar los criterios, no solo la variabilidad (6 minutos)
La variabilidad no dice si las respuestas son buenas. Para cada respuesta (y temperatura, si se midió), la hoja cuenta cuántos criterios se cumplen:

- T1 (extracción): ¿producto = DocuMind, prioridad = P2, usuarios = 120?
- T2 (eslogan): ¿máximo 8 palabras? ¿Es distinto de los anteriores (la hoja lo calcula con los números de grupo)? ¿Menciona Copilot, la revisión o las pull requests?
- T3 (resumen): ¿incluye la causa, la duración y la medida correctiva? ¿Tiene como máximo dos frases?

Mirar en la pestaña «Resultado» la columna «Criterios cumplidos de media» y «Respuestas con todos los criterios», y comparar las temperaturas.

Comprobación: la pestaña «Resultado» muestra, para cada tarea, cuántas respuestas cumplen todos los criterios.

### Paso 4 · Reproducibilidad con temperatura 0 (5 minutos)
Repetir T1 con temperatura 0 (o la configuración más determinista posible) cuarenta veces en cuatro series de diez. Anotar los grupos de respuesta (mismo número, mismo texto) y ver cuántas variantes distintas aparecen. Con los chats habituales se puede hacer una versión reducida: diez repeticiones. En la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), el bloque «T1 · extraccion» con temperatura 0 de la pestaña «Experimento» sirve para registrar las diez repeticiones de la versión reducida.

<details>
<summary>Con código: cuarenta repeticiones con temperatura 0</summary>

En la terminal, en la carpeta `laboratorios/06B`:

```bash
python experimento_parametros.py --tarea T1 --temps 0 --repeticiones 40
```

El script indica cuántas de las 40 respuestas son distintas.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: hay un recuento de variantes distintas en el bloque de temperatura 0.

### Paso 5 · Entender los límites de salida (6 minutos)
Con T3 (resumen):

1. Probar a pedir «dos frases» en el prompt: ¿se respeta?
2. Si hay control del máximo de tokens de salida (por ejemplo, en un playground o en el script, con `--max-tokens 30`), fijarlo a 30 y observar el truncamiento. Con un modelo de razonamiento, un límite tan bajo se agota pensando y la respuesta llega vacía: también es una forma de truncamiento (véase [Si algo falla](../comun/si-algo-falla.md)).
3. Si el proveedor permite una secuencia de parada, añadirla y comprobar su efecto.

Anotar qué controla cada mecanismo: el prompt dice cómo escribir; el máximo de tokens corta; la secuencia de parada detiene al encontrar un texto.

Comprobación: hay una conclusión sobre qué controla cada mecanismo.

### Paso 6 · Redactar la política de parámetros (7 minutos)
Completar la pestaña «Política» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) con una recomendación por tipo de tarea (extracción o clasificación, resumen factual, respuesta a clientes e ideación): la temperatura, si conviene generar varias muestras y elegir, y si la salida necesita una comprobación automática. Apoyarse en las cifras de la pestaña «Resultado».

Comprobación: la pestaña «Política» tiene cuatro filas completas.

## Conclusiones

### Qué se ha conseguido

Se ha medido cómo cambia la variabilidad con la temperatura y se ha visto que depende de la tarea: una extracción apenas varía incluso con temperaturas altas, mientras que un eslogan pasa de unas pocas respuestas distintas a una distinta cada vez. Se ha comprobado también que ni siquiera la temperatura 0 garantiza respuestas idénticas, y que variabilidad no es calidad. La política resultante es sencilla: temperatura baja para extraer y clasificar, media para resumir y redactar borradores, alta (con varias muestras) para ideación; y siempre con una comprobación asociada, porque el parámetro por sí solo no garantiza nada.

Referencia orientativa (rangos amplios con un modelo pequeño; con otro modelo pueden variar): A temperatura 0, la tarea de extracción da 1 o 2 respuestas distintas en 10 repeticiones; a temperatura 1,0, la tarea creativa (eslogan) da casi siempre 10 distintas, salvo con un top-p muy bajo (0,3), que puede dar una sola. El tope de longitud puede cortar las respuestas largas. Si el resultado queda muy lejos, conviene revisar datos, prompt y script antes de abrir la solución.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué tarea fue más sensible a la temperatura? ¿Por qué?

   <details>
   <summary>Respuesta</summary>

   La creativa (T2) es la que muestra más cambio visible; la extracción (T1) es la más sensible *en términos de riesgo* (un error de valor).

   </details>

2. ¿Qué pasa si se usa una temperatura alta en una extracción que alimenta un sistema automático?

   <details>
   <summary>Respuesta</summary>

   Se introduce ruido en datos que alimentan procesos automáticos: más fallos de formato y de valores, y resultados no repetibles.

   </details>

3. ¿La temperatura 0 garantiza reproducibilidad? ¿Qué otras causas de variación existen?

   <details>
   <summary>Respuesta</summary>

   No. También influyen actualizaciones del modelo, optimizaciones de servicio y diferencias numéricas. Para trazabilidad, registrar la versión del modelo y guardar la salida.

   </details>

4. ¿Para qué sirve generar varias respuestas con temperatura alta y luego elegir? ¿Cómo se relaciona con la autoconsistencia del laboratorio 04B?

   <details>
   <summary>Respuesta</summary>

   Generar varias muestras y elegir (o votar) aprovecha la diversidad para aumentar la fiabilidad (autoconsistencia) o la calidad (selección).

   </details>

5. ¿Cuándo es preferible pedir diversidad en el propio prompt («dame cinco opciones muy distintas») a subir la temperatura?

   <details>
   <summary>Respuesta</summary>

   Cuando se quiere diversidad *controlada* y evaluable: pedir cinco opciones distintas en una sola llamada es más predecible que repetir muestras con temperatura alta.

   </details>

### Autoevaluación

- [ ] Todas las condiciones tienen el mismo número de repeticiones (10).
- [ ] Se midió también la calidad, no solo la variabilidad.
- [ ] Solo se cambió un parámetro cada vez.
- [ ] Se anotó el modelo, la fecha y los parámetros exactos de cada serie.
- [ ] La política distingue tareas en las que importa la reproducibilidad de aquellas en las que importa la diversidad.

### Errores típicos

- Ajustar temperatura y top-p a la vez.
- Concluir con una sola ejecución por condición.
- Medir solo variabilidad.
- Asumir que cualquier modelo admite estos parámetros.
- Usar `max_tokens` para controlar la longitud del contenido en lugar de pedirla.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

> Los valores concretos dependen del modelo. Estas son las tendencias habituales y cómo interpretarlas.

### Patrón de resultados esperado — expectativa previa a la medición

| Tarea | T = 0 | T = 0,3–0,7 | T = 1,0 | Lectura |
|---|---|---|---|---|
| T1 extracción (respuesta única correcta) | 1–2 variantes distintas de 10 (a veces solo cambia el formato); similitud ≈ 0,95–1,0 | 1–4 variantes; casi todas correctas | Más variantes de formato y algún error de valor | La precisión no mejora con temperatura: solo se pierde estabilidad. |
| T2 eslogan (creativa) | Casi siempre el mismo eslogan | Varias opciones distintas | 8–10 distintas; algunas exceden 8 palabras o son rebuscadas | La diversidad aumenta; la calidad media puede bajar y hay más incumplimientos de restricciones. |
| T3 resumen | Resúmenes muy parecidos | Variaciones de redacción con el mismo contenido | Más diferencias de contenido: a veces omite la medida correctiva | Con temperatura alta, la omisión es el riesgo. |

- Top-p: reducir el *p* en T2 a 0,3 produce una diversidad tan baja como la de bajar la temperatura (con temperatura 1,0, hasta una sola respuesta distinta de 10). Ajustar ambos a la vez dificulta saber cuál produjo el efecto.
- Reproducibilidad: con temperatura 0 suele haber poca variación, pero no se garantiza identidad exacta (por cambios de versión del modelo, paralelismo en el servidor y desempates). No debe usarse como garantía de una auditoría.
- max_tokens: con 30 tokens el resumen se corta a mitad de frase (y un JSON quedaría roto). Pedir «dos frases» en el prompt controla la longitud con sentido; `max_tokens` es una red de seguridad contra respuestas excesivas y de coste. Una secuencia de parada corta el texto en cuanto aparece: útil para formatos delimitados.

### Política de parámetros de ejemplo

| Tipo de tarea | Temperatura | Otros | Comprobaciones |
|---|---|---|---|
| Extracción / clasificación | 0 (o el mínimo permitido) | Salida estructurada, `max_tokens` ajustado | Validación de esquema y casos de respuesta conocida |
| Resumen factual | 0–0,3 | Longitud pedida en el prompt | Checklist de hechos |
| Respuesta a clientes (borrador) | 0,2–0,5 | Restricciones explícitas | Revisión humana |
| Ideación / eslóganes | 0,7–1,0 o varias muestras | Pedir N opciones distintas | Selección humana con criterios |
| Evaluación con rúbrica (LLM como juez) | 0 | Rúbrica y formato fijo | Calibración con casos humanos |

> Si el modelo no permite fijar la temperatura (algunos modelos de razonamiento), compensar con prompt, validación y reintentos.

### Resultados medidos con un modelo real

> Medición realizada el 23 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama (`gemma4:latest`), una sola ejecución por condición y los scripts de este laboratorio. Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

Diez repeticiones por condición (valores que imprime el script):

| Tarea | Temp. | Respuestas distintas | Similitud media | Desv. de longitud |
|---|---|---|---|---|
| T1 extracción | 0 | 1/10 | 1,00 | 0,0 |
| T1 | 0,3 | 2/10 | 0,99 | 0,6 |
| T1 | 0,7 | 1/10 | 1,00 | 0,0 |
| T1 | 1,0 | 2/10 | 0,99 | 0,6 |
| T2 eslogan | 0 | 1/10 | 1,00 | 0,0 |
| T2 | 0,3 | 8/10 | 0,81 | 7,3 |
| T2 | 0,7 | 9/10 | 0,52 | 6,7 |
| T2 | 1,0 | 10/10 | 0,54 | 5,7 |
| T3 resumen | 0 | 2/10 | 0,93 | 6,3 |
| T3 | 0,3 | 10/10 | 0,49 | 17,0 |
| T3 | 0,7 | 10/10 | 0,39 | 19,7 |
| T3 | 1,0 | 10/10 | 0,28 | 29,4 |
| T2, T = 1,0, top-p 0,3 | 1,0 | 1/10 | 1,00 | 0,0 |
| T2, T = 1,0, top-p 0,7 | 1,0 | 10/10 | 0,64 | 7,7 |
| T2, T = 1,0, top-p 1,0 | 1,0 | 10/10 | 0,41 | 5,9 |

Lecturas:

1. T1 es estable porque su respuesta es única: casi no cambia ni con temperatura 1,0
2. Incluso con temperatura 0 el resumen (T3) dio 2 respuestas distintas de 10, así que la reproducibilidad exacta no está garantizada
3. En T2 y T3 la variedad sube ya con 0,3, y la similitud entre respuestas baja de 0,93 a 0,28 en el resumen al subir a 1,0
4. Con T = 1,0, bajar el top-p a 0,3 devuelve la misma respuesta las 10 veces: reduce la variedad más que bajar la temperatura a 0,3, y con top-p 0,7 la variedad se reduce poco.

</details>

### Para seguir

- Probar el top-p, si el modelo permite controlarlo: repetir la tarea T2 con temperatura 1,0 y top-p 0,3, 0,7 y 1,0 y comparar con las filas de temperatura equivalentes. Con código: `python experimento_parametros.py --tarea T2 --temps 1.0 --top-p 0.3 0.7 1.0 --repeticiones 10`. Sin control de parámetros, basta con leer en el módulo qué hace el top-p y anotar qué se esperaría.
- Repetir con un modelo distinto (pequeño y grande) y comparar la sensibilidad.
- Medir la variabilidad semántica, no solo textual, comparando significado con otro prompt evaluador.
- Probar el efecto de la temperatura sobre la tasa de JSON válido del laboratorio 06A.

---

[← Laboratorios](../README.md) · [Módulo 06](../../modulos/06-formato-de-salida-y-parametros/README.md) · [← 06A](../06A/README.md) · [07A →](../07A/README.md)
