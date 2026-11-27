[← Anterior](03-optimizacion-y-mantenimiento.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../08-fiabilidad-alucinaciones-y-sesgos/README.md)

# 4 · Despliegue, gobernanza y cierre

*Módulo 07: Ciclo de vida, evaluación y optimización de prompts*

## 4.1 Despliegue y mantenimiento: del laboratorio a producción

El ciclo de vida no termina con la aprobación del prompt. El paso a producción requiere un proceso controlado y el mantenimiento continuo garantiza que el sistema siga funcionando correctamente cuando cambian el modelo, los datos o los requisitos de negocio.

- **Entorno de prueba**: Validación completa con la suite de regresión antes de cualquier cambio
- **Control de cambios**: Aprobación formal con registro de versión y responsable
- **Monitorización**: Seguimiento de métricas en producción y alertas ante degradación
- **Retroalimentación y reversión**: Recoger señales del uso real y poder revertir a la versión anterior si es necesario

**Explicación**

El ciclo de vida no termina con la aprobación del prompt: el paso a producción requiere un proceso controlado y el mantenimiento garantiza que siga funcionando cuando cambian el modelo, los datos o los requisitos. Incluye un entorno de prueba con validación completa mediante la suite de regresión, control de cambios con aprobación formal, versión y responsable, monitorización con métricas y alertas ante degradación, y retroalimentación y reversión para poder volver a la versión anterior.

La reversión es una red de seguridad imprescindible: la versión previa debe conservarse y el despliegue estar preparado para volver atrás. La monitorización detecta el deterioro lento, difícil de percibir, y la retroalimentación del uso real cierra el círculo: los fallos que aparecen en producción y no estaban en la suite se incorporan como casos de prueba nuevos.

---

## 4.2 Gobernanza y responsabilidades

En entornos profesionales, los prompts son activos que pueden afectar a decisiones de negocio, a la experiencia del cliente o a la seguridad de la información. Definir quién tiene cada responsabilidad evita ambigüedades y garantiza la supervisión adecuada.

| Rol | Responsabilidad principal | Alcance de decisión |
|---|---|---|
| Propietario funcional | Define el caso de uso y los criterios de aceptación | Aprueba cambios de requisitos |
| Responsable técnico | Diseña, versiona y mantiene el prompt | Propone y valida cambios técnicos |
| Revisor de calidad | Ejecuta evaluación y análisis de errores | Aprueba o rechaza versiones |
| Responsable de seguridad | Revisa riesgos de inyección de prompts y datos sensibles | Supervisión según nivel de riesgo |
| Administrador de acceso | Controla quién puede modificar prompts en producción | Gestión de permisos y auditoría |

**Explicación**

Los prompts son activos que pueden afectar a decisiones de negocio, a la experiencia del cliente o a la seguridad, y definir responsabilidades evita ambigüedades. La tabla identifica cinco roles: el propietario funcional (define el caso de uso y los criterios de aceptación), el responsable técnico (diseña, versiona y mantiene), el revisor de calidad (evalúa, analiza errores y aprueba o rechaza versiones), el responsable de seguridad (revisa riesgos de inyección y datos sensibles) y el administrador de acceso (controla quién puede modificar prompts en producción).

La separación de roles protege contra conflictos de interés: quien diseña no debería ser el único que aprueba. En organizaciones pequeñas una persona puede asumir varios roles; lo importante es que las funciones estén identificadas y que, en lo posible, la aprobación de un cambio no dependa solo de quien lo propuso. El control de acceso, a menudo descuidado, evita que un cambio no revisado altere el sistema sin dejar rastro.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 07B · Iterar con hipótesis, regresiones y evaluación final](../../laboratorios/07B/README.md)
<!-- /labs-seccion -->

---

## 4.3 Caso integrado de optimización: clasificación de tickets

Este caso ilustrativo recorre el ciclo completo aplicado a un sistema de clasificación automática de tickets de soporte en categorías predefinidas. Los datos y resultados son ilustrativos.

**El ciclo aplicado**

1. Definir clasificación: 5 categorías, usuario final agente de soporte, impacto alto si se clasifica mal un ticket urgente
1. Crear baseline (v0.1): instrucción genérica sin ejemplos, temperatura 0.2, registrada con fecha y modelo
1. Diseñar pruebas: 40 tickets representativos (muestra pequeña, solo ilustrativa), 8 por categoría, incluye ambiguos y bilingües
1. Evaluar y agrupar fallos: F1=0.74; el 60% de los errores ocurre en la categoría "Facturación"
1. Modificar prompt (v0.2): se añaden dos ejemplos de tickets de Facturación correctamente clasificados
1. Comprobar regresiones: F1 global sube a 0.88; ninguna categoría empeora respecto a v0.1

**Lecciones del caso**

- El análisis de errores localizó la causa antes de intentar corregirla
- El cambio fue único y medible: solo se añadieron ejemplos
- La suite de regresión confirmó que no hubo degradación
- La v0.2 quedó registrada con métricas y estado "*aprobado para pruebas*"

**Explicación**

