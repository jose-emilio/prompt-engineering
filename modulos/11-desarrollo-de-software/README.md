[← Módulo 10](../10-generacion-creativa-y-contenidos/README.md) · [Inicio del curso](../../README.md) · [Módulo 12 →](../12-analisis-de-informacion-y-datos/README.md)

# Módulo 11 · Prompt Engineering aplicado al desarrollo de software

*Parte IV · Aplicaciones*

Duración estimada: 135 minutos (70 de presentación y 65 del laboratorio 11A). Los laboratorios 11B y 11C son opcionales.

> Generación, comprensión, depuración, traducción y pruebas de código con LLM. El desarrollador revisa y ejecuta siempre. Los modelos de lenguaje actúan como asistentes que aceleran cada fase del ciclo, pero la responsabilidad de verificar y validar recae en el profesional.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos del módulo y mapa del ciclo](00-objetivos-del-modulo.md#objetivos-del-módulo-y-mapa-del-ciclo)
- 1 · **[Generación de código](01-generacion-de-codigo.md)**
   - [1.1 El LLM como asistente de programación](01-generacion-de-codigo.md#11-el-llm-como-asistente-de-programación)
   - [1.2 Especificación funcional: describir el comportamiento requerido](01-generacion-de-codigo.md#12-especificación-funcional-describir-el-comportamiento-requerido)
   - [1.3 Contexto técnico: aportar información de entorno](01-generacion-de-codigo.md#13-contexto-técnico-aportar-información-de-entorno)
   - [1.4 Generación de funciones: solicitar código acotado](01-generacion-de-codigo.md#14-generación-de-funciones-solicitar-código-acotado)
   - [1.5 Generación de módulos: escalar a componentes](01-generacion-de-codigo.md#15-generación-de-módulos-escalar-a-componentes)
   - [1.6 Restricciones de código: controlar dependencias y convenciones](01-generacion-de-codigo.md#16-restricciones-de-código-controlar-dependencias-y-convenciones)
- 2 · **[Análisis y depuración](02-analisis-y-depuracion.md)**
   - [2.1 Explicación de código: comprender código existente](02-analisis-y-depuracion.md#21-explicación-de-código-comprender-código-existente)
   - [2.2 Análisis de arquitectura: examinar componentes](02-analisis-y-depuracion.md#22-análisis-de-arquitectura-examinar-componentes)
   - [2.3 Identificar dependencias: comprender librerías](02-analisis-y-depuracion.md#23-identificar-dependencias-comprender-librerías)
   - [2.4 Depuración: aportar evidencia del fallo](02-analisis-y-depuracion.md#24-depuración-aportar-evidencia-del-fallo)
   - [2.5 Trazas y excepciones: interpretar evidencia](02-analisis-y-depuracion.md#25-trazas-y-excepciones-interpretar-evidencia)
   - [2.6 Validar correcciones: no aceptar parches sin pruebas](02-analisis-y-depuracion.md#26-validar-correcciones-no-aceptar-parches-sin-pruebas)
   - [2.7 Refactorización: mejorar estructura preservando comportamiento](02-analisis-y-depuracion.md#27-refactorización-mejorar-estructura-preservando-comportamiento)
   - [2.8 Optimización de rendimiento: basar mejoras en evidencia](02-analisis-y-depuracion.md#28-optimización-de-rendimiento-basar-mejoras-en-evidencia)
- 3 · **[Traducción, pruebas y seguridad](03-traduccion-pruebas-y-seguridad.md)**
   - [3.1 Traducción entre lenguajes: convertir preservando semántica](03-traduccion-pruebas-y-seguridad.md#31-traducción-entre-lenguajes-convertir-preservando-semántica)
   - [3.2 Equivalencia de librerías: controlar sustituciones](03-traduccion-pruebas-y-seguridad.md#32-equivalencia-de-librerías-controlar-sustituciones)
   - [3.3 Pruebas unitarias: generar pruebas de comportamiento](03-traduccion-pruebas-y-seguridad.md#33-pruebas-unitarias-generar-pruebas-de-comportamiento)
   - [3.4 Casos límite y pruebas negativas: ampliar cobertura](03-traduccion-pruebas-y-seguridad.md#34-casos-límite-y-pruebas-negativas-ampliar-cobertura)
   - [3.5 Pruebas de integración: probar interacción entre componentes](03-traduccion-pruebas-y-seguridad.md#35-pruebas-de-integración-probar-interacción-entre-componentes)
   - [3.6 Documentación de código: generar documentación fiel](03-traduccion-pruebas-y-seguridad.md#36-documentación-de-código-generar-documentación-fiel)
   - [3.7 Revisión de código: evaluar con criterios explícitos](03-traduccion-pruebas-y-seguridad.md#37-revisión-de-código-evaluar-con-criterios-explícitos)
   - [3.8 Seguridad del código generado: reconocer riesgos](03-traduccion-pruebas-y-seguridad.md#38-seguridad-del-código-generado-reconocer-riesgos)
   - [3.9 Regla fundamental: no confiar en código sin ejecutar](03-traduccion-pruebas-y-seguridad.md#39-regla-fundamental-no-confiar-en-código-sin-ejecutar)
- 4 · **[Prompts completos, flujo y cierre](04-prompts-completos-flujo-y-cierre.md)**
   - [4.1 Prompt de debugging: integrar contexto y evidencia](04-prompts-completos-flujo-y-cierre.md#41-prompt-de-debugging-integrar-contexto-y-evidencia)
   - [4.2 Prompt de generación de código: integrar requisitos completos](04-prompts-completos-flujo-y-cierre.md#42-prompt-de-generación-de-código-integrar-requisitos-completos)
   - [4.3 Flujo de desarrollo asistido por LLM](04-prompts-completos-flujo-y-cierre.md#43-flujo-de-desarrollo-asistido-por-llm)
   - [4.4 Codificación con agentes](04-prompts-completos-flujo-y-cierre.md#44-codificación-con-agentes)
   - [4.5 Desarrollo dirigido por especificaciones (SDD)](04-prompts-completos-flujo-y-cierre.md#45-desarrollo-dirigido-por-especificaciones-sdd)
   - [4.6 El flujo de SDD en cinco pasos](04-prompts-completos-flujo-y-cierre.md#46-el-flujo-de-sdd-en-cinco-pasos)
   - [4.7 Anatomía de una buena especificación](04-prompts-completos-flujo-y-cierre.md#47-anatomía-de-una-buena-especificación)
   - [4.8 Límites y errores frecuentes del SDD](04-prompts-completos-flujo-y-cierre.md#48-límites-y-errores-frecuentes-del-sdd)
   - [4.9 Errores frecuentes: consolidar prácticas seguras](04-prompts-completos-flujo-y-cierre.md#49-errores-frecuentes-consolidar-prácticas-seguras)
   - [4.10 Caso integrado: pequeña aplicación de gestión de tareas](04-prompts-completos-flujo-y-cierre.md#410-caso-integrado-pequeña-aplicación-de-gestión-de-tareas)
   - [4.11 Resumen y comprobación de dominio](04-prompts-completos-flujo-y-cierre.md#411-resumen-y-comprobación-de-dominio)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Función**: Un bloque de código que recibe información (sus parámetros), aplica unas reglas y devuelve un resultado. ([ficha](../glosario.md#función))
- **Especificación funcional**: La descripción de qué debe hacer el código: entradas, salidas, reglas, errores y ejemplos, escrita antes de pedirlo. ([ficha](../glosario.md#especificación-funcional))
- **Caso de aceptación**: Un ejemplo con entradas y resultado exacto calculados a mano, que sirve para comprobar que el código hace lo especificado. ([ficha](../glosario.md#caso-de-aceptación))
- **Prueba unitaria**: Un pequeño programa que ejecuta una parte del código con unos datos y comprueba que el resultado es el esperado. ([ficha](../glosario.md#prueba-unitaria))
- **Depuración**: Encontrar la causa de un fallo en el código y corregirla, partiendo de evidencia: qué se esperaba, qué ocurrió y el mensaje de error. ([ficha](../glosario.md#depuración))
- **Traza de error y excepción**: Una excepción es el aviso de error que lanza un programa cuando algo falla; la traza es el rastro que indica dónde ocurrió. ([ficha](../glosario.md#traza-de-error-y-excepción))
- **Refactorización**: Reorganizar el código para que sea más claro sin cambiar lo que hace. ([ficha](../glosario.md#refactorización))
- **Equivalencia funcional**: Que dos versiones del código (por ejemplo, en dos lenguajes) den el mismo resultado para las mismas entradas. ([ficha](../glosario.md#equivalencia-funcional))
- **Dependencia**: Una biblioteca o servicio externo del que el código necesita para funcionar. ([ficha](../glosario.md#dependencia))
- **Desarrollo dirigido por especificaciones (SDD)**: Un modo de trabajo en el que se escribe primero una especificación detallada y un agente de codificación la ejecuta, con pruebas que comprueban el resultado. ([ficha](../glosario.md#desarrollo-dirigido-por-especificaciones-sdd))

## Vigencia

Revisión del contenido: noviembre de 2026. Las herramientas de asistencia al código y las guías de seguridad (por ejemplo, OWASP) se actualizan con frecuencia. Los agentes de codificación y las herramientas de desarrollo dirigido por especificaciones cambian con rapidez; los principios (especificar, dividir, verificar y revisar) no dependen de la herramienta.

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 11A · Especificar y generar una función con pruebas](../../laboratorios/11A/README.md) · 65 minutos · forma parte de las 30 horas del curso
- [Laboratorio 11B · Depurar con evidencia y revisar código sin delegar el criterio](../../laboratorios/11B/README.md) · 60 minutos · opcional
- [Laboratorio 11C · Traducir y documentar código sin perder el comportamiento](../../laboratorios/11C/README.md) · 70 minutos · opcional

No se practican en los laboratorios: la generación de módulos (§1.5), el análisis de arquitectura y de dependencias (§2.2 y 2.3), la optimización de rendimiento (§2.8) y las pruebas de integración (§3.5). Se estudian en el módulo y se practican con casos propios.
