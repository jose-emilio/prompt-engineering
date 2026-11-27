[← Laboratorios](../README.md) · [Módulo 10](../../modulos/10-generacion-creativa-y-contenidos/README.md) · [← 10B](../10B/README.md) · [11A →](../11A/README.md)

# Laboratorio 10C · Prompts visuales: de la descripción al guion gráfico

Módulo 10 · Generación creativa y producción de contenidos · Duración estimada: 65 minutos · Se hace solo con un chat

| De un vistazo | |
|---|---|
| Qué vas a hacer | Crear imágenes con prompts visuales, desde la descripción hasta un guion gráfico, y comprobar su coherencia. |
| Conviene haber hecho antes | [10A](../10A/README.md) y [10B](../10B/README.md) (recomendados) |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. **No hace falta generar imágenes**: el laboratorio trae trece imágenes de referencia con sus prompts (carpeta `imagenes/`) para evaluarlas. Si tu asistente crea imágenes, puedes generar las tuyas y compararlas, pero es opcional. |
| Cómo seguirlo | Todo el laboratorio se hace en el chat; ningún paso necesita código. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Analizar la anatomía de un prompt de imagen (8 min)
- Paso 2 · Escribir el prompt visual v1 (10 min)
- Paso 3 · Evaluar la primera imagen (9 min)
- Paso 4 · Iterar cambiando una variable (12 min)
- Paso 5 · Mantener la consistencia entre piezas (10 min)
- Paso 6 · Escribir el guion gráfico de 30 segundos (10 min)
- Paso 7 · Revisar límites y derechos (6 min)

<details>
<summary>Secciones del módulo relacionadas (10)</summary>

