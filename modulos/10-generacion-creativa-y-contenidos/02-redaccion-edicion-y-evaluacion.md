[← Anterior](01-ideacion-y-briefing.md) · [Índice del módulo](README.md) · [Siguiente →](03-produccion-multimedia-y-derechos.md)

# 2 · Redacción, edición y evaluación

*Módulo 10: Generación creativa y producción de contenidos*

## 2.1 Artículos y publicaciones

El prompt para un artículo debe comportarse como un encargo editorial completo. Cuanto más específica sea la instrucción, menos trabajo de edición requerirá el borrador resultante.

- **Propósito y audiencia**: ¿Qué acción debe tomar el lector al finalizar? ¿Cuánto sabe ya del tema?
- **Estructura o esquema**: Especifica las secciones, el número de palabras por sección y el tipo de contenido (argumento, ejemplo, dato).
- **Fuentes y datos**: Indica si el modelo puede citar fuentes o solo usar el material que le proporcionas. Siempre valida los datos antes de publicar.
- **Tono y longitud**: Especifica nivel de formalidad, uso de segunda persona, párrafos cortos vs. densos y longitud total en palabras.
- **Revisión factual**: Nunca publiques sin verificar cifras, citas y nombres propios generados por el modelo.

**Explicación**

El prompt para un artículo debe ser un encargo editorial completo: cuanto más específico, menos edición necesitará el borrador. Incluye propósito y audiencia (qué debe hacer el lector al terminar y cuánto sabe del tema), estructura (secciones, palabras por sección y tipo de contenido), fuentes y datos (si el modelo puede citar fuentes o solo usar el material aportado), tono y longitud, y revisión factual (nunca publicar sin verificar cifras, citas y nombres propios).

Un artículo fluido puede contener datos inventados o citas inexistentes, y la fluidez los hace menos visibles; el modelo añade a menudo una estadística plausible para dar fuerza a un argumento. Por eso conviene aportar uno mismo cifras y fuentes y pedir que se limite a ellas. Se parece a encargar a un redactor humano: con objetivo, público, esquema, fuentes y extensión, entrega algo mucho más cercano a lo necesario; la diferencia es que el modelo no pregunta lo que no sabe, lo suple con supuestos.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 10B · Campaña multicanal con voz de marca](../../laboratorios/10B/README.md)
<!-- /labs-seccion -->

---

## 2.2 Storytelling con propósito

Una narrativa eficaz no es una colección de hechos: es una secuencia emocional que lleva al lector desde su situación actual hasta la comprensión o acción deseada. El LLM puede construir esa secuencia si le das los ingredientes correctos.

1. **Personaje**: Protagonista con quien el lector se identifica.
2. **Objetivo y conflicto**: Qué quiere conseguir y qué obstáculo lo impide.
3. **Contexto y evolución**: El mundo en que vive y cómo cambia a lo largo de la historia.
4. **Punto de inflexión**: El momento decisivo que cambia el rumbo de la historia.
5. **Resolución y mensaje**: El desenlace y la idea que debe quedarse en la mente del lector.

> Especifica siempre la coherencia con la audiencia: una historia que emociona a un técnico puede dejar frío a un directivo y viceversa.

**Explicación**

Una narrativa eficaz es una secuencia emocional que lleva al lector desde su situación actual hasta la comprensión o la acción deseada. El modelo puede construirla si recibe cinco ingredientes: un personaje con el que el lector se identifica, un objetivo y un conflicto, un contexto que evoluciona, un punto de inflexión y una resolución con el mensaje que debe quedar.

Hay que adaptarlo a la audiencia: lo que emociona a un técnico puede dejar frío a un directivo. Con público técnico el conflicto puede ser un problema de arquitectura; con directivo, una decisión estratégica. Conviene pedir primero la estructura en cinco pasos, sin desarrollar el texto, y revisarla antes de solicitar la redacción final, porque corregir un esquema es mucho más barato que corregir un texto largo escrito sobre uno defectuoso.

---

## 2.3 Guiones y diálogos

El contenido hablado tiene reglas distintas al escrito: las frases deben sonar naturales al pronunciarse en voz alta, los turnos deben ser cortos y el ritmo debe mantener la atención.

**Elementos del prompt de guion**

