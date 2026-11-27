[← Módulo 11](../11-desarrollo-de-software/README.md) · [Inicio del curso](../../README.md) · [Módulo 13 →](../13-diseno-de-sistemas-de-prompts/README.md)

# Módulo 12 · Prompt Engineering para análisis de información y datos

*Parte IV · Aplicaciones*

Duración estimada: 120 minutos (65 de presentación y 55 del laboratorio 12A). Los laboratorios 12B y 12C son opcionales.

> Extracción, estructuración, síntesis e interpretación de contenido no estructurado. Generación y validación de código analítico con Python. Un módulo práctico para transformar documentos y datasets en conocimiento accionable.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos y mapa del módulo](00-objetivos-del-modulo.md#objetivos-y-mapa-del-módulo)
- 1 · **[Extracción y estructuración](01-extraccion-y-estructuracion.md)**
   - [1.1 El LLM como asistente de análisis](01-extraccion-y-estructuracion.md#11-el-llm-como-asistente-de-análisis)
   - [1.2 Fuentes no estructuradas](01-extraccion-y-estructuracion.md#12-fuentes-no-estructuradas)
   - [1.3 Diseñar un esquema de extracción](01-extraccion-y-estructuracion.md#13-diseñar-un-esquema-de-extracción)
   - [1.4 Extracción de entidades](01-extraccion-y-estructuracion.md#14-extracción-de-entidades)
   - [1.5 Normalización de valores extraídos](01-extraccion-y-estructuracion.md#15-normalización-de-valores-extraídos)
   - [1.6 Estructuración en JSON](01-extraccion-y-estructuracion.md#16-estructuración-en-json)
   - [1.7 Extracción por lotes](01-extraccion-y-estructuracion.md#17-extracción-por-lotes)
   - [1.8 Calidad de la extracción](01-extraccion-y-estructuracion.md#18-calidad-de-la-extracción)
- 2 · **[Síntesis y toma de decisiones](02-sintesis-y-toma-de-decisiones.md)**
   - [2.1 Resumen ejecutivo](02-sintesis-y-toma-de-decisiones.md#21-resumen-ejecutivo)
   - [2.2 Resumen técnico](02-sintesis-y-toma-de-decisiones.md#22-resumen-técnico)
   - [2.3 Síntesis multidocumento](02-sintesis-y-toma-de-decisiones.md#23-síntesis-multidocumento)
   - [2.4 Comparación documental](02-sintesis-y-toma-de-decisiones.md#24-comparación-documental)
   - [2.5 Análisis de transcripciones](02-sintesis-y-toma-de-decisiones.md#25-análisis-de-transcripciones)
   - [2.6 Generación de hipótesis](02-sintesis-y-toma-de-decisiones.md#26-generación-de-hipótesis)
   - [2.7 Análisis de causas](02-sintesis-y-toma-de-decisiones.md#27-análisis-de-causas)
   - [2.8 Tendencias y patrones](02-sintesis-y-toma-de-decisiones.md#28-tendencias-y-patrones)
   - [2.9 Análisis What-if y escenarios](02-sintesis-y-toma-de-decisiones.md#29-análisis-what-if-y-escenarios)
   - [2.10 Análisis de decisiones](02-sintesis-y-toma-de-decisiones.md#210-análisis-de-decisiones)
   - [2.11 Límites del análisis textual con LLMs](02-sintesis-y-toma-de-decisiones.md#211-límites-del-análisis-textual-con-llms)
- 3 · **[Análisis con Python](03-analisis-con-python.md)**
   - [3.1 Python para análisis asistido por LLM](03-analisis-con-python.md#31-python-para-análisis-asistido-por-llm)
   - [3.2 Pandas y DataFrames](03-analisis-con-python.md#32-pandas-y-dataframes)
   - [3.3 Limpieza y transformación de datos](03-analisis-con-python.md#33-limpieza-y-transformación-de-datos)
   - [3.4 Estadística descriptiva](03-analisis-con-python.md#34-estadística-descriptiva)
   - [3.5 Visualización con Matplotlib](03-analisis-con-python.md#35-visualización-con-matplotlib)
   - [3.6 Prompt para código analítico](03-analisis-con-python.md#36-prompt-para-código-analítico)
   - [3.7 Validar código y resultados](03-analisis-con-python.md#37-validar-código-y-resultados)
   - [3.8 Caso completo: de documentos a indicadores](03-analisis-con-python.md#38-caso-completo-de-documentos-a-indicadores)
   - [3.9 Errores frecuentes y buenas prácticas](03-analisis-con-python.md#39-errores-frecuentes-y-buenas-prácticas)
   - [3.10 Resumen](03-analisis-con-python.md#310-resumen)
   - [3.11 Comprobación de comprensión](03-analisis-con-python.md#311-comprobación-de-comprensión)
   - [3.12 Comprobación de comprensión: respuestas](03-analisis-con-python.md#312-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Esquema de extracción**: La lista de campos que se quieren sacar de un texto, con su tipo, sus valores permitidos y qué escribir cuando el dato no consta. ([ficha](../glosario.md#esquema-de-extracción))
- **Normalización**: Llevar valores escritos de formas distintas a un único formato. ([ficha](../glosario.md#normalización))
- **Valor inventado, omitido y equivocado**: Los tres errores de una extracción: inventado (el dato no consta y el asistente puso uno), omitido (consta y puso null) y equivocado (puso otro valor distinto). ([ficha](../glosario.md#valor-inventado-omitido-y-equivocado))
- **Resumen ejecutivo y resumen técnico**: El ejecutivo es breve y orientado a decidir; el técnico es más detallado y recoge los datos y los métodos. ([ficha](../glosario.md#resumen-ejecutivo-y-resumen-técnico))
- **Síntesis multidocumento**: Combinar la información de varios documentos en un único texto, indicando de dónde sale cada dato y qué se contradice. ([ficha](../glosario.md#síntesis-multidocumento))
- **Contradicción entre fuentes**: Dos fuentes que dan datos distintos sobre lo mismo; a veces es un error y a veces una diferencia de definición, de población o de método. ([ficha](../glosario.md#contradicción-entre-fuentes))
- **DataFrame (pandas)**: Una tabla de datos dentro de Python, con filas y columnas, sobre la que se pueden calcular totales, medias o recuentos; pandas es la biblioteca que la maneja. ([ficha](../glosario.md#dataframe-pandas))
- **Limpieza de datos**: Corregir antes de calcular los problemas de los datos: filas repetidas, nombres escritos de varias formas, unidades mezcladas y huecos. ([ficha](../glosario.md#limpieza-de-datos))
- **Referencia independiente**: Un resultado calculado por otro camino (a mano o con fórmulas) con el que se compara el que da el código. ([ficha](../glosario.md#referencia-independiente))

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 12A · Extracción estructurada de correos de clientes](../../laboratorios/12A/README.md) · 55 minutos · forma parte de las 30 horas del curso
- [Laboratorio 12B · Síntesis multidocumento para un decisor](../../laboratorios/12B/README.md) · 50 minutos · opcional
- [Laboratorio 12C · Análisis de datos con Python asistido por un modelo](../../laboratorios/12C/README.md) · 60 minutos · opcional
