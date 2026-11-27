[← Laboratorios](../README.md) · [Módulo 11](../../modulos/11-desarrollo-de-software/README.md) · [← 11B](../11B/README.md) · [12A →](../12A/README.md)

# Laboratorio 11C · Traducir y documentar código sin perder el comportamiento

Módulo 11 · Prompt Engineering aplicado al desarrollo de software · Duración estimada: 70 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Traducir una función a otro lenguaje y documentarla comprobando que no se pierde el comportamiento. |
| Conviene haber hecho antes | [11A](../11A/README.md) (recomendado) |
| Qué hace falta | Un chat con un asistente de IA, un navegador (para `comprobar.html`) y la hoja de cálculo del laboratorio. Para el camino con código, además, Python 3.9 o superior, acceso a un modelo (por API o local) y, opcionalmente, Node.js 18 o superior. |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Decidir qué debe conservar la traducción (8 min)
- Paso 2 · Pedir la traducción con el prompt básico (8 min)
- Paso 3 · Comprobar con los casos de aceptación (10 min)
- Paso 4 · Comprobar con la malla de equivalencia (10 min)
- Paso 5 · Corregir con evidencia (10 min)
- Paso 6 · Generar la documentación y contrastarla (12 min)
- Paso 7 · Escribir la especificación para un agente (12 min)

<details>
<summary>Secciones del módulo relacionadas (8)</summary>

