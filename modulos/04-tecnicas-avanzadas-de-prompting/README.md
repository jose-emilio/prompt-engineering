[← Módulo 03](../03-tipos-funcionales-de-prompts/README.md) · [Inicio del curso](../../README.md) · [Módulo 05 →](../05-roles-personas-y-comportamiento/README.md)

# Módulo 04 · Técnicas avanzadas de prompting

*Parte II · Técnicas y control de la salida*

Duración estimada: 125 minutos (70 de presentación y 55 del laboratorio 04A). El laboratorio 04B es opcional.

> Domina las estrategias esenciales para diseñar prompts de alta precisión: desde instrucciones directas hasta razonamiento estructurado, descomposición de problemas e interacción con herramientas.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos del módulo y mapa de técnicas](00-objetivos-del-modulo.md#objetivos-del-módulo-y-mapa-de-técnicas)
- 1 · **[Técnicas basadas en ejemplos](01-tecnicas-basadas-en-ejemplos.md)**
   - [1.1 ¿Por qué usar técnicas avanzadas?](01-tecnicas-basadas-en-ejemplos.md#11-por-qué-usar-técnicas-avanzadas)
   - [1.2 Zero-shot: definición y funcionamiento](01-tecnicas-basadas-en-ejemplos.md#12-zero-shot-definición-y-funcionamiento)
   - [1.3 Diseño de un prompt Zero-shot completo](01-tecnicas-basadas-en-ejemplos.md#13-diseño-de-un-prompt-zero-shot-completo)
   - [1.4 Ventajas y límites del prompting Zero-shot](01-tecnicas-basadas-en-ejemplos.md#14-ventajas-y-límites-del-prompting-zero-shot)
   - [1.5 One-shot: un ejemplo que transforma la instrucción](01-tecnicas-basadas-en-ejemplos.md#15-one-shot-un-ejemplo-que-transforma-la-instrucción)
   - [1.6 Cómo diseñar una demostración One-shot eficaz](01-tecnicas-basadas-en-ejemplos.md#16-cómo-diseñar-una-demostración-one-shot-eficaz)
   - [1.7 Few-shot: aprendizaje en contexto con varios ejemplos](01-tecnicas-basadas-en-ejemplos.md#17-few-shot-aprendizaje-en-contexto-con-varios-ejemplos)
   - [1.8 In-Context Learning: adaptación sin reentrenamiento](01-tecnicas-basadas-en-ejemplos.md#18-in-context-learning-adaptación-sin-reentrenamiento)
   - [1.9 Selección de buenos ejemplos para Few-shot](01-tecnicas-basadas-en-ejemplos.md#19-selección-de-buenos-ejemplos-para-few-shot)
   - [1.10 Cantidad y orden de ejemplos: optimizar el contexto](01-tecnicas-basadas-en-ejemplos.md#110-cantidad-y-orden-de-ejemplos-optimizar-el-contexto)
   - [1.11 Zero-shot, One-shot y Few-shot: comparativa](01-tecnicas-basadas-en-ejemplos.md#111-zero-shot-one-shot-y-few-shot-comparativa)
   - [1.12 Diseñar una evaluación comparativa justa](01-tecnicas-basadas-en-ejemplos.md#112-diseñar-una-evaluación-comparativa-justa)
- 2 · **[Razonamiento y descomposición](02-razonamiento-y-descomposicion.md)**
   - [2.1 Chain-of-Thought: razonamiento paso a paso](02-razonamiento-y-descomposicion.md#21-chain-of-thought-razonamiento-paso-a-paso)
   - [2.2 Solicitar pasos verificables: diseño práctico](02-razonamiento-y-descomposicion.md#22-solicitar-pasos-verificables-diseño-práctico)
   - [2.3 Zero-shot CoT y Few-shot CoT: variantes comparadas](02-razonamiento-y-descomposicion.md#23-zero-shot-cot-y-few-shot-cot-variantes-comparadas)
   - [2.4 CoT en modelos de razonamiento](02-razonamiento-y-descomposicion.md#24-cot-en-modelos-de-razonamiento)
   - [2.5 Descomposición de problemas complejos](02-razonamiento-y-descomposicion.md#25-descomposición-de-problemas-complejos)
   - [2.6 Least-to-Most Prompting: de lo simple a lo complejo](02-razonamiento-y-descomposicion.md#26-least-to-most-prompting-de-lo-simple-a-lo-complejo)
   - [2.7 Plan-and-Solve: separar planificación y ejecución](02-razonamiento-y-descomposicion.md#27-plan-and-solve-separar-planificación-y-ejecución)
   - [2.8 Self-Consistency: comparar múltiples soluciones candidatas](02-razonamiento-y-descomposicion.md#28-self-consistency-comparar-múltiples-soluciones-candidatas)
   - [2.9 Aplicaciones y límites de Self-Consistency](02-razonamiento-y-descomposicion.md#29-aplicaciones-y-límites-de-self-consistency)
   - [2.10 Decomposed Prompting: prompts especializados por subtarea](02-razonamiento-y-descomposicion.md#210-decomposed-prompting-prompts-especializados-por-subtarea)
- 3 · **[Herramientas, revisión y selección de técnica](03-herramientas-revision-y-seleccion-de-tecnica.md)**
   - [3.1 ReAct: razonamiento y acción combinados](03-herramientas-revision-y-seleccion-de-tecnica.md#31-react-razonamiento-y-acción-combinados)
   - [3.2 Uso de herramientas: controles operativos imprescindibles](03-herramientas-revision-y-seleccion-de-tecnica.md#32-uso-de-herramientas-controles-operativos-imprescindibles)
   - [3.3 Reflexion: revisión iterativa con rúbrica](03-herramientas-revision-y-seleccion-de-tecnica.md#33-reflexion-revisión-iterativa-con-rúbrica)
   - [3.4 Elegir la técnica según el problema](03-herramientas-revision-y-seleccion-de-tecnica.md#34-elegir-la-técnica-según-el-problema)
   - [3.5 Errores frecuentes al aplicar técnicas avanzadas](03-herramientas-revision-y-seleccion-de-tecnica.md#35-errores-frecuentes-al-aplicar-técnicas-avanzadas)
   - [3.6 Caso comparativo integrado: clasificación con casos ambiguos](03-herramientas-revision-y-seleccion-de-tecnica.md#36-caso-comparativo-integrado-clasificación-con-casos-ambiguos)
   - [3.7 Mapa resumen: técnicas avanzadas de prompting](03-herramientas-revision-y-seleccion-de-tecnica.md#37-mapa-resumen-técnicas-avanzadas-de-prompting)
   - [3.8 Comprobación de comprensión](03-herramientas-revision-y-seleccion-de-tecnica.md#38-comprobación-de-comprensión)
   - [3.9 Comprobación de comprensión: respuestas](03-herramientas-revision-y-seleccion-de-tecnica.md#39-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Zero-shot**: Pedir la tarea con una instrucción, sin dar ningún ejemplo. ([ficha](../glosario.md#zero-shot))
- **One-shot**: Pedir la tarea mostrando un único ejemplo de entrada y salida. ([ficha](../glosario.md#one-shot))
- **Few-shot**: Pedir la tarea mostrando varios ejemplos de entrada y salida. ([ficha](../glosario.md#few-shot))
- **Aprendizaje en contexto (in-context learning)**: La capacidad del modelo de adaptarse a una tarea a partir de los ejemplos y las instrucciones del propio prompt, sin reentrenarse. ([ficha](../glosario.md#aprendizaje-en-contexto-in-context-learning))
- **Chain-of-Thought (razonamiento paso a paso)**: Pedir al modelo que escriba los pasos intermedios antes de dar la respuesta. ([ficha](../glosario.md#chain-of-thought-razonamiento-paso-a-paso))
- **Autoconsistencia (self-consistency)**: Generar varias soluciones independientes al mismo problema y quedarse con la respuesta que más se repite. ([ficha](../glosario.md#autoconsistencia-self-consistency))
- **ReAct**: Un patrón en el que el modelo alterna razonar y actuar, por ejemplo consultando una herramienta antes de seguir. ([ficha](../glosario.md#react))

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 04A · Zero-shot, one-shot y few-shot: cuántos ejemplos hacen falta](../../laboratorios/04A/README.md) · 55 minutos · forma parte de las 30 horas del curso
- [Laboratorio 04B · Razonamiento paso a paso y autoconsistencia](../../laboratorios/04B/README.md) · 55 minutos · opcional

No se practican en los laboratorios: ReAct, el uso de herramientas y Reflexion (§3.1 a 3.3) y la descomposición con Least-to-Most y Decomposed Prompting (§2.6 y 2.10). Se estudian en el módulo y se practican con casos propios.
