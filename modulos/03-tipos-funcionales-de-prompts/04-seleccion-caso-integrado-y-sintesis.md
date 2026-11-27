[← Anterior](03-simulacion-y-combinacion-de-funciones.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../04-tecnicas-avanzadas-de-prompting/README.md)

# 4 · Selección, caso integrado y síntesis

*Módulo 03: Tipos funcionales de prompts*

## 4.1 Errores frecuentes de selección

Elegir el tipo funcional equivocado genera respuestas que no sirven para el propósito real, aunque puedan parecer razonables. Reconocer estos patrones de error es tan importante como dominar cada tipo de prompt.

- **Creatividad en lugar de extracción**: Pedir que el modelo "proponga" cuando en realidad se necesita recuperar un dato exacto del documento. Resultado: datos inventados que parecen plausibles.
- **Resumen en lugar de comparación**: Resumir dos opciones por separado no equivale a compararlas. Las diferencias clave quedan ocultas.
- **Role-play para obtener hechos**: Usar simulación cuando se necesita información factual: el personaje puede "inventar" respuestas coherentes con el rol pero incorrectas.
- **Clasificación sin reglas**: No definir categorías ni criterios de desempate produce clasificaciones inconsistentes entre ejecuciones.
- **No delimitar la fuente**: Sin indicar que la respuesta debe basarse exclusivamente en el documento aportado, el modelo puede combinar conocimiento externo no verificado.

> Ejemplo ilustrativo: «*Dame tu opinión sobre las obligaciones del contrato» → el modelo interpreta y opina en lugar de extraer literalmente. La corrección: «Lista las obligaciones del proveedor tal como aparecen en el contrato adjunto.*»

**Explicación**

Elegir el tipo equivocado produce respuestas que parecen razonables pero no sirven. Los errores frecuentes son: creatividad en lugar de extracción (el modelo «propone» y aparecen datos inventados), resumen en lugar de comparación (las diferencias quedan ocultas), role-play para obtener hechos (el personaje inventa respuestas coherentes con el rol), clasificación sin reglas (resultados inconsistentes) y no delimitar la fuente (se mezcla conocimiento externo no verificado).

El ejemplo contrasta «Dame tu opinión sobre las obligaciones del contrato», que invita a opinar, con «Lista las obligaciones del proveedor tal como aparecen en el contrato adjunto», que limita a extraer. Estos errores no avisan: la respuesta tiene buen aspecto, por lo que la defensa es elegir bien el tipo y validar según el criterio propio de ese tipo.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03B · Una misma tarea, tres tipos de prompt](../../laboratorios/03B/README.md)
<!-- /labs-seccion -->

---

## 4.2 Caso integrado: de documento a decisión

Este caso ilustra cómo combinar cinco tipos funcionales en un único proceso de trabajo para convertir una solicitud de cambio de servicio en una decisión documentada y trazable.

1. **Extraer hechos**: Obtener del documento los datos relevantes: fechas, importes, partes implicadas y condiciones.
2. **Clasificar prioridad**: Asignar cada hecho a una categoría de urgencia e impacto según criterios predefinidos.
3. **Sintetizar**: Condensar los hechos clasificados en un resumen ejecutivo de máximo 150 palabras.
4. **Generar opciones**: Proponer tres alternativas de respuesta con ventajas y riesgos de cada una.
5. **Validar**: Contrastar cada afirmación del resumen y las opciones contra la fuente original.

> Ejemplo ilustrativo: Solicitud ficticia de cambio de servicio → se ejecuta el flujo completo en tiempo real para mostrar cómo los prompts se encadenan.

**Explicación**

El caso integrado combina cinco tipos en un proceso que convierte una solicitud de cambio de servicio en una decisión documentada: extraer hechos, clasificar la prioridad, sintetizar en un resumen de 150 palabras como máximo, generar tres opciones de respuesta con ventajas y riesgos y validar cada afirmación contra la fuente original.

Los pasos informativos, que exigen exactitud, preceden al **generativo**, que admite variedad; si se invirtiera, las opciones creativas se apoyarían en hechos no verificados. El último paso permite documentar la decisión y hacerla trazable. Cada operación tiene su tipo, cada tipo su criterio de calidad y lo exacto va antes que lo creativo.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03A · Catálogo de prompts por tipo funcional](../../laboratorios/03A/README.md)
<!-- /labs-seccion -->

---

## 4.3 Prompts informativos frente a generativos

