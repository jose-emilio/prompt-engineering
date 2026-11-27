[Inicio del curso](../../README.md) · [Módulo 02 →](../02-fundamentos-del-prompt-engineering/README.md)

# Módulo 01 · Introducción a los Modelos de Lenguaje Grandes (LLM)

*Parte I · Fundamentos*

Duración estimada: 135 minutos (70 de presentación y 65 del laboratorio 01A). El laboratorio 01B es opcional.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos de aprendizaje](00-objetivos-del-modulo.md#objetivos-de-aprendizaje)
- 1 · **[Objetivos y contexto de la IA](01-objetivos-y-contexto-de-la-ia.md)**
   - [1.1 Mapa del módulo](01-objetivos-y-contexto-de-la-ia.md#11-mapa-del-módulo)
   - [1.2 De la IA tradicional a la IA generativa](01-objetivos-y-contexto-de-la-ia.md#12-de-la-ia-tradicional-a-la-ia-generativa)
   - [1.3 Evolución de los sistemas generativos](01-objetivos-y-contexto-de-la-ia.md#13-evolución-de-los-sistemas-generativos)
- 2 · **[Qué es un LLM](02-que-es-un-llm.md)**
   - [2.1 ¿Qué es un Modelo de Lenguaje Grande (LLM)?](02-que-es-un-llm.md#21-qué-es-un-modelo-de-lenguaje-grande-llm)
   - [2.2 LLM, chatbot y aplicación: no son lo mismo](02-que-es-un-llm.md#22-llm-chatbot-y-aplicación-no-son-lo-mismo)
   - [2.3 Modelos propietarios y modelos de pesos abiertos](02-que-es-un-llm.md#23-modelos-propietarios-y-modelos-de-pesos-abiertos)
   - [2.4 Tareas habituales que pueden realizar los LLM](02-que-es-un-llm.md#24-tareas-habituales-que-pueden-realizar-los-llm)
   - [2.5 Multimodalidad: más allá del texto](02-que-es-un-llm.md#25-multimodalidad-más-allá-del-texto)
- 3 · **[Cómo funciona un LLM](03-como-funciona-un-llm.md)**
   - [3.1 Concepto de tokenización](03-como-funciona-un-llm.md#31-concepto-de-tokenización)
   - [3.2 Del texto a las representaciones vectoriales: embeddings](03-como-funciona-un-llm.md#32-del-texto-a-las-representaciones-vectoriales-embeddings)
   - [3.3 Arquitectura Transformer: visión general](03-como-funciona-un-llm.md#33-arquitectura-transformer-visión-general)
   - [3.4 Mecanismo de atención (Attention)](03-como-funciona-un-llm.md#34-mecanismo-de-atención-attention)
   - [3.5 Predicción del siguiente token](03-como-funciona-un-llm.md#35-predicción-del-siguiente-token)
   - [3.6 Generación condicionada por el contexto](03-como-funciona-un-llm.md#36-generación-condicionada-por-el-contexto)
- 4 · **[Entrenamiento, contexto y generación](04-entrenamiento-contexto-y-generacion.md)**
   - [4.1 Entrenamiento e inferencia](04-entrenamiento-contexto-y-generacion.md#41-entrenamiento-e-inferencia)
   - [4.2 Preentrenamiento y ajuste posterior](04-entrenamiento-contexto-y-generacion.md#42-preentrenamiento-y-ajuste-posterior)
   - [4.3 Ventana de contexto (Context Window)](04-entrenamiento-contexto-y-generacion.md#43-ventana-de-contexto-context-window)
   - [4.4 Temperatura y selección de tokens: intuición](04-entrenamiento-contexto-y-generacion.md#44-temperatura-y-selección-de-tokens-intuición)
- 5 · **[Capacidades y limitaciones](05-capacidades-y-limitaciones.md)**
   - [5.1 Capacidades: comprensión y transformación de texto](05-capacidades-y-limitaciones.md#51-capacidades-comprensión-y-transformación-de-texto)
   - [5.2 Capacidades: generación, ideación y asistencia](05-capacidades-y-limitaciones.md#52-capacidades-generación-ideación-y-asistencia)
   - [5.3 Capacidades multimodales y herramientas externas](05-capacidades-y-limitaciones.md#53-capacidades-multimodales-y-herramientas-externas)
   - [5.4 Limitaciones: alucinaciones y factualidad](05-capacidades-y-limitaciones.md#54-limitaciones-alucinaciones-y-factualidad)
   - [5.5 Limitaciones: razonamiento y consistencia](05-capacidades-y-limitaciones.md#55-limitaciones-razonamiento-y-consistencia)
   - [5.6 Limitaciones: conocimiento, actualidad y contexto](05-capacidades-y-limitaciones.md#56-limitaciones-conocimiento-actualidad-y-contexto)
   - [5.7 Sesgos, privacidad y seguridad: primera aproximación](05-capacidades-y-limitaciones.md#57-sesgos-privacidad-y-seguridad-primera-aproximación)
   - [5.8 Cómo evaluar si un LLM es adecuado para una tarea](05-capacidades-y-limitaciones.md#58-cómo-evaluar-si-un-llm-es-adecuado-para-una-tarea)
- 6 · **[Resumen, comprobación y transición](06-resumen-comprobacion-y-transicion.md)**
   - [6.1 Resumen: modelo mental para trabajar con LLM](06-resumen-comprobacion-y-transicion.md#61-resumen-modelo-mental-para-trabajar-con-llm)
   - [6.2 Comprobación de comprensión](06-resumen-comprobacion-y-transicion.md#62-comprobación-de-comprensión)
   - [6.3 Comprobación de comprensión: respuestas](06-resumen-comprobacion-y-transicion.md#63-comprobación-de-comprensión-respuestas)
   - [6.4 Transición: del modelo al prompt](06-resumen-comprobacion-y-transicion.md#64-transición-del-modelo-al-prompt)
- 7 · **[Anexo: familias de modelos](07-anexo-familias-de-modelos.md)**
   - [7.1 Anexo (1/2): modelos propietarios](07-anexo-familias-de-modelos.md#71-anexo-12-modelos-propietarios)
   - [7.2 Anexo (2/2): modelos abiertos y especializados](07-anexo-familias-de-modelos.md#72-anexo-22-modelos-abiertos-y-especializados)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Token**: Un trozo de texto (una palabra, parte de una palabra o un signo) que es la unidad con la que el modelo lee y escribe. ([ficha](../glosario.md#token))
- **Tokenización**: El paso que corta el texto en tokens antes de dárselo al modelo. ([ficha](../glosario.md#tokenización))
- **Embedding**: Una representación del texto como una lista de números, de modo que los textos con significado parecido quedan cerca unos de otros. ([ficha](../glosario.md#embedding))
- **Transformer**: El tipo de red neuronal en el que se basan los LLM actuales; su idea clave es relacionar cada token con los demás del texto para decidir cuál va después. ([ficha](../glosario.md#transformer))
- **Atención (mecanismo de atención)**: El cálculo que permite al modelo dar más peso a unas partes del texto que a otras al generar cada token. ([ficha](../glosario.md#atención-mecanismo-de-atención))
- **Ventana de contexto**: La cantidad máxima de texto, medida en tokens, que el modelo puede tener en cuenta a la vez, contando lo que se le da y lo que contesta. ([ficha](../glosario.md#ventana-de-contexto))
- **Inferencia**: El momento en que el modelo ya entrenado se usa para generar una respuesta, a diferencia del entrenamiento, en el que aprendió. ([ficha](../glosario.md#inferencia))
- **LLM, chatbot y aplicación**: El LLM es el modelo; el chatbot es la interfaz de conversación; la aplicación añade instrucciones, datos, herramientas, memoria y controles. ([ficha](../glosario.md#llm-chatbot-y-aplicación))

## Vigencia

Revisión del contenido: noviembre de 2026. Las familias de modelos, sus tamaños, ventanas de contexto y capacidades cambian con cada versión. Los conceptos (tokens, atención, predicción del siguiente token) son estables; las cifras y los nombres de modelos, no.

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 01A · Tokens, ventana de contexto y coste](../../laboratorios/01A/README.md) · 65 minutos · forma parte de las 30 horas del curso
- [Laboratorio 01B · Mapa de capacidades y límites de un LLM](../../laboratorios/01B/README.md) · 55 minutos · opcional
