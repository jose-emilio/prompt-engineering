[← Laboratorios](../README.md) · [Módulo 08](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/README.md) · [← 07B](../07B/README.md) · [08B →](../08B/README.md)

# Laboratorio 08A · Cazar alucinaciones

Módulo 08 · Fiabilidad, alucinaciones y sesgos · Duración estimada: 65 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Revisar respuestas de un asistente descomponiéndolas en afirmaciones, contrastándolas con la fuente y comparando dos revisores automáticos. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Del chat: poder pegar o adjuntar los documentos de Altanoria en una conversación nueva. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Parte A · Revisar a mano
  - Paso 1 · Leer las respuestas y sus afirmaciones (8 min)
  - Paso 2 · Verificar cada afirmación contra la fuente (10 min)
  - Paso 3 · Clasificar los errores y cuantificar (9 min)
- Parte B · Usar un modelo como revisor, con y sin fuente
  - Paso 4 · Probar un revisor sin fuente (9 min)
  - Paso 5 · Probar un revisor con fuente (14 min)
  - Paso 6 · Comparar los dos revisores con la solución (6 min)
- Parte C · Defensas y política de revisión
  - Paso 7 · Proponer defensas (4 min)
  - Paso 8 · Decidir una política de revisión (5 min)

<details>
<summary>Secciones del módulo relacionadas (9)</summary>

