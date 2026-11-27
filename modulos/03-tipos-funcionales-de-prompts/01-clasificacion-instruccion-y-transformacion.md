[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-creatividad-y-resolucion-de-problemas.md)

# 1 · Clasificación, instrucción y transformación

*Módulo 03: Tipos funcionales de prompts*

## 1.1 Cómo clasificar un prompt

Antes de escribir un prompt, analiza el verbo principal y el tipo de salida esperada. Estas dos preguntas guían la elección del tipo funcional más adecuado.

**Preguntas clave**

- ¿Producir, transformar, recuperar, clasificar o evaluar?
- ¿La respuesta es factual, creativa o procedimental?
- ¿Existe una entrada que debe procesarse?
- ¿Hay criterios de decisión explícitos?

**Árbol de decisión por verbo**

- **Verbo de acción concreta**: → Instrucción directa
- **Verbo de pregunta**: → Q&A o extracción
- **Verbo de generar / crear**: → Creatividad o simulación
- **Verbo de analizar / comparar**: → Resolución o comparación

**Explicación**

Antes de escribir un prompt conviene analizar dos cosas: el verbo principal y el tipo de salida esperada. Cuatro preguntas ayudan: si se trata de producir, transformar, recuperar, clasificar o evaluar; si la respuesta es factual, creativa o procedimental; si hay una entrada que procesar; y si existen criterios de decisión explícitos.

El árbol por verbo ofrece una guía rápida: un verbo de acción concreta lleva a la **instrucción directa**; uno de pregunta, a preguntas y respuestas o extracción; uno de generar o crear, a creatividad o simulación; y uno de analizar o comparar, a resolución o **comparación**. Es una primera aproximación: un verbo como «analiza» puede significar extraer, comparar o evaluar, y por eso conviene reformularlo con una operación más concreta.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03A · Catálogo de prompts por tipo funcional](../../laboratorios/03A/README.md)
<!-- /labs-seccion -->

---

## 1.2 Prompts de instrucción directa

Los prompts de instrucción directa son los más habituales en entornos profesionales. Su eficacia depende de la precisión del verbo, la definición del objeto y el establecimiento de condiciones y formatos de salida.

1. **Verbos concretos**: Usar verbos inequívocos: *clasifica, extrae, resume, traduce, lista*. Evitar verbos ambiguos como "habla de" o "explica algo sobre".
2. **Objeto y alcance**: Definir con exactitud sobre qué material actúa el modelo y hasta dónde debe llegar.
3. **Límites y condiciones**: Indicar restricciones: longitud máxima, idioma, campos obligatorios, exclusiones.
4. **Formato de salida**: Especificar si se espera JSON, tabla, lista numerada, párrafo o cualquier otra estructura.

> Ejemplo ilustrativo: «*Clasifica las siguientes incidencias en las categorías Hardware, Software y Red. Justifica brevemente cada asignación en una columna adicional.*»

**Explicación**

Los prompts de instrucción directa son los más habituales en el trabajo profesional. Su eficacia depende de cuatro elementos: verbos inequívocos (clasifica, extrae, resume, traduce, lista) en lugar de otros ambiguos, la definición exacta del objeto y el alcance, los límites y condiciones (longitud, idioma, campos obligatorios, exclusiones) y el formato de salida.

El ejemplo clasifica incidencias en Hardware, Software y Red y pide justificar cada asignación en una columna adicional: verbo, objeto, categorías cerradas y formato en una sola instrucción. Su riesgo principal es la imprecisión, y la mejor defensa es releerla como si se desconociera el contexto y comprobar que el resultado esperado resulta inequívoco.

---

## 1.3 Variantes de instrucción directa

La instrucción directa no es un único patrón: agrupa un conjunto de operaciones habituales que comparten la misma lógica de «verbo + objeto + condiciones». Reconocer estas variantes permite elegir la más adecuada para cada tarea.

- **Clasificar y etiquetar**: Asignar cada elemento a una categoría predefinida y añadir la etiqueta correspondiente.
- **Extraer campos**: Identificar y aislar entidades concretas dentro de un texto no estructurado.
- **Reescribir y normalizar**: Adaptar el estilo, el tono o el formato sin alterar el significado original.
- **Comparar y priorizar**: Evaluar opciones según criterios definidos y ordenarlas por relevancia o urgencia.
- **Generar listas o procedimientos**: Producir pasos, requisitos o inventarios estructurados a partir de un objetivo.

> Ejemplo ilustrativo: Procesar tickets de soporte: clasificar por tipo, extraer prioridad declarada y normalizar el título a un máximo de diez palabras.

**Explicación**

