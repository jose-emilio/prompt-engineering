[← Módulo 12](../12-analisis-de-informacion-y-datos/README.md) · [Inicio del curso](../../README.md)

# Módulo 13 · Diseño de sistemas de prompts

*Parte V · Sistemas de prompts y proyecto final*

Duración estimada: 140 minutos (80 de presentación y 60 del laboratorio 13A). El laboratorio 13B es opcional.

> Del prompt aislado al flujo coordinado: secuencias, contexto, encadenamiento, roles, herramientas y evaluación integrada en arquitecturas profesionales de IA.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [¿Qué aprenderás en este módulo?](00-objetivos-del-modulo.md#qué-aprenderás-en-este-módulo)
- 1 · **[De prompt individual a sistema](01-de-prompt-individual-a-sistema.md)**
   - [1.1 De prompt individual a sistema](01-de-prompt-individual-a-sistema.md#11-de-prompt-individual-a-sistema)
   - [1.2 Identificar el proceso de negocio](01-de-prompt-individual-a-sistema.md#12-identificar-el-proceso-de-negocio)
   - [1.3 Descomposición en subtareas](01-de-prompt-individual-a-sistema.md#13-descomposición-en-subtareas)
   - [1.4 Contratos entre etapas](01-de-prompt-individual-a-sistema.md#14-contratos-entre-etapas)
   - [1.5 Arquitectura secuencial](01-de-prompt-individual-a-sistema.md#15-arquitectura-secuencial)
   - [1.6 Arquitectura ramificada](01-de-prompt-individual-a-sistema.md#16-arquitectura-ramificada)
   - [1.7 Arquitectura paralela](01-de-prompt-individual-a-sistema.md#17-arquitectura-paralela)
- 2 · **[Conversaciones, contexto y estado](02-conversaciones-contexto-y-estado.md)**
   - [2.1 Conversaciones multi-turn](02-conversaciones-contexto-y-estado.md#21-conversaciones-multi-turn)
   - [2.2 Gestión del contexto](02-conversaciones-contexto-y-estado.md#22-gestión-del-contexto)
   - [2.3 Ingeniería de contexto en agentes](02-conversaciones-contexto-y-estado.md#23-ingeniería-de-contexto-en-agentes)
   - [2.4 Memoria y persistencia](02-conversaciones-contexto-y-estado.md#24-memoria-y-persistencia)
   - [2.5 Estado de tarea](02-conversaciones-contexto-y-estado.md#25-estado-de-tarea)
   - [2.6 Recuperación ante errores](02-conversaciones-contexto-y-estado.md#26-recuperación-ante-errores)
- 3 · **[Encadenamiento y roles](03-encadenamiento-y-roles.md)**
   - [3.1 Prompt Chaining: concepto](03-encadenamiento-y-roles.md#31-prompt-chaining-concepto)
   - [3.2 Diseñar una cadena de prompts](03-encadenamiento-y-roles.md#32-diseñar-una-cadena-de-prompts)
   - [3.3 Validación entre etapas](03-encadenamiento-y-roles.md#33-validación-entre-etapas)
   - [3.4 Ejemplo resuelto: contrato y puerta entre dos etapas](03-encadenamiento-y-roles.md#34-ejemplo-resuelto-contrato-y-puerta-entre-dos-etapas)
   - [3.5 Encadenamiento con fuentes documentales](03-encadenamiento-y-roles.md#35-encadenamiento-con-fuentes-documentales)
   - [3.6 Sistemas con múltiples roles](03-encadenamiento-y-roles.md#36-sistemas-con-múltiples-roles)
   - [3.7 Patrón generador-revisor](03-encadenamiento-y-roles.md#37-patrón-generador-revisor)
   - [3.8 Coordinación multiagente](03-encadenamiento-y-roles.md#38-coordinación-multiagente)
   - [3.9 Riesgos en sistemas multiagente](03-encadenamiento-y-roles.md#39-riesgos-en-sistemas-multiagente)
- 4 · **[Herramientas, integración y evaluación](04-herramientas-integracion-y-evaluacion.md)**
   - [4.1 Integración con herramientas externas](04-herramientas-integracion-y-evaluacion.md#41-integración-con-herramientas-externas)
   - [4.2 Diseño de herramientas: la descripción es un prompt](04-herramientas-integracion-y-evaluacion.md#42-diseño-de-herramientas-la-descripción-es-un-prompt)
   - [4.3 Seguridad en flujos con herramientas](04-herramientas-integracion-y-evaluacion.md#43-seguridad-en-flujos-con-herramientas)
   - [4.4 Integración empresarial](04-herramientas-integracion-y-evaluacion.md#44-integración-empresarial)
   - [4.5 Observabilidad y trazabilidad](04-herramientas-integracion-y-evaluacion.md#45-observabilidad-y-trazabilidad)
   - [4.6 Evaluación end-to-end](04-herramientas-integracion-y-evaluacion.md#46-evaluación-end-to-end)
- 5 · **[Ejemplos, errores y proyecto práctico](05-ejemplos-errores-y-proyecto-practico.md)**
   - [5.1 Ejemplo: asistente de soporte técnico](05-ejemplos-errores-y-proyecto-practico.md#51-ejemplo-asistente-de-soporte-técnico)
   - [5.2 Ejemplo: sistema de gestión documental](05-ejemplos-errores-y-proyecto-practico.md#52-ejemplo-sistema-de-gestión-documental)
   - [5.3 Errores frecuentes y anti-patrones](05-ejemplos-errores-y-proyecto-practico.md#53-errores-frecuentes-y-anti-patrones)
   - [5.4 Resumen y preparación del proyecto práctico](05-ejemplos-errores-y-proyecto-practico.md#54-resumen-y-preparación-del-proyecto-práctico)
   - [5.5 Comprobación de comprensión](05-ejemplos-errores-y-proyecto-practico.md#55-comprobación-de-comprensión)
   - [5.6 Comprobación de comprensión: respuestas](05-ejemplos-errores-y-proyecto-practico.md#56-comprobación-de-comprensión-respuestas)
- 6 · **[Anexos: chuleta, glosario y vigencia](06-anexos-chuleta-glosario-y-vigencia.md)**
   - [6.1 Chuleta del curso: plantilla de prompt](06-anexos-chuleta-glosario-y-vigencia.md#61-chuleta-del-curso-plantilla-de-prompt)
   - [6.2 Chuleta del curso: errores que se repiten](06-anexos-chuleta-glosario-y-vigencia.md#62-chuleta-del-curso-errores-que-se-repiten)
   - [6.3 Glosario (1/2)](06-anexos-chuleta-glosario-y-vigencia.md#63-glosario-12)
   - [6.4 Glosario (2/2)](06-anexos-chuleta-glosario-y-vigencia.md#64-glosario-22)
   - [6.5 Qué caduca y cuándo revisarlo](06-anexos-chuleta-glosario-y-vigencia.md#65-qué-caduca-y-cuándo-revisarlo)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Encadenamiento de prompts (prompt chaining)**: Dividir una tarea en varios prompts seguidos, de modo que la salida de cada uno es la entrada del siguiente. ([ficha](../glosario.md#encadenamiento-de-prompts-prompt-chaining))
- **Contrato entre etapas**: Lo que cada etapa recibe y lo que debe devolver, escrito de forma que se pueda comprobar. ([ficha](../glosario.md#contrato-entre-etapas))
- **Puerta de validación**: Una comprobación con reglas fijas, entre dos etapas, que decide si la salida puede pasar a la siguiente o se repite o se deriva a una persona. ([ficha](../glosario.md#puerta-de-validación))
- **Arquitectura ramificada**: Un sistema en el que un primer paso decide por qué camino sigue cada caso, según su tipo. ([ficha](../glosario.md#arquitectura-ramificada))
- **Patrón generador-revisor**: Un prompt redacta y otro, distinto, revisa el resultado con una rúbrica; si no lo aprueba, se vuelve a redactar un número limitado de veces. ([ficha](../glosario.md#patrón-generador-revisor))
- **Conversación multi-turn y gestión del contexto**: Una conversación de varios mensajes en la que hay que decidir qué parte de lo anterior se mantiene, se resume o se descarta, porque la ventana de contexto es limitada. ([ficha](../glosario.md#conversación-multi-turn-y-gestión-del-contexto))
- **Memoria y estado de tarea**: La memoria guarda información entre conversaciones; el estado de tarea apunta en qué punto está un proceso (qué se ha hecho y qué falta). ([ficha](../glosario.md#memoria-y-estado-de-tarea))
- **Observabilidad**: Registrar lo que hace cada etapa (entradas, salidas, versiones y motivos) para poder entender y corregir lo que ocurre. ([ficha](../glosario.md#observabilidad))
- **Evaluación de extremo a extremo**: Medir el sistema completo, desde la entrada del usuario hasta la respuesta final, y no solo cada pieza por separado. ([ficha](../glosario.md#evaluación-de-extremo-a-extremo))

## Vigencia

Revisión del contenido: noviembre de 2026. Incluye la nota general de vigencia del curso y un glosario cuyos términos de normativa y seguridad siguen la misma regla: contrastar con las fuentes oficiales.

Fuentes oficiales para contrastar:

- [RGPD, Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) y [Agencia Española de Protección de Datos](https://www.aepd.es/)
- [AI Act, Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) y su modificación, [Reglamento (UE) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)
- [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/)

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 13A · Cadena de tres etapas con contratos y puertas de validación](../../laboratorios/13A/README.md) · 60 minutos · forma parte de las 30 horas del curso
- [Laboratorio 13B · Sistema ramificado con recuperación de documentos y evaluación extremo a extremo](../../laboratorios/13B/README.md) · 50 minutos · opcional

No se practican en los laboratorios: la ingeniería de contexto en agentes (§2.3), los sistemas con varios roles y la coordinación multiagente (§3.6, 3.8 y 3.9) y el diseño de herramientas (§4.2). Se estudian en el módulo y se practican con casos propios.

Proyecto final (forma parte de las 30 horas del curso): [Laboratorio 14 · Proyecto integrador: asistente de gestión de reclamaciones de Altanoria](../../laboratorios/14/README.md) · 100 minutos.
