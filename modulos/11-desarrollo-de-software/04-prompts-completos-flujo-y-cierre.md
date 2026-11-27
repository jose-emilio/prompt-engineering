[← Anterior](03-traduccion-pruebas-y-seguridad.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../12-analisis-de-informacion-y-datos/README.md)

# 4 · Prompts completos, flujo y cierre

*Módulo 11: Prompt Engineering aplicado al desarrollo de software*

## 4.1 Prompt de debugging: integrar contexto y evidencia

```text
[ROL]
Eres un ingeniero de software senior especializado en Python 3.11 y FastAPI.

[CONTEXTO DEL PROYECTO]
API REST de gestión de inventario. Framework: FastAPI 0.110. BD: PostgreSQL 15
con SQLAlchemy 2.0. Desplegado en Docker sobre Ubuntu 22.04.

[ERROR Y REPRODUCCIÓN]
Error: sqlalchemy.exc.IntegrityError — duplicate key value violates unique constraint "products_sku_key"
Ocurre al llamar POST /products con un SKU que no existe en la BD.
Pasos: 1) Iniciar servidor limpio 2) POST /products {"sku":"ABC-001","name":"Widget"}
3) Repetir la misma petición → falla en la segunda llamada.

[RESTRICCIONES]
No cambiar el esquema de BD. Mantener compatibilidad con SQLAlchemy 2.0.

[SALIDA ESPERADA]
1. Hipótesis ordenadas por probabilidad. 2. Pasos de verificación reproducibles.
3. Cambio mínimo propuesto con justificación.

```

> Ejemplo ilustrativo. Adapta cada sección a tu proyecto real antes de usar en producción.

**Explicación**

Un prompt de depuración efectivo combina cinco elementos: rol, contexto, evidencia, restricciones y formato de salida. En el ejemplo, un ingeniero senior de Python 3.11 y FastAPI recibe el contexto del proyecto (API REST de inventario con FastAPI 0.110, PostgreSQL 15 y SQLAlchemy 2.0 en Docker), el error (violación de unicidad del SKU en POST /products al repetir la petición) con sus pasos de reproducción, las restricciones (no cambiar el esquema y mantener la compatibilidad con SQLAlchemy 2.0) y la salida esperada: hipótesis ordenadas por probabilidad, pasos de verificación y un cambio mínimo con justificación.

La salida pide hipótesis y verificación, no una solución única, trasladando al modelo el método correcto: diagnosticar antes de actuar. El caso tiene un detalle instructivo: el error ocurre al repetir un SKU que ya existe, que es el comportamiento esperado de una restricción de unicidad; un buen diagnóstico distingue un fallo del código de la ausencia de un manejo adecuado del error. El ejemplo debe adaptarse al proyecto real.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 11B · Depurar con evidencia y revisar código sin delegar el criterio](../../laboratorios/11B/README.md)
<!-- /labs-seccion -->

---

## 4.2 Prompt de generación de código: integrar requisitos completos

```text
[ESPECIFICACIÓN FUNCIONAL]
Función: validate_and_normalize_email(raw_email: str) → str
- Acepta una cadena con un email potencialmente malformado.
- Devuelve el email en minúsculas y sin espacios si es válido.
- Lanza ValueError con mensaje descriptivo si el formato es inválido.
- Casos límite: None, cadena vacía, múltiples @, dominios sin punto.

[STACK Y RESTRICCIONES]
Python 3.11. Sin dependencias externas. Estilo PEP 8. 
Prohibido usar regex de terceros; solo módulo re de stdlib.

[CÓDIGO Y ESTRUCTURA ESPERADOS]
Archivo: utils/email_utils.py. Docstring Google style. Type hints completos.

[PRUEBAS REQUERIDAS]
Suite pytest completa: casos válidos, inválidos, límites y None.
Cobertura mínima: 10 casos de prueba.

[SUPUESTOS EXPLÍCITOS]
Si asumes algo no especificado, indícalo explícitamente antes del código.

```

> Ejemplo ilustrativo. La clave es que el LLM declare sus supuestos antes de generar código.

**Explicación**

Este es el equivalente para generar código: un prompt completo que integra **especificación funcional**, pila y restricciones, estructura y pruebas, y supuestos. La función validate_and_normalize_email recibe una cadena con un correo posiblemente malformado, lo devuelve en minúsculas y sin espacios si es válido y lanza ValueError con un mensaje descriptivo si no lo es, con casos límite como None, cadena vacía, varias arrobas y dominios sin punto. La pila es Python 3.11 sin dependencias externas, PEP 8 y solo el módulo re; el archivo es utils/email_utils.py con docstring de estilo Google y anotaciones de tipo; y se pide una suite pytest con al menos diez casos.