La instrucción directa agrupa varias operaciones con la misma lógica de verbo más objeto más condiciones: clasificar y etiquetar, extraer campos, reescribir y normalizar, comparar y priorizar, y generar listas o procedimientos. El ejemplo de procesar tickets de soporte combina tres de ellas: clasificar por tipo, extraer la prioridad declarada y normalizar el título a diez palabras como máximo.

Reconocer la variante ayuda a recordar su riesgo característico: clasificar sin categorías definidas produce inconsistencias; extraer sin distinguir lo literal de lo inferido produce datos inventados; reescribir sin fijar qué se conserva puede alterar el significado; comparar sin criterios comunes genera valoraciones arbitrarias; y generar listas sin objetivo claro da inventarios genéricos.

---

## 1.4 Prompts de pregunta-respuesta (Q&A)

Los prompts de Q&A orientan al modelo para que responda una pregunta específica. La calidad de la respuesta depende directamente de cómo se formula la pregunta y de si se delimita la fuente de información.

**Tipos de pregunta**

**Parámetros esenciales**

- Audiencia: ¿para quién es la respuesta? Define el nivel de detalle.
- Profundidad: respuesta breve, moderada o exhaustiva.
- Fuente: limitar a un documento cuando se requiere precisión.
- Ausencias: indicar qué hacer si la información no está disponible.

- **Abiertas**: Permiten respuestas elaboradas; útiles para explorar un tema.
- **Cerradas**: Esperan sí/no o un dato concreto; reducen la ambigüedad.
- **Condicionadas**: Vinculan la respuesta a un contexto o documento específico.

Ejemplo ilustrativo: «*Según el texto adjunto, identifica las tres obligaciones del proveedor. Si alguna no aparece explícitamente, indícalo.*»

**Explicación**

Los prompts de preguntas y respuestas (**Q&A**) piden al modelo que responda a una pregunta concreta; la calidad depende de cómo se formula y de si se delimita la fuente. Las preguntas pueden ser abiertas (permiten explorar), cerradas (esperan un sí, no o dato concreto) o condicionadas (vinculan la respuesta a un contexto o documento), que son las más fiables cuando importa la exactitud.

Cuatro parámetros completan la formulación: audiencia, profundidad, fuente y qué hacer si la información no está disponible. Preguntar sin fuente hace que el modelo responda desde su conocimiento general, con riesgo de imprecisión y desactualización; preguntar con fuente permite contrastar la respuesta con un documento concreto.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03B · Una misma tarea, tres tipos de prompt](../../laboratorios/03B/README.md)
<!-- /labs-seccion -->

---

## 1.5 Q&A basado en contexto

Cuando el modelo debe responder a partir de un material concreto, es fundamental anclar la respuesta a esa fuente y gestionar correctamente las ausencias de información. Este enfoque minimiza las alucinaciones y aumenta la trazabilidad.

1. **Identificar la fuente**: Proporcionar el documento, fragmento o base de conocimiento que el modelo debe consultar.
2. **Solicitar evidencia**: Pedir que la respuesta incluya fragmentos textuales o referencias que la sustenten.
3. **Gestionar ausencias**: Indicar explícitamente qué responder si la información no consta: «*Di "no consta" y no inventes*».
4. **Separar hechos de inferencias**: Pedir que el modelo distinga lo que dice la fuente de lo que deduce por razonamiento.
5. **Verificar citas**: Contrastar los fragmentos citados con el texto original antes de usar la respuesta.

> Ejemplo ilustrativo: «*Indica la fecha límite de entrega contractual. Si no aparece en el documento, responde "no consta" y no estimes ningún valor.*»

**Explicación**

Cuando la respuesta debe salir de un material concreto, hay que anclarla a esa fuente y gestionar las ausencias; así se reducen las alucinaciones y aumenta la trazabilidad. Los cinco pasos son: identificar la fuente, pedir evidencia (fragmentos que sustenten la respuesta), gestionar las ausencias (por ejemplo «di no consta y no inventes»), separar hechos de inferencias y verificar las citas contra el original.

En el ejemplo se pide la fecha límite de entrega y se indica que, si no figura, se responda «no consta» sin estimar ningún valor; sin esa cláusula el modelo podría proponer una fecha habitual. Pedir citas reduce el riesgo pero no lo elimina: puede citar un fragmento inexistente o alterar uno real, por lo que la verificación sigue siendo imprescindible, y es más rápida cuando el modelo señala dónde mirar.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03A · Catálogo de prompts por tipo funcional](../../laboratorios/03A/README.md) · [Laboratorio 03B · Una misma tarea, tres tipos de prompt](../../laboratorios/03B/README.md)
<!-- /labs-seccion -->

