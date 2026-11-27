[← Laboratorios](../README.md) · [Módulo 01](../../modulos/01-introduccion-a-los-llm/README.md) · [← 01A](../01A/README.md) · [02A →](../02A/README.md)

# Laboratorio 01B · Mapa de capacidades y límites de un LLM

Módulo 01 · Introducción a los LLM · Duración estimada: 55 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Probar un modelo con tareas distintas y construir un mapa propio de lo que hace de forma fiable y de dónde falla. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Ejecutar las 20 tareas (25 min)
- Paso 2 · Repetir con una mitigación las tareas que fallaron (16 min)
- Paso 3 · Atribuir una causa a cada fallo (6 min)
- Paso 4 · Distinguir el modelo de la aplicación y dibujar el mapa (8 min)

<details>
<summary>Secciones del módulo relacionadas (6)</summary>

- [§2.2 LLM, chatbot y aplicación: no son lo mismo](../../modulos/01-introduccion-a-los-llm/02-que-es-un-llm.md#22-llm-chatbot-y-aplicación-no-son-lo-mismo)
- [§5.1 Capacidades: comprensión y transformación de texto](../../modulos/01-introduccion-a-los-llm/05-capacidades-y-limitaciones.md#51-capacidades-comprensión-y-transformación-de-texto)
- [§5.4 Limitaciones: alucinaciones y factualidad](../../modulos/01-introduccion-a-los-llm/05-capacidades-y-limitaciones.md#54-limitaciones-alucinaciones-y-factualidad)
- [§5.5 Limitaciones: razonamiento y consistencia](../../modulos/01-introduccion-a-los-llm/05-capacidades-y-limitaciones.md#55-limitaciones-razonamiento-y-consistencia)
- [§5.6 Limitaciones: conocimiento, actualidad y contexto](../../modulos/01-introduccion-a-los-llm/05-capacidades-y-limitaciones.md#56-limitaciones-conocimiento-actualidad-y-contexto)
- [§5.8 Cómo evaluar si un LLM es adecuado para una tarea](../../modulos/01-introduccion-a-los-llm/05-capacidades-y-limitaciones.md#58-cómo-evaluar-si-un-llm-es-adecuado-para-una-tarea)

</details>

## Justificación del laboratorio

El equipo de Soporte de Altanoria quiere usar un asistente de IA para «todo lo que se pueda». Es una reacción comprensible: un asistente responde casi a cualquier cosa y casi siempre con aplomo. Pero ese aplomo es precisamente el problema. Un modelo de lenguaje acierta con total seguridad una redacción y falla con la misma seguridad al contar las letras de una palabra, multiplicar dos números grandes o decir qué plan contrató un cliente que nunca le ha dado ese dato.

Antes de encargarle tareas a un asistente conviene saber cuáles hace de forma fiable, cuáles solo con ayuda (un documento adjunto, una calculadora, un código que se ejecute) y cuáles no se le deben encargar nunca. Marta Illueca, directora de Soporte, ha pedido un mapa sencillo de esas tres zonas. Este laboratorio lo construye con evidencia propia: se prueba el modelo con veinte tareas, se comparan sus respuestas con las correctas y se averigua por qué falla cada vez que falla.

Hay además una distinción que explica muchos malentendidos: la diferencia entre el modelo, el chatbot y la aplicación. Muchos fallos y aciertos que se atribuyen al modelo pertenecen en realidad a la aplicación que lo rodea (por ejemplo, la memoria entre conversaciones o el acceso a documentos). Saber separarlos es una habilidad básica para cualquier persona que trabaje con IA.

## Objetivos

Construir con evidencia propia un mapa de capacidades y límites de un modelo de lenguaje: qué tareas realiza de forma fiable, cuáles solo con ayuda externa y cuáles no debe realizar. Además, distinguir entre modelo, chatbot y aplicación, porque muchos «fallos» y «aciertos» pertenecen a la aplicación y no al modelo.

Al terminar el laboratorio se habrá conseguido:

- Formular una hipótesis sobre una tarea antes de ejecutarla y contrastarla con el resultado.
- Reconocer los tipos de fallo más frecuentes: conteo de letras, aritmética, fechas, datos privados o recientes, citas inventadas, instrucciones numéricas estrictas.
- Atribuir cada fallo a una causa (tokenización, falta de información, predicción plausible en lugar de cálculo, ausencia de memoria).
- Proponer para cada fallo una mitigación concreta: herramienta, contexto, comprobación o revisión humana.

Conceptos que se usan:

- **El modelo predice texto plausible**. No consulta una base de datos ni ejecuta un programa: genera el texto más probable dadas las instrucciones y el contexto. Eso explica su fortaleza en tareas de lenguaje (resumir, traducir, clasificar, redactar) y su debilidad cuando se exige exactitud externa (cifras, citas, datos privados o recientes).
- **Modelo ≠ chatbot ≠ aplicación**. El modelo es el sistema entrenado; el chatbot es una interfaz de conversación; la aplicación añade datos, herramientas, memoria y controles. Una calculadora integrada, un buscador o una memoria entre sesiones son funciones de la aplicación, no del modelo.
- **Fiabilidad por tipo de tarea**. Una misma herramienta puede ser muy fiable en una tarea y poco fiable en otra. Por eso no se evalúa «el modelo», sino «el modelo en esta tarea con este prompt y estos datos».

## Recursos necesarios

- Un asistente de chat cualquiera. Idealmente, dos distintos (o un modelo pequeño y uno grande del mismo proveedor) para comparar.
- La hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), con las 20 tareas, los resultados, las causas y el mapa de zonas.
- Datos: [`datos/tareas_capacidades.csv`](datos/tareas_capacidades.csv): 20 tareas con su categoría, la respuesta correcta y una pista.

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Pasos de ejecución

Los pasos están pensados para hacerse en orden. Este laboratorio es de chat: ningún paso necesita código. Si es posible, usar dos asistentes distintos (o un modelo pequeño y uno grande del mismo proveedor) para comparar; si solo hay uno, el laboratorio funciona igual.

### Paso 1 · Ejecutar las 20 tareas (25 minutos)
1. Abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), pestaña «Tareas». Tiene las 20 tareas con su categoría (los datos vienen de [`datos/tareas_capacidades.csv`](datos/tareas_capacidades.csv)). Las columnas de respuesta correcta y de pista están ocultas: no mirar la respuesta correcta de una tarea hasta haber recibido la respuesta del asistente (se muestran con el botón «+» de la cabecera de columnas).
2. Para cada fila de la hoja, abrir una conversación nueva en el asistente, copiar el contenido de la columna `tarea` tal cual, enviarlo y esperar la respuesta.
3. Comparar con la respuesta correcta y anotar en la columna «Resultado»: ✓ si es correcta, ~ si es parcial, ✗ si es incorrecta. La respuesta del asistente no hace falta copiarla en la hoja.

Notas sobre tareas concretas:

- Tarea n.º 6 (fecha): comprobar la respuesta con un calendario.
- Tarea n.º 12 (código): copiar la función que escribe el asistente y probarla con 1, 2, 17, 18 y 97. Si no se sabe ejecutar código, se puede pegar la función en un intérprete en línea de Python, o pedir al propio asistente que la pruebe con esos valores y comprobar su razonamiento.
- Tarea n.º 15 (12 palabras): contar a mano las palabras de la respuesta.
- Tarea n.º 18: enviar primero «Mi cliente se llama Aceros del Turia» y después la pregunta, en la misma conversación.
- Tarea n.º 19: abrir una conversación nueva y hacer la pregunta sin dar el nombre.

Comprobación: las 20 filas tienen la marca ✓, ~ o ✗. La pestaña «Resumen» cuenta cuántas tareas fallaron: se necesitará en el paso siguiente.

### Paso 2 · Repetir con una mitigación las tareas que fallaron (16 minutos)
Para cada tarea marcada ✗ o ~, repetirla con una ayuda (en una conversación nueva) y anotar en la hoja el resultado con mitigación (✓, ~ o ✗); la hoja calcula si mejoró:

| Tipo de fallo | Mitigación a probar |
|---|---|
| Conteo de letras o aritmética | Pedir que escriba y ejecute código, usar una calculadora, o pedir el desglose letra a letra |
| Datos de Altanoria (tareas n.º 7 y 9) | Adjuntar [`catalogo_planes.md`](../comun/empresa/catalogo_planes.md) y pedir que responda solo con él |
| Cita inexistente (tarea n.º 8) | Añadir «si no existe o no estás seguro, dilo» |
| Fechas | Pedir el cálculo intermedio paso a paso |
| 12 palabras exactas | Pedir que numere las palabras |
| Ambigüedad (tarea n.º 16) | Añadir «si falta información, pregunta antes de responder» |

Plantillas de prompts para las tres mitigaciones más habituales:

Mitigación con documento (tareas n.º 7 y 9):

```text
Usa SOLO el documento siguiente para responder. Si el documento no contiene la respuesta, responde exactamente: «No consta en el documento».

<documento>
{pegar aquí el contenido de catalogo_planes.md}
</documento>

Pregunta: {texto de la tarea}
```

Mitigación de cálculos (tareas n.º 2, 3 y 6):

```text
Resuelve paso a paso, comprobando cada operación. Si los números usan punto como separador de miles (por ejemplo 48.273), trátalos como enteros. Termina con una última línea: «Resultado: …».

{texto de la tarea}
```

Mitigación de citas (tarea n.º 8):

```text
Si la norma, la ley o el artículo que menciono no existe o no estás seguro de que exista, dilo claramente y no inventes su contenido.

{texto de la tarea}
```

Comprobación: cada tarea que falló tiene el resultado con mitigación y la hoja indica si mejoró.

### Paso 3 · Atribuir una causa a cada fallo (6 minutos)
Para cada tarea que falló, elegir la causa más probable de esta lista y anotar su letra en la columna «Causa»:

| Código | Causa |
|---|---|
| A | Tokenización (el modelo no «ve» letras) |
| B | Predicción plausible en lugar de cálculo |
| C | Falta de información (privada o reciente) |
| D | Inventar para no dejar un hueco (alucinación) |
| E | Ausencia de memoria entre conversaciones |
| F | Instrucción ambigua o incompleta |
| G | Restricción exacta que el modelo no puede verificar |

Se pueden consultar las pistas de la columna `pista` del CSV para decidir.

Comprobación: cada fallo tiene una letra de causa.

### Paso 4 · Distinguir el modelo de la aplicación y dibujar el mapa (8 minutos)
1. Colocar cada una de las 20 tareas en una zona (columna «Zona»), según lo observado: fiables, solo con ayuda (con un documento, una calculadora, código o revisión) y no se encargan. La hoja cuenta cuántas tareas hay en cada zona.
2. Para cada mejora conseguida en el paso anterior, decidir qué parte aportó el modelo y cuál la aplicación o la persona (el documento adjunto, la herramienta, la instrucción adicional), apoyándose en la tabla de ejemplos de la solución.
3. Para terminar, escribir un párrafo corto para Marta Illueca, directora de Soporte, con tres reglas de uso del asistente sacadas del mapa.

Comprobación: las 20 tareas están en una zona y hay un párrafo de tres reglas para Marta Illueca.

## Conclusiones

### Qué se ha conseguido

Se ha construido, con evidencia propia, un mapa de lo que un asistente de IA hace bien, de lo que solo hace con ayuda y de lo que no conviene encargarle. Lo más revelador suele ser la distancia entre la seguridad con la que suenan las respuestas y su exactitud: los fallos clásicos (contar letras, multiplicar números grandes, citar fuentes inexistentes, hablar de un cliente del que no se dispone de datos) se dan con el mismo aplomo que los aciertos. También se ha visto que muchas mejoras no vienen de un modelo mejor, sino de rodearlo bien: un documento adjunto, una calculadora, una instrucción que le deje decir «no lo sé».

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿En qué tipos de tarea falló el modelo aunque la respuesta sonara segura? ¿Qué creencia hay que corregir?

   <details>
   <summary>Respuesta</summary>

   Las intuiciones suelen fallar en dos sentidos: se sobrestima al modelo en aritmética, fechas y conteo, y se subestima en tareas de lenguaje aparentemente complejas. La respuesta segura no es señal de acierto.

   </details>

2. ¿Por qué un modelo capaz de resumir un documento complejo puede fallar al contar las «r» de «ferrocarril»?

   <details>
   <summary>Respuesta</summary>

   Porque resumir es una tarea de patrones de lenguaje, mientras que contar letras exige operar sobre unidades (caracteres) que el modelo no recibe: ve tokens. Ver el laboratorio 01A.

   </details>

3. ¿Qué tareas de la lista cambian de categoría si el modelo dispone de herramientas (calculadora, buscador, ejecución de código)?

   <details>
   <summary>Respuesta</summary>

   Aritmética, fechas, datos recientes y verificación de código pasan a «fiable» con herramientas. La atribución de la mejora corresponde a la aplicación.

   </details>

4. La tarea n.º 19 muestra que el modelo no recuerda entre conversaciones. ¿Cómo podría una aplicación dar la sensación de memoria? ¿Qué riesgos de privacidad aparecerían?

   <details>
   <summary>Respuesta</summary>

   Guardando en una base de datos resúmenes o preferencias y reinyectándolos en el contexto de cada conversación. Riesgos: conservar datos personales más allá de lo necesario, mezclar información de usuarios y falta de derecho a borrado. Se retoma en el módulo 13 (memoria y persistencia) y en el módulo 09.

   </details>

5. ¿Qué cambia si la pregunta se hace a un modelo pequeño o a uno grande? ¿Y con el mismo modelo en otro momento?

   <details>
   <summary>Respuesta</summary>

   Los modelos grandes fallan menos, pero no desaparecen los fallos: cambian de lugar. Con el mismo modelo, el resultado puede variar entre ejecuciones (módulo 06).

   </details>

### Autoevaluación

- [ ] Cada tarea se ejecutó en una conversación nueva y limpia (salvo las indicadas).
- [ ] Cada resultado se anotó comparando con la respuesta correcta, no «a ojo».
- [ ] Las comprobaciones se hicieron con una fuente externa (calendario, calculadora, ejecución de código), no solo «a ojo».
- [ ] Al menos cuatro fallos están documentados con su causa y una mitigación probada.
- [ ] Hay al menos una tarea con resultado ✗ en la que el modelo respondió con aplomo, y está marcada.

### Errores típicos

- Hacer todas las tareas en una misma conversación (el contexto previo contamina).
- Dar por buena una respuesta porque suena segura.
- No ejecutar el código generado.
- Atribuir al «modelo» una mejora que en realidad aportó el documento adjunto.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

> Los resultados dependen del modelo y de su versión. La siguiente tabla indica qué se espera con mayor probabilidad en modelos actuales de uso general y por qué. Si el resultado propio difiere, anotarlo: es parte del aprendizaje.

### Mapa esperable

| # | Tarea | Fiabilidad esperable | Qué suele ocurrir | Causa de fallo | Mitigación |
|---|---|---|---|---|---|
| 1 | Letras «r» en «ferrocarril» | 🟡 | A veces falla (responde 3 o 5). Los modelos recientes aciertan más, pero sin garantía. | A (tokenización) | Pedir el desglose letra a letra o ejecutar código. |
| 2 | 48.273 × 3.916 | ❌ sin herramienta | Resultado cercano pero con errores en dígitos, salvo con ejecución de código. Resultado correcto: 189.037.068. | B | Calculadora / código. |
| 3 | √2025 | 🟡 | Normalmente acierta (45). | — | Verificar. |
| 4 | Resumen de una frase | ✅ | Suele hacerlo bien. Comprobar que incluye causa y duración. | — | — |
| 5 | Traducción | ✅ | Muy fiable. Revisar el «10 %» y el tono. | — | — |
| 6 | Día de la semana del 31-dic-2026 | 🟡 | Puede fallar sin cálculo explícito. Resultado correcto: jueves (5 de noviembre de 2026 es jueves, 56 días después, 56 = 8 semanas, jueves; 31 de diciembre es 56 días después). | B | Pedir el cálculo paso a paso o usar herramienta. |
| 7 | Mínimo de usuarios del plan Team | ❌ sin contexto | Inventa o dice que no lo sabe. | C | Adjuntar el catálogo. Respuesta: 5. |
| 8 | Artículo de una ley inventada | ❌ | Riesgo alto de cita inventada. Un buen resultado es «no existe esa ley». | D | «Si no existe o no estás seguro, dilo» + verificar en fuente oficial. |
| 9 | Precio actual de Copilot Team | ❌ sin contexto | Dará un precio inventado o genérico. Con el catálogo: 29 €. | C | Adjuntar el catálogo. |
| 10 | Segunda más joven | ✅ | Acierta (Carlos). | — | — |
| 11 | +20 % y −20 % | 🟡 | A menudo acierta (96 €); algunos modelos responden 100 €. | B | Pedir cálculo paso a paso. |
| 12 | Función de primo | ✅ | Genera código razonable. Hay que ejecutarlo: probar 1, 2, 17, 18, 97. | — | Ejecutar y probar. |
| 13 | Clasificación del ticket | ✅ | Acierta (acceso). | — | — |
| 14 | Extracción de importe y fecha | ✅ | Acierta si el texto es claro. Comprobar el formato (1194.00, 2026-09-14). | — | — |
| 15 | Frase de exactamente 12 palabras | 🟡 | Frecuentemente 11 o 13 palabras. | G | Pedir que numere las palabras. |
| 16 | «Dime cuánto cuesta» | 🟡 | Suele pedir aclaración; algunos responden con un precio inventado. | F | «Si falta información, pregunta primero». |
| 17 | Mejor lenguaje de programación | 🟡 | Los modelos suelen matizar. Riesgo: opinión presentada como hecho. | F | Pedir criterios y contexto de uso. |
| 18 | Memoria dentro de la conversación | ✅ | Acierta (Aceros del Turia). | — | — |
| 19 | Memoria entre conversaciones | ❌ | Dice que no lo sabe (bien) o inventa un nombre (mal). | E | Memoria gestionada por la aplicación. |
| 20 | 35 % de 140 | ✅ | Acierta (49). | — | — |

> Nota sobre la tarea n.º 6: el cálculo de comprobación es: de jueves 5 de noviembre al 31 de diciembre hay 56 días (25 días hasta fin de noviembre + 31 de diciembre = 56). 56 días son exactamente 8 semanas, por lo que el día de la semana coincide: jueves.

### Mapa final de ejemplo

- ✅ Fiable (con revisión ligera): resumir, traducir, clasificar, extraer, lógica sencilla, mantener contexto dentro de la conversación, generar borradores de código.
- 🟡 Con ayuda: aritmética y fechas (herramienta), conteo (desglose), cualquier dato de Altanoria (documento adjunto), restricciones numéricas estrictas (verificar), opiniones (pedir criterios).
- ❌ No apta sin controles: citas legales o normativas, cifras precisas sin fuente, memoria entre sesiones, cualquier dato reciente o privado sin contexto.

### Aporte de la mejora (ejemplos)

Qué aportó el modelo y qué aportó la aplicación o la persona en las mejoras más habituales:

| Tarea | Mejora | Qué aporta el modelo | Qué aporta la aplicación o la persona |
|---|---|---|---|
| 7 y 9 (datos de Altanoria) | Adjuntar el catálogo | Localizar el dato en el documento y redactarlo | El documento: el modelo no tenía el dato |
| 2, 6 y 11 (cálculos y fechas) | Pedir el cálculo paso a paso o usar una calculadora o código | Plantear la cuenta | La herramienta que ejecuta el cálculo, o la persona que pide el desglose y lo verifica |
| 1 (conteo de letras) | Pedir el desglose letra a letra | Seguir el método indicado | La persona que elige el método: el modelo no «ve» las letras, trabaja con tokens |
| 8 (ley inventada) | «Si no existe o no estás seguro, dilo» | Obedecer la instrucción | La instrucción y la verificación en una fuente oficial |
| 15 (12 palabras) | Pedir que numere las palabras | Numerar y ajustar | La comprobación final del recuento |
| 16 y 17 (ambigüedad y opiniones) | «Si falta información, pregunta primero» o pedir criterios | Preguntar o matizar | La instrucción adicional |
| 19 (memoria entre conversaciones) | Memoria gestionada por la aplicación | Usar lo que la aplicación le entrega | La aplicación: el modelo no recuerda de una conversación a otra |

### Párrafo de ejemplo para Marta Illueca

«Tres reglas: 1) el asistente redacta, resume, clasifica y traduce; todo dato concreto de Altanoria (precios, plazos, condiciones) debe ir con el documento adjunto y se contrasta con la fuente antes de enviarlo al cliente. 2) Cualquier cálculo, fecha o cifra se verifica con una herramienta, nunca con la apariencia de seguridad del texto. 3) Si no hay fuente, la respuesta correcta es "no consta"; las citas legales y las promesas de compensación las gestiona una persona.»

### Resultados medidos con un modelo real

> Medición realizada el 24 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada a 16.384 tokens, una sola ejecución por tarea y un script de medición propio (el laboratorio se hace por chat). Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

Resultados con 20 tareas ejecutadas una vez cada una, cada una en una conversación nueva (sin documento adjunto salvo indicación):

| # | Resultado real |
|---|---|
| 1 «r» en ferrocarril | Correcto (4). |
| 2 48.273 × 3.916 | Incorrecto: interpretó los puntos como decimales y respondió 188,2647328 (el resultado correcto es 189.037.068; además el producto entero que calculó, 188.264.732, tampoco es correcto). |
| 3 √2.025 | Incorrecto: respondió ≈ 1,423 (interpretó «2.025» como 2,025). Ambigüedad del separador de miles en español. |
| 4 y 5 Resumen y traducción | Contenido correcto, pero ofreció varias opciones («Opción 1…», «tres formas de traducirlo») cuando se pedía una frase: no siguió la restricción de formato. |
| 6 Día de la semana | Correcto (jueves) con cálculo paso a paso. |
| 7 Mínimo de usuarios del plan Team | No inventó: dijo que no tenía acceso a esa información. Con el catálogo adjunto respondió 5. |
| 8 Artículo 47 bis de la ley inventada | No alucinó: dijo que no tenía registro de esa ley y pidió verificar la referencia. |
| 9 Precio actual de Copilot Team | No inventó un precio. Con el catálogo adjunto respondió 29 € por usuario y mes. |
| 10 y 11 Lógica y +20 %/−20 % | Correctos (Carlos; 96 €). |
| 12 Función de primo | Código correcto: se ejecutó con 10 valores (0, 1, 2, 3, 4, 17, 25, 97, 100 y 7919) y todos dieron el resultado esperado. |
| 13 Clasificación de ticket | Respondió con una categoría libre («Problemas de Autenticación / Acceso») y tres opciones, en lugar de la categoría esperada de una lista cerrada. |
| 14 Extracción | Correcto (14 de septiembre de 2026; 1.194,00 €). |
| 15 Frase de 12 palabras | Correcto: la frase tenía exactamente 12 palabras. |
| 16 «Dime cuánto cuesta» | Pidió aclaración (correcto). |
| 17 Mejor lenguaje de programación | Respondió que no hay un «mejor» y que depende del problema (correcto). |
| 18 y 19 Memoria | Recordó el nombre dentro de la conversación y reconoció que no tiene memoria entre sesiones. |

Lecciones: los errores más claros fueron la aritmética con separadores de miles (tareas n.º 2 y 3, también sin ayuda de calculadora) y seguir restricciones de formato (una sola frase, una categoría de una lista cerrada): el modelo tiende a ofrecer varias opciones y a explicarlas. Con este modelo no hubo invenciones ante datos privados o inexistentes (tareas n.º 7, 8 y 9), pero eso no es una propiedad de «los modelos»: se debe a este modelo concreto, y el laboratorio sigue pidiendo comprobarlo con el que se vaya a usar. El conteo de letras y de palabras funcionó.

</details>

### Para seguir

- Añadir cinco tareas propias de su trabajo y clasificarlas.
- Repetir cada tarea cinco veces y anotar cuántas veces cambia el resultado (anticipo del módulo 06 sobre variabilidad).
- Comparar dos modelos de distinto tamaño y observar qué errores desaparecen y cuáles persisten.

---

[← Laboratorios](../README.md) · [Módulo 01](../../modulos/01-introduccion-a-los-llm/README.md) · [← 01A](../01A/README.md) · [02A →](../02A/README.md)
