[← Laboratorios](../README.md) · [Módulo 01](../../modulos/01-introduccion-a-los-llm/README.md) · [01B →](../01B/README.md)

# Laboratorio 01A · Tokens, ventana de contexto y coste

Módulo 01 · Introducción a los LLM · Duración estimada: 65 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Medir cómo se tokeniza el texto, estimar el coste anual de un asistente de soporte y comprobar si un documento largo que «cabe» en la ventana se aprovecha bien. |
| Conviene haber hecho antes | Nada; si es tu primer laboratorio, lee antes [Antes de empezar](../comun/antes-de-empezar.md) (30 minutos, sin programar) |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Parte A · Medir cómo se tokeniza el texto
  - Paso 1 · Medir cómo se tokeniza el texto y ordenar la tabla (12 min)
  - Paso 2 · Responder a las preguntas sobre la tabla (6 min)
  - Paso 3 · Deducir una regla práctica (4 min)
- Parte B · Estimar el coste anual
  - Paso 4 · Calcular el total de tickets del año (7 min)
  - Paso 5 · Convertir las palabras a tokens (5 min)
  - Paso 6 · Calcular el coste anual de cada modelo (6 min)
  - Paso 7 · Interpretar el coste (5 min)
- Parte C · La ventana de contexto
  - Paso 8 · La ventana de contexto y el experimento de la aguja en el pajar (14 min)
  - Paso 9 · Responder a Dirección (6 min)

<details>
<summary>Secciones del módulo relacionadas (4)</summary>

