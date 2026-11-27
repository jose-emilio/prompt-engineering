[← Laboratorios](../README.md) · [Módulo 09](../../modulos/09-seguridad-privacidad-y-uso-responsable/README.md) · [← 08B](../08B/README.md) · [09B →](../09B/README.md)

# Laboratorio 09A · Minimizar y anonimizar antes de enviar datos a un modelo

Módulo 09 · Seguridad, privacidad y uso responsable · Duración estimada: 50 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Quitar o sustituir los datos personales de unos expedientes antes de enviarlos a un asistente y redactar una norma interna de uso. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Inventario de datos (5 min)
- Paso 2 · Decidir qué se hace con cada dato (6 min)
- Paso 3 · Aplicar el tratamiento (8 min)
- Paso 4 · Comprobar que no ha quedado nada (7 min)
- Paso 5 · Verificar con la lista correcta (5 min)
- Paso 6 · Comprobar que la tarea sigue siendo posible (7 min)
- Paso 7 · Redactar la norma interna (12 min)

<details>
<summary>Secciones del módulo relacionadas (9)</summary>

- [§1.2 Privacidad y datos personales](../../modulos/09-seguridad-privacidad-y-uso-responsable/01-amenazas-y-privacidad.md#12-privacidad-y-datos-personales)
- [§1.3 Qué no introducir en prompts](../../modulos/09-seguridad-privacidad-y-uso-responsable/01-amenazas-y-privacidad.md#13-qué-no-introducir-en-prompts)
- [§1.4 Minimización y anonimización](../../modulos/09-seguridad-privacidad-y-uso-responsable/01-amenazas-y-privacidad.md#14-minimización-y-anonimización)
- [§1.5 Gobernanza de uso](../../modulos/09-seguridad-privacidad-y-uso-responsable/01-amenazas-y-privacidad.md#15-gobernanza-de-uso)
- [§3.1 Fugas de información](../../modulos/09-seguridad-privacidad-y-uso-responsable/03-fugas-permisos-y-pruebas-de-seguridad.md#31-fugas-de-información)
- [§4.1 Uso responsable y supervisión](../../modulos/09-seguridad-privacidad-y-uso-responsable/04-responsabilidad-normativa-y-cierre.md#41-uso-responsable-y-supervisión)
- [§4.2 Marco normativo y estándares de referencia](../../modulos/09-seguridad-privacidad-y-uso-responsable/04-responsabilidad-normativa-y-cierre.md#42-marco-normativo-y-estándares-de-referencia)
- [§4.5 Transparencia y trazabilidad](../../modulos/09-seguridad-privacidad-y-uso-responsable/04-responsabilidad-normativa-y-cierre.md#45-transparencia-y-trazabilidad)
- [§4.6 Evaluación de riesgos](../../modulos/09-seguridad-privacidad-y-uso-responsable/04-responsabilidad-normativa-y-cierre.md#46-evaluación-de-riesgos)

</details>

## Justificación del laboratorio

Recursos Humanos, Soporte y el área Legal de Altanoria quieren usar un asistente de IA para redactar resúmenes, respuestas y acuses de recibo a partir de expedientes: bajas médicas, reclamaciones de clientes, evaluaciones de desempeño y solicitudes de acceso a datos. La Responsable de Seguridad y Cumplimiento, Inés Calatayud, ha puesto una condición clara: ningún dato personal innecesario puede salir de la empresa, y el asistente es un servicio externo.

Un nombre, un DNI o un diagnóstico enviados por error a un servicio externo no se pueden recuperar. La solución profesional no es dejar de usar el asistente, sino aplicar minimización: enviar solo los datos que la tarea necesita, sustituyendo el resto por marcadores (seudonimización) y guardando la tabla de equivalencias aparte para poder reinsertar los datos al final. Hay que decidir dato por dato qué se elimina, qué se seudonimiza, qué se generaliza y qué se conserva; aplicar el tratamiento; comprobar que no ha quedado nada importante; y verificar que la tarea sigue siendo posible con el texto tratado.

Una herramienta automática ayuda con los datos estructurados (DNI, IBAN, correo, teléfono), pero no detecta nombres ni diagnósticos ni circunstancias personales, que exigen revisión humana. Este laboratorio recorre el proceso completo con ocho expedientes ficticios y termina con una norma interna.

## Objetivos

Preparar documentos que contienen datos personales y datos especialmente sensibles para poder usar un modelo de lenguaje con ellos sin exponer información innecesaria: decidir qué se elimina, qué se seudonimiza y qué se conserva, aplicar el tratamiento, comprobar que la tarea sigue siendo posible y redactar una norma interna de una página.

> **Importante.** Todos los datos de este laboratorio son sintéticos: nombres, DNI, IBAN, teléfonos y diagnósticos son inventados. Pero el procedimiento es el que se aplicaría con datos reales. **No se debe practicar con datos reales de personas** sin la base legal, la autorización y las garantías que correspondan.

Al terminar el laboratorio se habrá conseguido:

- Reconocer datos personales, identificadores directos e indirectos y categorías especiales (salud, vida privada).
- Aplicar el principio de minimización: enviar solo lo necesario para la tarea.
- Distinguir anonimización (irreversible) de seudonimización (reversible con una clave guardada aparte).
- Verificar el resultado con una herramienta automática y con revisión humana, y entender los límites de ambas.
- Redactar reglas prácticas de uso de modelos con datos de clientes y empleados.

Conceptos que se usan:

- **Dato personal**. Cualquier información sobre una persona identificada o identificable: nombre, DNI, correo, teléfono, IBAN, dirección, fecha de nacimiento, e incluso combinaciones de datos que permiten reconocerla.
- **Categorías especiales**. Datos de salud, vida sexual, creencias, afiliación sindical, etc. Exigen garantías reforzadas. Un diagnóstico médico o la mención de un divorcio entran aquí.
- **Minimización**. Solo se usa el dato necesario para el fin. Si la tarea es «resumir el calendario de cobertura», el diagnóstico no hace falta.
- **Seudonimización**. Sustituir identificadores por marcadores (`[PERSONA_1]`, `[DNI_1]`) y conservar la tabla de correspondencia en un lugar seguro y separado. Permite recuperar los datos en la respuesta final, pero el texto sigue siendo dato personal para la ley.
- **Anonimización**. Eliminar o generalizar de forma que la persona no sea identificable ni siquiera con información adicional. Es difícil de lograr de verdad: los datos indirectos pueden reidentificar.

## Recursos necesarios

- Un editor de texto. Opcionalmente, Python 3.9 o superior y un asistente de chat.
- Datos: [`datos/expedientes.json`](datos/expedientes.json): 8 expedientes sintéticos (bajas médicas, reclamaciones de clientes, evaluaciones de desempeño y solicitudes de acceso RGPD), cada uno con la tarea posterior que se quiere hacer con un modelo.
- Script: [`detectar_pii.py`](detectar_pii.py) (detecta DNI, NIE, IBAN, correo, teléfono, fechas largas y códigos postales mediante expresiones regulares).
- Para el camino con chat, [`detector.html`](detector.html): una página que se abre en el navegador y hace lo mismo que `detectar_pii.py` con el texto pegado.
- El fichero [`datos/pii_gold.jsonl`](datos/pii_gold.jsonl) contiene los datos personales realmente presentes en cada expediente. Usarlo solo en el Paso 5, para verificar.
- Hoja de cálculo: [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), para el inventario de datos personales y las decisiones, la tabla de correspondencia (que no se envía al asistente), la verificación y la comprobación de la tarea posterior.
- Documentos de Altanoria: [`politica_privacidad.md`](../comun/empresa/politica_privacidad.md).

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: una clienta de La Espiga escribe una queja y el equipo de calidad quiere que un asistente la resuma. El mensaje: «Soy Lola Pérez (tel. 600 123 456, calle Mayor 12). Soy celíaca y la barra llevaba gluten. Llamadme, por favor. Gracias, Lola». La tarea posterior es resumir el problema para el equipo de calidad.

Pasos 1 y 2: inventario y decisión. Para cada dato personal se anota su tipo, si hace falta para la tarea y qué se hace con él.

| Dato | Tipo | ¿Necesario para resumir? | Decisión |
|---|---|---|---|
| Lola Pérez (firma) | identificador directo | no | seudonimizar |
| Lola (despedida) | identificador directo | no | seudonimizar |
| 600 123 456 | identificador directo | no | eliminar |
| Calle Mayor 12 | identificador indirecto | no | eliminar |
| Celíaca | categoría especial (salud) | sí, es el motivo de la queja | generalizar a «intolerancia alimentaria» |

Paso 3: aplicar el tratamiento. El texto que se envía al asistente es: «Soy [PERSONA_1]. Tengo una intolerancia alimentaria y la barra llevaba un ingrediente al que soy intolerante. Llamadme, por favor. Gracias, Lola». La tabla de correspondencia («[PERSONA_1] = Lola Pérez») se guarda en un documento aparte y no se envía nunca.

Paso 4: comprobar que no ha quedado nada. Se pasa el texto por el detector de datos personales y se anota lo que queda.

| Medida | Resultado |
|---|---|
| Datos personales que siguen a la vista | 1 («Lola», en la despedida) |
| De ellos, los que detecta la herramienta | 0 |

El detector encuentra teléfonos, DNI, IBAN, correos y fechas, pero no los nombres propios: la revisión humana es insustituible.

Paso 5: verificar con la lista correcta.

| Medida | Resultado |
|---|---|
| Datos personales presentes | 5 |
| Sin tratar | 1 (el nombre de la despedida) |
| Proporción sin tratar | 20 % |

Paso 6: ¿sigue siendo posible la tarea? Se comprueban tres cosas con el texto tratado: ¿basta la información que queda para resumir? sí; ¿el resultado contiene algún dato que no debería? no; ¿se puede reinsertar el nombre con la tabla? sí. La tarea sigue siendo posible.

Qué se espera ver en tu laboratorio: lo mismo con tres expedientes de Altanoria, con su inventario, su tabla de correspondencia fuera de la hoja y la comparación con la lista correcta.

## Pasos de ejecución

Los pasos se hacen en orden. Camino con chat: se trabaja con una muestra de tres expedientes (EXP-01, EXP-02 y EXP-03) copiada en un editor de texto y se sustituye a mano con «buscar y reemplazar». Camino con código: se usan los scripts de seudonimización y de detección. En todos los casos, se trabaja solo con datos ficticios; nunca con datos reales.

### Paso 1 · Inventario de datos (5 minutos)
1. Abrir [`datos/muestra_chat.md`](datos/muestra_chat.md): contiene tres expedientes (EXP-01, baja médica; EXP-02, reclamación de cliente; EXP-03, evaluación de desempeño). La lista de datos personales realmente presentes está al final, plegada: no abrirla todavía. (Los ocho expedientes completos están en [`datos/expedientes.json`](datos/expedientes.json).)
2. Para cada expediente, listar en la pestaña «Inventario y decisiones» de la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) los datos personales que contiene, una fila por dato, clasificados en cuatro tipos (lista desplegable):
   - Identificadores directos: nombre, DNI, correo, teléfono, IBAN.
   - Identificadores indirectos: dirección, fecha de nacimiento, código postal, cargo, equipo.
   - Datos de categoría especial: salud, vida privada.
   - Datos de negocio no personales: importes, fechas de cargos.

Comprobación: la pestaña tiene los datos de cada expediente, cada uno en su tipo.

### Paso 2 · Decidir qué se hace con cada dato (6 minutos)
1. Cada expediente trae una tarea posterior (por ejemplo, «resumir para RR. HH. el calendario de cobertura del equipo durante la baja»). Leerla: determina qué datos hacen falta.
2. Rellenar, en las columnas de la misma pestaña, la decisión de cada dato y expediente: si es necesario para la tarea (sí o no) y qué se hace con él. Ejemplos:

| Dato | ¿Necesario para la tarea? | Decisión | Razón (no se anota en la hoja) |
|---|---|---|---|
| (por ejemplo) DNI | No | Eliminar | La tarea no requiere identificar a la persona |
| (por ejemplo) Nombre | Sí | Seudonimizar | Se sustituye por un marcador y se reinserta después |

Las decisiones posibles son: eliminar, seudonimizar, generalizar (por ejemplo, la edad en lugar de la fecha de nacimiento) y conservar.

Comprobación: cada dato del inventario tiene su «necesario» y su decisión, y la hoja cuenta cuántos datos hay de cada decisión y que no queda ninguno sin decisión.

### Paso 3 · Aplicar el tratamiento (8 minutos)
1. Copiar cada expediente de la muestra en un editor de texto nuevo (uno por expediente).
2. Aplicar las decisiones del Paso 2 con «buscar y reemplazar» (Ctrl+H en Word y en muchos editores): por ejemplo, sustituir el DNI por `[DNI_1]`, el IBAN por `[IBAN_1]`, el nombre por `[PERSONA_1]`, y eliminar o generalizar lo que se decidió.
3. Anotar en un documento de texto aparte (no en la hoja) qué marcador sustituye a qué dato real. Esta tabla de correspondencia se guarda separada del texto tratado y nunca se envía al asistente: no copiarla nunca al chat.

<details>
<summary>Con código: seudonimizar los datos estructurados de forma automática</summary>

Abrir una terminal en la carpeta `laboratorios/09A` y ejecutar:

```bash
python seudonimizar.py --ids EXP-01 EXP-02 EXP-03
```

Se crean dos ficheros: `expedientes_tratados.json` (los textos con marcadores como `[DNI_1]`) y `tabla_correspondencia.json` (que debe guardarse **aparte del texto tratado**). El script solo trata los datos estructurados (DNI, IBAN, correo y teléfono): los nombres, direcciones, fechas de nacimiento y datos de salud hay que revisarlos y tratarlos a mano, y esa es la parte del ejercicio.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: hay una versión tratada de cada expediente y una tabla de correspondencia en un documento aparte.

### Paso 4 · Comprobar que no ha quedado nada (7 minutos)
Camino con chat: pegar el texto tratado de un expediente en una conversación nueva con este prompt, que pide al asistente que liste los datos personales que ve. Es una forma de comprobar cuánto queda a la vista (con datos ficticios):

```text
Lista todos los datos personales y de categoría especial que aparecen en el siguiente texto, indicando el tipo de cada uno (nombre, DNI, correo, teléfono, IBAN, dirección, fecha de nacimiento, salud, vida privada). No añadas datos que no estén en el texto.

<texto>
{pegar el expediente}
</texto>
```

Además del asistente, abrir [`detector.html`](detector.html) con doble clic (se abre en el navegador y no envía nada a ningún sitio), pegar el texto tratado y pulsar «Buscar datos personales»: lista los DNI, NIE, IBAN, correos, teléfonos, fechas completas y códigos postales que siguen a la vista. Es lo mismo que hace el detector del camino con código.

Camino con código:

<details>
<summary>Con código: usar el detector</summary>

En la terminal, en la carpeta `laboratorios/09A`:

```bash
python detectar_pii.py --json expedientes_tratados.json
```

(El fichero tratado debe tener el mismo formato que `expedientes.json`: una lista de objetos con `id` y `texto`.) El detector busca DNI, NIE, IBAN, correo, teléfono, fechas largas y códigos postales con expresiones regulares.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

El detector y el asistente no sustituyen a una lectura propia: no encuentran con fiabilidad nombres, direcciones ni datos de salud o de vida privada. Antes de seguir, leer el texto tratado de cada expediente entero buscando a ojo esos tres tipos de dato.

Anotar en la pestaña «Datos que quedan», por expediente, cuántos datos personales siguen a la vista, cuántos de ellos detecta la herramienta (o el asistente) y si tu lectura ha encontrado algún nombre, dirección o dato de salud (sí o no). La hoja calcula la proporción detectada. Un expediente no se da por anonimizado mientras haya un «sí» en esa última columna.

Comprobación: la pestaña «Datos que quedan» tiene los tres datos de cada expediente tratado.

### Paso 5 · Verificar con la lista correcta (5 minutos)
Abrir ahora la lista de datos personales presentes: en la pestaña «Verificación», mostrar las columnas ocultas con el botón «+» (la lista también está plegada al final de la muestra; `pii_gold.jsonl` en el conjunto completo). Compararla con el texto tratado y marcar cuáles han quedado sin tratar; la hoja calcula cuántos son. Contestar también, para cada dato sin tratar, si lo detecta la herramienta.

Comprobación: hay un recuento de datos sin tratar y la hoja muestra la proporción sin tratar.

### Paso 6 · Comprobar que la tarea sigue siendo posible (7 minutos)
Con cada versión tratada, abrir una conversación nueva y ejecutar la tarea posterior del expediente con este prompt:

```text
Usa el texto de abajo, en el que los datos personales se han sustituido por marcadores como [DNI_1] o [PERSONA_1]. Realiza la tarea indicada sin intentar adivinar ni reconstruir los datos sustituidos, y mantén los marcadores tal cual en la respuesta.

Tarea: {tarea_posterior del expediente}

<texto>
{pegar el texto tratado}
</texto>
```

Comprobar tres cosas y anotarlas en la pestaña «Tarea posterior»: ¿basta la información conservada para hacer la tarea?, ¿el resultado contiene algún dato que no debería (el modelo inventa un nombre, repite un marcador mal)?, ¿es posible reinsertar los datos reales en la respuesta con la tabla de correspondencia?

Comprobación: la pestaña «Tarea posterior» indica, por expediente, si la tarea sigue siendo posible.

### Paso 7 · Redactar la norma interna (12 minutos)
Escribir una norma de una página con esta plantilla, completando cada punto:

```text
NORMA INTERNA · Uso de asistentes de IA con datos de personas
1. Prohibido introducir: ...
2. Antes de enviar cualquier texto: minimizar, seudonimizar, ... 
3. La tabla de correspondencia se guarda ...
4. Excepciones: solo con autorización de ... y registro.
5. Si se envía un dato por error: ...
6. Revisión de la norma: ...
```

Dos puntos de ejemplo, ya escritos, para ver el nivel de detalle que se espera (se pueden adaptar):

- «1. Prohibido introducir: nombres completos, DNI, IBAN, direcciones, datos de salud y cualquier dato de menores, en cualquier asistente externo».
- «5. Si se envía un dato por error: avisar el mismo día a [persona o cargo responsable], anotarlo en el registro de incidentes y pedir al proveedor que borre la conversación si lo permite».

La norma debe responder: qué datos no se pueden introducir nunca en un asistente externo, qué se seudonimiza, cómo se guarda la correspondencia, quién autoriza excepciones, cómo se comprueba antes de enviar y qué hacer si se envía un dato por error (notificación y registro).

Comprobación: la norma tiene los seis puntos y nombra un responsable para las excepciones.

## Conclusiones

### Qué se ha conseguido

Se ha seguido el proceso completo de minimización de datos: inventario, decisión dato por dato, tratamiento, comprobación, verificación contra la lista correcta y comprobación de que la tarea sigue siendo posible. Lo más importante es lo que se escapa: las herramientas automáticas tratan bien los datos estructurados (DNI, IBAN, correo, teléfono) pero no los nombres, los diagnósticos ni las circunstancias personales, que requieren revisión humana. La norma interna que se redacta convierte la experiencia en reglas que cualquier empleado puede seguir antes de enviar un texto a un servicio externo.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué tipos de dato no detecta una herramienta basada en patrones? ¿Cómo se cubren?

   <details>
   <summary>Respuesta</summary>

   Nombres, circunstancias, diagnósticos y datos indirectos. Se cubren con listas, modelos de reconocimiento de entidades y revisión humana.

   </details>

2. ¿Es suficiente reemplazar los nombres para considerar anonimizado un texto? ¿Qué otros datos permiten identificar?

   <details>
   <summary>Respuesta</summary>

   No: dirección, fecha de nacimiento, cargo y circunstancias pueden identificar a la persona incluso sin nombre.

   </details>

3. ¿Qué diferencia legal y práctica hay entre seudonimizar y anonimizar?

   <details>
   <summary>Respuesta</summary>

   Seudonimizar mantiene el vínculo con la persona (sigue siendo dato personal); anonimizar lo rompe de forma irreversible. Anonimizar de verdad es difícil.

   </details>

4. ¿Qué ocurre con los datos si el proveedor del modelo los conserva para mejorar su servicio? ¿Qué debe comprobarse en el contrato?

   <details>
   <summary>Respuesta</summary>

   Pueden quedar fuera del control de la empresa y de los derechos de las personas. Hay que comprobar retención, uso para entrenamiento, ubicación y subencargados.

   </details>

5. ¿Cuándo es preferible no usar un asistente externo y usar un modelo alojado en la propia infraestructura?

   <details>
   <summary>Respuesta</summary>

   Cuando los datos sean muy sensibles o la normativa exija que no salgan de la organización.

   </details>

### Autoevaluación

- [ ] El inventario incluye identificadores directos, indirectos y de categoría especial.
- [ ] Cada decisión está justificada por la tarea posterior, no por costumbre.
- [ ] Los datos de salud y vida privada no salen en los textos tratados salvo que sean imprescindibles (y en ese caso se justifica).
- [ ] La tabla de correspondencia se guarda separada.
- [ ] Se comprobó el resultado con la herramienta y con revisión humana.
- [ ] Se verificó que la tarea posterior sigue siendo posible.
- [ ] La norma indica el procedimiento ante un envío erróneo.

### Errores típicos

- Tachar solo los nombres.
- Dejar el diagnóstico “porque es el contexto”.
- Guardar la tabla de correspondencia junto al texto tratado.
- Confiar en que la herramienta lo detecta todo.
- No comprobar que la tarea posterior sigue siendo posible.
- Practicar con datos reales.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Inventario y decisión por tipo de dato

| Tipo de dato | Ejemplo en los expedientes | Decisión general |
|---|---|---|
| Nombre completo de empleado o cliente | «Javier Millán Navarro» | Seudonimizar si hay que dirigirse a la persona (`[PERSONA_1]`); eliminar si la tarea es agregada (calendarios, estadísticas). |
| DNI / NIE | `79554736J` | Eliminar (casi nunca es necesario para redactar o resumir). |
| IBAN | `ES00 …` | Eliminar (si la tarea es una reclamación de cargo, basta «cuenta del cliente»). |
| Correo y teléfono | `julia.bosch@…`, `+34 6xx…` | Eliminar; si hay que contestar, el envío lo hace el sistema, no el modelo. |
| Dirección y código postal | Calle, número, 46001 | Eliminar; generalizar a la provincia solo si es necesario. |
| Fecha de nacimiento | «25 de enero de 1994» | Generalizar (rango de edad) o eliminar. |
| Diagnóstico (categoría especial) | «un episodio de ansiedad» | Eliminar: la tarea de calendario de cobertura solo necesita fechas y duración. |
| Circunstancia personal (divorcio) | «atravesando un divorcio» | Eliminar; si la tarea es resumir fortalezas, no hace falta. Si hay que registrar la petición de flexibilidad, expresarla sin el motivo. |
| Importes y fechas del cargo | «120,50 €», «16 de enero» | Conservar (datos de negocio necesarios). |
| Médico o terceros | Nombre del facultativo | Eliminar (tercero ajeno a la tarea). |

### Ejemplo de tratamiento

Original:
«El empleado Javier Millán Navarro (DNI 79554736J) causó baja el 1 de febrero de 2026 por un episodio de ansiedad. El parte lo ha emitido su médico de cabecera, Gonzalo Carrasco Lozano. Se prevé una duración de 14 días.»

Tratado para la tarea «resumir el calendario de cobertura del equipo»:
«El empleado [PERSONA_1] causó baja el 1 de febrero de 2026. Se prevé una duración de 14 días.»

(El diagnóstico, el DNI y el nombre del médico se eliminan; el nombre del empleado se seudonimiza o incluso se omite.)

### Función orientativa de seudonimización

```python
import re

PATRONES = {
    "DNI": r"\b\d{8}[A-HJ-NP-TV-Z]\b",
    "IBAN": r"\bES\d{2}(?:\s?\d{4}){5}\b",
    "EMAIL": r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b",
    "TEL": r"(?<!\d)(?:\+34\s?)?[6-9]\d{2}[\s.-]?\d{3}[\s.-]?\d{3}(?!\d)",
}

def seudonimizar(texto, nombres_conocidos=()):
    tabla, contadores = {}, {}
    def reemplazo(tipo):
        def f(m):
            contadores[tipo] = contadores.get(tipo, 0) + 1
            marca = f"[{tipo}_{contadores[tipo]}]"
            tabla[marca] = m.group(0)
            return marca
        return f
    for tipo, pat in PATRONES.items():
        texto = re.sub(pat, reemplazo(tipo), texto)
    for i, n in enumerate(nombres_conocidos, 1):      # los nombres requieren una lista o un modelo de reconocimiento
        marca = f"[PERSONA_{i}]"
        if n in texto:
            tabla[marca] = n
            texto = texto.replace(n, marca)
    return texto, tabla
```

La tabla devuelta se guarda aparte (cifrada o en un sistema con permisos), y se usa para reinsertar los datos en la respuesta final.

### Comprobar que la tarea sigue siendo posible (Paso 6)

Con el expediente tratado del ejemplo anterior y la tarea «resumir el calendario de cobertura del equipo», las tres comprobaciones salen así:

- ¿Basta la información conservada? Sí: la tarea necesita la fecha de la baja y su duración, y ambas se conservan. Si se hubiera eliminado una fecha, la tarea ya no sería posible y habría que conservarla (por ejemplo, generalizada) o cambiar la tarea.
- ¿El resultado contiene algo que no debería? Se comprueba que el modelo no invente un nombre para `[PERSONA_1]`, que no intente adivinar el diagnóstico eliminado y que respete el marcador tal cual. Si lo cambia o lo reconstruye, hay que reforzar la instrucción («no intentes reconstruir los datos sustituidos»).
- ¿Se pueden reinsertar los datos reales? Sí, con la tabla de correspondencia, que se guarda aparte: `[PERSONA_1]` se sustituye por el nombre real en la respuesta final, fuera del asistente. Para un calendario agregado ni siquiera hace falta reinsertar el nombre.

### Qué escapa a la herramienta

| Tipo | ¿Lo detecta `detectar_pii.py`? | Cómo se cubre |
|---|---|---|
| DNI, IBAN, correo, teléfono con formato estándar | Sí | Sustitución automática |
| Nombres de personas | No | Lista de nombres conocidos, reconocimiento de entidades y revisión humana |
| Direcciones | Parcialmente (código postal) | Revisión humana |
| Diagnósticos y circunstancias personales | No | Revisión humana y regla «eliminar categoría especial» |
| Datos indirectos (cargo + equipo + fecha) | No | Principio de minimización, generalización |

Normalmente, tras aplicar solo la herramienta, quedan nombres, direcciones y datos de salud: eso es lo que muestra la verificación con el gold.

### Norma interna de ejemplo

1. Prohibido introducir en un asistente externo: documentos de identidad, IBAN, datos de salud o de vida privada, y datos de clientes sin acuerdo de encargo de tratamiento.
2. Antes de enviar cualquier texto con datos de personas: minimizar, seudonimizar los identificadores, pasar la herramienta de comprobación y revisar a mano.
3. La tabla de correspondencia se guarda cifrada, separada del texto y con acceso restringido.
4. Excepciones solo con autorización de la Responsable de Seguridad y Cumplimiento y registro.
5. Envío erróneo: avisar de inmediato a Seguridad, registrar el contenido enviado, el proveedor y la hora, y valorar la notificación a la autoridad y a los afectados.
6. Revisión trimestral de la norma y de los acuerdos con proveedores (retención, uso para entrenamiento, ubicación de los datos).

</details>

### Para seguir

- Escribir una función que genere automáticamente marcadores consistentes (`[PERSONA_1]`, `[PERSONA_2]`) y la tabla de correspondencia, y que reinserte los datos en una respuesta.
- Probar la herramienta con variantes de formato (DNI con espacios o guiones, teléfonos con puntos) y mejorar los patrones.
- Evaluar qué parte del trabajo puede hacer un modelo local para detectar nombres y datos de salud.

---

[← Laboratorios](../README.md) · [Módulo 09](../../modulos/09-seguridad-privacidad-y-uso-responsable/README.md) · [← 08B](../08B/README.md) · [09B →](../09B/README.md)
