[← Anterior](03-principios-de-diseno.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../03-tipos-funcionales-de-prompts/README.md)

# 4 · Ejemplos, revisión y síntesis

*Módulo 02: Fundamentos del Prompt Engineering*

## 4.1 Ejemplo completo: resumen ejecutivo

```text
## ROL [componente 1]
Actúa como asistente de análisis de negocio especializado en comunicación ejecutiva.

## CONTEXTO [componente 2]
El destinatario es el comité directivo. El tono debe ser formal y directo.

## TAREA [componente 3]
Sintetiza las decisiones adoptadas, los riesgos identificados y los próximos pasos.

## ENTRADA [componente 4]
---INICIO DOCUMENTO---
[Texto de la reunión de seguimiento del proyecto X — insertar aquí]
---FIN DOCUMENTO---

## RESTRICCIONES [componente 5]
- No añadas información externa al documento.
- Si falta algún dato, indícalo explícitamente.

## SALIDA [componente 6]
Tres secciones con viñetas: Decisiones | Riesgos | Próximos pasos.

## CRITERIOS [componente 7]
Fidelidad al texto fuente y claridad ejecutiva. Máximo 10 viñetas en total.
```

> Resultado ilustrativo: cada sección del prompt evita una ambigüedad diferente. Leer el ejemplo de principio a fin muestra la función de cada bloque.

**Explicación**

El primer ejemplo completo es un resumen ejecutivo anotado por componentes. El rol es un asistente de análisis de negocio especializado en comunicación ejecutiva; el contexto, un comité directivo y un tono formal y directo; la tarea, sintetizar decisiones, riesgos y próximos pasos; la entrada, el texto de la reunión delimitado entre marcas; las restricciones, no añadir información externa e indicar lo que falte; la salida, tres secciones con viñetas; y los criterios, fidelidad al texto y claridad, con un máximo de diez viñetas.

Cada sección evita una ambigüedad: sin rol, el tono sería genérico; sin contexto, no se sabría que el destinatario es la dirección; sin marcas, se mezclarían datos e instrucciones; sin restricciones, podrían inventarse datos; sin formato, la estructura sería imprevisible; sin criterios, no habría forma de evaluar. Es ilustrativo: al aplicarlo hay que probarlo con entradas reales.

---

## 4.2 Ejemplo completo: clasificación de solicitudes

La clasificación requiere definir categorías, reglas, datos de entrada y tratamiento de casos dudosos. Las categorías y criterios deben proceder del negocio; el modelo no inventa la taxonomía.

**Prompt de clasificación (extracto)**

Categorías: Fallo técnico | Consulta de uso | Solicitud de cambio | Incidencia de acceso

Prioridad: Alta (impacto en producción), Media (bloqueo parcial), Baja (mejora o duda)

Ambiguo: Clasificar en la categoría más probable e indicar *«clasificación provisional»*

Incompleto: Devolver «datos insuficientes» y listar qué información falta

Formato: Categoría | Prioridad | Justificación (1 frase)

**Entradas ilustrativas**

Solicitud A: «*No puedo acceder al sistema desde esta mañana.*»

→ Incidencia de acceso | Alta | Impacto en producción inmediato

Solicitud B: «*¿Cómo puedo exportar un informe en PDF?*»

→ Consulta de uso | Baja | Pregunta funcional sin bloqueo

Solicitud C: «*El módulo de facturación da error a veces.*»

→ Fallo técnico | Media | Bloqueo intermitente, clasificación provisional

**Explicación**

El segundo ejemplo es una clasificación de solicitudes. Las categorías (fallo técnico, consulta de uso, solicitud de cambio, incidencia de acceso) y las prioridades (alta por impacto en producción, media por bloqueo parcial, baja por mejora o duda) proceden del negocio: el modelo no inventa la taxonomía. Los casos dudosos tienen tratamiento previsto: si es ambiguo se clasifica en la categoría más probable como «clasificación provisional», y si está incompleto se devuelve «datos insuficientes» y se indica qué falta.

Las tres entradas lo muestran: no poder acceder al sistema desde por la mañana es una incidencia de acceso de prioridad alta; preguntar cómo exportar a PDF es una consulta de uso de prioridad baja; y un error de facturación que ocurre a veces es un fallo técnico de prioridad media, provisional. La salida lleva categoría, prioridad y una justificación de una frase, lo que facilita auditar y procesar.

