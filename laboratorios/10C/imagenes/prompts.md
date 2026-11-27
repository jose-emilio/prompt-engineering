# Prompts de las imágenes de referencia

Texto exacto enviado al generador (FLUX.1 [dev], cuantizado Q5_K_S; 24 pasos, guía 1,0, muestreo Euler). Tamaño y semilla de cada imagen entre paréntesis.

## 01 · Prompt vago (v0)

Archivo: `01_prompt_vago.jpg` (1024×576, semilla 7)

```text
Una imagen para la página de lanzamiento de «Revisión de pull requests», la nueva función de Altanoria Copilot.
```

## 02 · Prompt de referencia con las seis capas y exclusiones (v1)

Archivo: `02_prompt_v1.jpg` (1024×576, semilla 7)

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

## 03 · Iteración 1: cambia solo la luz

Archivo: `03_iter_luz.jpg` (1024×576, semilla 7)

```text
Fotografía editorial realista para la página de lanzamiento de «Revisión de pull requests», una función de Altanoria Copilot.

Sujeto y acción: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo, lee con atención una revisión de código en la pantalla de un portátil.
Entorno: una oficina luminosa y sobria, con una planta y una taza sobre la mesa.
Composición: plano medio, ligeramente de lado; Marta ocupa el tercio izquierdo del encuadre y el tercio derecho queda libre para el titular.
Luz y paleta: contraluz de atardecer, dorado y rasante, desde la derecha; azul petróleo, crema y un único acento naranja.
Estilo: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada.
Formato: 16:9.
Restricciones: sin texto legible en las pantallas, sin logotipos ni marcas de terceros y sin otras personas en la imagen.
```

## 04 · Iteración 2: cambia solo la composición

Archivo: `04_iter_composicion.jpg` (1024×576, semilla 7)

```text
Fotografía editorial realista para la página de lanzamiento de «Revisión de pull requests», una función de Altanoria Copilot.

Sujeto y acción: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo, lee con atención una revisión de código en la pantalla de un portátil.
Entorno: una oficina luminosa y sobria, con una planta y una taza sobre la mesa.
Composición: plano de detalle de las manos de Marta sobre el teclado del portátil, con la pantalla desenfocada al fondo.
Luz y paleta: luz natural cálida de ventana, desde la izquierda; azul petróleo, crema y un único acento naranja.
Estilo: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada.
Formato: 16:9.
Restricciones: sin texto legible en las pantallas, sin logotipos ni marcas de terceros y sin otras personas en la imagen.
```

## 05 · Iteración 3: cambia solo el estilo

Archivo: `05_iter_estilo.jpg` (1024×576, semilla 7)

```text
Fotografía editorial realista para la página de lanzamiento de «Revisión de pull requests», una función de Altanoria Copilot.

Sujeto y acción: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo, lee con atención una revisión de código en la pantalla de un portátil.
Entorno: una oficina luminosa y sobria, con una planta y una taza sobre la mesa.
Composición: plano medio, ligeramente de lado; Marta ocupa el tercio izquierdo del encuadre y el tercio derecho queda libre para el titular.
Luz y paleta: luz natural cálida de ventana, desde la izquierda; azul petróleo, crema y un único acento naranja.
Estilo: ilustración vectorial plana, bordes limpios, sin degradados ni texturas.
Formato: 16:9.
Restricciones: sin texto legible en las pantallas, sin logotipos ni marcas de terceros y sin otras personas en la imagen.
```

## 06 · Pieza 1 (16:9) con la guía de estilo

Archivo: `06_pieza1_con_guia.jpg` (1024×576, semilla 7)

```text
Estilo y atributos persistentes: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada. Luz natural cálida de ventana que entra desde la izquierda. Paleta de azul petróleo, crema y un único acento naranja. Personaje recurrente: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo. Ambiente: oficina luminosa y sobria. Sin logotipos ni marcas de terceros visibles y sin texto legible en las pantallas.

Fotografía para la página de lanzamiento de «Revisión de pull requests», función de Altanoria Copilot. Marta lee con atención la pantalla de su portátil. Formato 16:9.
```

## 07 · Pieza 2 (1:1) con la guía de estilo

