[← Anterior](02-razonamiento-y-descomposicion.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../05-roles-personas-y-comportamiento/README.md)

# 3 · Herramientas, revisión y selección de técnica

*Módulo 04: Técnicas avanzadas de prompting*

## 3.1 ReAct: razonamiento y acción combinados

ReAct (*Reasoning + Acting*) es un patrón conceptual en el que el modelo alterna entre generar razonamiento y ejecutar acciones sobre herramientas externas, incorporando las observaciones recibidas para decidir el siguiente paso.

- Combina planificación interna con acciones que devuelven observaciones reales.
- El flujo continúa o se ramifica según el resultado de cada herramienta.
- Requiere definir permisos explícitos y validación de argumentos antes de ejecutar.
- No está disponible en todas las plataformas ni modelos; verifica la documentación del proveedor.

**Ciclo ReAct (ilustrativo)**

1. **Razonar**: El modelo analiza la situación y decide qué herramienta invocar.
2. **Actuar**: Llama a la herramienta con argumentos validados.
3. **Observar**: Recibe el resultado y lo incorpora al contexto.
4. **Iterar o concluir**: Decide si necesita otra acción o si puede responder.

**ReAct** es un patrón conceptual. Su implementación concreta varía según la plataforma (function calling, tool use, etc.).

**Explicación**

ReAct (razonar y actuar) es un patrón en el que el modelo alterna razonamiento y acciones sobre herramientas externas, incorporando las observaciones recibidas para decidir el siguiente paso. El ciclo tiene cuatro pasos: razonar y decidir qué herramienta invocar, actuar llamándola con argumentos validados, observar el resultado e iterar o concluir. Requiere definir permisos explícitos y validar los argumentos antes de ejecutar, y no está disponible en todas las plataformas.

Ante la pregunta por el estado de un pedido, el modelo razona que debe consultar el sistema de pedidos, llama a la herramienta con el número, observa que está «en reparto» y responde. Su ventaja es que las respuestas se apoyan en datos reales; su riesgo, que cada acción tiene efectos externos, de ahí los controles de la sección siguiente.

---

## 3.2 Uso de herramientas: controles operativos imprescindibles

Integrar herramientas externas amplía las capacidades del modelo, pero introduce riesgos operativos significativos. Cada acción sobre un sistema externo debe estar explícitamente controlada.

- **Definir herramientas disponibles**: Lista explícita de herramientas permitidas; el modelo no debe invocar herramientas fuera de este inventario.
- **Mínimo privilegio**: Cada herramienta tiene solo los permisos estrictamente necesarios para su función.
- **Validar argumentos**: Verifica que los parámetros generados por el modelo son válidos antes de ejecutar la herramienta.
- **Separar lectura y escritura**: Nunca combines permisos de consulta y modificación en la misma herramienta.
- **Confirmar acciones sensibles**: Exige confirmación humana antes de acciones irreversibles o de alto impacto.
- **Registrar resultados**: Guarda un log de todas las llamadas a herramientas y sus resultados para auditoría.

**Explicación**

Integrar herramientas amplía las capacidades del modelo pero introduce riesgos operativos, por lo que cada acción sobre un sistema externo debe estar controlada. Los seis controles son: definir una lista cerrada de herramientas permitidas, aplicar el mínimo privilegio, validar los argumentos generados por el modelo antes de ejecutar, separar lectura y escritura, exigir confirmación humana antes de acciones irreversibles o de alto impacto y registrar todas las llamadas y sus resultados.

Cada control responde a un riesgo: el inventario cerrado evita llamadas imprevistas, el mínimo privilegio acota el alcance de un error o ataque, la validación de argumentos frena valores incorrectos o peligrosos, la separación de lectura y escritura evita que una consulta se convierta en modificación, la confirmación humana impide acciones irreversibles por un malentendido y el registro permite reconstruir lo ocurrido. Se aplican con independencia de lo inteligente que parezca el modelo y se amplían en el módulo [13](../13-diseno-de-sistemas-de-prompts/README.md).

