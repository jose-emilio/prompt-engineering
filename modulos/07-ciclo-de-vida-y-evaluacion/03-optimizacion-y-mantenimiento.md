[← Anterior](02-evaluacion.md) · [Índice del módulo](README.md) · [Siguiente →](04-despliegue-gobernanza-y-cierre.md)

# 3 · Optimización y mantenimiento

*Módulo 07: Ciclo de vida, evaluación y optimización de prompts*

## 3.1 Refinamiento de instrucciones: cambios concretos y verificables

El refinamiento es la traducción de los hallazgos del análisis de errores en modificaciones precisas del prompt. Cada cambio debe ser lo suficientemente acotado como para poder atribuirle los resultados observados.

- **Aclarar verbos y alcance**: "*Resume*" → "*Resume en máximo 3 frases el problema principal, sin mencionar soluciones*"
- **Añadir contexto necesario**: Si el modelo no tiene información suficiente para decidir, proporcionársela explícitamente en el prompt.
- **Incluir ejemplos**: Cuando el modelo no capta el patrón esperado, un ejemplo de entrada y salida correcta es más efectivo que más instrucciones.
- **Precisar restricciones y excepciones**: Añadir explícitamente los casos que deben tratarse de forma diferente al flujo principal.
- **Ajustar formato y repetir pruebas**: Verificar con la suite completa que el cambio mejora los casos objetivo sin degradar los que ya funcionaban.

**Explicación**

El refinamiento traduce los hallazgos del análisis de errores en modificaciones precisas y lo bastante acotadas como para atribuirles los resultados. Cinco tipos de cambio: aclarar verbos y alcance («Resume» pasa a «Resume en máximo 3 frases el problema principal, sin mencionar soluciones»), añadir el contexto necesario, incluir ejemplos cuando el modelo no capta el patrón, precisar restricciones y excepciones, y ajustar el formato repitiendo las pruebas.

Van, aproximadamente, de menor a mayor esfuerzo, y es razonable probarlos en ese orden. El último punto es el control de calidad: ejecutar la suite completa, porque un cambio que arregla los casos objetivo pero rompe otros no es una mejora. Cada cambio debe atribuirse a una causa identificada; modificar el prompt porque «quedaría mejor», sin hipótesis, conduce al ajuste aleatorio.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 07B · Iterar con hipótesis, regresiones y evaluación final](../../laboratorios/07B/README.md)
<!-- /labs-seccion -->

---

## 3.2 Control de regresiones: proteger lo que ya funciona

Una mejora que resuelve un fallo pero rompe diez casos que antes funcionaban no es una mejora, es un intercambio desfavorable. Las pruebas de regresión garantizan que cada iteración sea un avance neto.

**Principios de la suite de regresión**

- Mantener un conjunto estable de pruebas de referencia
- Ejecutar la suite completa tras cada cambio en el prompt
- Detectar tanto mejoras como degradaciones
- Registrar las excepciones aceptadas con justificación
- No aprobar un cambio basándose en un único caso exitoso

**Qué registrar en cada ejecución**

- Versión del prompt evaluada
- Fecha y modelo utilizado
- Resultados por caso (aprobado / fallado)
- Comparación con la versión anterior
- Decisión: aprobar, rechazar o escalar

**Explicación**

Una mejora que resuelve un fallo pero rompe diez casos que funcionaban es un intercambio desfavorable. Las pruebas de regresión garantizan que cada iteración sea un avance neto: se mantiene un conjunto estable de referencia, se ejecuta completo tras cada cambio, se detectan mejoras y degradaciones, se registran las excepciones aceptadas con su justificación y no se aprueba un cambio por un único caso exitoso.

En cada ejecución se registra la versión evaluada, fecha y modelo, resultados por caso, comparación con la versión anterior y decisión (aprobar, rechazar o escalar). La estabilidad del conjunto permite comparar versiones en el tiempo; si cambia en cada ejecución, no se sabe si la diferencia viene del prompt o de las pruebas. A veces una mejora importante degrada ligeramente un caso de poco peso: es legítimo si se decide de forma consciente y se documenta.

---

## 3.3 Versionado de prompts: gestionar cambios con trazabilidad

El versionado convierte el prompt en un activo gestionado. Sin trazabilidad, es imposible saber qué versión está en producción, quién la aprobó o por qué se realizó un cambio. El registro mínimo debe permitir reproducir cualquier estado anterior.

| Campo | Descripción | Ejemplo |
|---|---|---|
| Identificador | Nombre y número de versión únicos | clasificador-tickets-v1.4 |
| Fecha | Fecha de creación o modificación | 2025-06-10 |
| Responsable | Persona que realizó el cambio | Ana García |
| Modelo y configuración | Modelo, temperatura y parámetros clave | [modelo y versión], temp=0.2 |
| Cambio y motivo | Qué se modificó y por qué | Añadido ejemplo → reducir errores de formato |
| Resultados y estado | Métricas obtenidas y si está aprobado | F1=0.91 — Aprobado para producción |

