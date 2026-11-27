[← Anterior](01-diseno-y-pruebas.md) · [Índice del módulo](README.md) · [Siguiente →](03-optimizacion-y-mantenimiento.md)

# 2 · Evaluación

*Módulo 07: Ciclo de vida, evaluación y optimización de prompts*

## 2.1 Evaluación cualitativa: analizar calidad con rúbricas

La evaluación cualitativa permite capturar dimensiones de calidad que las métricas automáticas no pueden medir: si la respuesta es realmente útil, si el tono es apropiado, si la información es fiel a la fuente. Las rúbricas con descriptores por nivel hacen este juicio reproducible.

| Dimensión | Nivel 1 — Insuficiente | Nivel 3 — Aceptable | Nivel 5 — Excelente |
|---|---|---|---|
| Relevancia | No responde a la consulta | Responde parcialmente | Responde con precisión y foco |
| Claridad | Confusa o contradictoria | Comprensible con esfuerzo | Clara y bien estructurada |
| Completitud | Omite información crítica | Cubre los puntos principales | Completa y sin omisiones |
| Fidelidad a fuente | Contradice la fuente | Mayormente fiel | Totalmente fiel, sin alucinaciones |
| Cumplimiento de formato | Formato incorrecto | Formato parcialmente correcto | Esquema de salida cumplido |

**Explicación**

La **evaluación cualitativa** captura dimensiones que las métricas automáticas no miden: utilidad real, tono apropiado, fidelidad a la fuente. Las rúbricas con descriptores por nivel hacen reproducible el juicio. La tabla evalúa cinco dimensiones en tres niveles: relevancia, claridad, completitud, fidelidad a la fuente (desde contradecirla hasta ser totalmente fiel y sin alucinaciones) y cumplimiento de formato.

La clave son los descriptores: «puntúa la claridad de 1 a 5» deja el criterio a cada evaluador, mientras que describir qué significa cada nivel hace comprobable la puntuación. Para verificar que la **rúbrica** funciona, dos personas pueden evaluar de forma independiente una muestra y comparar; si discrepan sistemáticamente, los descriptores son ambiguos. Es más lenta y costosa que la automática, pero indispensable.

---

## 2.2 Evaluación cuantitativa: métricas cuando existe referencia

Las métricas cuantitativas permiten comparar versiones de forma objetiva y detectar regresiones automáticamente. Solo son válidas cuando existe una referencia (ground truth) con la que comparar las salidas del modelo.

**Métricas principales**

- Exactitud: porcentaje de casos correctos sobre el total
- Precisión: de los casos predichos positivos, cuántos son correctos
- Recall: de los casos positivos reales, cuántos se detectaron
- F1: media armónica de precisión y recall
- Tasa de extracción correcta: campos extraídos correctamente sobre total
- Cumplimiento de esquema: salidas válidas según el formato definido

**Interpretación de negocio**

Una exactitud del 95% puede parecer excelente, pero si el 5% de errores corresponde a los casos de mayor impacto, el sistema no es apto para producción.

Siempre relacionar las métricas con el impacto real del error en el caso de uso concreto.

**Explicación**

Las métricas cuantitativas permiten comparar versiones de forma objetiva y detectar **regresiones** automáticamente, pero solo son válidas cuando existe una referencia (ground truth). Las principales son la exactitud (porcentaje de casos correctos), la precisión (de los predichos positivos, cuántos lo son), el recall o exhaustividad (de los positivos reales, cuántos se detectaron), la puntuación F1 (media armónica de ambos), la tasa de extracción correcta y el cumplimiento de esquema.

Un clasificador de tickets urgentes puede tener una precisión altísima y un recall bajo si es muy cauteloso y solo marca los casos evidentes; F1 resume ambos en un número. Una exactitud del 95 % puede ser excelente o inaceptable si el 5 % de errores corresponde a los casos de mayor impacto, de modo que las métricas se relacionan siempre con el impacto real del error y se calculan también por categoría.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 07A · Contrato, suite de pruebas y línea base](../../laboratorios/07A/README.md)
<!-- /labs-seccion -->

---

## 2.3 Una métrica no representa toda la calidad

Optimizar un único indicador puede mejorar el número sin mejorar el sistema. Este fenómeno, conocido como la ley de Goodhart, es especialmente relevante en la evaluación de LLMs, donde la fluidez del texto puede enmascarar errores de contenido.