---

## 3.3 Reflexion: revisión iterativa con rúbrica

El patrón Reflexion estructura la mejora de una respuesta en ciclos explícitos de crítica y revisión, en lugar de iterar por ensayo y error. Cada ciclo produce una versión mejor documentada y controlada.

- **Generar primera respuesta**: Producir un borrador inicial sin restricciones excesivas.
- **Evaluar contra rúbrica**: Aplicar una lista de criterios predefinidos: exactitud, formato, completitud, tono.
- **Revisar con cambios acotados**: Aplicar solo las correcciones identificadas; evitar reescrituras completas innecesarias.
- **Identificar defectos concretos**: No «*mejorar en general*»: señalar qué falla y por qué.

> Define un criterio de parada claro (p. ej. 0 defectos en la rúbrica o máximo 3 ciclos) para evitar iteraciones infinitas.

**Explicación**

El patrón **Reflexion** estructura la mejora de una respuesta en ciclos de crítica y revisión, en lugar de iterar por ensayo y error. Se genera un primer borrador, se evalúa contra una rúbrica (exactitud, formato, completitud, tono), se identifican defectos concretos (no «mejorar en general») y se revisa con cambios acotados, sin reescrituras completas innecesarias.

Frente a pedir «mejóralo» repetidamente, que produce cambios imprevisibles, la rúbrica y los defectos concretos hacen que cada ciclo corrija algo identificado y conserve el resto. Hace falta un criterio de parada claro (por ejemplo, cero defectos o un máximo de tres ciclos). Y si critica el mismo modelo que generó el texto, comparte sus sesgos: para tareas de riesgo conviene complementar con una verificación externa.

---

## 3.4 Elegir la técnica según el problema

No existe una técnica universalmente superior. La elección debe partir de la naturaleza del problema, la complejidad de la tarea y las restricciones operativas del entorno.

| Perfil del problema | Técnica recomendada | Consideración clave |
|---|---|---|
| Tarea simple y clara | Zero-shot | Verifica consistencia con un conjunto de prueba. |
| Patrón o formato específico | One-shot / Few-shot | Cura los ejemplos; evita sesgos. |
| Problema multietapa | CoT / Descomposición | Valida cada etapa independientemente. |
| Múltiples candidatos útiles | Self-Consistency | Solo cuando el coste extra está justificado. |
| Acceso a sistemas externos | ReAct + controles | Mínimo privilegio y validación de argumentos. |

**Explicación**

No existe una técnica universalmente superior; la elección parte del problema, de la complejidad y de las restricciones operativas. Una tarea simple y clara pide zero-shot; un patrón o formato específico, one-shot o few-shot con ejemplos curados; un problema multietapa, CoT o descomposición con validación por etapa; cuando hay varios candidatos útiles, self-consistency si el coste extra se justifica; y el acceso a sistemas externos, ReAct con controles de mínimo privilegio y validación de argumentos.

La disciplina es empezar por la técnica más sencilla que pueda resolver el problema y escalar solo cuando la evidencia lo justifique, porque cada paso añade coste y complejidad. Las técnicas pueden combinarse, pero siempre por una necesidad concreta. El criterio final es empírico: si una técnica sencilla alcanza la calidad requerida con consistencia, no hay motivo para sustituirla por otra más compleja.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 04B · Razonamiento paso a paso y autoconsistencia](../../laboratorios/04B/README.md)
<!-- /labs-seccion -->

---

## 3.5 Errores frecuentes al aplicar técnicas avanzadas

Conocer los fallos más comunes permite evitarlos proactivamente. La siguiente tabla recoge los errores habituales, su manifestación y la mitigación recomendada.

