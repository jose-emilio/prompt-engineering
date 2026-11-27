[← Anterior](02-creatividad-y-resolucion-de-problemas.md) · [Índice del módulo](README.md) · [Siguiente →](04-seleccion-caso-integrado-y-sintesis.md)

# 3 · Simulación y combinación de funciones

*Módulo 03: Tipos funcionales de prompts*

## 3.1 Prompts de simulación y role-playing

Los prompts de simulación asignan al modelo un rol y un escenario para que interactúe como si fuera un personaje o sistema. Son especialmente útiles para preparar conversaciones difíciles, entrenar habilidades o explorar reacciones ante distintos comportamientos.

- **Rol del modelo**: Definir con precisión quién es el modelo: cliente, evaluador, experto, usuario hostil.
- **Escenario y objetivo**: Describir la situación de partida y qué debe lograrse al final de la interacción.
- **Reglas de interacción**: Indicar turnos, restricciones de comportamiento y hasta dónde puede "ceder" el personaje.
- **Nivel de dificultad**: Ajustar la resistencia del personaje según el nivel de entrenamiento deseado.
- **Feedback al finalizar**: Pedir al modelo que salga del rol y evalúe la interacción con criterios definidos.

> Ejemplo ilustrativo: «*Actúa como cliente exigente durante una entrevista de descubrimiento. Tienes dudas sobre el ROI y tiendes a desconfiar de las estimaciones. Mantén el rol hasta que yo te pida el feedback.*»

**Explicación**

Los prompts de simulación asignan al modelo un rol y un escenario para que interactúe como un personaje o sistema, y sirven para preparar conversaciones difíciles, entrenar habilidades o explorar reacciones. Hay que definir el rol, el escenario y el objetivo, las reglas de interacción, el nivel de dificultad y el feedback final, para el que el modelo sale del rol y evalúa con criterios definidos.

El ejemplo plantea un cliente exigente en una entrevista de descubrimiento, con dudas sobre el retorno de la inversión, que mantiene el rol hasta que se pida el feedback. Hay dos precauciones: la simulación sirve para practicar, no para obtener hechos, porque el personaje puede inventar respuestas coherentes con el rol pero incorrectas; y el feedback debe basarse en criterios definidos de antemano.

---

## 3.2 Role-playing educativo

El role-playing educativo diseña simulaciones orientadas a practicar una competencia concreta. A diferencia de la simulación libre, el escenario educativo tiene fases definidas, criterios de avance y feedback estructurado basado en rúbrica.

1. **Competencia a practicar**: Definir la habilidad objetivo: negociación, comunicación asertiva, resolución de conflictos.
2. **Escenario y personaje**: Crear un personaje consistente que no rompa el rol salvo instrucción explícita.
3. **Fases y reglas de avance**: Establecer cuándo avanza el escenario y qué acciones del participante lo desbloquean.
4. **Respuestas condicionadas**: El personaje reacciona de forma distinta según las decisiones tomadas, reforzando el aprendizaje.
5. **Feedback basado en criterios**: Al finalizar, el modelo evalúa la interacción con una rúbrica: qué funcionó, qué mejorar y por qué.

> Ejemplo ilustrativo: «*Practica una conversación de resolución de conflicto entre dos compañeros. Cuando yo haya respondido tres veces, sal del rol y dame feedback según los criterios de escucha activa y asertividad.*»

**Explicación**

El **role-playing** educativo diseña simulaciones para practicar una competencia concreta, con fases definidas, criterios de avance y feedback estructurado con rúbrica. Los pasos son: definir la competencia (negociación, asertividad, resolución de conflictos), crear un personaje consistente que no rompa el rol, establecer fases y reglas de avance, hacer que el personaje reaccione según las decisiones tomadas y evaluar al final con una rúbrica.

En el ejemplo, tras tres respuestas, el modelo sale del rol y da feedback según criterios de escucha activa y asertividad. La diferencia con la simulación libre es la intención pedagógica: por eso importan la rúbrica y la separación nítida entre el modo personaje y el modo evaluador; mezclarlos contamina el feedback.

---

## 3.3 Combinar funciones en un mismo flujo

