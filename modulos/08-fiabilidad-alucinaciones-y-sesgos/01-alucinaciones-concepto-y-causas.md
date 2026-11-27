[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-mitigacion-de-alucinaciones.md)

# 1 · Alucinaciones: concepto y causas

*Módulo 08: Fiabilidad, alucinaciones y sesgos*

## 1.1 ¿Qué significa fiabilidad en un LLM?

La fiabilidad no es una propiedad binaria: es un conjunto de dimensiones que deben evaluarse según el contexto de uso. Un modelo puede ser muy exacto en un dominio y poco fiable en otro.

- **Exactitud factual**: Las afirmaciones corresponden a hechos verificables en las fuentes disponibles.
- **Consistencia**: El modelo ofrece respuestas coherentes ante preguntas equivalentes reformuladas.
- **Fidelidad a fuentes**: El contenido generado se mantiene dentro de lo que respaldan los documentos aportados.
- **Calibración de incertidumbre**: El modelo reconoce sus límites y los comunica de forma adecuada.
- **Robustez**: Las respuestas no degradan significativamente ante variaciones menores en la entrada.
- **Adecuación al uso**: El nivel de precisión requerido varía: un borrador creativo no exige los mismos controles que un informe médico.

**Explicación**

La **fiabilidad** no es una propiedad binaria, sino un conjunto de dimensiones que se evalúan según el contexto de uso. La exactitud en un dominio no se traslada sin más a otro: el mismo modelo puede acertar mucho en uno y poco en otro. Las dimensiones son: exactitud factual, consistencia ante preguntas equivalentes reformuladas, fidelidad a las fuentes aportadas, **calibración** de la incertidumbre (reconocer y comunicar sus límites), robustez ante variaciones menores de la entrada y adecuación al uso.

Hablar de fiabilidad en singular puede inducir a error: un modelo puede ser consistente e inexacto (repetir siempre el mismo error), fiel a las fuentes y poco robusto, o exacto y mal calibrado. Cada dimensión se comprueba de forma distinta. La adecuación al uso recuerda la regla de proporcionalidad: un borrador creativo no exige los mismos controles que un informe médico.

---

## 1.2 ¿Qué es una alucinación?

Una **alucinación** es una afirmación falsa o no sustentada que el modelo presenta con apariencia de plausibilidad. No es un error de sintaxis: la respuesta suena razonable, está bien escrita y puede mezclar datos reales con elementos inventados, lo que complica enormemente su detección.

- **Puede afectar cualquier tipo de dato**: Nombres, cifras, citas bibliográficas, fechas y relaciones causales son igualmente vulnerables.
- **Mezcla verdad e invención**: La coexistencia de datos correctos e incorrectos dificulta separar lo fiable de lo fabricado.
- **El estilo no es indicador suficiente**: Un tono seguro y una prosa fluida no implican exactitud. Se necesita evidencia externa.

> ⚠️ Ejemplo ilustrativo: «*Según el estudio de Harvard (2021) publicado en Nature, el 73 % de los profesionales...*» — La referencia puede no existir aunque el dato parezca concreto.

**Explicación**

Una **alucinación** es lo que el modelo afirma sin sustento o en falso, pero con apariencia de plausibilidad. No es un error de sintaxis: la respuesta suena razonable, está bien escrita y puede mezclar datos reales con inventados. Afecta a cualquier tipo de dato (nombres, cifras, citas, fechas, relaciones causales) y el estilo no es indicador suficiente de exactitud.

Un ejemplo es «Según el estudio de Harvard (2021) publicado en Nature, el 73 % de los profesionales…»: la precisión de la cifra y las instituciones prestigiosas dan apariencia de rigor, pero la referencia puede no existir. La mezcla de verdad e invención es lo más peligroso, porque la parte correcta presta credibilidad a la incorrecta; por eso, en tareas críticas, cada dato relevante necesita su propia comprobación y no basta con verificar una muestra.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 08A · Cazar alucinaciones](../../laboratorios/08A/README.md)
<!-- /labs-seccion -->

