# Laboratorios

Los laboratorios no se evalúan y no hay nada que entregar: sirven para practicar con casos realistas lo que cada módulo explica. **El laboratorio guiado (A) de cada módulo y el proyecto final forman parte de las 30 horas del curso; el abierto (B) y los laboratorios opcionales adicionales (C) no cuentan para ese total**. Cada uno es un único documento con siete apartados: título, ficha «De un vistazo», justificación del laboratorio, objetivos, recursos necesarios, pasos de ejecución y conclusiones. Los pasos están explicados al detalle para perfiles no técnicos y, cuando el laboratorio usa scripts, cada paso incluye la alternativa con código. Las conclusiones traen las preguntas de reflexión con su respuesta y la solución de referencia, que se consulta solo después de haberlo intentado.

Todos comparten un mismo caso: Altanoria Software S.L., una empresa ficticia que desarrolla soluciones de software con IA generativa. Los documentos de la empresa (planes, SLA, condiciones, privacidad) están en [`comun/empresa`](comun/empresa/altanoria.md). Todos los datos son sintéticos.

## Antes de empezar

- [Primer laboratorio: Antes de empezar](comun/antes-de-empezar.md): 30 minutos de lectura y un calentamiento con una hoja de cálculo, sin programar; cómo trabajar con un chat y cómo se lee un laboratorio.
- [Guía de los laboratorios](comun/README.md): cómo trabajar, cómo configurar un modelo y cómo usar los scripts. Antes de empezar un laboratorio con scripts conviene ejecutar `python comun/comprobar_entorno.py`.
- [Guía para trabajar sin API](comun/sin-api.md): cuatro caminos si no se dispone de acceso a un modelo por API.
- [Guía para trabajar sin Python](comun/sin-python.md): cómo hacer todos los laboratorios con un chat y una hoja de cálculo.
- [Si algo falla](comun/si-algo-falla.md): qué hacer ante los errores más frecuentes al ejecutar los scripts (respuestas vacías, tiempos de espera, prompts truncados).
- [Perfil de Altanoria](comun/empresa/altanoria.md) y sus [documentos](comun/empresa/).

## Mapa de laboratorios

Los módulos se numeran del 01 al 13 y se agrupan en cinco partes. Cada módulo tiene dos laboratorios: la letra A indica el guiado (consolida los conceptos con una tarea paso a paso) y la B el abierto (aplica los conceptos a un caso con más margen). Algunos módulos tienen además un laboratorio C, opcional, que practica una parte del módulo que A y B no cubren. El laboratorio 14 es el proyecto integrador.

### Parte I · Fundamentos

| Módulo | Laboratorio | Duración | Sin API | Sin Python |
|---|---|---|---|---|
| Módulo 01 | [01A · Tokens, ventana de contexto y coste](01A/README.md) | 65 min | Sí (los scripts son opcionales) | Sí: pasos en el enunciado |
| Módulo 01 | [01B · Mapa de capacidades y límites de un LLM](01B/README.md) | 55 min | Sí: basta un chat | Sí: chat |
| Módulo 02 | [02A · Del prompt vago al contrato de tarea](02A/README.md) | 80 min | Sí: basta un chat | Sí: chat |
| Módulo 02 | [02B · Anatomía de un prompt: ablación de componentes](02B/README.md) | 45 min | Sí: basta un chat | Sí: chat |
| Módulo 03 | [03A · Catálogo de prompts por tipo funcional](03A/README.md) | 50 min | Sí: basta un chat | Sí: chat |
| Módulo 03 | [03B · Una misma tarea, tres tipos de prompt](03B/README.md) | 55 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |

### Parte II · Técnicas y control de la salida

| Módulo | Laboratorio | Duración | Sin API | Sin Python |
|---|---|---|---|---|
| Módulo 04 | [04A · Zero-shot, one-shot y few-shot: cuántos ejemplos hacen falta](04A/README.md) | 55 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 04 | [04B · Razonamiento paso a paso y autoconsistencia](04B/README.md) | 55 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 05 | [05A · Un mismo contenido, tres audiencias](05A/README.md) | 50 min | Sí: basta un chat | Sí: chat |
| Módulo 05 | [05B · Un asistente con rol, límites y voz consistente](05B/README.md) | 55 min | Sí: basta un chat, turno a turno | Sí: pasos en el enunciado |
| Módulo 06 | [06A · Salida consumible: Markdown, tabla y JSON validado](06A/README.md) | 80 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 06 | [06B · Temperatura y top-p: un experimento controlado](06B/README.md) | 50 min | Parcial: mejor con modelo local (temperatura y top-p) | Sí: pasos en el enunciado |

### Parte III · Evaluación, fiabilidad y seguridad