- [§3.1 Traducción entre lenguajes: convertir preservando semántica](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#31-traducción-entre-lenguajes-convertir-preservando-semántica)
- [§3.2 Equivalencia de librerías: controlar sustituciones](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#32-equivalencia-de-librerías-controlar-sustituciones)
- [§3.6 Documentación de código: generar documentación fiel](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#36-documentación-de-código-generar-documentación-fiel)
- [§4.3 Flujo de desarrollo asistido por LLM](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#43-flujo-de-desarrollo-asistido-por-llm)
- [§4.4 Codificación con agentes](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#44-codificación-con-agentes)
- [§4.5 Desarrollo dirigido por especificaciones (SDD)](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#45-desarrollo-dirigido-por-especificaciones-sdd)
- [§4.6 El flujo de SDD en cinco pasos](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#46-el-flujo-de-sdd-en-cinco-pasos)
- [§4.7 Anatomía de una buena especificación](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#47-anatomía-de-una-buena-especificación)

</details>

## Justificación del laboratorio

El equipo de producto de Altanoria quiere que el cálculo de la factura de Copilot, que hoy vive en una función de Python, funcione también en el formulario web de la página de precios, escrito en JavaScript. Nadie quiere reescribirlo a mano: se lo piden a un asistente, que devuelve en segundos una función de aspecto impecable y con comentarios.

Una traducción que compila no es una traducción equivalente. Python y JavaScript redondean, comparan tipos y gestionan errores de forma distinta, y una diferencia de un céntimo en una de cada doscientas facturas no salta a la vista ni en una lectura ni en las pruebas que ya existen. Tampoco sirve fiarse de la documentación que el modelo escribe sobre el código: describe con seguridad comportamientos que el código no tiene. Y cuando el cambio siguiente (un plan nuevo) se lo encargan a un agente de codificación, una instrucción vaga produce cambios que nadie sabe revisar.

Este laboratorio enseña a escribir lo que una traducción debe conservar, a comprobar la equivalencia con más entradas que las del ejemplo, a corregir con evidencia, a contrastar la documentación generada con el comportamiento real y a escribir la especificación que se le daría a un agente. Es opcional: amplía la traducción, la documentación y el desarrollo dirigido por especificaciones del módulo, que los laboratorios 11A y 11B no practican.

## Objetivos

Al terminar el laboratorio se habrá conseguido:

- Escribir los requisitos que una traducción de código debe conservar (nombre, entradas inválidas, errores, redondeo y salida).
- Pedir una traducción con un prompt que fija el lenguaje, las bibliotecas y el contrato de comportamiento.
- Comprobar la equivalencia con los casos de aceptación y con una malla de entradas generada a partir del original.
- Clasificar los fallos (redondeo, tipos, errores, regla de negocio) y corregirlos con evidencia: caso, esperado y obtenido.
- Contrastar cada afirmación de la documentación generada con el comportamiento real del código.
- Redactar la especificación de un cambio para un agente de codificación y revisarla con una lista de seis puntos.

Conceptos que se usan (se explican en el módulo, secciones [§3.1 Traducción entre lenguajes: convertir preservando semántica](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#31-traducción-entre-lenguajes-convertir-preservando-semántica), [§3.2 Equivalencia de librerías: controlar sustituciones](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#32-equivalencia-de-librerías-controlar-sustituciones), [§3.6 Documentación de código: generar documentación fiel](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#36-documentación-de-código-generar-documentación-fiel) y [§4.3 Flujo de desarrollo asistido por LLM](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#43-flujo-de-desarrollo-asistido-por-llm) a [§4.7 Anatomía de una buena especificación](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#47-anatomía-de-una-buena-especificación)):

- **Equivalencia de comportamiento**: la traducción devuelve lo mismo que el original para las mismas entradas, incluidos los errores; que compile o que se lea bien no la demuestra.
- **Malla de equivalencia**: un conjunto grande de entradas, generado ejecutando el original, con el que se compara la traducción además de los casos de aceptación.
- **Documentación fiel**: describe lo que el código hace, no lo que el modelo supone que debería hacer; cada afirmación se comprueba ejecutando.
- **Especificación para un agente**: objetivo, alcance, criterios de aceptación medibles, restricciones, casos límite y definición de «hecho», revisados antes de escribir código.

## Recursos necesarios

| Recurso | Camino | Para qué sirve | Dónde está o cómo conseguirlo |
|---|---|---|---|
| Un asistente de IA con chat | Chat | Pedir la traducción, la corrección y la documentación | Cualquiera (de pago o gratuito) |
| Un navegador | Los dos | Comprobar la traducción sin instalar nada | [`comprobar.html`](comprobar.html), que se abre con doble clic |
| Un programa de hojas de cálculo | Los dos | Anotar requisitos, fallos y veredictos | Excel, Google Sheets o LibreOffice Calc |
| Hoja de resultados | Los dos | Requisitos, equivalencia, fallos, documentación y especificación | [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx) |
| La función de Python que se traduce | Los dos | Origen de la traducción | [`facturacion.py`](facturacion.py) |
| Reglas de negocio | Los dos | Entender la función | [`datos/especificacion.md`](datos/especificacion.md) |
| Tres especificaciones de ejemplo | Los dos | Paso 7 | [`datos/especificaciones_ejemplo.md`](datos/especificaciones_ejemplo.md) |
| Casos de aceptación (106) y malla de equivalencia (2.188 entradas) | Los dos | Comprobar la traducción | [`datos/casos_aceptacion.csv`](datos/casos_aceptacion.csv); los usa la página y el script |
| Traducción ingenua de respaldo | Los dos | Paso 4, si la primera traducción no falla en la malla | [`datos/traduccion_ingenua.js`](datos/traduccion_ingenua.js) |
| Python 3.9 o superior y acceso a un modelo | Código | Pedir la traducción por script | Véase la [guía](../comun/README.md) |
| Node.js 18 o superior (opcional) | Código | Comprobar desde la terminal | `node --version`; si no está, se usa la página |
| Scripts de apoyo | Código | Pedir la traducción y comprobarla | [`generar_traduccion.py`](generar_traduccion.py) y [`comprobar.js`](comprobar.js) |
| Prompt básico (v1) | Los dos | Paso 2 | [`prompts/prompt_traduccion_v1.txt`](prompts/prompt_traduccion_v1.txt) |

Antes de empezar, conviene crear un documento de texto vacío titulado «Laboratorio 11C · Mis resultados», donde ir pegando los prompts, las traducciones y lo que se pida anotar, y abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx).

Un aviso de seguridad: [`comprobar.html`](comprobar.html) ejecuta en el navegador el código que se pega, sin enviarlo a ningún sitio. Es código de un modelo: se lee antes (Paso 2) y no se pega nada con datos reales.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

Tiempo de ejecución con código (orientativo, medido con Gemma 4 de 8 B en local; con una API rápida y sin razonamiento suele ser bastante menos): pedir la traducción al modelo, unos 25 segundos cada vez; comprobarla con los 106 casos y con la malla, menos de 1 segundo.

## Pasos de ejecución

Los pasos se hacen en orden. Camino con chat: se pide todo en un chat y se comprueba pegando el código en `comprobar.html`. Camino con código: se pide la traducción por script y se comprueba con `node comprobar.js` (o con la página).

### Paso 1 · Decidir qué debe conservar la traducción (8 minutos)
1. Leer [`facturacion.py`](facturacion.py) y [`datos/especificacion.md`](datos/especificacion.md).
2. En el documento de texto (no en la hoja), escribir cinco requisitos que la versión en JavaScript debe cumplir, cada uno observable (con un ejemplo de entrada y de salida). Ayuda: piensa en el nombre y la firma, en qué entradas se rechazan, en cómo se avisa de un error, en el redondeo de cada importe y en la forma del resultado.
3. Anotar para cada requisito en qué se parecen y en qué pueden diferir Python y JavaScript (por ejemplo, `5.0` es un decimal en Python y el mismo número que `5` en JavaScript).

Comprobación: el documento tiene cinco requisitos con un ejemplo y la diferencia posible entre lenguajes.

### Paso 2 · Pedir la traducción con el prompt básico (8 minutos)
Se lee el prompt básico (v1):

```text
Traduce a JavaScript esta función de Python:

{{codigo}}
```

1. Leer el prompt: dice el lenguaje de destino, pero no dice la versión, las bibliotecas, el nombre de la función, qué hacer con los errores ni cómo redondear.
2. Pedir la traducción: en el chat, pegando el prompt con el contenido de [`facturacion.py`](facturacion.py) donde dice `{{codigo}}`.

<details>
<summary>Con código: pedir la traducción por script</summary>

Abrir una terminal en la carpeta `laboratorios/11C` (antes, `python ../comun/comprobar_entorno.py`) y ejecutar:

```bash
python generar_traduccion.py --prompt prompts/prompt_traduccion_v1.txt --salida traduccion_v1.js
```

El script envía el prompt al modelo y guarda en `traduccion_v1.js` el primer bloque de código de la respuesta. No lo ejecuta.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Antes de comprobar nada, leer la traducción con esta lista y contestar sí o no en la pestaña «Lectura v1»: la función se llama `calcularFacturaCopilot`; no usa bibliotecas (ni `require` ni `import`); lanza `Error` cuando el original lanza `ValueError`; devuelve números (no textos); redondea cada importe.

Comprobación: hay una traducción guardada en el documento de texto y la pestaña «Lectura v1» tiene una marca en cada punto.

### Paso 3 · Comprobar con los casos de aceptación (10 minutos)
1. Pegar la traducción en [`comprobar.html`](comprobar.html) y pulsar «Comprobar con los 106 casos».

<details>
<summary>Con código: comprobar desde la terminal</summary>

En la terminal, en la carpeta `laboratorios/11C`:

```bash
node comprobar.js traduccion_v1.js
```

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

2. Anotar en la pestaña «Equivalencia» cuántos casos pasan y, si hay fallos, cuántos hay de cada categoría (no lanza error, error de más, formato, redondeo o regla de negocio).
3. Si la traducción ni siquiera se carga, anotar el mensaje: es el resultado y su causa suele ser una biblioteca que no existe, un nombre distinto o un error de sintaxis.

Comprobación: la pestaña «Equivalencia» tiene el recuento de casos de la traducción v1 y, si falla, su categoría.

### Paso 4 · Comprobar con la malla de equivalencia (10 minutos)
Los 106 casos son pocos. La malla reúne las 2.188 combinaciones válidas de plan, usuarios (hasta 200), periodo y descuento educativo, con el resultado que calcula la versión en Python.

1. Pulsar «Comprobar con la malla» en la página (o `node comprobar.js traduccion_v1.js --malla`).
2. Anotar en «Equivalencia» cuántas entradas pasan y comparar con el Paso 3: una traducción puede pasar los 106 casos y fallar en la malla.
3. Si la traducción pasa la malla entera, hacer los pasos siguientes con [`datos/traduccion_ingenua.js`](datos/traduccion_ingenua.js), que pasa los 106 casos y falla en 12 entradas de la malla.
4. Si hay entradas que fallan, anotar en «Equivalencia» cuántas hay de cada categoría (no lanza error, error de más, formato, redondeo, regla de negocio).

Comprobación: «Equivalencia» tiene los dos recuentos (106 casos y malla) y los fallos por categoría.

### Paso 5 · Corregir con evidencia (10 minutos)
1. Escribir un prompt de corrección que incluya la traducción, una de las entradas que fallan con el valor esperado y el obtenido (los da la página), y el requisito del Paso 1 que se incumple. Pedir el cambio mínimo y sin cambiar nada más.
2. Pegar la traducción corregida en la página y comprobar los 106 casos y la malla. Anotar los dos recuentos en la columna «Corregida» de «Equivalencia».
3. Si sigue habiendo fallos, repetir con otra entrada como evidencia. Con un modelo pequeño es normal que una corrección no arregle nada o rompa casos que pasaban: por eso se comprueban siempre los dos conjuntos. Parar tras tres intentos; si no se consigue, la traducción de referencia está plegada al final.

Comprobación: hay una traducción corregida con sus dos recuentos, o se han hecho tres intentos con las dos columnas de «Equivalencia» rellenas.

### Paso 6 · Generar la documentación y contrastarla (12 minutos)
1. Pedir al asistente la documentación (en formato JSDoc) de la traducción corregida. El prompt debe pedir propósito y ejemplo de uso, parámetros y retorno, los errores que lanza y que no documente nada que el código no haga.
2. Elegir seis afirmaciones comprobables de esa documentación.
3. Contrastar cada una con el comportamiento real, usando la sección «Probar una llamada» de la página (o `node comprobar.js archivo.js --probar Team 25 mensual false`), y anotar en la pestaña «Documentación» el veredicto (correcta, incorrecta o no se puede comprobar).

Comprobación: la pestaña «Documentación» tiene seis veredictos.

### Paso 7 · Escribir la especificación para un agente (12 minutos)
Altanoria va a lanzar el plan Business: 39 € al mes en facturación mensual, 33 € al mes en la anual y un mínimo de 20 usuarios, con las mismas reglas de descuento que los demás planes. Se lo encargarán a un agente de codificación.

1. Leer [`datos/especificaciones_ejemplo.md`](datos/especificaciones_ejemplo.md): tres especificaciones del mismo cambio. En la pestaña «Especificación», puntuar cada una con la lista de seis puntos (marcar «sí» o «no»).
2. Escribir la propia especificación del cambio, no el código: objetivo y contexto, alcance y exclusiones, criterios de aceptación (con cifras), restricciones técnicas, casos límite y errores, y definición de «hecho». Añadir un plan de tareas pequeñas, cada una con su comprobación.
3. Puntuarla con la misma lista en la columna «La mía» y corregir los puntos que no se cumplan.
4. Comprobar con una persona o con el asistente que cada criterio de aceptación se puede convertir en una prueba.

Comprobación: las tres especificaciones de ejemplo están puntuadas, la propia pasa los seis puntos de la lista y cada criterio de aceptación es medible.

## Conclusiones

### Qué se ha conseguido

Se ha comprobado que una traducción que se lee bien y pasa los casos del ejemplo puede no ser equivalente, y que la forma de saberlo es compararla con muchas entradas generadas por el original. También se ha visto que el prompt marca la diferencia (versión, bibliotecas, errores, redondeo y salida), que la documentación del modelo hay que ejecutarla y que un cambio encargado a un agente se pide con una especificación revisable.

Resultado medido con Gemma 4 (8 B, en local): de 10 traducciones con el prompt básico, 8 pasan los 106 casos de aceptación y ninguna pasa la malla; con el prompt con contrato ocurre lo mismo. Ninguna de las 20 es equivalente al original a la primera.

Referencia de lo que suele ocurrir (con un modelo pequeño; con otro pueden variar): la traducción pasa los casos del ejemplo o los pasa casi todos, falla en unas pocas entradas de la malla por el redondeo, y la corrección con evidencia no siempre arregla el fallo a la primera.

### Preguntas de reflexión

Conviene intentar responder antes de abrir cada respuesta.

1. ¿Por qué pasar los 106 casos no demuestra que la traducción sea equivalente?

   <details>
   <summary>Respuesta</summary>

   Porque 106 casos cubren los escalones de descuento y los errores, pero no todos los importes: un redondeo hecho con decimales de coma flotante solo se equivoca en algunas combinaciones concretas (por ejemplo, Team con 35 usuarios en facturación mensual). Cuantas más entradas generadas por el original, más difícil es que una diferencia se esconda.

   </details>

2. ¿Qué diferencias entre Python y JavaScript provocaron los fallos?

   <details>
   <summary>Respuesta</summary>

   Sobre todo el redondeo (Python usa `Decimal` con redondeo de la mitad hacia arriba; los números de JavaScript son decimales binarios y `Math.round` o `toFixed` no coinciden en algunas mitades) y los tipos (en JavaScript `5.0` es `5`, un texto o un booleano no se rechazan solos, `toFixed` devuelve un texto). Los errores también cambian: `ValueError` pasa a ser un `Error`.

   </details>

3. ¿Por qué se corrige con la entrada, el valor esperado y el obtenido y no con «está mal el redondeo»?

   <details>
   <summary>Respuesta</summary>

   Porque la evidencia permite al modelo localizar la línea responsable y permite a quien revisa comprobar que la corrección arregla ese caso sin romper los demás. Una queja general produce cambios amplios que no se pueden revisar.

   </details>

4. ¿Qué tipo de afirmación de la documentación generada conviene sospechar más?

   <details>
   <summary>Respuesta</summary>

   Las que describen comportamientos que no se ven en el código: validaciones que no existen, mensajes de error con un texto concreto, mayúsculas y minúsculas que se aceptan, o descuentos que se suman cuando el código elige el mayor. Se comprueban ejecutando la función con esa entrada.

   </details>

5. ¿Cuándo compensa escribir una especificación en lugar de pedir el cambio en el chat?

   <details>
   <summary>Respuesta</summary>

   Cuando el cambio lo ejecuta un agente que edita archivos, cuando lo revisan varias personas o cuando debe poder auditarse: la especificación fija la intención en un solo sitio y se revisa antes de gastar tiempo en código. Para un cambio de dos líneas sobra.

   </details>

### Autoevaluación

Esta lista sirve para valorar el propio trabajo (el laboratorio no se evalúa):

- [ ] Los cinco requisitos tienen un ejemplo y la diferencia posible entre lenguajes.
- [ ] La traducción se leyó antes de comprobarla.
- [ ] Se comprobaron los 106 casos y también la malla.
- [ ] Cada fallo tiene su categoría y una entrada con valor esperado y obtenido.
- [ ] La corrección se pidió con evidencia y se comprobó de nuevo.
- [ ] Seis afirmaciones de la documentación se contrastaron ejecutando la función.
- [ ] La especificación pasa los seis puntos de la lista.

### Errores típicos

- Dar por equivalente una traducción porque «compila» o porque pasa los casos del ejemplo.
- Pedir la traducción sin decir la versión, las bibliotecas, el nombre de la función ni el comportamiento ante errores.
- Aceptar una biblioteca que el modelo sugiere sin comprobar que existe (`decimal.js` y similares) cuando el contrato decía que no se usaran.
- Corregir con «está mal el redondeo» en lugar de entregar la entrada, lo esperado y lo obtenido.
- Copiar la documentación generada sin ejecutar ninguno de sus ejemplos.
- Escribir la especificación como una lista de deseos («que funcione bien») sin criterios que se puedan convertir en pruebas.
- Dejar que el agente modifique las pruebas para que pasen.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

<details>
<summary>Los cinco requisitos y sus diferencias entre lenguajes</summary>

| Requisito | Ejemplo | Diferencia posible |
|---|---|---|
| Nombre y firma | `calcularFacturaCopilot(plan, usuarios, periodo = "mensual", educativo = false)` | El original usa `snake_case`; el nombre cambia y debe fijarse |
| Entradas inválidas | Texto `"10"`, booleano y decimal `5.5` se rechazan | En JavaScript `5.0` es `5`; un texto o un booleano pueden pasar si solo se mira `usuarios < 1` |
| Errores | Plan, periodo o usuarios inválidos → `Error` | `ValueError` no existe; no se devuelven `null` ni objetos de error |
| Redondeo | Cada importe a 2 decimales, mitad hacia arriba, en el orden base, descuento, subtotal, IVA y total | `Decimal` frente a decimales binarios: `Math.round` y `toFixed` fallan en algunas mitades |
| Salida | Objeto con seis claves de tipo `number` | `toFixed` devuelve un texto; `descuento_pct` es una fracción |

</details>

<details>
<summary>Prompt v2 de referencia (con contrato)</summary>

```text
Eres un desarrollador que traduce código entre lenguajes conservando el comportamiento exacto del original. No añades funciones, mensajes ni validaciones que el original no tenga.
---USUARIO---
Traduce a JavaScript la función de Python de abajo.

Lenguaje: de Python 3.9 a JavaScript ES2020 (debe funcionar igual en Node.js 18 y en un navegador).
Bibliotecas: ninguna. No uses import, require ni módulos; solo JavaScript estándar.

Contrato que debe cumplir la traducción:
1. Nombre y firma: calcularFacturaCopilot(plan, usuarios, periodo = "mensual", educativo = false).
2. Entradas inválidas: usuarios debe ser un número entero positivo. Se rechazan los textos ("10"), los booleanos (true), los decimales (5.5), el cero y los negativos. El plan y el periodo se comparan tal cual, sin cambiar mayúsculas.
3. Errores: donde el original lanza ValueError, lanza un Error (con un mensaje claro). No devuelvas null ni un objeto con un campo de error.
4. Redondeo: cada importe (base, descuento, subtotal, IVA y total), en ese orden, se redondea a 2 decimales con la mitad hacia arriba (137,025 → 137,03). Math.round y toFixed no lo garantizan con decimales binarios: calcula internamente en céntimos con números enteros y devuelve siempre euros (por ejemplo, 12 y no 1200).
5. Salida: un objeto con las claves base, descuento_pct, descuento, subtotal, iva y total, todas de tipo number (no cadenas). descuento_pct es la fracción (0.1, 0.15, 0.3 o 0).

Responde solo con un bloque de código con la función y las constantes que necesite. Sin ejemplos de uso, sin console.log y sin explicaciones.

Función de Python que hay que traducir:

{{codigo}}
```

</details>

<details>
<summary>Traducción de referencia, con su documentación JSDoc</summary>

El comentario JSDoc de la función es la documentación de referencia del Paso 6: cada afirmación se ha comprobado ejecutando la función (el ejemplo, el descuento que se aplica, los errores y qué valores de `usuarios` se rechazan). Sirve para contrastar la que genere el asistente. Las imprecisiones que se observaron en documentaciones generadas fueron llamar «adicional» al descuento educativo (se aplica el mayor de los dos, no se suman), afirmar que la base es «divisible por 100» o que los precios del plan están en céntimos (están en euros).

```javascript
// Traducción de referencia de calcular_factura_copilot (Python 3.9) a JavaScript (ES2020, sin bibliotecas).
// Los importes se calculan en céntimos con enteros: así el redondeo «mitad hacia arriba» es exacto, igual que con Decimal en Python.
const PLANES = {
  Starter: { mensual: 12, anual: 10, minimo: 1 },
  Team: { mensual: 29, anual: 24, minimo: 5 },
  Enterprise: { mensual: 59, anual: 49, minimo: 50 },
};

// Porcentaje de un importe en céntimos, redondeado a céntimo con la mitad hacia arriba (porcentaje en enteros: 21 = 21 %).
function porcentaje(centimos, pct) {
  return Math.floor((centimos * pct + 50) / 100);
}

/**
 * Calcula la factura de Altanoria Copilot para un plan, un número de usuarios y un periodo.
 *
 * Reglas: la base es el precio por usuario multiplicado por los usuarios (en el periodo anual, por 12 meses). El descuento por volumen
 * solo se aplica en el periodo mensual: 10 % con 20 o más usuarios y 15 % con 100 o más. El descuento educativo es del 30 %, en
 * cualquier periodo. No se acumulan: se aplica el mayor de los dos porcentajes. El IVA es el 21 % del subtotal (base menos descuento).
 * Cada importe se redondea a céntimos con la mitad hacia arriba, en este orden: descuento, subtotal, IVA y total.
 *
 * @param {string} plan Plan contratado: "Starter", "Team" o "Enterprise".
 * @param {number} usuarios Número de usuarios, entero y mayor o igual que el mínimo del plan (Starter 1, Team 5, Enterprise 50).
 * @param {string} [periodo="mensual"] Periodo de facturación: "mensual" o "anual".
 * @param {boolean} [educativo=false] Si es exactamente `true`, se aplica el descuento educativo o sin ánimo de lucro.
 * @returns {{base: number, descuento_pct: number, descuento: number, subtotal: number, iva: number, total: number}}
 *   Importes en euros y porcentaje de descuento en forma decimal (0, 0.1, 0.15 o 0.3).
 * @throws {Error} Si el plan o el periodo no son válidos, si `usuarios` no es un número entero positivo (un texto, un decimal o un
 *   booleano no lo son) o si es menor que el mínimo del plan.
 *
 * @example
 * calcularFacturaCopilot("Team", 25);
 * // { base: 725, descuento_pct: 0.1, descuento: 72.5, subtotal: 652.5, iva: 137.03, total: 789.53 }
 */
function calcularFacturaCopilot(plan, usuarios, periodo = "mensual", educativo = false) {
  if (!Object.prototype.hasOwnProperty.call(PLANES, plan)) throw new Error("Plan desconocido: " + JSON.stringify(plan));
  if (periodo !== "mensual" && periodo !== "anual") throw new Error("Periodo desconocido: " + JSON.stringify(periodo));
  if (typeof usuarios !== "number" || !Number.isInteger(usuarios) || usuarios < 1) throw new Error("usuarios debe ser un entero positivo");
  const { mensual, anual, minimo } = PLANES[plan];
  if (usuarios < minimo) throw new Error("El plan " + plan + " requiere al menos " + minimo + " usuarios");

  let base, volumen;
  if (periodo === "mensual") {
    base = mensual * usuarios * 100;
    volumen = usuarios >= 100 ? 15 : usuarios >= 20 ? 10 : 0;
  } else {
    base = anual * usuarios * 12 * 100;
    volumen = 0;
  }
  const pct = Math.max(volumen, educativo === true ? 30 : 0);

  const descuento = porcentaje(base, pct);
  const subtotal = base - descuento;
  const iva = porcentaje(subtotal, 21);
  const total = subtotal + iva;
  return {
    base: base / 100, descuento_pct: pct / 100, descuento: descuento / 100,
    subtotal: subtotal / 100, iva: iva / 100, total: total / 100,
  };
}

if (typeof module !== "undefined" && module.exports) module.exports = { calcularFacturaCopilot };
```

</details>

<details>
<summary>Especificación de ejemplo para el agente (plan Business)</summary>

```markdown
# Especificación: añadir el plan Business a la facturación de Altanoria Copilot

## Objetivo y contexto
Altanoria lanza un plan intermedio, **Business**, entre Team y Enterprise. El equipo comercial necesita que el formulario web de la factura de Copilot lo calcule igual que los demás planes.

## Alcance y exclusiones
- Entra: la función `calcularFacturaCopilot` de `facturacion.js` y sus pruebas.
- No se toca: la forma del resultado (las seis claves), los planes Starter, Team y Enterprise, ni el resto del formulario.

## Criterios de aceptación
- `("Business", 20, "mensual", false)` → base 780,00; descuento_pct 0,10; descuento 78,00; subtotal 702,00; iva 147,42; total 849,42.
- `("Business", 20, "anual", false)` → base 7.920,00; sin descuento; subtotal 7.920,00; iva 1.663,20; total 9.583,20.
- `("Business", 20, "mensual", true)` → descuento_pct 0,30.
- Los 106 casos de `datos/casos_aceptacion.csv` siguen pasando sin modificarlos.

## Restricciones técnicas
JavaScript ES2020, sin bibliotecas ni módulos, importes en céntimos con enteros y la misma firma `calcularFacturaCopilot(plan, usuarios, periodo = "mensual", educativo = false)`.

## Casos límite y errores
- `("Business", 19, "mensual", false)` lanza un `Error` (mínimo 20 usuarios).
- Usuarios en texto, booleano o decimal lanzan un `Error`, como en los otros planes.
- `("business", 20, "mensual", false)` lanza un `Error` (el plan se compara tal cual).

## Definición de «hecho»
- `node comprobar.js facturacion.js` da 106/106 y `node comprobar.js facturacion.js --malla` pasa toda la malla.
- Los casos nuevos de Business están en `datos/casos_aceptacion.csv`.
- La documentación de la función menciona el plan Business y su mínimo.

## Plan y tareas (cada una con su comprobación)
1. Añadir Business a la tabla de planes (39 €/mes, 33 €/mes en anual, mínimo 20). Comprobación: los criterios de aceptación de base.
2. Añadir los casos de aceptación de Business. Comprobación: fallan antes del cambio y pasan después.
3. Actualizar la documentación. Comprobación: el ejemplo de la documentación se ejecuta y da el resultado escrito.
```

</details>

<details>
<summary>Puntuación de las tres especificaciones de ejemplo</summary>

| Punto de la lista | A | B | C |
|---|---|---|---|
| Qué se quiere conseguir y para quién | no | sí (el equipo comercial y el formulario) | sí |
| Qué entra y qué no se toca | no | no (solo dice qué entra) | sí |
| Criterios con cifras que se pueden convertir en prueba | no | sí (un criterio) | sí (tres criterios) |
| Lenguaje, dependencias y API pública | no | no | sí |
| Valores extremos y entradas inválidas | no | no | no (faltan el mínimo de 20 usuarios, los textos y los decimales) |
| Cuándo está «hecho» | no | no | no (no dice que las pruebas deban pasar sin modificarlas) |
| Puntos que cumple | 0 de 6 | 2 de 6 | 4 de 6 |

La A es una petición de chat, no una especificación. La B tiene un objetivo y un criterio, pero deja al agente decidir el lenguaje, el mínimo de usuarios y qué hacer con las entradas inválidas. La C es casi completa: le faltan los casos límite y la definición de «hecho».

</details>

<details>
<summary>Lista de seis puntos para revisar la especificación</summary>

1. Dice qué se quiere conseguir y para quién.
2. Dice qué entra en el trabajo y qué no se toca.
3. Los criterios de aceptación llevan cifras y se pueden convertir en una prueba.
4. Fija el lenguaje, las dependencias permitidas y lo que no cambia (la API pública).
5. Dice qué ocurre con los valores extremos y las entradas inválidas.
6. Define cuándo está «hecho»: qué pruebas deben pasar sin modificarlas y qué documentación se actualiza.

</details>

### Resultados medidos con un modelo real

Medición de noviembre de 2026 con Gemma 4 (8 B, en local con Ollama), temperatura 0,7, Node.js 24 y 10 traducciones por prompt. Cada traducción se comprobó con los 106 casos de aceptación y con la malla de 2.188 entradas.

| | Prompt v1 (básico) | Prompt v2 (con contrato) |
|---|---|---|
| Traducciones que se cargan | 9 de 10 | 10 de 10 |
| Pasan los 106 casos | 8 | 8 |
| Pasan la malla entera | 0 | 0 |
| Pasan los 106 casos y fallan en la malla | 8 (12 entradas cada una) | 8 (12 entradas cada una) |
| Media de casos de aceptación que pasan | 90,6 de 106 | 91,6 de 106 |
| Incluyen ejemplos de uso con `console.log` | 9 de 10 | 0 de 10 |

- Las dos versiones fallan en las mismas 12 entradas: todas las traducciones que pasan los 106 casos redondean con `Math.round(x * 100) / 100`, aunque el prompt v2 pedía trabajar en céntimos enteros. El fallo solo aparece en la malla (por ejemplo, Team con 35 usuarios en facturación mensual: IVA 191,83 en lugar de 191,84).
- Lo que sí cambia el contrato es la forma: con v2 ninguna traducción trae ejemplos de uso ni bibliotecas, y todas se cargan. Con v1 una usa `Decimal` sin definirlo y no se carga.
- Las traducciones que no pasan los 106 casos tienen errores de programación del modelo: una variable sin definir o con una errata (`periodoo`), un `NaN` en la facturación anual y, en una ejecución con v2, importes en céntimos (1200 en lugar de 12).
- Corrección con evidencia (una entrada que falla, el valor esperado y el obtenido, a las 8 traducciones de v2 que fallaban en la malla): una sola queda equivalente (106 casos y malla entera); cuatro devuelven lo mismo que antes; dos pasan a fallar casos que antes pasaban (104 y 105 de los 106); y en una la respuesta no trae código. Por eso, tras cada corrección se vuelve a comprobar todo.
- Documentación (observación exploratoria, tres documentaciones JSDoc de la traducción de referencia con un prompt que pedía no documentar nada que el código no haga): son en general fieles, pero dos de las tres llaman «adicional» al descuento educativo, cuando el código aplica el mayor de los dos descuentos y no los suma; una afirma que la base es «divisible por 100» y otra que los precios del plan están en céntimos (están en euros). Por eso cada afirmación se comprueba ejecutando la función.
- Estas cifras dependen del modelo y de la temperatura: sirven para saber qué esperar, no como valor que deba reproducirse.

</details>

### Para seguir

- Traducir la función a otro lenguaje (Go, Java o TypeScript) y generar su propia malla ejecutando el original.
- Pedir las pruebas de la traducción con Jest y comprobar que fallan con la traducción ingenua.
- Escribir el fichero de instrucciones del proyecto (`AGENTS.md`) con el comando de comprobación y las convenciones de `facturacion.js`.

---

[← Laboratorios](../README.md) · [Módulo 11](../../modulos/11-desarrollo-de-software/README.md) · [← 11B](../11B/README.md) · [12A →](../12A/README.md)
