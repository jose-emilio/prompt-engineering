[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-razonamiento-y-descomposicion.md)

# 1 · Técnicas basadas en ejemplos

*Módulo 04: Técnicas avanzadas de prompting*

## 1.1 ¿Por qué usar técnicas avanzadas?

Un prompt básico funciona para tareas sencillas, pero falla cuando la tarea es ambigua, compleja o requiere precisión específica. Las técnicas avanzadas resuelven problemas concretos.

- **Tareas ambiguas**: Requieren ejemplos o reglas explícitas para reducir la variabilidad de la salida.
- **Tareas complejas**: Pueden necesitar etapas separadas para evitar errores en cadena.
- **Múltiples candidatos**: Permiten comparar soluciones y seleccionar la más consistente con una comprobación externa.
- **Herramientas externas**: Amplían las capacidades del modelo pero añaden riesgos operativos que deben controlarse.

Ninguna técnica garantiza exactitud. La validación independiente es siempre necesaria.

**Explicación**

Un prompt básico funciona para tareas sencillas, pero falla cuando la tarea es ambigua, compleja o exige precisión. Cada técnica avanzada resuelve un problema concreto: las tareas ambiguas necesitan ejemplos o reglas explícitas para reducir la variabilidad; las complejas pueden requerir etapas separadas para evitar errores en cadena; cuando hay varios candidatos útiles, se pueden comparar y elegir el más consistente con una comprobación externa; y las herramientas externas amplían las capacidades pero añaden riesgos operativos que hay que controlar.

Si la salida varía o no sigue las convenciones, suelen ayudar los ejemplos; si los errores aparecen a mitad de un proceso largo, el razonamiento estructurado o la **descomposición**. Ninguna técnica sustituye la validación independiente: reduce el error, no lo elimina.

---

## 1.2 Zero-shot: definición y funcionamiento

En el prompting Zero-shot la tarea se especifica únicamente mediante instrucción, sin incluir ninguna demostración de entrada-salida. El modelo aplica las capacidades generales adquiridas durante el preentrenamiento para resolver la solicitud.

Es el punto de partida natural para cualquier nueva tarea: rápido, compacto y sin coste de curación de ejemplos.

- La tarea se especifica sin demostraciones previas.
- El modelo usa capacidades adquiridas en preentrenamiento.
- Adecuado para tareas claras y de propósito general.
- Depende de la calidad de la instrucción y el contexto proporcionado.
- Puede fallar ante reglas especializadas o taxonomías internas.

**Ejemplo ilustrativo**

**Prompt Zero-shot:**

*"Clasifica el siguiente mensaje de soporte en una de estas categorías: Facturación, Acceso, Error técnico, Otro. Responde solo con el nombre de la categoría.*

*Mensaje: «No puedo iniciar sesión desde esta mañana.»"*

Salida esperada: Acceso

**Explicación**

En el prompting zero-shot la tarea se describe solo con una instrucción, sin ejemplos. El modelo aplica sus capacidades generales para resolverla. Es el punto de partida natural: rápido, compacto y sin coste de preparar ejemplos. Es adecuado para tareas claras y generales, depende de la calidad de la instrucción y puede fallar ante reglas especializadas o taxonomías internas.

El ejemplo clasifica un mensaje de soporte («No puedo iniciar sesión desde esta mañana») entre Facturación, Acceso, Error técnico y Otro, con respuesta de una sola palabra: «Acceso». Aunque no tenga ejemplos, no es una pregunta informal: usa todo lo visto antes (verbo preciso, categorías enumeradas, formato fijado). Se recomienda empezar siempre por zero-shot y complicar el prompt solo si las pruebas muestran fallos sistemáticos.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 04A · Zero-shot, one-shot y few-shot: cuántos ejemplos hacen falta](../../laboratorios/04A/README.md)
<!-- /labs-seccion -->

---

## 1.3 Diseño de un prompt Zero-shot completo

Un prompt Zero-shot bien construido no es simplemente una pregunta: incorpora todos los elementos necesarios para que el modelo interprete la tarea de forma unívoca, sin necesidad de ejemplos.

