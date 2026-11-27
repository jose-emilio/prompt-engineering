[← Anterior](05-ejemplos-errores-y-proyecto-practico.md) · [Índice del módulo](README.md) · [Volver al inicio →](../../README.md)

# 6 · Anexos: chuleta, glosario y vigencia

*Módulo 13: Diseño de sistemas de prompts*

## 6.1 Chuleta del curso: plantilla de prompt

Una estructura reutilizable para empezar cualquier prompt: se usan solo los bloques que aporten valor y se revisa antes de enviar.

**Plantilla *(ilustrativa)***

```text
ROL: perspectiva relevante para la tarea
CONTEXTO: antecedentes, objetivo y audiencia
TAREA: verbo de acción + objeto + alcance
ENTRADA: datos delimitados, no instrucciones
RESTRICCIONES: límites, fuentes y ausencias
SALIDA: formato, estructura y longitud
CRITERIOS: condiciones observables de calidad
```

**Revisión antes de enviar**

- Objetivo: qué resultado o decisión se espera
- Datos: delimitados y sin información sensible
- Ausencias: qué hacer si falta un dato
- Formato: utilizable por quien lo recibe
- Verificación: criterios y revisión según el riesgo

**Explicación**

Esta chuleta reúne la estructura de prompt estudiada a lo largo del curso como lista de decisiones, no como formulario que rellenar entero. La plantilla tiene siete bloques: rol (perspectiva relevante), contexto (antecedentes, objetivo y audiencia), tarea (verbo de acción, objeto y alcance), entrada (datos delimitados, no instrucciones), restricciones (límites, fuentes y ausencias), salida (formato, estructura y longitud) y criterios (condiciones observables de calidad).

No hace falta usar todos los bloques: una tarea sencilla puede reducirse a tarea y salida, y una de riesgo, repetitiva o con datos sensibles se beneficia de casi todos; lo decide la proporción entre el esfuerzo de diseño y el riesgo. Cinco preguntas permiten revisar antes de enviar: qué resultado o decisión se espera, si los datos están delimitados y libres de información sensible, qué hacer si falta un dato, si el formato lo puede utilizar quien lo recibe y qué criterios y revisión corresponden al riesgo. Si alguna no tiene respuesta, el prompt probablemente no está listo.

---

## 6.2 Chuleta del curso: errores que se repiten

Los mismos errores aparecen en varios módulos; la tabla indica dónde se trabaja cada uno y qué control aplicar.

| Error que se repite | Dónde se trabaja | Control |
|---|---|---|
| Confiar en la fluidez | Módulos 01 y 08 | Verificar en una fuente primaria |
| Inventar lo que no consta | Módulos 02, 06 y 12 | «No consta» o null, con cita textual |
| Mezclar datos e instrucciones | Módulos 02 y 09 | Delimitadores y permisos mínimos |
| Cambiar varias variables a la vez | Módulos 07 y 10 | Una hipótesis, un cambio, una prueba |
| Aceptar sin ejecutar ni probar | Módulos 11 y 12 | Ejecutar, probar y comparar con el original |
| Automatizar sin supervisión | Módulos 08, 09 y 13 | Revisión humana proporcional al riesgo |

**Explicación**

Algunos errores se repiten en casi todos los módulos porque tienen causas comunes; la tabla indica dónde se trabaja cada uno y qué control aplicar. Confiar en la fluidez (módulos [01](../01-introduccion-a-los-llm/README.md) y [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md)) se corrige verificando en una fuente primaria. Inventar lo que no consta (02, 06 y 12) se corrige con «no consta» o null y cita textual. Mezclar datos e instrucciones (02 y 09) se corrige con delimitadores y permisos mínimos. Cambiar varias variables a la vez (07 y 10) se corrige con una hipótesis, un cambio y una prueba. Aceptar sin ejecutar ni probar (11 y 12) se corrige ejecutando, probando y comparando con el original. Y automatizar sin supervisión (08, 09 y 13) se corrige con revisión humana proporcional al riesgo.

Los seis comparten una raíz: dar por buena una salida sin una comprobación independiente, por lo que los seis controles son formas de verificar. La tabla puede usarse como lista de repaso al diseñar o revisar cualquier flujo con modelos de lenguaje.

---

## 6.3 Glosario (1/2)

Términos técnicos del curso, con una definición breve y el módulo donde se trabajan.

| Término | Definición | Módulo |
|---|---|---|
| Token | Unidad de texto que procesa el modelo | 01 |
| Ventana de contexto | Máximo de tokens por solicitud (entrada y salida) | 01 |
| Embedding | Representación vectorial de un texto | 01 |
| Few-shot | Instrucción con varios ejemplos en el prompt | 04 |
| Chain-of-Thought | Razonamiento paso a paso y verificable | 04 |
| RAG | Respuesta apoyada en fragmentos recuperados | 08 y 13 |

**Explicación**