Esta distinción es fundamental: los prompts informativos requieren exactitud y trazabilidad, mientras que los generativos buscan variedad y creatividad controlada. Mezclar los criterios de calidad de uno con el otro produce errores sistemáticos.

**Prompts informativos**

- Requieren evidencia explícita en la fuente
- El alcance debe delimitarse con precisión
- Las ausencias deben marcarse, no estimarse
- Criterio de calidad: exactitud y trazabilidad

**Prompts generativos**

- Permiten diversidad controlada de propuestas
- El marco define los límites, no los resultados exactos
- Los criterios de calidad son relevancia y variedad
- Nunca usar creatividad para rellenar datos desconocidos

> Ejemplo ilustrativo: Extraer la fecha de firma de un contrato (informativo: dato exacto o "no consta") vs. proponer nombres de campaña para un producto (generativo: variedad dentro del marco de marca).

**Explicación**

Los prompts informativos exigen exactitud y trazabilidad: requieren evidencia en la fuente, un alcance delimitado y marcar las ausencias en lugar de estimarlas. Los generativos buscan variedad y creatividad controlada: el marco fija los límites, los criterios son relevancia y variedad, y nunca se usa la creatividad para rellenar datos desconocidos.

Extraer la fecha de firma de un contrato es informativo (dato exacto o «no consta»); proponer nombres de campaña es generativo (variedad dentro del marco de marca). Aplicar el criterio equivocado produce errores sistemáticos: exigir variedad a una extracción da datos distintos en cada ejecución, y exigir exactitud literal a una lluvia de ideas da propuestas pobres. La peor mezcla es usar el modo generativo en una tarea informativa, porque el modelo cubrirá las lagunas con invención.

---

## 4.4 Prompts evaluativos

Los prompts evaluativos solicitan al modelo que valore un objeto concreto usando criterios observables y una escala definida. La calidad del resultado depende de que los criterios sean explícitos, medibles y estén respaldados por evidencia del material analizado.

- **Objeto evaluado**: Identificar con precisión qué se evalúa: una propuesta, un texto, un proceso, una solución técnica.
- **Criterios observables**: Usar dimensiones medibles: coste, claridad, viabilidad técnica, impacto esperado. Evitar criterios subjetivos sin definición.
- **Escala y ponderación**: Definir la escala (1-5, Bajo/Medio/Alto) y si algunos criterios tienen más peso que otros.
- **Evidencia por valoración**: Pedir que cada puntuación se acompañe de un fragmento o dato del material que la justifique.
- **Separar puntuación y recomendación**: La evaluación factual y las recomendaciones de mejora deben presentarse en secciones distintas.

> Ejemplo ilustrativo: «*Evalúa la propuesta adjunta según: coste estimado (1-5), impacto esperado (1-5) y nivel de riesgo (Alto/Medio/Bajo). Justifica cada valoración con un dato del documento.*»

**Explicación**

Los prompts **evaluativos** piden valorar un objeto concreto con criterios observables y una escala definida. Hay que identificar con precisión qué se evalúa, usar criterios medibles (coste, claridad, viabilidad, impacto), definir la escala y la ponderación, exigir que cada puntuación vaya acompañada del dato que la justifica y separar la puntuación de las recomendaciones de mejora.

En el ejemplo se valoran coste, impacto y riesgo con sus escalas, justificando cada valoración con un dato del documento. Sin evidencia, un modelo puede asignar un «4 sobre 5» con una justificación convincente que no se apoya en nada, y separar puntuación y recomendación evita que sus preferencias contaminen la evaluación objetiva. Es la base de la evaluación automatizada del módulo [07](../07-ciclo-de-vida-y-evaluacion/README.md).

---

## 4.5 Diseño de salidas para cada función

Cada tipo funcional de prompt tiene un formato de salida natural. La tabla recoge las funciones más habituales, incluidos subtipos como extracción, clasificación, comparación y evaluación. Definirlo explícitamente en el prompt aumenta la usabilidad del resultado y facilita su integración en flujos de trabajo posteriores.

| Función | Formato de salida recomendado | Notas clave |
|---|---|---|
| Extracción | Tabla o JSON con campos definidos | Incluir columna para ausencias y literalidad vs. inferencia |
| Clasificación | Categoría + justificación breve | Añadir columna "Otros" para casos fuera de categoría |
| Comparación | Matriz de opciones y criterios | Distinguir datos reales de supuestos en la tabla |
| Creatividad | Lista de alternativas agrupadas por enfoque | Pedir agrupación tras la generación, no durante |
| Simulación | Turnos de diálogo + feedback al cierre | Separar claramente el modo "personaje" del modo "evaluador" |
| Resolución | Causas + opciones + criterios de decisión | Ordenar causas por probabilidad e impacto |
| Evaluación | Tabla de criterios con puntuación y evidencia | Separar puntuación de recomendación en secciones distintas |