El último bloque es la clave: pedir al modelo que declare sus supuestos antes del código convierte las decisiones implícitas en explícitas y permite corregirlas antes de revisar cientos de líneas. Cada parte evita una ambigüedad, y su longitud está justificada por obtener un resultado utilizable en menos iteraciones.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 11A · Especificar y generar una función con pruebas](../../laboratorios/11A/README.md)
<!-- /labs-seccion -->

---

## 4.3 Flujo de desarrollo asistido por LLM

El prompting para código no es un acto puntual sino un proceso integrado en el ciclo de desarrollo. Cada fase tiene su propio tipo de prompt y sus propios criterios de validación.

1. **Requisito y diseño**: Especificación funcional, contexto técnico, restricciones y criterios de aceptación
2. **Generación**: Prompt de código con firma, tipos, ejemplos y restricciones de dependencias
3. **Revisión y pruebas**: Revisión humana + generación de suite de pruebas + ejecución en entorno controlado
4. **Integración**: Verificar contratos de interfaces, compatibilidad y ausencia de regresiones
5. **Documentación**: Generar docstrings y README fiel al comportamiento implementado y verificado
6. **Mantenimiento**: Refactorización y optimización basada en evidencia, con tests de regresión

**Explicación**

El prompting para código es un proceso integrado en el ciclo de desarrollo, con un tipo de prompt y unos criterios de validación en cada fase: requisito y diseño (especificación, contexto, restricciones y criterios de aceptación), generación (firma, tipos, ejemplos y dependencias), revisión y pruebas (revisión humana, suite de pruebas y ejecución en entorno controlado), integración (contratos, compatibilidad y regresiones), documentación fiel a lo implementado y mantenimiento (refactorización y optimización basadas en evidencia, con tests de regresión).

Es el recorrido de las secciones anteriores ordenado como flujo, y la validación no se deja para el final: es más barato detectar un malentendido en la especificación que en producción. Se parece al ciclo de vida de un prompt del módulo [07](../07-ciclo-de-vida-y-evaluacion/README.md): los prompts de código se versionan y evalúan, y el código que producen pasa por la revisión habitual.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 11C · Traducir y documentar código sin perder el comportamiento](../../laboratorios/11C/README.md)
<!-- /labs-seccion -->

---

## 4.4 Codificación con agentes

**Contexto persistente**

- Un archivo de instrucciones del proyecto (AGENTS.md o CLAUDE.md) recoge comandos de compilación y pruebas, y convenciones
- Debe ser breve, concreto y verificable: es contexto para el agente, no una norma que se haga cumplir sola
- Nunca incluyas secretos ni datos de clientes

**Controles imprescindibles**

- Mínimo privilegio y confirmación humana antes de ejecutar comandos o cambios sensibles
- Conecta herramientas y datos con MCP solo desde servidores de confianza
- Revisa el diff y ejecuta las pruebas: el agente también puede equivocarse con seguridad
- Acota cada tarea y mantén los cambios pequeños para poder revisarlos

El agente acelera la iteración, pero revisar, probar y aprobar sigue siendo responsabilidad del desarrollador.

**Explicación**

Los **agentes de codificación** no solo proponen código: lo ejecutan, editan archivos y lanzan comandos de forma autónoma en el repositorio. Necesitan contexto persistente: un archivo de instrucciones del proyecto (AGENTS.md o CLAUDE.md) con comandos de compilación y pruebas y convenciones, breve, concreto y verificable (es contexto para el agente, no una norma que se haga cumplir sola) y sin secretos ni datos de clientes.

Los controles imprescindibles son el mínimo privilegio y la confirmación humana antes de comandos o cambios sensibles, conectar herramientas y datos con MCP solo desde servidores de confianza, revisar el diff y ejecutar las pruebas (el agente también puede equivocarse con seguridad) y acotar las tareas con cambios pequeños. El agente acelera la iteración, pero la responsabilidad de revisar, probar y aprobar sigue siendo de quien desarrolla. Los riesgos crecen porque puede actuar, no solo escribir, y una instrucción incorrecta en el archivo de instrucciones influye en todo lo que haga el agente (módulos [09](../09-seguridad-privacidad-y-uso-responsable/README.md) y [13](../13-diseno-de-sistemas-de-prompts/README.md)).

---

## 4.5 Desarrollo dirigido por especificaciones (SDD)

El desarrollo dirigido por especificaciones (SDD, del inglés spec-driven development) toma la especificación como artefacto principal: describe qué debe hacer el sistema y cómo se comprobará, y el agente la implementa. El código es el resultado; lo que se revisa y se mantiene es la especificación.