El caso aplica el ciclo completo a un clasificador automático de tickets de soporte en cinco categorías. Se define la clasificación (usuario, impacto alto si se clasifica mal un ticket urgente); se crea el baseline v0.1 (instrucción genérica sin ejemplos, temperatura 0,2, con fecha y modelo); se diseñan 40 tickets representativos, ocho por categoría, con ambiguos y bilingües; se evalúa (F1 de 0,74, con el 60 % de errores en «Facturación»); se modifica el prompt en la v0.2 añadiendo dos ejemplos de facturación; y se comprueban regresiones (F1 de 0,88 sin que empeore ninguna categoría).

Las lecciones: el análisis localizó la causa antes de corregirla, el cambio fue único y medible, la suite confirmó que no hubo degradación y la v0.2 quedó registrada con métricas y estado «aprobado para pruebas». Esa prudencia es deliberada: con 40 casos el resultado es prometedor, pero no concluyente; antes de producción habría que ampliar la suite, repetir ejecuciones y revisar los casos de mayor impacto.

---

## 4.4 Resumen del proceso: ciclo de vida completo

El ciclo de vida de un prompt es un proceso continuo, no una secuencia lineal con fin. Cada iteración produce conocimiento que mejora el sistema y el proceso mismo.

1

Definición del problema y criterios de aceptación

6

Versionado, documentación y mantenimiento en producción

Refinamiento guiado por hipótesis y pruebas de regresión

2

Diseño del prompt inicial (baseline v0.1)

Construcción de un conjunto de pruebas diverso

**Ciclo continuo**

Cada iteración mejora el prompt y el proceso

Evaluación cualitativa y cuantitativa con análisis de errores

5

3

4

**Explicación**

El ciclo de vida es un proceso continuo, no una secuencia lineal con final: definición del problema y criterios de aceptación, prompt inicial (baseline), conjunto de pruebas diverso, evaluación cualitativa y cuantitativa con análisis de errores, refinamiento guiado por hipótesis con pruebas de regresión, y versionado, documentación y mantenimiento. Cada iteración mejora el prompt y también el proceso.

La idea central es que la calidad de un prompt se demuestra, no se supone, con criterios previos, pruebas representativas, métricas adecuadas, cambios guiados por hipótesis, control de regresiones y trazabilidad. Ninguna práctica es sofisticada por sí sola; lo exigente es mantenerlas con constancia. El módulo [08](../08-fiabilidad-alucinaciones-y-sesgos/README.md) se centra en las fuentes de error que este proceso debe detectar: alucinaciones, sesgos y fiabilidad.

---

## 4.5 Comprobación de comprensión

Piensa cada respuesta, de forma oral o por escrito, antes de ver las respuestas orientativas, que aparecen a continuación.

**¿Qué se define antes de probar?**

**¿Por qué incluir casos límite y negativos?**

**¿Métrica y criterio de aceptación son lo mismo?**

**¿Cómo detectar regresiones?**

**¿Qué registrar por versión?**

---

## 4.6 Comprobación de comprensión: respuestas

Contrasta tus respuestas con estas. Son orientativas: lo importante es que cubran las ideas clave del módulo.

- **¿Qué se define antes de probar?** El caso de uso: usuario y necesidad, tarea, impacto del error, datos y restricciones, criterios de aceptación y el contrato de entradas y salidas.
- **¿Por qué incluir casos límite y negativos?** Porque con entradas solo típicas no se ven los fallos en los bordes ni con datos incompletos, y el prompt parecería listo sin estarlo.
- **¿Métrica y criterio de aceptación son lo mismo?** No: la métrica mide y el criterio fija el mínimo aceptable. Un prompt puede tener una métrica alta y fallar los casos críticos o el umbral exigido.
- **¿Cómo detectar regresiones?** Con una suite de referencia estable que se ejecuta completa tras cada cambio y se compara con la versión anterior.
- **¿Qué registrar por versión?** Identificador, fecha, responsable, modelo y parámetros, cambio y motivo, resultados y estado de aprobación.

**Explicación**

La comprobación plantea cinco preguntas. Antes de probar se define el caso de uso: usuario y necesidad, tarea, impacto del error, datos y restricciones, criterios de aceptación y contrato de entradas y salidas. Se incluyen casos límite y negativos porque con entradas solo típicas no se ven los fallos en los bordes y el prompt parecería listo sin estarlo. La métrica y el criterio de aceptación no son lo mismo: la métrica mide y el criterio fija el mínimo aceptable. Las regresiones se detectan con una suite estable que se ejecuta completa tras cada cambio y se compara con la versión anterior. Y por versión se registran identificador, fecha, responsable, modelo y parámetros, cambio y motivo, resultados y estado.

La tercera suele generar más confusión: una métrica es un número que describe un comportamiento, y un criterio de aceptación es una decisión sobre qué valor es suficiente y en qué casos.

---

[← Anterior](03-optimizacion-y-mantenimiento.md) · [Índice del módulo](README.md) · [Siguiente módulo →](../08-fiabilidad-alucinaciones-y-sesgos/README.md)