> Ejemplo ilustrativo: Usar esta tabla como referencia rápida al diseñar el prompt: identificar la función, consultar el formato y añadirlo como instrucción de salida.

**Explicación**

Cada función tiene un formato de salida natural, y definirlo en el prompt aumenta la utilidad del resultado. La extracción se presenta como tabla o JSON con campos definidos, con columna para ausencias y distinción entre literal e inferido; la clasificación, como categoría más justificación breve, con «Otros»; la comparación, como matriz de opciones y criterios, distinguiendo datos de supuestos; la creatividad, como lista de alternativas agrupadas por enfoque, agrupando después de generar; la simulación, como turnos de diálogo y feedback final, separando el modo personaje del evaluador; la resolución, como causas, opciones y criterios, ordenando por probabilidad e impacto; y la evaluación, como tabla de criterios con puntuación y evidencia.

El formato refleja la lógica de la tarea: las operaciones informativas piden estructuras rígidas y comprobables y las generativas, agrupaciones flexibles. La tabla sirve de referencia rápida; el control de formatos estructurados se amplía en el módulo [06](../06-formato-de-salida-y-parametros/README.md).

---

## 4.6 Buenas prácticas de selección

El dominio de los tipos funcionales se consolida cuando se aplican de forma sistemática. Estas cinco prácticas resumen los principios más importantes para seleccionar y ejecutar el tipo de prompt correcto en cualquier situación profesional.

- **Define la operación principal**: Antes de escribir una sola palabra, identifica si la tarea es ejecutar, recuperar, transformar, generar, clasificar, resolver o simular.
- **Aporta datos y contexto suficientes**: El modelo no puede inferir lo que no se le proporciona. Incluye el material fuente, las restricciones y los criterios de calidad.
- **No combines sin ordenar**: Cuando necesites varias funciones, define la secuencia de pasos y el formato de salida de cada uno antes de lanzar el prompt.
- **Define criterios de salida**: Especifica formato, extensión, campos obligatorios y cómo representar ausencias o incertidumbres.
- **Valida la respuesta**: Contrasta siempre el resultado con la fuente original. Ningún tipo de prompt elimina la responsabilidad de verificar.

> Mapa de referencia: Tipo → Operación principal → Formato de salida. Usar como checklist antes de cada prompt en contexto profesional.

**Explicación**

El dominio de los tipos se consolida aplicándolos con sistema. Las cinco prácticas son: definir la operación principal antes de escribir (ejecutar, recuperar, transformar, generar, clasificar, resolver o simular), aportar datos y contexto suficientes, no combinar funciones sin ordenar la secuencia y el formato de cada paso, definir criterios de salida (formato, extensión, campos obligatorios, ausencias) y validar siempre la respuesta contra la fuente original.

El mapa de referencia, que relaciona tipo, operación principal y formato de salida, funciona como lista de comprobación previa a cada prompt profesional. La quinta práctica sostiene a las demás: ningún tipo de prompt elimina la responsabilidad de verificar.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03B · Una misma tarea, tres tipos de prompt](../../laboratorios/03B/README.md)
<!-- /labs-seccion -->

---

## 4.7 Resumen

Repasa los siete tipos funcionales y su operación principal. Usa este mapa como referencia rápida al enfrentarte a cualquier tarea nueva: identifica el verbo, el resultado esperado y el tipo de prompt que mejor se ajusta.

- **Instrucción directa**: Ejecutar una acción concreta con condiciones y formato definidos.
- **Q&A**: Responder a partir de una fuente delimitada con evidencia explícita.
- **Completado**: Continuar una estructura existente manteniendo tono y coherencia.
- **Transformación**: Convertir contenido definiendo qué cambia y qué se conserva.
- **Creatividad**: Generar alternativas diversas dentro de un marco controlado.
- **Resolución**: Analizar causas, generar opciones y evaluar consecuencias.
- **Simulación**: Practicar interacciones en escenarios con roles y feedback estructurado.

**Explicación**