| Técnica | Error frecuente | Mitigación |
|---|---|---|
| Few-shot | Ejemplos incorrectos o sesgados propagan errores a todas las salidas. | Revisar y validar cada ejemplo antes de incluirlo. |
| Chain-of-Thought | Cadena de razonamiento larga aceptada sin verificar el resultado final. | Verificar siempre el resultado final de forma independiente. |
| Self-Consistency | Consenso entre candidatos interpretado como garantía de verdad. | Complementar con comprobación externa; el consenso no corrige errores sistemáticos. |
| Descomposición | Exceso de subtareas que duplican contexto y aumentan el coste sin mejora medible. | Medir el impacto de cada etapa adicional antes de añadirla. |
| Herramientas | Permisos amplios que permiten acciones no previstas o irreversibles. | Aplicar mínimo privilegio y confirmar acciones sensibles. |

**Explicación**

Conocer los fallos habituales permite evitarlos. En few-shot, los ejemplos incorrectos o sesgados propagan errores: hay que revisar cada ejemplo. En chain-of-thought, una cadena larga puede aceptarse sin verificar el resultado final: hay que verificarlo siempre de forma independiente. En self-consistency, el consenso se interpreta como garantía de verdad: hay que complementar con comprobación externa. En descomposición, un exceso de subtareas duplica contexto y coste sin mejora: hay que medir el impacto de cada etapa añadida. Con herramientas, los permisos amplios permiten acciones no previstas o irreversibles: mínimo privilegio y confirmación de acciones sensibles.

En los cinco casos la técnica produce una apariencia de fiabilidad que no equivale a fiabilidad real, y la mitigación consiste en comprobar con un criterio externo o limitar el alcance de la técnica.

---

## 3.6 Caso comparativo integrado: clasificación con casos ambiguos

Aplicar las tres técnicas principales al mismo problema permite cuantificar su impacto relativo. El caso: clasificación de solicitudes de soporte con un 20% de casos ambiguos que no encajan claramente en ninguna categoría.

**01. Baseline Zero-shot**

Instrucción directa con categorías definidas. Medir exactitud y tasa de «Otro» en el conjunto de evaluación.

**Métricas a registrar**

- Exactitud global (% correcto)
- Tasa de errores por categoría
- Cumplimiento de formato
- Tokens consumidos por clasificación
- Variabilidad entre ejecuciones

1. **Añadir Few-shot**: Incluir 4-5 ejemplos cubriendo los casos ambiguos detectados en el paso anterior. Volver a medir con las mismas entradas.
2. **Aplicar descomposición**: Separar en dos prompts: extracción de señales clave → clasificación. Comparar con los pasos anteriores.
3. **Evaluar calidad, coste y consistencia**: Usar las mismas entradas de prueba en los tres enfoques. Documentar errores por categoría.

**Explicación**

El caso aplica las tres técnicas principales al mismo problema para cuantificar su impacto: clasificar solicitudes de soporte cuando un 20 % son ambiguas. Se mide primero la línea base zero-shot (exactitud y tasa de «Otro»); se añaden después cuatro o cinco ejemplos que cubren los casos ambiguos y se vuelve a medir con las mismas entradas; se prueba la descomposición en dos prompts (extraer señales clave y luego clasificar); y se comparan calidad, coste y consistencia, documentando los errores por categoría.

Las métricas son la exactitud global, los errores por categoría, el cumplimiento del formato, los tokens por clasificación y la variabilidad entre ejecuciones. El valor del caso está en el método: cada técnica se evalúa con los mismos datos, y la decisión depende de qué pese más (por ejemplo, el few-shot puede mejorar la exactitud a costa de más tokens). A menudo los casos ambiguos se benefician mucho de los ejemplos mientras que los claros ya funcionaban sin ellos.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 04A · Zero-shot, one-shot y few-shot: cuántos ejemplos hacen falta](../../laboratorios/04A/README.md)
<!-- /labs-seccion -->

---

## 3.7 Mapa resumen: técnicas avanzadas de prompting

Todas las técnicas del módulo comparten un principio común: la validación del resultado final siempre es necesaria, independientemente de la técnica empleada.

