[← Laboratorios](../README.md) · [Guía de los laboratorios](README.md)

# Antes de empezar

Lectura previa para quien hace su primer laboratorio y no ha trabajado antes con un asistente de IA ni con hojas de cálculo. Lleva unos 30 minutos entre leer y hacer el calentamiento del final. **No hace falta saber programar ni instalar nada**, y no cuenta para las 30 horas del curso: es una ayuda opcional que conviene hacer una sola vez.

Si ya usas un chat de IA y una hoja de cálculo con soltura, puedes saltártela.

## 1. El asistente es un chat

Un asistente de IA (ChatGPT, Claude, Gemini, Copilot u otros) funciona como una conversación: escribes un mensaje y contesta. Para los laboratorios sirve cualquiera que te deje pegar texto largo.

Lo más importante es esto: **el asistente tiene en cuenta todo lo que se ha dicho en la conversación abierta**. Por eso, en los laboratorios, cada vez que se prueba un prompt se pide **abrir una conversación nueva**: si se reutiliza la anterior, el asistente arrastra lo que ya sabe y los resultados dejan de ser comparables. Cuando un paso dice «conversación nueva», significa pulsar el botón de nuevo chat (suele estar arriba a la izquierda).

Esa memoria dura lo que dura la conversación y tiene un límite de tamaño (la «ventana de contexto», que verás en el módulo 1). Además, algunas plataformas ofrecen una **memoria persistente** (preferencias guardadas, proyectos o instrucciones compartidas entre conversaciones) que se aplica aunque abras un chat nuevo. Para los laboratorios conviene **desactivarla**, o usar un chat sin ella, para que los resultados sean comparables; si no puedes, anótalo y recuerda que el asistente puede estar usando datos de antes.

## 2. Trabajar con textos

- **Copiar y pegar.** Casi todo el trabajo consiste en copiar un texto del laboratorio y pegarlo en el chat. Si el laboratorio da un prompt con huecos entre llaves, como `{mensaje}`, se sustituye el hueco, llaves incluidas, por el contenido que se indica.
- **Adjuntar documentos.** Algunos laboratorios piden dar al asistente un documento de Altanoria. Si el chat permite adjuntar ficheros, se adjunta; si no, se abre el fichero, se copia su contenido y se pega en el mensaje.
- **Guardar lo que sale.** Las respuestas largas del asistente y los textos que se escriben (contratos, informes, prompts) se guardan en un documento de texto aparte (Word, Google Docs, Notas o el Bloc de notas). La hoja de cálculo es para anotar datos, no para guardar textos.
- **Una respuesta bien presentada puede estar mal.** Los laboratorios insisten en comprobar lo que dice el asistente contra una fuente o una solución, y no fiarse del tono seguro.

## 3. La hoja de cálculo

Cada laboratorio trae una hoja de resultados (`hoja_de_resultados.xlsx`) que se abre con Excel, con Google Sheets o con LibreOffice Calc. Se repiten cuatro cosas:

| En la hoja | Qué significa | Qué hacer |
|---|---|---|
| Celdas amarillas | Son las tuyas | Escribir o elegir ahí; el resto no se toca |
| Lista desplegable | La celda amarilla muestra una flecha al pulsarla | Elegir una opción de la lista en lugar de escribir |
| Columnas ocultas | Esconden la respuesta correcta hasta que termines | Después de anotar la tuya, pulsar el pequeño «+» que aparece sobre las letras de las columnas para mostrarlas |
| Celdas con fórmula | Se rellenan solas (totales, aciertos, porcentajes) | No editarlas: se recalculan al anotar tus datos |

Cada hoja tiene además una pestaña **«Cómo se usa»** que explica qué recoge cada pestaña. Si una celda con fórmula muestra un error o aparece vacía, normalmente es que falta una celda amarilla por rellenar.

## 4. Cómo se lee un laboratorio

Cada laboratorio es un solo documento y siempre tiene la misma forma:

- **De un vistazo.** Una tabla al principio: qué vas a hacer, qué hace falta, cuánto dura y qué hacer si algo no sale.
- **Partes y pasos.** Los pasos van numerados y cada uno indica su duración. En algunos laboratorios los pasos se agrupan en partes (A, B, C…), que sirven de puntos de parada.
- **Comprobación.** Cada paso termina con una frase que dice qué deberías ver. Si no lo ves, repite el paso antes de seguir.
- **Si te has atascado.** En varios pasos hay un material de rescate (una salida de ejemplo, un fichero) para poder continuar. Usarlo después de haberlo intentado.
- **Camino con chat y camino con código.** Todos los laboratorios se pueden hacer solo con un chat y la hoja. Los bloques plegados «Con código» son una ampliación para quien programa: se pueden saltar sin perder el hilo.
- **Conclusiones y solución.** Al final hay una referencia de lo que suele ocurrir y la solución. Conviene abrirla solo después de haberlo intentado.

Los laboratorios no se evalúan y no hay nada que entregar.

## 5. Datos ficticios y buenas costumbres

- Todo el material trabaja con una empresa inventada, Altanoria Software, y con clientes, facturas y documentos sintéticos.
- **No pegues en ningún asistente datos reales de personas ni de tu empresa**: nombres, DNI, cuentas bancarias, contraseñas o documentos internos. Es una de las cosas que se aprenden en el módulo 9.
- Los resultados del asistente cambian de una vez a otra y de un modelo a otro. Que tu resultado no sea idéntico al de la solución no significa que lo hayas hecho mal.

## 6. Calentamiento de 10 minutos

Con la hoja [`antes_de_empezar.xlsx`](antes_de_empezar.xlsx) practicas todo lo anterior:

1. Abre la hoja. En la pestaña «Calentamiento» hay tres textos de Altanoria.
2. Abre una **conversación nueva** en tu asistente. Copia el primer texto y pregunta: «¿Cuántas palabras tiene este texto?».
3. Anota en la celda amarilla de «Palabras que dice el asistente» el número que contesta y elige en la lista desplegable si sonaba seguro.
4. Repite con los otros dos textos, cada uno en una conversación nueva.
5. Pulsa el «+» que hay sobre la columna E para mostrar las palabras reales y comprueba la columna «Diferencia» y los dos totales, que se calculan solos.

Comprobación: la hoja muestra cuántos textos has acertado y la diferencia media. Es normal que algún recuento falle aunque el asistente suene seguro: por eso en los laboratorios se compara siempre con una respuesta conocida.

## 7. ¿Y el código?

No lo necesitas para aprender. El camino con código sirve para repetir los experimentos de forma automática y con más casos. Si algún día quieres probarlo, la [guía de los laboratorios](README.md) explica cómo configurarlo, y [si algo falla](si-algo-falla.md) recoge los problemas habituales.