- **Los promedios ocultan fallos críticos**: Un promedio del 94% puede coexistir con un fallo sistemático en un subconjunto de casos de alto riesgo que nunca aparece en el agregado.
- **Los casos raros pueden ser los más importantes**: En sistemas de soporte médico, legal o financiero, los casos poco frecuentes suelen ser los de mayor impacto. No pueden ignorarse por su baja frecuencia.
- **Las métricas automáticas no capturan toda la utilidad**: Un texto puede ser gramaticalmente impecable y semánticamente incorrecto. La fluidez no implica veracidad ni utilidad.
- **Combinar indicadores y definir umbrales según riesgo**: Usar conjuntos de métricas y establecer umbrales diferenciados según el impacto potencial del fallo en cada tipo de caso.

**Explicación**

Optimizar un único indicador puede mejorar el número sin mejorar el sistema, fenómeno conocido como ley de Goodhart: cuando una medida se convierte en objetivo, deja de ser una buena medida. Esto es especialmente relevante con LLM, donde la fluidez puede enmascarar errores de contenido.

Cuatro advertencias: los promedios ocultan fallos críticos (un 94 % puede coexistir con un fallo sistemático en casos de alto riesgo); los casos raros pueden ser los más importantes; las métricas automáticas no capturan toda la utilidad (un texto puede ser impecable y erróneo); y conviene combinar indicadores y definir umbrales según el riesgo. En la práctica, se desglosan los resultados por categoría, usuario y nivel de riesgo, y los umbrales pueden ser distintos: un 90 % puede bastar en un caso de bajo impacto y exigirse un 99 % o revisión humana en uno de alto.

---

## 2.4 Evaluación humana y automática: combinar métodos

Ningún método de evaluación es suficiente por sí solo. La evaluación humana aporta contexto y juicio, pero es lenta y costosa. La evaluación automática es rápida y escalable, pero no captura matices de utilidad real. Combinarlas produce resultados más fiables.

**1. Revisión humana**

**2. Reglas automáticas**

**3. LLM como evaluador**

• Comprensión del contexto

• Juicio subjetivo

• Lenta

• Costosa

• Validación de formato

• Expresiones regulares

• Rápidas

• Escalables

• Cobertura limitada

• Valoración matizada

• Criterios flexibles

• Requiere calibración

• No es verdad absoluta

**Resolución de discrepancias**

Priorizar la revisión humana, ajustar las reglas o calibrar el LLM según el contexto.

**Explicación**

Ningún método de evaluación basta por sí solo. La revisión humana aporta contexto y juicio, pero es lenta y costosa; las reglas automáticas (formato, expresiones regulares) son rápidas y escalables pero de cobertura limitada; y el **LLM como evaluador** ofrece valoraciones matizadas y criterios flexibles, pero requiere calibración y no es verdad absoluta. Combinarlos da resultados más fiables.

El evaluador con LLM tiene sus propios sesgos (prefiere respuestas largas, favorece su estilo, tiende a ser benévolo), por lo que debe calibrarse contra personas. Cuando los métodos discrepan, conviene priorizar la revisión humana y ajustar reglas o calibrar el evaluador: la discrepancia es información. Un esquema práctico usa las reglas como primer filtro, el LLM para dimensiones cualitativas y la revisión humana sobre muestras y casos de riesgo.

---

## 2.5 LLM como evaluador: un prompt con rúbrica

Un evaluador automático solo es fiable si recibe criterios explícitos, exige evidencia, devuelve un formato fijo y se calibra contra la revisión humana.

**Prompt de evaluador *(ilustrativo)***

```text
Evalúa la RESPUESTA con esta rúbrica.
Fuente única: el DOCUMENTO adjunto.
Criterios (0-2): fidelidad, cobertura, formato.
Cita el fragmento que justifica cada nota.
Devuelve solo JSON válido:
{"fidelidad":0,"cobertura":0,"formato":0,
 "evidencia":["…"],"defectos":["…"]}
Si falta evidencia, puntúa 0.
```

**Buenas prácticas**

- Rúbrica con descriptores: criterios observables y escala por nivel
- Evidencia por nota: fragmento que justifica cada puntuación
- Salida validable: JSON con campos fijos para procesarlo
- Calibración: comparar con una muestra revisada por personas
- Independencia: otro prompt o modelo, con temperatura baja

**Explicación**

Un evaluador automático solo es fiable si su prompt se diseña con la misma disciplina que cualquier otro. El ejemplo indica qué se evalúa y frente a qué fuente, define una rúbrica con criterios y escala (fidelidad, cobertura y formato de cero a dos), exige citar el fragmento que justifica cada nota, fija una salida JSON con campos conocidos y establece que, sin evidencia, se puntúa con cero.

