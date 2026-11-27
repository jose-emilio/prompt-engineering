[← Laboratorios](../README.md) · [Módulo 04](../../modulos/04-tecnicas-avanzadas-de-prompting/README.md) · [← 04A](../04A/README.md) · [05A →](../05A/README.md)

# Laboratorio 04B · Razonamiento paso a paso y autoconsistencia

Módulo 04 · Técnicas avanzadas de prompting · Duración estimada: 55 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Comprobar cuándo ayuda razonar paso a paso y cuándo conviene la autoconsistencia, y detectar cuándo no aportan nada. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Del chat: poder pegar o adjuntar el catálogo y el SLA, abrir conversaciones nuevas y repetir una misma petición varias veces (autoconsistencia). Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Resolver a mano un problema, y más si hay tiempo (8 min)
- Paso 2 · Respuesta directa (15 min)
- Paso 3 · Paso a paso (10 min)
- Paso 4 · Autoconsistencia (8 min)
- Paso 5 · Encontrar el razonamiento engañoso (5 min)
- Paso 6 · Plantear: el modelo extrae, el código calcula (5 min)
- Paso 7 · Redactar el informe (4 min)

<details>
<summary>Secciones del módulo relacionadas (9)</summary>

- [§2.1 Chain-of-Thought: razonamiento paso a paso](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#21-chain-of-thought-razonamiento-paso-a-paso)
- [§2.2 Solicitar pasos verificables: diseño práctico](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#22-solicitar-pasos-verificables-diseño-práctico)
- [§2.3 Zero-shot CoT y Few-shot CoT: variantes comparadas](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#23-zero-shot-cot-y-few-shot-cot-variantes-comparadas)
- [§2.4 CoT en modelos de razonamiento](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#24-cot-en-modelos-de-razonamiento)
- [§2.7 Plan-and-Solve: separar planificación y ejecución](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#27-plan-and-solve-separar-planificación-y-ejecución)
- [§2.8 Self-Consistency: comparar múltiples soluciones candidatas](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#28-self-consistency-comparar-múltiples-soluciones-candidatas)
- [§2.9 Aplicaciones y límites de Self-Consistency](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#29-aplicaciones-y-límites-de-self-consistency)
- [§3.4 Elegir la técnica según el problema](../../modulos/04-tecnicas-avanzadas-de-prompting/03-herramientas-revision-y-seleccion-de-tecnica.md#34-elegir-la-técnica-según-el-problema)
- [§3.5 Errores frecuentes al aplicar técnicas avanzadas](../../modulos/04-tecnicas-avanzadas-de-prompting/03-herramientas-revision-y-seleccion-de-tecnica.md#35-errores-frecuentes-al-aplicar-técnicas-avanzadas)

</details>

## Justificación del laboratorio

Facturación de Altanoria quiere que un asistente de IA calcule importes de forma automática: facturas con descuentos e IVA, prorratas por cambio de plan, créditos por incumplir la disponibilidad pactada y excesos de ejecuciones. El problema es que un modelo de lenguaje no calcula: predice texto. Con respuesta directa suele dar una cifra plausible y equivocada.

Hay técnicas para mejorar esto. Pedir que razone paso a paso (cadena de pensamiento) obliga al modelo a escribir los cálculos intermedios. Pedir varias soluciones y quedarse con la más votada (autoconsistencia) corrige errores aleatorios. Pero hay un caso peligroso: el razonamiento que parece impecable (ordenado, con pasos claros, en tono seguro) y que llega a un resultado erróneo. Quien lo lee tiende a verificar la apariencia, no el resultado.

Este laboratorio mide cuánto acierta cada estrategia con problemas de cálculo cuya solución exacta se conoce, cuánto cuesta cada una y qué tipos de problema siguen fallando incluso con razonamiento. La conclusión suele ser incómoda y útil: lo que se puede calcular con código determinista no debería calcularlo el modelo.

## Objetivos

Comprobar cuándo ayuda razonar paso a paso (Chain-of-Thought) y cuándo la autoconsistencia (varias soluciones y voto), y detectar el caso peligroso: un razonamiento de apariencia correcta que llega a un resultado erróneo. Los problemas son cálculos de facturación, SLA y consumo de Altanoria cuya solución exacta se conoce.

Al terminar el laboratorio se habrá conseguido:

- Diseñar tres variantes de prompt para el mismo problema: respuesta directa, paso a paso y varias muestras con votación.
- Medir mejora, coste en tokens y estabilidad.
- Verificar el resultado y no el aspecto del razonamiento.
- Identificar los tipos de error que el razonamiento explícito corrige y los que no.
- Complementar el modelo con una verificación determinista (código).

Conceptos que se usan:

- **Chain-of-Thought (CoT)**. Pedir al modelo que muestre los pasos intermedios antes de responder. Suele mejorar los problemas con varios pasos (cálculos, lógica) porque cada paso condiciona el siguiente. No garantiza que los pasos sean correctos ni que reflejen un «razonamiento interno» real: son texto generado. Algunos modelos de razonamiento ya lo hacen internamente y no conviene forzarlo ([§2.4 CoT en modelos de razonamiento](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#24-cot-en-modelos-de-razonamiento)).
- **Autoconsistencia**. Generar *n* soluciones independientes (con cierta temperatura) y elegir la respuesta más frecuente. Reduce errores aleatorios; no corrige errores sistemáticos (si el modelo se equivoca siempre igual, el voto no ayuda). Que las respuestas coincidan no las hace verdaderas: el voto mide el acuerdo entre respuestas, no la verdad, y cinco respuestas iguales pueden repetir el mismo error. Multiplica el coste por *n*.
- **Verificación externa**. Para cálculos exactos, el patrón más fiable es que el modelo plantee y una herramienta determinista calcule (véase el módulo 12).

## Recursos necesarios

> Sin acceso a una API: Resolver los 6 problemas de la muestra por estrategia en un chat (con el catálogo y el SLA adjuntos) o usar el modo manual de los scripts con `--n 10`. Con un modelo local se ejecutan los 30. Véase la [guía para trabajar sin API](../comun/sin-api.md).

- Un asistente de chat para el camino con chat; para el camino con código, además, Python 3.9 o superior y un modelo por API o local ([guía](../comun/README.md)).
- Datos: [`datos/problemas_calculo.csv`](datos/problemas_calculo.csv): 30 problemas con solución exacta.
- Hoja de cálculo: [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), con los seis problemas del camino con chat; calcula los aciertos y los tokens de cada estrategia y la autoconsistencia.
  - M-01 a M-08: facturas de Copilot (descuentos, IVA, periodo anual).
  - M-09 a M-14: prorrata por cambio de plan.
  - M-15 a M-20: créditos por incumplimiento de disponibilidad.
  - M-21 a M-24: exceso de ejecuciones en AgentHub.
  - M-25 a M-30: problemas con trampa de razonamiento.
- Script: [`evaluar_razonamiento.py`](evaluar_razonamiento.py), que inyecta como contexto el [catálogo](../comun/empresa/catalogo_planes.md) y el [SLA](../comun/empresa/sla.md).
- Alternativa manual: usar un chat con los 6 problemas de la muestra, adjuntar el catálogo y el SLA y resolverlos con cada estrategia.

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

Tiempo de ejecución con código (orientativo, medido con Gemma 4 de 8 B en local; con una API rápida y sin razonamiento suele ser bastante menos): con el razonamiento desactivado, 1 minuto en directo, 10 paso a paso y unos 40 en autoconsistencia; con el razonamiento por defecto, 9, 19 y 74 minutos (con `--n 10`, un tercio).

## Pasos de ejecución

Los pasos se hacen en orden. En el camino con chat se usa una muestra de 6 problemas con el catálogo de planes y el SLA adjuntos; en el camino con código, los 30 problemas con el script de evaluación.

### Paso 1 · Resolver a mano un problema, y más si hay tiempo (8 minutos)
1. Abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), pestaña «Los 30 problemas». Tiene los 30 problemas con las columnas `id`, `tipo`, `enunciado`, `trampa`, `respuesta correcta` y `explicación`; las dos últimas están ocultas de momento.
2. Abrir el [catálogo de planes](../comun/empresa/catalogo_planes.md) y el [SLA](../comun/empresa/sla.md): contienen las reglas de cálculo.
3. Resolver con calculadora, sin ayuda, el problema M-04 (y, si hay tiempo, M-09, M-15, M-20 y M-25). Anotar cada paso: base, descuento, subtotal, IVA, total.
4. Mostrar las columnas ocultas con el botón «+» de la cabecera y comparar con la respuesta correcta. El objetivo es entender las reglas antes de evaluar al modelo.

Comprobación: el problema M-04 está resuelto a mano y coincide con la respuesta correcta.

### Paso 2 · Respuesta directa (15 minutos)
Camino con chat:

1. Abrir [`datos/muestra_chat.md`](datos/muestra_chat.md): contiene seis problemas (M-01, M-04, M-09, M-15, M-25 y M-27). Las respuestas correctas están al final, plegadas. Para anotar las respuestas, los tokens y los aciertos de cada estrategia, usar la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx).
2. Abrir una conversación nueva, adjuntar o pegar el catálogo de planes y el SLA, y enviar este prompt con cada problema, uno por mensaje:

```text
Adjunto el catálogo de planes y el SLA. Responde sin explicar el razonamiento. Termina con una última línea con el formato exacto: RESPUESTA: <valor>

Problema: {enunciado}
```

3. Anotar la última línea de cada respuesta («RESPUESTA: …») y los tokens aproximados de la respuesta (una respuesta directa es corta).
4. Comparar con las respuestas correctas y contar aciertos, anotándolos en la pestaña «Problemas» de la hoja (la pestaña «Resultado» compara las estrategias).

<details>
<summary>Con código: los 30 problemas de una vez</summary>

En la terminal, en la carpeta `laboratorios/04B` (antes, `python ../comun/comprobar_entorno.py`):

```bash
python evaluar_razonamiento.py --modo directo
```

Si el modelo es de razonamiento (por ejemplo, Gemma 4 o los modelos con «thinking»), piensa antes de contestar aunque se le pida «sin explicar», y el contraste entre responder directamente y razonar paso a paso casi desaparece. Para ver el efecto que busca el laboratorio, desactivar ese razonamiento si el modelo lo permite (`export LLM_RAZONAMIENTO=no`) y repetir después con el comportamiento por defecto para comparar.

Para una prueba rápida, añadir `--n 10`. Anotar el acierto global, el acierto por tipo de problema, el acierto en los 22 problemas con trampa y los tokens de salida.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: hay un número de aciertos con la respuesta directa.

### Paso 3 · Paso a paso (10 minutos)
Camino con chat: repetir los mismos seis problemas, cada uno en una conversación nueva con el catálogo y el SLA, con este prompt:

```text
Adjunto el catálogo de planes y el SLA. Resuelve el problema paso a paso, mostrando los cálculos intermedios y comprobando cada regla aplicable antes de concluir. Termina con una última línea con el formato exacto: RESPUESTA: <valor>

Problema: {enunciado}
```

Anotar los aciertos y, de al menos tres problemas fallidos, copiar el razonamiento y señalar en qué paso aparece el error (¿una cuenta mal hecha?, ¿una regla mal aplicada?, ¿un redondeo?). Los aciertos y los tokens se anotan en las columnas «Paso a paso» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx).

<details>
<summary>Con código: paso a paso con los 30 problemas</summary>

En la terminal, en la carpeta `laboratorios/04B`:

```bash
python evaluar_razonamiento.py --modo paso_a_paso
```

Se crea `resultados_paso_a_paso.csv`: abrirlo y leer los razonamientos de tres problemas fallidos.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: hay un número de aciertos paso a paso y tres errores localizados en un paso concreto.

### Paso 4 · Autoconsistencia (8 minutos)
Camino con chat: para dos de los problemas que fallaron, pedir la solución cinco veces en conversaciones nuevas (con el prompt paso a paso) y anotar los cinco resultados. El resultado más repetido es el voto de la mayoría. Si los cinco coinciden en un error, es un error sistemático (el modelo entiende mal una regla); si hay dispersión, es un error aleatorio, y la votación lo corrige. La pestaña «Autoconsistencia» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) calcula los valores distintos y la respuesta mayoritaria.

<details>
<summary>Con código: autoconsistencia con 5 muestras</summary>

En la terminal, en la carpeta `laboratorios/04B`:

```bash
python evaluar_razonamiento.py --modo autoconsistencia --muestras 5 --temperatura 0.7
```

Mirar la columna `votos` de `resultados_autoconsistencia.csv`: en los problemas fallidos, ¿los cinco votos coinciden en el error o hay dispersión? La autoconsistencia cuesta unas cinco veces más tokens de salida.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: queda anotado si los errores son sistemáticos o aleatorios.

### Paso 5 · Encontrar el razonamiento engañoso (5 minutos)
Buscar un problema en el que el modelo muestre un razonamiento ordenado, con pasos claros y aparentemente correctos, pero con un resultado erróneo (son frecuentes en los problemas con trampa, M-25 a M-30). Documentar cuatro cosas: el enunciado, el razonamiento copiado, el paso exacto donde se produce el error y por qué la apariencia lo hace creíble.

Comprobación: hay un caso completo documentado.

### Paso 6 · Plantear: el modelo extrae, el código calcula (5 minutos)
La solución para los cálculos importantes es repartir el trabajo: el modelo solo extrae los parámetros (plan, cuota, minutos de caída) en un formato fijo y el cálculo lo hace una calculadora o un programa.

1. Elegir un problema de créditos por disponibilidad (por ejemplo, M-20). Pedir al asistente que no calcule nada, solo que devuelva los parámetros: plan, cuota mensual y minutos de caída del mes.
2. Hacer el cálculo con una calculadora, aplicando las reglas del SLA.
3. Comparar con la respuesta correcta.

<details>
<summary>Con código: escribir una función que calcule</summary>

Esta ampliación no tiene un script preparado: se escribe un fichero propio. En la carpeta `laboratorios/04B`, crear `calcular_propio.py` con este esqueleto para los problemas de créditos por disponibilidad (tipo `credito_sla`), completando la función `calcular` con las reglas de [`../comun/empresa/sla.md`](../comun/empresa/sla.md):

```python
import csv

# Parámetros que devolvió el modelo para cada problema (se anotan a mano, uno por problema)
PARAMETROS = {
    "M-20": {"plan": "Enterprise", "cuota": 4800, "minutos_caida": 480},
    # "M-15": {...}, "M-16": {...}
}

def calcular(p):
    """Devuelve el crédito en euros, con dos decimales, según el SLA."""
    raise NotImplementedError("completar con las reglas del SLA")

for fila in csv.DictReader(open("datos/problemas_calculo.csv", encoding="utf-8")):
    if fila["id"] in PARAMETROS:
        obtenido = f"{calcular(PARAMETROS[fila['id']]):.2f}"
        print(fila["id"], "OK" if obtenido == fila["respuesta_correcta"] else "NO", "esperado", fila["respuesta_correcta"], "obtenido", obtenido)
```

Para cada problema, pedir al asistente solo los parámetros en JSON, copiarlos en `PARAMETROS` y ejecutar:

```bash
python calcular_propio.py
```

Cada línea indica si el cálculo del código coincide con la respuesta correcta. Comparar el acierto de esta combinación (el modelo extrae, el código calcula) con el del modo directo medido antes en este laboratorio.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: queda anotado si la combinación acierta donde la respuesta directa fallaba.

### Paso 7 · Redactar el informe (4 minutos)
Escribir un informe de cinco líneas sobre cuándo usar cada estrategia, con su coste: respuesta directa, paso a paso, autoconsistencia y extracción más cálculo en código.

Comprobación: el informe incluye al menos una cifra de aciertos y una de coste.

## Conclusiones

### Qué se ha conseguido

Se ha comprobado que pasar de respuesta directa a razonamiento paso a paso multiplica el acierto en problemas de cálculo, que la votación entre varias soluciones corrige los errores aleatorios (a costa de varias veces más tokens) y que un razonamiento bien presentado puede llegar a un resultado erróneo: quien lee suele verificar la apariencia, no el resultado. La estrategia más fiable para los importes facturables, créditos, impuestos y fechas contractuales es repartir el trabajo: el modelo extrae los parámetros y el cálculo lo hace código determinista.

Referencia orientativa (rangos amplios con un modelo pequeño; con otro modelo pueden variar): Con un modelo que no razona antes de responder, se esperan con respuesta directa 20 % a 45 % de aciertos en los problemas de facturación; con razonamiento paso a paso, 65 % a 90 %; con autoconsistencia, igual o algo mejor que paso a paso, con varias veces más tokens de salida. Con un modelo de razonamiento, la respuesta directa ya acierta mucho más (en torno al 80 %) y el paso a paso aporta poco. Si el resultado queda muy lejos, conviene revisar datos, prompt y script antes de abrir la solución.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué tipo de problema mejoró más con razonamiento paso a paso? ¿Cuál no mejoró?

   <details>
   <summary>Respuesta</summary>

   Sin razonamiento propio del modelo, mejoraron sobre todo las prorratas (de 0/6 a 6/6), los excesos de AgentHub (de 0/4 a 4/4), los créditos de SLA (de 3/6 a 6/6) y las facturas (de 4/8 a 7/8). Mejoraron menos las trampas de razonamiento (de 2/6 a 4/6), que siguieron fallando en algún caso.

   </details>

2. ¿La autoconsistencia compensó su coste? ¿En qué problemas?

   <details>
   <summary>Respuesta</summary>

   En esta medición, poco: pasó del 90 % al 96,7 % (un problema más) con unas 3,7 veces más tokens de salida, y corrigió errores aleatorios como la coma decimal desplazada de la factura anual. Compensa cuando un error es caro y no hay una herramienta de cálculo; no compensa si el cálculo se puede programar.

   </details>

3. ¿Qué regla del catálogo falla más a menudo (descuentos no acumulables, prorrata sobre 30 días, tramos del crédito, el límite de «1 punto porcentual»)?

   <details>
   <summary>Respuesta</summary>

   Con razonamiento paso a paso fallaron el reembolso de una suscripción mensual (que es 0), la trampa de los 100 agentes y 100 tickets, y un error aritmético en una factura anual grande. En respuesta directa fallaron además todas las prorratas y los excesos de AgentHub, y la mitad de las facturas y de los créditos de SLA (el umbral de un punto porcentual y la garantía de cada plan).

   </details>

4. ¿Por qué un razonamiento largo y detallado puede aumentar la confianza injustificada de quien lo lee?

   <details>
   <summary>Respuesta</summary>

   Porque una forma ordenada y detallada se interpreta como señal de rigor, aunque el error esté en un paso (por ejemplo, redondear 1,011 a 1). Quien lee suele verificar la apariencia y no el resultado.

   </details>

5. ¿Qué cálculos de la empresa nunca se confiarían solo al modelo?

   <details>
   <summary>Respuesta</summary>

   Importes facturables, créditos y reembolsos, impuestos y fechas contractuales: se calculan con código determinista y el modelo solo extrae los parámetros.

   </details>

### Autoevaluación

- [ ] Se comprobó cada resultado contra la solución exacta del CSV y no contra el aspecto del razonamiento.
- [ ] Se compararon las tres variantes con los mismos problemas.
- [ ] Hay una tabla de acierto por tipo, no solo global.
- [ ] Se contabilizaron los tokens de salida de cada variante.
- [ ] Se documentó un error con razonamiento aparentemente correcto.
- [ ] El informe distingue errores sistemáticos de aleatorios.
- [ ] Se revisaron a mano los fallos para descartar falsos errores del comparador automático (por ejemplo, una respuesta correcta con distinto formato).

### Errores típicos

- Dar por bueno un razonamiento largo sin verificar la cifra final.
- Usar temperatura 0 en autoconsistencia (las cinco muestras serán idénticas).
- Comparar con distinto número de problemas entre variantes.
- Concluir que el paso a paso «siempre» mejora (con modelos de razonamiento puede no aportar).

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

> Los porcentajes dependen del modelo. Se indica el patrón habitual y los motivos.

### Soluciones a mano (Paso 1)

- M-04 (Starter, 35 usuarios, mensual): base 12 × 35 = 420,00; descuento por volumen del 10 % (≥ 20 usuarios, solo en mensual) = 42,00; subtotal 378,00; IVA 21 % = 79,38; total 457,38 €.
- M-09: (59 − 29) × 12 usuarios × 20/30 = 240,00 € sin IVA.
- M-15: disponibilidad 91,667 % (inferior al 95 %) → crédito del 50 % de la cuota: 299,50 €.
- M-20: disponibilidad 98,889 % en el plan Enterprise (garantizada 99,9 %). La diferencia es 1,011 puntos → más de 1 punto → tramo del 25 %: 25 % de 4.800 € = 1.200,00 €. Es una trampa de umbral: un error de redondeo (1,0 puntos) lleva al 10 %.
- M-25: 200 × 1,25 = 250; 250 × 0,75 = 187,50 € (no 200 €).

### Patrón de resultados habitual — expectativa previa a la medición

| Estrategia | Acierto global | Problemas con trampa | Tokens de salida | Observaciones |
|---|---|---|---|---|
| Directo | 25–70 % | 30–55 % | bajo | Falla en descuentos no acumulables, redondeos y umbrales. |
| Paso a paso | 70–90 % | 55–80 % | 3–8× | Corrige errores de orden de operaciones y reglas olvidadas. |
| Autoconsistencia (5 muestras) | +2 a +8 puntos sobre paso a paso | similar | ×5 sobre paso a paso | Ayuda con errores aleatorios; no con errores sistemáticos. |
| Plantear + código | 90–100 % en los tipos programados | 90–100 % | bajo | La parte de cálculo ya no depende del modelo; solo falla la extracción de parámetros. |

### Dónde se produce el error con más frecuencia

1. Descuentos no acumulables: aplicar volumen y educativo a la vez (la regla es aplicar el más favorable, no sumarlos).
2. Anual: aplicar descuento por volumen al plan anual (no procede).
3. Redondeo: redondear antes de tiempo o con otro criterio (la regla es mitad hacia arriba en cada importe).
4. Prorrata: usar los días reales del mes en lugar de 30.
5. Tramos del SLA: confundir «1 punto porcentual por debajo» con «1 %», y no distinguir el tramo del 50 % (< 95 %).
6. Trampas de sentido común: +25 % − 25 % ≠ 0; ejecutar 5 tareas con 5 agentes en 5 minutos; el mantenimiento programado no computa.

### El razonamiento engañoso (ejemplo típico)

En M-20, un modelo puede escribir: «Disponibilidad = (43.200 − 480)/43.200 = 98,889 %. La garantizada es 99,9 %. La diferencia es de 1,011 puntos, que es prácticamente 1 punto → crédito del 10 %: 480 €». Parece correcto: el cálculo de la disponibilidad es exacto, pero la conclusión redondea «1,011» a «1» y aplica el tramo equivocado. El error está en el paso final, no en las cuentas, y por eso se pasa por alto si solo se lee la forma.

### Función para el Paso 7 (créditos SLA)

```python
GARANTIZADA = {"Starter": 99.0, "Team": 99.5, "Enterprise": 99.9}

def credito_sla(plan, minutos_caida, cuota, dias_mes=30, minutos_mantenimiento=0):
    total = dias_mes * 24 * 60 - minutos_mantenimiento
    disponibilidad = 100 * (total - minutos_caida) / total
    garantizada = GARANTIZADA[plan]
    if disponibilidad >= garantizada:
        return 0.0
    if disponibilidad < 95.0:
        pct = 0.50
    elif garantizada - disponibilidad > 1.0:
        pct = 0.25
    else:
        pct = 0.10
    return round(cuota * pct, 2)
```

Prompt de extracción de parámetros (el modelo no calcula):

```text
Extrae del enunciado y devuelve solo un JSON: {"plan": "Starter|Team|Enterprise", "cuota": <número>, "minutos_caida": <entero>, "dias_mes": <entero>, "minutos_mantenimiento": <entero>}.
Si un dato no consta, usa null.
```

### Informe de ejemplo

«Para cálculos con reglas de varios pasos se recomienda separar plantear y calcular: el modelo extrae parámetros y el código calcula. Si no es posible programar el cálculo, usar razonamiento paso a paso y verificar el resultado con una calculadora. La autoconsistencia se reserva para decisiones donde un error aleatorio es costoso y se puede asumir ×5 de coste; no sustituye a la verificación porque los errores sistemáticos persisten. Ningún importe facturable debe depender únicamente de un modelo.»

### Resultados medidos con un modelo real

> Medición realizada el 24 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada a 16.384 tokens, una sola ejecución por condición y los scripts de este laboratorio. Gemma 4 es un modelo de razonamiento: por defecto piensa antes de contestar aunque se le pida «sin explicar», y eso borra el contraste que busca el laboratorio. Por eso la comparación principal se hizo con el razonamiento desactivado (`LLM_RAZONAMIENTO=no`, véase [`comun/README.md`](../comun/README.md)) y se repitió después con el comportamiento por defecto. Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

Con los 30 problemas del conjunto final (comparación numérica con tolerancia de 0,01), con el razonamiento desactivado:

| Estrategia | Aciertos | Tokens de salida | Observaciones |
|---|---|---|---|
| Directa | 9/30 (30 %) | 1.986 | Falló todas las prorratas (0/6) y los excesos de AgentHub (0/4), la mitad de las facturas (4/8) y de los créditos de SLA (3/6): respuestas rápidas y erróneas. |
| Paso a paso | 27/30 (90 %) | 20.358 | Acierta todas las prorratas, los créditos y los excesos, y 7/8 facturas; falla M-07 (una coma decimal desplazada en una factura anual de 100 usuarios: 7.114,80 en lugar de 71.148,00) y dos trampas: M-27 («no se puede determinar») y M-29 (pide datos en lugar de ver que una suscripción mensual no se reembolsa). |
| Autoconsistencia (5 muestras, T = 0,7) | 29/30 (96,7 %) | 75.758 | El voto corrige el error aritmético de M-07 y la trampa M-27; solo falla M-29, con ≈ 3,7 veces más tokens de salida que el paso a paso. |

Lecciones:

1. Pasar de respuesta directa a razonamiento explícito triplicó el acierto (del 30 % al 90 %) a cambio de multiplicar por 10 los tokens de salida
2. La votación de cinco muestras añadió un problema más (del 90 % al 96,7 %) con 3,7 veces más tokens: los errores del paso a paso eran sobre todo aleatorios, y la mayoría lo corrige el voto, pero no la trampa M-29, que falla de forma sistemática
3. Con un volumen real, el coste de tokens y la latencia de la autoconsistencia habría que justificarlos frente a una herramienta de cálculo determinista.

Con el razonamiento activado (el comportamiento por defecto de Gemma 4), las mismas tres estrategias dieron:

| Estrategia | Aciertos | Tokens de salida |
|---|---|---|
| Directa | 24/30 (80 %) | 17.437 |
| Paso a paso | 26/30 (86,7 %) | 39.692 |
| Autoconsistencia (5 muestras, T = 0,7) | 27/30 (90 %) | 150.624 |

El modelo ya razona internamente aunque se le pida responder sin explicar (≈ 580 tokens de salida por problema frente a ≈ 66 sin razonamiento), de modo que la respuesta «directa» acierta el 80 %: pedir «paso a paso» aporta poco (dos problemas más) y la autoconsistencia, uno más con casi cuatro veces más tokens. Otra ejecución de la respuesta directa con razonamiento dio 26/30 en lugar de 24/30, lo que muestra el ruido de una sola ejecución. Es el caso que advierten los errores típicos: con modelos de razonamiento, el «paso a paso» explícito puede no aportar, y el coste ya está en el razonamiento interno.

</details>

### Para seguir

- Probar la técnica Plan-and-Solve ([§2.7 Plan-and-Solve: separar planificación y ejecución](../../modulos/04-tecnicas-avanzadas-de-prompting/02-razonamiento-y-descomposicion.md#27-plan-and-solve-separar-planificación-y-ejecución)): pedir primero un plan y después su ejecución.
- Añadir ejemplos resueltos (few-shot CoT) y medir si ayudan.
- Repetir con un modelo de razonamiento y comparar si el «paso a paso» explícito sigue aportando.

---

[← Laboratorios](../README.md) · [Módulo 04](../../modulos/04-tecnicas-avanzadas-de-prompting/README.md) · [← 04A](../04A/README.md) · [05A →](../05A/README.md)