El resumen repasa los siete tipos funcionales: la instrucción directa ejecuta una acción con condiciones y formato definidos; las preguntas y respuestas responden a partir de una fuente delimitada con evidencia; el completado continúa una estructura manteniendo tono y coherencia; la transformación convierte contenido definiendo qué cambia y qué se conserva; la creatividad genera alternativas dentro de un marco; la resolución analiza causas, genera opciones y evalúa consecuencias; y la simulación practica interacciones con roles y feedback.

Cada tipo tiene su criterio de calidad: exactitud y trazabilidad en los más cercanos a la información, variedad y adecuación en los generativos, honestidad al separar hechos, hipótesis y supuestos en los analíticos, y coherencia del personaje y calidad del feedback en los interactivos. Con este módulo concluye el bloque de fundamentos; el módulo [04](../04-tecnicas-avanzadas-de-prompting/README.md) introduce las técnicas que dan más control sobre el comportamiento del modelo, empezando por los ejemplos.

---

## 4.8 Comprobación de comprensión

Piensa cada respuesta, de forma oral o por escrito, antes de ver las respuestas orientativas, que aparecen a continuación.

**Preguntas de comprobación**

1. ¿Qué diferencia hay entre un prompt informativo y uno generativo, y qué fallo se vigila en cada uno?
1. ¿Cuándo conviene una extracción y cuándo un resumen?
1. ¿Qué debe hacer un prompt de pregunta-respuesta basado en contexto si el dato no está en la fuente?
1. ¿Qué se define en un prompt de transformación?
1. ¿Por qué elegir mal el tipo de prompt es un error de diseño y no de redacción?

**Explicación**

La comprobación de comprensión propone cinco preguntas para repasar el módulo antes de seguir: la diferencia entre un prompt informativo y uno generativo y el fallo que se vigila en cada uno, cuándo conviene extraer y cuándo resumir, qué hace un prompt de pregunta-respuesta cuando el dato no está en la fuente, qué se define en una transformación y por qué elegir el tipo es una decisión de diseño. Conviene responderlas por escrito antes de ver las respuestas de la diapositiva siguiente.

Las preguntas recorren los tipos funcionales en el orden en que se estudiaron y se apoyan en los laboratorios 03A y 03B, donde se comprueba con casos reales que el tipo de prompt determina la salida y el fallo.

---

## 4.9 Comprobación de comprensión: respuestas

Contrasta tus respuestas con estas. Son orientativas: lo importante es que cubran las ideas clave del módulo.

**Preguntas de comprobación y respuestas orientativas**

1. ¿Qué diferencia hay entre un prompt informativo y uno generativo, y qué fallo se vigila en cada uno?

El informativo busca un dato verificable y el fallo a vigilar es que invente; el generativo produce algo nuevo y se vigila que respete el marco y sirva al uso previsto.

1. ¿Cuándo conviene una extracción y cuándo un resumen?

Extracción, cuando hacen falta campos concretos y verificables (con null si no constan); resumen, cuando se quiere una versión más corta que conserve fechas, cifras y decisiones.

1. ¿Qué debe hacer un prompt de pregunta-respuesta basado en contexto si el dato no está en la fuente?

Responder «no consta»: usar solo la fuente delimitada, citar la evidencia y no completar con conocimiento general.

1. ¿Qué se define en un prompt de transformación?

Qué cambia (formato, tono, idioma, longitud) y qué se conserva (hechos, cifras, estructura), para que la salida sea fiel al original.

1. ¿Por qué elegir mal el tipo de prompt es un error de diseño y no de redacción?

Porque el tipo determina la salida y su fallo característico; se elige según quién usará la salida y cuánto cuesta equivocarse, no según lo que suene natural.

**Explicación**

Las respuestas orientativas resumen el módulo en cinco ideas. El prompt informativo busca un dato verificable y el riesgo es que invente; el generativo produce algo nuevo y el riesgo es que se salga del marco. La extracción exige campos concretos, con null cuando no constan; el resumen conserva fechas, cifras y decisiones. Una pregunta basada en contexto responde «no consta» cuando la fuente no contiene el dato. La transformación declara qué cambia y qué se conserva. Y el tipo se elige según quién usará la salida y cuánto cuesta equivocarse, no según lo que suene natural.

Si alguna respuesta propia no coincide, conviene volver a la sección del tipo correspondiente y comprobar qué elemento del prompt estaba ausente.

---

[← Anterior](03-simulacion-y-combinacion-de-funciones.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../04-tecnicas-avanzadas-de-prompting/README.md)
