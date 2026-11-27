[← Anterior](03-encadenamiento-y-roles.md) · [Índice del módulo](README.md) · [Siguiente →](05-ejemplos-errores-y-proyecto-practico.md)

# 4 · Herramientas, integración y evaluación

*Módulo 13: Diseño de sistemas de prompts*

## 4.1 Integración con herramientas externas

Los modelos de lenguaje ganan capacidad operativa cuando pueden invocar herramientas externas: búsqueda web, calculadoras, bases de datos o APIs de negocio. La clave es definir con precisión cuándo y cómo se invocan, y cómo se gestionan sus resultados.

- **Búsqueda y recuperación**: El modelo determina cuándo necesita información actualizada y formula la consulta correcta.
- **Cálculo y lógica**: Delegar operaciones matemáticas o lógicas precisas a herramientas deterministas.
- **Bases de datos y APIs**: Consultar o escribir en sistemas externos con validación de parámetros y permisos.
- **Distinguir fuente**: Siempre indicar en la respuesta qué parte proviene del modelo y qué parte de una herramienta.

> ⚠️ Tratar siempre los errores de herramientas: timeout, permisos denegados, respuesta vacía. El flujo no debe asumir que la herramienta siempre responde correctamente.

**Explicación**

Los modelos ganan capacidad operativa al invocar herramientas externas (búsqueda web, calculadoras, bases de datos o APIs de negocio), y la clave es definir cuándo y cómo se invocan y cómo se gestionan sus resultados. Se usan para búsqueda y recuperación (el modelo decide cuándo necesita información actualizada), cálculo y lógica (delegar las operaciones precisas a herramientas deterministas), bases de datos y APIs (con validación de parámetros y permisos) y para distinguir en la respuesta qué viene del modelo y qué de una herramienta.

Es coherente con el módulo [12](../12-analisis-de-informacion-y-datos/README.md): el modelo no es fiable para calcular, así que se le da una calculadora. Hay que tratar siempre los errores de herramientas (tiempo agotado, permisos denegados, respuesta vacía) y no asumir que responden bien: una herramienta que falla y un modelo que lo ignora acaban en una respuesta inventada. Indicar la fuente de cada parte aporta trazabilidad, y dar instrucciones claras sobre cuándo usar cada herramienta reduce la dependencia del criterio del modelo.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 13B · Sistema ramificado con recuperación de documentos y evaluación extremo a extremo](../../laboratorios/13B/README.md)
<!-- /labs-seccion -->

---

## 4.2 Diseño de herramientas: la descripción es un prompt

Para el modelo, el nombre, la descripción y los parámetros de una herramienta son instrucciones: una definición ambigua produce llamadas incorrectas.

- **Nombre y propósito**: Un verbo claro y una función única; evitar herramientas solapadas.
- **Cuándo usarla**: Indicar casos de uso, casos en que no debe usarse y alternativas.
- **Parámetros tipados**: Tipo, formato, rangos y valores permitidos; marcar obligatorios y opcionales.
- **Salida y errores**: Estructura de la respuesta y errores que el modelo debe interpretar.

> ⚠️ Probar cada herramienta con llamadas adversariales: argumentos ambiguos, ausentes o maliciosos. La validación real se hace en la aplicación, no en la descripción.

**Explicación**

Para el modelo, el nombre, la descripción y los parámetros de una herramienta son instrucciones, y una definición ambigua produce llamadas incorrectas o innecesarias: diseñar una herramienta es redactar un prompt. Cuatro elementos: nombre y propósito (un verbo claro y una función única, sin herramientas solapadas), cuándo usarla (casos de uso, casos en que no debe usarse y alternativas), parámetros tipados (tipo, formato, rangos y valores permitidos, obligatorios y opcionales) y salida y errores (estructura de la respuesta y errores que el modelo debe interpretar).

Las herramientas deben probarse con llamadas adversariales: argumentos ambiguos, ausentes o maliciosos. Y la validación real se hace en la aplicación, no en la descripción: una descripción cuidadosa reduce los errores del modelo, pero no impide que lo manipulen, y son los permisos mínimos, la validación de argumentos y la confirmación humana de las acciones críticas los que protegen el sistema.

---

## 4.3 Seguridad en flujos con herramientas

