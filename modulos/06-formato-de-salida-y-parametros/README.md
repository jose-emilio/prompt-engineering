[← Módulo 05](../05-roles-personas-y-comportamiento/README.md) · [Inicio del curso](../../README.md) · [Módulo 07 →](../07-ciclo-de-vida-y-evaluacion/README.md)

# Módulo 06 · Control del formato de salida y parámetros de generación

*Parte II · Técnicas y control de la salida*

Duración estimada: 145 minutos (65 de presentación y 80 del laboratorio 06A). El laboratorio 06B es opcional.

> Aprende a especificar formatos legibles y estructurados — Markdown, JSON, XML, CSV y YAML — y a comprender los parámetros que gobiernan cómo un LLM genera sus respuestas. Del texto libre a la salida validable y consumible por máquinas.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos del módulo](00-objetivos-del-modulo.md#objetivos-del-módulo)
- 1 · **[Formatos de presentación](01-formatos-de-presentacion.md)**
   - [1.1 ¿Por qué importa el formato?](01-formatos-de-presentacion.md#11-por-qué-importa-el-formato)
   - [1.2 Elegir formato según el consumidor](01-formatos-de-presentacion.md#12-elegir-formato-según-el-consumidor)
   - [1.3 Markdown: estructura legible](01-formatos-de-presentacion.md#13-markdown-estructura-legible)
   - [1.4 Listas y tablas: elegir la estructura visual correcta](01-formatos-de-presentacion.md#14-listas-y-tablas-elegir-la-estructura-visual-correcta)
   - [1.5 Informes y plantillas: documentos repetibles](01-formatos-de-presentacion.md#15-informes-y-plantillas-documentos-repetibles)
   - [1.6 Formato y criterios de aceptación](01-formatos-de-presentacion.md#16-formato-y-criterios-de-aceptación)
- 2 · **[Salidas estructuradas](02-salidas-estructuradas.md)**
   - [2.1 Introducción a JSON](02-salidas-estructuradas.md#21-introducción-a-json)
   - [2.2 JSON: objetos y arrays](02-salidas-estructuradas.md#22-json-objetos-y-arrays)
   - [2.3 JSON: tipos y valores — evitar errores de tipado](02-salidas-estructuradas.md#23-json-tipos-y-valores--evitar-errores-de-tipado)
   - [2.4 Solicitar JSON: definir una salida consumible](02-salidas-estructuradas.md#24-solicitar-json-definir-una-salida-consumible)
   - [2.5 Salidas estructuradas nativas de la API](02-salidas-estructuradas.md#25-salidas-estructuradas-nativas-de-la-api)
   - [2.6 Esquemas y validación](02-salidas-estructuradas.md#26-esquemas-y-validación)
   - [2.7 Campos obligatorios y opcionales](02-salidas-estructuradas.md#27-campos-obligatorios-y-opcionales)
   - [2.8 Errores en salidas estructuradas: árbol de decisión](02-salidas-estructuradas.md#28-errores-en-salidas-estructuradas-árbol-de-decisión)
   - [2.9 XML: estructura jerárquica y usos](02-salidas-estructuradas.md#29-xml-estructura-jerárquica-y-usos)
   - [2.10 Solicitar XML: definir etiquetas y jerarquía](02-salidas-estructuradas.md#210-solicitar-xml-definir-etiquetas-y-jerarquía)
   - [2.11 CSV: datos tabulares planos](02-salidas-estructuradas.md#211-csv-datos-tabulares-planos)
   - [2.12 Solicitar CSV: evitar ambigüedad](02-salidas-estructuradas.md#212-solicitar-csv-evitar-ambigüedad)
   - [2.13 YAML: configuración legible](02-salidas-estructuradas.md#213-yaml-configuración-legible)
   - [2.14 Comparar JSON, XML, CSV y YAML](02-salidas-estructuradas.md#214-comparar-json-xml-csv-y-yaml)
   - [2.15 Longitud y límites de salida](02-salidas-estructuradas.md#215-longitud-y-límites-de-salida)
- 3 · **[Parámetros de generación y cierre](03-parametros-de-generacion-y-cierre.md)**
   - [3.1 Parámetros de generación](03-parametros-de-generacion-y-cierre.md#31-parámetros-de-generación)
   - [3.2 Temperature: variabilidad en la selección de tokens](03-parametros-de-generacion-y-cierre.md#32-temperature-variabilidad-en-la-selección-de-tokens)
   - [3.3 Top-p: muestreo por núcleo](03-parametros-de-generacion-y-cierre.md#33-top-p-muestreo-por-núcleo)
   - [3.4 Max tokens y límites de generación](03-parametros-de-generacion-y-cierre.md#34-max-tokens-y-límites-de-generación)
   - [3.5 Stop sequences: terminación configurable](03-parametros-de-generacion-y-cierre.md#35-stop-sequences-terminación-configurable)
   - [3.6 Reproducibilidad y variabilidad](03-parametros-de-generacion-y-cierre.md#36-reproducibilidad-y-variabilidad)
   - [3.7 Buenas prácticas de salidas estructuradas](03-parametros-de-generacion-y-cierre.md#37-buenas-prácticas-de-salidas-estructuradas)
   - [3.8 Errores frecuentes y diagnóstico](03-parametros-de-generacion-y-cierre.md#38-errores-frecuentes-y-diagnóstico)
   - [3.9 Resumen y comprobación](03-parametros-de-generacion-y-cierre.md#39-resumen-y-comprobación)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Markdown**: Un formato de texto con marcas sencillas (# para títulos, - para listas, barras para tablas) que se muestra ordenado a quien lee. ([ficha](../glosario.md#markdown))
- **JSON**: Un formato de texto para organizar datos como una ficha: cada campo tiene un nombre y un valor, y todo va entre llaves. ([ficha](../glosario.md#json))
- **Esquema**: La descripción de la ficha que se espera: qué campos tiene, de qué tipo es cada uno, cuáles son obligatorios y qué valores se admiten. ([ficha](../glosario.md#esquema))
- **Validación**: Comprobar automáticamente que una salida cumple el esquema: campos presentes, tipos correctos y valores permitidos. ([ficha](../glosario.md#validación))
- **Null (valor nulo)**: El valor que significa «no hay dato»; es distinto de cero y de un texto vacío. ([ficha](../glosario.md#null-valor-nulo))
- **Salida estructurada nativa**: Una función de la API del proveedor que obliga al modelo a respetar un esquema que se le indica. ([ficha](../glosario.md#salida-estructurada-nativa))
- **Temperatura**: Un parámetro que controla cuánto varía el modelo al elegir cada token: baja, casi siempre lo más probable; alta, más variedad. ([ficha](../glosario.md#temperatura))
- **Top-p**: Un parámetro que limita la elección del siguiente token a los más probables, hasta sumar una probabilidad p. ([ficha](../glosario.md#top-p))
- **Máximo de tokens**: El límite de tokens que puede generar una respuesta; al llegar a él, la respuesta se corta. ([ficha](../glosario.md#máximo-de-tokens))
- **Secuencia de parada**: Un texto que, al generarse, detiene de inmediato la respuesta. ([ficha](../glosario.md#secuencia-de-parada))

## Vigencia

Revisión del contenido: noviembre de 2026. La disponibilidad y el comportamiento de parámetros como la temperatura o top-p varían según el modelo y la API, y algunos modelos los limitan o los fijan. Consultar la documentación del proveedor antes de aplicar valores concretos.

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 06A · Salida consumible: Markdown, tabla y JSON validado](../../laboratorios/06A/README.md) · 80 minutos · forma parte de las 30 horas del curso
- [Laboratorio 06B · Temperatura y top-p: un experimento controlado](../../laboratorios/06B/README.md) · 50 minutos · opcional

No se practican en los laboratorios: los formatos XML, CSV y YAML (§2.9 a 2.13). Se estudian en el módulo y se practican con casos propios.