---

## 1.3 Formas de alucinación: catálogo de patrones

Conocer los patrones más habituales permite diseñar comprobaciones específicas. Cada tipo requiere una estrategia de verificación diferente.

| Patrón | Descripción | Ejemplo ilustrativo |
|---|---|---|
| Referencias inexistentes | Artículos, libros o estudios que no existen. | «Smith et al., 2019, Journal of AI Ethics» |
| Estadísticas inventadas | Cifras precisas sin fuente real. | «El 68 % de las empresas reportó...» |
| Atribuciones incorrectas | Citas asignadas a personas que no las dijeron. | Frase atribuida a Einstein sin evidencia. |
| Detalles añadidos a fuentes | El modelo completa con datos no presentes en el original. | Añadir resultados a un estudio real. |
| Causalidad no demostrada | Correlación presentada como causa-efecto. | «X provoca Y» sin respaldo empírico. |
| Confusión entre entidades | Mezcla de propiedades entre personas u organizaciones similares. | Datos de empresa A asignados a empresa B. |

**Explicación**

Conocer los patrones permite diseñar comprobaciones específicas. La tabla recoge seis: referencias inexistentes (artículos o estudios que no existen), estadísticas inventadas (cifras precisas sin fuente), atribuciones incorrectas (citas asignadas a quien no las dijo), detalles añadidos a fuentes (el modelo completa con datos que no están en el original), causalidad no demostrada (correlación presentada como causa) y confusión entre entidades (propiedades mezcladas entre personas u organizaciones parecidas).

Cada patrón sugiere su comprobación: buscar las referencias en bases bibliográficas, rastrear las estadísticas hasta su fuente primaria, contrastar las atribuciones, comparar línea a línea con el documento original, valorar el método para la causalidad y contrastar cada dato con la ficha de la entidad correcta. Cuando la fuente es real, la tranquilidad es engañosa: un modelo puede añadir a un estudio auténtico una conclusión que no contiene.

---

## 1.4 ¿Por qué aparecen las alucinaciones?

Las alucinaciones no son fallos aleatorios: emergen de la naturaleza estadística del proceso de generación. Comprender sus causas ayuda a diseñar mejores prompts y sistemas de verificación.

- **Generación de continuaciones plausibles**: El modelo predice el siguiente token más probable, no el más verdadero. La plausibilidad estadística y la exactitud factual son métricas distintas.
- **Contexto insuficiente o ambiguo**: Cuando el prompt no aporta información suficiente, el modelo rellena los huecos con patrones del entrenamiento, que pueden no corresponder al caso concreto.
- **Datos fuera del conocimiento disponible**: Preguntas sobre eventos recientes, datos internos o dominios muy especializados aumentan el riesgo de fabricación.
- **Presión por responder**: El modelo tiende a generar una respuesta completa incluso cuando no tiene información suficiente para hacerlo con precisión.
- **Fuentes ruidosas o contradictorias**: El corpus de entrenamiento contiene información inconsistente; el modelo puede promediar o combinar versiones incompatibles.

**Explicación**

Las alucinaciones no son fallos aleatorios: emergen de la naturaleza estadística de la generación. Hay cinco causas: el modelo predice el token más probable, no el más verdadero; con un contexto insuficiente o ambiguo rellena los huecos con patrones de su entrenamiento; ante datos fuera de su conocimiento (eventos recientes, datos internos, dominios muy especializados) aumenta el riesgo de fabricación; siente presión por responder aunque no tenga información suficiente; y las fuentes de su entrenamiento pueden ser ruidosas o contradictorias.

Las causas se traducen en medidas de diseño: aportar el contexto necesario, proporcionar los datos que no tiene o conectar una fuente, dar permiso explícito para decir que no sabe y pedirle que señale las discrepancias en lugar de resolverlas. La presión por responder está ligada a que el ajuste que convierte un modelo en asistente lo hace servicial, y una respuesta completa suele valorarse más que una negativa; por eso la instrucción de declarar desconocimiento cambia la conducta por defecto.

