[← Laboratorios](../README.md) · [Módulo 04](../../modulos/04-tecnicas-avanzadas-de-prompting/README.md) · [← 03B](../03B/README.md) · [04B →](../04B/README.md)

# Laboratorio 04A · Zero-shot, one-shot y few-shot: cuántos ejemplos hacen falta

Módulo 04 · Técnicas avanzadas de prompting · Duración estimada: 55 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Medir cómo mejora una clasificación al pasar de cero a varios ejemplos y si importa cómo se eligen (y, como ampliación, su orden y el sesgo). |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Revisar los datos (8 min)
- Paso 2 · Entender cómo se construye el prompt (7 min)
- Paso 3 · Medir la curva de aprendizaje (26 min)
- Paso 4 · Mejorar con diseño de ejemplos o de instrucción (14 min)

<details>
<summary>Secciones del módulo relacionadas (8)</summary>

- [§1.2 Zero-shot: definición y funcionamiento](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#12-zero-shot-definición-y-funcionamiento)
- [§1.5 One-shot: un ejemplo que transforma la instrucción](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#15-one-shot-un-ejemplo-que-transforma-la-instrucción)
- [§1.7 Few-shot: aprendizaje en contexto con varios ejemplos](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#17-few-shot-aprendizaje-en-contexto-con-varios-ejemplos)
- [§1.9 Selección de buenos ejemplos para Few-shot](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#19-selección-de-buenos-ejemplos-para-few-shot)
- [§1.10 Cantidad y orden de ejemplos: optimizar el contexto](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#110-cantidad-y-orden-de-ejemplos-optimizar-el-contexto)
- [§1.11 Zero-shot, One-shot y Few-shot: comparativa](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#111-zero-shot-one-shot-y-few-shot-comparativa)
- [§1.12 Diseñar una evaluación comparativa justa](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#112-diseñar-una-evaluación-comparativa-justa)
- [§3.6 Caso comparativo integrado: clasificación con casos ambiguos](../../modulos/04-tecnicas-avanzadas-de-prompting/03-herramientas-revision-y-seleccion-de-tecnica.md#36-caso-comparativo-integrado-clasificación-con-casos-ambiguos)

</details>

## Justificación del laboratorio

Soporte de Altanoria quiere repartir automáticamente los tickets entre los equipos (facturación, acceso, rendimiento, integración, error, funcionalidad, seguridad, cancelación y consulta) con un asistente de IA, pero sin entrenar ningún modelo: solo con prompts. Entonces surge una pregunta práctica que parece sencilla: ¿cuántos ejemplos conviene meter en el prompt?

Hay tres posibilidades. Con cero ejemplos (zero-shot) se da solo la instrucción y se confía en lo que el modelo ya sabe. Con uno (one-shot) se enseña un caso resuelto. Con varios (few-shot) se enseña un pequeño conjunto de casos resueltos. Más ejemplos suelen mejorar el resultado, pero cuestan tokens, es decir, dinero y tiempo en cada llamada, y no todos los ejemplos valen lo mismo: importa cuáles son, en qué orden van y si están equilibrados.

Este laboratorio mide todo eso con datos reales y con una cautela que casi nunca se aplica: una sola ejecución puede engañar. Con unos pocos casos, la diferencia entre dos configuraciones puede ser puro ruido. Por eso se aprende también a repetir, a comparar rangos en lugar de números sueltos y a no sacar conclusiones finas de muestras pequeñas.

## Objetivos

Medir cómo cambia la calidad de una clasificación cuando se pasa de ninguna demostración (zero-shot) a una (one-shot) y a varias (few-shot), y estudiar qué factores alteran el resultado: el número y la selección de los ejemplos.

Al terminar el laboratorio se habrá conseguido:

- Diseñar una evaluación comparativa justa ([§1.12 Diseñar una evaluación comparativa justa](../../modulos/04-tecnicas-avanzadas-de-prompting/01-tecnicas-basadas-en-ejemplos.md#112-diseñar-una-evaluación-comparativa-justa)): mismo conjunto de prueba, mismos criterios, una sola variable cambiada.
- Seleccionar ejemplos representativos, equilibrados y no solapados con el conjunto de evaluación.
- Observar el efecto de añadir ejemplos y el punto de rendimientos decrecientes.
- Comprobar el efecto del orden y de los ejemplos sesgados.
- Calcular el coste en tokens de cada técnica y relacionarlo con la mejora.

Conceptos que se usan:

- **Zero-shot**. Solo instrucciones, sin ejemplos. Es lo más barato y funciona bien cuando la tarea es clara y las categorías son conocidas.
- **One-shot y few-shot**. Se añaden uno o varios pares entrada-salida como demostración. El modelo imita el formato y el criterio de los ejemplos sin reentrenamiento (aprendizaje en contexto).
- **Qué cambia con los ejemplos**. Fijan el formato de salida, aclaran los límites entre categorías y muestran cómo tratar los casos difíciles. También introducen sesgos: si todos los ejemplos son de una categoría, el modelo tiende a repetirla; si el último ejemplo es de una categoría, puede inclinar la respuesta.
- **Evaluación justa**. Los ejemplos del prompt **nunca deben ser casos del conjunto de prueba** (se estaría «copiando el examen»).

## Recursos necesarios

> Sin acceso a una API: Seguir el camino con chat con los 10 tickets de prueba de la muestra y comparar 0, 1 y 3 ejemplos, o usar el modo manual de los scripts con `--n 20`. Con un modelo local se ejecuta completo. Véase la [guía para trabajar sin API](../comun/sin-api.md).

- Un asistente de chat para el camino con chat; para el camino con código, además, Python 3.9 o superior y un modelo por API o local ([guía](../comun/README.md)).
- Datos en [`datos/`](datos/):
  - [`tickets_ejemplos.csv`](datos/tickets_ejemplos.csv): 54 tickets etiquetados (6 por cada una de las 9 categorías) para usar como ejemplos.
  - [`tickets_prueba.csv`](datos/tickets_prueba.csv): 147 tickets de prueba (135 normales, 12 «difíciles» con dos temas).
  - [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): hoja de cálculo con los diez tickets de la muestra del camino con chat; calcula la exactitud de cada condición.
- Script: [`evaluar_fewshot.py`](evaluar_fewshot.py).
- Alternativa manual: usar un chat con los 10 tickets de prueba de la muestra (P-001 a P-010); anotar los resultados en la hoja de resultados preparada.

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

Tiempo de ejecución con código (orientativo, medido con Gemma 4 de 8 B en local; con una API rápida y sin razonamiento suele ser bastante menos): una serie de los 147 tickets, de 1 a 4 minutos según el número de ejemplos; la curva `--k 0 1 3 8 16 --repeticiones 3`, unos 40 minutos (con `--n 20`, unos 5).

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: La Espiga quiere que un asistente clasifique mensajes de clientes en cuatro categorías (pedido, cambio, consulta o queja). Se mide cuántos ejemplos dentro del prompt hacen falta.

Paso 1 y 2: los datos y el prompt. Se tienen 10 mensajes con su categoría correcta, y dos de ellos son difíciles porque mezclan dos temas (por ejemplo, «cambiad mi pedido y, por cierto, ¿abrís el domingo?»). El prompt tiene una instrucción y, según la prueba, ningún ejemplo, uno o tres.

Paso 3: la curva. Se prueba con los 10 mensajes y se cuentan los aciertos.

| Ejemplos en el prompt | Aciertos | Exactitud | Aciertos en los 2 difíciles |
|---|---|---|---|
| 0 (zero-shot) | 5 de 10 | 50 % | 0 de 2 |
| 1 (one-shot) | 6 de 10 | 60 % | 0 de 2 |
| 3 (few-shot) | 8 de 10 | 80 % | 1 de 2 |

Cada ejemplo que se añade mejora el resultado, pero con solo diez mensajes un acierto de más son diez puntos: la conclusión es una pista, no una prueba.

Paso 4: ¿mejorar los ejemplos o mejorar la instrucción? Se comparan cuatro condiciones con los mismos 10 mensajes.

| Condición | Instrucción | Ejemplos | Aciertos | Mejora frente a A |
|---|---|---|---|---|
| A | base | seis al azar | 6 de 10 | referencia |
| B | base | seis de frontera (los casos difíciles) | 7 de 10 | +10 puntos |
| C | con definiciones de cada categoría | ninguno | 8 de 10 | +20 puntos |
| D | con definiciones | seis de frontera | 9 de 10 | +30 puntos |

En este caso, definir las categorías aporta más que elegir mejor los ejemplos, y las dos cosas juntas dan el mejor resultado. Nada de esto entrena al modelo: solo cambian las instrucciones que recibe en esa conversación.

Qué se espera ver en tu laboratorio: la misma tabla de la curva con los tickets de Altanoria, y las cuatro condiciones del Paso 4 con su mejora calculada.

## Pasos de ejecución

Los pasos se hacen en orden. Se puede seguir el camino con chat (con una muestra de 10 tickets) o el camino con código (con el conjunto completo y repeticiones). En los dos, los ejemplos y los tickets de prueba son conjuntos distintos que nunca se mezclan.

### Paso 1 · Revisar los datos (8 minutos)
1. Abrir [`datos/tickets_ejemplos.csv`](datos/tickets_ejemplos.csv): son los tickets con los que se construyen los ejemplos del prompt (columnas `id`, `texto` y `categoria`).
2. Abrir [`datos/tickets_prueba.csv`](datos/tickets_prueba.csv): son los tickets con los que se mide (las mismas columnas, más `dificil`, que marca los casos ambiguos).
3. Comprobar que ningún texto de la prueba aparece en los ejemplos: elegir tres tickets de prueba al azar, copiar una frase característica de cada uno y buscarla en el otro fichero (Ctrl+F). No debe estar. Si el conjunto de prueba se mezclara con el de ejemplos, la medida estaría falseada.

Comprobación: ningún ticket de prueba está también entre los ejemplos.

### Paso 2 · Entender cómo se construye el prompt (7 minutos)
Un prompt few-shot tiene siempre la misma forma: la instrucción, después los ejemplos (cada uno con su ticket y su categoría) y al final el ticket que se quiere clasificar, con la categoría en blanco para que el modelo la complete. Leer estas dos plantillas.

Zero-shot (sin ejemplos):

```text
Clasifica el ticket de soporte en UNA de estas categorías: facturacion, acceso, rendimiento, integracion, error, funcionalidad, seguridad, cancelacion, consulta. Si el ticket menciona varios temas, elige la categoría del PRIMER problema que describe. Responde únicamente con el nombre de la categoría, en minúsculas, sin negritas, sin puntuación y sin explicación.

Ticket: {texto}
Categoría:
```

Few-shot (con ejemplos):

```text
[misma instrucción]

Ticket: {texto del ejemplo 1}
Categoría: {categoria 1}

Ticket: {texto del ejemplo 2}
Categoría: {categoria 2}

Ticket: {texto a clasificar}
Categoría:
```

<details>
<summary>Con código: cómo funciona evaluar_fewshot.py</summary>

El script [`evaluar_fewshot.py`](evaluar_fewshot.py) construye los prompts de este paso, los envía al modelo y mide la exactitud. Para cada valor de `k` (el número de ejemplos) y cada repetición hace lo siguiente:

1. Lee los datos. Los ejemplos salen de `tickets_ejemplos.csv` (54, seis por categoría) y los tickets que se evalúan, de `tickets_prueba.csv` (147). Son ficheros distintos y nunca se mezclan, para no medir con lo que el modelo ya ha visto en el prompt.
2. Elige los ejemplos (función `elegir`). Con `k = 0` no hay ejemplos. Con `k` mayor toma ejemplos de forma equilibrada: uno de cada categoría, luego otro de cada una, y así hasta llegar a `k`; dentro de cada categoría los elige al azar con una semilla. Después los ordena según `--orden` (`aleatorio`, `agrupado` por categoría o `inverso`). Con `--sesgo acceso` solo usa ejemplos de esa categoría, para ver qué pasa cuando los ejemplos están desequilibrados.
3. Construye el prompt (función `construir`): la instrucción, los ejemplos (`Ticket:` y `Categoría:`) y, al final, el ticket a clasificar con la categoría en blanco. Es la forma de las plantillas de este paso.
4. Llama al modelo una vez por cada ticket de prueba, con temperatura 0 (la más determinista) y un tope de 2000 tokens. Solo se espera una palabra, así que un modelo normal usa 1 o 3 tokens; el tope existe para los modelos de razonamiento, que necesitan margen para pensar antes de contestar.
5. Interpreta la respuesta (función `primera_categoria`): busca la primera de las nueve categorías que aparece, y tolera negritas, comillas, puntuación o una explicación añadida. Si no encuentra ninguna, la respuesta cuenta como error.
6. Calcula la exactitud (aciertos entre tickets), los aciertos entre los casos difíciles (los 12 con dos temas), los tokens de entrada y, al final, el informe por categoría con precisión (de los tickets que marcó con esa categoría, cuántos lo eran), exhaustividad (de los que eran de esa categoría, cuántos encontró) y F1 (una media de las dos).

Las opciones del script son:

| Opción | Qué hace | Por defecto |
|---|---|---|
| `--k` | Lista de números de ejemplos que se comparan, por ejemplo `--k 0 1 3 8` | 0 1 3 8 |
| `--orden` | Orden de los ejemplos: `aleatorio`, `agrupado` o `inverso` | `aleatorio` |
| `--sesgo` | Usa solo ejemplos de una categoría, por ejemplo `--sesgo acceso` | ninguno |
| `--n` | Usa solo los `n` primeros tickets de prueba, para ahorrar tiempo y coste | todos |
| `--semilla` | Semilla de la selección de ejemplos | 1 |
| `--repeticiones` | Repite cada condición con semillas distintas y da la media y el rango | 1 |
| `--instruccion` | Usa el texto de un fichero como instrucción en lugar de la instrucción base, por ejemplo `datos/instruccion_con_definiciones.txt` | instrucción base |
| `--ids` | Usa exactamente los ejemplos indicados por su id, en lugar de `--k`, por ejemplo `--ids E-int-1 E-err-1` | ninguno |
| `--listar-ejemplos` | Muestra los ids y el texto de los ejemplos (de una categoría o de todas) y termina | desactivado |
| `--matriz` | Imprime la matriz de confusión y las cinco confusiones más frecuentes de la última serie | desactivado |
| `--max-tokens` | Tope de tokens de cada respuesta | 2000 |

Conviene saber:

- Cuántas llamadas hace. Los valores de `k`, por las repeticiones, por los tickets. Por ejemplo, `--k 0 1 3 8 16 24 --repeticiones 3` con los 147 tickets son unas 2.600 llamadas, con su tiempo y su coste. Con `--n 20` bastan unas 360.
- Qué varía entre repeticiones. Con temperatura 0 el modelo casi no cambia entre ejecuciones; lo que cambia en cada repetición es la selección de ejemplos (la semilla). Por eso el rango entre repeticiones mide cuánto depende el resultado de qué ejemplos se eligen.
- Si la exactitud baja a medida que se añaden ejemplos, o sale casi a cero. Mirar el aviso del script: si dice que muchas respuestas están vacías y han agotado el límite de tokens, el modelo gasta todo el límite razonando y no llega a escribir la categoría (ocurre con los modelos de razonamiento, y más con prompts largos). Repetir con un límite mucho mayor, por ejemplo `--max-tokens 4000` (empezando con `--n 40` para ver el coste), o usar un modelo sin razonamiento, que además es más barato para esta tarea. Con el tope por defecto de 2000, los modelos de razonamiento habituales suelen bastar.
- Dónde cambiar cosas. La instrucción está en `INSTR`, las categorías en `CATS` y la estrategia de selección de ejemplos en `elegir`, que es lo que se modifica en el Paso 4.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: los prompts zero-shot y few-shot están copiados en el documento, con la parte que los distingue (los ejemplos) marcada.

### Paso 3 · Medir la curva de aprendizaje (26 minutos)
Camino con chat:

1. Abrir [`datos/muestra_chat.md`](datos/muestra_chat.md). Contiene nueve ejemplos etiquetados (uno de cada categoría, para el prompt few-shot), diez tickets de prueba (P-001 a P-010) y, al final y plegadas, las respuestas correctas, que no hay que abrir todavía. Para anotar las categorías y calcular la exactitud de cada condición, usar la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx).
2. Zero-shot: abrir una conversación nueva, pegar la instrucción y, debajo, los diez tickets de prueba juntos, cada uno con su identificador (`P-001: …`, `P-002: …`), y pedir una categoría por línea con el formato `P-001: categoria`. Anotar las diez categorías. Pegar los diez a la vez ahorra treinta mensajes y sirve para comparar las tres condiciones; en el camino con código, cada ticket va en una llamada independiente.
3. Con un ejemplo: abrir otra conversación nueva y repetir lo mismo, pero con un único ejemplo etiquetado de la muestra entre la instrucción y los tickets.
4. Con tres ejemplos: otra conversación nueva, con tres ejemplos de categorías distintas entre la instrucción y los tickets.
5. Abrir las respuestas correctas y calcular, para 0, 1 y 3 ejemplos, cuántos de los diez tickets se clasifican bien (la pestaña «Casos» de la hoja tiene una fila por ticket y calcula los aciertos).

<details>
<summary>Con código: curva de 0 a 24 ejemplos con repeticiones</summary>

Abrir una terminal en la carpeta `laboratorios/04A` y ejecutar (antes, `python ../comun/comprobar_entorno.py`):

```bash
python evaluar_fewshot.py --k 0 1 3 8 16 24 --repeticiones 3
```

La opción `--repeticiones 3` repite cada condición con tres selecciones distintas de ejemplos, y el informe final da la exactitud media y el rango. Con `--n 60` se usan solo 60 tickets de prueba, que ahorra tiempo y coste a cambio de más ruido. Para una prueba rápida, `--k 0 1 3 --n 20`.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Anotar para cada número de ejemplos: la exactitud, cuántos casos difíciles acierta y (con código) los tokens de entrada. Si los rangos de dos valores se solapan, no se puede afirmar que uno sea mejor. Con solo 10 tickets de prueba, una diferencia de un caso son 10 puntos: interpretar con mucha cautela. La pestaña «Resultado» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) ya calcula la exactitud de cada condición y los aciertos en los casos difíciles.

Comprobación: la pestaña «Resultado» de la hoja (o la tabla del script) muestra la exactitud de, como mínimo, 0, 1 y 3 ejemplos.

### Paso 4 · Mejorar con diseño de ejemplos o de instrucción (14 minutos)
1. Mirar los errores de los pasos anteriores y anotar qué pares de categorías se confunden (por ejemplo, error y funcionalidad, o consulta y funcionalidad). Con código, la opción `--matriz` imprime la matriz de confusión y las confusiones más frecuentes.
2. Elegir a mano seis ejemplos del CSV de ejemplos pensando en esos pares: uno que marque el límite en cada dirección. Con código, `python evaluar_fewshot.py --listar-ejemplos` (o `--listar-ejemplos integracion`) muestra los ids y los textos de los ejemplos.
3. Repetir la medida con esos seis ejemplos y compararla con seis ejemplos equilibrados al azar.
4. Probar la otra palanca: en lugar de añadir ejemplos, definir las categorías en la instrucción. En el chat, pegar la instrucción de [`datos/instruccion_con_definiciones.txt`](datos/instruccion_con_definiciones.txt) en lugar de la instrucción base, primero sin ejemplos y después con los seis de frontera. Esa instrucción define cada categoría y dice dónde está la frontera con las vecinas (por ejemplo, `integracion` son los conectores, las API y los webhooks, y `error` un defecto del producto que no es de integración).
5. Comparar las cuatro medidas con los mismos tickets de prueba: instrucción base con seis ejemplos al azar, instrucción base con seis de frontera, instrucción con definiciones sin ejemplos e instrucción con definiciones con los seis de frontera. ¿Qué mejora más: definir o ejemplificar? ¿Qué cuesta menos en tokens?
6. Con las definiciones ya puestas, comprobar si los ejemplos aportan algo más: comparar las definiciones sin ejemplos con las definiciones y seis ejemplos al azar, con tres selecciones distintas si se puede. Si los rangos se solapan, no se puede afirmar que los ejemplos mejoren, y cada uno sigue costando tokens.

<details>
<summary>Con código: ejemplos elegidos a mano con --ids</summary>

La opción `--ids` usa exactamente los ejemplos que se indican (por sus ids), sin tocar el código. Como los ejemplos y la temperatura (0) no cambian, basta con una serie. Una selección posible para los pares que más se confunden:

| Frontera | Ejemplos |
|---|---|
| `integracion` y `error` | `E-int-1` (un conector que no sincroniza) y `E-err-1` (un botón que no funciona) |
| `funcionalidad` y `seguridad` | `E-fun-3` (pedir exportar a PDF) y `E-seg-6` (pedir el registro de auditoría) |
| `facturacion` y `cancelacion` | `E-fac-6` (dos cargos iguales con petición de devolución) y `E-can-4` (cancelar un plan anual a los 12 días) |

En la terminal, en la carpeta `laboratorios/04A`:

```bash
python evaluar_fewshot.py --ids E-int-1 E-err-1 E-fun-3 E-seg-6 E-fac-6 E-can-4 --matriz
python evaluar_fewshot.py --k 6 --repeticiones 3 --matriz
```

El primer comando mide los seis ejemplos elegidos; el segundo, seis ejemplos equilibrados al azar con tres selecciones distintas. Si los seis elegidos mejoran la exhaustividad de las categorías confusas (en la matriz, bajan las confusiones de esos pares) y la exactitud queda por encima del rango de los seis al azar, el diseño de los ejemplos ayuda; si no, no se puede afirmar. Probar también otros pares de ejemplos y otras fronteras: es el experimento del paso.

Para comparar con la instrucción que define las categorías, la opción `--instruccion` usa el texto de un fichero en lugar de la instrucción base:

```bash
python evaluar_fewshot.py --k 0 --instruccion datos/instruccion_con_definiciones.txt --matriz
python evaluar_fewshot.py --ids E-int-1 E-err-1 E-fun-3 E-seg-6 E-fac-6 E-can-4 --instruccion datos/instruccion_con_definiciones.txt --matriz
python evaluar_fewshot.py --k 6 --repeticiones 3 --instruccion datos/instruccion_con_definiciones.txt
```

El primer comando mide solo las definiciones, sin ejemplos; el segundo, las definiciones con los seis ejemplos de frontera; el tercero, las definiciones con seis ejemplos al azar y tres selecciones distintas, que da el rango necesario para saber si los ejemplos aportan algo con las definiciones ya puestas. Con el resultado de los comandos anteriores se tienen las cuatro medidas. Fíjate en el coste: tanto las definiciones como los ejemplos viajan en cada llamada. Con el tokenizador de un modelo de tipo Gemma, las definiciones añaden del orden de 200 tokens por ticket y cada ejemplo, unos 50, de modo que las definiciones cuestan como cuatro ejemplos. Compara qué mejora cada una por token.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: hay una comparación entre seis ejemplos elegidos a mano y seis al azar, y otra entre mejorar los ejemplos y mejorar la instrucción (en la pestaña «Paso 4» de la hoja, con las cuatro medidas).

## Conclusiones

### Qué se ha conseguido

Se ha medido cómo cambia la calidad de una clasificación al pasar de ninguna demostración a una o varias, y se ha visto que más ejemplos no garantizan mejor resultado: la curva suele subir con los primeros ejemplos y después es irregular o plana, y cuesta mucho más en tokens. Se ha visto también que una sola ejecución puede engañar, que la elección de los ejemplos (cuáles y de qué categorías) importa tanto como su número, y que los ejemplos que marcan el límite entre categorías vecinas valen más que los fáciles. La recomendación práctica es empezar con pocos ejemplos bien elegidos, medir con repeticiones y detenerse cuando la curva deja de subir.

Referencia orientativa (rangos amplios con un modelo pequeño; con otro modelo pueden variar): Con 0 ejemplos se esperan entre el 50 % y el 75 % de exactitud, y con 1 a 8 ejemplos entre el 55 % y el 80 %; definir las categorías en la instrucción puede subir 5 o 10 puntos más que añadir ejemplos. La curva puede ser plana o no creciente y la selección de ejemplos cambia el resultado hasta 10 o 15 puntos: conviene comparar rangos de varias repeticiones (`--repeticiones 3`), no puntos sueltos. Si el resultado queda muy lejos, conviene revisar datos, prompt y script antes de abrir la solución.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿A partir de qué número de ejemplos deja de compensar añadir más?

   <details>
   <summary>Respuesta</summary>

   En la medición (147 casos, tres selecciones de ejemplos por condición) la curva fue prácticamente plana: 70,7 % con 0 ejemplos, 70,7 % con 1, 70,3 % con 3, 69,2 % con 8 y 72,3 % con 16, con rangos entre selecciones que se solapan salvo en el caso de 16 frente a 0 (1,6 puntos más por unas seis veces más tokens). Con esta instrucción y este modelo los ejemplos no aportaron una mejora apreciable, así que una sola serie puede engañar. Conviene medir antes de añadir ejemplos, repetir la medición y detenerse cuando la curva deja de subir.

   </details>

2. ¿El orden importó más o menos que el número de ejemplos?

   <details>
   <summary>Respuesta</summary>

   Con orden agrupado y 8 ejemplos, tres selecciones dieron 61,5 %, frente al 59,2 % del orden aleatorio: no hay diferencia apreciable. La variación entre selecciones es mayor que el efecto del orden, y por eso conviene repetir antes de concluir.

   </details>

3. ¿Qué categorías confundió el modelo y qué ejemplo concreto lo corregiría?

   <details>
   <summary>Respuesta</summary>

   Suelen confundirse categorías vecinas: error y funcionalidad, rendimiento y error, seguridad y acceso. Se corrigen con ejemplos que marquen el límite (un fallo visual es error; una pregunta sobre si existe una función es funcionalidad; una pregunta sobre precios o condiciones es consulta).

   </details>

4. ¿Cómo cambiaría la respuesta con una tarea con muchas más categorías o con categorías que cambian con frecuencia?

   <details>
   <summary>Respuesta</summary>

   Con muchas categorías hacen falta más ejemplos por categoría o seleccionar dinámicamente los ejemplos más parecidos al caso; con categorías cambiantes, ejemplos y definiciones versionados y revisados con una suite de pruebas.

   </details>

5. ¿Qué alternativa a añadir ejemplos tiene el equipo si el prompt se hace demasiado largo? (Véase el módulo 07: optimización y coste.)

   <details>
   <summary>Respuesta</summary>

   Seleccionar los ejemplos de forma dinámica, acortar las instrucciones, usar caché de prefijo, emplear un modelo más pequeño con pocos ejemplos buenos o, si el volumen lo justifica, ajustar un modelo.

   </details>

6. Redactar la recomendación en cinco líneas: ¿cuántos ejemplos se recomendaría usar y por qué?, ¿qué relación coste y beneficio tiene cada opción?, ¿qué riesgos tiene un conjunto de ejemplos mal elegido? Citar al menos dos cifras medidas y distinguir la mejora por encima del ruido de la anecdótica.

   <details>
   <summary>Respuesta</summary>

   «No se recomienda añadir ejemplos a la instrucción base: la exactitud fue del 70,7 % con 0 ejemplos y del 70,7 % con seis al azar (rango 69,4 – 72,8), y 16 ejemplos (72,3 %) costaron casi seis veces más tokens de entrada. Lo que sí mejoró fue definir las categorías en la instrucción (81,0 % sin ejemplos), con un coste de unos 200 tokens por ticket. El zero-shot es suficiente si el coste de equivocarse es bajo; en producción, los ejemplos pueden dar estabilidad de formato. Los riesgos de los ejemplos son: solapamiento con el conjunto de prueba (evaluación inflada), desequilibrio entre categorías (sesgo) y ejemplos obsoletos si las categorías cambian.»

   </details>

7. ¿Qué rinde más por token en este problema: definir las categorías en la instrucción o añadir ejemplos? ¿Cuándo convendría usar cada una?

   <details>
   <summary>Respuesta</summary>

   Depende del modelo y de la tarea, y se decide midiendo con los mismos tickets. Con Gemma en local (147 tickets de prueba): con la instrucción base, seis ejemplos al azar o de frontera quedan en torno al 70 % (68,0 % los de frontera); con definiciones y sin ejemplos, 81,0 %; con definiciones y seis ejemplos de frontera, 79,6 %; con definiciones y seis ejemplos al azar en tres selecciones, 80,7 % (79,6 – 81,6). Los rangos se solapan: con las definiciones puestas no se puede afirmar que los ejemplos mejoren, y cada uno añade unos 50 tokens por ticket (seis ejemplos, del orden de un 80 % más de entrada). Las definiciones añaden del orden de 200 tokens por ticket, el equivalente a cuatro ejemplos, y corrigen las confusiones que vienen de nombres ambiguos (por ejemplo, «integración» frente a «error»). Lo recomendable es definir primero las categorías, medir, y añadir ejemplos solo si quedan pares confundidos que las palabras no resuelven y la medida muestra una mejora por encima del rango. Con otro modelo el reparto puede ser distinto: no hay que dar por buena la regla, sino repetir la medida. Si hay desacuerdo entre las definiciones y las etiquetas de los datos, el problema está en los datos o en las definiciones, no en el modelo.

   </details>

### Autoevaluación

- [ ] Los ejemplos del prompt no están en el conjunto de prueba.
- [ ] En cada comparación solo cambia una variable (*k*, orden o sesgo).
- [ ] Se usó el mismo conjunto de prueba (y el mismo `--n`) en todas las variantes.
- [ ] Se repitió con varias semillas antes de sacar conclusiones sobre el orden.
- [ ] Se analizó al menos una matriz de confusión.
- [ ] Se contabilizó el coste en tokens.
- [ ] La recomendación distingue la mejora estadística (por encima del ruido) de la anecdótica.

### Errores típicos

- Usar ejemplos tomados del conjunto de prueba.
- Comparar con un conjunto de prueba distinto en cada ejecución.
- Concluir sobre el orden con una sola semilla.
- Elegir ejemplos «fáciles» y esperar que cubran los casos difíciles.
- Olvidar que más ejemplos significan más tokens en cada llamada.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

> Con modelos actuales, el zero-shot ya rinde bien en una tarea de nueve categorías, con algunas fronteras difusas. Los resultados exactos varían; lo valioso es el patrón y el análisis de los errores.

### Patrón de resultados esperado — expectativa previa a la medición

| *k* | Exactitud típica (prueba normal) | Casos difíciles | Tokens de entrada (relativo) |
|---|---|---|---|
| 0 (zero-shot) | 50–80 % | 6–10 de 12 | 1× |
| 1 (one-shot) | similar o algo mejor; fija el formato de salida | 6–10 | ≈ 1,3× |
| 3 | −2 a +4 puntos | 6–10 | ≈ 1,8× |
| 8 | −3 a +6 puntos | 6–10 | ≈ 3× |
| 16–24 | meseta: mejora marginal o nula | 6–10 | ≈ 5–7× |

Lectura:

- Los primeros ejemplos fijan el formato y los límites entre categorías; después la mejora es irregular y depende de qué ejemplos se elijan.
- Desde unos 8 ejemplos suele haber rendimientos decrecientes y el coste de tokens crece de forma lineal.
- Los casos difíciles (dos temas) mejoran poco con ejemplos fáciles: hace falta incluir ejemplos de casos difíciles con la regla («se clasifica por el primer problema descrito»).

### Orden y sesgo

- Orden: el efecto suele ser pequeño pero real (de 1 a 3 puntos). Con tres semillas se ve que la variación entre órdenes se mezcla con la variación entre muestras: sin repeticiones no se puede concluir. El orden «agrupado» tiende a sesgar hacia la última categoría vista.
- Sesgo: con ejemplos solo de `acceso` el modelo tiende a clasificar más tickets como `acceso`, especialmente los ambiguos (por ejemplo, tickets de `seguridad` que mencionan inicio de sesión). En la matriz de confusión se ve una columna `acceso` inflada. Con 6 ejemplos solo de `seguridad` ocurre algo parecido: más falsas alarmas de seguridad.

### Ejemplos seleccionados a mano (Paso 4)

Una buena selección de 6 ejemplos:

1. Un `facturacion` con cobro duplicado.
2. Un `acceso` por SSO caído (no confundir con rendimiento).
3. Un `rendimiento` con lentitud ocasional (para separarlo de `error`).
4. Un `error` con solución alternativa.
5. Un `seguridad` con consulta de cumplimiento (no urgente), para evitar que todo `seguridad` sea P1.
6. Un ticket difícil con dos temas y la categoría del primer problema descrito (la regla del enunciado).

La idea es que los ejemplos marquen la frontera entre las categorías que más se confunden, y no que sean muchos: la calidad y la diversidad deberían pesar más que la cantidad.

> Depende del modelo y de la muestra. Es una expectativa previa, no un resultado: en la medición con Gemma 4, seis ejemplos de frontera (67,3 %) no superaron a seis al azar (70,7 %, rango 69,4 – 72,8), mientras que definir las categorías sin ejemplos subió la exactitud del 70,7 % al 81,0 %, y añadir seis ejemplos a las definiciones no la mejoró (80,7 %, rango 78,9 – 82,3). No des por buena la regla: compara tus cuatro medidas con los mismos tickets y decide con tus propias cifras. Con 10 tickets de prueba una diferencia de uno o dos aciertos es ruido.

### Resultados medidos con un modelo real

> Medición realizada el 24 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada a 16.384 tokens, una ejecución por condición (salvo donde se indica) y los scripts de este laboratorio. Los conjuntos de desarrollo y prueba están separados por escenario (ninguna situación de dev aparece en test, ni siquiera reformulada). Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

Clasificación de los 147 tickets de prueba en 9 categorías, con tres selecciones distintas de ejemplos por condición (`--repeticiones 3`). Exactitud media y rango entre selecciones:

| Ejemplos (*k*) | Exactitud media (rango entre selecciones) | Tokens de entrada |
|---|---|---|
| 0 | 70,7 % (70,7 – 70,7) | 23.114 |
| 1 | 70,7 % (70,7 – 70,7) | 30.758 |
| 3 | 70,3 % (68,7 – 72,8) | 44.576 |
| 8 | 69,2 % (66,0 – 71,4) | 78.239 |
| 16 | 72,3 % (71,4 – 73,5) | 133.511 |

- La curva es prácticamente plana: 70,7 % sin ejemplos y entre el 69 % y el 72 % con cualquier número de ellos, con rangos que se solapan. Más ejemplos no mejoraron el resultado de forma apreciable, y 16 ejemplos cuestan casi seis veces más tokens que 0. Con la instrucción base, que solo nombra las categorías, los ejemplos no añaden información que el modelo no tuviera.
- Los casos más confundidos con la instrucción base fueron `integracion` (que el modelo clasifica como `rendimiento` o `error`) y `funcionalidad` (como `consulta` o `integracion`), además de `facturacion` frente a `consulta` y `cancelacion`; por eso el Paso 4 pide elegir ejemplos que marquen la frontera en lugar de añadirlos al azar, y compararlos con definir las categorías.
- Orden (*k* = 8, tres selecciones): aleatorio, 69,2 % (66,0 – 71,4); agrupado por categoría, 68,3 % (68,0 – 68,7); inverso, 70,5 % (69,4 – 72,1). Las diferencias están dentro del ruido.
- Sesgo (*k* = 6, una selección): seis ejemplos solo de `acceso` dieron 67,3 % y seis solo de `seguridad`, 70,7 %, frente al 70,7 % (69,4 – 72,8) de seis ejemplos equilibrados al azar: con una sola serie no se puede afirmar un efecto, aunque los de `acceso` quedaron algo por debajo.
- Diseño de los ejemplos y de la instrucción (paso 4): seis ejemplos de frontera elegidos a mano dieron 67,3 %, sin mejorar a los seis al azar (70,7 %). Definir las categorías en la instrucción, sin ejemplos, subió la exactitud al 81,0 % (con unos 200 tokens más por ticket, el equivalente a cuatro ejemplos); añadir a las definiciones los seis ejemplos de frontera dio 79,6 % y seis ejemplos al azar (tres selecciones), 80,7 % (78,9 – 82,3): con las definiciones puestas, los ejemplos no aportaron una mejora apreciable y casi duplicaron los tokens de entrada.
- Lección práctica: una medición depende de cómo se extrae la respuesta y del límite de tokens. Si el script interpreta mal las respuestas (por ejemplo, cuando vienen en negrita) o, con un límite bajo, un modelo de razonamiento como Gemma 4 devuelve respuestas vacías que se cuentan como errores, la exactitud sale muy baja sin que el prompt tenga la culpa. Por eso el script usa un límite por defecto de 2.000 tokens y avisa de las respuestas vacías. Antes de interpretar una curva, comprobar que el extractor y el límite no son la causa.

</details>

### Para seguir

- Probar el efecto del orden de los ejemplos. En el chat, repetir la condición de tres ejemplos del Paso 3 cambiando el orden en que se muestran (agrupados por categoría y al revés); con código: `python evaluar_fewshot.py --k 8 --orden aleatorio --repeticiones 3`, y lo mismo con `--orden agrupado` y `--orden inverso`. Si la variación entre repeticiones es del mismo tamaño que la diferencia entre órdenes, no se puede concluir nada.
- Probar el efecto del sesgo. En el chat, repetir el Paso 3 con tres ejemplos que sean todos de la categoría `acceso`; con código: `python evaluar_fewshot.py --k 6 --sesgo acceso` y `--sesgo seguridad`. Comparar con los ejemplos equilibrados y mirar a qué categoría se inclina el modelo cuando se equivoca.
- Seleccionar ejemplos similares al ticket que se va a clasificar (por palabras compartidas) en lugar de fijos.
- Probar un formato de ejemplo distinto (por ejemplo, con una breve justificación) y medir la exactitud y los tokens.
- Repetir con un modelo más pequeño y comprobar si el beneficio de los ejemplos es mayor.

---

[← Laboratorios](../README.md) · [Módulo 04](../../modulos/04-tecnicas-avanzadas-de-prompting/README.md) · [← 03B](../03B/README.md) · [04B →](../04B/README.md)
