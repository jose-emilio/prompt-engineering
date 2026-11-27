[← Laboratorios](../README.md) · [Módulo 12](../../modulos/12-analisis-de-informacion-y-datos/README.md) · [← 12A](../12A/README.md) · [12C →](../12C/README.md)

# Laboratorio 12B · Síntesis multidocumento para un decisor

Módulo 12 · Prompt Engineering para análisis de información y datos · Duración estimada: 50 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Redactar, a partir de informes que se contradicen en parte, un resumen para un decisor que no oculte esas diferencias. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Del chat: poder pegar o adjuntar los cinco informes en una conversación; conviene un modelo que admita textos largos. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Leer los informes (7 min)
- Paso 2 · Extraer las afirmaciones de cada informe (11 min)
- Paso 3 · Alinear y comparar por tema (10 min)
- Paso 4 · Redactar los resúmenes (6 min)
- Paso 5 · Comprobar la trazabilidad (6 min)
- Paso 6 · Comparar con una sola pasada (5 min)
- Paso 7 · Redactar la recomendación a Marketing (5 min)

<details>
<summary>Secciones del módulo relacionadas (10)</summary>

- [§2.1 Resumen ejecutivo](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#21-resumen-ejecutivo)
- [§2.2 Resumen técnico](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#22-resumen-técnico)
- [§2.3 Síntesis multidocumento](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#23-síntesis-multidocumento)
- [§2.4 Comparación documental](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#24-comparación-documental)
- [§2.6 Generación de hipótesis](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#26-generación-de-hipótesis)
- [§2.7 Análisis de causas](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#27-análisis-de-causas)
- [§2.10 Análisis de decisiones](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#210-análisis-de-decisiones)
- [§2.11 Límites del análisis textual con LLMs](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#211-límites-del-análisis-textual-con-llms)
- [§3.8 Caso completo: de documentos a indicadores](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#38-caso-completo-de-documentos-a-indicadores)
- [§3.9 Errores frecuentes y buenas prácticas](../../modulos/12-analisis-de-informacion-y-datos/03-analisis-con-python.md#39-errores-frecuentes-y-buenas-prácticas)

</details>

## Justificación del laboratorio

Marketing de Altanoria quiere publicar en la web un titular del tipo «Copilot mejora la productividad un X %». La Dirección, antes de aprobarlo, pide una síntesis de lo que dicen los datos disponibles y una recomendación sobre qué se puede afirmar. Hay cinco informes: uno interno de producto (telemetría), una encuesta de una consultora independiente, un análisis de tickets de soporte, un informe financiero y un observatorio de mercado. Miden cosas parecidas con métodos, poblaciones y periodos distintos, y sus cifras no coinciden.

Resumir cinco documentos de una vez, pegándolos todos y pidiendo «un resumen», es la forma más tentadora y menos fiable: el asistente puede omitir una fuente, mezclar cifras de dos informes o esconder una contradicción bajo un párrafo fluido. La forma fiable es un proceso en dos pasos, como lo haría un analista: primero extraer las afirmaciones de cada informe por separado, con su cifra, su método, su población y una cita literal (fase «map»), y después alinearlas y compararlas por tema para explicar cada diferencia (fase «reduce»).

La pregunta de fondo es si una diferencia entre dos cifras es una contradicción real o solo una diferencia de definición (por ejemplo, «adopción» medida como licencias con uso semanal frente a personas que dicen usar un asistente). Este laboratorio enseña a producir resúmenes trazables, en los que cada cifra se puede rastrear hasta su fuente, y a redactar una recomendación prudente sobre lo que se puede publicar.

## Objetivos

A partir de cinco informes que miden lo mismo con métodos distintos y se contradicen en parte, producir un resumen ejecutivo y un resumen técnico trazables, una tabla de contradicciones con su explicación (¿contradicción real o diferencia de definición?) y una recomendación sobre qué cifras puede afirmar Altanoria en público y cuáles no.

Al terminar el laboratorio se habrá conseguido:

- Descomponer una síntesis multidocumento en pasos: extraer afirmaciones por documento, alinear y comparar, sintetizar.
- Distinguir contradicciones reales de diferencias de definición, población, método y fecha.
- Mantener la trazabilidad: cada afirmación de la síntesis apunta a su fuente.
- Escribir resúmenes para audiencias distintas (dirección frente a especialistas).
- Reconocer los límites del análisis textual con un modelo y cuándo hace falta una persona.

Conceptos que se usan:

- **Síntesis multidocumento**. Combinar información de varias fuentes en un texto coherente. El peligro es mezclar datos de fuentes distintas como si fueran de una sola o «resolver» las contradicciones sin decirlo.
- **Comparabilidad**. Dos cifras son comparables solo si miden lo mismo (definición), en la misma población, con un método equivalente y en un periodo similar. Si no, la diferencia no es una contradicción: es una diferencia de medida.
- **Trazabilidad**. Cada dato de la síntesis lleva su fuente (por ejemplo, [A], [B]). Sin trazabilidad no se puede verificar.
- **Map-reduce con modelos**. Primero se procesa cada documento por separado (map) y luego se combinan los resultados (reduce). Reduce el riesgo de que el modelo ignore un documento largo y facilita la auditoría.

## Recursos necesarios

- Un asistente de chat (con capacidad de contexto suficiente para pegar cinco textos breves).
- Datos: [`datos/informes/`](datos/informes/) con cinco informes:
  - A · Informe interno de producto (telemetría de Altanoria).
  - B · Encuesta de una consultora independiente.
  - C · Análisis de tickets de soporte de Altanoria.
  - D · Informe financiero de Altanoria.
  - E · Observatorio de mercado (analista independiente).
- Hoja de cálculo: [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), con las fuentes y sus cifras, las citas comprobadas, la comparación por tema, los resúmenes, la trazabilidad de las cifras y la recomendación.
- Perfil de Altanoria: [`altanoria.md`](../comun/empresa/altanoria.md).

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Pasos de ejecución

Todo el laboratorio se hace en un chat, y las anotaciones van en la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx). Cada extracción se hace en una conversación nueva con un solo informe, para que no se mezclen las fuentes.

### Paso 1 · Leer los informes (7 minutos)
1. Abrir los cinco informes de la carpeta [`datos/informes/`](datos/informes/): [A, informe interno de producto](datos/informes/A_informe_interno_producto.md), [B, encuesta de una consultora](datos/informes/B_encuesta_consultora.md), [C, análisis de tickets de soporte](datos/informes/C_analisis_tickets_soporte.md), [D, informe financiero](datos/informes/D_informe_financiero.md) y [E, observatorio de mercado](datos/informes/E_observatorio_mercado.md).
2. En la pestaña «Fuentes» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) están ya, por informe, la fecha, la población (a quién se refiere), el método (cómo se midió) y las cifras sobre adopción, productividad, retención y satisfacción. Leer cada informe y comprobar tres de esas filas contra el texto.
3. Fijarse en qué cifras parecen contradecirse (por ejemplo, el 78 %, el 61 %, el 71 % y el 54 % de adopción).

Comprobación: la pestaña «Fuentes» muestra las cifras de los cinco informes y se puede señalar, en tres de ellos, la frase del informe de la que sale cada cifra.

### Paso 2 · Extraer las afirmaciones de cada informe (11 minutos)
Para cada informe, abrir una conversación nueva, pegar el informe y este prompt:

```text
Extrae las afirmaciones del informe en una lista JSON. Cada elemento: {"tema": "adopción|productividad|retención|satisfacción|mercado|otro", "afirmación": "…", "cifra": "valor y unidad o null", "método": "…", "población": "…", "periodo": "…", "cita": "frase literal del informe"}. Usa solo lo que dice el informe y null si no consta.

<informe>
{pegar el informe}
</informe>
```

Dejar el resultado en el chat. Después comprobar que cada cita existe de verdad en el informe (buscar la frase con Ctrl+F) y anotar en la pestaña «Citas», por afirmación, el informe y si la cita existe. Una cita que no existe es un dato inventado.

Comprobación: la pestaña «Citas» tiene las afirmaciones de cada informe con su comprobación y cuenta las citas inventadas.

### Paso 3 · Alinear y comparar por tema (10 minutos)
Abrir una conversación nueva, pegar las afirmaciones de los cinco informes y este prompt:

```text
Con las afirmaciones de los cinco informes, construye una tabla por tema con una columna por fuente y una columna «¿comparable?». Para cada diferencia, clasifica la causa: definición distinta, población distinta, método distinto (medición frente a percepción), periodo distinto o contradicción real sin explicación. No concilies ni promedies cifras.

<afirmaciones>
{pegar los cinco JSON}
</afirmaciones>
```

El resultado debe ser una tabla de comparación por tema (adopción, productividad, retención, satisfacción) con una columna por fuente y otra que diga si las cifras son comparables. Para cada diferencia, el asistente debe clasificar la causa: definición distinta, población distinta, método distinto (medición frente a percepción), periodo distinto o contradicción real sin explicación.

En la pestaña «Comparación» las cifras de cada fuente por tema aparecen ya (enlazadas con «Fuentes»); anotar si son comparables y la causa de la diferencia.

Comprobación: la pestaña «Comparación» tiene una fila por tema y cada diferencia tiene una causa.

### Paso 4 · Redactar los resúmenes (6 minutos)
Con la tabla anterior, pedir al asistente:

1. Un resumen ejecutivo de un máximo de 150 palabras para la Dirección (qué se sabe, qué no y qué se recomienda), con referencias a las fuentes entre corchetes [A] a [E].
2. Un resumen técnico (tabla y notas metodológicas) para el equipo de Producto.
3. Una tabla de contradicciones con la explicación de cada una.

Para el resumen ejecutivo se puede usar este prompt:

```text
Redacta un resumen ejecutivo de máximo 150 palabras para la Dirección: qué se sabe, qué no y qué se recomienda. Cada cifra lleva su fuente entre corchetes [A]–[E]. Distingue medición, percepción y estimación.

<tabla>
{pegar la tabla de comparación}
</tabla>
```

Dejar los productos en el chat o en el documento de texto y anotar en la pestaña «Resúmenes» cuáles se han hecho, las palabras del resumen ejecutivo y cuántas de sus cifras llevan fuente.

Comprobación: hay tres productos y cada cifra del resumen ejecutivo lleva su fuente.

### Paso 5 · Comprobar la trazabilidad (6 minutos)
Verificar, afirmación por afirmación, que cada cifra de los resúmenes aparece en el informe que se cita y que ninguna se ha atribuido a otra fuente. Anotar en la pestaña «Trazabilidad» una fila por cifra (la fuente que se cita y si la cifra aparece en ella) y, si hay error, de qué tipo: una cifra atribuida al informe equivocado, una cifra inventada o una cita parafraseada.

Comprobación: la pestaña «Trazabilidad» cuenta las cifras comprobadas y los errores.

### Paso 6 · Comparar con una sola pasada (5 minutos)
En una conversación nueva, pegar los cinco informes a la vez y pedir directamente el resumen ejecutivo. Comparar con el resultado del proceso en dos pasos: ¿omite alguna fuente?, ¿mezcla cifras?, ¿esconde una contradicción?, ¿se puede verificar? Anotar las respuestas (sí o no) en la pestaña «Una pasada».

Comprobación: la pestaña «Una pasada» tiene las cuatro respuestas de los dos procesos.

### Paso 7 · Redactar la recomendación a Marketing (5 minutos)
Escribir una recomendación para Marketing en el documento de texto: qué cifras se pueden publicar, con qué redacción exacta y bajo qué condiciones, y qué cifras no se pueden afirmar. En la pestaña «Recomendación», elegir para cada cifra si se puede publicar, con condiciones o no, incluida «mejora la productividad un 31 %».

Comprobación: la recomendación del documento distingue entre lo medido (con su población y método) y lo percibido, y la pestaña «Recomendación» cuenta las cifras de cada clase.

## Conclusiones

### Qué se ha conseguido

Se ha convertido un conjunto de informes que se contradicen en una síntesis trazable: afirmaciones extraídas por separado con su método y su cita, una comparación por tema que explica cada diferencia y resúmenes en los que cada cifra se puede rastrear hasta su fuente. Lo habitual es que buena parte de las contradicciones se deban a definiciones, poblaciones o métodos distintos más que a errores, y que el proceso en dos pasos detecte lo que una pasada única pasa por alto o mezcla. La recomendación final es prudente: se publica solo lo que está medido, con su población y su método, y no una cifra que mezcla fuentes.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Cuántas contradicciones eran reales y cuántas diferencias de definición o método?

   <details>
   <summary>Respuesta</summary>

   Ninguna era una contradicción real; todas se explican por diferencias de medida.

   </details>

2. ¿Por qué un modelo tiende a “promediar” cifras distintas? ¿Cómo se evita?

   <details>
   <summary>Respuesta</summary>

   Porque tiende a producir respuestas “razonables” y a conciliar; se evita pidiendo que no concilie, que cite la fuente y que clasifique las diferencias.

   </details>

3. ¿Qué información falta para poder decidir mejor (qué estudio nuevo haría falta)?

   <details>
   <summary>Respuesta</summary>

   Un estudio propio con grupo de control, definiciones comunes y periodo fijo.

   </details>

4. ¿Qué riesgos hay en publicar la cifra más favorable?

   <details>
   <summary>Respuesta</summary>

   Riesgo de publicidad engañosa, pérdida de credibilidad y responsabilidad legal.

   </details>

5. ¿Qué decisiones no deberían apoyarse solo en una síntesis automática?

   <details>
   <summary>Respuesta</summary>

   Las que tengan efectos económicos, jurídicos o reputacionales significativos.

   </details>

### Autoevaluación

- [ ] Cada cifra tiene fuente, método, población y periodo.
- [ ] Las citas del paso de extracción existen literalmente.
- [ ] Las diferencias de definición o método no se presentan como contradicciones.
- [ ] El resumen ejecutivo distingue medición de percepción y de estimación.
- [ ] Cada cifra de los resúmenes se verificó contra el informe de origen.
- [ ] No se «resolvieron» las contradicciones inventando una cifra única.
- [ ] La recomendación fija una redacción pública con condiciones.

### Errores típicos

- Promediar cifras de fuentes distintas.
- Atribuir a una fuente una cifra de otra.
- Ignorar el método (percepción frente a medición).
- Presentar la cifra más favorable.
- No comprobar las citas.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Tabla de comparación (referencia)

| Tema | A · Producto (interno) | B · Consultora | C · Soporte | D · Finanzas | E · Observatorio |
|---|---|---|---|---|---|
| Fecha/periodo | Datos a 30-sep-2026; informe 10-oct | Encuesta junio; publicado julio | Tickets enero–septiembre; informe 3-oct | 3T 2026; informe 28-oct | Estudio sept.; panel mayo |
| Población | 1.870 cuentas activas de Altanoria | 412 empresas españolas de 50–500 empleados, todos los proveedores | Cuentas Enterprise (estimación de gestores); muestra de 2.100 tickets | Ingresos de Copilot | Personas desarrolladoras en España; 1.150 en el panel |
| Adopción | 78 % de licencias con uso semanal (telemetría) | 61 % usa un asistente ≥ 1 vez/semana | 71 % de licencias Enterprise de uso «habitual» (estimación de gestores) | — | 54 % ≥ 1 vez/semana |
| Productividad | +31 % commits por persona y semana (con advertencia) y 9,5 h → 3,1 h en primera revisión (beta, 38 clientes) | +18 % mejora percibida | No medida | 25 % hipótesis de terceros (modelo de ROI) | +12 % mediana medida (rango −4 % a +35 %) |
| Retención | 5,2 % de baja de cuentas | — | — | 9,1 % de baja de ingresos | — |
| Satisfacción | CSAT 4,4 (post-ticket) | — | 4,1 (rendimiento), 4,6 (facturación) | NPS +38 | — |
| Mercado | — | — | — | ARR +34 % | Mercado +40 % en 2025; cuota de Altanoria 8 % |

### Tabla de contradicciones y su explicación

| # | Aparente contradicción | Explicación | ¿Real? |
|---|---|---|---|
| 1 | Adopción 78 % [A] frente a 71 % [C], 61 % [B] y 54 % [E] | Población y definición distintas: A mide licencias de clientes de Altanoria (que ya han comprado el producto) con telemetría; C estima en Enterprise por entrevistas; B y E miden el mercado general (incluye personas sin licencia). No son comparables. | No |
| 2 | Productividad +31 % [A], +25 % [D], +18 % [B], +12 % [E] | Medida frente a percepción frente a hipótesis: A mide *commits* (no es productividad, y coincide con el lanzamiento de la nueva versión del IDE); B recoge percepción; D usa una hipótesis de terceros; E es un ensayo controlado de tiempo de finalización. Solo E es una medición causal, y aun así con muestra pequeña y alta dispersión. | Parcial: ninguna cifra respalda un +31 % de productividad |
| 3 | Retención 5,2 % [A] frente a 9,1 % [D] | Base distinta: A cuenta bajas de cuentas; D bajas de ingresos (que pesan más cuando se van cuentas grandes o hay reducciones de plan). Ambas pueden ser ciertas. | No |
| 4 | «Las sugerencias han empeorado» [C] frente a CSAT alto [A] | Métricas distintas: CSAT post-ticket mide la atención de soporte, no la calidad de las sugerencias del producto; [C] indica que un 12 % de los tickets sobre calidad lo comenta, sin confirmar el cambio real. | No (hipótesis por verificar) |
| 5 | Crecimiento de mercado 40 % [E] frente a ARR +34 % [D] | Magnitudes distintas: el primero es el mercado europeo en 2025; el segundo, el ARR de Altanoria en 3T 2026 interanual. | No |

Conclusión: de cinco discrepancias aparentes, ninguna es una contradicción real sin explicar; todas son diferencias de definición, población, método o periodo. Eso es precisamente lo que un resumen automático “promedio” oculta.

### Resumen ejecutivo de ejemplo (≤ 150 palabras)

«Los datos disponibles respaldan que el uso de Copilot entre los clientes de Altanoria es alto (78 % de licencias con uso semanal [A]) y superior al del mercado español (54–61 % [B][E]), aunque las poblaciones no son comparables. En productividad no existe una cifra sólida: solo un ensayo controlado externo mide una mejora mediana del 12 % con gran dispersión [E]; el 31 % de [A] mide *commits* y el 25 % de [D] es una hipótesis de terceros. Sí hay evidencia propia de que la primera revisión de código pasa de 9,5 a 3,1 horas en la beta [A]. Se recomienda no publicar cifras de productividad general y comunicar únicamente la reducción del tiempo de primera revisión, con su contexto (38 clientes, mediana).»

### Resumen técnico (extracto)

- Las cifras de adopción difieren por población (clientes de Altanoria frente a mercado) y por fuente (telemetría, estimación de gestores, encuesta, panel).
- La única medición causal de productividad es [E]; el resto son indicadores indirectos [A], percepciones [B] o supuestos [D].
- Retención: bases distintas (cuentas frente a ingresos).
- Pendiente: medición propia controlada de productividad y análisis de la caída de calidad percibida desde agosto.

### Una sola pasada frente a dos pasos (resultado habitual) — expectativa previa a la medición

| Aspecto | Una pasada | Dos pasos (extracción + síntesis) |
|---|---|---|
| Cobertura de las fuentes | Suele privilegiar los primeros y últimos documentos | Todas las fuentes aparecen |
| Mezcla de cifras | Frecuente (promedia o atribuye mal) | Menos, y verificable gracias a las citas |
| Tratamiento de las contradicciones | Tiende a “resolverlas” con una cifra única | Se explican por definición/método |
| Verificabilidad | Baja | Alta |
| Coste | Menor | Mayor |

### Recomendación de ejemplo

- Se puede publicar: «En la beta de Revisión de pull requests, la mediana del tiempo hasta la primera revisión pasó de 9,5 a 3,1 horas (38 clientes)».
- Se puede publicar con matiz: «Más del 75 % de las licencias de Copilot de nuestros clientes se usan cada semana», indicando que se mide con telemetría de licencias de clientes de Altanoria.
- No se puede publicar: «Mejora la productividad un 31 %» (mide *commits*, no productividad); «un 25 %» (hipótesis); «un 18 %» (percepción) sin indicar que es una percepción.
- Pendiente: diseñar un estudio propio con metodología controlada.

</details>

### Para seguir

- Añadir un sexto informe inventado con una cifra extrema y comprobar cómo lo trata el modelo.
- Pedir un análisis de causas de la diferencia de adopción entre A y E y evaluar qué hipótesis son comprobables ([§2.7 Análisis de causas](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#27-análisis-de-causas)).
- Pedir un análisis *what-if*: «si la productividad real fuera del 12 % y no del 25 %, ¿cómo cambia el ROI de la hoja D?» ([§2.9 Análisis What-if y escenarios](../../modulos/12-analisis-de-informacion-y-datos/02-sintesis-y-toma-de-decisiones.md#29-análisis-what-if-y-escenarios)).

---

[← Laboratorios](../README.md) · [Módulo 12](../../modulos/12-analisis-de-informacion-y-datos/README.md) · [← 12A](../12A/README.md) · [12C →](../12C/README.md)
