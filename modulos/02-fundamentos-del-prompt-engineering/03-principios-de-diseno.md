[← Anterior](02-anatomia-de-un-prompt.md) · [Índice del módulo](README.md) · [Siguiente →](04-ejemplos-revision-y-sintesis.md)

# 3 · Principios de diseño

*Módulo 02: Fundamentos del Prompt Engineering*

## 3.1 Claridad frente a ambigüedad

La ambigüedad obliga al modelo a completar supuestos que quizá no coincidan con la intención del usuario. Identificar y resolver las expresiones vagas antes de ejecutar mejora notablemente la calidad del resultado.

| Expresión ambigua | Reformulación precisa | Tipo de ambigüedad |
|---|---|---|
| «Hazlo mejor» | «Reduce redundancias, conserva los datos y usa tono formal» | Objetivo vago |
| «Algo adecuado» | «Un párrafo de entre 80 y 100 palabras dirigido a directivos» | Criterio indefinido |
| «Lo anterior» | «El tercer punto de la lista de requisitos» | Referencia poco clara |
| «Sé completo» | «Incluye causa, impacto y medida correctora para cada incidencia» | Alcance implícito |

Algunas ambigüedades son *deliberadas* en tareas creativas; en ese caso, deben resolverse de forma consciente según el objetivo buscado.

**Explicación**

La ambigüedad obliga al modelo a completar supuestos que pueden no coincidir con la intención. La tabla muestra cuatro expresiones ambiguas y su reformulación: «Hazlo mejor» (objetivo vago) pasa a reducir redundancias, conservar datos y usar tono formal; «Algo adecuado» (criterio indefinido) pasa a un párrafo de 80 a 100 palabras para directivos; «Lo anterior» (referencia poco clara) pasa a señalar el elemento concreto; «Sé completo» (alcance implícito) pasa a indicar causa, impacto y medida correctora por incidencia.

Las expresiones ambiguas transmiten una intención pero no una operación. Una técnica útil es releer el prompt como si se desconociera el proyecto y resolver todo lo que admita dos interpretaciones razonables. En tareas creativas puede ser legítimo dejar libertad, siempre que se decida de forma consciente.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 02A · Del prompt vago al contrato de tarea](../../laboratorios/02A/README.md)
<!-- /labs-seccion -->

---

## 3.2 Especificidad sin sobrecargar el prompt

El prompt debe incluir la información necesaria, no acumular instrucciones irrelevantes. Tanto la falta de detalle como el exceso degradan la calidad del resultado.

- **❌ Demasiado breve**: «*Resume el texto.*» — Sin audiencia, extensión ni criterio. El modelo decide todo.
- **✅ Equilibrado**: «*Resume para directivos en máximo 5 puntos, priorizando decisiones y riesgos.*» — Contiene lo esencial.
- **⚠️ Sobrecargado**: «*Resume, traduce, formatea en HTML, incluye metadatos, optimiza para SEO y adapta para redes sociales.*» — Múltiples objetivos sin prioridad.

**Criterios para añadir detalle**

- Solo incluir información que cambie materialmente el resultado
- Eliminar contexto repetido o decorativo
- Agrupar reglas relacionadas en un solo punto
- Usar ejemplos cuando clarifiquen mejor que una explicación extensa

**Explicación**

El prompt debe incluir la información necesaria, ni más ni menos. «Resume el texto» es demasiado breve: sin audiencia, extensión ni criterio, el modelo decide todo. «Resume para directivos en máximo 5 puntos, priorizando decisiones y riesgos» está equilibrado. Una petición con resumen, traducción, HTML, metadatos, SEO y adaptación a redes sociales está sobrecargada: son varios objetivos sin prioridad.

Para decidir cuánto detalle añadir: incluir solo lo que cambie el resultado, eliminar el contexto repetido, agrupar reglas relacionadas y usar ejemplos cuando expliquen mejor que una descripción larga. La solución al exceso no es suprimir objetivos, sino separarlos en tareas distintas.