Cinco buenas prácticas completan el diseño: rúbrica con descriptores, evidencia por cada nota, salida validable, calibración (comparar con una muestra revisada por personas y medir el acuerdo; si es bajo, ajustar rúbrica o prompt) e independencia (otro prompt y, si es posible, otro modelo, con temperatura baja, porque un modelo tiende a valorar con benevolencia sus propias salidas). Su resultado orienta, pero no sustituye a la revisión humana de los casos de mayor riesgo, y debe recalibrarse al cambiar modelo o rúbrica.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 07B · Iterar con hipótesis, regresiones y evaluación final](../../laboratorios/07B/README.md)
<!-- /labs-seccion -->

---

## 2.6 Comparación A/B de prompts: control riguroso

La comparación A/B permite determinar si una nueva versión del prompt es objetivamente mejor que la anterior. Para que la comparación sea válida, las condiciones deben ser idénticas salvo la variable que se modifica.

**Condiciones de un A/B válido**

- Exactamente las mismas entradas de prueba para ambas versiones
- Métricas predefinidas antes de ejecutar la comparación
- Una única dimensión principal modificada entre versiones
- Muestra suficiente para detectar diferencias no aleatorias
- Considerar la variabilidad natural del modelo (temperatura)

**Ejemplo ilustrativo**

Prompt A (v1.2): instrucción genérica sin ejemplos → Exactitud: 78%, Cumplimiento de formato: 65%

Prompt B (v1.3): se añade un ejemplo de salida esperada → Exactitud: 86%, Cumplimiento de formato: 91%

Conclusión: el ejemplo mejora ambas métricas en esta muestra (indica n y repite ejecuciones antes de afirmar significancia). Se aprueba v1.3.

**Explicación**

La **comparación A/B** determina si una nueva versión es objetivamente mejor que la anterior. Para que sea válida, las condiciones deben ser idénticas salvo la variable que se modifica: las mismas entradas, métricas definidas antes de ejecutar, una sola dimensión principal cambiada, muestra suficiente y consideración de la variabilidad del modelo.

En el ejemplo, la versión 1.2 (instrucción genérica sin ejemplos) obtiene un 78 % de exactitud y un 65 % de cumplimiento de formato, y la 1.3 (con un ejemplo de salida) un 86 % y un 91 %; se aprueba la 1.3. Aun así, deben indicarse el tamaño de la muestra y repetirse las ejecuciones antes de afirmar que la diferencia es significativa, porque con muestras pequeñas ocho puntos pueden deberse al azar. La disciplina del A/B protege de la autocomplacencia de creer que lo nuevo es mejor porque se ha trabajado en ello.

---

## 2.7 Análisis de errores: convertir fallos en mejoras

El análisis de errores no es el final del ciclo, es el inicio del refinamiento. Su objetivo es entender por qué falla el sistema para intervenir en la causa correcta, no corregir síntomas aislados que reaparecerán.

1. **Agrupar errores por tipo**: Clasificar los fallos: errores de formato, de contenido, de tono, de completitud, de seguimiento de instrucciones…
2. **Buscar patrones y causas**: ¿Qué tienen en común los casos fallidos? ¿Es una instrucción ambigua, falta de contexto, o un límite del modelo?
3. **Distinguir origen del fallo**: Identificar si el problema está en el prompt, en el modelo base, en los datos de entrada o en una herramienta externa.
4. **Priorizar por frecuencia e impacto**: Aplicar el principio de Pareto: corregir primero los fallos que afectan a más casos o que tienen mayor impacto en el negocio.

**Explicación**

El **análisis de errores** es el inicio del refinamiento: busca entender por qué falla el sistema para intervenir en la causa y no en síntomas aislados. Los pasos son agrupar errores por tipo (formato, contenido, tono, completitud, seguimiento de instrucciones), buscar patrones y causas, distinguir el origen (prompt, modelo, datos de entrada o herramienta externa) y priorizar por frecuencia e impacto con criterio de Pareto.

Distinguir el origen evita atribuir al prompt un fallo que no es suyo: si la entrada llega truncada, ningún prompt lo arregla, y si el modelo carece de una capacidad, reformular no la creará. Una minoría de causas suele explicar la mayoría de los fallos, y corregirlas primero consigue la mayor mejora con menos esfuerzo. Un fallo aislado es una anécdota; un patrón de fallos es un diagnóstico.

---

[← Anterior](01-diseno-y-pruebas.md) · [Índice del módulo](README.md) · [Siguiente →](03-optimizacion-y-mantenimiento.md)
