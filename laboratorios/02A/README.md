[← Laboratorios](../README.md) · [Módulo 02](../../modulos/02-fundamentos-del-prompt-engineering/README.md) · [← 01B](../01B/README.md) · [02B →](../02B/README.md)

# Laboratorio 02A · Del prompt vago al contrato de tarea

Módulo 02 · Fundamentos del Prompt Engineering · Duración estimada: 80 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Convertir dos peticiones vagas de empleados en contratos de tarea y comprobar que el asistente responde mejor y no inventa datos. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md); en [`datos/rescate/`](datos/rescate/) hay material de referencia para poder seguir |

Hoja de ruta:

- Paso 1 · Elegir las peticiones y diagnosticar qué falta (10 min)
- Paso 2 · Probar las peticiones vagas (12 min)
- Paso 3 · Entender la estructura de un contrato de tarea (6 min)
- Paso 4 · Redactar el contrato de la petición 1 (19 min)
- Paso 5 · Redactar el contrato de la petición 3 (12 min)
- Paso 6 · Probar los contratos y comparar con las versiones vagas (11 min)
- Paso 7 · Probar la robustez: ¿qué pasa si falta un dato? (10 min)

<details>
<summary>Secciones del módulo relacionadas (6)</summary>

- [§1.4 Prompt como contrato de tarea](../../modulos/02-fundamentos-del-prompt-engineering/01-introduccion-que-es-prompt-engineering.md#14-prompt-como-contrato-de-tarea)
- [§1.5 Cuándo merece la pena estructurar un prompt](../../modulos/02-fundamentos-del-prompt-engineering/01-introduccion-que-es-prompt-engineering.md#15-cuándo-merece-la-pena-estructurar-un-prompt)
- [§3.1 Claridad frente a ambigüedad](../../modulos/02-fundamentos-del-prompt-engineering/03-principios-de-diseno.md#31-claridad-frente-a-ambigüedad)
- [§3.2 Especificidad sin sobrecargar el prompt](../../modulos/02-fundamentos-del-prompt-engineering/03-principios-de-diseno.md#32-especificidad-sin-sobrecargar-el-prompt)
- [§3.9 Manejo de información ausente o incierta](../../modulos/02-fundamentos-del-prompt-engineering/03-principios-de-diseno.md#39-manejo-de-información-ausente-o-incierta)
- [§4.3 Checklist para revisar un prompt](../../modulos/02-fundamentos-del-prompt-engineering/04-ejemplos-revision-y-sintesis.md#43-checklist-para-revisar-un-prompt)

</details>

## Justificación del laboratorio

En Altanoria Software, los empleados de Ventas, Soporte, Producto y Facturación usan un asistente de IA para trabajar más deprisa. El problema es que casi todos le escriben peticiones de una sola línea: «hazme algo con el acta», «contesta a este cliente», «escribe un correo». Cada petición admite muchas interpretaciones razonables, y el asistente elige una y la presenta con total seguridad. Los resultados son irregulares: a veces sirven, a veces inventan datos y casi siempre hay que corregirlos a mano, con la pérdida de tiempo que eso supone.

La causa rara vez es el modelo. Lo habitual es que la petición no diga para qué se necesita el resultado, quién lo va a leer, con qué datos hay que trabajar, en qué formato debe entregarse ni qué hacer cuando falta información. Una persona competente, ante una petición así, preguntaría. El modelo, en cambio, no pregunta: rellena los huecos por su cuenta.

Este laboratorio se hace para comprobarlo por uno mismo, con casos reales de la empresa, y para aprender el remedio: convertir cada petición en un contrato de tarea, es decir, en un encargo con el mismo rigor con que se encargaría un trabajo a un profesional. Es la habilidad más rentable del curso, porque se aplica a cualquier otro laboratorio y a cualquier uso cotidiano de un asistente.

La directora de Soporte de Altanoria ha pedido saber qué cambios concretos convierten una petición vaga en una buena, con ejemplos reales de «antes» y «después». Eso es lo que se averigua aquí.

## Objetivos

Al terminar el laboratorio se habrá conseguido:

- Detectar qué información falta en una petición vaga (objetivo, destinatario, datos, formato, límites y criterio de calidad).
- Comprobar con el propio asistente qué defectos produce una petición vaga: formato inadecuado, audiencia equivocada, datos inventados o longitud desajustada.
- Reescribir una petición como contrato de tarea sin sobrecargarla.
- Separar los datos de las instrucciones, para que el asistente no los confunda.
- Indicar al asistente qué hacer cuando falta un dato, en lugar de dejarle inventarlo.
- Comparar el resultado de la versión vaga con el de la versión contractual y explicar con una frase qué línea del contrato produjo qué mejora.
- Identificar los cambios de una petición que más mejoran el resultado, con ejemplos de «antes» y «después».

Conceptos que se usan (se explican en el módulo, sección [§1.4 Prompt como contrato de tarea](../../modulos/02-fundamentos-del-prompt-engineering/01-introduccion-que-es-prompt-engineering.md#14-prompt-como-contrato-de-tarea) y siguientes):

- **Contrato de tarea**: un prompt que define el resultado esperado, los datos de partida, las restricciones, el formato de entrega y el criterio de aceptación. No hace falta usar siempre todos los apartados: se usan los que reducen la ambigüedad y el riesgo.
- **Ambigüedad**: una petición es ambigua cuando admite varias interpretaciones razonables.
- **Delimitación**: encerrar los datos entre marcas claras (por ejemplo, `<acta>` y `</acta>`) para que no se confundan con las instrucciones.

## Recursos necesarios

Este laboratorio no necesita programar ni instalar nada. Hace falta lo siguiente:

| Recurso | Para qué sirve | Dónde está o cómo conseguirlo |
|---|---|---|
| Un asistente de IA con chat | Probar las peticiones | Cualquiera sirve (de pago o gratuito). Debe permitir abrir una conversación nueva en cada prueba |
| Un documento de texto | Escribir los contratos y las frases de mejora | Word, Google Docs, Notas o Bloc de notas |
| Lista de peticiones vagas | Elegir las peticiones con las que se trabaja | [`datos/peticiones_vagas.csv`](datos/peticiones_vagas.csv) |
| Acta de una reunión comercial | Datos de la petición 1 | [`datos/acta_reunion.md`](datos/acta_reunion.md) |
| Reclamación por cobro duplicado | Datos de la petición 3 | [`datos/ticket_ejemplo.txt`](datos/ticket_ejemplo.txt) |
| Métricas del trimestre (opcional) | Datos de la petición 4 | [`datos/metricas_trimestre.csv`](datos/metricas_trimestre.csv) |
| Hoja de cálculo | Peticiones, diagnóstico, criterios cumplidos y totales calculados | [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) |
| Catálogo de planes de Altanoria (opcional) | Datos de las peticiones 7 y 10 | [`../comun/empresa/catalogo_planes.md`](../comun/empresa/catalogo_planes.md) |

Cómo abrir y copiar un fichero del laboratorio: al pulsar el enlace de la tabla se abre el fichero en el navegador. Si se muestra con formato, pulsar el botón «Raw» (arriba a la derecha) para ver el texto sin formato; después, seleccionarlo todo (Ctrl+A en Windows, Cmd+A en Mac) y copiarlo (Ctrl+C o Cmd+C). Quien haya descargado el repositorio puede abrir el fichero con el Bloc de notas o con TextEdit y copiar de la misma manera.

Antes de empezar, conviene comprobar tres cosas:

- Un asistente de chat en el que se puedan abrir conversaciones nuevas (normalmente con un botón «Nuevo chat»).
- Un documento de texto (Word, Google Docs, Notas…) y la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): el documento sirve para escribir los contratos, y la hoja para el diagnóstico y los criterios cumplidos.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: Marta, de La Espiga, escribe a un asistente «contesta a este cliente» y pega un mensaje: «Mi pedido del sábado llegó tarde y la tarta estaba blanda». Esto es lo que ocurre y cómo se arregla con un contrato de tarea.

Paso 1: diagnosticar qué falta. Se marca si cada elemento de un buen contrato está en la petición original.

| Elemento | ¿Está en «contesta a este cliente»? |
|---|---|
| Objetivo: para qué se usará | no |
| Destinatario: quién lo leerá | no |
| Tarea: qué hay que hacer exactamente | no |
| Datos de entrada | sí (el mensaje) |
| Formato de salida | no |
| Restricciones y límites | no |
| Qué hacer si falta información | no |
| Criterio de calidad | no |

Faltan 7 de 8 elementos.

Paso 2: probar la petición vaga. El asistente devuelve tres párrafos, promete un reembolso («le devolveremos el importe») y firma con un nombre inventado. Se contestan cinco comprobaciones de sí o no.

| Comprobación | Versión vaga |
|---|---|
| Hace lo que necesitaba la persona | no |
| Se puede usar sin retocar | no |
| No inventa ningún dato | no |
| Marca como «a confirmar» lo que no consta | no |
| Longitud y tono adecuados al destinatario | sí |

Cumple 1 de 5.

Pasos 3 a 5: el contrato. Se escribe en el documento de texto con las partes del contrato y se prueba en una conversación nueva.

```text
Eres el asistente de atención al cliente de La Espiga.
Objetivo: contestar a un cliente que se queja de un pedido.
Tarea: redacta la respuesta al cliente a partir del mensaje.
Datos: <mensaje> … </mensaje>
Formato: saludo, una frase que reconozca el problema, el siguiente paso y despedida. De 60 a 90 palabras, trato de tú.
Restricciones: no prometas reembolsos ni descuentos; no firmes con ningún nombre.
Si falta un dato (por ejemplo, la hora de entrega), escribe «a confirmar».
Calidad: respuesta clara que se pueda enviar sin retocar.
```

Paso 6: comparar la versión vaga con la del contrato con las mismas cinco comprobaciones.

| Comprobación | Vaga | Contrato |
|---|---|---|
| Hace lo que necesitaba la persona | no | sí |
| Se puede usar sin retocar | no | sí |
| No inventa ningún dato | no | sí |
| Marca como «a confirmar» lo que no consta | no | sí |
| Longitud y tono adecuados | sí | sí |
| Total | 1 | 5 |

Mejora: de 1 a 5 comprobaciones cumplidas.

Paso 7: robustez. Se borra del mensaje la mención del sábado y se repite. Se contestan tres preguntas: ¿respeta «a confirmar»? sí; ¿inventa una fecha? no; ¿hizo falta reforzar la línea? no.

Qué se espera ver en tu laboratorio: el mismo diagnóstico de 8 elementos, la tabla de cinco comprobaciones para la versión vaga y para el contrato, y la prueba de robustez, con peticiones de Altanoria.

## Pasos de ejecución

Los pasos están pensados para hacerse en orden. Cada uno explica qué hacer, qué se debería ver al terminarlo y qué hacer si algo no sale como se espera. Los pasos indican si lo que se anota va en el documento de texto o en una pestaña de la hoja. Como este laboratorio es de chat, ningún paso necesita código.

La regla de oro de todo el laboratorio: cada prueba se hace en una conversación nueva. Si se reutiliza una conversación, el asistente recuerda lo anterior y los resultados dejan de ser comparables.

### Paso 1 · Elegir las peticiones y diagnosticar qué falta (10 minutos)
El laboratorio trabaja con dos peticiones reales de empleados de Altanoria. Hay otras tres opcionales, para quien quiera más práctica (véase «Para seguir»).

1. Abrir un documento de texto nuevo, titulado «Laboratorio 02A · Mis resultados», donde escribir los contratos (las respuestas del asistente se quedan en el chat). Abrir también la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): recoge las peticiones, el diagnóstico y los criterios cumplidos.
2. En la pestaña «Peticiones» están las dos peticiones con las que se trabaja: la 1 (`hazme algo con el acta`, de Lucía Benavent, de Ventas, con el contenido de `acta_reunion.md`) y la 3 (`contesta a este cliente`, de Marta Illueca, de Soporte, con el contenido de `ticket_ejemplo.txt`). Los números son los de `peticiones_vagas.csv`, que tiene más peticiones: las demás son opcionales.
3. Leer en esa pestaña la columna «Necesidad real» de cada petición (viene de `peticiones_vagas.csv`): es lo que la persona quería de verdad y no supo expresar.

Antes de probar nada, se piensa qué le falta a cada petición. Este diagnóstico es la clave del laboratorio, porque después se comprueba si acertó.

4. Abrir la pestaña «Qué falta» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx). Tiene una tabla para cada petición, con los ocho elementos de un buen contrato: objetivo, destinatario, tarea, datos de entrada, formato de salida, restricciones y límites, qué hacer si falta información y criterio de calidad.
5. Rellenar cada fila con «sí» o «no» en la columna «¿Está en la petición original?». Ejemplo para la petición 1 («hazme algo con el acta»): en «Tarea», la respuesta es «no»: no se sabe si se quiere un resumen, un correo o una lista de acuerdos.

Comprobación: la pestaña «Peticiones» muestra las dos peticiones con su necesidad real y ambas tablas de «Qué falta» están completas (la hoja cuenta cuántos elementos faltan). Lo normal es que casi todas las filas tengan «no».

### Paso 2 · Probar las peticiones vagas (12 minutos)
Se envía al asistente cada petición tal cual, junto con los datos, para ver qué hace.

Para la petición 1:

1. Abrir una conversación nueva en el asistente.
2. Escribir exactamente `hazme algo con el acta`, sin añadir nada.
3. A continuación, en el mismo mensaje, pegar el contenido completo del fichero `acta_reunion.md` (el asistente no puede adivinar los datos).
4. Enviar el mensaje y esperar la respuesta.
5. Dejar la respuesta en el chat: se puntuará enseguida.

Repetir los mismos cinco pasos para la petición 3, con el texto `contesta a este cliente` y el contenido de `ticket_ejemplo.txt`.

Después, en la pestaña «Puntuación» de la hoja, contestar «sí» o «no» a los cinco criterios de la columna «Versión vaga» de cada petición (la pestaña «Criterios» dice cuándo se contesta «sí»). Para decidirlo, comprobar cada fecha, responsable y cifra de la respuesta contra el acta o el ticket.

Comprobación: las dos columnas «Versión vaga» tienen los cinco criterios contestados y la hoja muestra cuántos se cumplen. Si el asistente hizo un trabajo excelente, no pasa nada: la comparación con el contrato dirá cuánto mejora.

### Paso 3 · Entender la estructura de un contrato de tarea (6 minutos)
Un contrato de tarea tiene siempre la misma forma. Se lee esta plantilla, que se usará en el paso siguiente:

```text
Contexto y objetivo: [para qué se necesita y quién lo leerá]
Tarea: [verbo + resultado concreto]

<datos>
[pegar aquí los datos]
</datos>

Restricciones: [qué usar, qué no, límites de longitud, tono]
Si falta información: [qué debe hacer el modelo: «no consta», preguntar…]
Formato de salida: [estructura exacta y longitud]
Criterio de calidad: [cómo se sabrá que está bien]
```

Reglas de redacción que se aplican en todo el laboratorio:

- Un verbo de acción claro por instrucción («redacta», «resume», «calcula»), nunca «ayúdame con…».
- Instrucciones en positivo («usa solo…») antes que prohibiciones («no inventes…»), y ambas si hace falta.
- Datos delimitados con etiquetas y separados de las instrucciones.
- Sin relleno: cada línea debe resolver una ambigüedad concreta.
- Siempre se dice qué hacer si falta información.

Copiar la plantilla en el documento de resultados y escribir, junto a cada una de sus siete partes, una palabra propia que la resuma. La plantilla junta «objetivo» y «destinatario» en «Contexto y objetivo»: por eso son siete partes y no los ocho elementos del Paso 1.

Comprobación: la plantilla está en el documento y cada una de sus siete partes lleva una palabra propia.

### Paso 4 · Redactar el contrato de la petición 1 (19 minutos)
Se parte de un contrato casi escrito. Las partes marcadas como `[COMPLETAR]` se deciden aquí.

1. Abrir el documento de resultados y copiar el prompt de partida siguiente bajo el título «Petición 1 · contrato».

```text
Contexto y objetivo: [COMPLETAR: para qué se necesita el resultado y quién lo leerá]
Tarea: [COMPLETAR: verbo + resultado concreto]

<acta>
{pegar aquí el contenido de acta_reunion.md}
</acta>

Contenido que debe incluir: [COMPLETAR: apartados del resultado, p. ej. resumen, acuerdos y asuntos pendientes]
Restricciones: [COMPLETAR: qué fuente usar, qué no inventar, tono y trato]
Si falta información: [COMPLETAR]
Formato de salida: [COMPLETAR: estructura exacta y longitud]
Criterio de calidad: [COMPLETAR: comprobaciones concretas contra el acta]
```

2. Sustituir cada `[COMPLETAR: …]` por una frase propia. Para no empezar de cero, estas son las preguntas que cada campo debe responder:

| Campo | Pregunta que debe responder | Ejemplo de enfoque |
|---|---|---|
| Contexto y objetivo | ¿Para qué se usará el resultado y quién lo leerá? | Un correo de seguimiento para los asistentes de la reunión |
| Tarea | ¿Qué verbo y qué resultado concreto? | «Redacta el correo a partir del acta» |
| Contenido que debe incluir | ¿Qué apartados tiene el resultado? | Resumen en 3 frases, tabla de acuerdos, párrafo sobre lo pendiente |
| Restricciones | ¿Qué fuente se usa, qué no se inventa, qué tono? | Solo el acta; ninguna fecha ni cifra inventada; trato de tú |
| Si falta información | ¿Qué se escribe cuando un dato no consta? | «a confirmar» |
| Formato de salida | ¿Estructura y longitud exactas? | Asunto + cuerpo de 150 a 200 palabras + tabla |
| Criterio de calidad | ¿Qué se puede comprobar contra el acta? | Las cifras coinciden con el acta; aparecen todos los acuerdos |

3. Sustituir `{pegar aquí el contenido de acta_reunion.md}` por el contenido real del acta, manteniendo las etiquetas `<acta>` y `</acta>` a ambos lados.
4. Guardar el resultado en el documento bajo «Petición 1 · contrato».

Si te has atascado: el contrato de referencia está en [`datos/rescate/contrato_peticion1.txt`](datos/rescate/contrato_peticion1.txt). Sirve para poder seguir con los Pasos 6 y 7, y para compararlo con el propio; copiarlo sin leerlo quita sentido al paso.

Comprobación: no queda ningún `[COMPLETAR]` ni ninguna llave `{ }` en el contrato.

### Paso 5 · Redactar el contrato de la petición 3 (12 minutos)
Se hace lo mismo con la reclamación. En este caso, además, hay que decidir qué puede y qué no puede prometer el asistente, que es la parte delicada.

1. Copiar este prompt de partida bajo el título «Petición 3 · contrato»:

```text
Rol y tono: [COMPLETAR: quién responde y con qué tono y trato]
Tarea: [COMPLETAR: verbo + resultado concreto]

<reclamacion>
{pegar aquí el contenido de ticket_ejemplo.txt}
</reclamacion>
<condiciones_aplicables>
5.4. Las suscripciones mensuales no son reembolsables, salvo error de facturación imputable a Altanoria.
</condiciones_aplicables>

Restricciones: [COMPLETAR: qué se puede prometer y qué no, qué no mencionar]
Si el cliente pide algo que las condiciones no cubren: [COMPLETAR]
Formato de salida: [COMPLETAR: estructura del correo y longitud]
Criterio de calidad: [COMPLETAR]
```

2. Completar los campos con estas guías:
   - Rol y tono: quién contesta (un agente de atención al cliente de Altanoria), con qué trato (de usted) y con qué tono (empático y profesional).
   - Restricciones: qué se puede prometer (nada que no esté en las condiciones) y qué no. Conviene prohibir de forma explícita el reembolso o el abono, los plazos de cualquier tipo (incluidos los vagos: «inmediatamente», «en breve», «en las próximas horas»), decir de quién es la culpa del error y mencionar información interna. Lo que no se prohíbe de forma explícita, el asistente suele hacerlo.
   - Si el cliente pide algo que las condiciones no cubren: qué hace el asistente (decirlo con claridad y ofrecer derivar el caso a una persona).
   - Formato de salida: partes del correo (saludo, reconocimiento, qué hará Altanoria, siguiente paso, despedida) y número de palabras.
   - Criterio de calidad: qué debe aparecer (por ejemplo, el importe de los dos cargos) y qué no (promesas de fecha).
3. Sustituir `{pegar aquí el contenido de ticket_ejemplo.txt}` por el contenido real del ticket.

Si te has atascado: el contrato de referencia está en [`datos/rescate/contrato_peticion3.txt`](datos/rescate/contrato_peticion3.txt).

Comprobación: igual que en el paso anterior, no queda ningún `[COMPLETAR]` ni llave.

### Paso 6 · Probar los contratos y comparar con las versiones vagas (11 minutos)
Los cinco criterios son los mismos en las dos versiones (están en la pestaña «Criterios» de la hoja) y la hoja cuenta los que se cumplen.

1. Abrir una conversación nueva. Pegar el contrato completo de la petición 1 y enviarlo. Dejar la respuesta en el chat.
2. Abrir otra conversación nueva y hacer lo mismo con el contrato de la petición 3.
3. En la pestaña «Puntuación» de la hoja hay una tabla para cada petición. Se contesta «sí» o «no» a cada criterio en la columna «Versión contrato» (la columna «Versión vaga» se rellenó en el Paso 2).
4. En el documento de resultados, escribir una frase por cada mejora importante indicando qué línea del contrato la produjo (por ejemplo: «dejó de inventar fechas por la línea Si falta información: a confirmar»).

Comprobación: ambas tablas tienen los cinco criterios contestados en las dos versiones y se puede ver una diferencia a favor del contrato. Si no hay diferencia, revisar si en el contrato se dijo con claridad el formato y qué hacer si falta información.

### Paso 7 · Probar la robustez: ¿qué pasa si falta un dato? (10 minutos)
Un buen contrato debe aguantar que falten datos. Se comprueba con la petición 1, cuyo contrato incluye la línea «Si falta información».

1. Abrir una copia del acta (no modificar el fichero original). En el apartado 5 del acta, «Acuerdos y tareas», localizar la fila «Resolver las 19 facturas con CIF erróneo | Tomás Albors | 16 de octubre» y borrar el responsable y la fecha, de modo que quede «Resolver las 19 facturas con CIF erróneo | | ».
2. Abrir una conversación nueva y pegar el contrato de la petición 1, sustituyendo el acta por esta copia modificada.
3. Enviarlo y buscar en la respuesta la fila de las facturas con CIF erróneo. ¿Pone lo que se indicó en «Si falta información» (por ejemplo, «a confirmar») o se ha inventado un responsable o una fecha?
4. Anotar en la pestaña «Robustez» de la hoja qué ocurrió (tres preguntas de sí o no). Si el asistente inventó un dato pese a la instrucción, reforzar la línea así: «Está prohibido estimar un valor; si un dato no consta, escribe a confirmar», y repetir.

Para terminar, apuntar en el documento de texto, en una línea, los tres cambios que más mejoraron las respuestas a lo largo del laboratorio (por ejemplo, decir para qué se quiere el resultado, fijar el formato, indicar qué hacer si falta un dato): son lo que la directora de Soporte quería saber.

Comprobación: la pestaña «Robustez» dice si el asistente respetó la instrucción de datos ausentes y si hizo falta reforzarla.

## Conclusiones

### Qué se ha conseguido

Se ha comprobado con casos reales que la calidad de una respuesta depende, sobre todo, de lo bien definido que está el encargo. Con el mismo asistente y los mismos datos, la versión contractual suele dar un resultado más útil, más fácil de verificar y con menos datos inventados que la versión vaga. Y se tiene ya una guía propia, con ejemplos reales, que se puede aplicar a cualquier otra petición.

Referencia de qué esperar (rangos amplios; con otro asistente pueden variar): lo que más suele mejorar el resultado es definir el formato de salida y el tratamiento de los datos ausentes, además de delimitar los datos. Con la versión vaga, el asistente suele inventar decisiones (en el acta, sobre el precio, que no se discutió) o prometer cosas que no puede (en la reclamación, plazos de abono).

### Preguntas de reflexión

Conviene intentar responder antes de abrir cada respuesta.

1. ¿Qué elemento del contrato produjo la mayor mejora en cada caso?

   <details>
   <summary>Respuesta</summary>

   Depende del caso, pero lo que más suele mejorar el resultado es definir el formato de salida y el tratamiento de los datos ausentes («si no consta, indícalo»), además de delimitar los datos. En el acta, la audiencia y el formato; en la reclamación por cobro duplicado, las restricciones sobre lo que no se puede prometer.

   </details>

2. ¿Hay algún contrato que haya quedado demasiado largo? ¿Qué se puede eliminar sin perder precisión?

   <details>
   <summary>Respuesta</summary>

   Sí, cuando se acumulan reglas redundantes. Se pueden eliminar adjetivos, repeticiones del rol y criterios que repiten las restricciones. Se mantiene todo lo que reduce una ambigüedad concreta.

   </details>

3. ¿En qué peticiones basta una línea bien escrita y no merece la pena un contrato completo? (Véase [§1.5 Cuándo merece la pena estructurar un prompt](../../modulos/02-fundamentos-del-prompt-engineering/01-introduccion-que-es-prompt-engineering.md#15-cuándo-merece-la-pena-estructurar-un-prompt).)

   <details>
   <summary>Respuesta</summary>

   En tareas atómicas y de bajo riesgo: traducir un párrafo, reformular una frase o resumir un texto sin consecuencias. Si no hay datos sensibles, ni formato crítico, ni riesgo de inventar, una línea clara basta.

   </details>

4. ¿Qué diferencia hay entre «no inventes datos» y «si un dato no consta, escribe no consta»?

   <details>
   <summary>Respuesta</summary>

   «No inventes datos» es una prohibición general que no indica qué hacer en su lugar. «Si un dato no consta, escribe no consta» ofrece una salida válida para la ignorancia, más fácil de cumplir y de comprobar.

   </details>

### Autoevaluación

Esta lista sirve para valorar el propio trabajo (el laboratorio no se evalúa):

- [ ] Cada contrato tiene una tarea concreta con verbo de acción, no «ayúdame con…».
- [ ] Los datos están delimitados y no se mezclan con las instrucciones.
- [ ] Hay una instrucción explícita sobre qué hacer si falta información.
- [ ] El formato de salida está definido (estructura, longitud, tono).
- [ ] Hay criterios de calidad que se pueden verificar.
- [ ] Se comparó con la versión vaga con los mismos datos.
- [ ] Se probó al menos una vez la ausencia de un dato.

### Errores típicos

- Añadir adjetivos («de forma excelente y detallada») en lugar de criterios verificables.
- Pedir varias tareas distintas en un único prompt sin estructura.
- Escribir contratos tan largos que el verdadero objetivo queda enterrado.
- No poner nunca a prueba el contrato con datos incompletos.
- Reutilizar la misma conversación para varias pruebas, con lo que el asistente arrastra el contexto anterior.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Lo que se comprobó al probar este laboratorio

Los contratos de referencia se ejecutaron seis veces cada uno con Gemma 4 (8 B, en local con Ollama; temperatura 0,3; medición del 24 de noviembre de 2026) para comprobar sus criterios de calidad. Con el contrato de la petición 3, las seis respuestas tuvieron entre 80 y 150 palabras, mencionaron los dos cargos de 599,00 € y ninguna prometió reembolso, abono ni plazo ni atribuyó la causa del error. Una versión más débil, que solo decía «no prometas plazos concretos de abono» y «no atribuyas la causa del error», tampoco falló con este modelo (en una de las seis respuestas, un detector por palabras clave marcó «ha iniciado inmediatamente una revisión», que no es una promesa de abono ni de plazo): otros modelos sí han incumplido esas restricciones, y la única manera de saber si un contrato es suficiente es probarlo con el modelo que se va a usar. Con el contrato de la petición 1, al quitar el responsable y la fecha de un acuerdo del acta, el asistente escribió «a confirmar» en las seis pruebas y no inventó ningún dato. La lección es general: lo que el contrato no prohíbe de forma explícita, el asistente puede hacerlo, y la única manera de saberlo es probar.

### Defectos habituales de las respuestas a las peticiones vagas (Paso 2)

Con las peticiones sin contrato, estos son los defectos que suelen aparecer; sirven para comprobar las respuestas de los criterios «No inventa ningún dato» y «Se puede usar sin retocar»:

- Petición 1 («hazme algo con el acta»). El asistente elige por su cuenta qué hacer (un resumen genérico, sin tabla de acuerdos ni responsables); no sabe para quién escribe, así que el tono y la longitud no encajan; puede añadir decisiones o fechas que el acta no recoge (por ejemplo, sobre el precio); mezcla la discusión con lo acordado.
- Petición 3 («contesta a este cliente»). Suele prometer lo que no puede (reembolso, abono, un plazo, aunque sea vago como «en breve»); puede atribuir la causa del error a Altanoria o al cliente sin base; el tono es genérico y la respuesta, larga o con relleno; no remite a las condiciones aplicables.
- En las dos. Decisiones que nadie ha pedido (formato, longitud, tono) y ningún aviso de lo que se ha supuesto.

### Una palabra por parte de la plantilla (Paso 3)

Un ejemplo de la palabra que puede resumir cada parte (cada persona puede elegir otra): *Contexto y objetivo* → «para qué»; *Tarea* → «verbo»; *Datos* → «material»; *Restricciones* → «límites»; *Si falta información* → «salida»; *Formato de salida* → «forma»; *Criterio de calidad* → «comprobar».

### Contratos de referencia

No hay una única redacción correcta. Se ofrecen contratos de referencia para comparar con los propios, no para copiarlos.

<details>
<summary>Petición 1 · «hazme algo con el acta» (Ventas)</summary>

Diagnóstico: falta el objetivo (¿para qué?), la audiencia (director comercial y asistentes), el formato (resumen, tabla de acuerdos, correo), la longitud y la instrucción sobre datos ausentes.

```text
Eres un asistente de la Jefa de Ventas de Altanoria.
Objetivo: preparar un correo de seguimiento para los asistentes de la reunión.
Tarea: redacta el correo a partir del acta.

<acta>
...pegar el contenido de acta_reunion.md...
</acta>

Contenido: (1) resumen de resultados en 3 frases, (2) tabla con los acuerdos, responsable y fecha límite, (3) un párrafo sobre el asunto pendiente de precios.
Restricciones: usa solo la información del acta; no inventes fechas ni cifras; no incluyas la discusión sobre la clasificación P1/P2 salvo como tarea pendiente.
Si falta un dato (por ejemplo, un responsable o una fecha), escribe «a confirmar».
Formato: asunto del correo + cuerpo de 150 a 200 palabras + tabla de acuerdos. Tono profesional y cercano; trato de tú.
Calidad: todas las cifras coinciden con el acta; los cinco acuerdos aparecen con su responsable y fecha.
```

Qué suele mejorar: el modelo ya no inventa decisiones sobre el precio (el acta no tomó ninguna), mantiene el trato y devuelve la tabla.

</details>

<details>
<summary>Petición 3 · «contesta a este cliente» (Soporte)</summary>

Diagnóstico: falta qué se puede y qué no se puede prometer, el tono, la longitud, los datos (ticket y condiciones aplicables) y el siguiente paso para el cliente.

```text
Eres un agente de atención al cliente de Altanoria. Tratas de usted, con tono empático y profesional.
Tarea: redacta la respuesta a la reclamación del cliente.

<reclamacion>
...contenido de ticket_ejemplo.txt...
</reclamacion>
<condiciones_aplicables>
5.4. Las suscripciones mensuales no son reembolsables, salvo error de facturación imputable a Altanoria.
</condiciones_aplicables>

Restricciones: reconoce el problema en una frase; no prometas reembolso, abono ni plazos de ningún tipo (tampoco «inmediatamente», «en breve» ni «en las próximas horas»); no digas de quién es la culpa del error; indica solo que el caso se revisará y que una persona del equipo de facturación confirmará los pasos; no menciones información interna.
Si el cliente pide algo que las condiciones no cubren, dilo con claridad y ofrece derivarlo a una persona.
Formato: saludo, reconocimiento (1 frase), qué hará Altanoria (máximo 3 frases), qué debe hacer el cliente si procede, despedida. De 80 a 150 palabras.
Calidad: menciona los dos cargos de 599,00 €, no promete reembolso ni plazo de ningún tipo, no atribuye la causa del error, el siguiente paso es claro.
```

</details>

<details>
<summary>Peticiones opcionales 4, 7 y 10</summary>

Petición 4 · «analiza las métricas» (Producto). «Analizar» no es un resultado: falta el criterio de comparación, la audiencia y el formato.

```text
Tarea: a partir de la tabla de métricas, identifica TRES tendencias y propón UNA acción por tendencia.
Restricciones: cada tendencia debe citar los datos (producto, meses y valores); si una conclusión no se puede deducir de la tabla, indica «no se puede concluir con estos datos».
Formato: tabla con columnas Tendencia | Evidencia | Acción | Riesgo de interpretación.
Audiencia: director de Producto. Máximo 200 palabras.
```

Petición 7 · «escribe un correo» (Ventas). Faltan el objetivo, el destinatario, el tono, las cifras permitidas y el formato. El cliente es Álvaro Millán, de Distribuciones Marfil: prueba Altanoria Copilot Team desde hace 10 días con 24 usuarios y ha preguntado por el plan Enterprise.

```text
Eres un asistente de la Jefa de Ventas de Altanoria.
Contexto y objetivo: Álvaro Millán, de Distribuciones Marfil, prueba Altanoria Copilot Team desde hace 10 días con 24 usuarios y ha preguntado por el plan Enterprise. Se quiere proponerle una reunión de 30 minutos para comparar planes.
Tarea: redacta el correo de propuesta.

<catalogo>
...pegar catalogo_planes.md...
</catalogo>

Restricciones: usa solo precios y características del catálogo; no prometas descuentos ni fechas; recuerda que Enterprise exige un mínimo de 50 usuarios; trato de tú, tono cercano y profesional.
Si falta información (por ejemplo, cuántos usuarios necesitaría en Enterprise): no la supongas; pregúntala en el correo.
Formato: asunto de máximo 50 caracteres y cuerpo de 80 a 120 palabras con una sola llamada a la acción.
Calidad: la cifra de mínimo de usuarios y el precio coinciden con el catálogo; hay una pregunta sobre usuarios y una propuesta concreta de reunión.
```

Sin el contrato, el modelo suele inventar descuentos o plazos. Con él cita el mínimo de 50 usuarios (el cliente tiene 24, así que el correo debe señalarlo y orientar a Team o a una conversación).

Petición 10 · «calcula lo que debemos» (Facturación). Faltan los datos (plan actual, plan nuevo, usuarios, días restantes), las reglas (prorrata sobre 30 días, IVA) y el formato del cálculo.

```text
Calcula el importe a facturar por un cambio de plan a mitad de periodo.
Datos: <catalogo> ...pegar catalogo_planes.md... </catalogo>; plan actual: Team; plan nuevo: Enterprise; 60 usuarios; faltan 18 días del periodo.
Reglas: diferencia de precio por usuario × usuarios × días restantes / 30; después aplica el IVA del catálogo.
Muestra cada paso del cálculo. Si falta algún dato, no calcules y pregunta.
Formato: lista numerada de pasos y una línea final «Importe sin IVA / IVA / Total».
```

Resultado esperado: diferencia = 59 − 29 = 30 € por usuario; × 60 usuarios = 1.800 €; × 18/30 = 1.080,00 € sin IVA; IVA del 21 % = 226,80 €; total 1.306,80 €. (Enterprise exige un mínimo de 50 usuarios: con 12 el cálculo sería incoherente con el catálogo.)

</details>

Qué se espera del Paso 7: con la instrucción «si falta un dato, escribe a confirmar», un modelo bien dirigido escribe «a confirmar» en la fila incompleta en lugar de inventar un responsable o una fecha. Si lo inventa pese a la instrucción, hay que reforzarla («Está prohibido estimar el valor; si no consta, escribe a confirmar») y plantearse si la tarea necesita una comprobación externa.

### Criterios para valorar un buen contrato

- Una tarea, un resultado, un formato.
- Cada línea elimina una ambigüedad.
- Los datos están separados de las instrucciones.
- La ausencia de datos tiene tratamiento explícito.
- El criterio de calidad es comprobable (cifras que coinciden, cinco acuerdos presentes…).

</details>

### Para seguir

- Repetir los pasos 2 a 6 con las peticiones opcionales 4 («analiza las métricas», con `metricas_trimestre.csv`), 7 («escribe un correo», con `catalogo_planes.md`) y 10 («calcula lo que debemos», con `catalogo_planes.md`); los criterios cumplidos se anotan en la pestaña «Peticiones opcionales» de la hoja (cuenta cuántos de los cinco criterios cumple cada versión). En las peticiones 7 y 10, los datos del cliente no están en la petición: observar qué hace el asistente cuando falta información que ni la petición ni los datos adjuntos aportan.
- Redactar una guía de una página para los empleados con los tres errores más frecuentes, una plantilla de contrato reducida y un ejemplo de antes y después.
- Convertir los contratos en plantillas con variables (por ejemplo, un hueco para el acta) que se puedan reutilizar.
- Escribir una lista de comprobación de diez puntos para revisar cualquier prompt antes de enviarlo.
- Resolver las diez peticiones restantes de `peticiones_vagas.csv` y detectar qué patrón de ambigüedad se repite más.
- Continuar con el laboratorio [02B](../02B/README.md), donde se mide qué aporta cada componente de un prompt.

---

[← Laboratorios](../README.md) · [Módulo 02](../../modulos/02-fundamentos-del-prompt-engineering/README.md) · [← 01B](../01B/README.md) · [02B →](../02B/README.md)