| Módulo | Laboratorio | Duración | Sin API | Sin Python |
|---|---|---|---|---|
| Módulo 07 | [07A · Contrato, suite de pruebas y línea base](07A/README.md) | 70 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 07 | [07B · Iterar con hipótesis, regresiones y evaluación final](07B/README.md) | 70 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 08 | [08A · Cazar alucinaciones](08A/README.md) | 65 min | Sí: basta un chat | Sí: chat |
| Módulo 08 | [08B · Responder solo con fuentes, admitir lo que no consta y medir el sesgo](08B/README.md) | 75 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 09 | [09A · Minimizar y anonimizar antes de enviar datos a un modelo](09A/README.md) | 50 min | Sí: basta un chat | Sí: muestra para chat |
| Módulo 09 | [09B · Red team de un asistente de buzón](09B/README.md) | 50 min | Chat por lotes, modo manual o modelo local | Sí: pasos en el enunciado |

### Parte IV · Aplicaciones

| Módulo | Laboratorio | Duración | Sin API | Sin Python |
|---|---|---|---|---|
| Módulo 10 | [10A · Briefing, ideación y selección](10A/README.md) | 50 min | Sí: basta un chat | Sí: chat |
| Módulo 10 | [10B · Campaña multicanal con voz de marca](10B/README.md) | 55 min | Sí: basta un chat | Sí: chat |
| Módulo 10 | [10C · Prompts visuales: de la descripción al guion gráfico](10C/README.md) | 65 min | Sí: basta un chat | Sí: chat |
| Módulo 11 | [11A · Especificar y generar una función con pruebas](11A/README.md) | 65 min | Sí: chat; las pruebas se ejecutan en local | Sí: muestra para chat |
| Módulo 11 | [11B · Depurar con evidencia y revisar código sin delegar el criterio](11B/README.md) | 60 min | Sí: chat; las pruebas se ejecutan en local | Sí: muestra para chat |
| Módulo 11 | [11C · Traducir y documentar código sin perder el comportamiento](11C/README.md) | 70 min | Sí: chat; la comprobación se hace en el navegador | Sí: chat |
| Módulo 12 | [12A · Extracción estructurada de correos de clientes](12A/README.md) | 55 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 12 | [12B · Síntesis multidocumento para un decisor](12B/README.md) | 50 min | Sí: basta un chat | Sí: chat |
| Módulo 12 | [12C · Análisis de datos con Python asistido por un modelo](12C/README.md) | 60 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |

### Parte V · Sistemas de prompts y proyecto final

| Módulo | Laboratorio | Duración | Sin API | Sin Python |
|---|---|---|---|---|
| Módulo 13 | [13A · Cadena de tres etapas con contratos y puertas de validación](13A/README.md) | 60 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Módulo 13 | [13B · Sistema ramificado con recuperación de documentos y evaluación extremo a extremo](13B/README.md) | 50 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |
| Proyecto final | [14 · Proyecto integrador: asistente de gestión de reclamaciones de Altanoria](14/README.md) | 100 min | Chat por lotes, modo manual o modelo local | Sí: muestra para chat |

Los 30 laboratorios, contando los opcionales (B y C), suman 30 h 15 min; las 30 horas del curso solo incluyen los laboratorios A y el proyecto final. Cada laboratorio indica su duración (suma de sus pasos, en múltiplos de 5 minutos) para una persona sin perfil técnico que trabaja con un chat; con código o con un modelo lento puede variar.

## Orden y dependencias

Los laboratorios pueden hacerse en el orden de los módulos. Casi todos son independientes entre sí; estas son las excepciones:

| Laboratorio | Qué conviene haber hecho antes | Por qué |
|---|---|---|
| [07B](07B/README.md) | [07A](07A/README.md) (necesario, o usar los datos y el prompt v0 de su solución) | Continúa el clasificador, su baseline y su registro de versiones. |
| [12A](12A/README.md) | [06A](06A/README.md) (recomendado) | Reutiliza la idea de salida JSON validada con un esquema. |
| [10C](10C/README.md) | [10A](10A/README.md) y [10B](10B/README.md) (recomendados) | Usa la misma hoja de hechos del producto y la idea de evaluar con criterios explícitos. |
| [11C](11C/README.md) | [11A](11A/README.md) (recomendado) | Traduce la función de facturación y reutiliza sus casos de aceptación. |
| [12C](12C/README.md) | [12A](12A/README.md) (recomendado) | Reutiliza la idea de validar el resultado del modelo contra una referencia. |
| [13A](13A/README.md) | [06A](06A/README.md) y [07A](07A/README.md) (recomendados) | Contratos de salida y medición con casos límite. |
| [13B](13B/README.md) | [08B](08B/README.md) (recomendado) | Respuestas fundamentadas con citas y abstención. |
| [14](14/README.md) | Ninguno: es autónomo. Reúne todo el curso, pero no hace falta haber hecho los laboratorios anteriores | Reúne clasificación, privacidad, recuperación y puertas de calidad. |

[← Inicio del curso](../README.md)