**Explicación**

El **versionado** convierte el prompt en un activo gestionado; sin trazabilidad no se sabe qué versión está en producción, quién la aprobó ni por qué se cambió. El registro mínimo incluye un identificador único (por ejemplo «clasificador-tickets-v1.4»), la fecha, el responsable, el modelo y la configuración, el cambio y su motivo, y los resultados y el estado de aprobación.

Cada campo responde a una pregunta que tarde o temprano se formula cuando algo falla. El motivo es el más valioso a largo plazo: un cambio sin motivo documentado se vuelve misterioso y alguien podría eliminarlo por superfluo, reintroduciendo el problema que resolvía. Los prompts pueden gestionarse con las mismas herramientas de control de versiones que el código; lo esencial es la disciplina de registrar cada cambio con su contexto y evidencia.

---

## 3.4 Documentación mínima útil

La documentación de un prompt no es un trámite burocrático: es la información que permite a otro profesional (o al mismo autor meses después) entender qué hace el sistema, por qué se tomaron las decisiones clave y cómo mantenerlo.

- **Propósito y alcance**: Qué problema resuelve, quién lo usa y qué queda fuera del alcance definido.
- **Entradas y salidas**: Formato, campos obligatorios, comportamiento ante ausencia y esquema de respuesta.
- **Prompt y variables**: Texto completo del prompt con las variables nombradas y sus valores por defecto.
- **Modelo y parámetros**: Modelo específico, temperatura, top\_p y cualquier restricción de configuración relevante.
- **Limitaciones y pruebas**: Qué no hace bien el sistema, casos no soportados y resultados del conjunto de pruebas de referencia.

**Explicación**

La documentación de un prompt no es un trámite: permite a otra persona, o al propio autor meses después, entender qué hace el sistema, por qué se tomaron las decisiones clave y cómo mantenerlo. La documentación mínima útil incluye propósito y alcance, entradas y salidas, el prompt con sus variables y valores por defecto, modelo y parámetros, y limitaciones y resultados de las pruebas de referencia.

«Mínima» es deliberado: una documentación exhaustiva que nadie mantiene queda obsoleta, y una breve y al día es más útil. Documentar lo que el sistema no hace bien es un acto de honestidad que evita aplicarlo a casos para los que no fue diseñado. Debe vivir junto al prompt para actualizarse a la vez que él.

---

## 3.5 Variables y plantillas: separar contenido fijo y dinámico

Las plantillas parametrizadas permiten reutilizar un prompt en múltiples contextos cambiando solo los valores variables. Esta separación mejora la mantenibilidad, reduce errores y facilita la validación de entradas antes de enviarlas al modelo.

**Ejemplo de plantilla parametrizada *(ilustrativo)***

```text
Eres un asistente de soporte para {{empresa}}.
Idioma de respuesta: {{idioma | default: "español"}}.
Ticket recibido:
---
{{ticket_text}}
---
Clasifica en una de: {{categorias}}.
```

**Buenas prácticas**

- Variables nombradas: usar nombres descriptivos, no posicionales
- Valores por defecto: definir qué ocurre si una variable está vacía
- Validación de campos: comprobar antes de construir el prompt
- Delimitadores claros: separar datos de usuario con marcadores explícitos
- Evitar concatenación insegura: que el contenido del usuario no pueda sobrescribir instrucciones del sistema

**Explicación**

Las plantillas parametrizadas permiten reutilizar un prompt en distintos contextos cambiando solo los valores variables, lo que mejora el mantenimiento, reduce errores y facilita validar las entradas. El ejemplo define un asistente de soporte para una empresa (variable), con idioma de respuesta por defecto en español, el texto del ticket delimitado entre líneas y una lista de categorías (variable).

Las buenas prácticas son usar variables con nombres descriptivos y no posicionales, definir valores por defecto, validar campos antes de construir el prompt, delimitar con marcadores los datos del usuario y evitar la concatenación insegura. La última enlaza con la seguridad: si el texto del ticket se pega sin delimitar, un usuario malintencionado puede insertar una orden que el modelo interprete como parte del prompt. Delimitar reduce el riesgo, aunque no lo elimina (módulo [09](../09-seguridad-privacidad-y-uso-responsable/README.md)). Además, un cambio en la parte fija se aplica una sola vez a todos los usos.

---

## 3.6 Pruebas entre modelos y versiones: evaluar portabilidad

Un prompt diseñado para un modelo concreto no garantiza el mismo comportamiento en otro. Los cambios de versión, proveedor o configuración pueden afectar al formato de salida, la capacidad de seguimiento de instrucciones o el coste operativo.

- **Mismo conjunto de pruebas**: Usar exactamente la misma suite para comparar modelos. Sin esta condición, la comparación no es válida.
- **Diferencias de formato y capacidades**: Algunos modelos respetan mejor las instrucciones de formato. Otros tienen capacidades específicas (visión, herramientas, contexto largo) que pueden cambiar el diseño del prompt.
- **Coste, latencia y dependencias**: Comparar el coste por llamada, el tiempo de respuesta medio y las dependencias de proveedor que pueden crear riesgo de bloqueo (vendor lock-in).