- Formato y duración: vídeo explicativo de 90 s, podcast de 10 min…
- Personajes y voces: narrador neutro, dos expertos, presentador y cliente…
- Escena y conflicto: contexto de la situación inicial.
- Ritmo y transiciones: indica pausas, cambios de tema y cierres.
- Indicaciones de locución: énfasis, velocidad, tono en momentos clave.

**Ejemplo ilustrativo**

*«Escribe un guion de 90 segundos para dos locutores (Ana, experta técnica, y Luis, usuario no técnico). Ana explica qué es un prompt en lenguaje coloquial. Luis hace preguntas que podría tener cualquier principiante. Incluye indicaciones de pausa y énfasis. Formato de guion con turnos etiquetados.»*

Siempre revisa la naturalidad leyendo en voz alta antes de producir.

**Explicación**

El contenido hablado tiene reglas distintas del escrito: las frases deben sonar naturales en voz alta, los turnos ser cortos y el ritmo mantener la atención. El prompt de guion incluye formato y duración, personajes y voces, escena y conflicto, ritmo y transiciones, e indicaciones de locución (énfasis, velocidad y tono).

El ejemplo pide un guion de 90 segundos para dos locutores (una experta técnica y un usuario no técnico) en el que ella explica qué es un prompt en lenguaje coloquial y él formula preguntas de principiante, con indicaciones de pausa y énfasis y turnos etiquetados. Es útil leer el texto en voz alta antes de producir: una frase que cuesta decir no está bien escrita para ser oída. Un interlocutor que hace las preguntas del público permite explicar sin parecer condescendiente.

---

## 2.4 Adaptación multicanal

El mismo mensaje central puede y debe vivir en múltiples canales, pero cada uno tiene sus propias convenciones de longitud, formato y llamada a la acción. El LLM puede adaptar con precisión si le indicas las diferencias explícitamente.

- **Web / Landing page**: Titular impactante, cuerpo de 150-250 palabras, CTA claro. Lenguaje directo y orientado a beneficio.
- **Correo electrónico**: Asunto de 6-9 palabras, preheader, cuerpo breve con un único CTA. Personalización en saludo.
- **Redes sociales**: Formato nativo por plataforma: anzuelo en las primeras líneas, hashtags pertinentes, CTA adaptado.

**Explicación**

El mismo mensaje central puede vivir en varios canales, pero cada uno tiene sus convenciones de longitud, formato y llamada a la acción. La web o página de aterrizaje pide titular impactante, cuerpo de 150 a 250 palabras y llamada a la acción clara, con lenguaje directo y orientado al beneficio. El correo, un asunto de seis a nueve palabras, un texto de previsualización, un cuerpo breve con una única llamada a la acción y personalización. Las redes sociales, formato nativo por plataforma, un gancho en las primeras líneas, etiquetas pertinentes y una llamada a la acción adaptada.

Pedir «adapta esto a todos los canales» sin dar sus convenciones produce un texto uniforme con ajustes superficiales. Es mejor indicar para cada canal longitud, tono y acción, o dar una pieza aprobada como referencia. Las convenciones cambian con el tiempo, y la adaptación no debe alterar el mensaje ni las afirmaciones: una versión corta no puede prometer lo que la larga no promete.

---

## 2.5 Tono y voz de marca

La consistencia editorial es lo que hace que una empresa suene a sí misma en todos sus canales. Incluir una guía de estilo compacta directamente en el prompt es la forma más efectiva de transferir esa identidad al modelo.

- **Atributos de voz**: Ej.: cercana, rigurosa, optimista, sin jerga innecesaria.
- **Vocabulario preferido**: Lista de términos de marca y sinónimos aprobados.
- **Expresiones a evitar**: Clichés, anglicismos no aprobados, términos de la competencia.
- **Nivel de formalidad**: Tuteo vs. ustedeo, uso de imperativo, longitud de frases.
- **Ejemplos de referencia**: Incluye 2-3 fragmentos aprobados como ancla estilística para el modelo.

**Explicación**

La consistencia editorial hace que una marca suene a sí misma en todos sus canales, y la forma más efectiva de transferirla al modelo es incluir en el prompt una guía de estilo compacta con cinco componentes: atributos de voz (cercana, rigurosa, optimista, sin jerga innecesaria), vocabulario preferido y sinónimos aprobados, expresiones a evitar, nivel de formalidad (tuteo o trato de usted, uso del imperativo, longitud de frases) y dos o tres ejemplos de referencia.

