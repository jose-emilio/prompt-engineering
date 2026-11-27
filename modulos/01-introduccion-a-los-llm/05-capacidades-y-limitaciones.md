[← Anterior](04-entrenamiento-contexto-y-generacion.md) · [Índice del módulo](README.md) · [Siguiente →](06-resumen-comprobacion-y-transicion.md)

# 5 · Capacidades y limitaciones

*Módulo 01: Introducción a los Modelos de Lenguaje Grandes (LLM)*

## 5.1 Capacidades: comprensión y transformación de texto

Los LLM pueden transformar información de una forma a otra cuando se especifican adecuadamente el objetivo, el contexto y el formato deseado. La salida debe contrastarse con el material fuente, especialmente en tareas críticas.

| Entrada | Operación | Salida |
|---|---|---|
| Política corporativa extensa | Extracción y listado | Lista de obligaciones con referencia al texto fuente |
| Informe técnico | Reformulación | Resumen ejecutivo adaptado a dirección no técnica |
| Texto en inglés | Traducción y localización | Versión en español adaptada al contexto cultural |
| Conjunto de documentos | Comparación | Diferencias y coincidencias identificadas y listadas |

Capacidades incluyen también:

- clasificación de textos
- etiquetado automático
- detección de duplicados
- extracción de entidades nombradas (fechas, personas, organizaciones)

**Explicación**

Los LLM pueden transformar información de una forma a otra si se especifican el objetivo, el contexto y el formato. Los cuatro ejemplos de la tabla combinan una entrada, una operación y una salida definida: extraer obligaciones de una política, resumir un informe técnico para una dirección no técnica, traducir y localizar un texto, y comparar documentos para listar diferencias y coincidencias. Pensar un prompt como la descripción de una transformación mejora los resultados.

También son capacidades de esta familia clasificar textos, etiquetar, detectar duplicados y extraer entidades como fechas, personas u organizaciones. En todos los casos la salida debe contrastarse con la fuente, sobre todo en tareas críticas.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 01B · Mapa de capacidades y límites de un LLM](../../laboratorios/01B/README.md)
<!-- /labs-seccion -->

---

## 5.2 Capacidades: generación, ideación y asistencia

Los LLM pueden ayudar a producir borradores, alternativas y explicaciones adaptadas. La revisión humana sigue siendo importante: la calidad de la salida depende de la especificación de la tarea y del nivel de supervisión aplicado.

- **Redacción y borradores**: Generación de contenidos, propuestas y comunicaciones adaptadas a tono y audiencia.
- **Brainstorming**: Exploración de alternativas, enfoques y soluciones ante un problema definido.
- **Explicación adaptada**: Ajuste del nivel de detalle y vocabulario a diferentes perfiles de audiencia.
- **Código y documentación**: Generación, revisión y explicación de fragmentos de código y su documentación técnica.

*Ejemplo ilustrativo: un asistente genera tres enfoques para una propuesta comercial y explica las diferencias entre ellos — el profesional selecciona, ajusta y valida el resultado.*

**Explicación**

Los LLM ayudan a redactar borradores, explorar alternativas, explicar contenidos adaptados a distintos públicos y generar o revisar código y documentación. El reparto de papeles es claro: el modelo genera y explica; la persona selecciona, ajusta y valida. La decisión y la responsabilidad siguen siendo humanas.

Conviene recordar que la fluidez de un borrador puede reducir el cuidado con que se revisa. Cuanto mejor suena un texto, más fácil resulta pasar por alto un dato inventado o una afirmación que no se puede sostener, por lo que hay que revisarlo con el mismo rigor que el trabajo de un colaborador nuevo.

---

## 5.3 Capacidades multimodales y herramientas externas

La experiencia de un asistente puede combinar el modelo con herramientas, recuperación documental y procesamiento multimodal. Cada integración introduce permisos, posibles errores y riesgos adicionales que deben gestionarse.

![El LLM como modelo central conectado a cuatro capacidades de la aplicación: 1 búsqueda web o recuperación documental, para encontrar información; 2 archivos e imágenes subidos, para acceder a tus archivos; 3 ejecución de código, para ejecutar y obtener resultados; 4 herramientas y APIs externas, para ampliar capacidades.](img/d28-1.jpg)

**Consideraciones clave**

- La entrada de archivos e imágenes depende de que la plataforma lo permita.
- La búsqueda externa puede actualizar información con datos recientes.
- La ejecución de código o herramientas solo está disponible en sistemas habilitados para ello.
- La herramienta puede aportar datos o acciones que el modelo por sí solo no realiza.

No atribuir acceso a Internet o ejecución de código a todos los modelos o interfaces. Verificar las capacidades concretas del entorno antes de diseñar la solución.

**Explicación**

Parte de lo que ofrece un asistente no depende del modelo, sino de su entorno: búsqueda web o recuperación documental, archivos e imágenes subidos, ejecución de código y herramientas o APIs externas. Cada integración añade permisos, posibles errores y riesgos. Cuando el modelo solo genera texto, el peor caso es un texto erróneo; cuando puede actuar, el peor caso es una acción errónea.

