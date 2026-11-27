[← Laboratorios](../README.md) · [Módulo 03](../../modulos/03-tipos-funcionales-de-prompts/README.md) · [← 02B](../02B/README.md) · [03B →](../03B/README.md)

# Laboratorio 03A · Catálogo de prompts por tipo funcional

Módulo 03 · Tipos funcionales de prompts · Duración estimada: 50 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Construir un catálogo de prompts de cinco tipos funcionales sobre un mismo documento y reescribir los que peor funcionan. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Leer el documento y apuntar los hechos clave (5 min)
- Paso 2 · Preparar las fichas de los prompts (12 min)
- Paso 3 · Ejecutar y valorar los prompts (24 min)
- Paso 4 · Reescribir los dos peores (9 min)

<details>
<summary>Secciones del módulo relacionadas (11)</summary>

- [§1.1 Cómo clasificar un prompt](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#11-cómo-clasificar-un-prompt)
- [§1.2 Prompts de instrucción directa](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#12-prompts-de-instrucción-directa)
- [§1.5 Q&A basado en contexto](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#15-qa-basado-en-contexto)
- [§1.7 Prompts de transformación](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#17-prompts-de-transformación)
- [§1.8 Prompts de resumen y síntesis](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#18-prompts-de-resumen-y-síntesis)
- [§1.9 Prompts de extracción](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#19-prompts-de-extracción)
- [§1.10 Prompts de clasificación](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#110-prompts-de-clasificación)
- [§2.7 Prompts de comparación](../../modulos/03-tipos-funcionales-de-prompts/02-creatividad-y-resolucion-de-problemas.md#27-prompts-de-comparación)
- [§2.8 Prompts de planificación](../../modulos/03-tipos-funcionales-de-prompts/02-creatividad-y-resolucion-de-problemas.md#28-prompts-de-planificación)
- [§3.4 Elegir el tipo de prompt correcto](../../modulos/03-tipos-funcionales-de-prompts/03-simulacion-y-combinacion-de-funciones.md#34-elegir-el-tipo-de-prompt-correcto)
- [§4.5 Diseño de salidas para cada función](../../modulos/03-tipos-funcionales-de-prompts/04-seleccion-caso-integrado-y-sintesis.md#45-diseño-de-salidas-para-cada-función)

</details>

## Justificación del laboratorio

La circular interna CI-2026-014 de Altanoria cambia el criterio de prioridad de las incidencias de los conectores. La directora de Soporte quiere que los equipos la aprovechen de muchas maneras: quien consulta una duda, quien la resume para su equipo, quien extrae las reglas para una herramienta o quien clasifica incidencias con ellas. Cada una de esas necesidades es un tipo de prompt distinto.

Un error muy común es usar siempre el mismo tipo de prompt para todo («resúmeme esto», «explícame esto»). El tipo de prompt determina qué tipo de salida se obtiene y también qué tipo de fallo hay que vigilar: un resumen puede omitir lo importante, una extracción puede inventar un dato que no consta, una clasificación puede equivocarse con un caso límite y una simulación puede salirse del guion.

Este laboratorio construye el catálogo de prompts reutilizables que pide la directora: uno por tipo funcional, aplicados todos al mismo documento. Al probarlos se verá con datos propios que el tipo decide el resultado y el fallo, y se aprenderá a elegir el adecuado para cada necesidad.

## Objetivos

Construir un catálogo de diez prompts, uno por tipo funcional, aplicados a un mismo documento (una circular interna de Altanoria). Se comprobará que el tipo de prompt determina el tipo de salida y el tipo de fallo, y se aprenderá a elegir el tipo adecuado para cada necesidad.

Al terminar el laboratorio se habrá conseguido:

- Identificar el tipo funcional de una necesidad (pregunta, transformación, resumen, extracción, clasificación, comparación, planificación…).
- Diseñar la entrada, la salida esperada y el criterio de calidad de cada tipo.
- Reconocer el fallo característico de cada tipo (por ejemplo, resumen que omite lo importante; extracción que inventa; clasificación fuera de las categorías).
- Diseñar la salida pensando en quién la va a usar.

Conceptos que se usan:

- **Tipo funcional**. Clasificación de los prompts según lo que se pide hacer con la información: responder, transformar, condensar, extraer, clasificar, generar, comparar, planificar, simular… Cada tipo tiene un diseño típico, una salida característica y errores propios ([§1.1 Cómo clasificar un prompt](../../modulos/03-tipos-funcionales-de-prompts/01-clasificacion-instruccion-y-transformacion.md#11-cómo-clasificar-un-prompt)).
- **Informativo, generativo y evaluativo** ([§4.3 Prompts informativos frente a generativos](../../modulos/03-tipos-funcionales-de-prompts/04-seleccion-caso-integrado-y-sintesis.md#43-prompts-informativos-frente-a-generativos) y [§4.4 Prompts evaluativos](../../modulos/03-tipos-funcionales-de-prompts/04-seleccion-caso-integrado-y-sintesis.md#44-prompts-evaluativos)). Un prompt informativo busca hechos de una fuente; uno generativo crea contenido nuevo; uno evaluativo juzga algo con criterios. Cada uno requiere controles distintos.
- **Salida diseñada para el consumidor** ([§4.5 Diseño de salidas para cada función](../../modulos/03-tipos-funcionales-de-prompts/04-seleccion-caso-integrado-y-sintesis.md#45-diseño-de-salidas-para-cada-función)). La misma información se presenta distinto si la leerá una persona o la consumirá un programa.

## Recursos necesarios

- Un asistente de chat cualquiera.
- Documento de trabajo: [`datos/circular_interna.md`](datos/circular_interna.md), la circular CI-2026-014 sobre prioridades de incidencias de conectores.
- Documentos auxiliares de Altanoria en [`../comun/empresa/`](../comun/empresa/sla.md) (en particular `sla.md`).
- Hoja de cálculo: [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), con los hechos clave, las fichas de los cinco prompts con sus comprobaciones y la reescritura de los dos peores.

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: La Espiga publica un aviso para sus clientes y quiere comprobar cinco usos del asistente con él.

Aviso de ejemplo: «Del 22 al 31 de diciembre abrimos de 7:00 a 14:00. Los pedidos de roscón se cierran el 20 de diciembre a las 20:00. Los pedidos por WhatsApp se confirman en un máximo de 2 horas laborables. No se admiten cambios en las 24 horas anteriores a la entrega.»

Paso 1: los hechos clave. Se leen y se localizan en el texto: horario (7:00 a 14:00), fecha de cierre del roscón (20 de diciembre, 20:00), confirmación (2 horas laborables) y plazo para cambios (24 horas antes). Cuatro hechos, todos localizados.

Pasos 2 y 3: las fichas. Se ejecuta un prompt de cada tipo y se contestan tres comprobaciones de sí o no por respuesta, junto con el fallo observado.

| Tipo | Petición | Cumple el tipo | Fidelidad | Utilizable | Cumplidas | Fallo |
|---|---|---|---|---|---|---|
| Pregunta-respuesta | ¿Hasta cuándo puedo pedir un roscón? | sí | sí | sí | 3 | ninguno |
| Transformación | Pasa el horario a una tabla | sí | sí | sí | 3 | ninguno |
| Resumen | Resume el aviso en 30 palabras | no | sí | no | 1 | se pasa de longitud (58 palabras) |
| Extracción | Devuelve los plazos en JSON | sí | no | sí | 2 | inventa un dato («domingos cerrado») |
| Clasificación | ¿Qué tipo de aviso es? | sí | sí | sí | 3 | ninguno |

Paso 4: reescribir los dos peores, que son el resumen (1) y la extracción (2).

| Ficha | Causa | Línea que se añade | Antes | Después |
|---|---|---|---|---|
| Resumen | se pasa de longitud | «Máximo 30 palabras.» | 1 | 3 |
| Extracción | inventa un dato | «Si un dato no consta, escribe null.» | 2 | 3 |

Cada reescritura corrige una causa con una sola línea, y se repite la prueba en una conversación nueva.

Qué se espera ver en tu laboratorio: los hechos de la circular de Altanoria, una ficha por tipo con sus comprobaciones y los dos peores con su reescritura.

## Pasos de ejecución

El laboratorio es de chat y se hace en orden. La regla de oro: cada prompt se prueba en una conversación nueva, con la circular pegada en el mensaje, para que el asistente no use lo que ya sabe de pruebas anteriores.

### Paso 1 · Leer el documento y apuntar los hechos clave (5 minutos)
1. Abrir [`datos/circular_interna.md`](datos/circular_interna.md) y leerla entera, sin ayuda de IA.
2. En la pestaña «Hechos clave» de la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) están los diez hechos verificables de la circular (fechas, porcentajes, plazos, responsables y reglas de prioridad). Localizar cada uno en el texto y marcar «sí» en la columna «¿Localizado en la circular?».
3. Dejar a mano la circular copiada (Ctrl+A y Ctrl+C sobre el texto del fichero) para pegarla en los pasos siguientes.

Comprobación: la pestaña «Hechos clave» cuenta los diez hechos localizados. Servirán para comprobar las respuestas.

### Paso 2 · Preparar las fichas de los prompts (12 minutos)
El catálogo tiene diez tipos. En esta versión se ejecutan cinco (los tipos 2, 4, 5, 6 y 7) y los otros cinco se dejan como ampliación.

1. Abrir la pestaña «Fichas» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx). Tiene una fila por cada uno de los cinco tipos que se ejecutan, con su necesidad y su prompt ya cargados:
   - Tipo 2, pregunta-respuesta basada en contexto: «¿Quién puede bajar la prioridad de una incidencia de conector?».
   - Tipo 4, transformación: pasar la sección 2 (criterio de prioridad) a una tabla.
   - Tipo 5, resumen: resumen para la dirección en 60 palabras.
   - Tipo 6, extracción: extraer a JSON la vigencia, los plazos de aviso y la frecuencia de información al cliente por prioridad.
   - Tipo 7, clasificación: clasificar una incidencia de ejemplo en P1 a P4 según la circular.
2. Escribir en el documento de texto, antes de ejecutar nada, la salida esperada y el criterio de calidad de los tipos 2, 4, 6 y 7. El tipo 5 está resuelto más abajo como modelo.

Un criterio de calidad es verificable cuando se puede comprobar con un sí o un no, sin interpretar. Se escribe con tres partes:
   - Forma: el formato y la longitud que debe tener la salida.
   - Contenido obligatorio: los datos de la circular que deben aparecer (los hechos del Paso 1).
   - Lo prohibido: lo que no puede aparecer ni inventarse.

Ejemplo resuelto, para el tipo 5 (resumen):
   - Salida esperada: un párrafo de 60 palabras como máximo con el cambio (el nuevo criterio de prioridad de las incidencias de conectores), el motivo (41 incidencias en el tercer trimestre, el 37 % reclasificadas) y la fecha de entrada en vigor (3 de noviembre de 2026).
   - Criterio de calidad: se cumple si (1) tiene 60 palabras o menos; (2) incluye la fecha 3 de noviembre de 2026 y el motivo con sus dos cifras (41 y 37 %); (3) no contiene opiniones ni ningún dato que no esté en la circular.

Un criterio como «que el resumen sea bueno» no vale: no se puede comprobar. Si al escribirlo no se puede responder sí o no, hay que concretarlo.

3. Leer los diez prompts de partida de abajo, que sirven como punto de partida o para comparar con los que se escriban.

Prompts de los diez tipos:

```text
1 Instrucción directa:
Redacta un aviso de tres líneas para el canal interno que anuncie el cambio de criterio de prioridad de conectores a partir del 3 de noviembre. Tono claro y directo. Usa solo la información de la circular.

2 Pregunta-respuesta con contexto:
Responde usando solo la circular. Si no está, di «no consta». Pregunta: ¿Quién puede bajar la prioridad de una incidencia de conector?

3 Completado:
Completa la frase manteniendo el sentido de la circular: «El agente de primera línea puede subir la prioridad, pero…»

4 Transformación:
Convierte la sección 2 en una tabla con las columnas Prioridad, Condición y Observaciones. No cambies ningún dato.

5 Resumen:
Resume en 60 palabras para la dirección: cambio, motivo y fecha. Sin opiniones.

6 Extracción:
Extrae a JSON {vigencia, aviso_interno_minutos, info_cliente_horas: {P1, P2}, causa_raiz_dias_habiles}. Si un dato no consta, usa null.

7 Clasificación:
Clasifica la incidencia en P1, P2, P3 o P4 según la circular y justifica con la regla aplicada. Incidencia: «Desde hace 8 horas el conector de SharePoint no sincroniza y hay 120 documentos pendientes».

8 Comparación:
Compara los tiempos de información al cliente de P1 y P2 en una tabla de tres columnas: Aspecto, P1, P2.

9 Planificación:
Plan de implantación en tres semanas con acciones, responsables (solo los que aparezcan en la circular) y entregables.

10 Simulación:
Actúa como un agente nuevo y hazme preguntas sobre la circular, de una en una. Cuando responda, indica si mi respuesta es coherente con la circular.

(En todos los casos, anteponer: «<circular> … </circular>»)
```

Comprobación: el documento tiene la salida esperada y el criterio de calidad de los cuatro tipos, y cada criterio se puede comprobar con un sí o un no.

### Paso 3 · Ejecutar y valorar los prompts (24 minutos)
Para cada uno de los cinco prompts:

1. Abrir una conversación nueva en el asistente.
2. Pegar el contenido completo de la circular y, justo debajo, el prompt del tipo. Enviar.
3. Comprobar la respuesta contra los hechos de la pestaña «Hechos clave».
4. En la pestaña «Fichas», contestar sí o no a las tres comprobaciones de esa respuesta (la pestaña «Comprobaciones» dice cuándo se contesta «sí»):
   - Cumple el tipo: ¿hace lo que ese tipo pide, en la forma indicada?
   - Fidelidad: ¿todo lo que dice está en la circular y coincide con los hechos?
   - Utilizable: ¿se puede usar sin retocar?
5. Elegir en la columna «Fallo observado» qué ha fallado, o «ninguno» si no ha fallado nada. La hoja suma las comprobaciones cumplidas.

Comprobación: las cinco fichas tienen sus tres comprobaciones contestadas, el total y el fallo observado.

### Paso 4 · Reescribir los dos peores (9 minutos)
1. Elegir las dos fichas con menos comprobaciones cumplidas: la hoja las marca con «Reescribir» en la última columna de «Fichas».
2. En la pestaña «Reescritura», elegir la ficha y la causa del problema entre las de la lista (por ejemplo, «inventa un dato» si la extracción no decía qué hacer cuando un dato no consta y el asistente inventó un plazo).
3. Reescribir el prompt añadiendo la línea que corrige esa causa, ejecutarlo en una conversación nueva con la circular y comprobar si mejora. Contestar de nuevo las tres comprobaciones y anotar cuántas se cumplen ahora (de 0 a 3); la hoja calcula la mejora. El prompt reescrito se queda en el chat. Líneas correctoras habituales, según la causa:

| Causa del fallo | Línea que se puede añadir |
|---|---|
| Inventa un dato que no está | «Usa solo la circular. Si un dato no consta, escribe `no consta` (o `null` en JSON).» |
| El formato no es el pedido | «Responde únicamente con [formato], sin texto antes ni después.» |
| Se pasa de longitud | «Máximo [N] palabras.» |
| Mezcla varias cosas | «Responde solo a [lo que se pide]; no añadas nada más.» |
| Cambia o redondea una cifra | «Copia las cifras literalmente de la circular.» |

Comprobación: la pestaña «Reescritura» tiene las dos fichas con su causa y la mejora.

## Conclusiones

### Qué se ha conseguido

Se ha construido un catálogo de prompts reutilizables y se ha comprobado que cada tipo de prompt produce un tipo de salida y un tipo de fallo propio. Una pregunta con contexto debe responder «no consta» cuando el dato no está; una extracción debe usar `null`; una clasificación debe justificar la regla aplicada; un resumen debe conservar fechas y cifras. Lo habitual es que los prompts peor puntuados mejoren con una sola línea que cierre el fallo concreto observado, y la guía final convierte esa experiencia en un criterio de decisión que el equipo puede reutilizar.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué tipos de prompt resultaron más fiables y cuáles más propensos a inventar?

   <details>
   <summary>Respuesta</summary>

   Los más fiables son los que se pueden verificar campo a campo: extracción, clasificación y transformación. Los más propensos a inventar son los que no tienen una única respuesta en el documento: planificación, completado y simulación.

   </details>

2. ¿Qué diferencia práctica hay entre «resumir» y «extraer»?

   <details>
   <summary>Respuesta</summary>

   Resumir condensa y decide qué es importante; su fallo típico es la omisión. Extraer devuelve campos concretos que se piden; su fallo típico es la invención o un valor equivocado. La extracción se puede validar con un esquema; el resumen, no.

   </details>

3. ¿Qué tipo de prompt conviene para alimentar una herramienta automática y cuál para una persona?

   <details>
   <summary>Respuesta</summary>

   Para una herramienta automática, extracción y clasificación con salida estructurada y esquema. Para una persona, resumen, transformación a tabla o redacción con estructura legible.

   </details>

4. ¿En qué se parecen una transformación y una extracción, y en qué se diferencian?

   <details>
   <summary>Respuesta</summary>

   Ambas cambian la forma de la información sin crear contenido nuevo. La transformación conserva todo el contenido en otro formato; la extracción selecciona campos y descarta el resto.

   </details>

5. Una misma necesidad («informar al equipo») puede resolverse con varios tipos. ¿Qué preguntas conviene hacerse para elegir? Escribir tres y, con ellas, decidir qué tipo usar para cada una de estas necesidades: conocer un plazo exacto de la circular, avisar al equipo del cambio, pasar la sección 2 a otro formato y asignar una prioridad a una incidencia ([§3.4 Elegir el tipo de prompt correcto](../../modulos/03-tipos-funcionales-de-prompts/03-simulacion-y-combinacion-de-funciones.md#34-elegir-el-tipo-de-prompt-correcto)).

   <details>
   <summary>Respuesta</summary>

   Se elige según quién usará la salida, el riesgo de equivocarse y la forma más sencilla de resolver la necesidad. Tres preguntas que sirven: ¿la respuesta está en el documento o hay que crear algo nuevo? ¿Se necesita el mismo contenido en otro formato o menos texto? ¿Se necesita un campo concreto o una etiqueta de una lista cerrada? Con ellas: un plazo exacto, pregunta-respuesta con contexto (o extracción si debe pasar a otra herramienta); avisar al equipo, un resumen o una instrucción directa; la sección 2 en otro formato, una transformación; la prioridad de una incidencia, una clasificación con la regla aplicada.

   </details>

### Autoevaluación

- [ ] Cada prompt corresponde claramente a un tipo y su salida lo refleja.
- [ ] Cada ficha tiene un criterio de calidad que se pueda verificar.
- [ ] Se comprobaron las respuestas contra la circular y no por impresión.
- [ ] Se documentó al menos un fallo real de cada tipo (o su ausencia razonada).
- [ ] En los prompts de extracción y clasificación hay instrucciones sobre datos ausentes o casos fuera de categoría.

### Errores típicos

- Redactar prompts del mismo tipo con distinto nombre.
- No fijar un criterio de calidad verificable.
- No prever la ausencia de datos en extracción y clasificación.
- Valorar solo el “aspecto” del resultado sin contrastarlo con el documento.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Hechos clave de la circular (Paso 1, ya cargados en la hoja)

1. Vigencia desde el 3 de noviembre de 2026.
2. 41 incidencias de conectores en el tercer trimestre.
3. El 37 % se clasificó inicialmente como P3 y se reclasificó como P2.
4. Tiempo medio hasta la primera respuesta en esos casos: 9 horas, frente a 4 horas comprometidas para el plan Team.
5. P1: exposición de documentos a usuarios sin permiso, o sincronización detenida que afecta a más de un espacio de un cliente Enterprise.
6. P2: sincronización detenida más de 6 horas o más de 500 documentos pendientes.
7. El agente de primera línea puede subir la prioridad; solo un especialista de segundo nivel puede bajarla.
8. Aviso interno en el canal #incidencias-conectores en menos de 15 minutos para P1/P2.
9. Información al cliente cada 4 horas (P1) y cada 8 horas (P2).
10. Resumen de causa raíz en un máximo de 5 días hábiles.

### Salida esperada y criterio de calidad de los cinco tipos que se ejecutan (Paso 2)

Cada criterio tiene tres partes (forma, contenido obligatorio y lo prohibido) y se comprueba con un sí o un no. Los hechos son los del Paso 1.

- Tipo 2 · Pregunta-respuesta con contexto. *Salida esperada:* una frase que dice que solo un especialista de segundo nivel puede bajar la prioridad. *Criterio:* se cumple si (1) es una frase, o dos como máximo; (2) nombra al especialista de segundo nivel; (3) no atribuye esa facultad al agente de primera línea ni a nadie más, y no añade datos que no estén en la circular.
- Tipo 4 · Transformación. *Salida esperada:* una tabla con las columnas Prioridad, Condición y Observaciones, y una fila por cada prioridad (P1 a P4), con las condiciones de la sección 2. *Criterio:* se cumple si (1) tiene exactamente tres columnas con esos nombres y cuatro filas; (2) conserva los datos: P1 menciona a los clientes Enterprise y más de un espacio, P2 «más de 6 horas» y «más de 500 documentos», P3 «menos de 6 horas»; (3) no añade condiciones ni prioridades que no estén en la circular.
- Tipo 5 · Resumen (el modelo del paso). *Salida esperada:* un párrafo de 60 palabras como máximo con el cambio, el motivo (41 incidencias, 37 % reclasificadas) y la fecha (3 de noviembre de 2026). *Criterio:* se cumple si (1) tiene 60 palabras o menos; (2) incluye la fecha y las dos cifras; (3) no contiene opiniones ni datos que no estén en la circular.
- Tipo 6 · Extracción. *Salida esperada:* un JSON con vigencia 2026-11-03, aviso interno de 15 minutos, información al cliente cada 4 horas (P1) y cada 8 (P2), y causa raíz en 5 días hábiles. *Criterio:* se cumple si (1) es un JSON válido y no lleva texto alrededor; (2) tiene las cuatro claves pedidas con los valores 2026-11-03, 15, 4 y 8, y 5; (3) ningún valor está inventado: lo que no consta aparece como `null`.
- Tipo 7 · Clasificación. *Salida esperada:* P2, justificado con la regla de la sincronización detenida más de 6 horas. *Criterio:* se cumple si (1) responde P2 y no otra prioridad; (2) cita la regla de las 6 horas; (3) no inventa condiciones (por ejemplo, un cliente Enterprise) ni trata los 120 documentos pendientes como si superasen el umbral de 500.

### Fichas de referencia

| N.º | Prompt de ejemplo | Salida y criterio | Fallo característico |
|---|---|---|---|
| 1 Instrucción directa | «Redacta un aviso de tres líneas para el canal interno que anuncie el cambio de criterio de prioridad de conectores a partir del 3 de noviembre. Tono claro y directo. Usa solo la información de la circular.» | 3 líneas; incluye la fecha. | Añadir datos no contenidos (p. ej., enlaces o nombres). |
| 2 Q&A con contexto | «Responde usando solo la circular. Si no está, di “no consta”. Pregunta: ¿Quién puede bajar la prioridad de una incidencia de conector?» | «Un especialista de segundo nivel». | Responder con conocimiento general en lugar de la circular. |
| 3 Completado | «Completa la frase manteniendo el sentido de la circular: “El agente de primera línea puede subir la prioridad, pero…”» | «…solo un especialista de segundo nivel puede bajarla». | Completar con algo plausible pero distinto. |
| 4 Transformación | «Convierte la sección 2 en una tabla con las columnas Prioridad, Condición y Observaciones. No cambies ningún dato.» | Tabla con P1–P4 fieles. | Alterar umbrales (6 horas, 500 documentos). |
| 5 Resumen | «Resume en 60 palabras para la dirección: cambio, motivo y fecha. Sin opiniones.» | ≤ 60 palabras con motivo (41 incidencias, 37 %) y fecha. | Omitir la fecha o el motivo; exceder la longitud. |
| 6 Extracción | «Extrae a JSON {vigencia, aviso_interno_minutos, info_cliente_horas:{P1,P2}, causa_raiz_dias_habiles}. Si un dato no consta, usa null.» | `{"vigencia":"2026-11-03","aviso_interno_minutos":15,"info_cliente_horas":{"P1":4,"P2":8},"causa_raiz_dias_habiles":5}` | Inventar valores para P3/P4 (no constan). |
| 7 Clasificación | «Clasifica la incidencia en P1, P2, P3 o P4 según la circular y justifica con la regla aplicada. Incidencia: “Desde hace 8 horas el conector de SharePoint no sincroniza y hay 120 documentos pendientes”.» | P2 (más de 6 horas sin sincronizar). | Fuerza una categoría sin base; ignora la regla de las 6 horas. |
| 8 Comparación | «Compara los tiempos de información al cliente de P1 y P2 en una tabla de tres columnas: Aspecto, P1, P2.» | 4 h frente a 8 h, aviso de 15 minutos en ambas. | Mezclar datos de otras prioridades. |
| 9 Planificación | «Plan de implantación en tres semanas con acciones, responsables (solo los que aparezcan en la circular) y entregables.» | Plan con hitos. | Inventar responsables y fechas. |
| 10 Simulación | «Actúa como un agente nuevo y hazme preguntas sobre la circular, de una en una. Cuando responda, indica si mi respuesta es coherente con la circular.» | Diálogo interactivo. | Dejar de ser fiel a la circular. |

### Observaciones habituales

- Los tipos con más riesgo de invención son planificación, completado y simulación: no tienen “respuesta única” en el documento y el modelo rellena huecos.
- Los más verificables son extracción, clasificación y transformación, donde se puede comprobar campo a campo.
- Resumen y comparación fallan sobre todo por omisión (algo importante no aparece), que es más difícil de detectar que la invención.

### Criterio de elección (apoya la pregunta de reflexión 5)

1. ¿La respuesta está en el documento? → Q&A con contexto.
2. ¿Se necesita el mismo contenido en otro formato? → Transformación.
3. ¿Se necesita menos texto con las ideas principales? → Resumen.
4. ¿Se necesitan campos concretos para otra herramienta? → Extracción.
5. ¿Se necesita asignar una etiqueta de una lista cerrada? → Clasificación.
6. ¿Se necesita decidir entre alternativas? → Comparación.
7. ¿Hay que crear algo nuevo? → Generación / planificación, con los límites explícitos.
8. ¿Se quiere ensayar una conversación? → Simulación.

</details>

### Para seguir

- Encadenar dos tipos: extracción → comparación, o extracción → clasificación → resumen ([§3.3 Combinar funciones en un mismo flujo](../../modulos/03-tipos-funcionales-de-prompts/03-simulacion-y-combinacion-de-funciones.md#33-combinar-funciones-en-un-mismo-flujo) y [§4.2 Caso integrado: de documento a decisión](../../modulos/03-tipos-funcionales-de-prompts/04-seleccion-caso-integrado-y-sintesis.md#42-caso-integrado-de-documento-a-decisión)).
- Añadir un undécimo tipo (por ejemplo, un prompt evaluativo que valore la claridad de la circular con una rúbrica).

---

[← Laboratorios](../README.md) · [Módulo 03](../../modulos/03-tipos-funcionales-de-prompts/README.md) · [← 02B](../02B/README.md) · [03B →](../03B/README.md)
