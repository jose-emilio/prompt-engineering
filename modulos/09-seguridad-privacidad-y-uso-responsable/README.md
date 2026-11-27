[← Módulo 08](../08-fiabilidad-alucinaciones-y-sesgos/README.md) · [Inicio del curso](../../README.md) · [Módulo 10 →](../10-generacion-creativa-y-contenidos/README.md)

# Módulo 09 · Seguridad, privacidad y uso responsable

*Parte III · Evaluación, fiabilidad y seguridad*

Duración estimada: 115 minutos (65 de presentación y 50 del laboratorio 09A). El laboratorio 09B es opcional.

> Privacidad, inyección de prompts, Jailbreaking y fugas de información. El prompt forma parte de un sistema más amplio que requiere controles técnicos, organizativos y de supervisión para operar de forma segura y responsable.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos y agenda del módulo](00-objetivos-del-modulo.md#objetivos-y-agenda-del-módulo)
- 1 · **[Amenazas y privacidad](01-amenazas-y-privacidad.md)**
   - [1.1 Modelo de amenazas en sistemas LLM](01-amenazas-y-privacidad.md#11-modelo-de-amenazas-en-sistemas-llm)
   - [1.2 Privacidad y datos personales](01-amenazas-y-privacidad.md#12-privacidad-y-datos-personales)
   - [1.3 Qué no introducir en prompts](01-amenazas-y-privacidad.md#13-qué-no-introducir-en-prompts)
   - [1.4 Minimización y anonimización](01-amenazas-y-privacidad.md#14-minimización-y-anonimización)
   - [1.5 Gobernanza de uso](01-amenazas-y-privacidad.md#15-gobernanza-de-uso)
- 2 · **[Inyección de prompts y jailbreaking](02-inyeccion-de-prompts-y-jailbreaking.md)**
   - [2.1 Inyección de prompts: definición](02-inyeccion-de-prompts-y-jailbreaking.md#21-inyección-de-prompts-definición)
   - [2.2 Inyección directa](02-inyeccion-de-prompts-y-jailbreaking.md#22-inyección-directa)
   - [2.3 Inyección indirecta](02-inyeccion-de-prompts-y-jailbreaking.md#23-inyección-indirecta)
   - [2.4 Flujo de ataque indirecto](02-inyeccion-de-prompts-y-jailbreaking.md#24-flujo-de-ataque-indirecto)
   - [2.5 Delimitar instrucciones y datos](02-inyeccion-de-prompts-y-jailbreaking.md#25-delimitar-instrucciones-y-datos)
   - [2.6 Jerarquía de instrucciones](02-inyeccion-de-prompts-y-jailbreaking.md#26-jerarquía-de-instrucciones)
   - [2.7 Jailbreaking: definición](02-inyeccion-de-prompts-y-jailbreaking.md#27-jailbreaking-definición)
   - [2.8 Patrones de Jailbreaking](02-inyeccion-de-prompts-y-jailbreaking.md#28-patrones-de-jailbreaking)
   - [2.9 Límites de las defensas basadas en prompts](02-inyeccion-de-prompts-y-jailbreaking.md#29-límites-de-las-defensas-basadas-en-prompts)
- 3 · **[Fugas, permisos y pruebas de seguridad](03-fugas-permisos-y-pruebas-de-seguridad.md)**
   - [3.1 Fugas de información](03-fugas-permisos-y-pruebas-de-seguridad.md#31-fugas-de-información)
   - [3.2 Instrucciones internas y secretos](03-fugas-permisos-y-pruebas-de-seguridad.md#32-instrucciones-internas-y-secretos)
   - [3.3 Principio de mínimo privilegio](03-fugas-permisos-y-pruebas-de-seguridad.md#33-principio-de-mínimo-privilegio)
   - [3.4 Seguridad en asistentes con herramientas](03-fugas-permisos-y-pruebas-de-seguridad.md#34-seguridad-en-asistentes-con-herramientas)
   - [3.5 Seguridad en recuperación documental](03-fugas-permisos-y-pruebas-de-seguridad.md#35-seguridad-en-recuperación-documental)
   - [3.6 Pruebas de seguridad](03-fugas-permisos-y-pruebas-de-seguridad.md#36-pruebas-de-seguridad)
   - [3.7 Respuesta segura y escalado](03-fugas-permisos-y-pruebas-de-seguridad.md#37-respuesta-segura-y-escalado)
- 4 · **[Responsabilidad, normativa y cierre](04-responsabilidad-normativa-y-cierre.md)**
   - [4.1 Uso responsable y supervisión](04-responsabilidad-normativa-y-cierre.md#41-uso-responsable-y-supervisión)
   - [4.2 Marco normativo y estándares de referencia](04-responsabilidad-normativa-y-cierre.md#42-marco-normativo-y-estándares-de-referencia)
   - [4.3 Alfabetización y transparencia en IA](04-responsabilidad-normativa-y-cierre.md#43-alfabetización-y-transparencia-en-ia)
   - [4.4 Propiedad intelectual y contenido](04-responsabilidad-normativa-y-cierre.md#44-propiedad-intelectual-y-contenido)
   - [4.5 Transparencia y trazabilidad](04-responsabilidad-normativa-y-cierre.md#45-transparencia-y-trazabilidad)
   - [4.6 Evaluación de riesgos](04-responsabilidad-normativa-y-cierre.md#46-evaluación-de-riesgos)
   - [4.7 Caso integrado: documento malicioso y herramienta](04-responsabilidad-normativa-y-cierre.md#47-caso-integrado-documento-malicioso-y-herramienta)
   - [4.8 Resumen](04-responsabilidad-normativa-y-cierre.md#48-resumen)
   - [4.9 Comprobación de comprensión](04-responsabilidad-normativa-y-cierre.md#49-comprobación-de-comprensión)
   - [4.10 Comprobación de comprensión: respuestas](04-responsabilidad-normativa-y-cierre.md#410-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Modelo de amenazas**: Un mapa de por dónde puede entrar un ataque en un sistema con IA y qué podría pasar si entra. ([ficha](../glosario.md#modelo-de-amenazas))
- **Datos personales (PII)**: Información que identifica a una persona, sola o combinada con otra. ([ficha](../glosario.md#datos-personales-pii))
- **Minimización**: Dar al modelo solo los datos imprescindibles para la tarea. ([ficha](../glosario.md#minimización))
- **Seudonimización**: Sustituir los identificadores por marcadores y guardar aparte la tabla que los une a la persona: se puede revertir. ([ficha](../glosario.md#seudonimización))
- **Anonimización**: Eliminar o generalizar los datos de modo que nadie pueda volver a identificar a la persona, ni siquiera con información adicional. ([ficha](../glosario.md#anonimización))
- **Inyección de prompts**: Una instrucción escondida en un texto que el sistema lee, con la que se intenta cambiar lo que hace el asistente. ([ficha](../glosario.md#inyección-de-prompts))
- **Jailbreaking**: Intentar que el modelo se salte sus reglas de seguridad con trucos de redacción. ([ficha](../glosario.md#jailbreaking))
- **Jerarquía de instrucciones**: El orden de prioridad entre quien da instrucciones: primero las del sistema, después las de la aplicación y las del usuario, y por último el contenido externo, que son datos. ([ficha](../glosario.md#jerarquía-de-instrucciones))
- **Mínimo privilegio**: Dar al asistente únicamente los permisos que necesita para su tarea. ([ficha](../glosario.md#mínimo-privilegio))
- **Fuga de información**: Que el asistente revele algo que no debía: sus instrucciones internas, secretos o datos de otros clientes. ([ficha](../glosario.md#fuga-de-información))
- **Red team**: Un ejercicio en el que se ataca el sistema a propósito, con autorización, para encontrar sus fallos antes de que lo haga un atacante real. ([ficha](../glosario.md#red-team))
- **Canario**: Un dato secreto de prueba que el sistema no debe revelar nunca: si aparece en una respuesta, ha habido una fuga. ([ficha](../glosario.md#canario))

## Vigencia

Revisión del contenido: noviembre de 2026. Normativa y guías de seguridad en evolución: el calendario de aplicación del AI Act (modificado por el Reglamento (UE) 2026/1744), las obligaciones de transparencia del artículo 50 y la lista OWASP de riesgos para aplicaciones con LLM. Contrastar siempre con el texto oficial y con asesoría jurídica antes de decidir en un caso real.

Fuentes oficiales para contrastar:

- [RGPD, Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) y [Agencia Española de Protección de Datos](https://www.aepd.es/)
- [AI Act, Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) y su modificación, [Reglamento (UE) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)
- [OWASP Top 10 para aplicaciones con LLM](https://genai.owasp.org/llm-top-10/)

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 09A · Minimizar y anonimizar antes de enviar datos a un modelo](../../laboratorios/09A/README.md) · 50 minutos · forma parte de las 30 horas del curso
- [Laboratorio 09B · Red team de un asistente de buzón](../../laboratorios/09B/README.md) · 50 minutos · opcional
