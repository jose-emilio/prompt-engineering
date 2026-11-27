[← Laboratorios](../README.md) · [Módulo 05](../../modulos/05-roles-personas-y-comportamiento/README.md) · [← 04B](../04B/README.md) · [05B →](../05B/README.md)

# Laboratorio 05A · Un mismo contenido, tres audiencias

Módulo 05 · Roles, personas y comportamiento · Duración estimada: 50 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Adaptar una misma cláusula contractual a tres audiencias y comprobar que se mantienen los hechos, el tono y la longitud. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Leer la cláusula y los tres perfiles (6 min)
- Paso 2 · Preparar el prompt base (6 min)
- Paso 3 · Generar las tres versiones (16 min)
- Paso 4 · Evaluar con comprobaciones de sí o no (7 min)
- Paso 5 · Comprobar la consistencia cruzada (4 min)
- Paso 6 · Cambiar solo una variable (5 min)
- Paso 7 · Probar el control de longitud (6 min)

<details>
<summary>Secciones del módulo relacionadas (7)</summary>

- [§2.1 Audiencia destinataria: adaptar la respuesta al lector](../../modulos/05-roles-personas-y-comportamiento/02-audiencia-tono-y-estilo.md#21-audiencia-destinataria-adaptar-la-respuesta-al-lector)
- [§2.2 Tono y formalidad: controlar el registro comunicativo](../../modulos/05-roles-personas-y-comportamiento/02-audiencia-tono-y-estilo.md#22-tono-y-formalidad-controlar-el-registro-comunicativo)
- [§2.3 Estilos de escritura: técnico, divulgativo y ejecutivo](../../modulos/05-roles-personas-y-comportamiento/02-audiencia-tono-y-estilo.md#23-estilos-de-escritura-técnico-divulgativo-y-ejecutivo)
- [§2.4 Voz y consistencia: mantener la identidad comunicativa](../../modulos/05-roles-personas-y-comportamiento/02-audiencia-tono-y-estilo.md#24-voz-y-consistencia-mantener-la-identidad-comunicativa)
- [§3.1 Profundidad y nivel de detalle](../../modulos/05-roles-personas-y-comportamiento/03-profundidad-comportamiento-y-asistentes.md#31-profundidad-y-nivel-de-detalle)
- [§3.2 Control de longitud: solicitar la extensión útil](../../modulos/05-roles-personas-y-comportamiento/03-profundidad-comportamiento-y-asistentes.md#32-control-de-longitud-solicitar-la-extensión-útil)
- [§4.8 Roles y formatos: separar perspectiva y presentación](../../modulos/05-roles-personas-y-comportamiento/04-tecnicas-avanzadas-errores-y-sintesis.md#48-roles-y-formatos-separar-perspectiva-y-presentación)

</details>

## Justificación del laboratorio

Altanoria tiene que explicar las exclusiones y los créditos de su acuerdo de nivel de servicio (SLA) a tres públicos muy distintos: un cliente que ha sufrido una caída y pregunta qué le corresponde, un agente comercial que debe explicarlo por teléfono sin prometer de más y el jurista de un cliente Enterprise que revisa el contrato. El contenido es el mismo; lo que cambia es todo lo demás: el vocabulario, el tono, la longitud y el formato.

Pedirle a un asistente de IA que «lo explique» sin más produce un texto genérico que no sirve del todo a nadie. Adaptar el mensaje a la audiencia es una de las habilidades más rentables del prompting, pero tiene un riesgo: cuando se simplifica o se formaliza un texto, el asistente puede omitir un dato, cambiar una cifra o inventar una promesa. Una versión «muy clara» que dice algo distinto del contrato es peor que una versión difícil.

Este laboratorio enseña a controlar el tono, el registro, la profundidad y la longitud sin alterar los hechos, y a comprobarlo con preguntas de sí o no: unas miden si la adaptación ha funcionado (formato, tono, utilidad) y otras miden la fidelidad (si siguen estando los cinco hechos del original). La directora de Soporte quiere tres textos coherentes entre sí.

## Objetivos

Adaptar un mismo contenido a tres audiencias distintas (cliente no técnico, agente comercial y jurista) controlando tono, registro, estilo, profundidad y longitud, sin alterar los hechos. Además, aprender a medir si la adaptación ha funcionado con comprobaciones de sí o no (formato, tono, utilidad y fidelidad).

Al terminar el laboratorio se habrá conseguido:

- Describir una audiencia con las variables que importan: conocimiento previo, necesidad, tono, longitud y formato.
- Pedir al modelo una adaptación sin que pierda ni invente información.
- Controlar la longitud con rangos y comprobarla.
- Separar perspectiva (rol, audiencia) y presentación (formato).
- Comprobar la consistencia de hechos entre versiones.

Conceptos que se usan:

- **Audiencia**. La persona que leerá el texto. Determina el vocabulario, el nivel de detalle, el orden de la información y el formato. Un mismo contenido puede ser perfecto para una audiencia e inútil para otra.
- **Tono y registro**. El tono expresa la actitud (cercano, formal, neutro); el registro, el nivel de lenguaje (coloquial, profesional, técnico-jurídico). Se piden de forma explícita y, si es posible, con un ejemplo.
- **Fidelidad**. Adaptar es cambiar la forma, no el fondo. Una buena adaptación mantiene exactamente los mismos hechos.

## Recursos necesarios

- Un asistente de chat cualquiera.
- Datos en [`datos/`](datos/):
  - [`clausula_sla.md`](datos/clausula_sla.md): el texto original y los cinco hechos que deben mantenerse.
  - [`perfiles_audiencia.csv`](datos/perfiles_audiencia.csv): tres audiencias descritas.
  - [`perfiles_audiencia_ampliacion.csv`](datos/perfiles_audiencia_ampliacion.csv): dos audiencias más para la ampliación.
  - [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): hoja de cálculo con los perfiles, la evaluación con comprobaciones de sí o no (que calcula sola la fidelidad y la longitud), la consistencia, el cambio de tono y el control de longitud.
- Documento fuente: [`sla.md`](../comun/empresa/sla.md).

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: La Espiga cambia su horario en Navidad y debe contárselo a tres públicos: clientes, repartidores y su gestoría. El mismo contenido, tres versiones. Hechos que no pueden perderse: horario nuevo (7:00 a 14:00), desde cuándo (22 de diciembre), cierre de pedidos de roscón (20 de diciembre a las 20:00) y plazo para cambios (24 horas antes de la entrega).

Pasos 1 a 3: los perfiles y las versiones. Cada perfil fija el tono, la longitud y el formato; se genera una versión de cada uno con el mismo prompt base y se anotan las palabras.

| Perfil | Tono | Longitud pedida | Formato | Palabras que salen |
|---|---|---|---|---|
| Cliente | cercano, sin jerga | 50 a 70 palabras | párrafos cortos y una lista de pasos | 62 |
| Repartidor | directo y práctico | 30 a 45 palabras | puntos clave | 52 |
| Gestoría | formal e impersonal | 70 a 100 palabras | texto numerado | 85 |

Paso 4: evaluar con cinco comprobaciones de sí o no. Los cuatro hechos se marcan uno a uno en cada versión; la hoja calcula las dos primeras comprobaciones.

| Versión | Conserva los hechos | Longitud en rango | Respeta el formato | Tono constante | Dice qué hacer | Cumplidas |
|---|---|---|---|---|---|---|
| Cliente | sí (4 de 4) | sí | sí | sí | sí | 5 |
| Repartidor | no (3 de 4: falta el cierre del roscón) | no (52 > 45) | sí | sí | sí | 3 |
| Gestoría | sí (4 de 4) | sí | sí | no (una frase coloquial) | sí | 4 |

Paso 5: consistencia cruzada. Para cada cifra clave se contesta, versión por versión, si aparece con el mismo valor que en el original.

| Cifra clave | Cliente | Repartidor | Gestoría | ¿Igual en las tres? |
|---|---|---|---|---|
| Horario 7:00 a 14:00 | sí | sí | sí | sí |
| Desde el 22 de diciembre | sí | sí | sí | sí |
| Cierre del roscón: 20 de diciembre, 20:00 | sí | no aparece | sí | no |
| Cambios hasta 24 horas antes | sí | sí | sí | sí |

La versión de la gestoría añade además un plazo de pago de 30 días que no estaba en el original: es un dato inventado, aunque el resto sea correcto.

Paso 6: cambiar solo una variable. Se repite la versión del cliente cambiando únicamente el tono.

| Tono | Palabras | Hechos conservados | ¿Mismo formato? |
|---|---|---|---|
| Cercano (el original) | 62 | 4 de 4 | sí |
| Formal | 58 | 4 de 4 | sí |
| Ejecutivo | 41 | 3 de 4 | no |

Al volverse más corto, el tono ejecutivo perdió un hecho y cambió la estructura: conviene vigilar la fidelidad cuando se pide brevedad.

Paso 7: control de longitud, con la versión del repartidor.

| Instrucción de longitud | Palabras o viñetas | Longitud pedida | Desviación |
|---|---|---|---|
| «Sé breve» | 74 palabras | sin cifra | no se puede medir |
| «Entre 40 y 50 palabras» | 55 palabras | 40 a 50 | +5 |
| «Exactamente 3 viñetas» | 4 viñetas | 3 | +1 |

Cuanto más concreta es la instrucción, menor es la desviación; aun así, no se cumple a la primera.

Qué se espera ver en tu laboratorio: lo mismo, con la cláusula del SLA de Altanoria, sus cinco hechos y sus tres perfiles.

## Pasos de ejecución

Todos los pasos se hacen en un chat. Cada versión se genera en una conversación nueva, con el mismo prompt base y cambiando solo el bloque de audiencia.

### Paso 1 · Leer la cláusula y los tres perfiles (6 minutos)
1. Abrir [`datos/clausula_sla.md`](datos/clausula_sla.md). Contiene el texto original y, al final, los cinco hechos que deben mantenerse en las tres versiones (exclusiones, mantenimiento programado, plazo de solicitud del crédito, forma de aplicar el crédito y los porcentajes).
2. Abrir la pestaña «Audiencias» de la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): describe las tres audiencias (los datos vienen de [`datos/perfiles_audiencia.csv`](datos/perfiles_audiencia.csv)) (A1, cliente no técnico; A2, agente comercial; A3, jurista) con su conocimiento, necesidad, tono, longitud y formato.
3. Releer cada perfil con la cláusula delante y preguntarse, antes de generar nada, qué tendría que cambiar de una versión a otra (la hoja no recoge esa reflexión: orientará el prompt base del paso siguiente).

Comprobación: la pestaña «Audiencias» muestra los tres perfiles y se puede decir, para cada uno, la longitud y el formato que pide.

### Paso 2 · Preparar el prompt base (6 minutos)
El prompt base es el mismo para las tres versiones. Solo cambia el bloque de audiencia, tono, longitud y formato. Copiarlo en el documento:

```text
Eres un especialista en comunicación de Altanoria, responsable de explicar condiciones del servicio con precisión.

Audiencia: {copiar de perfiles_audiencia.csv: audiencia, conocimiento y necesidad}
Tono y estilo: {tono}. Longitud: {longitud}. Formato: {formato}.

<texto_original>
{pegar clausula_sla.md}
</texto_original>

Hechos que deben mantenerse en todas las versiones:
1. Exclusiones: red del cliente, uso contrario a las condiciones, fuerza mayor, servicios de terceros no gestionados por Altanoria y pruebas gratuitas.
2. Mantenimiento programado: hasta 4 horas al mes, con 72 horas de aviso; no computa.
3. El crédito se solicita por escrito en 30 días naturales; si no, se pierde.
4. El crédito se aplica a la factura siguiente; no se abona en efectivo.
5. Porcentajes: 10 %, 25 % y 50 % según el tramo de disponibilidad.

Restricciones: usa solo la información del texto original; no inventes cifras ni plazos; no prometas nada fuera del texto.
```

Las partes entre llaves se sustituyen: en «Audiencia», el contenido de las columnas `audiencia`, `conocimiento` y `necesidad` del perfil; en «Tono», «Longitud» y «Formato», los valores de las columnas con esos nombres; y en `texto_original`, el contenido de la cláusula.

Anotar debajo del prompt la lista de partes entre llaves que se sustituyen en cada perfil.

Comprobación: el prompt base está copiado en el documento y debajo hay la lista de marcadores que cambian en cada perfil.

### Paso 3 · Generar las tres versiones (16 minutos)
Para cada perfil (A1, A2 y A3):

1. Abrir una conversación nueva en el asistente.
2. Pegar el prompt base y sustituir los marcadores por los datos del perfil y por el texto de la cláusula. Mantener la lista de cinco hechos tal cual.
3. Enviar, esperar la respuesta y copiarla en el documento con el nombre «versión cliente», «versión comercial» o «versión jurídica».

Comprobación: hay tres textos guardados, uno por audiencia.

### Paso 4 · Evaluar con comprobaciones de sí o no (7 minutos)
Cada versión se evalúa con cinco comprobaciones que se contestan con un sí o un no (la pestaña «Comprobaciones» dice cuándo se contesta «sí»):

| Comprobación | Quién la contesta |
|---|---|
| Conserva los cinco hechos | La hoja, a partir de los hechos que se marquen |
| Longitud dentro del rango | La hoja, a partir de las palabras que se anoten |
| Respeta el formato pedido | La persona: tiene los elementos del formato del perfil |
| Tono constante | La persona: ninguna frase se sale del tono pedido |
| Dice qué hacer | La persona: aparecen la acción, el plazo de 30 días naturales y el medio (por escrito) |

En la pestaña «Evaluación» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): pegar cada versión en un contador de palabras y anotar el número; marcar uno a uno los cinco hechos en cada versión (sí o no) y responder si cambia o inventa alguno; contestar sí o no al formato, al tono y a «dice qué hacer».

Comprobación: la pestaña «Evaluación» tiene los hechos marcados, las palabras y las tres comprobaciones de las tres versiones.

### Paso 5 · Comprobar la consistencia cruzada (4 minutos)
1. En la pestaña «Consistencia», para cada cifra clave de la cláusula (mantenimiento, aviso, plazo del crédito y porcentajes), contestar en cada versión «sí» si aparece con el mismo valor que en el original, «no» si cambia y «no aparece» si falta.
2. Buscar en cada versión cualquier cifra que no esté en el texto original: si aparece alguna, es un dato inventado. Contestar sí o no en la misma pestaña.

Comprobación: la hoja indica si las cifras coinciden en las tres versiones y cuántas versiones tienen datos inventados.

### Paso 6 · Cambiar solo una variable (5 minutos)
1. Repetir la versión del cliente tres veces, cambiando solo el tono: «cercano» (el original), «formal» y «ejecutivo». Cada una, en una conversación nueva.
2. Anotar en la pestaña «Un solo cambio» las palabras de cada versión, cuántos de los cinco hechos conserva y si mantiene el mismo formato.

Comprobación: las tres filas de «Un solo cambio» tienen sus tres datos, y se ve lo que cambia y lo que no cuando solo se cambia el tono.

### Paso 7 · Probar el control de longitud (6 minutos)
Pedir la versión comercial con tres instrucciones de longitud distintas, cada una en una conversación nueva, y contar las palabras o las viñetas que salen:

1. «Sé breve».
2. «Entre 100 y 120 palabras».
3. «Exactamente 5 viñetas de máximo 20 palabras cada una».

Anotar en la pestaña «Longitud» las palabras o las viñetas que salen; la hoja calcula la desviación respecto a lo pedido.

Comprobación: hay tres desviaciones anotadas. Suele verse que cuanto más concreta es la instrucción de longitud, menor es la desviación.

## Conclusiones

### Qué se ha conseguido

Se ha comprobado que un mismo contenido se puede adaptar a tres audiencias distintas controlando el tono, el registro y la longitud, y que la adaptación se mide con comprobaciones de sí o no en lugar de con una impresión. Lo más importante es la fidelidad: al simplificar o formalizar, el asistente puede omitir un hecho o cambiar una cifra, y la única forma de saberlo es contrastar cada versión con la lista de hechos del original. También se ha visto que las instrucciones de longitud vagas («sé breve») se cumplen peor que las concretas («entre 100 y 120 palabras»).

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué hecho fue más difícil de mantener en la versión para el cliente? ¿Por qué?

   <details>
   <summary>Respuesta</summary>

   Suele ser el hecho 3 (pérdida del derecho si no se solicita), porque parece una consecuencia secundaria.

   </details>

2. ¿La versión jurídica mejoró con más longitud o con más estructura?

   <details>
   <summary>Respuesta</summary>

   Con estructura: la numeración y el orden por apartados son más útiles que añadir texto.

   </details>

3. ¿Cómo comprobaría de forma automática que un texto adaptado mantiene los mismos hechos?

   <details>
   <summary>Respuesta</summary>

   Con una lista de comprobación de hechos aplicada a cada versión (por palabras clave o con un segundo prompt de comparación), siempre con revisión humana en textos con implicaciones legales.

   </details>

4. ¿Qué diferencia hay entre pedir «tono formal» y mostrar un ejemplo de tono formal?

   <details>
   <summary>Respuesta</summary>

   Un ejemplo fija el registro de forma concreta; el adjetivo «formal» es ambiguo y cada ejecución lo interpreta distinto.

   </details>

5. ¿Qué riesgos tiene adaptar contenidos legales a un cliente no experto?

   <details>
   <summary>Respuesta</summary>

   Simplificar puede alterar el alcance jurídico: lo adaptado nunca sustituye al texto contractual y debe revisarlo una persona cualificada.

   </details>

### Autoevaluación

- [ ] Los cinco hechos del original aparecen en las tres versiones, o la omisión está justificada por la audiencia.
- [ ] Ninguna versión contiene cifras o plazos ausentes del texto original.
- [ ] Las tres versiones usan vocabulario distinto, pero los datos coinciden.
- [ ] La longitud se midió contando palabras.
- [ ] El tono pedido es observable (por ejemplo, trato de usted frente a tú).
- [ ] Se probó el control de longitud con rangos y con estructura, no solo con adjetivos.

### Errores típicos

- Pedir tono y longitud en una sola frase ambigua.
- No indicar los hechos que no se pueden perder.
- Evaluar “a ojo” sin contar palabras ni marcar hechos.
- Permitir que el modelo añada ejemplos con cifras propias.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Prompt base de referencia

```text
Eres un especialista en comunicación de Altanoria, responsable de explicar condiciones del servicio con precisión.
Audiencia: {{descripción de la audiencia}}
Tarea: explica el contenido del texto original adaptado a esa audiencia.

<texto_original>
{{pegar clausula_sla.md}}
</texto_original>

Hechos que deben mantenerse en todas las versiones (no se pueden omitir ni cambiar):
1. Exclusiones: red del cliente, uso contrario a las condiciones, fuerza mayor, servicios de terceros no gestionados por Altanoria y pruebas gratuitas.
2. Mantenimiento programado: hasta 4 horas al mes, con 72 horas de aviso; no computa.
3. El crédito se solicita por escrito en 30 días naturales; si no, se pierde.
4. El crédito se aplica a la factura siguiente; no se abona en efectivo.
5. Porcentajes: 10 %, 25 % y 50 % según el tramo de disponibilidad.

Tono y estilo: {{tono}}. Longitud: {{rango de palabras}}. Formato: {{formato}}.
Restricciones: usa solo la información del texto original; no inventes cifras ni plazos; no prometas nada fuera del texto.
```

### Cómo debería diferenciarse cada versión

| Aspecto | Cliente | Agente comercial | Jurista |
|---|---|---|---|
| Orden | Primero «qué me corresponde» y después «cómo pedirlo» | «Qué decir» y «qué no decir» | Alcance → exclusiones → remedios → plazos |
| Vocabulario | Sin «disponibilidad mensual garantizada» sin explicarla | Frases cortas repetibles por teléfono | Terminología precisa, referencias a las cláusulas |
| Tono | Cercano | Directo y práctico | Formal e impersonal |
| Formato | Párrafos cortos y pasos | Viñetas | Texto numerado |
| Longitud | 150–200 palabras | 120–160 | 180–250 |

### Ejemplo de la versión para el cliente (extracto)

«Si el servicio no funciona durante un mes por debajo del nivel que le garantizamos, tiene derecho a un descuento en su cuota mensual (10 %, 25 % o 50 %, según la gravedad). Para recibirlo debe pedirlo por escrito en los 30 días siguientes al final del mes afectado; si no lo pide, se pierde. El descuento se aplica en la factura siguiente; no se devuelve en efectivo. No cuentan como caída los mantenimientos avisados con 72 horas (hasta 4 al mes), los fallos de su propia red ni los de servicios de terceros que no gestionamos.»

### Ejemplo de la versión comercial (extracto)

- Qué decir: «Si el servicio baja del nivel garantizado, hay un crédito del 10, 25 o 50 % de la cuota. Se pide por escrito en 30 días y se descuenta de la factura siguiente».
- Qué no decir: que se devuelve en efectivo; que cubre fallos de la red del cliente; que hay un tiempo de resolución garantizado.
- Si pregunta por mantenimiento: hasta 4 horas al mes, avisadas con 72 horas, no cuentan.

### Qué distingue a las audiencias (Paso 1)

Lo que ya sabe, lo que necesita, lo que le sobra, el tono y el formato de cada una; sirve para orientar el prompt base:

| | Cliente (A1) | Agente comercial (A2) | Jurista (A3) |
|---|---|---|---|
| Qué ya sabe | Su negocio, no el vocabulario del SLA | Los productos y los planes, no el derecho | La contratación |
| Qué necesita | Qué pasa si el servicio falla y qué hacer para recibir el crédito | Explicarlo en una llamada sin prometer de más | Alcance, plazos, exclusiones y remedios con precisión |
| Qué le sobra | Jerga del SLA y referencias a cláusulas | Matices jurídicos y párrafos largos | Explicaciones básicas y lenguaje comercial |
| Tono | Cercano pero profesional | Directo y práctico | Formal e impersonal |
| Formato | Párrafos cortos y una lista de pasos | Puntos clave con «qué decir» y «qué no decir» | Texto numerado con referencias a las cláusulas |

### Consistencia entre versiones y un solo cambio (Pasos 5 y 6)

- Consistencia cruzada (Paso 5). Las afirmaciones que deben coincidir en las tres versiones son, por ejemplo, el plazo de 30 días naturales para pedir el crédito y que no se abona en efectivo. Una cifra que no esté en la cláusula (un plazo nuevo, un porcentaje distinto) es un dato inventado.
- Un solo cambio (Paso 6). Al cambiar únicamente el tono (cercano, formal, ejecutivo), debe cambiar el vocabulario, la longitud y la estructura, y los cinco hechos deben mantenerse. Si un hecho desaparece o se altera al cambiar el tono, el tono está pesando más que la fidelidad y hay que reforzar la lista de hechos en el prompt.

### Control de longitud (resultado esperable) — expectativa previa a la medición

- «Sé breve» produce resultados muy variables (de 40 a 150 palabras).
- «Entre 100 y 120 palabras» suele quedar cerca, con desviaciones del 10–20 %.
- «5 viñetas de máximo 20 palabras» es el más fiable porque la estructura es verificable.
- Conclusión: la estructura controla la longitud mejor que un adjetivo, y los rangos mejor que las cifras exactas.

### Fallos típicos observados

- La versión para el cliente suaviza el hecho 3 («puede pedirlo») y omite que se pierde si no se pide.
- La versión comercial convierte «no se abona en efectivo» en «se descuenta», perdiendo la restricción.
- La versión jurídica añade referencias a cláusulas que no existen (inventadas) si no se prohíbe.
- Aparecen plazos nuevos («a la mayor brevedad») que cambian el sentido.

</details>

### Para seguir

- Generar las versiones para las dos audiencias de `perfiles_audiencia_ampliacion.csv` y compararlas con las anteriores.
- Pedir al modelo que detecte qué versión se dirige a qué audiencia sin decírselo (prueba de que el estilo es identificable).
- Convertir el prompt base en una plantilla con variables y reutilizarla con otra cláusula (por ejemplo, la política de cancelación).

---

[← Laboratorios](../README.md) · [Módulo 05](../../modulos/05-roles-personas-y-comportamiento/README.md) · [← 04B](../04B/README.md) · [05B →](../05B/README.md)