- **Pedir cambios sueltos**: Instrucciones breves y sucesivas en el chat. Es rápido para tareas pequeñas, pero la intención queda repartida en la conversación y es difícil de revisar o de repetir.
- **Partir de una especificación**: Objetivo, alcance y criterios de aceptación escritos antes de empezar. El agente trabaja contra un documento que una persona puede revisar y versionar.

> Compensa cuando la tarea es grande, la ejecutan varios agentes o personas o el resultado debe poder auditarse. Para un cambio de dos líneas sobra.

**Explicación**

El **desarrollo dirigido por especificaciones** (SDD) consiste en escribir primero una especificación que describa qué debe hacer el sistema y cómo se comprobará, y encargar después su implementación a un agente. Es la versión estructurada de algo que ya se ha visto en el módulo: especificar antes de pedir código. La diferencia está en la escala: con un agente que edita archivos y ejecuta comandos, una instrucción vaga produce cambios grandes y difíciles de revisar.

Pedir cambios sueltos sigue siendo razonable para tareas pequeñas. La especificación compensa cuando la tarea es grande, la reparten varios agentes o varias personas, o el resultado debe poder auditarse: el documento fija la intención en un solo sitio, se puede revisar antes de gastar tiempo en código y sirve de referencia para comprobar el resultado.

---

## 4.6 El flujo de SDD en cinco pasos

Las herramientas y los nombres de las fases cambian con rapidez; lo estable son los artefactos y los puntos de revisión humana.

1. **Especificar**: Objetivo, alcance y criterios de aceptación. Revisión humana: ¿es esto lo que se necesita?
2. **Planificar**: Enfoque técnico, componentes afectados y restricciones. Revisión humana: ¿es una solución aceptable?
3. **Dividir en tareas**: Tareas pequeñas, ordenadas y con su propia comprobación.
4. **Implementar**: El agente ejecuta una tarea cada vez y deja los cambios listos para revisar.
5. **Verificar**: Pruebas y revisión del diff contra la especificación. Si algo falla, se corrige la especificación o el código; no se improvisa en el chat.

> Las personas revisan sobre todo en dos puntos: la especificación y el plan. Corregir un error ahí cuesta mucho menos que corregirlo en el código.

**Explicación**

El flujo se repite en casi todas las variantes del SDD: especificar, planificar, dividir en tareas, implementar y verificar. Las herramientas lo nombran y lo automatizan de formas distintas y esos detalles envejecen pronto, pero los artefactos (la especificación, el plan y la lista de tareas) y los momentos de revisión son estables.

Las dos primeras fases son las que más piden juicio humano: especificar es decidir qué se quiere y planificar es decidir cómo, y un error en cualquiera de ellas se propaga a todo lo demás. Dividir en tareas pequeñas, cada una con su comprobación, permite revisar el diff por partes y detectar pronto cuándo el agente se desvía. La verificación final compara el resultado con los criterios de aceptación de la especificación y no con la impresión de que «parece correcto»; si falla, se decide si el problema está en la especificación o en el código y se corrige donde esté.

---

## 4.7 Anatomía de una buena especificación

Una especificación útil para un agente responde a seis preguntas y deja poco espacio a las suposiciones.

- **Objetivo y contexto**: Qué se quiere conseguir y para quién.
- **Alcance y exclusiones**: Qué entra en el trabajo y qué no se toca.
- **Criterios de aceptación**: Condiciones medibles, con ejemplos de entrada y salida.
- **Restricciones técnicas**: Lenguaje y versión, dependencias permitidas, API pública que no cambia.
- **Casos límite y errores**: Valores extremos, entradas inválidas y cómo debe reaccionar el sistema.
- **Definición de «hecho»**: Qué pruebas deben pasar y qué documentación se actualiza.

Ejemplo ilustrativo: «*Calcular la factura mensual de Altanoria Copilot. Alcance: planes Starter, Team y Enterprise; no incluye impuestos. Criterios: 5 usuarios en Team con facturación mensual → 145,00 €; 4 usuarios en Team → error de validación (mínimo 5); redondeo mitad hacia arriba. Hecho cuando pasen las pruebas de aceptación sin modificarlas.*»

**Explicación**

Una buena especificación para un agente responde a seis preguntas: qué se quiere conseguir y para quién, qué entra en el trabajo y qué queda fuera, cómo se sabrá que está bien, qué restricciones técnicas hay, qué ocurre en los casos límite y qué significa que la tarea esté terminada. Es el contrato de tarea del módulo [02](../02-fundamentos-del-prompt-engineering/README.md) aplicado a código, con la misma idea de fondo: lo que no se escribe, el agente lo supone.