Cuando un sistema de prompts puede ejecutar acciones sobre sistemas externos, la seguridad deja de ser opcional. Aplicar controles de seguridad desde el diseño es más eficiente que añadirlos a posteriori.

- **Mínimo privilegio**: El sistema solo debe tener acceso a los recursos estrictamente necesarios para su función. Sin permisos de escritura si solo necesita leer.
- **Separar lectura y escritura**: Las operaciones de lectura y escritura deben ser roles distintos con autorizaciones separadas.
- **Validar parámetros**: Antes de invocar cualquier herramienta, validar que los parámetros son seguros y coherentes.
- **Confirmar acciones sensibles**: Las acciones irreversibles (eliminar, enviar, publicar) deben requerir confirmación explícita.
- **Controlar datos devueltos**: Filtrar y sanitizar las respuestas de las herramientas antes de incorporarlas al contexto.
- **Auditar**: Registrar cada invocación con parámetros, resultado y usuario que la desencadenó.

**Explicación**

Cuando un sistema puede ejecutar acciones en sistemas externos, la seguridad deja de ser opcional, y aplicarla desde el diseño es más eficiente que añadirla después. Seis controles: mínimo privilegio (sin escritura si solo necesita leer), separar lectura y escritura en roles con autorizaciones distintas, validar los parámetros antes de invocar cualquier herramienta, exigir confirmación explícita en acciones irreversibles como eliminar, enviar o publicar, filtrar y sanear las respuestas de las herramientas antes de incorporarlas al contexto y auditar cada invocación con sus parámetros, resultado y usuario.

El quinto conecta con la inyección indirecta del módulo [09](../09-seguridad-privacidad-y-uso-responsable/README.md): lo que devuelve una herramienta puede contener instrucciones maliciosas y debe tratarse como datos, no como órdenes; además, con permisos mínimos el daño de un fallo queda acotado. Separar lectura y escritura permite niveles de control distintos (consultas con pocas fricciones, modificaciones con autorización y confirmación), y la auditoría permite reconstruir un incidente.

---

## 4.4 Integración empresarial

Situar un sistema de prompts en las operaciones de una organización requiere más que conectar una API. Implica definir puntos de integración, gestionar formatos, supervisar excepciones y medir resultados en producción.

- **Punto de integración**: ¿Dónde se inserta el sistema en el flujo de trabajo existente? ¿Reemplaza un paso manual o lo asiste?
- **Origen de datos y formatos**: ¿De qué sistemas provienen los datos? Define contratos de formato con cada fuente y trata las inconsistencias.
- **Supervisión y excepciones**: ¿Quién recibe las alertas cuando el sistema falla o genera resultados anómalos?
- **Medir calidad, tiempo y coste**: Define KPIs de negocio (no solo técnicos): precisión, tiempo de resolución, coste por transacción.
- **Mantenimiento**: Los prompts son código: necesitan versionado, revisión periódica y proceso de actualización controlado.

**Explicación**

Situar un **sistema de prompts** en las operaciones de una organización requiere más que conectar una API. Hay que decidir el punto de integración (dónde se inserta y si reemplaza un paso manual o lo asiste), el origen de los datos y sus formatos (con contratos y tratamiento de las inconsistencias), quién recibe las alertas cuando el sistema falla o produce resultados anómalos, qué indicadores de negocio se medirán (precisión, tiempo de resolución, coste por transacción) y cómo se mantendrá: los prompts son código y necesitan versionado, revisión periódica y actualización controlada.

La pregunta de si reemplaza o asiste es decisiva porque cambia el nivel de supervisión: un sistema que asiste deja la decisión a una persona, y uno que reemplaza decide por sí mismo con efectos directos. Los indicadores de negocio garantizan que el sistema se valora por lo que importa a la organización: un modelo muy preciso en una métrica técnica que no reduce tiempos ni costes no justifica su integración.

---

## 4.5 Observabilidad y trazabilidad

Un sistema de prompts en producción debe ser visible: hay que poder saber qué prompt generó qué salida, cuándo, con qué modelo y con qué resultado. Sin observabilidad, el diagnóstico de fallos es imposible y la mejora continua, impracticable.

**¿Qué registrar?**

- Versión de prompt y modelo en cada llamada
- Entradas y salidas (con anonimización de datos sensibles)
- Latencia por etapa y latencia total
- Errores, reintentos y causa
- Coste de tokens por llamada y por flujo