Archivo: `07_pieza2_con_guia.jpg` (768×768, semilla 7)

```text
Estilo y atributos persistentes: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada. Luz natural cálida de ventana que entra desde la izquierda. Paleta de azul petróleo, crema y un único acento naranja. Personaje recurrente: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo. Ambiente: oficina luminosa y sobria. Sin logotipos ni marcas de terceros visibles y sin texto legible en las pantallas.

Fotografía para una publicación en redes sociales sobre «Revisión de pull requests», función de Altanoria Copilot. Marta, de pie junto a su mesa, sostiene una taza y mira una pantalla grande con comentarios de revisión. Formato 1:1.
```

## 08 · Pieza 3 (9:16) con la guía de estilo

Archivo: `08_pieza3_con_guia.jpg` (576×1024, semilla 7)

```text
Estilo y atributos persistentes: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada. Luz natural cálida de ventana que entra desde la izquierda. Paleta de azul petróleo, crema y un único acento naranja. Personaje recurrente: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo. Ambiente: oficina luminosa y sobria. Sin logotipos ni marcas de terceros visibles y sin texto legible en las pantallas.

Fotografía vertical para una historia sobre «Revisión de pull requests», función de Altanoria Copilot. Marta, sentada ante su mesa, pulsa el botón de aprobar en la pantalla de su portátil. Formato 9:16.
```

## 09 · Pieza 1 (16:9) sin guía de estilo

Archivo: `09_pieza1_sin_guia.jpg` (1024×576, semilla 7)

```text
Fotografía para la página de lanzamiento de «Revisión de pull requests», función de Altanoria Copilot. Una desarrolladora lee con atención la pantalla de su portátil. Formato 16:9.
```

## 10 · Pieza 2 (1:1) sin guía de estilo

Archivo: `10_pieza2_sin_guia.jpg` (768×768, semilla 7)

```text
Fotografía para una publicación en redes sociales sobre «Revisión de pull requests», función de Altanoria Copilot. Una desarrolladora, de pie junto a su mesa, sostiene una taza y mira una pantalla grande con comentarios de revisión. Formato 1:1.
```

## 11 · Pieza 3 (9:16) sin guía de estilo

Archivo: `11_pieza3_sin_guia.jpg` (576×1024, semilla 7)

```text
Fotografía vertical para una historia sobre «Revisión de pull requests», función de Altanoria Copilot. Una desarrolladora, sentada ante su mesa, pulsa el botón de aprobar en la pantalla de su portátil. Formato 9:16.
```

## 12 · Propuesta con un cartel «0 errores», con la guía de estilo

Archivo: `12_cartel_0_errores.jpg` (768×768, semilla 7)

```text
Estilo y atributos persistentes: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada. Luz natural cálida de ventana que entra desde la izquierda. Paleta de azul petróleo, crema y un único acento naranja. Personaje recurrente: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo. Ambiente: oficina luminosa y sobria. Sin logotipos ni marcas de terceros visibles y sin texto legible en las pantallas.

Fotografía para una publicación sobre «Revisión de pull requests»: Marta sonríe ante una pantalla grande que muestra un cartel verde con el texto «0 errores». Formato 1:1.
```

## 13 · La propuesta anterior sin cartel y con objetos genéricos sin marca

Archivo: `13_propuesta_corregida.jpg` (768×768, semilla 7)

```text
Estilo y atributos persistentes: fotografía editorial realista, objetivo de 35 mm, profundidad de campo moderada. Luz natural cálida de ventana que entra desde la izquierda. Paleta de azul petróleo, crema y un único acento naranja. Personaje recurrente: Marta, desarrolladora senior de unos 35 años, de pelo castaño corto, gafas redondas de montura fina y jersey azul petróleo. Ambiente: oficina luminosa y sobria. Sin logotipos ni marcas de terceros visibles y sin texto legible en las pantallas.

Fotografía para una publicación sobre «Revisión de pull requests»: Marta sonríe ante una pantalla grande que muestra tres comentarios de revisión sobre un fragmento de código. La pantalla y el portátil son genéricos, sin marca, y no hay ningún texto escrito en la escena. Formato 1:1.
```