No debe suponerse que cualquier modelo o interfaz tenga acceso a internet o pueda ejecutar código. Hay que verificar las capacidades del entorno concreto antes de diseñar una solución.

---

## 5.4 Limitaciones: alucinaciones y factualidad

Un LLM puede generar afirmaciones plausibles que no están respaldadas por hechos o fuentes fiables. La formulación segura y confiada de una respuesta no demuestra que su contenido sea verdadero.

**Tipos de alucinación habituales**

- Inventar nombres, cifras, citas o referencias bibliográficas inexistentes.
- Mezclar información correcta e incorrecta en la misma respuesta.
- Presentar afirmaciones sin respaldo con tono de certeza.
- Generar URLs o fuentes que no existen o no contienen lo indicado.

**Ejemplo ilustrativo**

Si pides al modelo que cite el artículo científico que respalda una afirmación, puede devolver una respuesta con:

- Título plausible pero inventado.
- Autores que pueden existir pero no haber escrito ese trabajo.
- Revista y año verosímiles pero incorrectos.

La respuesta es convincente — y falsa.

**Qué hacer**

- Verificar externamente cualquier dato de impacto.
- No solicitar referencias sin comprobarlas después.
- Pedir al modelo que indique su nivel de certeza, aunque esto no elimina el riesgo.

> El término alucinación se introduce aquí para reconocer el fenómeno. Las técnicas de mitigación se desarrollan en el módulo [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md).

**Explicación**

Una **alucinación** es una afirmación plausible que no está respaldada por hechos ni fuentes fiables. Ocurre porque el modelo genera continuaciones probables y no dispone de un mecanismo interno que distinga «esto lo sé» de «esto suena bien»; por eso el tono seguro no indica fiabilidad.

Los tipos habituales son inventar nombres, cifras, citas o referencias; mezclar información correcta e incorrecta; presentar sin respaldo con tono de certeza; y generar direcciones web o fuentes inexistentes. Ante esto, hay que verificar externamente los datos importantes y comprobar cualquier referencia solicitada. Pedir al modelo su nivel de certeza ayuda poco, porque esa certeza también puede ser inventada. El ejemplo de la cita científica lo ilustra: título, autores, revista y año verosímiles, pero falsos. Las técnicas de mitigación se estudian en el módulo [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md).

---

## 5.5 Limitaciones: razonamiento y consistencia

Los LLM pueden fallar en cálculos, lógica, seguimiento de restricciones múltiples y consistencia entre turnos de conversación. Ni carecen siempre de razonamiento, ni lo realizan de forma infalible.

**Tipos de error frecuentes**

- Errores aritméticos o de conteo: cálculos simples que producen resultados incorrectos.
- Pérdida de condiciones: en problemas largos, puede olvidar restricciones establecidas al inicio.
- Contradicciones internas: distintas partes de una respuesta pueden ser incompatibles.
- Sensibilidad a la formulación: una pequeña variación en el prompt puede producir respuestas distintas.

**Estrategia de mitigación básica**

1. **Descomponer**: Dividir problemas complejos en pasos más pequeños y manejables.
2. **Comprobar**: Pedir al modelo que verifique sus propias condiciones y resultados.
3. **Validar**: Confirmar externamente los resultados en tareas de alto impacto.

*Ejemplo: un problema con cuatro restricciones puede producir una respuesta que cumple tres correctamente y falla en la cuarta sin señalarlo.*

**Explicación**

Los LLM pueden fallar en cálculos, lógica, seguimiento de varias restricciones y coherencia entre turnos; ni carecen siempre de razonamiento ni lo hacen sin errores. Entre los fallos frecuentes están los errores aritméticos o de conteo, el olvido de condiciones en problemas largos, las contradicciones internas y la sensibilidad a pequeños cambios de formulación.

La mitigación básica consiste en descomponer los problemas en pasos más pequeños, pedir al modelo que compruebe sus propias condiciones y validar externamente los resultados importantes. Lo peligroso es que el error no se señala: una respuesta puede cumplir tres de cuatro restricciones y fallar la cuarta sin avisar, con el mismo aspecto que una respuesta correcta.

---

## 5.6 Limitaciones: conocimiento, actualidad y contexto

El conocimiento disponible en el modelo puede estar limitado por los datos de entrenamiento, el contexto suministrado y las herramientas conectadas. La precisión depende de la calidad y pertinencia de lo que se aporta.

**1. Fuente 1**

**2. Fuente 2**

**3. Fuente 3**

**Conocimiento paramétrico**

- El modelo puede no conocer hechos posteriores a su entrenamiento.
- La fecha de corte no siempre se expone de forma sencilla ni es idéntica en todos los productos.

- **Parámetros del modelo**: Conocimiento del entrenamiento; puede no incluir hechos recientes.
- **Contexto del usuario**: Documentos y datos aportados; pueden ser incompletos o contradictorios.
- **Herramientas externas**: Búsqueda web y bases de datos; hay que evaluar las fuentes.

**Contexto y herramientas**

- La búsqueda externa puede actualizar información, pero requiere evaluar las fuentes.
- Los documentos aportados pueden ser incompletos o contradictorios.

**RESPUESTA DEL LLM**