- **Definir tarea y objetivo**: Enunciar con precisión qué debe hacer el modelo y cuál es el resultado esperado.
- **Aportar contexto mínimo**: Incluir solo la información relevante; el ruido reduce la precisión.
- **Enumerar categorías o criterios**: Listar explícitamente las opciones posibles para evitar invenciones.
- **Fijar formato de salida**: Especificar si la respuesta debe ser una palabra, una frase, JSON, etc.
- **Indicar tratamiento de casos dudosos**: Instruir explícitamente qué hacer cuando ninguna categoría encaja con claridad.

**Explicación**

Un prompt zero-shot completo incluye cinco elementos: definir la tarea y el resultado esperado, aportar solo el contexto mínimo relevante, enumerar las categorías o criterios posibles para evitar invenciones, fijar el formato de salida e indicar qué hacer en los casos dudosos.

Dos son especialmente importantes. Enumerar las categorías obliga a que la respuesta pertenezca a una lista cerrada; y prever el tratamiento de los casos dudosos distingue un prompt robusto de uno ingenuo, porque sin una salida prevista el modelo forzará una categoría con apariencia de seguridad. Una buena comprobación es releer el prompt buscando decisiones que quedan en manos del modelo sin que nadie las haya tomado.

---

## 1.4 Ventajas y límites del prompting Zero-shot

**✅ Ventajas**

**⚠️ Límites**

- **Preparación mínima**: No requiere curación ni etiquetado de ejemplos; listo para usar de inmediato.
- **Interpretación implícita de reglas**: El modelo puede aplicar convenciones propias que difieren de las internas del equipo.
- **Prompts más cortos**: Menor consumo de tokens y latencia reducida en producción.
- **Consistencia variable**: La misma instrucción puede producir salidas distintas; es necesario probarla con un conjunto representativo.
- **Adecuado para tareas generales**: Funciona bien cuando la tarea coincide con el conocimiento general del modelo.
- **Taxonomías especializadas**: Las clasificaciones propias de un negocio requieren habitualmente ejemplos o definiciones explícitas.

**Explicación**

El zero-shot tiene ventajas claras: preparación mínima, prompts más cortos (menos tokens y menor latencia) y buen encaje con tareas generales que coinciden con el conocimiento del modelo. Sus límites son la interpretación implícita de reglas (el modelo puede aplicar convenciones propias distintas de las del equipo), la consistencia variable entre ejecuciones y la dificultad con taxonomías especializadas, que suelen requerir ejemplos o definiciones explícitas.

Distinguir «consulta» de «queja» es una distinción general que el modelo conoce; clasificar con una taxonomía interna de nueve tipos exige explicar criterios que no conoce. La regla de decisión es: si la tarea es general y las pruebas dan resultados consistentes, basta zero-shot; si depende de convenciones internas o los resultados varían, hay que aportar **demostraciones**.

---

## 1.5 One-shot: un ejemplo que transforma la instrucción

El prompting One-shot incorpora un único par de entrada-salida antes de la nueva tarea. Este ejemplo actúa como demostración concreta del patrón o formato esperado, resolviendo ambigüedades que la instrucción verbal no siempre puede cubrir.

- **Un par entrada → salida**: Muestra explícitamente el patrón o formato deseado.
- **Útil cuando la instrucción no basta**: Especialmente en formatos no estándar o convenciones internas.

**Ejemplo ilustrativo**

*Extrae el nombre y el importe de la siguiente factura.*

*Entrada de ejemplo: «Factura de Proveedor ABC por servicios de consultoría: 1.200 €»*

*Salida de ejemplo*: *Nombre: Proveedor ABC | Importe: 1.200 €*

*Nueva entrada*: *«Recibo de Logística XYZ por transporte urgente: 340 €»*

- **El ejemplo debe ser correcto**: Un ejemplo erróneo puede propagar el error a todas las salidas.
- **Riesgo de sesgo**: Un solo ejemplo sesgado puede inducir un patrón no deseado en la respuesta.

**Explicación**

