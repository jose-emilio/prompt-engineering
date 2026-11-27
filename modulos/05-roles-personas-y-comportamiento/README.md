[← Módulo 04](../04-tecnicas-avanzadas-de-prompting/README.md) · [Inicio del curso](../../README.md) · [Módulo 06 →](../06-formato-de-salida-y-parametros/README.md)

# Módulo 05 · Roles, personas y comportamiento

*Parte II · Técnicas y control de la salida*

Duración estimada: 120 minutos (70 de presentación y 50 del laboratorio 05A). El laboratorio 05B es opcional.

> Aprende a diseñar prompts que controlen perspectiva, responsabilidades, tono, estilo, audiencia y profundidad. Este módulo te dota de las herramientas para construir asistentes especializados, coherentes y alineados con objetivos profesionales reales.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos y mapa del módulo](00-objetivos-del-modulo.md#objetivos-y-mapa-del-módulo)
- 1 · **[Roles y personas](01-roles-y-personas.md)**
   - [1.1 ¿Qué aporta un rol al prompt?](01-roles-y-personas.md#11-qué-aporta-un-rol-al-prompt)
   - [1.2 Rol, persona, identidad y especialización](01-roles-y-personas.md#12-rol-persona-identidad-y-especialización)
   - [1.3 Cómo seleccionar un rol pertinente](01-roles-y-personas.md#13-cómo-seleccionar-un-rol-pertinente)
   - [1.4 Definir responsabilidades del rol](01-roles-y-personas.md#14-definir-responsabilidades-del-rol)
   - [1.5 Definir límites del rol](01-roles-y-personas.md#15-definir-límites-del-rol)
- 2 · **[Audiencia, tono y estilo](02-audiencia-tono-y-estilo.md)**
   - [2.1 Audiencia destinataria: adaptar la respuesta al lector](02-audiencia-tono-y-estilo.md#21-audiencia-destinataria-adaptar-la-respuesta-al-lector)
   - [2.2 Tono y formalidad: controlar el registro comunicativo](02-audiencia-tono-y-estilo.md#22-tono-y-formalidad-controlar-el-registro-comunicativo)
   - [2.3 Estilos de escritura: técnico, divulgativo y ejecutivo](02-audiencia-tono-y-estilo.md#23-estilos-de-escritura-técnico-divulgativo-y-ejecutivo)
   - [2.4 Voz y consistencia: mantener la identidad comunicativa](02-audiencia-tono-y-estilo.md#24-voz-y-consistencia-mantener-la-identidad-comunicativa)
- 3 · **[Profundidad, comportamiento y asistentes](03-profundidad-comportamiento-y-asistentes.md)**
   - [3.1 Profundidad y nivel de detalle](03-profundidad-comportamiento-y-asistentes.md#31-profundidad-y-nivel-de-detalle)
   - [3.2 Control de longitud: solicitar la extensión útil](03-profundidad-comportamiento-y-asistentes.md#32-control-de-longitud-solicitar-la-extensión-útil)
   - [3.3 Contexto profesional: adaptar el rol al entorno](03-profundidad-comportamiento-y-asistentes.md#33-contexto-profesional-adaptar-el-rol-al-entorno)
   - [3.4 Instrucciones de comportamiento: cómo interactúa el asistente](03-profundidad-comportamiento-y-asistentes.md#34-instrucciones-de-comportamiento-cómo-interactúa-el-asistente)
   - [3.5 Especificación de un asistente especializado](03-profundidad-comportamiento-y-asistentes.md#35-especificación-de-un-asistente-especializado)
   - [3.6 Asistente de soporte técnico de primer nivel](03-profundidad-comportamiento-y-asistentes.md#36-asistente-de-soporte-técnico-de-primer-nivel)
   - [3.7 Asistente de análisis documental](03-profundidad-comportamiento-y-asistentes.md#37-asistente-de-análisis-documental)
   - [3.8 Asistente de gestión de proyectos](03-profundidad-comportamiento-y-asistentes.md#38-asistente-de-gestión-de-proyectos)
   - [3.9 Asistente de comunicación](03-profundidad-comportamiento-y-asistentes.md#39-asistente-de-comunicación)
- 4 · **[Técnicas avanzadas, errores y síntesis](04-tecnicas-avanzadas-errores-y-sintesis.md)**
   - [4.1 Roles múltiples: separar perspectivas secuenciales](04-tecnicas-avanzadas-errores-y-sintesis.md#41-roles-múltiples-separar-perspectivas-secuenciales)
   - [4.2 Rol evaluador: crítica estructurada con rúbrica](04-tecnicas-avanzadas-errores-y-sintesis.md#42-rol-evaluador-crítica-estructurada-con-rúbrica)
   - [4.3 Roles contraproducentes: detectar diseños deficientes](04-tecnicas-avanzadas-errores-y-sintesis.md#43-roles-contraproducentes-detectar-diseños-deficientes)
   - [4.4 Sesgo inducido por el rol: reconocer perspectivas parciales](04-tecnicas-avanzadas-errores-y-sintesis.md#44-sesgo-inducido-por-el-rol-reconocer-perspectivas-parciales)
   - [4.5 Prompt de rol completo: integrar todos los componentes](04-tecnicas-avanzadas-errores-y-sintesis.md#45-prompt-de-rol-completo-integrar-todos-los-componentes)
   - [4.6 Prueba de consistencia: evaluar la estabilidad del asistente](04-tecnicas-avanzadas-errores-y-sintesis.md#46-prueba-de-consistencia-evaluar-la-estabilidad-del-asistente)
   - [4.7 Ajuste iterativo de estilo: refinar el comportamiento](04-tecnicas-avanzadas-errores-y-sintesis.md#47-ajuste-iterativo-de-estilo-refinar-el-comportamiento)
   - [4.8 Roles y formatos: separar perspectiva y presentación](04-tecnicas-avanzadas-errores-y-sintesis.md#48-roles-y-formatos-separar-perspectiva-y-presentación)
   - [4.9 Resumen: canvas para diseñar asistentes especializados](04-tecnicas-avanzadas-errores-y-sintesis.md#49-resumen-canvas-para-diseñar-asistentes-especializados)
   - [4.10 Comprobación de comprensión](04-tecnicas-avanzadas-errores-y-sintesis.md#410-comprobación-de-comprensión)
   - [4.11 Comprobación de comprensión: respuestas](04-tecnicas-avanzadas-errores-y-sintesis.md#411-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Rol**: La función que se le pide desempeñar al asistente en la conversación, con sus responsabilidades y sus límites. ([ficha](../glosario.md#rol))
- **Persona**: Los rasgos de comunicación del asistente (cómo habla), a diferencia del rol, que es lo que hace. ([ficha](../glosario.md#persona))
- **Límites del rol**: Lo que el asistente no puede o no debe hacer, junto con lo que hace en esos casos. ([ficha](../glosario.md#límites-del-rol))
- **Tono y registro**: El nivel de formalidad y de cercanía de lo que se escribe, adaptado a quien lo lee. ([ficha](../glosario.md#tono-y-registro))
- **Voz**: La identidad comunicativa que se mantiene constante a lo largo de textos y conversaciones distintos. ([ficha](../glosario.md#voz))
- **Prompt de sistema**: El texto de instrucciones que fija el papel, las reglas y el estilo del asistente durante toda la conversación. ([ficha](../glosario.md#prompt-de-sistema))
- **Prueba de consistencia**: Comprobar con casos de prueba que el asistente mantiene su rol, sus límites y su voz a lo largo de la conversación y de varias ejecuciones. ([ficha](../glosario.md#prueba-de-consistencia))

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 05A · Un mismo contenido, tres audiencias](../../laboratorios/05A/README.md) · 50 minutos · forma parte de las 30 horas del curso
- [Laboratorio 05B · Un asistente con rol, límites y voz consistente](../../laboratorios/05B/README.md) · 55 minutos · opcional

No se practican en los laboratorios: los roles múltiples secuenciales y el rol evaluador (§4.1 y 4.2) y los asistentes de análisis documental, gestión de proyectos y comunicación (§3.7 a 3.9). Se estudian en el módulo y se practican con casos propios.
