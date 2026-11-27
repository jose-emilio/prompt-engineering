[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-audiencia-tono-y-estilo.md)

# 1 · Roles y personas

*Módulo 05: Roles, personas y comportamiento*

## 1.1 ¿Qué aporta un rol al prompt?

Asignar un rol no es un truco mágico: es una instrucción que orienta al modelo sobre la perspectiva desde la que debe responder. Un rol pertinente mejora la coherencia del vocabulario, el enfoque analítico y la estructura de la respuesta.

**✗ Prompt sin rol**

«*Explica qué es el churn en una empresa SaaS.*»

El modelo elige libremente el nivel técnico, el tono y el enfoque. El resultado puede ser demasiado genérico o inadecuado para el lector.

**✓ Prompt con rol**

«*Actúa como analista de retención de clientes en una empresa SaaS B2B. Explica qué es el churn a un equipo de ventas que no tiene formación técnica, usando ejemplos del sector.*»

El rol orienta perspectiva, vocabulario y audiencia de forma simultánea.

> Un rol nunca crea credenciales reales ni garantiza conocimiento factual. Debe ir siempre acompañado de instrucciones concretas sobre qué hacer y cómo hacerlo.

**Explicación**

Asignar un rol no es un truco: es una instrucción que orienta la perspectiva desde la que responde el modelo, y un rol pertinente mejora la coherencia del vocabulario, el enfoque analítico y la estructura. Sin rol, el modelo elige libremente nivel técnico, tono y enfoque, y la respuesta puede ser demasiado genérica. Con un rol y una **audiencia** («analista de retención de clientes… explica el churn a un equipo de ventas sin formación técnica, con ejemplos del sector»), perspectiva, vocabulario y audiencia quedan orientados a la vez.

Buena parte de la mejora procede también de la tarea, la audiencia y los ejemplos que acompañan al rol, no solo del título. Un rol nunca crea credenciales reales ni garantiza conocimiento factual: orienta la respuesta, pero lo que afirme sigue necesitando verificación.

---

## 1.2 Rol, persona, identidad y especialización

Estos cuatro conceptos se solapan con frecuencia en la práctica. Distinguirlos permite diseñar prompts más precisos y evitar instrucciones contradictorias o ambiguas.

| Concepto | Definición | Ejemplo ilustrativo |
|---|---|---|
| Rol | Función que el modelo desempeña en la tarea. | «Eres un analista de riesgos financieros.» |
| Persona | Rasgos comunicativos: tono, estilo, forma de expresarse. | «Responde de forma directa, sin eufemismos y con ejemplos breves.» |
| Especialización | Ámbito de práctica o dominio específico. | «Con especialización en mercados emergentes de renta fija.» |
| Identidad | No debe atribuirse falsamente a personas reales. | No uses «Eres el CFO de [empresa real]». |

La regla de oro: define función, no finjas autoridad. Un rol bien diseñado describe qué hace el asistente, no quién finge ser.

**Explicación**

Rol, persona, identidad y especialización se solapan en la práctica, pero conviene distinguirlos. El rol es la función que desempeña el modelo en la tarea («analista de riesgos financieros»). La persona son los rasgos comunicativos, tono y estilo («responde de forma directa, con ejemplos breves»). La especialización es el ámbito o dominio concreto. La identidad no debe atribuirse falsamente a personas reales, como «eres el CFO de una empresa real».

El rol responde a qué hace el asistente y la persona a cómo se expresa; pueden combinarse y especificarse por separado. La regla de oro es definir la función, no fingir autoridad: fingir ser una persona real o una autoridad certificada genera confusión sobre quién dice qué y expectativas de fiabilidad que el modelo no puede cumplir.

---

## 1.3 Cómo seleccionar un rol pertinente

El rol debe resolver una pregunta concreta: ¿qué perspectiva profesional aportaría más valor a esta tarea específica? No se trata de elegir un título impresionante, sino de seleccionar la función que genera la respuesta más útil para el lector.

1. **Identifica el problema real**: ¿Qué necesita entender o decidir el lector a partir de la respuesta?
2. **Selecciona la disciplina relevante**: Elige la función profesional cuyo enfoque es más útil para ese problema.
3. **Evita títulos ornamentales**: «*Experto de clase mundial*» no aporta perspectiva; «*auditor de procesos*» sí lo hace.
4. **Alinea rol con audiencia y resultado**: El rol del analista de riesgos es pertinente si el lector toma decisiones de inversión.