El one-shot incorpora un único par de entrada y salida antes de la nueva tarea. El ejemplo actúa como demostración del patrón o formato esperado y resuelve ambigüedades que la instrucción verbal no cubre. Es útil en formatos no estándar o convenciones internas, pero tiene riesgos: si el ejemplo es erróneo, el error se propaga a todas las salidas, y un solo ejemplo sesgado puede inducir un patrón no deseado.

En el ejemplo de extracción de facturas, el par «Factura de Proveedor ABC… 1.200 €» con salida «Nombre / Importe» enseña no solo qué campos extraer, sino también cómo escribirlos. Con un único ejemplo, el modelo puede sobregeneralizar rasgos accidentales (el orden, el tipo de documento), de modo que sirve para fijar un formato pero no para cubrir variaciones.

---

## 1.6 Cómo diseñar una demostración One-shot eficaz

No basta con incluir cualquier ejemplo; la calidad del par entrada-salida determina directamente la calidad de la salida generada. Sigue estas pautas para maximizar su efectividad.

- **Entrada clara**: La entrada del ejemplo debe ser representativa y sin ambigüedad; evita casos extremos.
- **Salida correcta y completa**: Verifica que la salida del ejemplo sea exactamente lo que esperarías del modelo en producción.
- **Eliminar detalles irrelevantes**: Incluir información superflua puede distraer al modelo y reducir la precisión.
- **Mantener el formato esperado**: El formato de la salida del ejemplo debe coincidir exactamente con el formato deseado en la nueva tarea.
- **Delimitar ejemplo y nueva tarea**: Usa separadores visuales (líneas, etiquetas, corchetes) para que el modelo no confunda el ejemplo con la entrada real.

**Explicación**

La calidad del par de entrada y salida determina la calidad de la respuesta. Cinco pautas: usar una entrada clara y representativa, sin casos extremos; una salida correcta y completa, exactamente la que se esperaría en producción; eliminar los detalles irrelevantes; mantener el formato exacto que se desea en la nueva tarea; y delimitar con separadores el ejemplo y la nueva tarea para que no se confundan.

La segunda pauta es la más ignorada: el modelo trata el ejemplo como la verdad y reproduce sus defectos de forma sistemática. Sin delimitadores, puede continuar el ejemplo en lugar de procesar la entrada nueva. Conviene someter el ejemplo al mismo escrutinio que una salida del modelo y comprobar si sería aceptable en producción.

---

## 1.7 Few-shot: aprendizaje en contexto con varios ejemplos

El prompting Few-shot proporciona varios pares de entrada-salida antes de la nueva tarea. Esta colección de demostraciones permite al modelo inferir reglas implícitas, convenciones de formato y excepciones que serían difíciles de expresar solo con instrucciones.

- Muestra reglas y convenciones mediante múltiples demostraciones.
- Puede ayudar significativamente en tareas especializadas o con taxonomías propias.
- No actualiza los parámetros del modelo; el efecto existe solo durante la inferencia.
- La calidad de los ejemplos es crítica: errores en los ejemplos se propagan a la salida.

**Estructura típica Few-shot**

1. **Ejemplo 1**: Entrada A → Salida A
2. **Ejemplo 2**: Entrada B → Salida B
3. **Ejemplo 3**: Entrada C → Salida C
4. **Nueva tarea**: Entrada D → ?

**Explicación**

El few-shot proporciona varios pares de entrada y salida antes de la nueva tarea. Permite al modelo inferir reglas implícitas, convenciones de formato y excepciones difíciles de expresar solo con instrucciones, lo que ayuda en tareas especializadas o con taxonomías propias. La estructura es sencilla: varios ejemplos y, al final, la nueva entrada cuya salida se espera.

No actualiza los parámetros del modelo: el efecto solo existe durante esa llamada, así que si la tarea se repite los ejemplos deben incluirse cada vez. Y la calidad de los ejemplos es crítica, porque sus errores se propagan. Frente al one-shot, la ventaja está en la cobertura: pueden mostrarse casos distintos, incluidas las excepciones.

