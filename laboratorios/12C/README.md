[← Laboratorios](../README.md) · [Módulo 12](../../modulos/12-analisis-de-informacion-y-datos/README.md) · [← 12B](../12B/README.md) · [13A →](../13A/README.md)

# Laboratorio 12C · Análisis de datos con Python asistido por un modelo

Módulo 12 · Prompt Engineering para análisis de información y datos · Duración estimada: 60 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Analizar un conjunto de datos con código Python generado por un modelo y comprobar los resultados antes de fiarse. |
| Conviene haber hecho antes | [12A](../12A/README.md) (recomendado) |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Conocer los datos y decidir cómo limpiarlos (8 min)
- Paso 2 · Leer el prompt básico (6 min)
- Paso 3 · Pedir el código y revisarlo antes de ejecutarlo (10 min)
- Paso 4 · Ejecutar y comparar con la referencia (10 min)
- Paso 5 · Diagnosticar los errores (8 min)
- Paso 6 · Escribir el prompt con contrato y repetir (12 min)
- Paso 7 · Leer el gráfico (6 min)

<details>
<summary>Secciones del módulo relacionadas (9)</summary>

- [§3.1 Python para análisis asistido por LLM](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#31-python-para-análisis-asistido-por-llm)
- [§3.2 Pandas y DataFrames](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#32-pandas-y-dataframes)
- [§3.3 Limpieza y transformación de datos](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#33-limpieza-y-transformación-de-datos)
- [§3.4 Estadística descriptiva](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#34-estadística-descriptiva)
- [§3.5 Visualización con Matplotlib](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#35-visualización-con-matplotlib)
- [§3.6 Prompt para código analítico](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#36-prompt-para-código-analítico)
- [§3.7 Validar código y resultados](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#37-validar-código-y-resultados)
- [§3.8 Caso completo: de documentos a indicadores](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#38-caso-completo-de-documentos-a-indicadores)
- [§3.9 Errores frecuentes y buenas prácticas](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#39-errores-frecuentes-y-buenas-prácticas)

</details>

## Justificación del laboratorio

Dirección de Altanoria quiere saber cómo ha ido 2026 en Soporte y le pide a un analista seis cifras: cuántas incidencias hubo por producto, cuánto duraron de media, qué porcentaje fue de prioridad P1, cómo evolucionaron mes a mes, cuántos usuarios afectó una incidencia típica y cuál fue la causa más frecuente. Los datos son un fichero de 360 filas exportado a mano, y el analista decide pedirle el código a un asistente en lugar de escribirlo.

El código llega en segundos y parece correcto. Pero un script que se ejecuta sin errores puede calcular mal sin avisar: cuenta dos veces las filas repetidas, trata «Copilot» y «Altanoria Copilot» como productos distintos, suma 1,5 horas como 1,5 minutos, lee el 04/03/2026 como abril o toma los usuarios vacíos por ceros. El resultado es una tabla de cifras razonables y equivocadas que acaba en un informe para Dirección. La diferencia entre el analista que se fía del código y el que lo valida es una referencia independiente con la que comparar.

Este laboratorio mide cuántas de las seis cifras acierta el código que genera un modelo, enseña a diagnosticar de dónde sale cada error, a escribir un prompt con contrato (columnas, supuestos y salida exacta) que los evita y a comprobar que un gráfico dice lo que los datos dicen. Es opcional: amplía la sección de Python del módulo, que los laboratorios 12A y 12B no practican.

## Objetivos

Al terminar el laboratorio se habrá conseguido:

- Describir los problemas de calidad de un conjunto de datos (duplicados, nombres, unidades, formatos de fecha y vacíos) y decidir cómo tratar cada uno.
- Pedir a un modelo un script de análisis con un prompt que incluye el entorno, las columnas, los supuestos y la salida exacta.
- Revisar el código antes de ejecutarlo y compararlo con una referencia calculada de forma independiente.
- Diagnosticar de dónde sale un valor equivocado: qué corrección de los datos falta en el código.
- Comprobar que un gráfico representa los datos (ejes, escala, meses, valores y suma) y no solo que se dibuja.

Conceptos que se usan (se explican en el módulo, secciones [§3.1 Python para análisis asistido por LLM](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#31-python-para-análisis-asistido-por-llm) a [§3.7 Validar código y resultados](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#37-validar-código-y-resultados)):

- **Referencia independiente**: el valor correcto calculado por otra vía (una hoja de cálculo o un script revisado) con el que se compara el resultado del código generado.
- **Limpieza de datos**: quitar duplicados, unificar nombres, convertir unidades y fechas y decidir qué hacer con los vacíos antes de calcular nada.
- **Prompt para código analítico**: pide el entorno, la descripción de las columnas, los supuestos y el formato exacto de la salida; no deja que el modelo los adivine.
- **Validación del resultado**: el código que se ejecuta sin errores no está validado; solo lo está el que coincide con la referencia.

## Recursos necesarios

| Recurso | Camino | Para qué sirve | Dónde está o cómo conseguirlo |
|---|---|---|---|
| Un asistente de IA con chat (idealmente, uno que pueda ejecutar código) | Chat | Pedir el código y, si puede, ejecutarlo | Cualquiera (de pago o gratuito) |
| Un programa de hojas de cálculo | Los dos | Abrir la hoja de resultados y su referencia | Excel, Google Sheets o LibreOffice Calc |
| Muestra de 30 incidencias con sus indicadores correctos (plegados) | Chat | Pasos 1 a 5 sin ejecutar nada en el ordenador | [`datos/muestra_chat.md`](datos/muestra_chat.md) |
| Hoja de resultados con la muestra y su referencia calculada con fórmulas | Los dos | Limpieza, comparación, errores y gráficos | [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) |
| Las 360 incidencias de 2026 | Código | Medir el código con todos los datos | [`datos/incidencias_2026.csv`](datos/incidencias_2026.csv) |
| Descripción de las columnas | Los dos | Prompt con contrato | [`datos/columnas.md`](datos/columnas.md) |
| Indicadores de referencia | Los dos | Evaluar el código (Paso 4) y los gráficos (Paso 7); no para escribir el código | [`datos/referencia_indicadores.json`](datos/referencia_indicadores.json) |
| Tres gráficos de ejemplo | Los dos | Paso 7 | [`datos/graficos/`](datos/graficos/grafico_1.png) |
| Python 3.9 o superior, pandas 2 o superior, Matplotlib y acceso a un modelo | Código | Ejecutar el código generado y pedirlo por script | Véase la [guía](../comun/README.md); `pip install "pandas>=2,<3" matplotlib` (pandas 2, como en el módulo) |
| Scripts de apoyo | Código | Pedir el código, ejecutarlo y compararlo | [`generar_codigo.py`](generar_codigo.py), [`comparar_indicadores.py`](comparar_indicadores.py) y [`calcular_referencia.py`](calcular_referencia.py) |
| Prompt básico (v1) | Los dos | Paso 3 | [`prompts/prompt_codigo_v1.txt`](prompts/prompt_codigo_v1.txt) |

Antes de empezar, conviene crear un documento de texto vacío titulado «Laboratorio 12C · Mis resultados», donde ir pegando los prompts, el código que devuelve el asistente y lo que se pida anotar, y abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx).

Un aviso de seguridad: el código generado por un modelo es código de otra persona. En este laboratorio se ejecuta solo después de leerlo (Paso 3) y nunca con datos reales.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

Tiempo de ejecución con código (orientativo, medido con Gemma 4 de 8 B en local; con una API rápida y sin razonamiento suele ser bastante menos): pedir el código al modelo, de 25 a 30 segundos cada vez; ejecutarlo sobre las 360 filas, de 1 a 3 segundos.

## Pasos de ejecución

Los pasos se hacen en orden. Camino con chat: se trabaja con una muestra de 30 incidencias y se compara con la pestaña «Referencia» de la hoja, que calcula con fórmulas los seis indicadores correctos. Camino con código: se pide el código por script, se ejecuta sobre las 360 filas y se compara con `comparar_indicadores.py`.

### Paso 1 · Conocer los datos y decidir cómo limpiarlos (8 minutos)
1. Abrir [`datos/columnas.md`](datos/columnas.md) y leer qué significa cada columna.
2. Abrir la pestaña «Muestra» de la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): tiene 30 incidencias (las mismas de [`datos/muestra_chat.md`](datos/muestra_chat.md)). Buscar en ellas cinco problemas: filas repetidas, el mismo producto escrito de varias formas, duraciones en horas y en minutos, fechas en dos formatos y usuarios afectados vacíos.
3. En la pestaña «Limpieza», elegir para cada problema la decisión de la lista: cómo se debe tratar antes de calcular (por ejemplo, «dos filas con el mismo `id` son una sola incidencia»). La columna de la decisión recomendada está oculta: mostrarla al terminar y comprobar cuántas coinciden.

Comprobación: la pestaña «Limpieza» tiene los cinco problemas con su decisión y cuenta cuántas coinciden con la recomendada.

### Paso 2 · Leer el prompt básico (6 minutos)
Se lee el prompt básico (v1), que es el que se enviaría sin pensar más:

```text
Escribe un script de Python con pandas que lea `datos/incidencias_2026.csv` y calcule estos indicadores:

- incidencias_por_producto
- duracion_media_min_por_producto
- porcentaje_p1
- incidencias_por_mes (con la clave en formato AAAA-MM)
- mediana_usuarios_afectados
- causa_mas_frecuente (la causa y su porcentaje)

Imprime un único objeto JSON con esas claves.

Primeras filas del fichero:

{{muestra}}
```

1. Leer el prompt: dice qué indicadores se quieren y cómo se llaman las claves del resultado, pero no dice nada sobre las columnas, los duplicados, las unidades ni los vacíos.
2. Comprobar, con la lista de problemas del Paso 1, cuáles de ellos no menciona el prompt.

Comprobación: se pueden nombrar, de los cinco problemas de los datos, al menos tres que el prompt no menciona.

### Paso 3 · Pedir el código y revisarlo antes de ejecutarlo (10 minutos)
Camino con chat:

1. Abrir una conversación nueva en el asistente. Pegar el prompt v1 sustituyendo `{{muestra}}` por las 30 filas de [`datos/muestra_chat.md`](datos/muestra_chat.md) (con la fila de cabecera).
2. Si el asistente puede ejecutar código, pedirle que lo ejecute sobre esas 30 filas y que imprima el JSON. Si no puede, copiar el código para ejecutarlo en un cuaderno en línea (por ejemplo, un cuaderno de Google Colab) o, si no es posible, pedirle que explique paso a paso cómo calcula cada indicador.
3. Guardar el código y su resultado en el documento de texto.

<details>
<summary>Con código: pedir el código por script</summary>

Abrir una terminal en la carpeta `laboratorios/12C` (antes, `python ../comun/comprobar_entorno.py`) y ejecutar:

```bash
python generar_codigo.py --prompt prompts/prompt_codigo_v1.txt --salida codigo_v1.py
```

El script envía el prompt al modelo y guarda en `codigo_v1.py` el primer bloque de código que contenga la respuesta. No lo ejecuta.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Antes de ejecutar nada, leer el código con esta lista y anotar en el documento cuáles se cumplen: lee el fichero de datos correcto; no escribe ni borra ficheros; no accede a internet; no usa datos inventados; imprime solo un JSON; tiene un paso de limpieza (quitar duplicados, unificar productos, convertir unidades, leer las dos fechas, tratar los vacíos).

Comprobación: hay un código guardado y la lista de revisión tiene una marca en cada punto.

### Paso 4 · Ejecutar y comparar con la referencia (10 minutos)
Camino con chat:

1. Comparar el JSON que devolvió el asistente con la pestaña «Referencia» de la hoja, que calcula los seis indicadores de la muestra con fórmulas.
2. Anotar en la pestaña «Comparación», para cada indicador, si el valor obtenido coincide con la referencia.

<details>
<summary>Con código: comparar con la referencia</summary>

En la terminal, en la carpeta `laboratorios/12C`:

```bash
python comparar_indicadores.py codigo_v1.py
```

El script ejecuta el código sobre las 360 filas (límite de 120 segundos), lee el último JSON que imprima y compara cada indicador con la referencia. Para cada indicador que no coincide, dice si el valor es el que daría uno de los errores típicos (duplicados sin quitar, productos sin unificar, horas sin convertir, vacíos como 0 o media en lugar de mediana). Anotar el resultado en la pestaña «Comparación».

Si el código falla al ejecutarse, contar todos los indicadores como «no»: también es un resultado.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: la pestaña «Comparación» tiene los seis indicadores del prompt v1 con su «coincide» y la hoja los cuenta.

### Paso 5 · Diagnosticar los errores (8 minutos)
1. Para cada indicador que no coincide, buscar en el código la causa. Las causas habituales son siete: no quita duplicados, no unifica los productos, no convierte las horas, lee mal las fechas (por ejemplo, `04/03/2026` como 3 de abril), trata los vacíos como cero o usa la media en lugar de la mediana, falla al ejecutarse (una opción de pandas que no existe en la versión instalada, tipos de numpy que `json` no sabe escribir o un error de sintaxis) o inventa datos de ejemplo y los guarda encima del fichero de datos «para que el script se pueda ejecutar».
2. Anotar en la pestaña «Errores», para cada causa, a cuántos indicadores afecta (el recuento de causas distintas lo calcula la hoja).

Comprobación: cada indicador equivocado tiene una causa y la pestaña «Errores» cuenta las causas distintas.

### Paso 6 · Escribir el prompt con contrato y repetir (12 minutos)
1. Escribir una versión v2 del prompt que añada lo que faltaba: el entorno (Python y pandas), la descripción de las columnas ([`datos/columnas.md`](datos/columnas.md)), los supuestos de limpieza que se decidieron en el Paso 1 y la salida exacta (las seis claves, los decimales y que no se imprima nada más).
2. Anotar en la pestaña «Prompt», para cada error del Paso 5, si el prompt v2 tiene una línea que lo corrige.
3. Repetir los Pasos 3 y 4 con el prompt v2 y anotar si coincide cada indicador en la columna «v2» de la pestaña «Comparación».

<details>
<summary>Con código: repetir con el prompt v2</summary>

Guardar el prompt en `mi_prompt_v2.txt` (puede usar las variables `{{columnas}}` y `{{muestra}}`) y ejecutar:

En la terminal, en la carpeta `laboratorios/12C`:

```bash
python generar_codigo.py --prompt mi_prompt_v2.txt --salida codigo_v2.py
python comparar_indicadores.py codigo_v2.py
```

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

El prompt v2 de referencia está en la solución, para compararlo con el propio.

Comprobación: hay un prompt v2, la pestaña «Prompt» indica qué errores cubre y los seis indicadores están medidos de nuevo, hayan mejorado o no.

### Paso 7 · Leer el gráfico (6 minutos)
Tres versiones del código que escribió un asistente dibujaron «un gráfico de barras con las incidencias por mes de 2026». Los tres gráficos están en [`datos/graficos/`](datos/graficos/): [`grafico_1.png`](datos/graficos/grafico_1.png), [`grafico_2.png`](datos/graficos/grafico_2.png) y [`grafico_3.png`](datos/graficos/grafico_3.png). Se dibujan los tres sin ningún error, pero no todos dicen lo que dicen los datos.

1. Mirar cada gráfico y, en la pestaña «Gráfico», marcar «sí» o «no» en cinco comprobaciones: los ejes tienen título, la escala del eje vertical empieza en cero, los meses son los que existen y están en orden, los valores coinciden con los indicadores de referencia ([`datos/referencia_indicadores.json`](datos/referencia_indicadores.json), clave `incidencias_por_mes`) y la suma de las barras es igual al total de incidencias únicas (348).
2. Para cada gráfico, contestar si afirma algo que los datos no respaldan (por ejemplo, «las incidencias se disparan en otoño») y si se publicaría tal cual.
3. Pensar qué se pediría al asistente para corregir los demás.

<details>
<summary>Con código: pedir un gráfico propio</summary>

Pedir al asistente que añada al código del prompt v2 un gráfico de barras con el recuento por mes, guardarlo como `grafico.png` y pasarle las mismas cinco comprobaciones. Para ejecutarlo, guardar el código que devuelva como `codigo_grafico.py` en la carpeta `laboratorios/12C` (tras leerlo con la lista de revisión de arriba) y ejecutar:

```bash
python codigo_grafico.py
```

Se crea `grafico.png` en la misma carpeta. Si el código falla o no crea la imagen, copiar el error al asistente y pedir la corrección con el mismo método del Paso 3.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: la pestaña «Gráfico» tiene las cinco comprobaciones de los tres gráficos y si cada uno se publicaría.

## Conclusiones

### Qué se ha conseguido

Se ha comprobado que el código que un modelo escribe para analizar datos suele ejecutarse sin errores y, aun así, calcular mal alguna de las cifras, y que la única forma de saberlo es compararlo con una referencia calculada de otra manera. También se ha visto que el prompt marca la diferencia: describir las columnas, decir qué hacer con los duplicados, las unidades, las fechas y los vacíos, y fijar la salida exacta evita casi todos los fallos.

Resultado medido con Gemma 4 (8 B, en local): con el prompt básico, ninguna de las 10 ejecuciones acierta un solo indicador; con el prompt con contrato, la media sube a 4,2 de 6.

Referencia de lo que suele ocurrir (rangos amplios con un modelo pequeño; con otro modelo pueden variar): con un prompt sin contrato el código suele fallar al ejecutarse o inventar datos, y los indicadores correctos son 0 o muy pocos; con contrato salen bien entre 3 y 6 de los 6, y lo que más falla son las fechas y los nombres de producto.

### Preguntas de reflexión

Conviene intentar responder antes de abrir cada respuesta.

1. ¿Por qué un script que se ejecuta sin errores no está validado?

   <details>
   <summary>Respuesta</summary>

   Porque un error de ejecución es una señal visible y un cálculo equivocado no lo es: el código puede contar dos veces las filas repetidas o sumar horas como minutos y producir cifras plausibles. Solo la comparación con una referencia independiente lo detecta.

   </details>

2. ¿Qué dos problemas de los datos fueron más difíciles de ver y por qué?

   <details>
   <summary>Respuesta</summary>

   Los que no producen ningún aviso: los duplicados (el recuento sube un poco) y las duraciones en horas (la media baja un poco). Los nombres de producto distintos y las fechas mal leídas sí suelen dejar una pista visible (productos de más, meses fuera de orden).

   </details>

3. ¿Qué parte del prompt v2 fue la que más indicadores corrigió?

   <details>
   <summary>Respuesta</summary>

   Los supuestos de limpieza escritos como una lista numerada: cada uno corrige un tipo de error y, juntos, evitan casi todos los fallos. La descripción de las columnas y la salida exacta ayudan, pero por sí solas no corrigen los cálculos.

   </details>

4. ¿Qué haría si la referencia y el código discrepan y no se sabe cuál es el correcto?

   <details>
   <summary>Respuesta</summary>

   Comprobar la referencia a mano con tres o cuatro filas concretas, buscar la regla que cada uno aplica a los casos dudosos (por ejemplo, qué se hace con los vacíos) y fijar esa regla por escrito. La referencia también puede estar mal.

   </details>

5. ¿Cuándo no conviene pedirle el cálculo directamente al modelo y es mejor pedirle el código?

   <details>
   <summary>Respuesta</summary>

   Cuando los datos son muchos, la cifra se va a reutilizar o hay que poder auditarla: el código se puede leer, repetir y comprobar con una referencia; un número calculado «de cabeza» por el modelo no tiene rastro.

   </details>

### Autoevaluación

Esta lista sirve para valorar el propio trabajo (el laboratorio no se evalúa):

- [ ] Los cinco problemas de los datos están descritos con un ejemplo real y una decisión.
- [ ] El código se leyó antes de ejecutarlo.
- [ ] Los seis indicadores se compararon con la referencia, no con lo que parecía razonable.
- [ ] Cada error tiene una causa y una línea del código donde se corrige.
- [ ] Cada línea del prompt v2 se puede asociar a un error del Paso 5.
- [ ] Los tres gráficos se contrastaron con la referencia (ejes, escala, meses, valores y suma de las barras).

### Errores típicos

- Ejecutar el código generado sin leerlo: puede escribir sobre los datos o inventarlos.
- Instalar la última versión de pandas sin mirar para qué versión se pidió el código: los modelos usan opciones que ya no existen y el script falla al ejecutarse.
- Dar por buena una cifra porque «parece razonable».
- Comparar con otra salida del mismo modelo en lugar de con una referencia independiente.
- Corregir el código a mano para que cuadre sin entender qué regla de los datos faltaba.
- Dar por bueno un gráfico porque se dibuja y tiene buen aspecto, sin comprobar su escala, sus meses, sus valores y la suma de sus barras.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

<details>
<summary>Los cinco problemas de los datos y cómo tratarlos</summary>

| Problema | Cómo se ve | Decisión |
|---|---|---|
| Filas repetidas | El mismo `id` aparece dos veces con los mismos valores | Una sola incidencia: conservar la primera fila |
| Producto escrito de varias formas | «Copilot», «copilot» y «Altanoria Copilot»; «Docu Mind», «Documind» y «DocuMind»; «Agent Hub», «agenthub» y «AgentHub» | Unificar en los tres nombres oficiales |
| Duraciones en horas | `unidad` es `h` y el número tiene decimales (1,5) | Multiplicar por 60 para trabajar siempre en minutos |
| Fechas en dos formatos | `2026-03-04` y `04/03/2026` | Leer cada una con su formato; en la segunda, el día va primero |
| Usuarios afectados vacíos | La celda está vacía | «No consta»: no es 0 y no entra en la mediana |

</details>

<details>
<summary>Prompt v2 de referencia</summary>

```text
Eres un analista de datos que escribe código Python correcto, legible y reproducible. Solo escribes el código en un único bloque, sin explicaciones.
---USUARIO---
Escribe un script de Python 3.9 o superior que use pandas (versión 2 o superior) y la biblioteca estándar, sin otras dependencias, para analizar el fichero `datos/incidencias_2026.csv` (la ruta es relativa a la carpeta desde la que se ejecuta el script).

Descripción de los datos:

{{columnas}}

Primeras filas del fichero:

{{muestra}}

Antes de calcular nada, el script debe preparar los datos así:
1. Quitar las filas repetidas: dos filas con el mismo `id` son la misma incidencia (conservar la primera).
2. Unificar el producto: `Copilot`, `copilot` y `Altanoria Copilot` son el producto «Altanoria Copilot»; `Docu Mind`, `Documind` y `DocuMind` son «DocuMind»; `Agent Hub`, `agenthub` y `AgentHub` son «AgentHub».
3. Convertir todas las duraciones a minutos (si la unidad es `h`, multiplicar por 60).
4. Convertir `abierta` a fecha. Hay dos formatos mezclados: `AAAA-MM-DD` y `DD/MM/AAAA` (el día va primero). Convertir cada fila con su formato, sin dejar que se interprete un día como mes.
5. `usuarios_afectados` vacío significa «no consta»: no es 0 y no entra en el cálculo.

Calcular sobre los datos ya preparados:
- `incidencias_por_producto`: número de incidencias por producto.
- `duracion_media_min_por_producto`: duración media en minutos por producto, con un decimal.
- `porcentaje_p1`: porcentaje de incidencias con prioridad P1 sobre el total, con dos decimales.
- `incidencias_por_mes`: número de incidencias por mes, con la clave `AAAA-MM`.
- `mediana_usuarios_afectados`: mediana de `usuarios_afectados` (no la media), con un decimal.
- `causa_mas_frecuente`: objeto con `causa` y `porcentaje` (un decimal) de la causa que más aparece.

Salida: terminar el script imprimiendo con `print(json.dumps(resultado, ensure_ascii=False))` un único objeto con exactamente esas seis claves, con números normales de Python (no tipos de numpy). No imprimas nada más.
```

</details>

<details>
<summary>Los tres gráficos: qué hay en cada uno</summary>

| Comprobación | Gráfico 1 | Gráfico 2 | Gráfico 3 |
|---|---|---|---|
| Ejes con título | sí | no (el eje vertical no tiene título ni unidades) | sí |
| Escala vertical desde cero | sí | no (empieza en 20) | sí |
| Meses que existen y en orden | sí (enero a octubre) | sí (enero a octubre) | no (aparecen noviembre y diciembre, que no tienen datos) |
| Valores iguales a la referencia | sí (25, 27, 29, 33, 39, 33, 21, 25, 48 y 68) | sí | no (octubre muestra 53 en lugar de 68; febrero, 20 en lugar de 27) |
| Suma de las barras = 348 | sí | sí | no (suman 300) |
| Lo que afirma | «Incidencias abiertas por mes»: octubre es el mes con más (68) y julio el que menos (21) | «Las incidencias se disparan en otoño»: los datos de septiembre y octubre sí son los más altos, pero con el eje en 20 octubre parece 48 veces julio cuando es 3,2 veces | «Incidencias abiertas por mes»: parece un resultado limpio, pero ha leído el día como mes en las fechas DD/MM/AAAA: pierden 48 incidencias y aparecen dos meses imposibles |

Solo el gráfico 1 se publicaría. El 2 solo necesita que el eje empiece en cero y tenga título. El 3 no se arregla en el gráfico: hay que corregir la lectura de las fechas (el Paso 5) y repetir el cálculo. Una comprobación de la suma de las barras habría detectado el gráfico 3 sin mirar mes a mes. Los gráficos se hicieron con Matplotlib sobre los datos del laboratorio.

</details>

<details>
<summary>Los seis indicadores de las 360 filas</summary>

```json
{
  "incidencias_por_producto": {
    "AgentHub": 81,
    "Altanoria Copilot": 127,
    "DocuMind": 140
  },
  "duracion_media_min_por_producto": {
    "AgentHub": 44.5,
    "Altanoria Copilot": 43.2,
    "DocuMind": 48.7
  },
  "porcentaje_p1": 8.33,
  "incidencias_por_mes": {
    "2026-01": 25,
    "2026-02": 27,
    "2026-03": 29,
    "2026-04": 33,
    "2026-05": 39,
    "2026-06": 33,
    "2026-07": 21,
    "2026-08": 25,
    "2026-09": 48,
    "2026-10": 68
  },
  "mediana_usuarios_afectados": 9.0,
  "causa_mas_frecuente": {
    "causa": "configuracion",
    "porcentaje": 24.7
  }
}
```

El que más suele fallar es el recuento por mes (la fecha con el día y el mes cambiados) y el que menos, el porcentaje de P1 (no depende de las unidades ni de los nombres de producto).

</details>

<details>
<summary>Los errores típicos y su valor</summary>

Con `python calcular_referencia.py --ingenuo <error>` se ven los valores que daría cada error: `sin_deduplicar`, `producto_sin_unificar`, `horas_sin_convertir`, `vacios_como_cero` y `media_en_vez_de_mediana`. `comparar_indicadores.py` usa esos mismos cálculos para explicar un valor equivocado.

</details>

### Resultados medidos con un modelo real

Medición de noviembre de 2026 con Gemma 4 (8 B, en local con Ollama), temperatura 0,7, pandas 2.3.3 y 10 ejecuciones por prompt. Cada código se ejecutó sobre una copia de los datos y se comparó con `referencia_indicadores.json`.

| | Prompt v1 (básico) | Prompt v2 (con contrato) |
|---|---|---|
| Ejecuciones que terminan sin error | 3 de 10 | 10 de 10 |
| Indicadores correctos por ejecución | 0 en las 10 | 4, 5, 3, 4, 6, 5, 5, 4, 6 y 0 |
| Media de indicadores correctos | 0,0 de 6 | 4,2 de 6 |
| Ejecuciones que escriben sobre los datos | 5 | 1 |

- Con v1 fallan 7 ejecuciones al ejecutarse: seis con `Object of type int64 is not JSON serializable` y una con un error de sintaxis. Las tres que terminan inventan datos de ejemplo y los guardan en `incidencias_2026.csv`, así que sus seis indicadores son incorrectos. Un código que se ejecuta no es un código que calcula bien.
- Con v2 el indicador que más falla es «Incidencias por mes» (6 de 10 ejecuciones), por las fechas en dos formatos. Después fallan, cada uno en 3 ejecuciones, las incidencias y la duración media por producto (nombres sin unificar), y la causa más frecuente.
- Una de las 10 ejecuciones con v2 también escribió sobre los datos y obtuvo 0 de 6.
- Estas cifras dependen del modelo, de la temperatura y de la versión de pandas: sirven para saber qué esperar, no como valor que deba reproducirse.

</details>

### Para seguir

- Añadir un séptimo indicador (por ejemplo, el porcentaje de incidencias reabiertas por producto) y comprobarlo con la hoja.
- Pedir el mismo análisis con otro modelo y comparar cuántos indicadores acierta cada uno.
- Escribir una lista de cinco comprobaciones que se aplicaría a cualquier código analítico generado por un modelo (por ejemplo, «comparar con una referencia independiente» o «mirar qué hace con los vacíos»), cada una verificable con un sí o un no, y convertirla en un script que se ejecute siempre que se genere código analítico.

---

[← Laboratorios](../README.md) · [Módulo 12](../../modulos/12-analisis-de-informacion-y-datos/README.md) · [← 12B](../12B/README.md) · [13A →](../13A/README.md)