con fiabilidad variable

> ⚠️ Evitar fechas de corte genéricas. Consultar las especificaciones de cada modelo en la documentación oficial vigente.

**Explicación**

El conocimiento del modelo procede de tres fuentes: sus parámetros (lo aprendido en el entrenamiento, que puede no incluir hechos recientes), el contexto aportado por el usuario (documentos o datos, a veces incompletos o contradictorios) y las herramientas externas (búsqueda o bases de datos, cuyas fuentes hay que evaluar). La fiabilidad de la respuesta depende de la combinación de las tres.

Su conocimiento puede estar desactualizado y es desigual: más sólido en temas muy documentados y más débil en los locales o especializados. Si se pregunta por una norma recién modificada, un modelo sin herramientas puede describir la versión anterior con seguridad. La solución es aportar el texto vigente o usar recuperación, y consultar en la documentación oficial las especificaciones de cada modelo en lugar de dar por supuestas fechas de corte genéricas.

---

## 5.7 Sesgos, privacidad y seguridad: primera aproximación

El uso de LLM requiere considerar estas dimensiones desde el diseño, no como una comprobación final. La seguridad no se resuelve únicamente redactando un prompt.

- **⚖️ Sesgos**: Las respuestas pueden reproducir sesgos presentes en los datos de entrenamiento o en las instrucciones del sistema. Los resultados pueden favorecer sistemáticamente ciertas perspectivas.
- **🔒 Privacidad**: No introducir datos sensibles o confidenciales sin autorización y controles adecuados. Las entradas pueden ser utilizadas según las políticas del proveedor.
- **🛡️ Seguridad**: Las entradas externas pueden contener instrucciones maliciosas (*inyección de prompts*). Un documento aportado podría intentar modificar el comportamiento del sistema.
- **👁️ Supervisión**: Las salidas deben revisarse según el impacto de la tarea. Mayor autonomía del sistema exige mayor rigor en la validación humana.

> Solo se introducen los riesgos. El tratamiento detallado y las técnicas de mitigación corresponden a los módulos 08 (alucinaciones y sesgos) y 09 (privacidad y seguridad).

**Explicación**

**Sesgos**, privacidad y seguridad son dimensiones que deben considerarse desde el diseño, no al final, y que no se resuelven solo con un buen prompt. Los sesgos son patrones heredados de los datos o de las instrucciones, que pueden favorecer sistemáticamente ciertas perspectivas. En privacidad, no deben introducirse datos sensibles o confidenciales sin autorización y controles, porque las entradas pueden tratarse según las políticas del proveedor. En seguridad, las entradas externas pueden contener instrucciones maliciosas (prompt injection), y el modelo no siempre distingue instrucciones de datos. Por último, las salidas deben supervisarse en proporción al impacto, con más rigor cuanta más autonomía tenga el sistema.

El tratamiento detallado está en los módulos [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md) y [09](../09-seguridad-privacidad-y-uso-responsable/README.md). Por ahora basta con que estas cuatro preguntas estén presentes desde el inicio de cualquier uso.

---

## 5.8 Cómo evaluar si un LLM es adecuado para una tarea

La idoneidad no depende de elegir el modelo «más potente» — depende de analizar los requisitos concretos del caso de uso. El proceso debe comenzar siempre por los requisitos, no por el proveedor.

| Criterio | Preguntas de evaluación |
|---|---|
| Naturaleza de la tarea | ¿Es lingüística, lógica, creativa? ¿Qué complejidad tiene? |
| Calidad de la salida | ¿Qué formato y nivel de precisión se requiere? ¿Cómo se valida? |
| Actualidad y herramientas | ¿Se necesita información reciente o acceso a sistemas externos? |
| Privacidad y condiciones | ¿Qué datos se procesan? ¿Qué dice la política del proveedor? |
| Coste y operación | ¿Cuál es el volumen esperado? ¿Qué latencia es aceptable? |
| Riesgo y supervisión | ¿Cuáles son las consecuencias de un error? ¿Qué nivel de revisión se aplicará? |

*Comparación ilustrativa: generar ideas de bajo riesgo (supervisión ligera) vs. clasificar automáticamente solicitudes sensibles (supervisión estricta, validación rigurosa).*

**Explicación**

La idoneidad de un LLM no depende de elegir el modelo más potente, sino de analizar los requisitos del caso de uso, empezando por ellos y no por el proveedor. Los seis criterios de la tabla son: naturaleza de la tarea, calidad y validación de la salida, necesidad de información reciente o herramientas, privacidad y condiciones del proveedor, coste y operación, y riesgo y supervisión.

El último es el más determinante. Generar ideas de bajo riesgo admite una supervisión ligera, mientras que clasificar automáticamente solicitudes sensibles exige supervisión estricta y validación rigurosa. La misma tecnología requiere controles muy distintos según lo que cueste equivocarse. Si no se sabe cómo comprobar que una salida es correcta, todavía no existe un caso de uso.

---

[← Anterior](04-entrenamiento-contexto-y-generacion.md) · [Índice del módulo](README.md) · [Siguiente →](06-resumen-comprobacion-y-transicion.md)