---

## 1.6 Prompts de completado

Los prompts de completado instruyen al modelo para que continúe una estructura existente: un párrafo, una plantilla, un bloque de código o una sección de documento. La clave es preservar el estilo, el tono y la coherencia con lo ya escrito, sin inventar datos factuales.

- **Completar párrafos o plantillas**: Proporcionar el inicio y pedir la continuación manteniendo la estructura definida.
- **Continuar código o documentación**: Indicar el lenguaje, el contexto y las convenciones del proyecto antes de solicitar el completado.
- **Mantener tono y formato**: Especificar si el texto es formal, técnico o divulgativo para que la continuación sea coherente.
- **No inventar datos ausentes**: Si faltan datos factuales, el modelo debe señalarlo con un marcador como [DATO PENDIENTE] en lugar de estimarlos.

> Ejemplo ilustrativo: «*Continúa la sección de riesgos del informe usando únicamente los datos del análisis adjunto. Mantén el mismo estilo formal y el formato de lista numerada.*»

**Explicación**

Los prompts de **completado** piden continuar una estructura existente (un párrafo, una plantilla, código o una sección de documento) conservando estilo, tono y coherencia sin inventar datos factuales. Las prácticas son: dar el inicio y pedir la continuación respetando la estructura, indicar lenguaje y convenciones al continuar código, especificar el tono y marcar con algo como [DATO PENDIENTE] lo que falte en lugar de estimarlo.

El completado aprovecha que el modelo predice continuaciones y funciona mejor cuando el inicio establece claramente el patrón. Su riesgo es que la fluidez puede ocultar que se está rellenando con datos plausibles lo que debería quedar pendiente; el marcador hace visible lo que falta y es fácil de localizar después.

---

## 1.7 Prompts de transformación

Transformar un contenido implica definir con precisión qué cambia y qué debe conservarse. Sin estas restricciones, el modelo puede alterar significado, cifras o tono de forma inadvertida.

![Cinco operaciones de transformación: 1 traducción, cambiar de idioma conservando el significado; 2 reformulación, reescribir con otras palabras; 3 simplificación, reducir la complejidad para otra audiencia; 4 cambio de tono, de técnico a ejecutivo o viceversa; 5 conversión de formato, de párrafo a tabla o de texto a JSON.](img/d10-1.jpg)

**Qué debe conservarse siempre**

- Cifras, fechas y datos cuantitativos
- Significado y conclusiones principales
- Referencias normativas o contractuales

**Ejemplo ilustrativo**

«*Convierte la siguiente nota técnica en un resumen ejecutivo de máximo 150 palabras. Mantén todas las cifras y no incluyas jerga técnica. El destinatario es el Comité de Dirección.*»

**Explicación**

Transformar un contenido exige definir qué cambia y qué se conserva; si no, el modelo puede alterar significado, cifras o tono sin avisar. Las cinco operaciones son traducción, reformulación, simplificación, cambio de tono y conversión de formato.

Deben conservarse siempre las cifras, fechas y datos cuantitativos, el significado y las conclusiones principales, y las referencias normativas o contractuales; son los puntos donde un cambio pasa más fácilmente inadvertido (un «hasta» que desaparece, una cifra redondeada, una obligación convertida en recomendación). El ejemplo convierte una nota técnica en un **resumen** ejecutivo de 150 palabras, manteniendo las cifras y evitando la jerga. Conviene declarar ambas listas y revisar después cifras, fechas y referencias contra el original.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03A · Catálogo de prompts por tipo funcional](../../laboratorios/03A/README.md)
<!-- /labs-seccion -->

---

## 1.8 Prompts de resumen y síntesis

El resumen no es simplemente recortar texto: implica identificar qué información es crítica para el destinatario y el propósito específico. Un buen prompt de síntesis define audiencia, profundidad y qué elementos nunca pueden omitirse.

> **Resumen ejecutivo**
>
> **Resumen técnico**
>
> **Síntesis temática**
>
> Decisiones clave, riesgos y próximos pasos para un perfil directivo.
>
> Metodología, parámetros y resultados para un equipo especializado.
>
> Agrupación por temas de varios documentos, señalando discrepancias.

**Parámetros obligatorios**

- Audiencia y propósito del resumen
- Extensión máxima admitida
- Elementos que no pueden omitirse: decisiones, responsables, fechas y riesgos

Ejemplo ilustrativo: «*Resume la reunión adjunta en máximo 200 palabras. Incluye obligatoriamente: decisiones adoptadas, responsable de cada acción y fecha límite. Destaca los puntos sin acuerdo.*»

**Explicación**