---

## 3.3 Concisión y relevancia del contexto

El contexto debe ser suficiente, pertinente y distinguible de las instrucciones. Seleccionar bien qué se incluye es tan importante como el propio contenido.

**Filtro de contexto**

- ✅ Relevante: Cambia cómo se ejecuta la tarea
- 🟡 Opcional: Puede ayudar, pero no es imprescindible
- ❌ Prescindible: No afecta al resultado

**Buenas prácticas**

- Incluir antecedentes necesarios para interpretar la petición
- Priorizar datos relevantes sobre los meramente disponibles
- Usar encabezados y delimitadores en prompts extensos
- Comprobar que no existan contradicciones internas

**Ejemplo ilustrativo**

Un informe de ventas contiene datos de tres regiones; el prompt indica *analizar solo la región solicitada*, evitando procesar información irrelevante.

**Explicación**

El contexto debe ser suficiente, pertinente y distinguible de las instrucciones. Un filtro sencillo lo clasifica en relevante (cambia cómo se ejecuta la tarea), opcional (puede ayudar) y prescindible (no afecta al resultado). Se conserva lo primero, se valora lo segundo según el espacio y el riesgo, y se elimina lo tercero.

Otras buenas prácticas son priorizar los datos relevantes sobre los meramente disponibles, usar encabezados y **delimitadores** en prompts largos y comprobar que no haya contradicciones internas. Si el informe contiene datos de tres regiones y solo interesa una, el prompt debe delimitar esa región. Como la ventana de contexto es limitada y el modelo no filtra el ruido, un contexto breve y bien seleccionado suele rendir más que uno extenso y desordenado.

---

## 3.4 Verbos de acción y estructura de instrucciones

Los verbos de acción ayudan a definir operaciones observables y reducen instrucciones genéricas. Un verbo preciso orienta directamente el tipo de procesamiento esperado.

- **Clasifica**: Asigna categorías según reglas explícitas definidas en el prompt.
- **Extrae**: Recupera campos concretos de un documento o texto.
- **Compara**: Identifica similitudes y diferencias según criterios definidos.
- **Prioriza**: Ordena elementos según reglas explícitas de importancia.
- **Transforma**: Cambia formato o estilo conservando el significado original.
- **Verifica**: Contrasta con criterios o fuentes disponibles. Requiere fuente real.

Transformar «*revisa este documento*» en «*extrae obligaciones, fechas límite y responsables*» convierte una petición vaga en una tarea accionable.

**Explicación**

Los verbos de acción definen operaciones observables. Clasificar asigna categorías según reglas explícitas, extraer recupera campos concretos, comparar identifica similitudes y diferencias según criterios, priorizar ordena según reglas de importancia, transformar cambia formato o estilo conservando el significado y verificar contrasta con una fuente real.

Cada verbo implica un tipo de resultado distinto (etiquetas, campos, diferencias, un orden, una versión equivalente, un juicio apoyado en una fuente), de modo que elegir el verbo equivale a elegir la forma de la respuesta. Convertir «revisa este documento» en «extrae obligaciones, fechas límite y responsables» transforma una petición vaga en una tarea accionable.

---

## 3.5 Descomponer tareas complejas

Las tareas complejas pueden dividirse en etapas con objetivos y salidas intermedias claras. Las instrucciones monolíticas son difíciles de ejecutar y de depurar cuando el resultado no es el esperado.

**Extraer datos**

**Resumir**

**Clasificar**

1. **Identificar el resultado final**: Qué salida debe producir el proceso completo.
2. **Separar subtareas**: Distinguir dependientes (secuenciales) de independientes (paralelas).
3. **Definir salidas intermedias**: Especificar qué resultado alimenta la etapa siguiente.
4. **Validar progresivamente**: Comprobar resultados intermedios antes de continuar. Evitar descomponer en exceso tareas simples.

**Explicación**