Describir un estilo con adjetivos ayuda, pero mostrar ejemplos reales suele ser más eficaz, porque el modelo imita mejor lo que ve que lo que se le describe (aprendizaje en contexto del módulo [04](../04-tecnicas-avanzadas-de-prompting/README.md)). La guía debe ser compacta, porque todo lo incluido consume espacio y compite por la atención: media página con lo esencial se aplica mejor que veinte. Si el modelo repite un desvío, se añade una regla específica, como en el refinamiento del módulo [07](../07-ciclo-de-vida-y-evaluacion/README.md).

---

## 2.6 Edición y refinamiento

El primer borrador del modelo es el punto de partida, no el destino. El prompting de edición permite mejorar el texto de forma quirúrgica, sin que el modelo reescriba todo y pierda la intención original.

**Instrucciones de edición efectivas**

- «*Elimina redundancias sin cambiar el significado.*»
- «*Acorta a 150 palabras manteniendo los tres puntos principales.*»
- «*Sustituye la metáfora del párrafo 2 por una más concreta.*»
- «*Mejora la fluidez entre los párrafos 3 y 4 sin añadir información.*»

**Proceso recomendado**

1. Revisar estructura: ¿el orden lógico es el correcto?

2. Eliminar redundancias: cada frase debe añadir algo nuevo.

3. Mejorar precisión: sustituir términos vagos por concretos.

4. Comparar versiones: solicita siempre al modelo que muestre los cambios realizados para validar que no alteró el sentido.

**Explicación**

El primer borrador es el punto de partida, no el destino. El prompting de edición mejora el texto de forma quirúrgica sin que el modelo reescriba todo y pierda la intención. Las instrucciones efectivas son concretas y acotadas, e indican qué cambiar y qué conservar: eliminar redundancias sin cambiar el significado, acortar a 150 palabras manteniendo los tres puntos principales, sustituir una metáfora por otra más concreta o mejorar la fluidez entre dos párrafos sin añadir información.

El proceso tiene cuatro pasos: revisar la estructura, eliminar redundancias, mejorar la precisión sustituyendo términos vagos y comparar versiones pidiendo al modelo que muestre los cambios realizados. Este último paso es una salvaguarda: al editar, un modelo puede modificar sin avisar un dato, un matiz o una cifra, y la lista de cambios permite detectarlo. Se trabaja de lo estructural a lo detallado, porque pulir frases de un párrafo que luego se eliminará es trabajo perdido.

---

## 2.7 Evaluación editorial

Antes de dar por buena una pieza generada, aplica esta rúbrica de seis criterios. Puedes pedirle al propio modelo que autoevalúe el texto usando estos mismos criterios como instrucción de verificación.

- **Adecuación al briefing**: ¿Responde al objetivo y audiencia definidos?
- **Relevancia**: ¿Todo el contenido es pertinente? ¿Sobra algo?

**Claridad**

**Exactitud**

¿Los datos, cifras y citas son verificables?

¿Es comprensible para la audiencia objetivo?

- **Originalidad**: ¿Aporta algo nuevo o replica lugares comunes?
- **Marca y canal**: ¿Cumple con la guía de estilo y el formato del canal?

**Explicación**

Antes de dar por buena una pieza se aplica una rúbrica editorial de seis criterios, y puede pedirse al modelo que autoevalúe el texto con ellos: adecuación al briefing, relevancia, claridad, exactitud (datos, cifras y citas verificables), originalidad (si aporta algo nuevo o replica lugares comunes) y ajuste a la marca y al canal.

Dos advertencias. La autoevaluación detecta problemas evidentes, pero no equivale a una verificación independiente: quien revisa y quien genera comparten sesgos. Y la exactitud es el criterio que más requiere intervención humana, porque es la más afectada por las alucinaciones. La rúbrica funciona mejor como lista de comprobación, con cada criterio marcado y justificado; los de exactitud y marca suelen requerir revisión humana y los de claridad y relevancia se benefician de la ayuda del modelo. La decisión de publicar es de una persona.

---

[← Anterior](01-ideacion-y-briefing.md) · [Índice del módulo](README.md) · [Siguiente →](03-produccion-multimedia-y-derechos.md)