Muchas tareas profesionales requieren más de un tipo funcional de prompt. La combinación eficaz ordena las operaciones en secuencia lógica, define la salida de cada etapa y valida la coherencia antes de pasar a la siguiente.

![Camino de cuatro etapas para combinar funciones: 1 extracción, obtener hechos del documento fuente; 2 clasificación, asignar cada hecho a una categoría de prioridad; 3 síntesis, condensar los hechos clasificados en un resumen ejecutivo; 4 generación, redactar un borrador de respuesta basado en la síntesis.](img/d26-1.jpg)

**Reglas para combinar bien**

- Identificar todas las funciones necesarias antes de escribir el prompt
- No mezclar extracción y generación creativa en una misma etapa; sepáralas como en el ejemplo
- Definir el formato de salida de cada etapa explícitamente
- Validar cada resultado parcial antes de usarlo como entrada siguiente

Ejemplo ilustrativo: «*Lee la reclamación adjunta. Paso 1: extrae los hechos. Paso 2: clasifica la prioridad de cada hecho (Alta/Media/Baja). Paso 3: sintetízalos en un resumen ejecutivo. Paso 4: redacta una respuesta al cliente de máximo 150 palabras.*»

**Explicación**

Muchas tareas profesionales requieren varios tipos de prompt. La combinación eficaz ordena las operaciones en una secuencia lógica, define la salida de cada etapa y valida antes de continuar. El camino del ejemplo es extracción de hechos, clasificación por prioridad, síntesis en resumen ejecutivo y generación de un borrador de respuesta.

Las reglas son: identificar todas las funciones necesarias antes de escribir, no mezclar extracción y **generación creativa** en la misma etapa (sus criterios de calidad son opuestos), definir el formato de cada etapa y validar los resultados parciales. El ejemplo reúne los cuatro pasos en un solo prompt por claridad didáctica, pero en uso profesional es preferible encadenarlos para poder revisar cada salida. Lo exacto debe ir antes que lo creativo.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 03A · Catálogo de prompts por tipo funcional](../../laboratorios/03A/README.md) · [Laboratorio 03B · Una misma tarea, tres tipos de prompt](../../laboratorios/03B/README.md)
<!-- /labs-seccion -->

---

## 3.4 Elegir el tipo de prompt correcto

Aplicar los criterios de selección adecuados evita el error más frecuente en prompt engineering: usar un tipo funcional que no corresponde a la operación real que necesita ejecutarse. Este árbol de decisión simplifica la elección.

![Árbol de decisión que asigna el tipo de prompt según la pregunta: ¿recuperar la respuesta de una fuente? Q&A basado en contexto; ¿transformar texto existente? transformación o reformulación; ¿generar alternativas nuevas? creatividad o brainstorming; ¿clasificar o extraer campos? clasificación o extracción; ¿resolver o comparar opciones? resolución de problemas o comparación; ¿simular una interacción? role-playing o simulación.](img/d27-1.jpg)

> Ejercicio ilustrativo: Asigna el tipo de prompt a cinco tareas profesionales reales en tu día a día.

**Explicación**

Elegir el tipo de prompt correcto evita el error más frecuente: usar un tipo que no corresponde a la operación real. El árbol plantea seis preguntas: ¿recuperar la respuesta de una fuente? (Q&A basado en contexto); ¿transformar texto existente? (**transformación**); ¿generar alternativas? (creatividad); ¿clasificar o extraer campos? (clasificación o extracción); ¿resolver o comparar opciones? (resolución o comparación); ¿simular una interacción? (role-playing).

Si dos preguntas parecen aplicables, la tarea probablemente es compuesta y conviene descomponerla en etapas. El ejercicio sugerido, asignar tipo a cinco tareas reales del trabajo propio, suele revelar que muchas tareas aparentemente simples combinan varias operaciones: preparar la respuesta a una reclamación reúne extracción, clasificación, síntesis y generación.

---

[← Anterior](02-creatividad-y-resolucion-de-problemas.md) · [Índice del módulo](README.md) · [Siguiente →](04-seleccion-caso-integrado-y-sintesis.md)