Los criterios de aceptación son la parte más rentable. Un criterio como «calcula bien el importe» no se puede comprobar; «5 usuarios en Team con facturación mensual dan 145,00 €» sí, y se convierte casi directamente en una prueba. El ejemplo del laboratorio 11A muestra el nivel de precisión que conviene: cifras concretas, errores esperados y una **definición de «hecho»** que impide modificar las pruebas para que pasen.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 11A · Especificar y generar una función con pruebas](../../laboratorios/11A/README.md) · [Laboratorio 11B · Depurar con evidencia y revisar código sin delegar el criterio](../../laboratorios/11B/README.md) · [Laboratorio 11C · Traducir y documentar código sin perder el comportamiento](../../laboratorios/11C/README.md)
<!-- /labs-seccion -->

---

## 4.8 Límites y errores frecuentes del SDD

El SDD no garantiza un buen resultado por sí solo: cambia dónde se invierte el esfuerzo.

- **Deriva**: Si el código cambia y la especificación no, esta deja de ser una fuente fiable. Conviene actualizar las dos en la misma tarea.
- **Demasiado o demasiado poco**: Un exceso de detalle convierte la especificación en código escrito en prosa; muy poco deja huecos que el agente rellena por su cuenta.
- **Cumplimiento no garantizado**: El agente puede ignorar o reinterpretar un requisito. Se comprueba con pruebas y con la revisión del diff, no por confianza.
- **Coste**: Redactar y revisar especificaciones lleva tiempo; compensa en tareas complejas o repetibles.

> Cuándo no usarlo: correcciones pequeñas, prototipos desechables y exploración inicial. Ahí basta un prompt acotado.

**Explicación**

El SDD desplaza el esfuerzo del código a la especificación, y eso trae sus propios riesgos. El principal es la **deriva**: cuando el código evoluciona y la especificación se queda atrás, el documento deja de ser una fuente fiable y pasa a ser un obstáculo. La práctica que lo evita es sencilla: cualquier cambio toca la especificación y el código en la misma tarea, y la revisión comprueba ambos.

También se falla por los extremos. Una especificación demasiado detallada acaba siendo el propio código en prosa, con el coste de mantener dos versiones de lo mismo; una demasiado vaga deja huecos que el agente rellena con suposiciones. Y escribir una especificación no obliga al agente a cumplirla: puede ignorar un requisito o reinterpretarlo con total seguridad, por lo que el control sigue estando en las pruebas y en la revisión del diff. Por último, tiene un coste de tiempo que solo compensa en tareas complejas o repetibles; para una corrección pequeña, un prototipo desechable o una exploración inicial basta un prompt acotado.

---

## 4.9 Errores frecuentes: consolidar prácticas seguras

Estos son los errores más comunes al usar LLM para desarrollo de software. Conocerlos y evitarlos sistemáticamente marca la diferencia entre un uso profesional y uno arriesgado.

| Error | Consecuencia | Corrección |
|---|---|---|
| Contexto insuficiente | Código genérico incompatible con el proyecto | Incluir lenguaje, versión y stack completo |
| Solicitud demasiado amplia | Resultado inmanejable y difícil de revisar | Dividir en funciones o módulos acotados |
| Versiones omitidas | APIs obsoletas o incompatibles | Especificar versión exacta siempre |
| APIs inventadas no verificadas | Errores en runtime difíciles de rastrear | Verificar en documentación oficial |
| No ejecutar pruebas | Bugs silenciosos llegan a producción | Ejecutar siempre en entorno controlado |
| Compartir secretos en el prompt | Exposición de credenciales | Usar variables de entorno, nunca hardcode |
| No revisar dependencias | Vulnerabilidades en paquetes transitivales | Auditar con pip-audit, npm audit |

**Explicación**

Esta tabla consolida los errores más comunes: contexto insuficiente (código genérico incompatible; incluir lenguaje, versión y pila), solicitud demasiado amplia (resultado inmanejable; dividir en piezas acotadas), versiones omitidas (APIs obsoletas; indicar la exacta), APIs inventadas no verificadas (errores difíciles de rastrear; verificar en la documentación), no ejecutar las pruebas (errores silenciosos en producción; ejecutar en entorno controlado), compartir secretos en el prompt (usar variables de entorno) y no revisar dependencias (vulnerabilidades en paquetes transitivos; auditar con pip-audit o npm audit).