**Alertas y monitorización**

Define umbrales de alerta para:

- Tasa de error superior al umbral acordado
- Latencia por encima del SLA definido
- Cambios de comportamiento tras actualización de modelo
- Coste diario/mensual que supere el presupuesto

Protege los datos de trazabilidad: aplica enmascaramiento o tokenización a información personal antes de registrarla.

**Explicación**

Un sistema en producción debe ser visible: hay que saber qué prompt generó qué salida, cuándo, con qué modelo y con qué resultado; sin observabilidad no hay diagnóstico ni mejora continua. Conviene registrar la versión del prompt y del modelo, las entradas y salidas (anonimizando los datos sensibles), la latencia por etapa y total, los errores y reintentos con su causa y el coste de tokens por llamada y por flujo. Y definir alertas ante una tasa de error superior al umbral, latencia por encima del acuerdo de nivel de servicio, cambios de comportamiento tras actualizar el modelo y coste que supere el presupuesto.

La trazabilidad crea su propio riesgo de privacidad: los registros pueden contener datos personales y deben enmascararse o tokenizarse y protegerse como cualquier dato sensible. La alerta por cambios tras una actualización es muy valiosa, porque el mismo prompt puede dar resultados distintos con otra versión del modelo y solo se detecta si se mide, comparando periódicamente con la suite de referencia. El desglose por etapa permite localizar cuellos de botella y fuentes de error.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 13A · Cadena de tres etapas con contratos y puertas de validación](../../laboratorios/13A/README.md) · [Laboratorio 13B · Sistema ramificado con recuperación de documentos y evaluación extremo a extremo](../../laboratorios/13B/README.md)
<!-- /labs-seccion -->

---

## 4.6 Evaluación end-to-end

Evaluar etapa por etapa no es suficiente: una cadena puede tener todas sus etapas funcionando correctamente de forma individual y aun así producir un resultado final incorrecto. La evaluación de sistema completo es imprescindible.

| Dimensión | Qué evaluar | Método |
|---|---|---|
| Calidad de etapa | ¿Cada componente cumple su contrato? | Test unitario con casos de prueba |
| Integración | ¿Los contratos entre etapas se respetan? | Test de integración con datos reales |
| Calidad final | ¿El resultado final cumple el objetivo de negocio? | Evaluación humana + rúbrica automática |
| Excepciones | ¿El sistema gestiona bien los casos límite? | Test adversarial con inputs malformados |
| Rendimiento | Latencia y coste dentro de SLA | Test de carga y monitorización |
| Supervisión humana | ¿Los revisores pueden auditar y corregir? | Revisión de muestra periódica |

**Explicación**

Evaluar etapa por etapa no basta: una cadena puede tener todas sus etapas bien individualmente y producir un resultado final incorrecto. La tabla distingue seis dimensiones: la calidad de etapa (si cada componente cumple su contrato; test unitario), la integración (si se respetan los contratos entre etapas; test con datos reales), la calidad final (si se cumple el objetivo de negocio; evaluación humana y rúbrica automática), las excepciones (casos límite; test adversarial con entradas malformadas), el rendimiento (latencia y coste dentro del nivel de servicio; carga y monitorización) y la supervisión humana (si los revisores pueden auditar y corregir; revisión periódica de muestras).

Es la pirámide de pruebas del software aplicada a sistemas con modelos, con dos añadidos propios: una rúbrica de calidad final, porque el resultado es lenguaje y no un valor exacto, y una supervisión humana periódica que detecte degradaciones que las métricas no capturan. Una cadena puede fallar de forma emergente: cada etapa cumple su contrato, pero la combinación no resuelve el problema del usuario, y solo una **evaluación de extremo a extremo** con casos representativos lo revela.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 13B · Sistema ramificado con recuperación de documentos y evaluación extremo a extremo](../../laboratorios/13B/README.md) · [Laboratorio 14 · Proyecto integrador: asistente de gestión de reclamaciones de Altanoria](../../laboratorios/14/README.md)
<!-- /labs-seccion -->

---

[← Anterior](03-encadenamiento-y-roles.md) · [Índice del módulo](README.md) · [Siguiente →](05-ejemplos-errores-y-proyecto-practico.md)
