[← Laboratorios](../README.md) · [Módulo 11](../../modulos/11-desarrollo-de-software/README.md) · [← 10C](../10C/README.md) · [11B →](../11B/README.md)

# Laboratorio 11A · Especificar y generar una función con pruebas

Módulo 11 · Prompt Engineering aplicado al desarrollo de software · Duración estimada: 65 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Generar una función de facturación con un flujo guiado por pruebas y comprobar el resultado con casos que el asistente no ha visto. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. La pestaña «Guía» de la hoja de cálculo indica qué pestaña usar en cada paso. Antes de los pasos hay un ejemplo resuelto con otro caso (unos cinco minutos de lectura). |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Entender la especificación y resolver a mano (6 min)
- Paso 2 · Pedir primero las pruebas (8 min)
- Paso 3 · Revisar las pruebas (12 min)
- Paso 4 · Pedir la implementación (16 min)
- Paso 5 · Ejecutar y depurar con evidencia (10 min)
- Paso 6 · Validar con los casos de aceptación (5 min)
- Paso 7 · Revisar el código (8 min)

<details>
<summary>Secciones del módulo relacionadas (11)</summary>

- [§1.1 El LLM como asistente de programación](../../modulos/11-desarrollo-de-software/01-generacion-de-codigo.md#11-el-llm-como-asistente-de-programación)
- [§1.2 Especificación funcional: describir el comportamiento requerido](../../modulos/11-desarrollo-de-software/01-generacion-de-codigo.md#12-especificación-funcional-describir-el-comportamiento-requerido)
- [§1.3 Contexto técnico: aportar información de entorno](../../modulos/11-desarrollo-de-software/01-generacion-de-codigo.md#13-contexto-técnico-aportar-información-de-entorno)
- [§1.4 Generación de funciones: solicitar código acotado](../../modulos/11-desarrollo-de-software/01-generacion-de-codigo.md#14-generación-de-funciones-solicitar-código-acotado)
- [§1.6 Restricciones de código: controlar dependencias y convenciones](../../modulos/11-desarrollo-de-software/01-generacion-de-codigo.md#16-restricciones-de-código-controlar-dependencias-y-convenciones)
- [§2.6 Validar correcciones: no aceptar parches sin pruebas](../../modulos/11-desarrollo-de-software/02-analisis-y-depuracion.md#26-validar-correcciones-no-aceptar-parches-sin-pruebas)
- [§3.3 Pruebas unitarias: generar pruebas de comportamiento](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#33-pruebas-unitarias-generar-pruebas-de-comportamiento)
- [§3.4 Casos límite y pruebas negativas: ampliar cobertura](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#34-casos-límite-y-pruebas-negativas-ampliar-cobertura)
- [§3.9 Regla fundamental: no confiar en código sin ejecutar](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#39-regla-fundamental-no-confiar-en-código-sin-ejecutar)
- [§4.2 Prompt de generación de código: integrar requisitos completos](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#42-prompt-de-generación-de-código-integrar-requisitos-completos)
- [§4.7 Anatomía de una buena especificación](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#47-anatomía-de-una-buena-especificación)

</details>

## Justificación del laboratorio

El equipo de Facturación de Altanoria necesita una función fiable que calcule cuánto se factura a un cliente de Copilot según el plan, el número de usuarios, el periodo y los descuentos. Un error aquí no es un detalle: es dinero en una factura. Se usará un asistente de IA para escribirla, pero el equipo es responsable de que sea correcta.

El modelo puede escribir el código en segundos, pero no lo sabe ejecutar mentalmente: una función que «parece correcta» puede tener un redondeo mal hecho en el caso 21 de 106. La forma profesional de trabajar con un asistente es guiarse por pruebas: leer la especificación, resolver a mano varios casos para saber qué se espera, pedir primero las pruebas (y revisarlas, porque también pueden estar mal), pedir después el código, ejecutarlo, corregir aportando evidencia (la prueba que falla, la salida real y la esperada) y, por último, validar con casos de aceptación que el asistente no ha visto.

Para quien no programa hay un camino alternativo con el mismo objetivo pedagógico: comprobar, con seis casos, por qué un cálculo de dinero no se debe confiar a la «aritmética» del modelo y cómo se detectan los fallos con una referencia correcta.

## Objetivos

Generar con ayuda de un modelo una función de negocio (el cálculo de la factura de Altanoria Copilot) siguiendo un flujo guiado por pruebas: leer una especificación, pedir primero casos de prueba, después la implementación, ejecutarla, corregir con la evidencia de los fallos y verificar contra un conjunto independiente de 106 casos de aceptación.

Al terminar el laboratorio se habrá conseguido:

- Traducir una especificación funcional a un prompt de generación de código acotado (contrato, entorno, restricciones).
- Pedir las pruebas antes que el código y usarlas como criterio de aceptación.
- Aportar evidencia (resultados, trazas, casos que fallan) para depurar en lugar de decir «no funciona».
- **No aceptar código sin ejecutarlo** ([§3.9 Regla fundamental: no confiar en código sin ejecutar](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#39-regla-fundamental-no-confiar-en-código-sin-ejecutar)).
- Revisar el código generado con criterios explícitos: corrección, casos límite, tipos, redondeo, legibilidad.

Conceptos que se usan:

- **Especificación ejecutable**. Una especificación clara con ejemplos numéricos es casi una prueba. Cuanto más precisa, mejor el resultado.
- **Desarrollo guiado por pruebas con IA**. Se pide al modelo primero los casos de prueba (que se revisan a mano), luego la implementación, y las pruebas deciden si el código vale.
- **Aritmética monetaria**. Los números en coma flotante producen errores de redondeo en cálculos con dinero; se usa `decimal.Decimal` y reglas de redondeo explícitas (aquí, mitad hacia arriba).
- **Los casos de aceptación son independientes**. El fichero `casos_aceptacion.csv` simula la validación de un tercero: el modelo no lo ha visto y sirve para comprobar si las pruebas propias eran suficientes.

## Recursos necesarios

> Sin acceso a una API: Generar pruebas y código en un chat; `comprobar.py` y las pruebas se ejecutan en local sin API. Véase la [guía para trabajar sin API](../comun/sin-api.md).

- Un asistente de chat (para pedir las pruebas y el código) y, para ejecutarlos, Python 3.9 o superior (solo biblioteca estándar; no hace falta API).
- Ficheros del laboratorio:
  - [`datos/especificacion.md`](datos/especificacion.md): la función `calcular_factura_copilot`, sus reglas y tres ejemplos.
  - [`facturacion.py`](facturacion.py): plantilla vacía donde se pega la implementación.
  - [`comprobar.py`](comprobar.py): ejecuta la función contra los casos de aceptación.
  - [`ejecutor.html`](ejecutor.html): alternativa sin terminal: una página que ejecuta Python en el navegador, con el código y las pruebas pegados, y lanza los mismos casos de aceptación (necesita conexión a internet la primera vez).
  - [`datos/casos_aceptacion.csv`](datos/casos_aceptacion.csv): 96 casos de cálculo y 10 casos de error (106 en total).
  - [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx): hoja de cálculo con los seis casos del camino con chat; compara el total del asistente con el correcto.
- Documento de reglas de negocio: [`catalogo_planes.md`](../comun/empresa/catalogo_planes.md).

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

## Ejemplo resuelto

Lectura previa de unos cinco minutos, fuera de los pasos y de la duración: el mismo método aplicado a un caso pequeño y ajeno al laboratorio (una panadería ficticia, «La Espiga»), para ver el procedimiento completo antes de hacerlo con los datos de Altanoria.

Caso: La Espiga quiere una función que calcule el total de un pedido. Se sigue el método: especificar, pedir primero las pruebas, pedir el código y validar con casos de aceptación calculados a mano.

Paso 1: la especificación y el cálculo a mano. Reglas: la barra cuesta 1,20 € y las magdalenas 0,90 € cada una; con 20 unidades o más hay un 10 % de descuento; se añade un 10 % de IVA; todo se redondea a céntimos, con la mitad hacia arriba. La función se llama `total_pedido(producto, cantidad)` y devuelve base, descuento, IVA y total.

Casos de aceptación: se calculan a mano antes de pedir nada, incluyendo los valores límite del descuento (19, 20 y 21 unidades).

| Producto | Cantidad | Base | Descuento | IVA | Total |
|---|---|---|---|---|---|
| Barra | 5 | 6,00 | 0,00 | 0,60 | 6,60 |
| Magdalenas | 20 | 18,00 | 1,80 | 1,62 | 17,82 |
| Barra | 19 | 22,80 | 0,00 | 2,28 | 25,08 |
| Barra | 21 | 25,20 | 2,52 | 2,27 | 24,95 |

El último caso lo prueba todo: el IVA de 22,68 € es 2,268 € y se redondea a 2,27 €.

Pasos 2 y 3: pedir primero las pruebas y revisarlas. El asistente propone pruebas; se comprueba que cubren los límites (19, 20 y 21) y los errores (un producto que no existe). Falta una para cantidad cero, y se pide.

Pasos 4 y 5: la implementación y la ejecución. Se pide el código con la especificación y se ejecutan las pruebas. Falla la de 21 unidades por un redondeo: la evidencia dice «esperado 24,95, obtenido 24,94». Se pasa al asistente la prueba que falla, el resultado esperado y el obtenido, y corrige el redondeo.

Paso 6: validar con los casos de aceptación. En un chat sin ejecutar código, se pide al asistente el total de cada caso paso a paso y se compara con el cálculo a mano.

| Caso | Total correcto | Total del asistente | ¿Acierta? | Diferencia |
|---|---|---|---|---|
| Barra, 5 | 6,60 | 6,60 | sí | 0,00 |
| Magdalenas, 20 | 17,82 | 17,82 | sí | 0,00 |
| Barra, 19 | 25,08 | 25,08 | sí | 0,00 |
| Barra, 21 | 24,95 | 24,94 | no | −0,01 |

Resultado: 3 de 4 casos acertados y una diferencia máxima de un céntimo. Por eso se especifican los casos límite y se calculan fuera del asistente: él mismo explica el cálculo con seguridad y falla el redondeo.

Paso 7: revisar el código. Se comprueba, con una lista, que usa solo la especificación, que no inventa productos y que redondea cada importe. Se anota que el código no valida que la cantidad sea un número entero, y se pide.

Qué se espera ver en tu laboratorio: la especificación de facturación de Altanoria, sus casos de aceptación calculados a mano y la tabla de seis casos con el total del asistente.

## Pasos de ejecución

Los pasos se hacen en orden. Camino con código: se ejecutan pruebas y casos de aceptación en el propio ordenador (no se necesita API, solo Python 3.9 o superior y un chat para generar el código). Quien no tenga Python o no quiera usar la terminal puede hacer lo mismo en la página [`ejecutor.html`](ejecutor.html), que ejecuta Python en el navegador (necesita conexión la primera vez). Camino con chat: se usa una muestra de seis casos y el chat, sin ejecutar nada.

### Paso 1 · Entender la especificación y resolver a mano (6 minutos)
1. Abrir [`datos/especificacion.md`](datos/especificacion.md): la función `calcular_factura_copilot`, sus reglas (descuentos por volumen y educativo, IVA, redondeo) y tres ejemplos resueltos.
2. Resolver a mano, con calculadora, los tres ejemplos de la especificación y comprobar que coinciden. Después calcular un cuarto caso propio: plan Enterprise, 120 usuarios, facturación mensual, sin descuento educativo. Anotar los pasos (base, descuento, subtotal, IVA, total).

Comprobación: los tres ejemplos están resueltos a mano y coinciden con la especificación.

### Paso 2 · Pedir primero las pruebas (8 minutos)
Camino con chat: elegir dos casos de facturación (el cuarto caso propio del Paso 1 y otro cualquiera) y anotar, antes de ver ningún cálculo del asistente, el total que se espera de cada uno; se compararán en el Paso 3.

<details>
<summary>Con código: pedir las pruebas al asistente y guardarlas</summary>

Abrir una conversación nueva en el asistente y pedir solo las pruebas, no la implementación, con este prompt (se pega la especificación completa donde se indica):

```text
Escribe pruebas con unittest (Python 3.9) para esta función. NO escribas la implementación. Cubre cada plan y periodo, valores límite (Team: 4 y 5 usuarios; 19, 20 y 21; 99, 100 y 101), descuento educativo con y sin volumen, anual sin descuento por volumen, errores ValueError y redondeo mitad hacia arriba. Calcula a mano cada resultado esperado.

<especificacion>
{pegar datos/especificacion.md}
</especificacion>
```

Guardar las pruebas generadas en un fichero llamado `test_facturacion.py` dentro de la carpeta del laboratorio.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: hay un fichero de pruebas guardado (camino con código).

### Paso 3 · Revisar las pruebas (12 minutos)
Camino con chat: abrir [`datos/muestra_chat.md`](datos/muestra_chat.md), que contiene seis casos de facturación (las respuestas correctas están al final, plegadas). Abrir una conversación nueva, adjuntar la especificación y pedir, para cada caso, que lo calcule sin escribir código: «Sin escribir código, calcula a mano y paso a paso el total de la factura para: plan Team, 6 usuarios, facturación mensual, descuento educativo: no. Muestra base, descuento, subtotal, IVA y total. Termina con una última línea “TOTAL: <importe en euros>”». Si no se dice «sin escribir código», el asistente suele responder con un programa. Anotar los totales. Anotar el total que da el asistente en la pestaña «Casos» de la hoja [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), que lo compara con el correcto; la pestaña «Resultado» cuenta los aciertos.

<details>
<summary>Con código: revisar a mano las pruebas generadas</summary>

Sin ejecutar todavía, revisar a mano al menos diez casos de las pruebas: ¿el resultado esperado es correcto según la especificación?, ¿hay valores calculados con mal redondeo?, ¿falta algún caso límite? Las pruebas generadas por el modelo también pueden estar equivocadas. Corregir las que lo estén.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: queda anotado qué pruebas (o qué cálculos del asistente) están mal.

### Paso 4 · Pedir la implementación (16 minutos)
Camino con chat: comparar los resultados del asistente del Paso 3 con las respuestas correctas de la muestra (plegadas al final). Contar cuántos de los seis casos acierta el asistente al calcularlos «a mano» y en qué paso falla cuando se equivoca. Con un modelo pequeño es habitual que acierte la mayoría y falle por unos céntimos en alguno (por ejemplo, 663,14 € en lugar de 663,20 €): un error que en una factura no se admite.

<details>
<summary>Con código: pedir la implementación y guardarla</summary>

1. Abrir una conversación nueva y pegar este prompt con la especificación y las pruebas revisadas:

```text
Eres un ingeniero de software. Implementa en Python 3.9 (solo biblioteca estándar, usa decimal.Decimal con ROUND_HALF_UP) el módulo con la función descrita. Devuelve solo el código del módulo en un único bloque.

<especificacion>
{pegar datos/especificacion.md}
</especificacion>
```

2. Copiar el código que devuelve el asistente y pegarlo en el fichero [`facturacion.py`](facturacion.py) (sustituyendo su contenido).

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: hay una implementación guardada (con código), o un recuento de aciertos del cálculo directo (sin código).

### Paso 5 · Ejecutar y depurar con evidencia (10 minutos)
Camino con chat: para dos de los casos en los que el asistente falló, escribir el prompt de corrección con evidencia (entrada, resultado esperado, resultado obtenido y el cálculo del asistente) y comprobar si a la segunda acierta.

<details>
<summary>Con código: ejecutar las pruebas y depurar con evidencia</summary>

1. Abrir una terminal en la carpeta `laboratorios/11A` y ejecutar las pruebas propias con `python -m unittest -v test_facturacion` (`unittest` es la biblioteca de pruebas que trae Python). Sin terminal: abrir [`ejecutor.html`](ejecutor.html) con doble clic, pegar el código de la implementación en el primer cuadro y las pruebas en el segundo, y pulsar «Ejecutar mis pruebas».
2. Si alguna falla, pedir la corrección al asistente aportando la evidencia, no «arréglalo». Este prompt la estructura:

````text
La función no cumple un caso.
Entrada: {plan, usuarios, periodo, educativo}
Resultado esperado: {valores}
Resultado obtenido: {valores}
Código actual:
```python
{pegar el código}
```
Identifica la causa raíz, corrige con el cambio mínimo y no cambies la firma de la función.
````

La causa raíz es el origen del fallo, no el lugar donde se nota.


3. Aplicar el cambio y repetir hasta que pasen.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: las pruebas propias pasan (con código), o los dos casos fallidos se han corregido con evidencia (sin código).

### Paso 6 · Validar con los casos de aceptación (5 minutos)
Camino con chat: concluir por escrito, en tres frases, por qué un cálculo de dinero no se debe confiar a la «aritmética» del modelo y cómo se comprueba con pruebas (explicación, sin ejecutar nada).

<details>
<summary>Con código: ejecutar el comprobador de casos de aceptación</summary>

Ejecutar el comprobador, que prueba la función con 106 casos que el asistente no ha visto (96 de cálculo y 10 de error). Sin terminal, se hace en [`ejecutor.html`](ejecutor.html): con el código pegado, el botón «Ejecutar los casos de aceptación» da el mismo informe. Con terminal:

En la terminal, en la carpeta `laboratorios/11A`:

```bash
python comprobar.py
```

Informa de los casos que fallan, por línea del CSV, con el valor esperado y el obtenido. Analizar los fallos: ¿qué faltaba en las pruebas propias que sí estaba en los casos de aceptación?

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: queda anotado cuántos casos fallan (con código) o la conclusión escrita (sin código).

### Paso 7 · Revisar el código (8 minutos)
Revisar el código final con esta lista: tipos de entrada validados, un booleano no se acepta como número, `Decimal` en todo el cálculo, redondeo después de cada paso, mensajes de error útiles, constantes en un solo sitio y funciones cortas. Anotar tres mejoras posibles. Quien no programa puede pedir al asistente: «Revisa este código con esta lista y señala qué cumple y qué no».

Comprobación: hay tres mejoras anotadas.

## Conclusiones

### Qué se ha conseguido

Se ha trabajado con un asistente como lo haría un equipo de ingeniería: primero una especificación y casos resueltos a mano, después pruebas (revisadas, porque también pueden fallar), después el código y, por último, la validación con casos que el asistente no había visto. Lo habitual es que el asistente escriba una implementación que supera la mayoría de los casos y falle en unos pocos de redondeo o de valores límite, y que los casos de aceptación revelen lo que las pruebas propias no cubrían. La lección es que la responsabilidad de que un cálculo de dinero sea correcto no se delega: se comprueba con evidencia.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué errores había en las pruebas generadas por el modelo?

   <details>
   <summary>Respuesta</summary>

   Suele ser resultados esperados mal calculados (redondeos) y casos que repiten el mismo camino.

   </details>

2. ¿Qué casos de aceptación detectaron fallos que las pruebas propias no cubrían?

   <details>
   <summary>Respuesta</summary>

   Los límites de volumen, el máximo de descuentos y los redondeos de medio céntimo.

   </details>

3. ¿Por qué no se recomienda usar `float` para el dinero?

   <details>
   <summary>Respuesta</summary>

   Porque los números binarios no representan exactamente muchas fracciones decimales; se acumulan errores de redondeo.

   </details>

4. ¿Qué parte de la especificación era ambigua? ¿Cómo se resolvió?

   <details>
   <summary>Respuesta</summary>

   La especificación original decía «mitad hacia arriba» sin aclarar el orden de redondeo; se fijó (base → descuento → subtotal → IVA → total).

   </details>

5. ¿Qué haría falta para confiar en esta función en producción (revisión, pruebas de propiedades, comparación con la facturación real)?

   <details>
   <summary>Respuesta</summary>

   Revisión por pares, comparación con facturas reales anteriores, pruebas de propiedades, control de versiones de la tabla de precios y registro de cada cálculo.

   </details>

### Autoevaluación

- [ ] Las pruebas se pidieron antes del código.
- [ ] Se revisaron a mano las pruebas generadas por el modelo.
- [ ] El código se ejecutó; no se aceptó por su aspecto.
- [ ] Las correcciones se pidieron con evidencia (caso, esperado, obtenido).
- [ ] Se ejecutó `comprobar.py` y cada fallo que queda tiene su causa anotada (idealmente, termina con cero fallos).
- [ ] El código usa `Decimal` y redondeo explícito.
- [ ] Se analizaron las diferencias entre las pruebas propias y los casos de aceptación.

### Errores típicos

- Pedir código y pruebas a la vez y confiar en las pruebas del modelo.
- No ejecutar nada.
- Pedir “arregla el fallo” sin enseñar el caso.
- Aceptar un redondeo distinto “porque da casi lo mismo”.
- No guardar los casos que fallaron como regresión.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Cálculo a mano del cuarto caso

Enterprise, 120 usuarios, mensual, sin educativo:
- base = 59 × 120 = 7.080,00
- descuento por volumen: 120 ≥ 100 → 15 % = 1.062,00
- subtotal = 6.018,00
- IVA = 6.018,00 × 0,21 = 1.263,78
- total = 7.281,78

### Prompt de pruebas (ejemplo)

```text
Eres un ingeniero de software con experiencia en pruebas. Escribe pruebas con unittest (Python 3.9) para la función calcular_factura_copilot descrita abajo. NO escribas la implementación.
Cubre: cada plan y periodo; valores límite (Team: 4 y 5 usuarios; 19, 20 y 21; 99, 100 y 101); descuento educativo con y sin volumen (se aplica el mayor); anual sin descuento por volumen; errores ValueError (plan, periodo, usuarios no entero, booleano, menor que el mínimo); redondeo mitad hacia arriba.
Para cada prueba calcula el resultado esperado a mano a partir de la especificación y escribe en un comentario el cálculo.
<especificacion>
...pegar datos/especificacion.md...
</especificacion>
```

### Implementación de referencia

```python
from decimal import Decimal, ROUND_HALF_UP

PLANES = {  # plan: (precio mensual, precio anual por mes, mínimo de usuarios)
    "Starter": (Decimal("12"), Decimal("10"), 1),
    "Team": (Decimal("29"), Decimal("24"), 5),
    "Enterprise": (Decimal("59"), Decimal("49"), 50),
}
IVA = Decimal("0.21")


def _r(x):
    return Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calcular_factura_copilot(plan, usuarios, periodo="mensual", educativo=False):
    if plan not in PLANES:
        raise ValueError(f"Plan desconocido: {plan!r}")
    if periodo not in ("mensual", "anual"):
        raise ValueError(f"Periodo desconocido: {periodo!r}")
    if isinstance(usuarios, bool) or not isinstance(usuarios, int) or usuarios < 1:
        raise ValueError("usuarios debe ser un entero positivo")
    mensual, anual, minimo = PLANES[plan]
    if usuarios < minimo:
        raise ValueError(f"El plan {plan} requiere al menos {minimo} usuarios")

    if periodo == "mensual":
        base = _r(mensual * usuarios)
        volumen = Decimal("0.15") if usuarios >= 100 else Decimal("0.10") if usuarios >= 20 else Decimal("0")
    else:
        base = _r(anual * usuarios * 12)
        volumen = Decimal("0")
    porcentaje = max(volumen, Decimal("0.30") if educativo else Decimal("0"))

    descuento = _r(base * porcentaje)
    subtotal = _r(base - descuento)
    iva = _r(subtotal * IVA)
    total = _r(subtotal + iva)
    return {"base": float(base), "descuento_pct": float(porcentaje), "descuento": float(descuento),
            "subtotal": float(subtotal), "iva": float(iva), "total": float(total)}
```

### Pruebas de referencia

Un conjunto de pruebas `unittest` para guardar como `test_facturacion.py`. Los resultados esperados están calculados a mano a partir de la especificación (el cálculo está en los comentarios), no con la función. Cubren los ejemplos de la especificación, cada plan y periodo, los valores límite (19, 20 y 21; 99, 100 y 101), el descuento educativo con y sin volumen, el anual sin descuento por volumen, el formato de la salida y los errores. Se ejecutan con `python -m unittest -v test_facturacion` (o pegadas en `ejecutor.html`). Con la implementación de referencia pasan todas; con una implementación que redondea mitad al par, acumula los descuentos, aplica el descuento por volumen en el anual o acepta un booleano como número, fallan.

```python
import unittest

from facturacion import calcular_factura_copilot as f


class PruebasFactura(unittest.TestCase):
    """Los resultados esperados están calculados a mano a partir de la especificación (no con la función)."""

    def comprobar(self, entrada, base, pct, descuento, subtotal, iva, total):
        r = f(*entrada)
        esperado = {"base": base, "descuento_pct": pct, "descuento": descuento,
                    "subtotal": subtotal, "iva": iva, "total": total}
        for clave, valor in esperado.items():
            with self.subTest(entrada=entrada, clave=clave):
                self.assertAlmostEqual(r[clave], valor, places=2)

    # --- Ejemplos de la especificación ---
    def test_ejemplos_de_la_especificacion(self):
        self.comprobar(("Team", 10, "mensual", False), 290.00, 0.0, 0.00, 290.00, 60.90, 350.90)
        # 25 × 29 = 725; 10 % = 72,50; subtotal 652,50; IVA 137,025 → 137,03 (mitad hacia arriba)
        self.comprobar(("Team", 25, "mensual", False), 725.00, 0.10, 72.50, 652.50, 137.03, 789.53)
        # 3 × 10 × 12 = 360; 30 % = 108; subtotal 252; IVA 52,92
        self.comprobar(("Starter", 3, "anual", True), 360.00, 0.30, 108.00, 252.00, 52.92, 304.92)

    # --- Cada plan, mensual y anual ---
    def test_starter_mensual(self):
        self.comprobar(("Starter", 1, "mensual", False), 12.00, 0.0, 0.00, 12.00, 2.52, 14.52)

    def test_enterprise_mensual_en_el_minimo(self):
        # 50 × 59 = 2950; 10 % = 295; subtotal 2655; IVA 557,55
        self.comprobar(("Enterprise", 50, "mensual", False), 2950.00, 0.10, 295.00, 2655.00, 557.55, 3212.55)

    def test_anual_se_factura_el_año_completo(self):
        # 24 × 30 × 12 = 8640
        self.comprobar(("Team", 30, "anual", False), 8640.00, 0.0, 0.00, 8640.00, 1814.40, 10454.40)

    # --- Valores límite del descuento por volumen: 19 / 20 / 21 y 99 / 100 / 101 ---
    def test_limite_19_20_21_usuarios(self):
        self.comprobar(("Team", 19, "mensual", False), 551.00, 0.0, 0.00, 551.00, 115.71, 666.71)
        self.comprobar(("Team", 20, "mensual", False), 580.00, 0.10, 58.00, 522.00, 109.62, 631.62)
        # 21 × 29 = 609; 10 % = 60,90; subtotal 548,10; IVA 115,101 → 115,10
        self.comprobar(("Team", 21, "mensual", False), 609.00, 0.10, 60.90, 548.10, 115.10, 663.20)

    def test_limite_99_100_101_usuarios(self):
        self.comprobar(("Team", 99, "mensual", False), 2871.00, 0.10, 287.10, 2583.90, 542.62, 3126.52)
        self.comprobar(("Team", 100, "mensual", False), 2900.00, 0.15, 435.00, 2465.00, 517.65, 2982.65)
        # 101 × 29 = 2929; 15 % = 439,35; subtotal 2489,65; IVA 522,8265 → 522,83
        self.comprobar(("Team", 101, "mensual", False), 2929.00, 0.15, 439.35, 2489.65, 522.83, 3012.48)

    def test_limite_inferior_del_descuento_en_starter(self):
        self.comprobar(("Starter", 19, "mensual", False), 228.00, 0.0, 0.00, 228.00, 47.88, 275.88)
        self.comprobar(("Starter", 20, "mensual", False), 240.00, 0.10, 24.00, 216.00, 45.36, 261.36)

    def test_enterprise_100_usuarios(self):
        self.comprobar(("Enterprise", 100, "mensual", False), 5900.00, 0.15, 885.00, 5015.00, 1053.15, 6068.15)

    # --- Descuento educativo: no se suma al de volumen, se aplica el mayor ---
    def test_educativo_sin_volumen(self):
        self.comprobar(("Team", 10, "mensual", True), 290.00, 0.30, 87.00, 203.00, 42.63, 245.63)

    def test_educativo_con_volumen_se_aplica_el_mayor(self):
        # 10 % de volumen y 30 % educativo: no 40 %, sino 30 %. IVA: 507,50 × 0,21 = 106,575 → 106,58
        self.comprobar(("Team", 25, "mensual", True), 725.00, 0.30, 217.50, 507.50, 106.58, 614.08)
        self.comprobar(("Team", 100, "mensual", True), 2900.00, 0.30, 870.00, 2030.00, 426.30, 2456.30)

    def test_anual_no_tiene_descuento_por_volumen(self):
        # 10 × 25 × 12 = 3000, aunque haya más de 20 usuarios
        self.comprobar(("Starter", 25, "anual", False), 3000.00, 0.0, 0.00, 3000.00, 630.00, 3630.00)
        self.comprobar(("Enterprise", 120, "anual", False), 70560.00, 0.0, 0.00, 70560.00, 14817.60, 85377.60)

    # --- Valores por defecto y formato de la salida ---
    def test_valores_por_defecto(self):
        self.assertEqual(f("Team", 10), f("Team", 10, "mensual", False))

    def test_la_salida_tiene_las_seis_claves_y_son_float(self):
        r = f("Team", 10)
        self.assertEqual(set(r), {"base", "descuento_pct", "descuento", "subtotal", "iva", "total"})
        for valor in r.values():
            self.assertIsInstance(valor, float)

    # --- Errores: siempre ValueError ---
    def test_plan_desconocido(self):
        with self.assertRaises(ValueError):
            f("Premium", 10)

    def test_periodo_desconocido(self):
        with self.assertRaises(ValueError):
            f("Team", 10, "trimestral")

    def test_por_debajo_del_minimo_de_cada_plan(self):
        for plan, usuarios in (("Team", 4), ("Enterprise", 49)):
            with self.subTest(plan=plan, usuarios=usuarios):
                with self.assertRaises(ValueError):
                    f(plan, usuarios)

    def test_usuarios_no_validos(self):
        for usuarios in (0, -1, 5.0, "10", True, None):
            with self.subTest(usuarios=usuarios):
                with self.assertRaises(ValueError):
                    f("Starter", usuarios)


if __name__ == "__main__":
    unittest.main()
```

### Errores habituales en lo que genera el modelo

| Fallo | Explicación | Cómo se detecta |
|---|---|---|
| Usar `float` y `round()` | `round()` usa redondeo al par más cercano y la coma flotante no representa bien los medios céntimos: `round(2.675, 2)` da 2.67 y `round(0.125, 2)` da 0.12, no 2,68 ni 0,13 | Casos con importes que acaban en medio céntimo (diferencias de 0,01 €) |
| Sumar volumen y educativo | La regla es aplicar el mayor, no la suma | Casos Starter 20 usuarios educativo |
| Descuento por volumen en anual | No procede | Casos anuales con ≥ 20 usuarios |
| Aceptar `True` como número de usuarios | En Python, `True` es un `int` | Caso de error con booleano |
| Aceptar `5.0` o `"10"` | Deben rechazarse | Casos de error de tipo |
| Mínimos de usuarios mal aplicados | Enterprise exige 50 | Caso Enterprise 49 |
| Redondear solo el total | La regla redondea cada importe en el orden indicado | Diferencias de un céntimo |
| Pruebas con resultados mal calculados | El modelo «calcula» mentalmente | Revisión manual de las pruebas |

### Qué suelen aportar los casos de aceptación

Las pruebas escritas por el modelo suelen cubrir el camino principal y los errores más obvios, pero muchas veces omiten: los medios céntimos, el máximo entre dos descuentos, los límites 99/100/101 y los errores de tipo. Los casos de aceptación (106) cubren las combinaciones plan × periodo × educativo × tramo de usuarios y diez errores. Si `comprobar.py` falla en algún caso, ese caso debe convertirse en una prueba propia (regresión).

### Revisión de código: mejoras típicas

1. Extraer los precios a constantes o a una estructura de datos.
2. Documentar con un docstring las reglas y la excepción.
3. Separar el cálculo del descuento en una función auxiliar.
4. Añadir pruebas de propiedades.
5. Devolver `Decimal` internamente y convertir a `float` solo en la salida (o devolver `Decimal` si el consumidor lo admite).

### Resultados medidos con un modelo real

> Medición realizada el 24 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada a 16.384 tokens, una sola ejecución por condición y scripts de medición propios (el laboratorio se hace por chat). Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

Con el modelo, usando prompts equivalentes a los de la solución:

- Implementación: con tres intentos (uno con temperatura 0 y dos con 0,5), dos acertaron los 106 casos de aceptación (usaron `Decimal` y `ROUND_HALF_UP`) y el tercero ni siquiera se podía importar: el módulo contenía `from typing import dict`, que no existe. Por eso conviene ejecutar el código antes de confiar en él, aunque el resto parezca correcto.
- Pruebas generadas: 20 pruebas `unittest` sin ningún código de implementación en el fichero. Contra la implementación de referencia, 17 pasaron y 3 fallaron, y en las tres el código era correcto y las pruebas eran las equivocadas: en Enterprise con 50 usuarios mensual y en Team con 99 usuarios no aplicó el 10 % de volumen que corresponde desde 20 usuarios (entendió «menos de 100» como «sin descuento»), y en Team anual calculó 24 × 10 = 240 sin multiplicar por los 12 meses. Es la razón de revisar las pruebas a mano antes de usarlas: el modelo escribe con aplomo cálculos mal hechos en los comentarios.

</details>

### Para seguir

- Pedir pruebas basadas en propiedades (por ejemplo: el total nunca es menor que el subtotal; con `educativo=True` el descuento es al menos del 30 % cuando procede).
- Añadir la función de prorrata de cambio de plan y su especificación.
- Generar la documentación de la función y comprobar que coincide con su comportamiento ([§3.6 Documentación de código: generar documentación fiel](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#36-documentación-de-código-generar-documentación-fiel)).

---

[← Laboratorios](../README.md) · [Módulo 11](../../modulos/11-desarrollo-de-software/README.md) · [← 10C](../10C/README.md) · [11B →](../11B/README.md)