- [§3.1 Concepto de tokenización](../../modulos/01-introduccion-a-los-llm/03-como-funciona-un-llm.md#31-concepto-de-tokenización)
- [§3.2 Del texto a las representaciones vectoriales: embeddings](../../modulos/01-introduccion-a-los-llm/03-como-funciona-un-llm.md#32-del-texto-a-las-representaciones-vectoriales-embeddings)
- [§4.2 Preentrenamiento y ajuste posterior](../../modulos/01-introduccion-a-los-llm/04-entrenamiento-contexto-y-generacion.md#42-preentrenamiento-y-ajuste-posterior)
- [§4.3 Ventana de contexto (Context Window)](../../modulos/01-introduccion-a-los-llm/04-entrenamiento-contexto-y-generacion.md#43-ventana-de-contexto-context-window)

</details>

## Justificación del laboratorio

Dirección de Altanoria quiere añadir a su soporte un asistente que clasifique cada ticket y redacte un borrador de respuesta, y antes de aprobar el proyecto hace tres preguntas muy prácticas: cuánto costará al año, si cabe en un modelo pequeño o hace falta uno grande, y qué pasa si se pega en el prompt toda la documentación de la empresa. Ninguna de las tres se puede contestar sin entender una idea que casi todo el mundo da por supuesta y que es falsa: que un modelo de lenguaje lee palabras.

No las lee. Trabaja con tokens, fragmentos de texto que pueden ser una palabra, media palabra, un signo o un dígito. El coste de cada llamada, el límite de lo que cabe en una conversación y hasta la fiabilidad con la que el modelo recuerda un dato dependen de cuántos tokens hay, no de cuántas palabras. Un presupuesto hecho contando palabras sale mal, y un documento que «cabe» en la ventana de contexto no siempre se aprovecha bien.

En este laboratorio se mide todo con textos y datos de la propia empresa: primero cómo se tokeniza el texto (el español, el código, los números, los emojis), después cuánto costaría el proyecto durante un año con precios de modelos ficticios, y por último qué ocurre cuando se le da al modelo un documento muy largo y se le pregunta por un dato escondido en él. Al final se podrá contestar a Dirección con cifras propias.

## Objetivos

Comprobar de forma empírica que un modelo de lenguaje trabaja con tokens y no con palabras, y aprender a estimar con ello tres magnitudes que condicionan cualquier proyecto: el coste, el límite de contexto y la fiabilidad de la información situada en distintas posiciones del contexto.

Al terminar el laboratorio se habrá conseguido:

- Cuántos tokens consume el mismo contenido según el idioma, el tipo de texto y los caracteres especiales.
- Por qué «mil palabras» no equivalen a una cantidad fija de tokens.
- Cómo estimar el coste anual de una aplicación a partir de un volumen real de uso.
- Qué ocurre cuando un documento se acerca al límite de la ventana de contexto y por qué «caber» no significa «ser tenido en cuenta».

Conceptos que se usan:

- **Token**. Unidad de texto que procesa el modelo:
  - puede ser una palabra
  - una parte de una palabra
  - un signo
  - unos pocos caracteres

  Cada proveedor usa su propio tokenizador; por eso el mismo texto produce recuentos diferentes en modelos diferentes.

- **Ventana de contexto**. Cantidad máxima de tokens que el modelo puede manejar en una solicitud, sumando entrada y salida. Si el texto de entrada ocupa casi toda la ventana, queda poco espacio para la respuesta.
- **Coste**. Los proveedores cobran por tokens, con un precio para los de entrada y otro, normalmente mayor, para los de salida. Coste = (tokens de entrada × precio de entrada + tokens de salida × precio de salida) / 1.000.000, si los precios son por millón de tokens.
- **Estimación frente a medición**. Para planificar basta una estimación; para facturar o diseñar límites hay que usar el recuento que informa la API de cada proveedor (campo de uso o `usage`).

## Recursos necesarios

> Sin acceso a una API: El recuento de tokens funciona sin API (con la estimación del script) y la Parte C se hace en un chat con un documento más corto si el chat tiene límites. Véase la [guía para trabajar sin API](../comun/sin-api.md).

- Un visor de tokens en línea del proveedor que se prefiera (casi todos ofrecen uno), o el script [`contar_tokens.py`](contar_tokens.py) de este laboratorio.
  - Sin dependencias, el script estima (caracteres ÷ 3,6). Con `pip install tiktoken` pasa a usar un tokenizador real. Ninguna de las dos opciones coincide exactamente con el tokenizador de un proveedor concreto: sirven para comparar tendencias.
- Tokenizadores interactivos (comprobados el 9 de noviembre de 2026; dan una estimación, porque cada proveedor usa su propio tokenizador):

| Herramienta | Dirección |
|---|---|
| Tiktokenizer: muestra los tokens de las codificaciones de OpenAI, en el navegador | https://tiktokenizer.vercel.app |
| Tokenizer Playground (Hugging Face): tokenizadores de modelos abiertos como Llama o Mistral | https://huggingface.co/spaces/Xenova/the-tokenizer-playground |

- Un asistente de chat con ventana de contexto grande (para la Parte C).
- Opcional: Python 3.9 o superior.
- Datos (carpeta [`datos/`](datos/)):
  - [`corpus_tokenizacion.csv`](datos/corpus_tokenizacion.csv): 43 textos de tipos muy distintos.
  - [`precios_modelos_ficticios.csv`](datos/precios_modelos_ficticios.csv): precios y ventanas de cuatro modelos ficticios.
  - [`volumen_tickets_2026.csv`](datos/volumen_tickets_2026.csv): tickets mensuales de Altanoria por producto.
  - [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): hoja de cálculo preparada para anotar los tokens del corpus y calcular el coste por modelo (también sirve para el camino con chat).
  - [`registro_de_cambios.md`](datos/registro_de_cambios.md): documento largo (240 entradas).
  - [`construir_contexto.py`](construir_contexto.py): genera documentos de la longitud que se desee, con «agujas» escondidas en el pajar para la Parte C.

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

Tiempo de ejecución con código (orientativo, medido con Gemma 4 de 8 B en local; con una API rápida y sin razonamiento suele ser bastante menos): `contar_tokens.py` es inmediato; en el experimento de la aguja con un documento de unos 100.000 tokens, la primera pregunta tarda unos 35 segundos (el modelo lee el documento) y las siguientes, unos segundos.

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: La Espiga quiere saber cuánto costaría que un asistente redactara un borrador de respuesta a cada mensaje de WhatsApp que recibe. Las cifras de este ejemplo son inventadas para que las cuentas salgan limpias.

Paso 1 y 2: medir cómo se trocea el texto. Se pegan tres textos en el visor de tokens y se anotan los resultados.

| Texto | Palabras | Tokens | Tokens por palabra |
|---|---|---|---|
| Frase en español: «Quiero dos barras de pan para mañana a las nueve» | 12 | 20 | 1,7 |
| La misma frase en inglés | 12 | 15 | 1,3 |
| Un código de pedido: «ES-2026-000451» | 1 | 9 | 9,0 |

Lo que se aprende: el español sale más caro que el inglés por palabra, y los códigos y los números son lo más caro de todo.

Paso 3: una regla práctica. Con el español en prosa: «un texto de N palabras ocupa unos 1,7 tokens por palabra».

Pasos 4 y 5: el volumen y los tokens del año. La Espiga recibe 1.200 mensajes al mes, de 30 palabras de media, y quiere respuestas de 80 palabras; las instrucciones fijas ocupan 400 tokens.

| Medida | Cálculo | Resultado |
|---|---|---|
| Mensajes al año | 1.200 × 12 | 14.400 |
| Tokens de entrada por mensaje | 400 + 30 × 1,7 | 451 |
| Tokens de entrada al año | 14.400 × 451 | 6.494.400 |
| Tokens de salida por mensaje | 80 × 1,7 | 136 |
| Tokens de salida al año | 14.400 × 136 | 1.958.400 |

Paso 6: el coste con dos modelos de precios inventados (euros por millón de tokens).

| Modelo | Entrada | Salida | Coste de entrada | Coste de salida | Total al año |
|---|---|---|---|---|---|
| Pequeño | 0,10 | 0,40 | 0,65 € | 0,78 € | 1,43 € |
| Grande | 3,00 | 12,00 | 19,48 € | 23,50 € | 42,98 € |

Paso 7: interpretar. El grande cuesta unas 30 veces más que el pequeño, y en los dos casos la salida pesa un poco más que la entrada (un 55 %), porque cada token escrito se paga más caro que uno leído. Si la respuesta se limitara a 40 palabras, la salida se reduciría a la mitad.

Paso 8: la aguja en el pajar. Se pega una lista de 40 precios y se pregunta por tres productos, uno al principio, uno en medio y otro al final.

| Pregunta | Posición | ¿Acierta? | ¿Sonaba seguro? |
|---|---|---|---|
| Precio de la barra | principio | sí | sí |
| Precio del roscón | medio | sí | sí |
| Precio de las magdalenas | final | no | sí |

Que un texto quepa en la ventana de contexto no significa que se use bien: el modelo puede fallar un dato y sonar igual de seguro. Por eso conviene no pegar documentos enteros cuando basta con el fragmento que importa.

Qué se espera ver en tu laboratorio: la misma cadena de cálculos con los datos de Altanoria, en la hoja, y un párrafo final para Dirección con tres cifras.

## Pasos de ejecución

Los pasos están pensados para hacerse en orden y se agrupan en tres partes: A (medir cómo se tokeniza), B (estimar el coste anual) y C (la ventana de contexto). En cada paso se indica qué hacer, qué se debería ver y, cuando existe, la alternativa con código. En el documento de resultados se anota todo lo que cada paso pide anotar.

Dos herramientas de apoyo según el camino. Camino con chat: un visor de tokens en el navegador (por ejemplo, Tiktokenizer, https://tiktokenizer.vercel.app: se pega el texto y muestra los tokens que cuenta). Camino con código: el script `contar_tokens.py` de este laboratorio. Los dos dan una estimación; el recuento exacto es siempre el que informa el proveedor al responder.

### Parte A · Medir cómo se tokeniza el texto

#### Paso 1 · Medir cómo se tokeniza el texto y ordenar la tabla (12 minutos)
1. Abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), pestaña «Corpus»: tiene los 43 textos de tipos muy distintos, con las columnas `id`, `tipo`, `idioma` y `texto`, y calcula sola los caracteres, las palabras y las razones por palabra y por carácter. Los mismos textos están en [`datos/corpus_tokenizacion.csv`](datos/corpus_tokenizacion.csv), que usa el script del camino con código.
2. Abrir el visor de tokens en el navegador.
3. Copiar el primer texto de la columna `texto` y pegarlo en el visor. Anotar el número de tokens que indica (suele aparecer como «Token count»).
4. Hacer lo mismo con, al menos, estos textos: los números 1 a 5, 11 a 15, 34 y 35, y un texto de cada uno de estos tipos: código o JSON, números o fechas, emojis y un alfabeto distinto del latino (japonés, ruso, árabe o chino).
5. Escribir el número de tokens que dio el visor en la columna amarilla «tokens (anotar)» de cada texto medido; las demás columnas de la fila se calculan solas.
6. Ordenar la tabla por tokens por palabra, de mayor a menor (Datos > Ordenar), para ver de un vistazo qué textos «salen más caros». La pestaña «Resumen del corpus» da las medias por tipo de texto y por idioma, que sirven para el Paso 2.

<details>
<summary>Con código: medir los 43 textos de una vez</summary>

Abrir una terminal en la carpeta `laboratorios/01A` y ejecutar:

```bash
python contar_tokens.py --csv datos/corpus_tokenizacion.csv --col texto
```

Imprime una fila por texto con los caracteres, las palabras y los tokens. Sin dependencias, el script estima (caracteres entre 3,6); con `pip install tiktoken` usa un tokenizador real. Copiar la salida en el documento.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: la hoja tiene, como mínimo, 12 textos con sus caracteres, palabras y tokens, y la tabla está ordenada por tokens por palabra.

#### Paso 2 · Responder a las preguntas sobre la tabla (6 minutos)
Con la tabla delante, responder por escrito (una frase cada una, con el número que lo respalda):

1. ¿Cuántos tokens por palabra consume el español en prosa? ¿Y el inglés? ¿Cuál de los dos sale más caro?
2. ¿Cambia el recuento si se eliminan las tildes (textos 2 y 3)? ¿Por qué podría cambiar?
3. ¿Cómo se comportan las palabras largas y técnicas (textos 11 a 15)?
4. ¿Qué ocurre con el código, el JSON y el YAML frente a la prosa?
5. ¿Y con números, fechas, IBAN y teléfonos? ¿Cuánto cuesta un dígito?
6. ¿Y con emojis y símbolos? Comparar cinco emojis seguidos con una frase de agradecimiento con emojis.
7. ¿Y con otros alfabetos? ¿Cuánto más consumen por carácter?
8. Texto en mayúsculas frente a minúsculas (textos 34 y 35): ¿hay diferencia?
9. ¿Se comprimen las repeticiones (`aaaa…`, `ja ja ja…`)? ¿Qué implica para los costes?

Comprobación: nueve respuestas, cada una con un número. No hay respuestas «de memoria».

#### Paso 3 · Deducir una regla práctica (4 minutos)
Con los datos del español en prosa, completar esta frase con un número: «en español, un texto de N palabras ocupa aproximadamente ___ tokens por palabra». Se usará en la Parte B. Una regla sencilla vale: un número con un decimal.

Comprobación: la regla está escrita con un número concreto.

### Parte B · Estimar el coste anual

#### Paso 4 · Calcular el total de tickets del año (7 minutos)
1. Abrir la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), pestaña «Volumen y coste». Tiene 36 filas: 12 meses por 3 productos, con las columnas A (mes), B (producto), C (tickets recibidos), D (palabras de media por ticket) y E (palabras de media por respuesta); el resto de columnas se calcula a partir de ellas y de la pestaña «Precios».
2. Localizar la fila «Total año», al final de la tabla: la columna C da el total anual de tickets.
3. En la misma fila, la columna D es la media ponderada de palabras por ticket, que da más peso a los meses con más tickets (en la hoja, `=SUMAPRODUCT(C4:C39;D4:D39)/SUMA(C4:C39)`). Comprobar a mano un mes para entender qué se está ponderando.
4. La columna E de la fila «Total año» es lo mismo para las palabras por respuesta.

Comprobación: hay tres números anotados: total de tickets, palabras medias por ticket y palabras medias por respuesta.

#### Paso 5 · Convertir las palabras a tokens (5 minutos)
Supuesto del diseño: cada ticket se procesa con una sola llamada; el prompt contiene unas instrucciones fijas (se suponen 600 tokens) más el texto del ticket, y el modelo devuelve el borrador de respuesta.

1. En la pestaña «Precios», escribir en la celda amarilla «Tokens por palabra» la regla del Paso 3 (la hoja trae 1,7 como valor de partida) y dejar los 600 tokens fijos de instrucciones. La hoja calcula los tokens de entrada de todo el año: total de tickets por (600 más las palabras medias por ticket multiplicadas por la regla). Está en la fila «Total año» de «Volumen y coste», columna F.
2. La columna G de la misma fila son los tokens de salida: total de tickets por (palabras medias por respuesta multiplicadas por la regla).

Comprobación: quedan dos números grandes (en millones o miles de millones de tokens).

#### Paso 6 · Calcular el coste anual de cada modelo (6 minutos)
1. En la pestaña «Precios» están los cuatro modelos ficticios (S, M, L y Local), con el precio por millón de tokens de entrada y de salida, la ventana de contexto y la salida máxima.
2. La pestaña «Coste anual» calcula el coste de cada modelo: tokens de entrada entre un millón, por el precio de entrada, más tokens de salida entre un millón, por el precio de salida. Revisar la fórmula de una celda para comprobar que hace eso.
3. Anotar los cuatro costes anuales y el reparto entre entrada y salida (columnas «% entrada» y «% salida»).

Comprobación: hay cuatro costes anuales; el modelo local sale a 0 € en tokens (aunque tendrá otros costes que aquí no se cuentan).

#### Paso 7 · Interpretar el coste (5 minutos)
Responder por escrito:

1. ¿Qué parte del coste procede de la entrada y cuál de la salida? ¿Qué componente pesa más en cada modelo?
2. ¿Cuánto representa la parte fija de las instrucciones (600 tokens por llamada)? ¿Qué podría hacerse para reducirla?
3. Si el volumen crece un 30 %, ¿cómo cambia el coste? ¿Es lineal?
4. Si la respuesta se limitara a 80 palabras en lugar de 153, ¿cuánto se ahorraría?
5. ¿Qué otras partidas de coste no aparecen en este cálculo? Pensar en reintentos, pruebas, supervisión humana y almacenamiento.

Comprobación: cinco respuestas con cifras, no solo opiniones.

### Parte C · La ventana de contexto

#### Paso 8 · La ventana de contexto y el experimento de la aguja en el pajar (14 minutos)
Primero, cuánto cabe: medir con el visor de tokens (o con `python contar_tokens.py --archivo datos/registro_de_cambios.md`) cuántos tokens tiene [`registro_de_cambios.md`](datos/registro_de_cambios.md), un documento largo con 240 entradas, y anotarlo en la pestaña «Ventana de contexto» de la hoja, que calcula cuántas veces cabe en ventanas de 32.000, 128.000 y 200.000 tokens (descontados 4.000 tokens reservados para la respuesta). Si el documento es demasiado grande para pegarlo en el visor, medir una cuarta parte y multiplicar por cuatro.

Se esconde un dato único (la aguja) en distintas posiciones de un documento largo (el pajar) y se comprueba si el modelo lo encuentra. Es la forma de ver si un texto que cabe en la ventana también se aprovecha bien.

1. Abrir una conversación nueva en un asistente cuyo contexto admita unos 10.000 tokens como mínimo.
2. Pegar el contenido completo de [`datos/registro_de_cambios.md`](datos/registro_de_cambios.md) (o adjuntarlo, si el asistente lo permite).
3. Hacer las tres preguntas siguientes, cada una en un mensaje distinto, y anotar la respuesta y si suena segura:
   - «¿Cuál es la referencia interna de la entrada DocuMind 3.5.1 (2026-06-29)?» (está al principio; la respuesta correcta es AL-2110).
   - «¿Cuál es la referencia interna de la entrada DocuMind 3.11.8 (2026-01-25)?» (a la mitad; AL-6278).
   - «¿Cuál es la referencia interna de la entrada DocuMind 3.18.13 (2026-05-28)?» (al final; AL-3927).
4. Repetir las preguntas en una conversación nueva cambiando la forma de preguntar: «Cita literalmente la entrada y después contesta».
5. Anotar si la posición del dato cambia el acierto y si pedir la cita literal ayuda.

<details>
<summary>Con código: pajares más largos, con las agujas generadas</summary>

Para probar con documentos de 25.000 o 100.000 tokens, generarlos desde la terminal, en la carpeta `laboratorios/01A`:

```bash
python construir_contexto.py --tokens 25000
```

Crea `contexto_largo.md` (documento con tres datos únicos al principio, a la mitad y al final) y `preguntas_aguja.md` (las preguntas, sin las respuestas, que están en la solución). Hacer las tres preguntas por separado y, si el modelo lo admite, repetir con `--tokens 100000`.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: la hoja muestra cuántas veces cabe el documento en cada ventana; hay tres respuestas anotadas con su posición, y una conclusión sobre si la posición importa. Con documentos de este tamaño, los modelos actuales suelen acertar las tres; la dificultad aparece con textos mucho más largos.

#### Paso 9 · Responder a Dirección (6 minutos)
Con los resultados, responder:

1. ¿Hay diferencia de acierto según la posición del dato? ¿Con qué longitud empieza a notarse?
2. ¿Ayuda pedir la cita literal?
3. ¿Qué diferencia hay entre que un texto quepa en la ventana y que el modelo lo aproveche bien?
4. ¿Qué estrategia alternativa a «pegar todo» propone el módulo para documentos grandes? (Pista: recuperación de fragmentos, que se estudia en el módulo 13.)

Para terminar, escribir un párrafo de cinco líneas para Dirección con tres cifras: el coste anual del modelo pequeño, el del grande y qué documentos conviene no pegar enteros. Se puede completar este esquema:

```text
Para clasificar y redactar un borrador de cada ticket, el coste anual en tokens sería de [x] € con el modelo pequeño y de [y] € con el grande: [una frase sobre si el coste decide algo].
Antes de aprobar el proyecto, conviene [una decisión: qué medir o qué probar].
Los documentos que no conviene pegar enteros en el prompt son [tipo de documento], porque [motivo: «cabe» no significa «se aprovecha»]; en su lugar, [alternativa].
```

Comprobación: el párrafo para Dirección tiene tres cifras propias.

## Conclusiones

### Qué se ha conseguido

Se ha comprobado con datos propios que un modelo trabaja con tokens y no con palabras, y que el recuento depende del idioma, del tipo de contenido y de los números: el español en prosa gasta más tokens por palabra que el inglés, el código y los números son caros, y los otros alfabetos consumen mucho más por carácter. Con una regla práctica de tokens por palabra se ha estimado el coste anual de la aplicación con cuatro modelos, y se ha visto que la parte de salida y la parte fija de las instrucciones pesan más de lo que parece. Por último, se ha comprobado que un documento quepa en la ventana de contexto no garantiza que el modelo lo aproveche bien.

Referencia orientativa (rangos amplios con un modelo pequeño; con otro modelo pueden variar): El recuento real de tokens de un texto en español suele ser entre un 5 % y un 35 % mayor que la estimación por caracteres del script, según el tokenizador. Con documentos de 25.000 a 100.000 tokens reales que quepan en la ventana, los modelos actuales suelen localizar bien una referencia colocada al inicio, a la mitad o al final; si el documento no cabe, el servidor puede truncarlo sin avisar y el modelo falla. Si el resultado queda muy lejos, conviene revisar datos, prompt y script antes de abrir la solución.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Por qué los proveedores cobran más por los tokens de salida que por los de entrada?

   <details>
   <summary>Respuesta</summary>

   Porque generar es más costoso que leer: cada token de salida exige una pasada completa del modelo y se produce de forma secuencial, mientras que los de entrada se procesan en paralelo. El precio refleja ese coste de cómputo y de latencia.

   </details>

2. Si dos proveedores anuncian el mismo precio por millón de tokens, ¿puede salir uno más caro que el otro para el mismo texto en español? ¿Por qué?

   <details>
   <summary>Respuesta</summary>

   Sí. El precio por token es igual, pero el número de tokens depende del tokenizador: el mismo texto en español puede producir más o menos tokens según el vocabulario de cada proveedor, y por tanto costar más o menos.

   </details>

3. ¿Qué decisiones de diseño reducen tokens sin perder calidad (formato, instrucciones, ejemplos, recuperación de fragmentos)?

   <details>
   <summary>Respuesta</summary>

   Instrucciones más breves; eliminar ejemplos innecesarios; pedir salidas concisas y en formato compacto; reutilizar el prefijo estable con caché de prompt cuando el proveedor lo ofrece; recuperar solo los fragmentos relevantes en lugar de pegar documentos enteros; y usar un modelo pequeño para las tareas sencillas.

   </details>

4. ¿Qué riesgo hay en confiar en que «cabe en el contexto» para una tarea crítica?

   <details>
   <summary>Respuesta</summary>

   Que «quepa» no significa que se aproveche bien: con contextos largos pueden perderse datos intermedios, aumentan el coste y la latencia, y hay un límite de salida aparte. En una tarea crítica hay que verificar con citas, recuperar solo lo relevante y comprobar el resultado.

   </details>

### Autoevaluación

- [ ] Las medidas incluyen al menos un texto de cada tipo (prosa, código, números, emojis, otros alfabetos).
- [ ] La regla «N palabras ≈ X tokens» sale de los datos propios, no de una cifra recordada.
- [ ] En el cálculo de coste se distingue entre tokens de entrada y de salida y se usan sus precios respectivos.
- [ ] Se ha incluido la parte fija del prompt en la entrada de cada llamada.
- [ ] Las cantidades están expresadas en las unidades correctas (precio por *millón* de tokens).
- [ ] En la Parte C se han hecho las preguntas por separado y se ha anotado el resultado de cada una.
- [ ] La conclusión menciona límites de la estimación.

### Errores típicos

- Aplicar el mismo precio a entrada y salida.
- Olvidar el prompt fijo en cada llamada.
- Confundir precio por mil tokens con precio por millón.
- Suponer que todos los tokenizadores producen el mismo recuento.
- Concluir que un documento «cabe» y por tanto «se entiende».

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

> Los valores concretos de tokens dependen del tokenizador. Lo importante son las tendencias y el procedimiento. Los cálculos de la Parte B se dan con una regla de ejemplo y se pueden reproducir con otra.

### Parte A · Tendencias esperables

| Contenido | Comportamiento típico | Por qué |
|---|---|---|
| Español en prosa | Entre 1,5 y 2,0 tokens por palabra | El vocabulario del tokenizador está dominado por el inglés; el español se parte más. |
| Inglés en prosa | Entre 1,2 y 1,5 tokens por palabra | Muchas palabras frecuentes son un solo token. |
| Español sin tildes | Puede variar poco o consumir algo menos | Las secuencias sin tilde suelen ser más frecuentes en los datos de entrenamiento del tokenizador; pero cambia el significado y la calidad. |
| Palabras largas técnicas | Muchos fragmentos (4 a 8 tokens) | Palabras raras se descomponen en sílabas o raíces. |
| Código, JSON y YAML | Más tokens por palabra (símbolos, sangrado, nombres compuestos) | Cada llave, comilla y espacio de sangría cuenta. |
| Números e identificadores | Aproximadamente 1 token por cada 1 a 3 dígitos | No se tratan como cantidades, sino como cadenas. Un IBAN o un teléfono consume bastante. |
| Emojis y símbolos | 1 a 3 o más tokens por emoji (los compuestos, como la familia, pueden ser muchos) | Están codificados con varios bytes. |
| Otros alfabetos | Muchos más tokens por carácter | Menor cobertura en el vocabulario del tokenizador. |
| MAYÚSCULAS | Más tokens que las minúsculas | Las palabras en mayúsculas son menos frecuentes y se parten. |
| Repeticiones | Se comprimen parcialmente, pero siguen costando | Se agrupan en tokens frecuentes (`aaaa`), pero no desaparecen. |

Regla práctica de ejemplo (Paso 3): «en español, 1 palabra ≈ 1,7 tokens». Los cálculos que siguen la usan; con otra cifra, el procedimiento es el mismo.

### Parte B · Cálculo con la regla de 1,7 tokens por palabra

Procedimiento y resultado con los datos generados:

Paso 4 · Total de tickets. Total anual de tickets: 91.906. Media ponderada: 112,7 palabras por ticket y 153,2 palabras por respuesta.

Paso 5 · De palabras a tokens. Entrada por ticket: 112,7 × 1,7 + 600 = 791,6 tokens. Salida por ticket: 153,2 × 1,7 = 260,4 tokens. Totales anuales: 72,75 millones de tokens de entrada y 23,93 millones de salida.

Paso 6 · Coste anual (entrada + salida):

| Modelo | Entrada | Salida | Total anual |
|---|---|---|---|
| S (pequeño) | 10,91 € | 14,36 € | ≈ 25 € |
| M (medio) | 181,88 € | 239,34 € | ≈ 421 € |
| L (grande) | 873,04 € | 1.436,03 € | ≈ 2.309 € |
| Local | 0 € | 0 € | 0 € de tokens (pero hay coste de infraestructura) |

Paso 7 · Interpretar el coste. Respuestas a las cinco preguntas, en el orden del paso:

- Entrada y salida. La salida pesa más que la entrada en todos los modelos de pago (aunque se procesen menos tokens de salida, cada uno es varias veces más caro). Con estos precios: M, 57 %; L, 62 %.
- Instrucciones fijas. Los 600 tokens fijos son 55 millones de los 72,75 millones de entrada: el 76 % de la entrada. Se reducen acortando las instrucciones, quitando ejemplos innecesarios o usando el almacenamiento en caché de prompt que ofrecen algunos proveedores para el prefijo estable.
- Crecimiento del volumen. Es lineal respecto al volumen (a igual prompt), pero no lo es respecto a la calidad: un modelo mayor cuesta mucho más.
- Respuestas más cortas. Con respuestas de 80 palabras: salida = 80 × 1,7 = 136 tokens (frente a 260). La salida baja un 48 % y el coste de salida del modelo M pasa de 239 € a ≈ 125 €.
- Partidas que faltan. Reintentos por formato inválido, llamadas de evaluación y pruebas, revisión humana, registro y observabilidad, el coste de recuperación de documentos y, sobre todo, el coste de los errores que no se detecten.

### Parte C · Ventana de contexto

Paso 8 · La ventana de contexto y la aguja en el pajar. El registro de cambios tiene unos 10.500 tokens (estimados): cabe unas 2,7 veces en 32.000 (descontados 4.000 de respuesta), unas 11,8 veces en 128.000 y unas 18,7 en 200.000. Resultados típicos de la aguja (varían con el modelo):

- Con el documento del paso (unos 10.500 tokens) y con documentos de 25.000, los modelos actuales suelen acertar las tres agujas; los más pequeños pueden fallar la de la mitad.
- Con 100.000 tokens o más es más probable que fallen algún dato intermedio o que mezclen referencias de entradas parecidas. El efecto se atribuye a que la atención se reparte peor sobre contextos muy largos.
- Pedir que cite literalmente la entrada antes de responder mejora el acierto, porque obliga al modelo a localizar el pasaje.

Respuestas de las agujas del ejemplo con la semilla por defecto: «Cometa verde» → ZX-4471; «Lince» → QW-8820; «Brújula» → MP-1359.

Paso 9 · Responder a Dirección. Respuestas a las cuatro preguntas:

- Posición del dato. Con documentos de hasta unos 25.000 tokens, la posición (principio, mitad o final) apenas cambia el acierto. La diferencia empieza a notarse con textos de 100.000 tokens o más, y primero en los datos del medio.
- Cita literal. Sí ayuda: obliga al modelo a localizar el pasaje antes de contestar, y permite comprobar que lo citado existe en el documento.
- Caber o aprovechar. Que un texto *quepa* en la ventana solo significa que no se trunca. Aprovecharlo bien es otra cosa: con contextos largos se pierden datos intermedios, aumentan el coste y la latencia, y si el documento no cabe el servidor puede truncarlo sin avisar.
- Alternativa a «pegar todo». Recuperar solo los fragmentos relevantes para cada pregunta (recuperación de fragmentos o RAG, que se estudia en el módulo 13) y pasar al modelo únicamente esos.

Párrafo de ejemplo para Dirección, con las tres cifras:

> Para clasificar y redactar un borrador de cada uno de los ~92.000 tickets al año, el coste anual en tokens sería de unos 25 € con el modelo pequeño y de unos 2.300 € con el grande: el coste no decide la elección (son estimaciones, con una regla de 1,7 tokens por palabra y precios ficticios; el recuento real depende del tokenizador). Antes de aprobar el proyecto, conviene medir la calidad de cada modelo con un conjunto de pruebas (módulo 07) y valorar los riesgos, y probar el pequeño y el medio, escalando a uno grande solo los casos difíciles. Los documentos que no conviene pegar enteros en el prompt son los de más de unos 100.000 tokens, porque «cabe» no significa «se aprovecha»; en su lugar, recuperar solo los fragmentos relevantes.

### Resultados medidos con un modelo real

> Medición realizada el 24 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada al máximo del modelo (131.072 tokens), una sola ejecución por condición y un script de medición propio. Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

- Recuento de tokens: el documento de «25.000 tokens» según la estimación del script ocupó 33.375 tokens reales de entrada, y uno de «75.000» ocupó 100.711 (la estimación por caracteres se queda corta alrededor de un 33 % con este tokenizador, que es menos eficiente con el español; con otros tokenizadores la diferencia es menor).
- Agujas: el modelo acertó las tres referencias (inicio, mitad y final) con ≈ 33.000 y con ≈ 100.000 tokens. Con documentos sintéticos tan regulares y una pregunta directa, los modelos actuales localizan bien un dato único.
- Un documento que no cabe: el de «100.000» según la estimación equivale a unos 133.000 tokens reales, más que la ventana de 131.072. El servidor lo truncó sin avisar y el modelo falló las tres preguntas con respuestas inventadas («ZX33», «MPD: 2026-05-03»). Es la diferencia entre que un texto «quepa» y que el modelo lo aproveche, y un buen motivo para contar los tokens reales antes de pegar un documento largo.
- La degradación por posición aparece con documentos más largos, con datos parecidos entre sí o cuando hay que combinar varios datos; conviene reproducir el experimento con esas variaciones antes de concluir que «el contexto largo no es un problema».

</details>

### Para seguir

- Repetir la Parte A con otro tokenizador y comparar las tendencias.
- Medir cómo cambia el recuento de un mismo texto en español, inglés y catalán traducido por el modelo.
- Cambiar las celdas de entrada de la hoja (volumen, regla de tokens por palabra y precios) para simular otros escenarios, como un 30 % más de tickets o respuestas de 80 palabras.

---

[← Laboratorios](../README.md) · [Módulo 01](../../modulos/01-introduccion-a-los-llm/README.md) · [01B →](../01B/README.md)