- [§1.2 ¿Qué es una alucinación?](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#12-qué-es-una-alucinación)
- [§1.3 Formas de alucinación: catálogo de patrones](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#13-formas-de-alucinación-catálogo-de-patrones)
- [§1.4 ¿Por qué aparecen las alucinaciones?](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#14-por-qué-aparecen-las-alucinaciones)
- [§1.5 Fluidez no equivale a verdad](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#15-fluidez-no-equivale-a-verdad)
- [§1.6 Hechos, inferencias, supuestos y opiniones](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#16-hechos-inferencias-supuestos-y-opiniones)
- [§2.5 Contraste de fuentes: corroborar información](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/02-mitigacion-de-alucinaciones.md#25-contraste-de-fuentes-corroborar-información)
- [§4.1 Calibración de confianza: interpretar expresiones de certeza](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/04-aplicacion-evaluacion-y-supervision.md#41-calibración-de-confianza-interpretar-expresiones-de-certeza)
- [§4.2 Alucinaciones en tareas de extracción](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/04-aplicacion-evaluacion-y-supervision.md#42-alucinaciones-en-tareas-de-extracción)
- [§4.4 Evaluación de respuestas fundamentadas: rúbrica de criterios](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/04-aplicacion-evaluacion-y-supervision.md#44-evaluación-de-respuestas-fundamentadas-rúbrica-de-criterios)

</details>

## Justificación del laboratorio

Un asistente de IA responde consultas de clientes de Altanoria sin que nadie supervise las respuestas. Una persona de Calidad ha extraído quince de ellas para revisarlas, y hay que decidir si el asistente es fiable, qué tipos de error comete y si puede mantenerse sin revisión humana. La dificultad es que los errores de un modelo de lenguaje no se parecen a los de una persona: una respuesta con un precio equivocado, una certificación que no existe o una cláusula atribuida a un artículo inexistente suena exactamente igual de segura que una respuesta correcta.

Revisar con método significa descomponer cada respuesta en afirmaciones verificables, contrastar cada una con la fuente y clasificar el tipo de error. Solo así se puede contar, comparar y decidir. Y cuando se piensa en automatizar la revisión con otro modelo, hay que saber hasta dónde se puede fiar uno: un revisor que no tiene la fuente tiende a dar por buenas las respuestas que suenan razonables, y un revisor con la fuente detecta bastante más.

Este laboratorio recorre las tres partes del problema: revisar a mano (Parte A), usar un modelo como revisor con y sin fuente (Parte B) y diseñar defensas para reducir cada tipo de error y una política de revisión (Parte C).

## Objetivos

Aprender a revisar las salidas de un modelo con método: descomponer una respuesta en afirmaciones verificables, contrastarlas con una fuente fiable, clasificar cada error según el catálogo de alucinaciones y comprobar hasta qué punto otro modelo, usado como revisor, detecta esos errores.

Al terminar el laboratorio se habrá conseguido:

- Separar una respuesta fluida en afirmaciones verificables (hechos, cifras, citas, atribuciones, inferencias).
- Verificar cada una contra la fuente y clasificarla: correcta, incorrecta, no verificable o inferencia no respaldada.
- Reconocer patrones de alucinación: cifra errónea, entidad inventada, cita inexistente, extrapolación plausible, sobreextensión del alcance, compromiso inventado.
- Entender que la fluidez no es evidencia y que el tono seguro no dice nada de la veracidad.
- Valorar las posibilidades y límites del LLM como revisor.

Conceptos que se usan:

- **Alucinación**. Contenido generado que parece plausible pero no está respaldado por la realidad o por la fuente proporcionada ([§1.2 ¿Qué es una alucinación?](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#12-qué-es-una-alucinación)). Se produce porque el modelo genera texto probable, no consulta una base de hechos.
- **Catálogo de patrones** ([§1.3 Formas de alucinación: catálogo de patrones](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#13-formas-de-alucinación-catálogo-de-patrones)): datos numéricos incorrectos, entidades o citas inventadas, atribuciones erróneas, extrapolaciones plausibles, mezclas de contextos, afirmaciones de capacidades o compromisos inexistentes.
- **Hecho, inferencia, supuesto, opinión** ([§1.6 Hechos, inferencias, supuestos y opiniones](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/01-alucinaciones-concepto-y-causas.md#16-hechos-inferencias-supuestos-y-opiniones)). Son tipos distintos de afirmación; solo los hechos se verifican directamente contra una fuente. Una inferencia puede ser razonable pero no estar en el documento.
- **Fuente de verdad**. Para estas pruebas es el conjunto de documentos de Altanoria en [`../comun/empresa/`](../comun/empresa/altanoria.md). No se verifica con otro modelo, sino con el documento.

## Recursos necesarios

- Un asistente de chat para la Parte B (revisor automático).
- Datos: [`datos/respuestas_asistente.md`](datos/respuestas_asistente.md): 15 respuestas de un asistente a consultas de clientes (la versión corta del laboratorio revisa las ocho primeras; las demás son una ampliación). Algunas son correctas; otras contienen errores. No hay clave de errores fuera de la solución.
- Hoja de cálculo: [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), para verificar afirmación por afirmación, cuantificar los errores, comparar los dos revisores y escribir las defensas y la política de revisión.
- Documentos de referencia: [`catalogo_planes.md`](../comun/empresa/catalogo_planes.md), [`sla.md`](../comun/empresa/sla.md), [`condiciones_servicio.md`](../comun/empresa/condiciones_servicio.md), [`politica_privacidad.md`](../comun/empresa/politica_privacidad.md).

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: el asistente de La Espiga contesta preguntas de clientes y un empleado revisa sus respuestas con la carta como fuente. La carta dice: barra 1,20 €, contiene gluten, roscón 18 € para 8 personas, horario de 7:00 a 14:00, pedidos confirmados en 2 horas, sin entregas en domingo y sin certificación sin gluten.

Pasos 1 y 2: separar cada respuesta en afirmaciones y darles un veredicto contra la fuente.

| Código | Afirmación | Veredicto |
|---|---|---|
| R1.1 | «La barra cuesta 1,50 €» | incorrecta (la carta dice 1,20 €) |
| R1.2 | «La barra contiene gluten» | correcta |
| R2.1 | «Tenemos certificación sin gluten de una asociación de celíacos» | no respaldada (la carta dice que no hay certificación) |
| R2.2 | «Abrimos de 7:00 a 14:00» | correcta |
| R3.1 | «El roscón sirve a 8 personas» | correcta |
| R3.2 | «Los pedidos se confirman en 2 horas» | correcta |

Paso 3: clasificar los errores y contar.

| Tipo de error | Afirmaciones |
|---|---|
| Cifra errónea | R1.1 |
| Entidad o certificación inventada | R2.1 |

| Medida | Resultado |
|---|---|
| Respuestas totalmente correctas | 1 de 3 (la R3) |
| Afirmaciones erróneas | 2 de 6 (33 %) |
| Tipo más frecuente | empate: uno de cada |

Pasos 4 a 6: dos revisores automáticos. Se marca qué afirmaciones señala cada uno como error.

| Revisor | Señala como error | Errores reales detectados | No detectados | Falsas alarmas |
|---|---|---|---|---|
| Sin la carta | R2.1 y R3.1 | 1 de 2 | 1 (R1.1) | 1 (R3.1 era correcta) |
| Con la carta | R1.1 y R2.1 | 2 de 2 | 0 | 0 |

Detección: 50 % sin fuente y 100 % con fuente. El revisor sin fuente solo reconoce lo que suena raro, y deja pasar una cifra plausible pero equivocada. Aun con fuente, hay que comprobar que las frases que cita existen de verdad.

Paso 7: defensas. Para la cifra errónea se eligen medidas de una lista: responder solo con fragmentos de la carta citando el apartado, leer los precios de una tabla y no redactarlos de memoria, y revisión humana antes de enviar.

Paso 8: política de revisión.

| Tipo de respuesta | Política |
|---|---|
| Precios | revisión humana siempre |
| Certificaciones y alérgenos | revisión humana siempre |
| Horarios | muestreo con revisor con fuente |
| Saludos | sin revisión |

Qué se espera ver en tu laboratorio: las afirmaciones de las respuestas de Altanoria, ya separadas, para dar el veredicto de cada una, y la comparación de los dos revisores calculada por la hoja.

## Pasos de ejecución

Todos los pasos se hacen en un chat, y las anotaciones van en la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx). Las respuestas que se revisan están en [`datos/respuestas_asistente.md`](datos/respuestas_asistente.md): quince respuestas de un asistente, algunas correctas y otras con errores. La fuente de verdad son los documentos de la carpeta [`../comun/empresa/`](../comun/empresa/altanoria.md): el catálogo de planes, el SLA, las condiciones de servicio y la política de privacidad. En la versión corta del laboratorio se revisan las respuestas 1 a 8.

### Parte A · Revisar a mano

#### Paso 1 · Leer las respuestas y sus afirmaciones (8 minutos)
1. Abrir `respuestas_asistente.md` y leer la primera respuesta.
2. En la pestaña «Afirmaciones» de la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) ya están separadas las afirmaciones verificables de cada respuesta (cifras, plazos, nombres, condiciones, citas), con su código (R1.1, R1.2…). Una afirmación es algo que se puede comprobar como cierto o falso, por ejemplo «cuesta 29 € por usuario y mes». Leer las de la respuesta 1 y comprobar que recogen todo lo que dice la respuesta.
3. Repetir con las respuestas 2 a 8 (las respuestas 9 a 15 son una ampliación opcional para quien tenga tiempo).

Comprobación: la pestaña «Afirmaciones» muestra las afirmaciones de las respuestas 1 a 8 y se puede señalar, en tres de ellas, la cifra, el plazo o la cita que hay que verificar.

#### Paso 2 · Verificar cada afirmación contra la fuente (10 minutos)
Para cada afirmación, localizar en los documentos el pasaje que la respalda o la contradice (con Ctrl+F se busca la cifra o la palabra clave) y elegir el veredicto en la columna «Veredicto» de la pestaña «Afirmaciones» (lista desplegable):

- Correcta: está respaldada literalmente por la fuente.
- Incorrecta: contradice la fuente.
- No respaldada: no consta en la fuente (ni se confirma ni se desmiente).
- Inferencia: es razonable, pero no está en la fuente.

Las columnas de la solución están ocultas: no abrirlas hasta terminar el Paso 3.

Comprobación: cada afirmación de las respuestas 1 a 8 tiene un veredicto.

#### Paso 3 · Clasificar los errores y cuantificar (9 minutos)
1. Para cada afirmación incorrecta o no respaldada, elegir, en la columna «Tipo de alucinación» (lista desplegable), un tipo de alucinación: cifra errónea, entidad o certificación inventada, cita o fuente inexistente, extrapolación plausible, sobreextensión (aplica a un plan lo que es de otro), compromiso inventado, atribución normativa errónea, o dato de lugar o fecha erróneo.
2. Abrir la pestaña «Cuantificar», que calcula cuántas respuestas son totalmente correctas, cuántas tienen errores, qué proporción de las afirmaciones son erróneas y cuántos errores hay de cada tipo; indica también cuál es el tipo más frecuente.
3. Mostrar las columnas ocultas de «Afirmaciones» (botón «+») y comparar con la solución: la pestaña «Cuantificar» cuenta cuántos veredictos coinciden. Revisar los que no coinciden volviendo a la fuente.

Comprobación: cada error tiene un tipo y la pestaña «Cuantificar» muestra las tres cifras (respuestas totalmente correctas, con errores y proporción de afirmaciones erróneas), el tipo más frecuente y los veredictos que coinciden con la solución.

### Parte B · Usar un modelo como revisor, con y sin fuente

#### Paso 4 · Probar un revisor sin fuente (9 minutos)
Abrir una conversación nueva, pegar las ocho respuestas y pedir: «Indica cuáles contienen errores y por qué». No adjuntar ningún documento. Marcar «sí» en la columna «¿Lo señala como error el revisor sin fuente?» de la pestaña «Afirmaciones» en cada afirmación que el revisor da por errónea (sean errores reales o no):

```text
Indica cuáles de las siguientes respuestas contienen errores y por qué.

{pegar R1 a R8}
```

Comprobación: están marcadas todas las afirmaciones que el revisor sin fuente considera errores.

#### Paso 5 · Probar un revisor con fuente (14 minutos)
Abrir otra conversación nueva, adjuntar o pegar los documentos de Altanoria y pegar las mismas ocho respuestas con este prompt:

```text
Eres un revisor de calidad. Para cada respuesta del lote, descompónla en afirmaciones verificables y comprueba cada una SOLO con los documentos adjuntos. No uses conocimiento externo.

Para cada afirmación devuelve:
Respuesta: R<n>
Afirmación: «<cita literal>»
Veredicto: correcta | incorrecta | no respaldada
Evidencia: «<cita literal del documento>» (apartado)

Si no encuentras evidencia en los documentos, el veredicto es «no respaldada».

<documentos>
{pegar catalogo_planes.md, sla.md, condiciones_servicio.md y politica_privacidad.md}
</documentos>
<respuestas>
{pegar R1 a R8}
</respuestas>
```

Marcar en la columna «¿Lo señala como error el revisor con fuente?» las afirmaciones que ahora da por erróneas.

Comprobación: están marcadas las afirmaciones que el revisor con fuente considera errores.

#### Paso 6 · Comparar los dos revisores con la solución (6 minutos)
Mirar la pestaña «Revisores»: la hoja cuenta los errores detectados, los no detectados y las falsas alarmas (afirmaciones correctas que el revisor marcó como errores) de cada revisor, comparando las marcas con la solución. Comprobar a mano las citas del revisor con fuente en los documentos y anotar cuántas son evidencias inventadas; responder también si cita alguna frase que no existe.

Comprobación: la pestaña «Revisores» está completa y muestra qué revisor es más fiable.

### Parte C · Defensas y política de revisión

#### Paso 7 · Proponer defensas (4 minutos)
Con el catálogo de errores observados, elegir en la pestaña «Defensas», para tres de los tipos de error más frecuentes, tres medidas de la lista desplegable que reduzcan ese tipo de error en el asistente original. Un ejemplo, para el tipo «cifra errónea»: responder solo con fragmentos de los documentos y citar el apartado; calcular con una herramienta en lugar de con el modelo; y revisión humana antes de enviar.

Comprobación: hay tres medidas por tipo de error principal.

#### Paso 8 · Decidir una política de revisión (5 minutos)
En la pestaña «Política de revisión», elegir para cada tipo de respuesta si se revisa siempre por una persona, por muestreo con un revisor automático con fuente, o no se revisa. Criterio: cuanto más caro es un error (dinero, compromisos, responsabilidad legal), más revisión humana. Ejemplo: los precios y los plazos se revisan siempre.

Comprobación: los seis tipos de respuesta tienen una política y la hoja cuenta cuántos tipos requieren revisión humana siempre.

## Conclusiones

### Qué se ha conseguido

Se ha revisado con método una muestra de respuestas de un asistente: descomponiendo cada una en afirmaciones, contrastándolas con la fuente y clasificando los errores. Lo habitual es que los errores más frecuentes sean cifras o plazos ligeramente equivocados y certificaciones o cláusulas inexistentes, y que los más peligrosos sean los que parecen más seguros. También se ha visto que un modelo usado como revisor sin acceso a la fuente tiende a aprobar lo que suena razonable, mientras que con la fuente detecta bastante más (aunque a veces cita una frase que no existe), y que la política de revisión no debe depender de un revisor automático sin comprobar sus citas.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué respuestas era más difícil identificar como erróneas? ¿Qué las hacía creíbles?

   <details>
   <summary>Respuesta</summary>

   Las que mezclan datos correctos con un detalle erróneo: R6 (la primera respuesta de 1 hora es correcta, la resolución en 4 horas es inventada), R10 («todos los conectores») y la cita de Gartner en R13. El tono seguro y los datos verdaderos junto al error las hacen creíbles.

   </details>

2. ¿Por qué el revisor sin fuente tiende a dar por buenas respuestas incorrectas?

   <details>
   <summary>Respuesta</summary>

   Porque no puede contrastar con una fuente: evalúa la coherencia interna y la plausibilidad. Una cifra plausible pasa; solo detecta lo que «suena» mal.

   </details>

3. ¿Qué diferencia hay entre «no respaldada» e «incorrecta» y por qué importa?

   <details>
   <summary>Respuesta</summary>

   Incorrecta contradice la fuente; no respaldada no aparece en ella. Importa porque el tratamiento es distinto (corregir frente a eliminar o derivar) y porque «no consta» no equivale a «es falso».

   </details>

4. ¿Qué respuesta del lote tiene el mayor riesgo legal o comercial? ¿Por qué?

   <details>
   <summary>Respuesta</summary>

   R6 (promesa de resolución en 4 horas) y R4 (certificación SOC 2 inexistente): generan responsabilidad contractual y reputacional.

   </details>

5. ¿Qué parte de la revisión se puede automatizar y cuál debe seguir siendo humana?

   <details>
   <summary>Respuesta</summary>

   Se puede automatizar la descomposición en afirmaciones, la comprobación de citas literales y el contraste con la fuente. Sigue siendo humana la decisión sobre compromisos contractuales o legales, la valoración de matices y el muestreo.

   </details>

### Autoevaluación

- [ ] Cada veredicto cita el documento y el apartado.
- [ ] Las respuestas con mezcla de aciertos y errores se descomponen en afirmaciones (no se juzga la respuesta como un todo).
- [ ] Se distinguen errores (❌) de lo no respaldado (⚠️) y de las inferencias (💭).
- [ ] La comparación de revisores incluye falsos negativos y falsos positivos.
- [ ] Se comprobó que las citas de evidencia del revisor existen realmente en los documentos.
- [ ] Las medidas de la Parte C están asociadas a un tipo de error concreto.

### Errores típicos

- Valorar la respuesta completa como correcta porque la primera frase lo es.
- Verificar con otro modelo en lugar de con el documento.
- Confundir «no consta» con «es falso».
- No comprobar las citas de evidencia del revisor.
- Medir solo cuántos errores se detectan, sin contar falsas alarmas.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Clave de errores del lote

| Resp. | Veredicto global | Afirmaciones erróneas o no respaldadas | Tipo de alucinación | Fuente |
|---|---|---|---|---|
| R1 | ✅ Correcta | — | — | Catálogo (Copilot: Team 29 €, mínimo 5, anual 24 €) |
| R2 | ❌ Con error | «Team garantiza 99,9 %» → son 99,5 % (99,9 % es Enterprise) | Cifra errónea / mezcla de planes | SLA §1 |
| R3 | ✅ Correcta | — | — | SLA §2 |
| R4 | ❌ Con error | «SOC 2 Tipo II desde 2024» → no consta; solo ISO 27001 (2023) y ENS en proceso | Certificación inventada | Privacidad §5 |
| R5 | ✅ Correcta | — | — | Privacidad §3 |
| R6 | ❌ Con error parcial | «1 hora 24x7» es correcto; «garantiza resolver en 4 horas» → no consta: Altanoria no garantiza tiempos de resolución | Compromiso inventado (extrapolación plausible) | SLA §4 |
| R7 | ✅ Correcta | — | — | Condiciones §5.3 |
| R8 | ❌ Con error | «72 horas, conforme al RGPD» → el plazo contractual a los clientes es de 48 horas | Cifra errónea y atribución normativa | Condiciones §12 |
| R9 | ✅ Correcta | — | — | Condiciones §7 |
| R10 | ❌ Con error parcial | 50.000 documentos y 50 usuarios son correctos; «todos los conectores» → en Team son 6; «todos» es del plan Enterprise | Sobreextensión del alcance de un plan | Catálogo (DocuMind) |
| R11 | ✅ Correcta | — | — | Privacidad §1 |
| R12 | ❌ Con error | «30 días» → la prueba gratuita dura 14 días | Cifra errónea | Catálogo, condiciones comunes |
| R13 | ❌ Con error parcial | 10 % para 25 usuarios mensual es correcto; el estudio de Gartner de 2025 es una cita inventada | Cita/fuente inexistente | Catálogo (descuento por volumen); la cita no consta en ningún documento |
| R14 | ❌ Con error parcial | Ley española correcta; «tribunales de Madrid» → son los de Valencia | Dato de lugar erróneo | Condiciones §15 |
| R15 | ✅ Correcta | — | — | Catálogo (Copilot) |

Resumen: 7 respuestas totalmente correctas y 8 con algún error (R2, R4, R6, R8, R10, R12, R13, R14). El patrón más frecuente son las cifras y plazos erróneos (R2, R8, R12); los más peligrosos son los compromisos inventados (R6: promesa de resolución en 4 horas) y las certificaciones inexistentes (R4: engaña a un proveedor que audita), porque generan responsabilidad contractual y reputacional. La cita de Gartner (R13) es el tipo más difícil de detectar sin buscarla, porque su apariencia es muy creíble.

### Qué suele ocurrir con los revisores automáticos

| Revisor | Comportamiento habitual |
|---|---|
| Sin fuente | Detecta errores flagrantes por lógica interna (por ejemplo, la cita inventada «huele» mal) pero acepta como correctas respuestas con cifras plausibles (R2, R8, R12) porque no puede contrastarlas. A veces marca como erróneas respuestas correctas por desconfianza. |
| Con fuente y formato de evidencia | Detecta la mayoría (6–8 de 8), incluidos R2, R4, R8, R12 y R14. Los fallos habituales: dar por correcto «todos los conectores» (R10) por una lectura rápida, y aceptar R6 porque la primera parte («1 hora 24x7») es correcta y contagia a la segunda. A veces inventa una evidencia: por eso hay que comprobar que las citas existen. |

Conclusión: el revisor automático con fuente reduce mucho el trabajo humano, pero no sustituye la comprobación de las citas ni la revisión de los casos de mayor impacto. Sin fuente, solo reconoce lo que "suena" mal.

### Medidas de la Parte C (ejemplo)

| Tipo de error | Medida |
|---|---|
| Cifras y plazos | Responder solo con fragmentos del catálogo y las condiciones, y citar apartado; los cálculos con herramienta. |
| Certificaciones y compromisos | Lista cerrada de afirmaciones permitidas sobre certificaciones y SLA; si no consta, «no consta» y derivar. |
| Citas externas | Prohibir citar estudios o fuentes que no estén en los documentos aportados. |
| Sobreextensión entre planes | Incluir en el contexto la tabla del plan del cliente y exigir que la respuesta indique el plan al que se refiere. |
| Datos de lugar y normativa | Datos fijos en la plantilla de respuesta; revisión humana de cualquier mención normativa. |

### Política de revisión (ejemplo)

- Siempre humana: cualquier mención a certificaciones, plazos de resolución, indemnizaciones, normativa o compromisos contractuales.
- Muestreo (10 %) con revisor automático con fuente + humano en los desacuerdos: precios, límites y condiciones de planes.
- Sin revisión: saludos, reformulaciones y resúmenes de conversaciones sin datos nuevos.

</details>

### Para seguir

- Pedir a otro modelo que genere las 15 respuestas con la misma consulta y repetir el análisis con los documentos adjuntos.
- Medir si el formato «afirmación + evidencia + veredicto» mejora la detección frente a una petición abierta.
- Implementar una comprobación automática de las citas de evidencia (que la cita literal aparezca en el texto de los documentos).

---

[← Laboratorios](../README.md) · [Módulo 08](../../modulos/08-fiabilidad-alucinaciones-y-sesgos/README.md) · [← 07B](../07B/README.md) · [08B →](../08B/README.md)
