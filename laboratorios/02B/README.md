[← Laboratorios](../README.md) · [Módulo 02](../../modulos/02-fundamentos-del-prompt-engineering/README.md) · [← 02A](../02A/README.md) · [03A →](../03A/README.md)

# Laboratorio 02B · Anatomía de un prompt: ablación de componentes

Módulo 02 · Fundamentos del Prompt Engineering · Duración estimada: 45 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Quitar uno a uno los componentes de un prompt y medir cuánto aporta cada uno al resultado. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Preparar las siete variantes (7 min)
- Paso 2 · Ejecutar el experimento (22 min)
- Paso 3 · Medir cada respuesta (8 min)
- Paso 4 · Decidir el prompt mínimo (8 min)

<details>
<summary>Secciones del módulo relacionadas (9)</summary>

- [§2.1 Anatomía general de un prompt](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#21-anatomía-general-de-un-prompt)
- [§2.2 Componente 1: Rol o perspectiva](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#22-componente-1-rol-o-perspectiva)
- [§2.3 Componente 2: Contexto](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#23-componente-2-contexto)
- [§2.4 Componente 3: Instrucción o tarea](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#24-componente-3-instrucción-o-tarea)
- [§2.5 Componente 4: Datos de entrada](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#25-componente-4-datos-de-entrada)
- [§2.6 Componente 5: Restricciones y condiciones](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#26-componente-5-restricciones-y-condiciones)
- [§2.7 Componente 6: Formato de salida](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#27-componente-6-formato-de-salida)
- [§2.8 Componente 7: Criterios de calidad](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#28-componente-7-criterios-de-calidad)
- [§2.9 Cómo se relacionan los componentes](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#29-cómo-se-relacionan-los-componentes)

</details>

## Justificación del laboratorio

En Altanoria, el equipo de Soporte redacta cada día decenas de respuestas a reclamaciones con ayuda de un asistente de IA, y el prompt que usa es largo: tiene un rol, un contexto, una tarea, datos, restricciones, un formato y unos criterios de calidad. Un responsable propone «simplificar los prompts porque son larguísimos». Otro responde que «cada línea tiene su motivo». Los dos tienen una opinión; ninguno tiene datos.

Un prompt largo cuesta más (se paga por token), es más difícil de mantener y puede esconder partes que no sirven para nada. Pero un prompt recortado a ciegas puede perder justo la línea que evitaba un error grave, como prometer un reembolso que las condiciones no permiten. La única forma de saber qué aporta cada parte es medirlo.

Este laboratorio aplica un método propio de la ciencia: la ablación. Se parte de un prompt completo, se elimina un componente cada vez y se compara el resultado con tres medidas fijas. Al final se sabrá, con evidencia, qué componentes son imprescindibles para esta tarea, cuáles son opcionales y cuál es el prompt mínimo viable, y se podrá zanjar la discusión del equipo.

## Objetivos

Medir qué aporta cada componente de un prompt (rol, contexto, tarea, datos de entrada, restricciones, formato y criterios de calidad) mediante un experimento de ablación: se parte de un prompt completo, se elimina un componente cada vez y se compara el resultado con tres medidas fijas.

Al terminar el laboratorio se habrá conseguido:

- Diseñar un experimento controlado sobre prompts: una sola variable por prueba.
- Medir las respuestas con criterios que se pueden comprobar (palabras, promesas, importe) en lugar de valorarlas por impresión.
- Descubrir qué componentes tienen más impacto en una tarea concreta y cuáles son prescindibles.
- Entender que la importancia de cada componente depende de la tarea: no hay una receta universal.

Conceptos que se usan:

- **Ablación**. Técnica de investigación que consiste en retirar una parte de un sistema para medir su contribución. Aplicada a prompts: se quita un componente y se observa cuánto empeora la respuesta.
- **Los siete componentes** (véase [§2.1 Anatomía general de un prompt](../../modulos/02-fundamentos-del-prompt-engineering/02-anatomia-de-un-prompt.md#21-anatomía-general-de-un-prompt)):
  - rol
  - contexto
  - tarea
  - datos de entrada
  - restricciones
  - formato de salida
  - criterios de calidad

  No todos son necesarios en todas las tareas; el diseño busca proporcionalidad entre el esfuerzo del prompt y el riesgo o la repetición de la tarea.

- **Medida comprobable**. Criterio que se contesta con un número o con sí/no, sin interpretación: cuántas palabras tiene la respuesta, si promete algo prohibido, si cita el importe. Evita valorar «a ojo» y permite comparar versiones.
- **Variabilidad**. Los modelos no responden idéntico dos veces. Por eso cada variante se ejecuta varias veces (tres como mínimo) y se promedia.

## Recursos necesarios

- Un asistente de chat cualquiera con el que se pueda iniciar conversaciones nuevas fácilmente.
- Datos en [`datos/`](datos/):
  - [`prompt_completo.md`](datos/prompt_completo.md): el prompt de referencia con los siete componentes.
  - [`reclamaciones_ablacion.csv`](datos/reclamaciones_ablacion.csv): cinco casos de reclamación con hechos, condición aplicable y límites.
- La hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), para las ejecuciones, las medidas y el resultado por variante (se mide sin conocer la variante).

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Pasos de ejecución

Los pasos se hacen en orden y solo necesitan un chat y una hoja de cálculo. La regla de oro: cada ejecución se hace en una conversación nueva, para que el asistente no arrastre el contexto de la anterior.

### Paso 1 · Preparar las siete variantes (7 minutos)
1. Abrir la carpeta [`prompts/`](prompts/). Contiene siete ficheros, V0 a V6. V0 es el prompt completo; cada una de las demás elimina una parte:

| Código | Variante | Qué se hace |
|---|---|---|
| V0 | Completa | Prompt completo de referencia |
| V1 | Sin rol | Se elimina el bloque [ROL] |
| V2 | Sin contexto | Se elimina el bloque [CONTEXTO] |
| V3 | Sin restricciones | Se elimina el bloque [RESTRICCIONES] |
| V4 | Sin formato | Se elimina el bloque [FORMATO DE SALIDA] |
| V5 | Sin criterios | Se elimina el bloque [CRITERIOS DE CALIDAD] |
| V6 | Mínima | Solo [TAREA] y [DATOS DE ENTRADA] |

2. Abrir [`prompts/V0.txt`](prompts/V0.txt) y leerlo entero: son los siete componentes. Después abrir V3 y V4 y comprobar que cada uno lo único que hace es quitar el bloque indicado. Los componentes [TAREA] y [DATOS DE ENTRADA] no se quitan por separado porque sin ellos no hay prompt.
3. Abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): la pestaña «Ejecuciones» tiene las 14 combinaciones de variante y caso (las seis obligatorias están marcadas) y la pestaña «Medidas» las columnas de medida: palabras, ¿promete algo fuera de las condiciones?, ¿menciona el importe? y observaciones.

Anotar en el documento qué bloque falta en V3 y en V4 respecto a V0.

Comprobación: hay dos notas (una por variante) con el bloque que falta, y la pestaña «Ejecuciones» está abierta con sus 14 combinaciones.

### Paso 2 · Ejecutar el experimento (22 minutos)
Se ejecutan las variantes V0 (completa), V3 (sin restricciones) y V4 (sin formato) sobre dos casos de reclamación, C1 y C2: seis ejecuciones. Si hay tiempo, se pueden añadir las otras cuatro variantes.

1. Preparar los datos de los dos casos. Los valores que se sustituyen en cada ejecución son:

| Marcador del prompt | Caso C1 | Caso C2 |
|---|---|---|
| `{{DATOS_DEL_CASO}}` | Cliente: Carolina Vidal Roig (Aceros del Turia). Producto: DocuMind, plan Team. Hecho: cargo duplicado de 599,00 € (1 y 3 de octubre). Antigüedad como cliente: 2 años. Gravedad: media. | Cliente: Bruno Esteve Cano (Logística Pirineos). Producto: Altanoria Copilot, plan Starter. Hecho: caída de 6 horas el día 14 de septiembre. Cuota mensual afectada: 36,00 €. Antigüedad: 8 meses. Gravedad: alta. |
| `{{CONDICION_APLICABLE}}` | Error de facturación imputable a Altanoria: reembolso (condiciones 5.4) | Crédito SLA según disponibilidad del mes (sla.md §2); hay que solicitarlo en 30 días |
| `{{NO_PROMETER}}` | plazos de abono concretos | compensación en efectivo |

2. Para cada una de las seis combinaciones (V0, V3 y V4, con C1 y con C2):
   - Abrir una conversación nueva.
   - Abrir el fichero de la variante (por ejemplo, `prompts/V3.txt`), copiar todo su contenido y pegarlo en el chat.
   - Sustituir los tres marcadores entre llaves dobles por los valores de la tabla del caso. Si una variante no contiene un marcador (por ejemplo, V3 no tiene el bloque de restricciones y por tanto no tiene `{{NO_PROMETER}}`), se ignora ese valor.
   - Enviar, nombrar la conversación con el código de la ejecución (el que figura en la pestaña «Ejecuciones») y marcar la ejecución como hecha.
3. Para puntuar sin sesgo, no mirar la variante al leer cada respuesta: la pestaña «Medidas» ordena las respuestas por código (R1, R2…) y tiene ocultas las columnas de variante y caso. Mostrarlas, con el botón «+» de la cabecera, solo después de haber medido todas.

Comprobación: hay seis conversaciones, cada una con su código de ejecución, y la pestaña «Ejecuciones» cuenta seis ejecutadas.

### Paso 3 · Medir cada respuesta (8 minutos)
Para cada una de las seis respuestas, anotar tres cosas objetivas en la pestaña «Medidas», por código:

1. Número de palabras: pegar la respuesta en un contador de palabras (el de cualquier editor de texto) y anotar el número; la hoja indica si está dentro del rango pedido de 90 a 150.
2. Promesas fuera de las condiciones: ¿promete algo que el campo «no prometer» prohíbe (un plazo de abono, una compensación en efectivo)? Responder sí o no.
3. Mención del importe: ¿cita el importe o el hecho concreto del caso? Responder sí o no.

Comprobación: la pestaña «Medidas» tiene las tres medidas de las seis respuestas.

### Paso 4 · Decidir el prompt mínimo (8 minutos)
1. Leer en la pestaña «Resultado», por variante, el promedio de palabras y cuántas respuestas prometen algo indebido o no citan el importe (la hoja lo calcula con las medidas, ya con la variante a la vista).
2. Mirar la columna «¿Empeora respecto a V0?»: es «sí» si al quitar ese componente hay más promesas indebidas, más respuestas sin el importe o más respuestas fuera del rango de palabras que con la variante completa.
3. Contestar «sí» o «no» en la columna «¿Se mantiene en el prompt mínimo?» de cada variante ejecutada: lo razonable es mantener los componentes cuya ausencia empeora alguna medida y quitar los demás.

Comprobación: cada variante ejecutada tiene su decisión y se puede señalar la cifra de la hoja que la respalda.

## Conclusiones

### Qué se ha conseguido

Se ha convertido una discusión de opiniones en una medida. Lo habitual es que no todos los componentes pesen igual: los que acotan la salida (el formato y las restricciones) suelen cambiar mucho el resultado, y otros (el rol o los criterios de calidad) cambian menos en tareas concretas. Eso permite recortar los prompts con criterio, sin perder las líneas que evitan errores graves, y es un método que se puede repetir con cualquier otro prompt largo.

Referencia orientativa (rangos amplios con un modelo pequeño; con otro modelo pueden variar): Quitar el formato (variante sin formato) o dejar el prompt mínimo suele multiplicar por 2 o por 3 la longitud de la respuesta; quitar el rol o el contexto cambia poco las métricas automáticas, y quitar los criterios puede hacer que falten datos que el criterio exigía (como el importe). Los efectos de calidad requieren valoración humana. Si el resultado queda muy lejos, conviene revisar datos, prompt y script antes de abrir la solución.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué componente tuvo más impacto? ¿Sobre qué medida?

   <details>
   <summary>Respuesta</summary>

   En la medición con Gemma 4 y métricas automáticas, el componente con más impacto sobre la longitud fue el formato de salida: sin él, las respuestas pasaron de 151 a 262 palabras de media y ninguna quedó dentro del rango pedido; y los criterios fueron los que más influyeron en que se mencionara el importe (de 15 de 15 a 6 de 15 respuestas). Afectan, respectivamente, a los criterios de longitud y estructura y de precisión. Con otro modelo o tarea, el orden puede cambiar.

   </details>

2. ¿Hubo algún componente cuya eliminación no empeoró nada? ¿Es entonces superfluo?

   <details>
   <summary>Respuesta</summary>

   Sí: quitar el rol, el contexto o los criterios apenas movió las métricas medibles automáticamente. Eso no los hace superfluos: pueden aportar tono o siguiente paso, que requieren valoración humana, y con cinco casos no se puede concluir.

   </details>

3. ¿Qué efecto tuvo eliminar el formato: peor contenido o peor presentación?

   <details>
   <summary>Respuesta</summary>

   Peor presentación más que peor contenido: los hechos y el importe seguían apareciendo, pero la longitud y la estructura se descontrolaban.

   </details>

4. ¿Cuánta variabilidad hay entre repeticiones de la misma variante? ¿Cuántas ejecuciones harían falta para que la diferencia entre dos variantes fuera fiable?

   <details>
   <summary>Respuesta</summary>

   Bastante en tareas de redacción con temperatura mayor que cero. Para que una diferencia de uno o dos puntos sobre diez sea fiable hacen falta decenas de ejecuciones por variante; como regla práctica, repetir hasta que la diferencia entre variantes supere claramente la variabilidad entre repeticiones.

   </details>

5. Si el rol no mejora la corrección pero sí el tono, ¿cuándo compensa incluirlo?

   <details>
   <summary>Respuesta</summary>

   Cuando el tono importa para el cliente (atención al cliente, comunicación de marca), cuando mantener la misma voz entre piezas es un objetivo y cuando añade pocos tokens. No compensa si alarga el prompt sin efecto observable.

   </details>

### Autoevaluación

- [ ] Solo se cambió un componente entre V0 y cada variante V1–V5.
- [ ] Hay al menos tres repeticiones por caso y variante (o la limitación está anotada).
- [ ] Las medidas se hicieron sin conocer la variante.
- [ ] Los promedios y recuentos se calculan por variante y se comparan con la variante completa.
- [ ] El prompt mínimo viable reconoce que el impacto puede cambiar con otra tarea.

### Errores típicos

- Cambiar dos componentes a la vez.
- Medir sabiendo qué variante es (sesgo de confirmación).
- Sacar conclusiones con una sola ejecución.
- Concluir que un componente «no sirve» cuando solo no sirve para esa tarea.
- Tomar una sola medida como la calidad total.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

> Los números exactos dependen del modelo. Lo que sigue describe el patrón típico y el procedimiento de análisis.

### Patrón de resultados que suele observarse — expectativa previa a la medición

| Variante | Efecto habitual | Medida que más cambia |
|---|---|---|
| V0 Completa | Referencia | — |
| V1 Sin rol | Cambio pequeño; el tono puede ser más genérico | Ninguna de las tres |
| V2 Sin contexto | Respuestas correctas pero menos orientadas al siguiente paso | Ninguna de las tres |
| V3 Sin restricciones | Mayor riesgo: aparecen promesas no respaldadas («le abonaremos en 24 horas») | Promesas indebidas |
| V4 Sin formato | Longitud y estructura variables | Palabras fuera de 90–150 |
| V5 Sin criterios | Cambio pequeño o nulo si la tarea es sencilla | Importe citado |
| V6 Mínima | La más baja y la más variable | Promesas y palabras |

Interpretación habitual:

- Restricciones y formato son los que más protegen los resultados verificables (no prometer, longitud, estructura).
- Rol y contexto mejoran sobre todo el tono y la orientación, pero con una tarea y datos claros su efecto es moderado.
- Criterios de calidad tienen más valor cuando hay un proceso de revisión que los utiliza; solos, tienden a ser redundantes con las restricciones.
- La variante mínima no solo puntúa menos: varía más entre ejecuciones, lo que importa en producción.

### Cómo analizar

Para cada variante: promedio de palabras, número de respuestas dentro de 90–150, número de respuestas con promesa indebida y número sin el importe. La pestaña «Resultado» de la hoja lo calcula y marca si quitar el componente empeora alguna medida respecto a la variante completa. Las cifras reales de una medición están más abajo.

### Prompt mínimo viable de ejemplo

«Para respuestas a reclamaciones, el prompt mínimo viable debe incluir tarea + datos delimitados + restricciones (incluida la lista de lo que no se puede prometer) + formato. El rol y el contexto son recomendables porque mejoran el tono y el siguiente paso. Los criterios de calidad se reservan para el revisor automático o humano. Este orden puede cambiar en otras tareas: en clasificación, por ejemplo, el formato y las definiciones de categorías pesan más que el rol.»

### Resultados medidos con un modelo real

> Medición realizada el 23 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada a 16.384 tokens, tres repeticiones por caso y variante (15 respuestas por variante) y un script de medición propio (el laboratorio se hace por chat). Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

Ablación con los cinco casos y tres repeticiones por caso (T = 0,5), solo con métricas automáticas (palabras, presencia del importe y de frases de promesa):

| Variante | Palabras de media | Dentro de 90–150 palabras | Frases de promesa | Menciona el importe |
|---|---|---|---|---|
| V0 completa | 151 | 7/15 | 0/15 | 15/15 |
| V1 sin rol | 136 | 13/15 | 0/15 | 15/15 |
| V2 sin contexto | 141 | 13/15 | 0/15 | 13/15 |
| V3 sin restricciones | 160 | 3/15 | 1/15 | 15/15 |
| V4 sin formato | 262 | 0/15 | 1/15 | 15/15 |
| V5 sin criterios | 143 | 12/15 | 0/15 | 6/15 |
| V6 mínima | 352 | 0/15 | 3/15 | 10/15 |

Lectura:

1. El componente cuya eliminación más cambia la longitud es el formato (de 151 a 262 palabras de media, y ninguna respuesta dentro del rango); el prompt mínimo la multiplica por 2,3
2. Quitar los criterios casi no cambia la longitud, pero hace que el importe aparezca solo en 6 de 15 respuestas, frente a 15 de 15 con el prompt completo: el componente que más importa depende de la métrica que se mire
3. Sin restricciones la longitud también se sale del rango (3/15) y aparece una frase de promesa
4. Quitar el rol o el contexto apenas altera las métricas automáticas, y la V0 completa queda fuera del rango más veces que V1 o V2 (7/15 frente a 13/15): con 15 respuestas por variante, diferencias de pocas respuestas son compatibles con el ruido, y por eso la comparación es orientativa.

Las «frases de promesa» se detectan por palabras clave, un indicador tosco. El orden de importancia que se supuso en la solución (restricciones > formato…) no se confirma con estos datos: depende del modelo y de la tarea, que es la lección del laboratorio.

</details>

### Para seguir

- Añadir una variante con un rol equivocado (por ejemplo, «eres un abogado penalista») y medir el daño.
- Añadir una variante con instrucciones contradictorias (véase [§3.8 Instrucciones contradictorias y prioridades](../../modulos/02-fundamentos-del-prompt-engineering/03-principios-de-diseno.md#38-instrucciones-contradictorias-y-prioridades)).
- Repetir con otra tarea (por ejemplo, clasificar tickets) y comprobar si el orden de importancia cambia.

---

[← Laboratorios](../README.md) · [Módulo 02](../../modulos/02-fundamentos-del-prompt-engineering/README.md) · [← 02A](../02A/README.md) · [03A →](../03A/README.md)
