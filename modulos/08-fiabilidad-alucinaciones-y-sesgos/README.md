[← Módulo 07](../07-ciclo-de-vida-y-evaluacion/README.md) · [Inicio del curso](../../README.md) · [Módulo 09 →](../09-seguridad-privacidad-y-uso-responsable/README.md)

# Módulo 08 · Fiabilidad, alucinaciones y sesgos

*Parte III · Evaluación, fiabilidad y seguridad*

Duración estimada: 135 minutos (70 de presentación y 65 del laboratorio 08A). El laboratorio 08B es opcional.

> Respuestas no fundamentadas · Incertidumbre · Sesgos · Verificación y supervisión

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos del módulo y mapa de contenidos](00-objetivos-del-modulo.md#objetivos-del-módulo-y-mapa-de-contenidos)
- 1 · **[Alucinaciones: concepto y causas](01-alucinaciones-concepto-y-causas.md)**
   - [1.1 ¿Qué significa fiabilidad en un LLM?](01-alucinaciones-concepto-y-causas.md#11-qué-significa-fiabilidad-en-un-llm)
   - [1.2 ¿Qué es una alucinación?](01-alucinaciones-concepto-y-causas.md#12-qué-es-una-alucinación)
   - [1.3 Formas de alucinación: catálogo de patrones](01-alucinaciones-concepto-y-causas.md#13-formas-de-alucinación-catálogo-de-patrones)
   - [1.4 ¿Por qué aparecen las alucinaciones?](01-alucinaciones-concepto-y-causas.md#14-por-qué-aparecen-las-alucinaciones)
   - [1.5 Fluidez no equivale a verdad](01-alucinaciones-concepto-y-causas.md#15-fluidez-no-equivale-a-verdad)
   - [1.6 Hechos, inferencias, supuestos y opiniones](01-alucinaciones-concepto-y-causas.md#16-hechos-inferencias-supuestos-y-opiniones)
- 2 · **[Mitigación de alucinaciones](02-mitigacion-de-alucinaciones.md)**
   - [2.1 Respuestas basadas en fuentes documentales](02-mitigacion-de-alucinaciones.md#21-respuestas-basadas-en-fuentes-documentales)
   - [2.2 Diseño para la incertidumbre](02-mitigacion-de-alucinaciones.md#22-diseño-para-la-incertidumbre)
   - [2.3 Preguntas aclaratorias para resolver ambigüedad](02-mitigacion-de-alucinaciones.md#23-preguntas-aclaratorias-para-resolver-ambigüedad)
   - [2.4 Citas y trazabilidad: vincular afirmación con evidencia](02-mitigacion-de-alucinaciones.md#24-citas-y-trazabilidad-vincular-afirmación-con-evidencia)
   - [2.5 Contraste de fuentes: corroborar información](02-mitigacion-de-alucinaciones.md#25-contraste-de-fuentes-corroborar-información)
   - [2.6 Recuperación documental (RAG): apoyo de fuentes externas](02-mitigacion-de-alucinaciones.md#26-recuperación-documental-rag-apoyo-de-fuentes-externas)
   - [2.7 Límites de las instrucciones anti-alucinación](02-mitigacion-de-alucinaciones.md#27-límites-de-las-instrucciones-anti-alucinación)
- 3 · **[Sesgos](03-sesgos.md)**
   - [3.1 Sesgos: definición y origen](03-sesgos.md#31-sesgos-definición-y-origen)
   - [3.2 Tipos de sesgo: manifestaciones más frecuentes](03-sesgos.md#32-tipos-de-sesgo-manifestaciones-más-frecuentes)
   - [3.3 Detectar sesgos: pruebas contrafactuales](03-sesgos.md#33-detectar-sesgos-pruebas-contrafactuales)
   - [3.4 Mitigar sesgos con un diseño cuidadoso del prompt](03-sesgos.md#34-mitigar-sesgos-con-un-diseño-cuidadoso-del-prompt)
   - [3.5 Decisiones de alto impacto](03-sesgos.md#35-decisiones-de-alto-impacto)
- 4 · **[Aplicación, evaluación y supervisión](04-aplicacion-evaluacion-y-supervision.md)**
   - [4.1 Calibración de confianza: interpretar expresiones de certeza](04-aplicacion-evaluacion-y-supervision.md#41-calibración-de-confianza-interpretar-expresiones-de-certeza)
   - [4.2 Alucinaciones en tareas de extracción](04-aplicacion-evaluacion-y-supervision.md#42-alucinaciones-en-tareas-de-extracción)
   - [4.3 Alucinaciones en tareas de análisis](04-aplicacion-evaluacion-y-supervision.md#43-alucinaciones-en-tareas-de-análisis)
   - [4.4 Evaluación de respuestas fundamentadas: rúbrica de criterios](04-aplicacion-evaluacion-y-supervision.md#44-evaluación-de-respuestas-fundamentadas-rúbrica-de-criterios)
   - [4.5 Human-in-the-loop: supervisión humana estructurada](04-aplicacion-evaluacion-y-supervision.md#45-human-in-the-loop-supervisión-humana-estructurada)
   - [4.6 Políticas y gobernanza: integrar fiabilidad en la organización](04-aplicacion-evaluacion-y-supervision.md#46-políticas-y-gobernanza-integrar-fiabilidad-en-la-organización)
   - [4.7 Caso: construcción de una respuesta fundamentada](04-aplicacion-evaluacion-y-supervision.md#47-caso-construcción-de-una-respuesta-fundamentada)
   - [4.8 Resumen: la fiabilidad como proceso continuo](04-aplicacion-evaluacion-y-supervision.md#48-resumen-la-fiabilidad-como-proceso-continuo)
   - [4.9 Comprobación de comprensión](04-aplicacion-evaluacion-y-supervision.md#49-comprobación-de-comprensión)
   - [4.10 Comprobación de comprensión: respuestas](04-aplicacion-evaluacion-y-supervision.md#410-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Alucinación**: Una afirmación que suena plausible pero no tiene respaldo en la realidad ni en la fuente que se aportó. ([ficha](../glosario.md#alucinación))
- **Fundamentación (respuesta basada en fuentes)**: Hacer que la respuesta se apoye solo en los documentos aportados y diga cuándo algo no consta en ellos. ([ficha](../glosario.md#fundamentación-respuesta-basada-en-fuentes))
- **Abstención**: Responder «no consta» o pedir una aclaración cuando no hay información suficiente, en lugar de inventar. ([ficha](../glosario.md#abstención))
- **Cita y trazabilidad**: Vincular cada afirmación con la parte de la fuente que la respalda, para poder comprobarla. ([ficha](../glosario.md#cita-y-trazabilidad))
- **RAG (recuperación documental)**: Buscar los fragmentos de documentos más relevantes y dárselos al modelo para que responda apoyándose en ellos. ([ficha](../glosario.md#rag-recuperación-documental))
- **Sesgo**: Una tendencia sistemática del modelo a favorecer o perjudicar a ciertos grupos o puntos de vista, heredada de los datos o del diseño del prompt. ([ficha](../glosario.md#sesgo))
- **Prueba contrafactual**: Comparar la respuesta a dos casos idénticos salvo un atributo personal, para ver si ese atributo cambia el resultado. ([ficha](../glosario.md#prueba-contrafactual))
- **Calibración de confianza**: Interpretar con cuidado lo seguro que suena el modelo: la seguridad del tono no indica que acierte. ([ficha](../glosario.md#calibración-de-confianza))
- **Human-in-the-loop (supervisión humana)**: Que una persona revise o apruebe antes de que algo se envíe o se ejecute, según el riesgo. ([ficha](../glosario.md#human-in-the-loop-supervisión-humana))

## Vigencia

Revisión del contenido: noviembre de 2026. Las referencias al RGPD y al AI Act son orientativas. Los plazos de aplicación del AI Act se han modificado y pueden volver a cambiar; el módulo 09 recoge el calendario vigente en la fecha de revisión.

Fuentes oficiales para contrastar:

- [RGPD, Reglamento (UE) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj) y [Agencia Española de Protección de Datos](https://www.aepd.es/)
- [AI Act, Reglamento (UE) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) y su modificación, [Reglamento (UE) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj)

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 08A · Cazar alucinaciones](../../laboratorios/08A/README.md) · 65 minutos · forma parte de las 30 horas del curso
- [Laboratorio 08B · Responder solo con fuentes, admitir lo que no consta y medir el sesgo](../../laboratorios/08B/README.md) · 75 minutos · opcional
