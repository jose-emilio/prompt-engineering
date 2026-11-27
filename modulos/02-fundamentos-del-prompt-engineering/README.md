[← Módulo 01](../01-introduccion-a-los-llm/README.md) · [Inicio del curso](../../README.md) · [Módulo 03 →](../03-tipos-funcionales-de-prompts/README.md)

# Módulo 02 · Fundamentos del Prompt Engineering

*Parte I · Fundamentos*

Duración estimada: 155 minutos (75 de presentación y 80 del laboratorio 02A). El laboratorio 02B es opcional.

> Curso: Prompt Engineering — Diseño, optimización y aplicación profesional de prompts De formular preguntas a diseñar instrucciones: aprende a construir especificaciones de tarea claras, contextualizadas y verificables que orienten el comportamiento de los modelos hacia resultados útiles.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos de aprendizaje](00-objetivos-del-modulo.md#objetivos-de-aprendizaje)
- 1 · **[Introducción: qué es Prompt Engineering](01-introduccion-que-es-prompt-engineering.md)**
   - [1.1 Recorrido del módulo](01-introduccion-que-es-prompt-engineering.md#11-recorrido-del-módulo)
   - [1.2 Qué es Prompt Engineering](01-introduccion-que-es-prompt-engineering.md#12-qué-es-prompt-engineering)
   - [1.3 Más allá de hacer preguntas](01-introduccion-que-es-prompt-engineering.md#13-más-allá-de-hacer-preguntas)
   - [1.4 Prompt como contrato de tarea](01-introduccion-que-es-prompt-engineering.md#14-prompt-como-contrato-de-tarea)
   - [1.5 Cuándo merece la pena estructurar un prompt](01-introduccion-que-es-prompt-engineering.md#15-cuándo-merece-la-pena-estructurar-un-prompt)
- 2 · **[Anatomía de un prompt](02-anatomia-de-un-prompt.md)**
   - [2.1 Anatomía general de un prompt](02-anatomia-de-un-prompt.md#21-anatomía-general-de-un-prompt)
   - [2.2 Componente 1: Rol o perspectiva](02-anatomia-de-un-prompt.md#22-componente-1-rol-o-perspectiva)
   - [2.3 Componente 2: Contexto](02-anatomia-de-un-prompt.md#23-componente-2-contexto)
   - [2.4 Componente 3: Instrucción o tarea](02-anatomia-de-un-prompt.md#24-componente-3-instrucción-o-tarea)
   - [2.5 Componente 4: Datos de entrada](02-anatomia-de-un-prompt.md#25-componente-4-datos-de-entrada)
   - [2.6 Componente 5: Restricciones y condiciones](02-anatomia-de-un-prompt.md#26-componente-5-restricciones-y-condiciones)
   - [2.7 Componente 6: Formato de salida](02-anatomia-de-un-prompt.md#27-componente-6-formato-de-salida)
   - [2.8 Componente 7: Criterios de calidad](02-anatomia-de-un-prompt.md#28-componente-7-criterios-de-calidad)
   - [2.9 Cómo se relacionan los componentes](02-anatomia-de-un-prompt.md#29-cómo-se-relacionan-los-componentes)
   - [2.10 Plantilla reutilizable de prompt](02-anatomia-de-un-prompt.md#210-plantilla-reutilizable-de-prompt)
- 3 · **[Principios de diseño](03-principios-de-diseno.md)**
   - [3.1 Claridad frente a ambigüedad](03-principios-de-diseno.md#31-claridad-frente-a-ambigüedad)
   - [3.2 Especificidad sin sobrecargar el prompt](03-principios-de-diseno.md#32-especificidad-sin-sobrecargar-el-prompt)
   - [3.3 Concisión y relevancia del contexto](03-principios-de-diseno.md#33-concisión-y-relevancia-del-contexto)
   - [3.4 Verbos de acción y estructura de instrucciones](03-principios-de-diseno.md#34-verbos-de-acción-y-estructura-de-instrucciones)
   - [3.5 Descomponer tareas complejas](03-principios-de-diseno.md#35-descomponer-tareas-complejas)
   - [3.6 Instrucciones positivas y negativas](03-principios-de-diseno.md#36-instrucciones-positivas-y-negativas)
   - [3.7 Delimitadores y separación de secciones](03-principios-de-diseno.md#37-delimitadores-y-separación-de-secciones)
   - [3.8 Instrucciones contradictorias y prioridades](03-principios-de-diseno.md#38-instrucciones-contradictorias-y-prioridades)
   - [3.9 Manejo de información ausente o incierta](03-principios-de-diseno.md#39-manejo-de-información-ausente-o-incierta)
- 4 · **[Ejemplos, revisión y síntesis](04-ejemplos-revision-y-sintesis.md)**
   - [4.1 Ejemplo completo: resumen ejecutivo](04-ejemplos-revision-y-sintesis.md#41-ejemplo-completo-resumen-ejecutivo)
   - [4.2 Ejemplo completo: clasificación de solicitudes](04-ejemplos-revision-y-sintesis.md#42-ejemplo-completo-clasificación-de-solicitudes)
   - [4.3 Checklist para revisar un prompt](04-ejemplos-revision-y-sintesis.md#43-checklist-para-revisar-un-prompt)
   - [4.4 Errores frecuentes en el diseño de prompts](04-ejemplos-revision-y-sintesis.md#44-errores-frecuentes-en-el-diseño-de-prompts)
   - [4.5 Principios de un prompt eficaz](04-ejemplos-revision-y-sintesis.md#45-principios-de-un-prompt-eficaz)
   - [4.6 Comprobación de comprensión](04-ejemplos-revision-y-sintesis.md#46-comprobación-de-comprensión)
   - [4.7 Comprobación de comprensión: respuestas](04-ejemplos-revision-y-sintesis.md#47-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Contrato de tarea**: Un prompt escrito como un encargo claro: qué se quiere, con qué datos, qué hacer, en qué forma y cómo se comprobará que está bien. ([ficha](../glosario.md#contrato-de-tarea))
- **Contexto**: La información de fondo que ayuda al modelo a entender la situación: quién pregunta, para qué se usará el resultado y qué se sabe del caso. ([ficha](../glosario.md#contexto))
- **Datos de entrada**: El material concreto sobre el que el modelo debe operar: el texto que hay que resumir, el correo que hay que clasificar. ([ficha](../glosario.md#datos-de-entrada))
- **Restricciones**: Los límites que la respuesta debe respetar: la longitud, el tono, lo que no puede decir o inventar. ([ficha](../glosario.md#restricciones))
- **Criterios de calidad**: Condiciones observables que permiten comprobar si la respuesta es buena, sin depender de la impresión. ([ficha](../glosario.md#criterios-de-calidad))
- **Delimitadores**: Marcas (encabezados, etiquetas, comillas) que separan las instrucciones de los datos para que no se mezclen. ([ficha](../glosario.md#delimitadores))
- **Descomposición de tareas**: Dividir una tarea compleja en etapas más pequeñas, cada una con su objetivo y su salida. ([ficha](../glosario.md#descomposición-de-tareas))

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 02A · Del prompt vago al contrato de tarea](../../laboratorios/02A/README.md) · 80 minutos · forma parte de las 30 horas del curso
- [Laboratorio 02B · Anatomía de un prompt: ablación de componentes](../../laboratorios/02B/README.md) · 45 minutos · opcional