---

## 1.8 In-Context Learning: adaptación sin reentrenamiento

El In-Context Learning (ICL) es el mecanismo por el que el modelo ajusta su comportamiento en función de los patrones presentes en el prompt, sin modificar sus pesos internos. Es un fenómeno de inferencia, no de entrenamiento.

- **Ocurre durante la inferencia**: El modelo utiliza los patrones del contexto actual para generar la respuesta; no aprende de forma permanente.
- **No equivale a reentrenar**: Al cerrar la sesión o cambiar el prompt, el efecto desaparece por completo.
- **El efecto depende del contexto**: Distintos ejemplos en el mismo prompt pueden producir comportamientos notablemente diferentes.

Para un comportamiento estable y persistente, considera el ajuste fino (*fine-tuning*) en lugar de ICL.

**Explicación**

El **aprendizaje en contexto** (in-context learning, ICL) es el mecanismo por el que el modelo ajusta su comportamiento según los patrones del prompt sin modificar sus pesos. Ocurre durante la inferencia, no equivale a reentrenar, desaparece al cerrar la sesión o cambiar el prompt, y depende del contexto: ejemplos distintos pueden producir comportamientos muy diferentes.

Es flexible, porque puede cambiarse en cada llamada, pero también frágil, por depender de la selección y el orden de los ejemplos. Cuando se necesita un comportamiento estable y persistente, la alternativa es el ajuste fino (fine-tuning), que exige datos, coste y mantenimiento. Para empezar e iterar rápido, el aprendizaje en contexto suele ser la opción más ágil.

---

## 1.9 Selección de buenos ejemplos para Few-shot

La eficacia del Few-shot depende directamente de la calidad del conjunto de ejemplos. Un ejemplo inadecuado puede degradar el rendimiento por debajo del nivel Zero-shot.

- **Cubrir casos frecuentes**: Los ejemplos deben representar las situaciones más habituales en producción, no casos atípicos.
- **Incluir excepciones importantes**: Al menos un ejemplo de caso límite o excepción ayuda al modelo a manejar situaciones fronterizas.
- **Evitar contradicciones**: Dos ejemplos con la misma entrada y salidas diferentes confunden al modelo y degradan la consistencia.
- **Consistencia de etiquetas**: Usar exactamente las mismas etiquetas en todos los ejemplos; variaciones tipográficas cuentan como categorías distintas.
- **Sin datos sensibles reales**: Nunca incluir PII, credenciales ni información confidencial en los ejemplos de un prompt.

**Explicación**

La eficacia del few-shot depende de la calidad del conjunto de ejemplos; uno inadecuado puede empeorar el rendimiento por debajo del zero-shot. Hay cinco criterios: cubrir los casos frecuentes de producción, incluir al menos un caso límite o excepción, evitar contradicciones (misma entrada con salidas distintas), mantener etiquetas idénticas en todos los ejemplos (una variación tipográfica cuenta como otra categoría) y no incluir datos sensibles reales.

La consistencia de etiquetas importa: «Error técnico», «error técnico» y «Error Técnico» pueden interpretarse como tres categorías y romper el procesamiento posterior. Los ejemplos viajan al servicio con cada llamada, por lo que conviene usar ejemplos sintéticos o anonimizados. El conjunto debe tratarse como un activo de calidad: se diseña, revisa, versiona y prueba.

---

## 1.10 Cantidad y orden de ejemplos: optimizar el contexto

**Cantidad**

Añadir más ejemplos no mejora necesariamente el resultado. A partir de un umbral, el rendimiento se estabiliza o incluso decrece por sobrecarga del contexto.

- Prioriza variedad informativa frente a cantidad.
- Evita ejemplos redundantes que consuman tokens sin aportar información nueva.
- Considera el presupuesto de contexto del modelo al diseñar el conjunto.

**Orden**

Algunos modelos muestran sensibilidad al orden de los ejemplos. El último ejemplo puede tener un peso mayor (efecto de recencia).

