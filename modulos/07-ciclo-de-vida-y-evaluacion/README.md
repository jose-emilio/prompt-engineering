[← Módulo 06](../06-formato-de-salida-y-parametros/README.md) · [Inicio del curso](../../README.md) · [Módulo 08 →](../08-fiabilidad-alucinaciones-y-sesgos/README.md)

# Módulo 07 · Ciclo de vida, evaluación y optimización de prompts

*Parte III · Evaluación, fiabilidad y seguridad*

Duración estimada: 145 minutos (75 de presentación y 70 del laboratorio 07A). El laboratorio 07B es opcional.

> Diseñar, probar, evaluar, refinar y versionar. Este módulo introduce un proceso sistemático para tratar los prompts como artefactos de ingeniería: la calidad no se asume, se demuestra con pruebas.

## Contenido del módulo

- **[Objetivos del módulo](00-objetivos-del-modulo.md)**
   - [Objetivos y mapa del módulo](00-objetivos-del-modulo.md#objetivos-y-mapa-del-módulo)
- 1 · **[Diseño y pruebas](01-diseno-y-pruebas.md)**
   - [1.1 El prompt como artefacto de ingeniería](01-diseno-y-pruebas.md#11-el-prompt-como-artefacto-de-ingeniería)
   - [1.2 Identificar el problema antes de redactar](01-diseno-y-pruebas.md#12-identificar-el-problema-antes-de-redactar)
   - [1.3 Definir entradas y salidas: el contrato de tarea](01-diseno-y-pruebas.md#13-definir-entradas-y-salidas-el-contrato-de-tarea)
   - [1.4 Criterios de aceptación: de expectativas a condiciones verificables](01-diseno-y-pruebas.md#14-criterios-de-aceptación-de-expectativas-a-condiciones-verificables)
   - [1.5 Diseñar la primera versión: el baseline medible](01-diseno-y-pruebas.md#15-diseñar-la-primera-versión-el-baseline-medible)
   - [1.6 Hipótesis de mejora: cambios comprobables](01-diseno-y-pruebas.md#16-hipótesis-de-mejora-cambios-comprobables)
   - [1.7 Diseñar el conjunto de pruebas](01-diseno-y-pruebas.md#17-diseñar-el-conjunto-de-pruebas)
   - [1.8 Cobertura y representatividad: evitar conjuntos sesgados](01-diseno-y-pruebas.md#18-cobertura-y-representatividad-evitar-conjuntos-sesgados)
   - [1.9 Pruebas normales y casos límite: evaluar las fronteras](01-diseno-y-pruebas.md#19-pruebas-normales-y-casos-límite-evaluar-las-fronteras)
   - [1.10 Pruebas negativas y robustez](01-diseno-y-pruebas.md#110-pruebas-negativas-y-robustez)
- 2 · **[Evaluación](02-evaluacion.md)**
   - [2.1 Evaluación cualitativa: analizar calidad con rúbricas](02-evaluacion.md#21-evaluación-cualitativa-analizar-calidad-con-rúbricas)
   - [2.2 Evaluación cuantitativa: métricas cuando existe referencia](02-evaluacion.md#22-evaluación-cuantitativa-métricas-cuando-existe-referencia)
   - [2.3 Una métrica no representa toda la calidad](02-evaluacion.md#23-una-métrica-no-representa-toda-la-calidad)
   - [2.4 Evaluación humana y automática: combinar métodos](02-evaluacion.md#24-evaluación-humana-y-automática-combinar-métodos)
   - [2.5 LLM como evaluador: un prompt con rúbrica](02-evaluacion.md#25-llm-como-evaluador-un-prompt-con-rúbrica)
   - [2.6 Comparación A/B de prompts: control riguroso](02-evaluacion.md#26-comparación-ab-de-prompts-control-riguroso)
   - [2.7 Análisis de errores: convertir fallos en mejoras](02-evaluacion.md#27-análisis-de-errores-convertir-fallos-en-mejoras)
- 3 · **[Optimización y mantenimiento](03-optimizacion-y-mantenimiento.md)**
   - [3.1 Refinamiento de instrucciones: cambios concretos y verificables](03-optimizacion-y-mantenimiento.md#31-refinamiento-de-instrucciones-cambios-concretos-y-verificables)
   - [3.2 Control de regresiones: proteger lo que ya funciona](03-optimizacion-y-mantenimiento.md#32-control-de-regresiones-proteger-lo-que-ya-funciona)
   - [3.3 Versionado de prompts: gestionar cambios con trazabilidad](03-optimizacion-y-mantenimiento.md#33-versionado-de-prompts-gestionar-cambios-con-trazabilidad)
   - [3.4 Documentación mínima útil](03-optimizacion-y-mantenimiento.md#34-documentación-mínima-útil)
   - [3.5 Variables y plantillas: separar contenido fijo y dinámico](03-optimizacion-y-mantenimiento.md#35-variables-y-plantillas-separar-contenido-fijo-y-dinámico)
   - [3.6 Pruebas entre modelos y versiones: evaluar portabilidad](03-optimizacion-y-mantenimiento.md#36-pruebas-entre-modelos-y-versiones-evaluar-portabilidad)
   - [3.7 Coste, latencia y eficiencia: criterios operativos](03-optimizacion-y-mantenimiento.md#37-coste-latencia-y-eficiencia-criterios-operativos)
   - [3.8 Reducir coste y latencia sin perder calidad](03-optimizacion-y-mantenimiento.md#38-reducir-coste-y-latencia-sin-perder-calidad)
- 4 · **[Despliegue, gobernanza y cierre](04-despliegue-gobernanza-y-cierre.md)**
   - [4.1 Despliegue y mantenimiento: del laboratorio a producción](04-despliegue-gobernanza-y-cierre.md#41-despliegue-y-mantenimiento-del-laboratorio-a-producción)
   - [4.2 Gobernanza y responsabilidades](04-despliegue-gobernanza-y-cierre.md#42-gobernanza-y-responsabilidades)
   - [4.3 Caso integrado de optimización: clasificación de tickets](04-despliegue-gobernanza-y-cierre.md#43-caso-integrado-de-optimización-clasificación-de-tickets)
   - [4.4 Resumen del proceso: ciclo de vida completo](04-despliegue-gobernanza-y-cierre.md#44-resumen-del-proceso-ciclo-de-vida-completo)
   - [4.5 Comprobación de comprensión](04-despliegue-gobernanza-y-cierre.md#45-comprobación-de-comprensión)
   - [4.6 Comprobación de comprensión: respuestas](04-despliegue-gobernanza-y-cierre.md#46-comprobación-de-comprensión-respuestas)

## Términos nuevos de este módulo

Definiciones cortas de los términos que más hacen falta en este módulo; alguno puede haberse nombrado antes, pero aquí se trabaja a fondo. Cada uno enlaza con su ficha del [glosario completo](../glosario.md), con un ejemplo y con qué no confundirlo.

- **Baseline (línea base)**: La primera versión del prompt, ya medida: el punto de partida con el que se comparan todas las mejoras. ([ficha](../glosario.md#baseline-línea-base))
- **Criterio de aceptación**: Una condición medible, con un número, que el prompt debe cumplir para darlo por bueno. ([ficha](../glosario.md#criterio-de-aceptación))
- **Suite de pruebas (conjunto de pruebas)**: Una colección de casos con la respuesta correcta ya conocida, que se ejecuta cada vez que cambia el prompt. ([ficha](../glosario.md#suite-de-pruebas-conjunto-de-pruebas))
- **Conjunto de desarrollo y conjunto de prueba**: El conjunto de desarrollo se usa para ir mejorando el prompt; el de prueba se guarda aparte y se usa una sola vez, al final, para comprobar que la mejora no es casualidad. ([ficha](../glosario.md#conjunto-de-desarrollo-y-conjunto-de-prueba))
- **Caso límite**: Una entrada situada en los extremos de lo que el prompt debe manejar: muy corta, muy larga, vacía o en otro idioma. ([ficha](../glosario.md#caso-límite))
- **Prueba negativa**: Un caso que el prompt no debe atender o debe rechazar: fuera de su ámbito, mal formado o con una orden escondida. ([ficha](../glosario.md#prueba-negativa))
- **Regresión**: Un caso que antes salía bien y deja de salir bien después de un cambio en el prompt. ([ficha](../glosario.md#regresión))
- **Exactitud (accuracy)**: El porcentaje de casos que el sistema resuelve bien sobre el total. ([ficha](../glosario.md#exactitud-accuracy))
- **Precisión (precision)**: De los casos que el sistema marcó como positivos, cuántos lo eran de verdad. ([ficha](../glosario.md#precisión-precision))
- **Recall (exhaustividad)**: De los casos que de verdad eran positivos, cuántos detectó el sistema. ([ficha](../glosario.md#recall-exhaustividad))
- **F1**: Un único número que resume la precisión y el recall a la vez; si uno de los dos es muy bajo, el F1 también lo es. ([ficha](../glosario.md#f1))
- **Falso positivo y falso negativo**: Un falso positivo es marcar como positivo algo que no lo era; un falso negativo es no marcar algo que sí lo era. ([ficha](../glosario.md#falso-positivo-y-falso-negativo))
- **Rúbrica**: Una lista de criterios con una escala (por ejemplo, 0, 1 o 2) que dice qué significa cada puntuación, para evaluar sin depender de la impresión. ([ficha](../glosario.md#rúbrica))
- **Comparación A/B**: Comparar dos versiones de un prompt con exactamente las mismas entradas y cambiando una sola cosa entre ellas. ([ficha](../glosario.md#comparación-ab))
- **LLM como evaluador**: Usar un modelo para puntuar las respuestas de otro, dándole una rúbrica, pidiéndole que cite la evidencia y comprobándolo después con revisión humana. ([ficha](../glosario.md#llm-como-evaluador))

## Laboratorios

Práctica de este módulo (sin evaluación):

- [Laboratorio 07A · Contrato, suite de pruebas y línea base](../../laboratorios/07A/README.md) · 70 minutos · forma parte de las 30 horas del curso
- [Laboratorio 07B · Iterar con hipótesis, regresiones y evaluación final](../../laboratorios/07B/README.md) · 70 minutos · opcional
