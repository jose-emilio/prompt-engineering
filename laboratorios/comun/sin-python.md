[← Laboratorios](../README.md) · [Guía de los laboratorios](README.md)

# Hacer los laboratorios sin Python

Los laboratorios están pensados para que cualquier perfil pueda hacerlos, también quien no programa. Los scripts de Python automatizan mediciones, pero todo lo que miden se puede hacer a mano con un chat y una hoja de cálculo. Esta guía explica cómo.

## Qué se necesita

- Un asistente de chat (gratuito o de pago). Los pasos para conseguir un acceso están en la [guía sin API](sin-api.md).
- Un editor de texto cualquiera, con las funciones de «buscar y reemplazar» y de contar palabras.
- Una hoja de cálculo (Excel, Google Sheets o equivalente) para anotar resultados y hacer sumas.
- Nada más: no hay que instalar Python ni abrir una terminal.

## Cómo está preparado cada laboratorio

1. Las plantillas de prompts son las mismas que para el resto del alumnado: se copian tal cual en el chat.
2. Cada laboratorio que usa scripts explica en cada paso, dentro de su `README.md`, el camino con chat (sin código) y, plegada debajo, la alternativa con código.
3. Hojas de cálculo listas para anotar. Todos los laboratorios tienen un fichero `datos/hoja_de_resultados.xlsx` (Excel, Google Sheets o LibreOffice): se rellenan las celdas amarillas y el resto se calcula solo; las respuestas correctas están en columnas agrupadas y ocultas, que se muestran con el botón «+» de la cabecera.
4. Muestras listas para copiar. En 15 laboratorios (03B, 04A, 04B, 06A, 07A, 07B, 08B, 09A, 11A, 11B, 12A, 12C, 13A, 13B y 14), la carpeta `datos/` incluye un fichero `muestra_chat.md` con entre 3 y 30 casos ya formateados para pegarlos en el chat, y con las respuestas correctas plegadas al final. No hace falta abrir ficheros CSV ni JSON.
5. Once laboratorios (01B, 02A, 02B, 03A, 05A, 08A, 10A, 10B, 10C, 11C y 12B) se hacen enteros con un chat, sin ejecutar nada. El 10C trabaja con imágenes de referencia incluidas en el laboratorio y el 11C trae un comprobador que se abre en el navegador (`comprobar.html`), de modo que no hace falta Python. En los otros cuatro (01A, 05B, 06B y 09B) el camino con chat está explicado en los propios pasos, sin muestra aparte.
6. Con esto quedan cubiertos los 30 laboratorios: 15 con muestra de chat, 11 de chat puro y 4 explicados en los pasos.

## Equivalencias con lo que hacen los scripts

| El script… | Sin Python |
|---|---|
| Ejecuta un prompt sobre muchos casos | Pegar de 5 en 5 casos en un chat y pedir la respuesta de cada uno en una lista numerada; usar las muestras de `muestra_chat.md` |
| Calcula la exactitud | Marcar acierto o error en una hoja de cálculo y sumar; exactitud = aciertos ÷ casos. Todos los laboratorios, incluido el proyecto 14, incluyen en su carpeta `datos/` una hoja `hoja_de_resultados.xlsx` con la muestra cargada, que calcula la exactitud y las demás métricas |
| Valida un JSON | Pegarlo en un validador en línea como https://jsonlint.com, o pedir al chat que compruebe que es válido y que tiene todos los campos del esquema |
| Cuenta tokens | Usar un tokenizador interactivo (véase el laboratorio 01A) |
| Cuenta palabras | La función de contar palabras de cualquier editor |
| Detecta datos personales | Pedir al chat que los liste con el prompt del laboratorio 09A y revisar a mano |
| Mide la variabilidad con la temperatura | Repetir la misma petición 10 veces en conversaciones nuevas y contar cuántas respuestas distintas salen (los chats no dejan fijar la temperatura) |
| Ejecuta código generado | Se omite la ejecución: se pide al chat que explique o calcule paso a paso y se compara con el resultado correcto (laboratorios 11A y 11B) |

## Buenas costumbres

- Abrir una conversación nueva para cada prueba, salvo cuando el laboratorio pida una conversación continuada.
- Pegar los casos tal cual, sin corregirlos; las erratas forman parte del ejercicio.
- Anotar en la hoja de cálculo: caso, respuesta del modelo, ¿correcta?, y observaciones. Con esa tabla se hace el análisis.
- No abrir la parte plegada de respuestas hasta haber anotado las propias.
- **No pegar datos personales reales** en ningún chat; los datos de los laboratorios son ficticios.

## Qué se pierde y qué no

Con muestras de 5 a 10 casos las cifras son menos fiables que con 60 o 120, pero las conclusiones cualitativas (qué tipo de error comete el modelo, qué instrucción lo corrige, qué riesgos hay) son las mismas. La parte de programar (completar una función de código o una puerta de validación) queda fuera; en su lugar se razona sobre la regla en lenguaje natural.

Sin Python se **comprende cómo funciona** cada técnica; con Python se aprende además a **implementarla y verificarla de forma automática**. En concreto, esto es lo que el camino con chat no reproduce por completo:

| Laboratorio | Sin Python se hace | Lo que no se reproduce por completo |
|---|---|---|
| 06B | Repetir la petición en conversaciones nuevas | Fijar la temperatura y top-p, que los chats no dejan controlar |
| 11A | Calcular los casos a mano y compararlos con lo que dice el chat | Ejecutar de verdad la función generada |
| 11B | Analizar los defectos y las propuestas de arreglo | Comprobar los parches ejecutando las pruebas |
| 12C | Analizar los resultados con el chat | Ejecutar y depurar el código de análisis |
| 13A | Simular las tres etapas una a una | Ejecutar la cadena automatizada y su registro real |
| 13B | Simular las ramas | Medir el algoritmo de recuperación |
| 14 | Recorrer el sistema con el chat | Ejecutar el sistema completo y medirlo sobre los 45 mensajes |

Todos esos laboratorios se pueden completar y no hay nada que entregar: lo que cambia es qué parte de lo aprendido se comprueba con una ejecución y cuál con razonamiento.