> Rol ornamental (ilustrativo): «*Eres un gurú visionario del futuro digital.*» — no orienta vocabulario ni enfoque.
>
> Rol funcional (ilustrativo): «*Eres un consultor de transformación digital especializado en pymes industriales.*»

**Explicación**

El rol debe resolver una pregunta concreta: qué perspectiva profesional aportaría más valor a esta tarea. Cuatro pasos guían la elección: identificar el problema real del lector, seleccionar la disciplina cuyo enfoque más ayude, evitar títulos ornamentales («experto de clase mundial» no aporta perspectiva; «auditor de procesos» sí) y alinear el rol con la audiencia y el resultado.

Un rol ornamental como «gurú visionario del futuro digital» no orienta vocabulario ni enfoque; uno funcional como «consultor de transformación digital especializado en pymes industriales» delimita disciplina, tipo de cliente y criterios. Una prueba de utilidad: si al quitar el título la respuesta no cambiaría, el título es decorativo. Un auditor busca controles y evidencias; un consultor comercial, oportunidades.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 05B · Un asistente con rol, límites y voz consistente](../../laboratorios/05B/README.md)
<!-- /labs-seccion -->

---

## 1.4 Definir responsabilidades del rol

Asignar un título no es suficiente. Para que el rol sea operativo, debes describir exactamente qué se espera que haga el asistente. Piensa en ello como redactar una descripción de puesto funcional, no una tarjeta de visita.

- **Responsabilidades concretas**: ¿Qué tareas específicas debe realizar? Analizar, sintetizar, redactar, revisar, priorizar…
- **Ámbito de actuación**: ¿Sobre qué materiales, datos o documentos trabaja? Define el alcance de la intervención.
- **Información que utilizará**: ¿Qué contexto, datos o restricciones le proporcionas tú? El modelo no puede inventar lo que no tiene.
- **Acciones permitidas**: ¿Puede proponer, recomendar, redactar, o solo analizar? Define el nivel de intervención.
- **Criterios de calidad**: ¿Cómo sabes que la respuesta es buena? Incluye indicadores como precisión, brevedad o cobertura.

**Explicación**

Un título no basta: hay que describir qué se espera que haga el asistente, como en una descripción de puesto. Incluye las responsabilidades concretas (analizar, sintetizar, redactar, revisar, priorizar), el ámbito de actuación (sobre qué materiales trabaja), la información que usará, las acciones permitidas (si solo analiza o también propone o redacta) y los criterios de calidad.

Es frecuente describir el rol y omitir los datos de que dispone: sin información suficiente, el asistente completa con supuestos. Conviene declarar qué información usará y qué hacer cuando falte. El nivel de intervención también importa: un asistente que solo debe analizar no debería recomendar, y uno que recomienda no debería decidir.

---

## 1.5 Definir límites del rol

Tan importante como decir qué hace el asistente es definir qué no debe hacer. Los límites protegen al usuario de respuestas que excedan el mandato, inventen información o tomen decisiones que corresponden a personas.

- **Qué puede analizar**: Solo la información proporcionada en el prompt o en el contexto de la conversación.
- **Qué no debe decidir**: Decisiones estratégicas, jurídicas o de personal que requieren responsabilidad humana.
- **Cuándo pedir aclaración**: Ante ambigüedad en el alcance, datos insuficientes o instrucciones contradictorias.
- **Cuándo escalar**: Cuando la solicitud supera el mandato o implica riesgos que el asistente no puede evaluar.

> **Fuentes permitidas**
>
> Datos y hechos: solo los aportados. El conocimiento general sirve para explicar, no para afirmar datos.

**Explicación**

Tan importante como lo que hace el asistente es lo que no debe hacer. Los límites protegen de respuestas que excedan el mandato, inventen información o tomen decisiones que corresponden a personas. Se definen qué puede analizar (solo la información aportada), qué no debe decidir (decisiones estratégicas, jurídicas o de personal), cuándo pedir aclaración, cuándo escalar y qué fuentes están permitidas.

La distinción sobre las fuentes es muy útil: el conocimiento general del modelo sirve para explicar un concepto, pero no para afirmar cifras o hechos del caso, que deben salir de los datos aportados. Un asistente puede explicar qué es un ratio de liquidez, pero el valor de una empresa solo puede salir de sus estados financieros. Y la escalada debe tener criterios: un asistente que nunca deriva a una persona, o lo hace sin criterio, es poco fiable.

---

[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-audiencia-tono-y-estilo.md)