- **Zero-shot**: Instrucción directa, sin ejemplos. Rápido y compacto. Verifica consistencia con un conjunto de prueba representativo.
- **Few-shot**: Patrón por ejemplos curados. Mayor control sobre el formato y las reglas específicas de la tarea.
- **CoT y descomposición**: Etapas verificables. Especialmente útil para tareas multietapa donde los errores en cadena son un riesgo.
- **Self-Consistency**: Comparar múltiples candidatos. Solo cuando el problema tiene respuesta verificable y el coste extra está justificado.
- **ReAct + herramientas**: Interacción con sistemas externos. Requiere controles estrictos de permisos, validación y registro de acciones.
- **Validación siempre**: Ninguna técnica garantiza exactitud por sí sola. La verificación independiente es siempre el último paso.

**Explicación**

Todas las técnicas del módulo comparten un principio: el resultado final siempre debe validarse. Zero-shot es la instrucción directa, rápida y compacta; few-shot aporta patrones por ejemplos curados y más control sobre el formato; CoT y descomposición dan etapas verificables en tareas multietapa; self-consistency compara candidatos cuando el problema es verificable y el coste lo justifica; ReAct con herramientas permite interactuar con sistemas externos con controles estrictos de permisos, validación y registro.

Puede verse como una escalera que solo se asciende cuando el escalón inferior no resuelve el problema, y cada escalón se paga con coste, latencia o riesgo. Las técnicas no se excluyen: un sistema real combina ejemplos, descomposición, razonamiento estructurado y herramientas con controles. El módulo [05](../05-roles-personas-y-comportamiento/README.md) sigue con roles, personas y estilo, y el 06 con formatos estructurados y parámetros.

---

## 3.8 Comprobación de comprensión

Piensa cada respuesta, de forma oral o por escrito, antes de ver las respuestas orientativas, que aparecen a continuación.

**1. ¿Cuándo basta Zero-shot?**

**2. ¿Qué hace útil un ejemplo?**

**3. ¿Qué no garantiza el consenso?**

**4. ¿Cómo validar etapas?**

**5. ¿Qué controles exige una herramienta?**

---

## 3.9 Comprobación de comprensión: respuestas

Contrasta tus respuestas con estas. Son orientativas: lo importante es que cubran las ideas clave del módulo.

1. **¿Cuándo basta Zero-shot?** Cuando la tarea es clara y de propósito general, y una prueba con un conjunto representativo muestra resultados consistentes sin ejemplos.
2. **¿Qué hace útil un ejemplo?** Que sea correcto, representativo, con el formato exacto esperado, etiquetas consistentes y bien delimitado; si no, puede empeorar el resultado.
3. **¿Qué no garantiza el consenso?** La verdad: un error sistemático puede repetirse en todos los candidatos, así que hace falta una comprobación externa.
4. **¿Cómo validar etapas?** Definir la salida de cada etapa, revisar el resultado parcial con criterios explícitos y no pasar a la siguiente hasta aprobarlo.
5. **¿Qué controles exige una herramienta?** Inventario explícito de herramientas, mínimo privilegio, validación de argumentos, separar lectura y escritura, confirmación humana en acciones sensibles y registro.

**Explicación**

La comprobación de comprensión repasa cinco ideas. El zero-shot basta cuando la tarea es clara y general y una prueba con un conjunto representativo muestra resultados consistentes. Un ejemplo es útil si es correcto, representativo, con el formato exacto, etiquetas consistentes y bien delimitado; si no, puede empeorar el resultado. El consenso no garantiza la verdad, porque un error sistemático puede repetirse en todos los candidatos y hace falta una comprobación externa. Las etapas se validan definiendo la salida de cada una, revisándola con criterios explícitos y no pasando a la siguiente hasta aprobarla. Y una herramienta exige inventario explícito, mínimo privilegio, validación de argumentos, separación de lectura y escritura, confirmación humana en acciones sensibles y registro.

El hilo común de las cinco respuestas es la prudencia metodológica:

- elegir lo más sencillo que funcione
- medir con las mismas entradas
- comprobar con un criterio externo
- limitar lo que el modelo puede hacer

---

[← Anterior](02-razonamiento-y-descomposicion.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../05-roles-personas-y-comportamiento/README.md)
