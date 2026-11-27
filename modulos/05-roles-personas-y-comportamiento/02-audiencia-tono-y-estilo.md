[← Anterior](01-roles-y-personas.md) · [Índice del módulo](README.md) · [Siguiente →](03-profundidad-comportamiento-y-asistentes.md)

# 2 · Audiencia, tono y estilo

*Módulo 05: Roles, personas y comportamiento*

## 2.1 Audiencia destinataria: adaptar la respuesta al lector

El mismo contenido puede ser útil o inútil dependiendo de quién lo lee. Especificar la audiencia en el prompt es una de las palancas más eficaces para mejorar la calidad de la respuesta sin cambiar el fondo del mensaje.

| Dimensión | Principiante | Técnico | Directivo |
|---|---|---|---|
| Vocabulario | Sin jerga; analogías cotidianas | Terminología precisa del dominio | Términos de negocio y KPIs |
| Profundidad | Conceptual, paso a paso | Mecanismos y parámetros | Impacto y decisión |
| Ejemplos | Situaciones cotidianas | Casos de implementación | Casos de negocio y ROI |
| Longitud | Breve y gradual | Completa y referenciada | Ejecutiva y sintetizada |

**Explicación**

El mismo contenido puede ser útil o inútil según quién lo lea, y especificar la audiencia es una de las palancas más eficaces. La tabla compara tres perfiles: el principiante necesita un lenguaje sin jerga, analogías cotidianas, enfoque conceptual paso a paso y respuestas breves y graduales; el técnico, terminología precisa, mecanismos y parámetros, casos de implementación y respuestas completas y referenciadas; el directivo, términos de negocio e indicadores, enfoque en impacto y decisión, casos de negocio y retorno, y respuestas ejecutivas y sintetizadas.

Si no se declara la audiencia, el modelo adopta un **registro** intermedio que probablemente no sirva bien a ninguno. Conviene indicar también qué sabe el lector y qué necesita hacer con la respuesta: «un directivo que debe decidir si aprueba un presupuesto» orienta más que «un directivo».

Al adaptar un texto a otra audiencia hay una condición que no cambia: la fidelidad. La versión adaptada cambia el vocabulario, el tono y la profundidad, pero mantiene los mismos hechos, cifras y plazos que el original; si la adaptación omite uno o añade otro, deja de ser una adaptación y pasa a ser otro texto.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 05A · Un mismo contenido, tres audiencias](../../laboratorios/05A/README.md)
<!-- /labs-seccion -->

---

## 2.2 Tono y formalidad: controlar el registro comunicativo

El tono define la distancia entre el asistente y el lector. Un tono inadecuado puede hacer que un contenido correcto parezca inapropiado o poco profesional. Especifica el registro de forma explícita en el prompt.

- **Formal**: Usted, tercera persona, sin coloquialismos. Documentos legales, informes corporativos.
- **Neutro**: Profesional pero accesible. Comunicaciones internas estándar, correos de negocio.
- **Cercano**: Tú, primera persona plural. Materiales formativos, comunicación de equipo.
- **Conversacional**: Informal, directo, con ejemplos cotidianos. Chatbots de atención al cliente, FAQs.

> Recomendación: Evita la informalidad excesiva en contextos profesionales y mantén la consistencia de tono a lo largo de toda la respuesta. Un cambio de registro en mitad de un texto rompe la cohesión y genera desconfianza.

**Explicación**

El tono define la distancia entre el asistente y el lector, y uno inadecuado puede hacer que un contenido correcto parezca poco profesional. Los cuatro registros son: formal (trato de usted, tercera persona, sin coloquialismos; documentos legales e informes), neutro (profesional pero accesible; comunicaciones internas y correos de negocio), cercano (tuteo y primera persona del plural; materiales formativos y comunicación de equipo) y conversacional (informal y directo; chatbots y preguntas frecuentes).

Hay que evitar la informalidad excesiva en contextos profesionales y mantener el registro a lo largo de toda la respuesta: un asistente que empieza de usted y pasa al tuteo da impresión de descuido. Conviene declarar el registro en el prompt de sistema y concretarlo con reglas observables (persona gramatical, tratamiento, uso de coloquialismos).