---

## 1.5 Fluidez no equivale a verdad

- **Un texto bien escrito puede ser completamente falso.** Esta es una de las intuiciones más difíciles de corregir. El cerebro humano interpreta la claridad, el vocabulario técnico y la sintaxis correcta como señales de competencia y veracidad. Los LLM explotan exactamente estos mecanismos.
- **❌ Respuesta fluida pero no fundamentada**: «*El Protocolo de Lisboa (2018) establece en su artículo 7 que las empresas con más de 500 empleados deben...*» — Tono autoritativo, cita específica, estructura normativa. Sin embargo, el protocolo no existe.

**✅ Principios de verificación**

- Tono seguro ≠ exactitud demostrada
- Coherencia interna puede coexistir con falsedad
- La confianza verbal no es probabilidad calibrada
- Siempre contrastar con fuentes primarias
- En tareas críticas: revisión humana obligatoria

**Explicación**

Un texto bien escrito puede ser completamente falso. El cerebro humano interpreta la claridad, el vocabulario técnico y la sintaxis correcta como señales de competencia y veracidad, y los LLM producen justo esas características sin intención. El ejemplo, un «Protocolo de Lisboa (2018)» con un artículo 7 sobre empresas de más de 500 empleados, tiene tono autoritativo, cita específica y estructura normativa, pero el protocolo no existe: cada rasgo que invita a creerlo es parte de la invención.

Los principios de verificación son que el tono seguro no equivale a exactitud, que la coherencia interna puede coexistir con la falsedad, que la confianza verbal no es una probabilidad calibrada, que hay que contrastar con fuentes primarias y que en tareas críticas la revisión humana es obligatoria. La coherencia interna es necesaria en un buen texto, pero no suficiente para la verdad: para saber si lo que dice es cierto hay que acudir a algo externo al texto.

---

## 1.6 Hechos, inferencias, supuestos y opiniones

Separar estas categorías es una habilidad crítica para evaluar cualquier salida de un LLM. El modelo no siempre distingue entre ellas de forma explícita; el diseño del prompt puede forzar esa separación.

| Categoría | Definición | Ejemplo ilustrativo | Acción recomendada |
|---|---|---|---|
| Hecho respaldado | Verificable en una fuente primaria identificable. | «La Constitución española fue aprobada en referéndum el 6 de diciembre de 1978.» | Verificar la fuente citada. |
| Inferencia derivada | Conclusión lógica a partir de evidencia, pero no directamente observada. | «Dado el tiempo transcurrido desde su aprobación, es probable que...» | Comprobar validez del razonamiento. |
| Supuesto provisional | Dato asumido sin confirmación por necesidad operativa. | «Asumiendo que la tasa se mantiene constante...» | Explicitar y revisar el supuesto. |
| Opinión valorativa | Juicio que depende de criterios subjetivos o normativos. | «Esta política es injusta porque...» | Etiquetar como opinión; pedir criterios. |

> En prompts de análisis, instruye al modelo para que etiquete explícitamente cada afirmación con su categoría epistémica.

**Explicación**

Separar hechos, inferencias, **supuestos** y opiniones es una habilidad crítica para evaluar cualquier salida, y el prompt puede forzarla. Un hecho respaldado es verificable en una fuente primaria identificable (acción: verificar la fuente). Una inferencia derivada es una conclusión lógica a partir de evidencia, pero no observada directamente (acción: comprobar la validez del razonamiento). Un supuesto provisional es un dato asumido por necesidad operativa sin confirmarlo (acción: explicitarlo y revisarlo). Una opinión valorativa depende de criterios subjetivos o normativos (acción: etiquetarla como opinión y pedir los criterios).

En prompts de análisis conviene instruir al modelo para que etiquete cada afirmación con su categoría. Sin esa separación, los cuatro tipos se funden en un texto fluido y el lector tiende a leerlo todo como hechos; con ella, la salida es auditable.

---

[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-mitigacion-de-alucinaciones.md)