El glosario recoge, en esta primera parte, términos técnicos que más se usan en el curso, con una definición breve y el módulo donde se trabajan. Un token es la unidad de texto que procesa el modelo, y la ventana de contexto el máximo de tokens por solicitud, contando entrada y salida (ambos en el módulo [01](../01-introduccion-a-los-llm/README.md)). Un embedding es la representación vectorial de un texto, donde la proximidad aproxima la similitud de significado. El few-shot incluye varios ejemplos en el prompt y el chain-of-thought plantea un razonamiento paso a paso verificable (módulo [04](../04-tecnicas-avanzadas-de-prompting/README.md)). El RAG apoya la respuesta en fragmentos recuperados de una base documental (módulos [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md) y 13).

Las definiciones son breves y sirven de ayuda de memoria, remitiendo al módulo donde se explican con detalle. Cuando un término tenga matices, como ocurre con «agente» o con «ventana de contexto efectiva», conviene acudir a la sección correspondiente o a la documentación del proveedor, porque algunos significados varían entre herramientas.

---

## 6.4 Glosario (2/2)

Términos técnicos del curso, con una definición breve y el módulo donde se trabajan.

| Término | Definición | Módulo |
|---|---|---|
| Temperature | Controla la variabilidad al elegir tokens | 06 |
| Top-p | Limita la selección a un núcleo de probabilidad | 06 |
| Alucinación | Afirmación plausible sin respaldo real | 08 |
| Inyección de prompts | Instrucción maliciosa en la entrada o en los datos | 09 |
| HITL | Revisión humana integrada en el flujo | 08 y 13 |
| MCP | Protocolo para conectar herramientas y datos | 11 y 13 |

**Explicación**

La segunda parte del glosario recoge los términos de parámetros, fiabilidad, seguridad e integración. La temperatura controla la variabilidad al elegir tokens y top-p limita la selección a un núcleo de probabilidad (módulo [06](../06-formato-de-salida-y-parametros/README.md)), con la salvedad de que su disponibilidad y efecto dependen del modelo y la plataforma. Una alucinación es una afirmación plausible sin respaldo real (módulo [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md)) y la inyección de prompts (prompt injection) es una instrucción maliciosa en la entrada o en los datos que busca alterar el comportamiento del sistema (módulo [09](../09-seguridad-privacidad-y-uso-responsable/README.md)). HITL, de human in the loop, es la revisión humana integrada en el flujo, en los puntos donde más control aporta (módulos [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md) y 13). MCP, el protocolo de contexto de modelos, es un estándar para conectar herramientas y datos con los asistentes (módulos [11](../11-desarrollo-de-software/README.md) y 13), siempre desde servidores de confianza.

El significado de algunos términos evoluciona con rapidez, sobre todo los de agentes, herramientas y protocolos, por lo que conviene contrastarlos con la documentación oficial al aplicarlos a un sistema real.

---

## 6.5 Qué caduca y cuándo revisarlo

Algunos contenidos del curso envejecen con rapidez; conviene revisarlos al cambiar de versión de modelo, de API o de normativa.

- **Modelos y capacidades**: Familias, ventanas de contexto y modalidades (anexo del módulo [01](../01-introduccion-a-los-llm/README.md)).
- **Parámetros y APIs**: Controles de generación, salidas estructuradas y MCP (módulos 06, 11 y 13).
- **Normativa**: RGPD, Reglamento de IA de la UE y su calendario (módulo [09](../09-seguridad-privacidad-y-uso-responsable/README.md)).
- **Seguridad**: Patrones de ataque y guías como el Top 10 de OWASP para LLM (módulo [09](../09-seguridad-privacidad-y-uso-responsable/README.md)).

> ⚠️ Última revisión del curso: noviembre de 2026. Anotar la fecha de cada nueva revisión y verificar siempre las fuentes oficiales.

**Explicación**

Una parte del contenido del curso envejece con rapidez, y este anexo identifica qué conviene revisar de forma deliberada. Cuatro familias caducan: los modelos y sus capacidades (familias, ventanas y modalidades del anexo del módulo [01](../01-introduccion-a-los-llm/README.md)), los parámetros y las APIs (controles de generación, salidas estructuradas y MCP, en los módulos 06, 11 y 13), la normativa (RGPD, Reglamento de IA de la UE y su calendario, módulo [09](../09-seguridad-privacidad-y-uso-responsable/README.md)) y la seguridad (patrones de ataque y guías como el Top 10 de OWASP para LLM).

La última revisión del curso corresponde a noviembre de 2026; se recomienda anotar la fecha de cada nueva revisión y verificar siempre las fuentes oficiales, en lugar de apoyarse en la memoria o en resúmenes de terceros. La revisión no tiene que ser exhaustiva cada vez: basta comprobar los elementos más sensibles cuando ocurre un hecho relevante, como la salida de un modelo nuevo, un cambio en una API usada como ejemplo o una modificación normativa.

---

[← Anterior](05-ejemplos-errores-y-proyecto-practico.md) · [Índice del módulo](README.md) · [Volver al inicio →](../../README.md)