---

## 4.3 Checklist para revisar un prompt

Una revisión sistemática permite detectar omisiones y ambigüedades antes de utilizar el prompt. No sustituye las pruebas con entradas reales, pero es un control inicial de diseño eficaz.

- **¿Objetivo claro?** El propósito de la tarea está expresado de forma explícita y sin ambigüedad.
- **¿Contexto suficiente?** Se han proporcionado los antecedentes necesarios para interpretar la petición.
- **¿Datos delimitados?** Los datos de entrada están claramente separados de las instrucciones.
- **¿Restricciones coherentes?** Las condiciones no se contradicen entre sí y son realizables.
- **¿Formato definido?** Se ha especificado cómo debe presentarse el resultado.
- **¿Datos ausentes tratados?** Se indica qué debe hacer el modelo si falta información.

> **¿Criterios definidos?**
>
> Existen condiciones observables para evaluar si la respuesta es aceptable.

**Explicación**

La lista de comprobación permite revisar un prompt antes de usarlo. Hace siete preguntas: si el objetivo es claro, si el contexto es suficiente, si los datos están delimitados, si las restricciones son coherentes, si el formato está definido, si se ha previsto qué hacer ante datos ausentes y si hay criterios para evaluar la respuesta. Cada respuesta negativa señala una mejora concreta.

Se aplica antes de la primera ejecución, y no solo cuando falla, porque corregir un prompt es mucho más barato que corregir cientos de resultados defectuosos. No es una garantía: un prompt que supere todas las preguntas puede fallar con entradas reales imprevistas, así que es el primer filtro y la prueba con casos reales, incluidos los difíciles, el segundo.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 02A · Del prompt vago al contrato de tarea](../../laboratorios/02A/README.md)
<!-- /labs-seccion -->

---

## 4.4 Errores frecuentes en el diseño de prompts

Los fallos más habituales proceden de objetivos vagos, contexto insuficiente y expectativas implícitas. Reconocer estos patrones es el primer paso para evitarlos.

| Error | Consecuencia | Corrección |
|---|---|---|
| Varias tareas sin orden | Resultados mezclados o incompletos | Descomponer y secuenciar |
| Sin audiencia ni detalle | Nivel inadecuado de la respuesta | Declarar audiencia y profundidad |
| Mezclar datos e instrucciones | Confusión entre qué hacer y sobre qué | Delimitar bloques con encabezados |
| Restricciones omitidas | Resultado fuera del alcance permitido | Añadir condiciones explícitas |
| Formato sin estructura | Respuesta inusable por sistemas o personas | Definir campos y orden |
| Datos internos no provistos | Invención de información | Incluir todos los datos necesarios |
| Sin validación de respuesta | Errores no detectados | Añadir criterios de aceptación |

**Explicación**

Los fallos habituales proceden de objetivos vagos, contexto insuficiente y expectativas implícitas. La tabla recoge siete: varias tareas sin orden (se corrige descomponiendo), sin audiencia ni detalle (declarándolos), datos mezclados con instrucciones (delimitando bloques), restricciones omitidas (añadiéndolas), formato sin estructura (definiendo campos y orden), datos internos no aportados (incluyéndolos) y sin validación (añadiendo criterios de aceptación).

Cada error corresponde a un componente que falta o está mal definido, de modo que la anatomía de siete componentes sirve también como herramienta de diagnóstico: ante un mal resultado, se recorre la lista y se busca cuál faltaba o era ambiguo.

---

## 4.5 Principios de un prompt eficaz

Un prompt eficaz define una tarea clara, aporta contexto pertinente y establece condiciones verificables. Estos siete principios resumen el método trabajado a lo largo del módulo:

1. **Claridad primero**: Claridad antes que complejidad. Una instrucción simple y clara supera a una instrucción compleja y vaga.
2. **Especificidad proporcional**: El nivel de detalle debe ser proporcional a la complejidad y al impacto de la tarea.
3. **Contexto relevante**: Incluir solo los antecedentes que cambian materialmente la ejecución de la tarea.
4. **Restricciones coherentes**: Reglas explícitas, no contradictorias y realizables por el modelo.
5. **Formato adecuado**: El formato de salida debe adaptarse al uso previsto: lectura, comparación o procesamiento.
6. **Criterios observables**: Definir condiciones de aceptación y tratamiento explícito de la incertidumbre.
7. **Revisión e iteración**: Evaluar resultados reales y mejorar la especificación de forma continua.