- [§3.1 Anatomía de un prompt de imagen](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#31-anatomía-de-un-prompt-de-imagen)
- [§3.2 Composición y lenguaje visual](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#32-composición-y-lenguaje-visual)
- [§3.3 Estilos y referencias visuales](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#33-estilos-y-referencias-visuales)
- [§3.4 Iteración de prompts visuales](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#34-iteración-de-prompts-visuales)
- [§3.5 Consistencia visual entre piezas](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#35-consistencia-visual-entre-piezas)
- [§3.6 Prompts para vídeo](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#36-prompts-para-vídeo)
- [§3.7 Storyboard y planificación](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#37-storyboard-y-planificación)
- [§3.8 Campañas visuales integradas](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#38-campañas-visuales-integradas)
- [§3.9 Limitaciones multimedia](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#39-limitaciones-multimedia)
- [§3.10 Derechos y uso responsable](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#310-derechos-y-uso-responsable)

</details>

## Justificación del laboratorio

El equipo de marketing de Altanoria prepara la campaña de lanzamiento de «Revisión de pull requests» y quiere fotografías de personas: una desarrolladora que revisa código, repetida en la página de lanzamiento, en las redes y en un vídeo de 30 segundos. Quien lo encarga escribe «una imagen moderna y atractiva sobre IA para programadores» y espera que la herramienta adivine el resto.

Un prompt de imagen es una especificación, y lo que no dice lo rellena la herramienta a su manera: añade un rótulo con el nombre del producto, un logotipo que no existe, una persona distinta en cada pieza. Con personas, los fallos se multiplican: la misma «desarrolladora» tiene otra cara y otra ropa en cada imagen, las manos y los rostros salen con artefactos, las exclusiones («sin logotipos», «sin texto») se cumplen solo en parte y cualquier cartel dentro de la imagen puede afirmar algo que la hoja de hechos prohíbe. El gusto no sirve para decidir qué hacer: hay que poder decir qué se pidió, qué se obtuvo y qué cambió.

Este laboratorio enseña a descomponer un prompt de imagen en sus capas, a escribirlo con restricciones, a evaluar imágenes con comprobaciones de sí o no, a mantener un personaje y un estilo a lo largo de una serie con una guía de estilo, a planificar un guion gráfico y a revisar límites, derechos y transparencia antes de publicar. No hace falta un generador de imágenes: el laboratorio incluye trece fotografías ya generadas, con el prompt exacto de cada una, y quien tenga un generador puede repetir los pasos con sus propias imágenes. Es opcional: amplía la parte multimedia del módulo, que los laboratorios 10A y 10B no practican.

## Objetivos

Al terminar el laboratorio se habrá conseguido:

- Descomponer un prompt de imagen en sus seis capas y detectar las que faltan y las contradicciones.
- Escribir un prompt visual que fija sujeto, entorno, composición, luz y paleta, estilo, formato y restricciones.
- Evaluar una imagen con seis comprobaciones de sí o no y comprobar si cada cambio de una sola variable aparece en la imagen.
- Comprobar rasgo por rasgo qué conserva una serie de piezas con guía de estilo y qué pierde sin ella (en especial, el aspecto de un personaje recurrente), y reescribir las exclusiones en positivo cuando la herramienta las ignora.
- Escribir un guion gráfico de 30 segundos con seis planos que suman la duración exacta.
- Revisar cada pieza antes de publicarla: texto dentro de la imagen, marcas, artefactos en rostros y manos, fidelidad al prompt y a los hechos, e indicación de uso de IA.

Conceptos que se usan (se explican en el módulo, secciones [§3.1 Anatomía de un prompt de imagen](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#31-anatomía-de-un-prompt-de-imagen) a [§3.10 Derechos y uso responsable](../../modulos/10-generacion-creativa-y-contenidos/03-produccion-multimedia-y-derechos.md#310-derechos-y-uso-responsable)):

- **Prompt visual**: una especificación con seis capas (sujeto y acción, entorno, composición, luz y paleta, estilo, y formato con restricciones); lo que no dice, lo decide la herramienta.
- **Iteración controlada**: se evalúa, se conserva lo que funciona, se cambia una sola variable y se vuelve a generar; si la herramienta ignora el cambio, se ajusta el objetivo.
- **Guía de estilo visual**: un bloque de texto fijo con los atributos persistentes (estilo, paleta, luz y la descripción del personaje recurrente), que se pega entero en el prompt de cada pieza de la serie.
- **Guion gráfico**: la secuencia de planos de un vídeo (duración, acción, cámara y restricciones) escrita antes de generar nada.

## Recursos necesarios

| Recurso | Para qué sirve | Dónde está o cómo conseguirlo |
|---|---|---|
| Un asistente de IA con chat (opcional) | Revisar un prompt o pedir una descripción de una imagen, si el asistente admite imágenes | Cualquiera (de pago o gratuito) |
| Un programa de hojas de cálculo | Anotar el análisis, las iteraciones y las revisiones | Excel, Google Sheets o LibreOffice Calc |
| Hoja de resultados | Anatomía, iteraciones, consistencia, guion y revisión | [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) |
| Hoja de hechos del producto | Única fuente de lo que las piezas pueden afirmar | [`datos/hechos_producto.md`](datos/hechos_producto.md) |
| Tres prompts de imagen para analizar | Paso 1 | [`datos/prompts_ejemplo.md`](datos/prompts_ejemplo.md) |
| Guía de estilo visual | Paso 5 | [`datos/guia_de_estilo.md`](datos/guia_de_estilo.md) |
| Comprobaciones visuales | Pasos 3, 4 y 7 | [`datos/comprobaciones_visuales.md`](datos/comprobaciones_visuales.md) |
| Trece imágenes de referencia y sus prompts | Pasos 3, 4, 5 y 7 | [`imagenes/`](imagenes/prompts.md) |
| Prompt visual vago (v0) | Punto de partida del Paso 3 | [`prompts/prompt_visual_v0.txt`](prompts/prompt_visual_v0.txt) |
| Un generador de imágenes (opcional) | Repetir los pasos con imágenes propias | Cualquiera; se usan los mismos criterios |

Antes de empezar, conviene crear un documento de texto vacío titulado «Laboratorio 10C · Mis resultados», donde ir pegando los prompts y lo que se pida anotar, y abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx).

Las imágenes de [`imagenes/`](imagenes/prompts.md) se generaron con FLUX.1 [dev] (cuantizado Q5_K_S) en noviembre de 2026; cada una lleva su prompt exacto, su tamaño y su semilla. Los resultados de un generador cambian de una herramienta y de una versión a otra: lo que se aprende aquí es el método de evaluación, no el comportamiento de un generador concreto. Si se dispone de un generador, se pueden generar imágenes propias con los prompts del laboratorio y evaluarlas con la misma rúbrica; antes de reutilizar las imágenes del laboratorio fuera del curso, conviene consultar la licencia de FLUX.1 [dev].

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [qué hacer si algo falla](../comun/si-algo-falla.md).

## Pasos de ejecución

Los pasos se hacen en orden. Se mira cada imagen con atención (conviene verla a tamaño completo) y se anota lo que se ve, no lo que se esperaba ver.

### Paso 1 · Analizar la anatomía de un prompt de imagen (8 minutos)
1. Leer [`datos/prompts_ejemplo.md`](datos/prompts_ejemplo.md): tres prompts que piden la imagen principal de la página de lanzamiento.
2. En la pestaña «Anatomía» de la hoja, marcar «sí» o «no» para cada una de las seis capas en cada prompt. Una capa cuenta si el prompt da un valor concreto («tonos azules» es una paleta; «moderna» no es un estilo). La última capa exige el formato y, al menos, una exclusión.
3. Buscar en el prompt C una contradicción entre dos instrucciones (se anota en el documento de texto, no en la hoja).

Comprobación: la pestaña «Anatomía» tiene las seis capas marcadas en los tres prompts y se puede señalar la contradicción del prompt C.

### Paso 2 · Escribir el prompt visual v1 (10 minutos)
1. Leer [`datos/hechos_producto.md`](datos/hechos_producto.md): la imagen no puede afirmar nada que no esté ahí (por ejemplo, no puede mostrar un cartel que diga «sin errores» ni sugerir que la función «reemplaza a los revisores»). La persona de la imagen es ficticia: no se describe a nadie real ni se imita a ninguna persona conocida.
2. Escribir en el documento de texto un prompt visual v1 para la imagen principal de la página (formato 16:9): una desarrolladora que revisa código en su portátil. Debe incluir las seis capas, una descripción concreta de la persona (edad aproximada, pelo, gafas, ropa) y, al menos, tres exclusiones (por ejemplo, sin texto legible en las pantallas, sin logotipos de marcas y sin otras personas).
3. Contar las capas del prompt con la misma lista del Paso 1 y corregir las que falten.

Comprobación: el prompt v1 cita las seis capas, describe a la persona y tiene al menos tres exclusiones.

### Paso 3 · Evaluar la primera imagen (9 minutos)
Se hace lo siguiente:

1. Abrir [`imagenes/01_prompt_vago.jpg`](imagenes/01_prompt_vago.jpg), generada con el prompt vago de [`prompts/prompt_visual_v0.txt`](prompts/prompt_visual_v0.txt), y [`imagenes/02_prompt_v1.jpg`](imagenes/02_prompt_v1.jpg), generada con el prompt de seis capas de referencia (el que se despliega al final del laboratorio; no hace falta mirarlo todavía).
2. Para cada imagen, anotar en la fila «v0» y en la fila «v1» de la pestaña «Iteraciones» cuántas de las seis capas respeta y cuántos de los tres elementos no pedidos aparecen (texto, logotipos, personas).
3. Contestar sí o no a las seis [comprobaciones visuales](datos/comprobaciones_visuales.md) de cada imagen; la hoja cuenta las cumplidas. Son dos preguntas distintas: si la imagen cumple lo que pedía el prompt (las cuatro primeras) y si es utilizable por sí misma (las dos últimas). Una imagen puede ser bonita y no haber respetado el prompt.
4. Comparar la imagen v1 de referencia con lo que pedía el prompt v1 escrito en el Paso 2 y fijarse en qué capa falta en la imagen aunque estuviera en el prompt.

Comprobación: la pestaña «Iteraciones» tiene las filas v0 y v1 con las capas respetadas, los elementos añadidos y las comprobaciones cumplidas.

### Paso 4 · Iterar cambiando una variable (12 minutos)
Las imágenes [`03_iter_luz.jpg`](imagenes/03_iter_luz.jpg), [`04_iter_composicion.jpg`](imagenes/04_iter_composicion.jpg) y [`05_iter_estilo.jpg`](imagenes/05_iter_estilo.jpg) parten del prompt v1 de referencia y cambian una sola variable cada una (con la misma semilla, así que lo demás debería conservarse). Sus prompts están en [`imagenes/prompts.md`](imagenes/prompts.md).

1. Para cada iteración, leer el cambio de su prompt y comprobar en la imagen si el cambio aparece: ¿se ve la luz pedida (contraluz de atardecer), el plano pedido (detalle de las manos sobre el teclado), el estilo pedido (ilustración vectorial)? Anotar en la pestaña «Iteraciones» la variable cambiada (de la lista) y si la imagen lo refleja.
2. Contar también los elementos que cambiaron sin que se hubiera pedido (texto, logotipos, personas) y contestar las seis comprobaciones visuales, prestando atención a las manos.
3. Decidir qué iteración se conserva y cuál se descarta. Si una iteración baja la puntuación, se vuelve a la versión anterior; si la herramienta ignora un cambio, se ajusta el objetivo en lugar de repetir la misma instrucción.
4. Escribir en el documento de texto la siguiente iteración que se probaría (una sola variable) y por qué.

<details>
<summary>Con un generador de imágenes: iterar con las variables propias</summary>

Generar la imagen del prompt v1 propio y tres iteraciones cambiando cada vez una variable, fijando la semilla si la herramienta lo permite, y contestar las comprobaciones visuales.

</details>

Comprobación: tres filas más en «Iteraciones», cada una con la variable cambiada, si la imagen lo refleja y las comprobaciones cumplidas.

### Paso 5 · Mantener la consistencia entre piezas (10 minutos)
1. Leer [`datos/guia_de_estilo.md`](datos/guia_de_estilo.md): el bloque fijo que se pega entero en cada prompt de la serie.
2. Mirar las tres piezas hechas con la guía ([`06_pieza1_con_guia.jpg`](imagenes/06_pieza1_con_guia.jpg), [`07_pieza2_con_guia.jpg`](imagenes/07_pieza2_con_guia.jpg) y [`08_pieza3_con_guia.jpg`](imagenes/08_pieza3_con_guia.jpg)) y marcar en la pestaña «Consistencia», rasgo por rasgo, si cada pieza lo mantiene o deriva.
3. Mirar las tres piezas hechas con los mismos encargos pero sin el bloque fijo (se pide «una desarrolladora» en lugar de Marta) ([`09_pieza1_sin_guia.jpg`](imagenes/09_pieza1_sin_guia.jpg), [`10_pieza2_sin_guia.jpg`](imagenes/10_pieza2_sin_guia.jpg) y [`11_pieza3_sin_guia.jpg`](imagenes/11_pieza3_sin_guia.jpg)) y anotar cuántos rasgos se pierden de media.
4. Pensar qué no consiguió mantener la guía (por ejemplo, el aspecto de Marta: la cara, el pelo, las gafas o el jersey) y qué se haría para mantenerlo mejor.

Comprobación: la pestaña «Consistencia» tiene marcados los seis rasgos de las tres piezas con guía y el número de rasgos que se pierden sin ella.

### Paso 6 · Escribir el guion gráfico de 30 segundos (10 minutos)
1. Escribir en el documento de texto seis planos para un vídeo de 30 segundos que presente la función: duración en segundos, acción (qué se ve), cámara, movimiento y transición, y restricciones de cada plano. Anotar las seis duraciones en la pestaña «Guion».
2. Comprobar que las duraciones suman 30 segundos exactamente y que ningún plano afirma algo que la hoja de hechos prohíbe (cifras distintas, «sin errores»).
3. Pensar en lo que se ha visto en las imágenes: ¿qué restricciones del guion es probable que la herramienta ignore (por ejemplo, «sin logotipos» o «sin texto») y qué planos serán difíciles (primeros planos de manos y de rostros)? Reescribirlas en positivo y evitar esos planos.

Comprobación: la pestaña «Guion» tiene seis planos y la suma de duraciones marca 30 segundos.

### Paso 7 · Revisar límites y derechos (6 minutos)
1. En la pestaña «Revisión», revisar cinco imágenes ([`06`](imagenes/06_pieza1_con_guia.jpg), [`07`](imagenes/07_pieza2_con_guia.jpg), [`08`](imagenes/08_pieza3_con_guia.jpg), [`12_cartel_0_errores.jpg`](imagenes/12_cartel_0_errores.jpg) y [`13_propuesta_corregida.jpg`](imagenes/13_propuesta_corregida.jpg)) y marcar «cumple» o «no cumple» en cinco criterios: sin texto escrito en la imagen, sin marcas ni logotipos de terceros, rostros y manos sin artefactos, respeta la hoja de hechos y lo que el prompt pedía, e indica que es una pieza generada con IA con el registro de la herramienta, el prompt y la fecha.
2. Para cada «no cumple», pensar qué cambio del prompt lo corregiría. La imagen 13 es el resultado de aplicar uno de esos cambios a la propuesta de la imagen 12: comprobar si ha funcionado.
3. Decidir qué piezas se publicarían tal cual, cuáles tras retocarlas y cuáles se descartarían. Recordar que las personas de la campaña son sintéticas: no deben presentarse como clientes ni como testimonios reales, y conviene indicar en la publicación que la imagen está generada con IA (consultar la normativa aplicable a la publicidad y a los contenidos sintéticos).


Comprobación: cada imagen tiene un veredicto en los cinco criterios y la hoja cuenta cuántos cumple cada una.

## Conclusiones

### Qué se ha conseguido

Se ha comprobado que un prompt de imagen es una especificación y que se evalúa mirando la imagen: lo que el prompt no dice lo rellena la herramienta con rótulos, logotipos y personas distintas, y lo que el prompt dice no siempre se cumple. También se ha visto que un cambio de una sola variable puede no aparecer en la imagen, que sin un bloque fijo de atributos el personaje cambia en cada pieza, que la guía mantiene el conjunto pero no garantiza cada detalle y que un cambio en el prompt puede arreglar un fallo y provocar otro.

Resultado con las imágenes de referencia (FLUX.1 [dev]): con el prompt vago, la imagen es una maqueta web con un logotipo inventado y un texto sin sentido; con las seis capas, aparece lo pedido, aunque el pelo «castaño» sale pelirrojo; de los tres cambios de una sola variable, dos se ignoran (la luz de atardecer y el plano de detalle de las manos) y uno se aplica (el estilo de ilustración); sin guía, las tres piezas muestran a tres mujeres distintas y con ella, a la misma persona con el mismo jersey y las mismas gafas; y la corrección del cartel «0 errores» elimina el cartel pero deja ver un logotipo de manzana.

Referencia de lo que suele ocurrir (con un generador de imágenes; otro generador o otra versión pueden comportarse de forma distinta): el texto dentro de la imagen sale deformado, las exclusiones se cumplen solo en parte, los cambios de luz y de composición se ignoran con frecuencia, las manos y los fondos traen artefactos y una guía pegada entera mantiene la serie más unida que prompts sueltos.

### Preguntas de reflexión

Conviene intentar responder antes de abrir cada respuesta.

1. ¿Por qué se evalúa lo que el prompt pide y no si la imagen «gusta»?

   <details>
   <summary>Respuesta</summary>

   Porque el gusto no permite decidir qué cambiar. Si el prompt pedía una luz lateral cálida y la imagen tiene luz de pantalla, hay un fallo que se puede nombrar, corregir y comprobar; «no me convence» no dice qué variable tocar.

   </details>

2. ¿Qué rellenó la herramienta por su cuenta con el prompt vago y por qué importa?

   <details>
   <summary>Respuesta</summary>

   Todo lo que el prompt no decía: el formato (una maqueta de página web en lugar de una ilustración), un logotipo con el nombre de la empresa, un titular y párrafos de texto (mal escritos y sin sentido) y la paleta. Importa porque son decisiones de marca y de derechos que nadie tomó: un rótulo puede salir mal escrito y un logotipo inventado puede infringir derechos de terceros.

   </details>

3. ¿Por qué se cambia una sola variable por iteración?

   <details>
   <summary>Respuesta</summary>

   Porque si se cambian la luz, la composición y el estilo a la vez no se sabe cuál produjo la mejora o el empeoramiento. Con un solo cambio, la diferencia de puntuación se atribuye a esa variable y se conserva o se descarta.

   </details>

4. ¿Qué pasó con la serie sin guía de estilo y qué lo evita?

   <details>
   <summary>Respuesta</summary>

   Cada pieza se interpreta por separado y el generador no recuerda las anteriores: sin guía salieron tres mujeres distintas, una de ellas en forma de ilustración, sin paleta ni ambiente comunes. Un bloque de texto fijo, pegado entero en cada prompt, mantiene los atributos persistentes (estilo, paleta, luz y el aspecto del personaje), aunque no los garantiza: con guía, el pelo «castaño» salió pelirrojo y la luz cambió de lado en una pieza.

   </details>

5. ¿Por qué se revisa la imagen y no solo el prompt?

   <details>
   <summary>Respuesta</summary>

   Porque la herramienta no siempre hace lo que el prompt dice, y una corrección puede arreglar un fallo y provocar otro. El prompt del cartel «0 errores» pedía una afirmación que la hoja de hechos prohíbe y la imagen mostró un cartel verde con un texto deformado; al quitar el cartel, apareció un logotipo de manzana que nadie había pedido. Lo que se publica es la imagen, así que es la imagen lo que se compara con las exclusiones y con las afirmaciones prohibidas, cada vez que cambia el prompt.

   </details>

### Autoevaluación

Esta lista sirve para valorar el propio trabajo (el laboratorio no se evalúa):

- [ ] Los tres prompts de ejemplo se descompusieron en las seis capas y se encontró la contradicción.
- [ ] El prompt v1 incluye las seis capas y al menos tres exclusiones.
- [ ] Cada iteración se comparó con su prompt y se anotó si el cambio aparece en la imagen.
- [ ] La serie de tres piezas se revisó rasgo por rasgo y se midió el efecto de quitar la guía.
- [ ] El guion tiene seis planos que suman 30 segundos.
- [ ] Cada pieza se revisó con los cinco criterios y cada «no cumple» tiene un cambio propuesto.

### Errores típicos

- Pedir «una imagen moderna y atractiva» y esperar que la herramienta adivine el estilo, la paleta y el formato.
- Escribir instrucciones que se anulan entre sí («luz suave» y «iluminación dramática»; «desenfocado» y «máximo detalle»).
- Cambiar varias variables a la vez y no saber qué produjo el cambio.
- Resumir la guía de estilo o cambiar sus palabras en cada prompt, en lugar de pegar el bloque entero.
- Pedir texto dentro de la imagen y publicar sin comprobarlo: lo fiable es añadirlo en postproducción.
- Dar por hecho que la herramienta cumple las exclusiones («sin logotipos», «sin texto») sin mirar la imagen, y no volver a revisarla después de cambiar el prompt.
- Describir al personaje de forma distinta en cada prompt (o no describirlo) y esperar que la herramienta lo recuerde.
- Repetir una instrucción que la herramienta ignora en lugar de reescribirla en positivo o ajustar el objetivo.
- Dar por buena una pieza porque «queda bien» sin compararla con el prompt y con la hoja de hechos.
- No registrar la herramienta, el prompt y la fecha de cada pieza.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

<details>
<summary>Análisis de los tres prompts de ejemplo</summary>

| Capa | Prompt A | Prompt B | Prompt C |
|---|---|---|---|
| Sujeto y acción | no | sí (una desarrolladora revisando código en un portátil) | sí (una desarrolladora de unos 35 años, de pelo castaño corto y gafas redondas, lee la pantalla de un portátil) |
| Entorno | no | no | sí (una oficina luminosa y sobria) |
| Composición | no | no | sí (plano medio, ligeramente de lado, ella en el tercio izquierdo) |
| Luz y paleta | no | sí (tonos azules) | sí (azul petróleo, crema y acento naranja) |
| Estilo | no | sí (fotografía realista) | sí (fotografía editorial realista) |
| Formato y restricciones | no | no (hay formato, pero ninguna exclusión) | sí (16:9; sin texto legible, sin logotipos y sin otras personas) |
| Capas presentes | 0 de 6 | 3 de 6 | 6 de 6 |

La contradicción del prompt C: pide a la vez «luz suave de ventana lateral» e «iluminación dramática de alto contraste».

</details>

<details>
<summary>Prompt visual de referencia (con las seis capas y exclusiones)</summary>

```text
Fotografía editorial realista para la página de lanzamiento de «Revisión de pull requests», una función de Altanoria Copilot.

Sujeto y acción: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo, lee con atención una revisión de código en la pantalla de un portátil.
Entorno: una oficina luminosa y sobria, con una planta y una taza sobre la mesa.
Composición: plano medio, ligeramente de lado; Marta ocupa el tercio izquierdo del encuadre y el tercio derecho queda libre para el titular.
Luz y paleta: luz natural cálida de ventana, desde la izquierda; azul petróleo, crema y un único acento naranja.
Estilo: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada.
Formato: 16:9.
Restricciones: sin texto legible en las pantallas, sin logotipos ni marcas de terceros y sin otras personas en la imagen.
```

</details>

<details>
<summary>Guion gráfico de referencia (30 segundos)</summary>

```markdown
# Guion gráfico de 30 segundos: campaña de lanzamiento de «Revisión de pull requests»

Formato 16:9, con la guía de estilo (fotografía editorial realista; luz natural cálida desde la izquierda; azul petróleo, crema y acento naranja). Protagoniza Marta, la desarrolladora de la guía. Los rótulos y la fecha se añaden en postproducción; la voz y el texto no afirman nada que la hoja de hechos prohíba.

| Plano | Duración | Acción (qué se ve) | Cámara y transición | Restricciones |
|---|---|---|---|---|
| 1 | 4 s | Marta llega a su mesa en una oficina luminosa y abre el portátil | Plano general fijo; corte | Sin texto legible; sin otras personas |
| 2 | 5 s | Aparece en la pantalla una notificación de un *pull request* nuevo; Marta lo abre | Plano medio de lado; paneo lento a la pantalla; fundido | Pantalla con formas, sin letras |
| 3 | 6 s | La pantalla muestra el código con tres globos de comentario sobre fragmentos concretos; Marta los lee | Plano medio frontal; zoom suave a la pantalla; corte | Sin cifras ni afirmaciones de rendimiento |
| 4 | 5 s | Marta acepta uno de los comentarios con un clic y sonríe levemente | Plano de detalle de la pantalla y plano corto de Marta; corte | Evitar primeros planos de las manos si se ven deformadas |
| 5 | 6 s | Marta decide aprobar el cambio: la decisión final es suya | Plano medio; sin movimiento; fundido | No sugerir que la herramienta aprueba sola |
| 6 | 4 s | Plano de cierre con Marta en el tercio izquierdo y espacio libre para el titular y la fecha | Plano general fijo | Sin texto en la imagen; el titular se añade después |

Suma de duraciones: 4 + 5 + 6 + 5 + 6 + 4 = 30 s.
```

</details>

<details>
<summary>Qué cambiaría en cada «no cumple» (y qué se vio al hacerlo)</summary>

| Fallo | Cambio del prompt |
|---|---|
| Aparece un rótulo con el nombre del producto | Añadir «sin texto legible dentro de la imagen; el titular se añade después» |
| Aparece un logotipo (por ejemplo, la manzana de un monitor) | Describir el objeto en positivo: «un monitor genérico sin marca» en lugar de «sin logotipos» y repetir la revisión |
| El personaje cambia de una pieza a otra | Pegar entera la guía con la descripción del personaje en cada prompt, usar los mismos términos y, si la herramienta lo permite, fijar la semilla o usar una imagen de referencia |
| Manos o rostro con artefactos | Cambiar el plano (evitar primeros planos de manos), regenerar con otra semilla o retocar la imagen |
| El prompt pide una afirmación (un cartel «0 errores») | Quitar el cartel y mostrar un elemento neutro, como comentarios de revisión sobre un fragmento de código |
| Aparece una cifra o un texto | Quitar la cifra del prompt y añadir los textos y las cifras de la fase beta en postproducción |
| No indica que es una pieza generada con IA | Añadir la indicación en la publicación y registrar herramienta, prompt y fecha |

</details>

### Resultados medidos con un modelo real

Las trece imágenes de [`imagenes/`](imagenes/prompts.md) se generaron en noviembre de 2026 con FLUX.1 [dev] (cuantizado Q5_K_S, 24 pasos, semilla fija) en una sola ejecución por prompt, así que son observaciones de una muestra pequeña, no medidas estadísticas. Lo que se ve en cada una:

| Imagen | Qué se ve |
|---|---|
| 01 · Prompt vago | Una maqueta de página web con un logotipo «Altanoria» que nadie dio, un titular mal escrito («Revisón de pul requests») y párrafos de texto sin sentido. Del prompt solo se respeta la idea general: no hay ninguna de las seis capas |
| 02 · Prompt v1 | Fotografía realista de una mujer de perfil con gafas y jersey azul petróleo que lee código en un portátil, en una oficina con luz de ventana. Respeta estilo, formato, plano y exclusiones (sin logotipos ni texto legible); añade una taza y plantas. Ella está en el tercio izquierdo, pero el pelo «castaño corto» sale pelirrojo y el «portátil» es un monitor |
| 03 · Cambia la luz | La luz pedida (contraluz de atardecer, dorado, desde la derecha) no se aprecia: sigue la luz diurna de ventana; cambia el fondo (más oficina) y el peinado |
| 04 · Cambia la composición | El plano de detalle de las manos se ignora: sigue siendo un plano medio de ella ante el monitor. Las manos salen sin artefactos visibles |
| 05 · Cambia el estilo | El estilo de ilustración vectorial se aplica a medias: es una ilustración digital con volumen y degradados, y cambian la cara, el peinado y el color del pelo |
| 06 · Pieza 1 con guía | Fotografía de la mujer pelirroja con gafas y jersey azul, en primer plano y sonriendo, con un monitor enorme delante; las manos quedan fuera de plano |
| 07 · Pieza 2 con guía | La misma mujer, con el pelo aún más corto y pendientes, sonriendo ante un portátil; manos y teclado con buen aspecto |
| 08 · Pieza 3 con guía | Retrato vertical de la misma mujer, con luz de ventana a la derecha; no se ve el botón de aprobar (el prompt no se cumple en esa parte) |
| 09 a 11 · Las tres sin guía | Tres mujeres distintas: una de pelo oscuro recogido y chaqueta mostaza en una oficina oscura (09), una ilustración plana de una mujer de pelo largo negro (10) y una mujer de pelo recogido y jersey negro señalando un portátil (11). Sin paleta, luz ni ambiente comunes |
| 12 · Cartel «0 errores» | La pantalla muestra un cartel verde con un texto deformado («OLITTHE»): la herramienta no sabe escribir la frase, pero el prompt pedía una afirmación que la hoja de hechos prohíbe, y el cartel verde sugiere un resultado perfecto |
| 13 · Propuesta corregida | Sin cartel ni texto, con tres comentarios en la pantalla, pero aparece un logotipo de manzana en el monitor (marca de terceros) y el pelo vuelve a cambiar. El cambio corrigió un fallo y provocó otro |

- El «naranja» de la paleta parece contagiarse al pelo: Marta, descrita como de pelo castaño, sale pelirroja en las piezas de la serie.
- Los resultados cambian con la semilla y con la versión del generador: sirven para practicar el método de evaluación, no para predecir lo que hará otro generador.
- El prompt exacto, el tamaño y la semilla de cada imagen figuran en [`imagenes/prompts.md`](imagenes/prompts.md), para repetirlas con otro generador.

</details>

### Para seguir

- Pedir una cuarta pieza con Marta y un compañero, con la misma guía de estilo, y comprobar si se mantienen los seis rasgos con dos personas en la escena.
- Si se dispone de un generador de imágenes, generar la imagen del prompt v1 propio y comparar su puntuación con la de la imagen 02.
- Convertir el guion en prompts de vídeo, uno por plano, con las seis capas de §3.6.

---

[← Laboratorios](../README.md) · [Módulo 10](../../modulos/10-generacion-creativa-y-contenidos/README.md) · [← 10B](../10B/README.md) · [11A →](../11A/README.md)