Las tareas complejas pueden dividirse en etapas con objetivos y salidas intermedias claras. En el ejemplo, extraer datos, clasificar y resumir son tres etapas encadenadas. Si el resultado final es defectuoso, la descomposición permite saber en qué etapa falló, algo imposible cuando todo se pide en un único prompt.

Los pasos son: identificar el resultado final, separar las subtareas distinguiendo las dependientes de las independientes, definir las salidas intermedias y validar progresivamente. Pero no hay que **descomponer** en exceso las tareas simples: añade coste, tiempo y puntos de fallo sin beneficio. Se justifica cuando hay fases distintas o resultados intermedios que necesitan validación (se desarrolla en el módulo [13](../13-diseno-de-sistemas-de-prompts/README.md)).

---

## 3.6 Instrucciones positivas y negativas

Las instrucciones positivas describen qué hacer; las negativas aclaran límites y comportamientos que deben evitarse. El equilibrio entre ambas produce especificaciones más robustas.

**✅ Instrucciones positivas**

- «*Responde únicamente con la información del documento*»
- «*Si el dato no aparece, escribe no consta*»
- «*Usa un tono formal y directo*»
- «*Incluye una justificación breve por cada categoría*»

**🚫 Instrucciones negativas**

- «*No inventes datos*» → Complementar con alternativa positiva
- «*No uses jerga técnica*» → Especificar el nivel deseado
- «*No repitas el enunciado*» → Aclarar qué sí debe empezar la respuesta

**Regla de oro**

Una prohibición aislada deja sin definir la respuesta correcta ante el caso límite. Siempre complementar con la alternativa positiva deseada.

**Explicación**

Las instrucciones positivas dicen qué hacer; las negativas marcan límites. Un buen equilibrio produce especificaciones más robustas. Ejemplos positivos son «Responde únicamente con la información del documento», «Si el dato no aparece, escribe no consta» o «Usa un tono formal y directo».

Las negativas necesitan complemento: «No inventes datos» debe ir acompañado de qué hacer cuando el dato falta; «No uses jerga técnica», del nivel deseado; «No repitas el enunciado», de cómo debe empezar la respuesta. Una prohibición aislada deja sin definir la respuesta correcta ante el caso límite, y el modelo puede resolverlo de formas muy distintas, incluida la invención sutil. Las prohibiciones son útiles para marcar límites, pero nunca como único control.

---

## 3.7 Delimitadores y separación de secciones

Los encabezados y delimitadores hacen más legible la estructura del prompt y ayudan a identificar sus partes con claridad. Son especialmente útiles en prompts extensos con bloques de datos integrados.

```text
## CONTEXTO
Eres asistente de análisis de operaciones. El usuario es el responsable de calidad.

## TAREA
Extrae las tres incidencias más graves del documento adjunto.

## RESTRICCIONES
- Usa solo la información del documento.
- Si un campo no aparece, indica "no consta".
- No añadas recomendaciones propias.

## DOCUMENTO
[Aquí se inserta el texto del informe de incidencias]

## SALIDA
Tabla con columnas: Incidencia | Gravedad | Fecha | Responsable
```

> ⚠️ Los delimitadores organizan el contenido y mejoran la legibilidad, pero no son una barrera de seguridad absoluta frente a instrucciones maliciosas. La defensa frente a la inyección de prompts requiere controles adicionales.

**Explicación**

Los encabezados y delimitadores hacen más legible la estructura del prompt y ayudan a identificar sus partes, sobre todo cuando hay bloques de datos integrados. El ejemplo organiza un prompt en contexto, tarea, restricciones, documento y salida: una tabla con incidencia, gravedad, fecha y responsable, usando solo la información del documento y «no consta» cuando falte un campo.

La estructura mejora la legibilidad, facilita la edición por bloques y reduce el riesgo de confundir datos con instrucciones. Pero los delimitadores no son una barrera de seguridad absoluta frente a instrucciones maliciosas: la defensa frente a la inyección de prompts requiere controles adicionales (módulo [09](../09-seguridad-privacidad-y-uso-responsable/README.md)).