---

## 2.3 Estilos de escritura: técnico, divulgativo y ejecutivo

El estilo determina cómo se expresa el contenido, más allá del tono. Cada estilo responde a un propósito distinto y a una audiencia diferente. A continuación, el mismo concepto —la latencia de red— expresado en tres estilos distintos *(ejemplo ilustrativo)*:

- **🔬 Técnico**: «*La latencia de red mide el tiempo de ida y vuelta (RTT) en ms entre cliente y servidor; valores superiores a 100 ms degradan la experiencia de usuario en aplicaciones interactivas.*»
- **📖 Divulgativo**: «*La latencia es el tiempo que tarda la información en ir del servidor a tu pantalla y volver. Cuando es alta, la aplicación parece lenta aunque tu internet funcione bien.*»
- **📊 Ejecutivo**: «*Una latencia elevada reduce la satisfacción del usuario y puede aumentar la tasa de abandono. Optimizarla es prioritaria antes del lanzamiento.*»

Existen también el estilo académico (estructura argumentativa y cautela epistemológica) y el narrativo (secuencia y recursos expresivos). Elige el que mejor sirva al objetivo del documento.

**Explicación**

El estilo determina cómo se expresa el contenido, más allá del tono. El mismo concepto, la latencia de red, aparece en tres estilos: técnico (tiempo de ida y vuelta en milisegundos y umbrales), divulgativo (el tiempo que tarda la información en ir al servidor y volver, explicado desde la experiencia) y ejecutivo (consecuencias para la satisfacción y el abandono, y prioridad antes del lanzamiento). También existen el estilo académico (estructura argumentativa y cautela) y el narrativo.

El tono expresa la actitud hacia el lector y el estilo organiza la forma de presentar el contenido: un texto técnico puede tener un tono cercano, y uno ejecutivo, un tono formal. Especificar ambos por separado da más control que pedir un único «estilo profesional».

---

## 2.4 Voz y consistencia: mantener la identidad comunicativa

Una voz consistente genera confianza y profesionalidad. Para mantenerla en prompts de larga duración o en sistemas de asistencia, debes codificar las reglas de estilo directamente en la instrucción.

**Elementos de una guía de estilo reducida**

- Rasgos positivos: directo, preciso, sin jerga innecesaria.
- Vocabulario preferido: «*propuesta*» en lugar de «*solución*», «*equipo*» en lugar de «*recursos humanos*».
- Expresiones a evitar: «*en el contexto de*», «*es importante destacar que*», eufemismos corporativos.
- Reglas para títulos: frases nominales breves, sin verbo.
- Reglas para listas: máximo 5 ítems; ítems paralelos en forma.

**Cómo revisar desviaciones**

Incluye en el prompt una instrucción de autoevaluación: «*Antes de responder, verifica que el tono sea neutro y que no hayas usado las expresiones de la lista de exclusión.*»

**Señales de inconsistencia**

- Cambio de persona gramatical a mitad del texto.
- Mezcla de registros formal e informal.
- Variación en la terminología para el mismo concepto.

**Explicación**

Una **voz** consistente genera confianza, y para mantenerla en prompts largos o en sistemas de asistencia hay que codificar las reglas de estilo en la instrucción. Una guía reducida incluye rasgos positivos (directo, preciso, sin jerga), vocabulario preferido, expresiones a evitar (por ejemplo «es importante destacar que»), reglas para títulos y reglas para listas.

Para revisar desviaciones se puede añadir una instrucción de autoevaluación: antes de responder, verificar el tono y la lista de exclusión. Son señales de inconsistencia el cambio de persona gramatical, la mezcla de registros y la variación de terminología para un mismo concepto. Las reglas observables son más eficaces que los adjetivos, y dos o tres textos aprobados como referencia refuerzan el resultado.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 05A · Un mismo contenido, tres audiencias](../../laboratorios/05A/README.md) · [Laboratorio 05B · Un asistente con rol, límites y voz consistente](../../laboratorios/05B/README.md)
<!-- /labs-seccion -->

---

[← Anterior](01-roles-y-personas.md) · [Índice del módulo](README.md) · [Siguiente →](03-profundidad-comportamiento-y-asistentes.md)