> La matriz modelo-tarea es un recurso ilustrativo para registrar el rendimiento de cada modelo en cada tipo de caso, facilitando la decisión de selección o migración.

**Explicación**

Un prompt diseñado para un modelo no garantiza el mismo comportamiento en otro: los cambios de versión, proveedor o configuración pueden afectar al formato de salida, al seguimiento de instrucciones o al coste. Hay que usar exactamente la misma suite para comparar modelos, tener en cuenta las diferencias de formato y capacidades (visión, herramientas, contexto largo) y comparar coste, **latencia** y dependencias que pueden crear bloqueo de proveedor (vendor lock-in).

La matriz modelo-tarea registra el rendimiento de cada modelo en cada tipo de caso y facilita decidir la selección o la migración. Es necesaria porque los proveedores actualizan y retiran versiones, de modo que una migración forzosa puede producirse en cualquier momento, y contar con la suite lista permite evaluarla en horas. Además, a menudo un modelo más pequeño y barato basta para una tarea concreta, algo que solo se descubre probando con casos propios.

---

## 3.7 Coste, latencia y eficiencia: criterios operativos

La calidad técnica de un prompt no es suficiente si el sistema no es viable en producción. Los criterios operativos deben evaluarse junto con los de calidad desde el principio del ciclo de vida, no como una consideración posterior.

**~70%**

**N+1**

- **3. Dimensiones clave**: Calidad, coste y latencia. Las tres deben equilibrarse según los requisitos del caso de uso.
- **Reducción típica de tokens**: Instrucciones más precisas suelen reducir la longitud del prompt y la salida sin perder calidad (resultado ilustrativo).
- **Llamadas encadenadas**: Cada llamada adicional al modelo multiplica coste y latencia. Minimizar el número de llamadas es un objetivo de diseño.

Nunca sacrificar controles de seguridad, validación de salida o tratamiento de errores por reducir tokens. La eficiencia debe obtenerse en las partes del prompt que no afectan a las garantías del sistema.

**Explicación**

La calidad técnica no basta si el sistema no es viable en producción, y los criterios operativos se evalúan desde el principio del ciclo de vida. Las tres dimensiones son calidad, coste y latencia, que deben equilibrarse según el caso de uso. Instrucciones más precisas suelen reducir la longitud del prompt y de la salida sin perder calidad (la cifra del 70 % es ilustrativa), y cada llamada adicional al modelo multiplica coste y latencia, por lo que minimizar llamadas es un objetivo de diseño.

El equilibrio depende del caso: un asistente en tiempo real prioriza latencia, un proceso nocturno puede aceptar más latencia a cambio de menos coste y una tarea de alto riesgo prioriza calidad. Nunca deben sacrificarse controles de seguridad, validación de salida ni tratamiento de errores por ahorrar tokens: la eficiencia se obtiene en las partes que no afectan a las garantías, y se mide con datos.

---

## 3.8 Reducir coste y latencia sin perder calidad

La eficiencia se obtiene con diseño y medición, nunca recortando validación, seguridad o tratamiento de errores. Las condiciones de precio y de caché cambian: consulta al proveedor.

- **Prefijo estable y caché**: Fijo primero, variable después; el prefijo repetido puede abaratarse.
- **Modelo según la tarea**: Probar un modelo menor en extracción y clasificación y reservar el mayor para tareas complejas.
- **Contexto mínimo**: Pasar solo los fragmentos necesarios y resumir el historial.
- **Presupuesto de tokens**: Estimar entrada y salida por llamada y por flujo, fijar un límite de salida y alertas de gasto.
- **Medir antes de optimizar**: Comparar coste, latencia y calidad de cada versión con las mismas pruebas.

**Explicación**

Reducir coste y latencia sin perder calidad se consigue con diseño y medición, nunca recortando validación, seguridad o tratamiento de errores. Cinco medidas: mantener un prefijo estable, colocando primero lo fijo (instrucciones, ejemplos, esquema) y después lo variable, porque algunos proveedores abaratan el prefijo repetido, con condiciones que varían y deben consultarse; elegir el modelo según la tarea, probando uno menor en extracción y clasificación con la misma suite; reducir el contexto al mínimo, con solo los fragmentos necesarios y el historial resumido; fijar un presupuesto de tokens, con límite de salida y alertas de gasto; y medir antes de optimizar, comparando coste, latencia y calidad de cada versión con las mismas pruebas.

Una optimización que abarata la llamada pero degrada el resultado no es una mejora. El equilibrio se decide con datos y según los requisitos del caso de uso.

---

[← Anterior](02-evaluacion.md) · [Índice del módulo](README.md) · [Siguiente →](04-despliegue-gobernanza-y-cierre.md)