Cada error es el reverso de una práctica del módulo, y la tabla sirve como lista de comprobación antes de enviar un prompt de código y de revisar código generado. Los errores parecen ahorrar tiempo (omitir la versión, pedir el módulo entero, saltarse las pruebas), pero el coste reaparece multiplicado en la depuración y la producción.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 11B · Depurar con evidencia y revisar código sin delegar el criterio](../../laboratorios/11B/README.md)
<!-- /labs-seccion -->

---

## 4.10 Caso integrado: pequeña aplicación de gestión de tareas

Este ejercicio recorre el ciclo completo de desarrollo asistido por LLM sobre una aplicación acotada. Cada paso utiliza las técnicas aprendidas en el módulo y produce un artefacto verificable.

1. **Definir aplicación acotada**: CLI de gestión de tareas: añadir, listar, completar y eliminar. Stack: Python 3.11, stdlib únicamente.
2. **Generar módulo**: Prompt completo con especificación funcional, restricciones y estructura de archivos esperada. El LLM genera task\_manager.py.
3. **Analizar código generado**: Pedir explicación por bloques, identificar efectos secundarios y verificar que el modelo señala sus hipótesis.
4. **Corregir fallo controlado**: Introducir un bug conocido (p. ej., ID duplicado) y aplicar el flujo completo de depuración: traza → hipótesis → parche → prueba.
5. **Crear pruebas**: Generar suite pytest con casos normales, límite y negativos. Verificar cobertura mínima del 80%.
6. **Ejecutar y revisar**: Ejecutar todas las pruebas, revisar seguridad con checklist y generar docstrings finales.

**Explicación**

El ejercicio recorre el ciclo completo sobre una aplicación acotada. Seis pasos: definir una herramienta de línea de comandos para gestionar tareas (añadir, listar, completar y eliminar) en Python 3.11 con la biblioteca estándar; generar el módulo con un prompt completo; analizar el código generado con explicación por bloques y señalando hipótesis; corregir un fallo controlado, como un identificador duplicado, con el flujo completo de depuración; crear una suite pytest con casos normales, límite y negativos y cobertura mínima del 80 %; y ejecutar y revisar todo con la lista de seguridad y los docstrings finales.

Cada paso depende del anterior y produce algo comprobable. Al ser una aplicación acotada, permite practicar el método completo sin la complejidad de un proyecto real, y el método es transferible a cualquier tamaño de código.

---

## 4.11 Resumen y comprobación de dominio

Al finalizar este módulo debes ser capaz de responder afirmativamente a cada uno de estos puntos. Si alguno genera duda, es la señal de qué repasar.

- **Especificar antes de generar**: ¿Incluyes objetivo, entradas/salidas, casos límite, restricciones y criterios de aceptación en cada prompt de código?
- **Aportar entorno**: ¿Especificas siempre lenguaje, versión, framework y convenciones del proyecto?
- **Depurar con evidencia**: ¿Aportas stack trace completo, código mínimo reproductor y entorno exacto al pedir ayuda con bugs?
- **Traducir preservando semántica**: ¿Verificas el comportamiento de errores y generas pruebas equivalentes al traducir entre lenguajes?
- **Probar límites**: ¿Cubres nulos, vacíos, límites numéricos, formatos incorrectos y dependencias no disponibles?
- **Revisar seguridad**: ¿Verificas validación de entradas, gestión de secretos e inyección antes de integrar cualquier código generado?
- **Delegar en un agente con especificación**: ¿Escribes alcance, criterios de aceptación y definición de «hecho» antes de pedir a un agente que implemente?

> Regla de oro: genera → revisa → ejecuta. El LLM acelera; el desarrollador valida.

**Explicación**

El resumen plantea siete puntos a los que se debe poder responder afirmativamente: especificar antes de generar (objetivo, entradas y salidas, casos límite, restricciones y criterios de aceptación), aportar el entorno (lenguaje, versión, framework y convenciones), depurar con evidencia (traza completa, código mínimo reproductor y entorno exacto), traducir preservando la semántica (verificar el comportamiento de errores y generar pruebas equivalentes), probar los límites (nulos, vacíos, límites numéricos, formatos incorrectos y dependencias no disponibles), revisar la seguridad (entradas, secretos e inyección) antes de integrar y, por último, delegar en un agente con una especificación (alcance, criterios de aceptación y definición de «hecho» escritos antes de pedir la implementación).

La regla de oro es generar, revisar, ejecutar: el modelo acelera y el desarrollador valida. El código que produce un modelo no es mejor ni peor por venir de un modelo: necesita revisión, pruebas y responsabilidad. El módulo siguiente aplica el prompt engineering al análisis de información y datos.

---

[← Anterior](03-traduccion-pruebas-y-seguridad.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../12-analisis-de-informacion-y-datos/README.md)
