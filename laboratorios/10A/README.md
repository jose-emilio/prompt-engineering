[← Laboratorios](../README.md) · [Módulo 10](../../modulos/10-generacion-creativa-y-contenidos/README.md) · [← 09B](../09B/README.md) · [10B →](../10B/README.md)

# Laboratorio 10A · Briefing, ideación y selección

Módulo 10 · Generación creativa y producción de contenidos · Duración estimada: 50 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Pasar de un encargo vago a un briefing, generar ideas con varias técnicas, elegir con criterios y desarrollar la mejor sin salirse de los hechos. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md); en [`datos/rescate/`](datos/rescate/) hay material de referencia para poder seguir |

Hoja de ruta:

- Paso 1 · Del encargo vago al briefing (11 min)
- Paso 2 · Generar ideas con distintas técnicas (16 min)
- Paso 3 · Medir la homogeneidad (5 min)
- Paso 4 · Converger con criterios (10 min)
- Paso 5 · Desarrollar la idea elegida (8 min)

<details>
<summary>Secciones del módulo relacionadas (8)</summary>

- [§1.1 El LLM como colaborador creativo](../../modulos/10-generacion-creativa-y-contenidos/01-ideacion-y-briefing.md#11-el-llm-como-colaborador-creativo)
- [§1.2 Definir un briefing creativo](../../modulos/10-generacion-creativa-y-contenidos/01-ideacion-y-briefing.md#12-definir-un-briefing-creativo)
- [§1.3 Brainstorming divergente](../../modulos/10-generacion-creativa-y-contenidos/01-ideacion-y-briefing.md#13-brainstorming-divergente)
- [§1.4 Técnicas de ideación](../../modulos/10-generacion-creativa-y-contenidos/01-ideacion-y-briefing.md#14-técnicas-de-ideación)
- [§1.5 Convergencia y selección](../../modulos/10-generacion-creativa-y-contenidos/01-ideacion-y-briefing.md#15-convergencia-y-selección)
- [§1.6 Generación de alternativas estratégicas](../../modulos/10-generacion-creativa-y-contenidos/01-ideacion-y-briefing.md#16-generación-de-alternativas-estratégicas)
- [§4.2 Errores frecuentes en prompting creativo](../../modulos/10-generacion-creativa-y-contenidos/04-caso-practico-errores-y-cierre.md#42-errores-frecuentes-en-prompting-creativo)
- [§4.3 Plantillas creativas reutilizables](../../modulos/10-generacion-creativa-y-contenidos/04-caso-practico-errores-y-cierre.md#43-plantillas-creativas-reutilizables)

</details>

## Justificación del laboratorio

El 2 de febrero de 2027 Altanoria lanza «Revisión de pull requests» en Altanoria Copilot, y Marketing necesita un concepto de campaña dirigido a responsables de ingeniería. El encargo original es una sola frase: «Necesitamos una campaña chula para lo de las revisiones de código». Si se le pasa tal cual a un asistente de IA, devolverá ideas genéricas, parecidas entre sí y, con frecuencia, con afirmaciones que el producto no puede cumplir.

Un asistente es un buen colaborador creativo si se le da un buen briefing, se le pide variedad de verdad y se usa un criterio explícito para elegir. Este laboratorio recorre ese proceso completo: primero convertir el encargo vago en un briefing sólido, después generar muchas ideas con técnicas de ideación distintas (sin evaluarlas todavía), luego medir cuánta variedad hay realmente y, por último, converger con una matriz de criterios ponderados y desarrollar la idea ganadora comprobando que no promete nada fuera de la hoja de hechos del producto.

La idea central es no perder el control: el modelo propone, pero el criterio y la responsabilidad de lo que se publica son humanos.

## Objetivos

Usar un modelo como colaborador creativo sin perder el control del resultado: redactar un briefing sólido, generar muchas ideas con técnicas de ideación distintas, y converger con una matriz de criterios explícita para elegir la idea que se desarrollará. Todo sobre un lanzamiento de producto de Altanoria, con una hoja de hechos como única fuente de verdad.

Al terminar el laboratorio se habrá conseguido:

- Convertir un encargo vago en un briefing completo (objetivo, público, insight, mensaje, tono, canales, restricciones, qué no se quiere).
- Diferenciar divergir (muchas ideas, sin filtrar) de converger (evaluar y elegir) y no mezclar ambas fases.
- Aplicar técnicas de ideación: lista libre, restricciones forzadas, analogías, inversión, «y si…», puntos de vista distintos.
- Evitar el cliché y la homogeneidad de las ideas generadas.
- Usar criterios ponderados para seleccionar, y comprobar la veracidad frente a la hoja de hechos.

Conceptos que se usan:

- **Briefing creativo**. Documento breve que alinea a todos sobre qué se quiere conseguir, para quién y con qué límites. Un briefing débil produce ideas genéricas.
- **Divergencia y convergencia**. Primero se generan muchas opciones sin juzgarlas; después se evalúan con criterios. Si el modelo evalúa mientras genera, las ideas se parecen entre sí.
- **Homogeneidad**. Los modelos tienden a las ideas más probables. Para obtener variedad hay que forzarla: restricciones, perspectivas, analogías y exclusiones («nada de metáforas de velocidad ni cohetes»).
- **Veracidad creativa**. La creatividad no autoriza a inventar características, cifras o fechas del producto: solo pueden usarse los hechos aprobados.

## Recursos necesarios

- Un asistente de chat cualquiera.
- Datos en [`datos/`](datos/):
  - [`hechos_producto.md`](datos/hechos_producto.md): hoja de hechos de «Revisión de pull requests» de Altanoria Copilot, con datos aprobados, qué no hace y afirmaciones prohibidas.
  - [`plantilla_briefing.md`](datos/plantilla_briefing.md): plantilla de briefing.
  - [`criterios_seleccion.csv`](datos/criterios_seleccion.csv): seis criterios ponderados.
  - [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): matriz de selección en hoja de cálculo, con los criterios y sus pesos; calcula el total ponderado y el puesto de cada idea.
- Perfil de la empresa: [`altanoria.md`](../comun/empresa/altanoria.md).

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: La Espiga quiere una campaña para el roscón de reyes. Se recorre el método: briefing, ideas, comprobar que no son todas iguales, elegir con criterios y desarrollar la elegida.

Paso 1: del encargo vago al briefing. Encargo vago: «hazme una campaña del roscón». El briefing lo concreta.

| Elemento | Contenido |
|---|---|
| Objetivo | vender 200 roscones antes del 5 de enero |
| Público | familias del barrio que ya compran pan |
| Mensaje | el roscón de La Espiga se hace cada mañana, con ingredientes de siempre |
| Tono | cercano y cálido |
| Canal | cartel en la tienda y mensajes de WhatsApp |
| Restricciones | no prometer descuentos que no existan; no afirmar «sin gluten» |
| Éxito | pedidos recibidos antes del 20 de diciembre |

Pasos 2 y 3: ideas y homogeneidad. Con el briefing se piden 10 ideas sin más instrucciones y otras 10 aplicando la técnica de las restricciones («sin usar descuentos»). Se agrupan por tema.

| Prompt | Ideas | Temas distintos |
|---|---|---|
| Sin técnica | 10 | 3 (casi todas, descuentos y regalos) |
| Con la restricción «sin descuentos» | 10 | 7 |

Las ideas de un asistente tienden a parecerse entre sí; una restricción abre el abanico.

Paso 4: converger con criterios. Los criterios y sus pesos se fijan antes de mirar las ideas; cada finalista se puntúa de 1 a 5 en cada criterio.

| Criterio | Peso |
|---|---|
| Originalidad | 0,30 |
| Viabilidad | 0,30 |
| Ajuste al mensaje | 0,25 |
| Coste (5 = barato) | 0,15 |

| Idea | Originalidad | Viabilidad | Ajuste | Coste | Total ponderado | Puesto |
|---|---|---|---|---|---|---|
| A · Roscón sorpresa a domicilio | 4 | 3 | 5 | 2 | 3,65 | 2 |
| B · Concurso de la mejor corona | 5 | 2 | 3 | 3 | 3,30 | 3 |
| C · Reserva anticipada con regalo | 2 | 5 | 4 | 5 | 3,85 | 1 |

Gana la C sobre todo por viabilidad y coste. Si el equipo valorase más la originalidad, la A pasaría delante: conviene revisar si los pesos reflejan lo que de verdad importa.

Paso 5: desarrollar la idea elegida. Se pide un cartel de 40 palabras y un mensaje de WhatsApp de 25, con el briefing y la idea. Se comprueba que no prometen más de lo que dice la restricción («el regalo» es una felicitación, no un descuento).

Qué se espera ver en tu laboratorio: el briefing de Altanoria, las ideas con y sin técnica, la matriz con los pesos que figuran en la hoja y el total calculado solo.

## Pasos de ejecución

Todo el laboratorio se hace en un chat. Se usa siempre una conversación nueva para cada técnica de ideación, para que las ideas de una no contaminen a la siguiente.

### Paso 1 · Del encargo vago al briefing (11 minutos)
1. Partir del encargo original: «Necesitamos una campaña chula para lo de las revisiones de código». Escribir las diez preguntas que habría que responder antes de generar ideas (público, objetivo, qué se puede decir, tono, canales, restricciones…).
2. Abrir [`datos/plantilla_briefing.md`](datos/plantilla_briefing.md) y [`datos/hechos_producto.md`](datos/hechos_producto.md) (la hoja de hechos aprobados, lo que el producto no hace y las afirmaciones prohibidas). Completar el briefing en el documento de resultados, de modo que cada mensaje de apoyo salga de la hoja de hechos.
3. Pegar el briefing en una conversación nueva con este prompt, que pide una crítica sin proponer ideas todavía:

```text
Revisa este briefing de campaña. Señala ambigüedades, huecos y contradicciones; no propongas ideas todavía.

<briefing>
{pegar el briefing completado}
</briefing>
<hechos>
{pegar hechos_producto.md}
</hechos>
```

4. Incorporar al briefing las observaciones que parezcan útiles.

Si te has atascado: un briefing completo de ejemplo está en [`datos/rescate/briefing_ejemplo.md`](datos/rescate/briefing_ejemplo.md); permite seguir con la ideación y comparar con el propio.

Comprobación: hay un briefing completo en el que cada mensaje de apoyo remite a un hecho aprobado.

### Paso 2 · Generar ideas con distintas técnicas (16 minutos)
Con el briefing pegado en el prompt, generar ideas de campaña con técnicas distintas, pidiendo solo ideas (sin evaluarlas) y ocho cada vez. Cada técnica en una conversación nueva. En esta versión se usan dos (si hay tiempo, probar las otras tres de la tabla):

Técnica T2 · restricciones forzadas:

```text
Con este briefing, genera 8 conceptos de campaña que no usen la palabra «velocidad», ni cohetes, ni robots. Solo ideas: una frase por idea, sin evaluarlas.

<briefing>
{pegar el briefing}
</briefing>
```

Técnica T4 · inversión:

```text
Con este briefing, genera 8 conceptos partiendo del peor momento de una revisión de código. Solo ideas: una frase por idea, sin evaluarlas.

<briefing>
{pegar el briefing}
</briefing>
```

Otras técnicas: T1, lista libre («genera 8 conceptos de campaña muy distintos entre sí»); T3, analogías («8 conceptos basados en analogías con oficios no tecnológicos: correctores de imprenta, árbitros, editores…»); T5, puntos de vista («8 conceptos desde la mirada de un desarrollador junior, una responsable de ingeniería y un auditor de seguridad»).

Guardar todas las ideas con una frase cada una.

Comprobación: hay, como mínimo, 16 ideas guardadas con su frase.

### Paso 3 · Medir la homogeneidad (5 minutos)
1. Agrupar las ideas por familia temática (por ejemplo, «velocidad», «seguridad», «trabajo en equipo»). Contar cuántas familias distintas hay.
2. Anotar qué técnica produjo más variedad y cuál más clichés.
3. Marcar las ideas que incumplen la hoja de hechos: prometen más de lo permitido, citan cifras inventadas o usan afirmaciones prohibidas.

Comprobación: hay un recuento de familias y una lista de ideas descartadas por incumplir los hechos.

### Paso 4 · Converger con criterios (10 minutos)
1. Seleccionar diez ideas candidatas, sin repetir familia y respetando los hechos.
2. Abrir [`datos/criterios_seleccion.csv`](datos/criterios_seleccion.csv): seis criterios ponderados, con lo que significa un 1, un 3 y un 5 en cada uno (columnas `valor_1`, `valor_3` y `valor_5`; la pestaña «Criterios» de la hoja los repite). Pedir al asistente que puntúe cada idea de 1 a 5 en cada criterio, con una justificación breve para cada nota: Para guardar las puntuaciones y calcular el total ponderado de cada idea, usar la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) (pestaña «Matriz»).

```text
Puntúa cada idea de 1 a 5 en cada criterio de la tabla, con una justificación breve por cada nota. Usa la escala de la tabla: valor_1 describe una idea que merece un 1, valor_3 un 3 y valor_5 un 5; las notas 2 y 4 son intermedias. Calcula la puntuación ponderada. Penaliza cualquier idea que contradiga la hoja de hechos.

<criterios>
{pegar criterios_seleccion.csv}
</criterios>
<hechos>
{pegar hechos_producto.md}
</hechos>
<ideas>
{pegar las 10 ideas elegidas}
</ideas>
```

3. Escribir las notas en la pestaña «Matriz» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): calcula la puntuación ponderada de cada idea (cada nota multiplicada por el peso del criterio) y su puesto. Ordenar las ideas por la columna «Puesto».
4. Contrastar con el propio criterio: ¿hay alguna idea que se elegiría por intuición pese a su puntuación? ¿Falta algún criterio?

Comprobación: la pestaña «Matriz» tiene diez ideas ordenadas con su puntuación ponderada.

### Paso 5 · Desarrollar la idea elegida (8 minutos)
1. Pedir al asistente que desarrolle la idea ganadora en una ficha: concepto, mensaje central, tres piezas, tono, riesgos y qué hecho de la hoja respalda cada afirmación. Para que la ficha salga con esa forma, conviene pedirla con esta estructura:

   ```text
   Concepto: [una frase]
   Mensaje central: [una frase]
   Piezas: 1) [pieza y canal]  2) [pieza y canal]  3) [pieza y canal]
   Tono: [tres adjetivos]
   Riesgos: [qué podría salir mal]
   Hechos que respaldan: [cada afirmación → el hecho de la hoja del que sale]
   ```

2. En una conversación nueva, pasar la ficha y la hoja de hechos y pedir una segunda pasada: «Señala cualquier afirmación que no esté respaldada por la hoja de hechos».

Comprobación: la ficha está completa y cada afirmación remite a un hecho de la hoja.

## Conclusiones

### Qué se ha conseguido

Se ha recorrido un proceso creativo completo con un asistente sin perder el control del resultado: un briefing sólido que parte de hechos aprobados, ideas generadas con técnicas distintas para ganar variedad, una medida de cuántas familias de ideas había de verdad, una selección con criterios explícitos y ponderados, y una comprobación de que lo que se promete está respaldado. Lo habitual es que las ideas de una sola petición se parezcan mucho entre sí y que algunas prometan más de lo que el producto hace; por eso el valor del proceso está en las técnicas que fuerzan la variedad, en el filtro de hechos y en que la decisión final siga siendo humana.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué técnica de ideación dio resultados más originales? ¿Por qué?

   <details>
   <summary>Respuesta</summary>

   Normalmente las restricciones forzadas, las analogías y la inversión, porque obligan a salir de lo más probable; la lista libre produce familias repetidas.

   </details>

2. ¿Qué pasó cuando se pidió generar y evaluar a la vez (si se probó)?

   <details>
   <summary>Respuesta</summary>

   Las ideas se parecen entre sí y el modelo se autocensura o evalúa demasiado pronto, con lo que se pierde variedad; por eso se separan las fases de generar y de evaluar.

   </details>

3. ¿Qué criterios de selección tienen más riesgo de que el modelo “regale” notas altas?

   <details>
   <summary>Respuesta</summary>

   Originalidad y relevancia, que son subjetivas. La veracidad es verificable contra la hoja de hechos. Conviene exigir una justificación por nota y contrastarla.

   </details>

4. ¿Qué papel debe jugar una persona en la selección final?

   <details>
   <summary>Respuesta</summary>

   Define los criterios, valida los hechos, decide la selección final, asume la responsabilidad y aprueba.

   </details>

5. ¿Cómo evitaría que la campaña suene igual que la de la competencia?

   <details>
   <summary>Respuesta</summary>

   Excluyendo en el briefing los clichés y enfoques descartados, usando analogías de otros sectores, contrastando con campañas existentes y haciendo revisar la originalidad y la voz de marca a una persona.

   </details>

### Autoevaluación

- [ ] El briefing responde a los diez apartados y cada mensaje de apoyo sale de la hoja de hechos.
- [ ] La generación de ideas y su evaluación se hicieron en pasos separados.
- [ ] Hay al menos cinco técnicas distintas y más de seis familias temáticas.
- [ ] Se han descartado las ideas que incumplen la hoja de hechos.
- [ ] La selección usa criterios ponderados con justificación.
- [ ] La ficha final no contiene cifras, fechas ni funciones fuera de la hoja de hechos.
- [ ] Se identifica qué decisiones fueron humanas.

### Errores típicos

- Un briefing de tres líneas.
- Aceptar la primera idea que suena bien.
- Pedir ideas «originales» sin decir qué clichés evitar.
- Dejar que el modelo puntúe sus propias ideas sin justificación.
- No comprobar los hechos de la ficha final.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Diez preguntas del briefing

1. ¿Qué se quiere conseguir con la campaña (pruebas, upgrades, awareness) y cómo se medirá?
2. ¿Quién decide la compra y quién influye?
3. ¿Qué preocupación real tienen esas personas respecto a las revisiones de código?
4. ¿Qué es exactamente «Revisión PR» y qué no hace?
5. ¿Qué datos de la beta pueden usarse y cuáles no?
6. ¿Qué mensaje principal se quiere que recuerden?
7. ¿Qué tono tiene la marca?
8. ¿En qué canales se difundirá?
9. ¿Qué afirmaciones están prohibidas?
10. ¿Qué enfoques o clichés se descartan?

### Briefing de ejemplo

1. Objetivo: conseguir 400 pruebas gratuitas de Copilot Team en el primer mes tras el lanzamiento (2 de febrero de 2027).
2. Público: responsables de ingeniería (decisores) y desarrolladores senior (influencers) de equipos de 5 a 200 personas.
3. Insight: la revisión de código es imprescindible, pero el primer comentario tarda horas y retrasa la entrega.
4. Mensaje principal: revisiones más rápidas sin perder el control humano.
5. Apoyo: (a) en la beta, la mediana del tiempo hasta la primera revisión pasó de 9,5 h a 3,1 h; (b) el código del cliente nunca se usa para entrenar modelos; (c) funciona con los repositorios que ya usas.
6. Tono: cercano, directo, con humor discreto; trato de tú; sin grandilocuencia.
7. Canales: correo, redes y vídeo corto.
8. Restricciones: disponible en Team y Enterprise (no Starter); no sustituye a los revisores; sin cifras fuera de la beta; sin nombrar competidores.
9. Qué no queremos: cohetes y robots, metáforas de velocidad, «el futuro es hoy», miedo a perder el empleo.
10. Entregables: concepto, mensaje central y tres piezas.

### Ejemplos de lo que aparece en cada técnica

| Técnica | Ejemplos típicos | Observación |
|---|---|---|
| T1 Lista libre | «Primera impresión» · «El segundo par de ojos» | Familias repetidas: velocidad, ayudante, equipo |
| T2 Restricciones | «Cero horas de espera» (evita «velocidad») | Mayor variedad que T1 |
| T3 Analogías | «El corrector de pruebas de tu código» · «El árbitro que avisa, no pita» | Original, cuidado con exagerar capacidades |
| T4 Inversión | «El pull request que lleva tres días esperando» | Conecta con el insight; humor |
| T5 Puntos de vista | «Lo que desearía un junior que le dijeran en su primer PR» | Variedad emocional |

Suelen aparecer tres a seis familias en una ideación sin restricciones y ocho a doce al forzar técnicas distintas.

### Ideas que incumplen la hoja de hechos (ejemplos)

- «Elimina los errores antes de que lleguen a producción» → prohibido («elimina los errores»).
- «Un 70 % más rápido» → cifra no aprobada (la beta indica 9,5 h → 3,1 h, una reducción de aproximadamente dos tercios, pero no se debe usar otra cifra que las de la hoja; usar «de 9,5 a 3,1 horas»).
- «Tu nuevo revisor» → sugiere sustitución humana.
- «Disponible para todos los planes» → falso.

### Matriz de selección (ejemplo con puntuaciones ilustrativas)

| Idea | Alineación (0,25) | Veracidad (0,20) | Originalidad (0,15) | Relevancia (0,20) | Viabilidad (0,10) | Escalabilidad (0,10) | Total |
|---|---|---|---|---|---|---|---|
| «El PR que esperaba» (inversión) | 5 | 5 | 4 | 5 | 4 | 4 | 4,65 |
| «El árbitro que avisa, no pita» | 4 | 4 | 5 | 4 | 3 | 4 | 4,05 |
| «Cero horas de espera» | 4 | 3 | 3 | 4 | 5 | 5 | 3,85 |

(Valores ilustrativos: sirven para mostrar el cálculo. Total = suma de nota × peso.)

### Ficha de la idea ganadora (ejemplo, Paso 5)

- Concepto: «El PR que esperaba»: la campaña parte del peor momento de una revisión de código, el pull request que espera comentarios, y lo cuenta desde su punto de vista.
- Mensaje central: revisiones más rápidas sin perder el control humano (mensaje clave 1 de la hoja de hechos).
- Tres piezas: (1) un correo a responsables de ingeniería, con la cifra de la beta; (2) una publicación en redes con la pregunta «¿y si el primer comentario llegara en horas?»; (3) un vídeo corto de unos 20 segundos desde el pull request.
- Tono: cercano, directo, con humor discreto; trato de tú.
- Riesgos: sugerir que sustituye a los revisores; presentar la cifra de la beta como una promesa y no como una mediana medida en 38 clientes; mencionar una fecha o un plan distintos de los de la hoja.
- Hechos que respaldan cada afirmación: «de 9,5 horas a 3,1 horas hasta la primera revisión» → datos de la fase beta; «sin perder el control humano» → «No sustituye la revisión humana»; «disponible en Team y Enterprise» → disponibilidad; «el código nunca se usa para entrenar modelos» → mensaje clave 2.



Los modelos tienden a regalar notas altas en «originalidad» y «relevancia»; conviene exigir la justificación y, cuando discrepe el criterio humano, prevalece este.

### Reglas que mejoran la fase creativa

1. Separar generar y evaluar.
2. Dar al modelo restricciones y exclusiones, no solo temas.
3. Pedir cantidad antes que calidad (8 a 12 ideas por técnica) y filtrar después.
4. Cotejar siempre con la hoja de hechos.
5. La decisión final es humana.

</details>

### Para seguir

- Repetir la ideación con un público distinto (auditores de seguridad) y comparar.
- Generar un «anti-briefing» (qué no hacer) y usarlo como filtro.
- Comparar el resultado con el de otro modelo.

---

[← Laboratorios](../README.md) · [Módulo 10](../../modulos/10-generacion-creativa-y-contenidos/README.md) · [← 09B](../09B/README.md) · [10B →](../10B/README.md)