**Explicación**

Los siete principios resumen el método: claridad antes que complejidad; **especificidad** proporcional a la complejidad y al impacto; contexto relevante, solo lo que cambia la ejecución; restricciones coherentes y realizables; formato adecuado al uso; criterios observables, con tratamiento explícito de la incertidumbre; y revisión e iteración con resultados reales.

Se agrupan en tres ideas: decir lo necesario, acotar lo posible y comprobar lo obtenido. Ningún prompt está terminado hasta que se ha probado con entradas reales, incluidas las difíciles, y se han corregido los fallos.

Cuando se comparan versiones de un prompt, dos cautelas evitan sacar conclusiones falsas: puntuar con una rúbrica (criterios con una puntuación fijada de antemano, que el módulo 7 desarrolla) y repetir cada prueba, porque el modelo no responde idéntico dos veces (variabilidad) y una sola ejecución puede engañar.

---

## 4.6 Comprobación de comprensión

Piensa cada respuesta, de forma oral o por escrito, antes de ver las respuestas orientativas, que aparecen a continuación.

**Preguntas de comprobación**

1. ¿Qué diferencia hay entre contexto e instrucción?
1. ¿Cuándo conviene definir un rol explícito?
1. ¿Qué aporta un criterio de calidad a la especificación?
1. ¿Por qué conviene delimitar los datos de entrada?
1. ¿Cómo debe tratar el modelo la información ausente?
1. ¿Qué problemas genera una instrucción contradictoria?

---

## 4.7 Comprobación de comprensión: respuestas

Contrasta tus respuestas con estas. Son orientativas: lo importante es que cubran las ideas clave del módulo.

**Preguntas de comprobación y respuestas orientativas**

1. ¿Qué diferencia hay entre contexto e instrucción?

El contexto aporta antecedentes, propósito y audiencia; la instrucción indica la operación concreta que debe realizar el modelo.

1. ¿Cuándo conviene definir un rol explícito?

Cuando una perspectiva especializada cambia el enfoque, el vocabulario o el nivel de detalle; sin títulos decorativos ni credenciales falsas.

1. ¿Qué aporta un criterio de calidad a la especificación?

Convierte expectativas implícitas en condiciones observables para decidir si una respuesta es aceptable.

1. ¿Por qué conviene delimitar los datos de entrada?

Para separar datos de instrucciones, evitar confusiones y reducir el riesgo de que el contenido altere la tarea.

1. ¿Cómo debe tratar el modelo la información ausente?

Indicando que falta (p. ej., «no consta») en lugar de inventarla, y distinguiendo hechos, inferencias y supuestos.

1. ¿Qué problemas genera una instrucción contradictoria?

Resultados impredecibles: el modelo elige una regla sin que se le diga cuál; hay que resolver el conflicto y fijar prioridades antes de ejecutar.

**Explicación**

La comprobación de comprensión propone seis preguntas. El contexto aporta antecedentes, propósito y audiencia, y la instrucción indica la operación. Un rol explícito conviene cuando una perspectiva especializada cambia el enfoque, sin títulos decorativos ni credenciales falsas. Un criterio de calidad convierte expectativas implícitas en condiciones observables. Los datos se delimitan para separarlos de las instrucciones y reducir el riesgo de que alteren la tarea. La información ausente se señala (por ejemplo con «no consta»), distinguiendo hechos, inferencias y supuestos. Y una instrucción contradictoria produce resultados impredecibles, por lo que hay que resolver el conflicto y fijar prioridades antes de ejecutar.

El módulo [03](../03-tipos-funcionales-de-prompts/README.md) aplica esta estructura a los distintos tipos funcionales de prompts, y el bloque 2 presenta técnicas que amplían el control: ejemplos, personas, formatos estructurados y parámetros.

---

[← Anterior](03-principios-de-diseno.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../03-tipos-funcionales-de-prompts/README.md)
