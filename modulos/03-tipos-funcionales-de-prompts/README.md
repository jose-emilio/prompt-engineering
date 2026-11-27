[← Módulo 02](../02-fundamentos-del-prompt-engineering/README.md) · [Inicio del curso](../../README.md) · [Módulo 04 →](../04-tecnicas-avanzadas-de-prompting/README.md)

# Módulo 03 · Tipos funcionales de prompts

*Parte I · Fundamentos*

Duración estimada: 120 minutos (70 de presentación y 50 del laboratorio 03A). El laboratorio 03B es opcional.

> Aprende a reconocer, seleccionar y diseñar prompts según la operación que necesitas: instrucción directa, Q&A, completado, transformación, creatividad, resolución de problemas y simulación. Una misma fuente puede resumirse, clasificarse, traducirse o convertirse en ideas según el prompt que uses.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos y mapa del módulo](00-objetivos-del-modulo.md#objetivos-y-mapa-del-módulo)
- 1 · **[Clasificación, instrucción y transformación](01-clasificacion-instruccion-y-transformacion.md)**
   - [1.1 Cómo clasificar un prompt](01-clasificacion-instruccion-y-transformacion.md#11-cómo-clasificar-un-prompt)
   - [1.2 Prompts de instrucción directa](01-clasificacion-instruccion-y-transformacion.md#12-prompts-de-instrucción-directa)
   - [1.3 Variantes de instrucción directa](01-clasificacion-instruccion-y-transformacion.md#13-variantes-de-instrucción-directa)
   - [1.4 Prompts de pregunta-respuesta (Q&A)](01-clasificacion-instruccion-y-transformacion.md#14-prompts-de-pregunta-respuesta-qa)
   - [1.5 Q&A basado en contexto](01-clasificacion-instruccion-y-transformacion.md#15-qa-basado-en-contexto)
   - [1.6 Prompts de completado](01-clasificacion-instruccion-y-transformacion.md#16-prompts-de-completado)
   - [1.7 Prompts de transformación](01-clasificacion-instruccion-y-transformacion.md#17-prompts-de-transformación)
   - [1.8 Prompts de resumen y síntesis](01-clasificacion-instruccion-y-transformacion.md#18-prompts-de-resumen-y-síntesis)
   - [1.9 Prompts de extracción](01-clasificacion-instruccion-y-transformacion.md#19-prompts-de-extracción)
   - [1.10 Prompts de clasificación](01-clasificacion-instruccion-y-transformacion.md#110-prompts-de-clasificación)
- 2 · **[Creatividad y resolución de problemas](02-creatividad-y-resolucion-de-problemas.md)**
   - [2.1 Prompts de generación creativa](02-creatividad-y-resolucion-de-problemas.md#21-prompts-de-generación-creativa)
   - [2.2 Brainstorming divergente](02-creatividad-y-resolucion-de-problemas.md#22-brainstorming-divergente)
   - [2.3 Narrativa e historias](02-creatividad-y-resolucion-de-problemas.md#23-narrativa-e-historias)
   - [2.4 Prompts de comunicación profesional](02-creatividad-y-resolucion-de-problemas.md#24-prompts-de-comunicación-profesional)
   - [2.5 Prompts de resolución de problemas](02-creatividad-y-resolucion-de-problemas.md#25-prompts-de-resolución-de-problemas)
   - [2.6 Descomposición de problemas](02-creatividad-y-resolucion-de-problemas.md#26-descomposición-de-problemas)
   - [2.7 Prompts de comparación](02-creatividad-y-resolucion-de-problemas.md#27-prompts-de-comparación)
   - [2.8 Prompts de planificación](02-creatividad-y-resolucion-de-problemas.md#28-prompts-de-planificación)
- 3 · **[Simulación y combinación de funciones](03-simulacion-y-combinacion-de-funciones.md)**
   - [3.1 Prompts de simulación y role-playing](03-simulacion-y-combinacion-de-funciones.md#31-prompts-de-simulación-y-role-playing)
   - [3.2 Role-playing educativo](03-simulacion-y-combinacion-de-funciones.md#32-role-playing-educativo)
   - [3.3 Combinar funciones en un mismo flujo](03-simulacion-y-combinacion-de-funciones.md#33-combinar-funciones-en-un-mismo-flujo)
   - [3.4 Elegir el tipo de prompt correcto](03-simulacion-y-combinacion-de-funciones.md#34-elegir-el-tipo-de-prompt-correcto)
- 4 · **[Selección, caso integrado y síntesis](04-seleccion-caso-integrado-y-sintesis.md)**
   - [4.1 Errores frecuentes de selección](04-seleccion-caso-integrado-y-sintesis.md#41-errores-frecuentes-de-selección)
   - [4.2 Caso integrado: de documento a decisión](04-seleccion-caso-integrado-y-sintesis.md#42-caso-integrado-de-documento-a-decisión)
   - [4.3 Prompts informativos frente a generativos](04-seleccion-caso-integrado-y-sintesis.md#43-prompts-informativos-frente-a-generativos)
   - [4.4 Prompts evaluativos](04-seleccion-caso-integrado-y-sintesis.md#44-prompts-evaluativos)
   - [4.5 Diseño de salidas para cada función](04-seleccion-caso-integrado-y-sintesis.md#45-diseño-de-salidas-para-cada-función)
   - [4.6 Buenas prácticas de selección](04-seleccion-caso-integrado-y-sintesis.md#46-buenas-prácticas-de-selección)
   - [4.7 Resumen](04-seleccion-caso-integrado-y-sintesis.md#47-resumen)
   - [4.8 Comprobación de comprensión](04-seleccion-caso-integrado-y-sintesis.md#48-comprobación-de-comprensión)
   - [4.9 Comprobación de comprensión: respuestas](04-seleccion-caso-integrado-y-sintesis.md#49-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Prompt de clasificación**: Un prompt que pide asignar cada entrada a una de varias categorías fijas. ([ficha](../glosario.md#prompt-de-clasificación))
- **Prompt de extracción**: Un prompt que pide sacar datos concretos de un texto y devolverlos en un formato fijo. ([ficha](../glosario.md#prompt-de-extracción))
- **Prompt de transformación**: Un prompt que pide cambiar la forma de un texto sin cambiar su contenido: traducirlo, reescribirlo o pasarlo a una tabla. ([ficha](../glosario.md#prompt-de-transformación))
- **Prompt informativo y prompt generativo**: El informativo busca un dato verdadero de una fuente; el generativo crea contenido nuevo, y en él la creatividad es el objetivo. ([ficha](../glosario.md#prompt-informativo-y-prompt-generativo))
- **Pregunta-respuesta basada en contexto**: Responder a una pregunta usando solo un material que se aporta, y decir que no consta cuando el material no lo recoge. ([ficha](../glosario.md#pregunta-respuesta-basada-en-contexto))
- **Prompt evaluativo**: Un prompt que pide valorar un objeto concreto con criterios observables y una escala definida. ([ficha](../glosario.md#prompt-evaluativo))

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 03A · Catálogo de prompts por tipo funcional](../../laboratorios/03A/README.md) · 50 minutos · forma parte de las 30 horas del curso
- [Laboratorio 03B · Una misma tarea, tres tipos de prompt](../../laboratorios/03B/README.md) · 55 minutos · opcional

No se practican en los laboratorios: la creatividad, la resolución de problemas y la simulación (§1.6, 2.1 a 2.6, 3.1 y 3.2); el laboratorio 03A ejecuta cinco de los diez tipos de prompt y deja los demás como ampliación. Se estudian en el módulo y se practican con casos propios.