Resumir no es recortar: es decidir qué información es crítica para el destinatario y el propósito. Se distinguen el resumen ejecutivo (decisiones, riesgos y próximos pasos para un perfil directivo), el técnico (metodología, parámetros y resultados) y la síntesis temática (agrupa varios documentos y señala discrepancias).

Los parámetros obligatorios son la audiencia y el propósito, la extensión máxima y los elementos que no pueden omitirse, como decisiones, responsables, fechas y riesgos. Es importante porque un resumen automático tiende a eliminar justo los detalles específicos que permiten actuar. En el ejemplo, la palabra «obligatoriamente» y la petición de destacar los puntos sin acuerdo evitan omitir datos operativos y presentar como consenso una reunión conflictiva.

---

## 1.9 Prompts de extracción

Los prompts de extracción obtienen campos estructurados a partir de texto no estructurado. La precisión depende de definir con exactitud los nombres de campo, los tipos de dato y cómo representar ausencias, distinguiendo siempre lo literal de lo inferido.

**Campos habituales a extraer**

- Entidades: personas, organizaciones, lugares
- Fechas y plazos
- Importes y unidades
- Referencias y números de documento

**Instrucciones de diseño**

- **Nombre y tipo de campo**: Especificar si es texto, fecha ISO, número o booleano.
- **Literal vs. inferido**: Indicar si el campo debe copiarse tal cual o puede deducirse del contexto.
- **Ausencias**: Usar un marcador explícito como null o "no consta".
- **Contraste con la fuente**: Siempre verificar los valores extraídos contra el documento original.

> Ejemplo ilustrativo: «*Del albarán adjunto, extrae: número de pedido, fecha de emisión (formato AAAA-MM-DD), nombre del proveedor e importe total sin IVA. Si algún campo no aparece, escribe "no consta".*»

**Explicación**

La extracción obtiene campos estructurados a partir de texto libre. La precisión depende de definir los nombres de campo, los tipos de dato y cómo representar las ausencias, distinguiendo lo literal de lo inferido. Los campos habituales son entidades, fechas y plazos, importes y unidades, y referencias o números de documento.

Hay que indicar el nombre y tipo de cada campo (texto, fecha ISO, número o booleano), si se copia tal cual o puede deducirse, cómo marcar las ausencias (null o «no consta») y verificar siempre contra el documento. Si el documento dice «pago a 30 días» y se pide la fecha de vencimiento, calcularla es una inferencia del modelo, no un dato del documento: debe pedirse expresamente y marcarse como inferida. La extracción se profundiza en el módulo [12](../12-analisis-de-informacion-y-datos/README.md).

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03A · Catálogo de prompts por tipo funcional](../../laboratorios/03A/README.md) · [Laboratorio 03B · Una misma tarea, tres tipos de prompt](../../laboratorios/03B/README.md)
<!-- /labs-seccion -->

---

## 1.10 Prompts de clasificación

La clasificación asigna cada elemento de entrada a una categoría predefinida. Para que el modelo opere de forma consistente, las categorías deben estar claramente definidas y se deben establecer reglas para los casos ambiguos y los que no encajan en ninguna clase.

- **Definir clases y límites**: Enumerar todas las categorías posibles con una descripción breve de cada una para evitar solapamientos.
- **Reglas de desempate**: Establecer qué criterio prevalece cuando un elemento podría pertenecer a más de una categoría.
- **Ejemplos por categoría**: Incluir uno o dos ejemplos por clase cuando el límite entre categorías es sutil o técnico.
- **Casos ambiguos y fuera de categoría**: Crear una categoría "Otros" o "Ambiguo" y pedir justificación cuando se use.

> Ejemplo ilustrativo: «*Clasifica cada solicitud adjunta en Consulta, Incidencia o Reclamación. Si no encaja en ninguna, indícalo como "Otros" y justifica en una línea.*»

**Explicación**

La **clasificación** asigna cada elemento a una categoría predefinida. Para que sea consistente hay que definir las clases con una descripción breve para evitar solapamientos, establecer reglas de desempate, incluir uno o dos ejemplos por clase cuando el límite es sutil y prever una categoría «Otros» o «Ambiguo» con justificación.

El error más frecuente es dejar que el modelo invente la taxonomía o aplique criterios distintos en cada ejecución: una misma solicitud podría etiquetarse de formas diferentes y el conjunto resultante no serviría para contar ni automatizar. Las categorías y criterios deben proceder de la organización. Conviene evaluar la clasificación con casos de respuesta conocida, incluidos los dudosos, antes de aplicarla a gran escala.

---

[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-creatividad-y-resolucion-de-problemas.md)