- Coloca los ejemplos más representativos al final si detectas sensibilidad al orden.
- Prueba al menos dos órdenes distintos con el mismo conjunto de evaluación.
- No elijas el orden basándote solo en casos favorables.

> Regla práctica: comienza con 3-5 ejemplos diversos y mide antes de ampliar el conjunto.

**Explicación**

Añadir más ejemplos no mejora necesariamente el resultado: a partir de cierto punto el rendimiento se estabiliza o incluso baja por sobrecargar el contexto. Conviene priorizar la variedad informativa frente a la cantidad, evitar ejemplos redundantes y tener en cuenta el presupuesto de contexto.

El orden también puede importar: algunos modelos dan más peso a los últimos ejemplos (efecto de recencia), por lo que, si se detecta sensibilidad, se colocan al final los más representativos, se prueban al menos dos órdenes y no se elige según los casos favorables. La regla práctica es empezar con tres a cinco ejemplos diversos y medir antes de ampliar; la intuición engaña y solo una evaluación con las mismas entradas distingue una mejora real de una impresión.

---

## 1.11 Zero-shot, One-shot y Few-shot: comparativa

Las tres técnicas difieren en coste de preparación, longitud del prompt y adecuación según el tipo de tarea. La elección debe basarse en evidencia, no en preferencias.

| Criterio | Zero-shot | One-shot | Few-shot |
|---|---|---|---|
| Preparación | Mínima | Baja | Media-alta |
| Longitud del prompt | Corto | Medio | Largo |
| Cobertura de variaciones | Baja | Media | Alta |
| Riesgo de sesgo | Bajo | Medio | Alto si mal curado |
| Mejor para | Tareas claras | Patrón único | Taxonomías propias |

> Compara siempre con el mismo conjunto de evaluación para evitar conclusiones sesgadas.

**Explicación**

Zero-shot, one-shot y few-shot difieren en coste de preparación, longitud del prompt y adecuación. La preparación es mínima, baja y media-alta; la longitud, corta, media y larga; la cobertura de variaciones, baja, media y alta; el riesgo de sesgo, bajo, medio y alto si los ejemplos están mal elegidos. Zero-shot sirve para tareas claras, one-shot para un patrón único y few-shot para taxonomías propias.

Hay un compromiso: más cobertura exige más preparación, más longitud y más riesgo de sesgos. También cuenta el mantenimiento, que es mayor en few-shot cuando la taxonomía cambia. Y toda comparación debe hacerse con el mismo conjunto de evaluación; de lo contrario, las conclusiones son anecdóticas.

---

## 1.12 Diseñar una evaluación comparativa justa

Para elegir entre técnicas con rigor es imprescindible diseñar una evaluación controlada que minimice los sesgos de selección y medición.

1. **Mismas entradas de prueba**: Todas las técnicas reciben exactamente las mismas entradas; nunca selecciones casos favorables para una técnica.
2. **Respuestas esperadas definidas**: Establece las respuestas correctas antes de ejecutar los prompts para evitar sesgos de confirmación.
3. **Métricas de exactitud y formato**: Mide tanto la corrección del contenido como el cumplimiento del formato especificado.
4. **Registro de errores**: Documenta los fallos específicos de cada técnica para identificar patrones y áreas de mejora.

**Explicación**

Una **evaluación comparativa** justa sigue cuatro pasos. Primero, usar las mismas entradas de prueba para todas las técnicas, sin elegir casos favorables a ninguna. Segundo, definir las respuestas correctas antes de ejecutar los prompts, para evitar el sesgo de confirmación. Tercero, medir tanto la exactitud del contenido como el cumplimiento del formato, porque un contenido correcto en un formato incorrecto puede equivaler a un fallo. Cuarto, registrar los errores de cada técnica para detectar patrones.

El registro por técnica orienta la siguiente iteración mejor que un simple porcentaje de aciertos: por ejemplo, revela que el zero-shot falla en los casos ambiguos o que el few-shot confunde dos categorías cercanas. Este método se desarrolla en el módulo [07](../07-ciclo-de-vida-y-evaluacion/README.md).

---

[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-razonamiento-y-descomposicion.md)