---

## 3.8 Instrucciones contradictorias y prioridades

Las reglas incompatibles generan resultados impredecibles o fuerzan al modelo a priorizar de forma no deseada. Los conflictos deben resolverse antes de enviar el prompt, no confiar en que el modelo los resuelva correctamente.

- **Contradicción de extensión**: «*Sé exhaustivo*» + «*Responde en una sola frase*» hace imposible cumplir ambas simultáneamente.
- **Contradicción de formato**: «*Devuelve una tabla completa*» + «*No uses tablas*» — El modelo no puede elegir por el usuario.
- **Reglas duplicadas**: Dos restricciones similares con matices distintos generan ambigüedad sobre cuál prevalece.

**Proceso de resolución**

1. Listar todas las condiciones del prompt
1. Identificar pares de reglas que puedan entrar en conflicto
1. Definir explícitamente cuál tiene prioridad en caso de compromiso
1. Eliminar o reformular la regla subordinada

**Explicación**

Las reglas incompatibles generan resultados impredecibles u obligan al modelo a decidir qué prima. Hay contradicciones de extensión («sé exhaustivo» y «una sola frase»), de formato («tabla completa» y «no uses tablas») y reglas duplicadas con matices distintos. En prompts largos, ampliados con el tiempo o por varias personas, es frecuente que una regla nueva contradiga otra antigua.

Para resolverlas: listar todas las condiciones, localizar los pares que puedan chocar, declarar cuál tiene prioridad (por ejemplo, «si hay conflicto entre brevedad y completitud, prevalece la completitud») y eliminar o reformular la subordinada. Conviene repetir esta revisión tras cada cambio importante.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 02B · Anatomía de un prompt: ablación de componentes](../../laboratorios/02B/README.md)
<!-- /labs-seccion -->

---

## 3.9 Manejo de información ausente o incierta

Un prompt robusto especifica qué debe hacer el modelo cuando la entrada no permite una conclusión fiable. No hacerlo incentiva la invención de datos para rellenar los huecos.

![Diagrama con los elementos: Ausente; Inferible con cautela; Disponible; Dato requerido.](img/d29-diagrama.png)

<details>
<summary>Descripción del diagrama en texto</summary>

1. Ausente — Devolver «no consta»
2. Inferible con cautela — Indicar como inferencia
3. Disponible — Usar directamente
4. Dato requerido — Punto de decisión

</details>

- **Campos obligatorios**: Indicar cuáles son imprescindibles para la tarea.
- **Valor por defecto**: Permitir «no consta» o «desconocido» cuando el dato no esté disponible.
- **Solicitar aclaración**: Cuando un dato sea crítico y ausente, el modelo puede pedir la información en lugar de inventarla.
- **Separar tipos**: Distinguir hechos, inferencias y supuestos en la respuesta.

Ejemplo: extracción de una factura sin fecha → devolver «*fecha: no consta*» en lugar de completar el campo con una fecha inventada.

**Explicación**

Un prompt robusto especifica qué hacer cuando la entrada no permite una conclusión fiable. Como el modelo tiende a completar con lo más plausible, si falta la fecha de una factura la respuesta más probable es una fecha creíble, no el reconocimiento de que falta. Por eso la ausencia debe preverse.

El esquema de decisión es: si el dato está disponible, se usa; si es inferible con cautela, se indica como inferencia; si está ausente, se devuelve «no consta». Ayuda indicar los campos obligatorios, permitir «no consta» o «desconocido», dejar que el modelo pida aclaración cuando el dato es crítico y separar hechos, inferencias y supuestos. Una fecha inventada es peor que un campo vacío, porque parece un dato real y puede propagarse a otros sistemas.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 02A · Del prompt vago al contrato de tarea](../../laboratorios/02A/README.md)
<!-- /labs-seccion -->

---

[← Anterior](02-anatomia-de-un-prompt.md) · [Índice del módulo](README.md) · [Siguiente →](04-ejemplos-revision-y-sintesis.md)
