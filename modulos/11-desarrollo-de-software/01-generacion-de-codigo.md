[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-analisis-y-depuracion.md)

# 1 · Generación de código

*Módulo 11: Prompt Engineering aplicado al desarrollo de software*

## 1.1 El LLM como asistente de programación

**Capacidades**

- Propone código y explicaciones en lenguaje natural
- Interpreta mensajes de error y stack traces
- Genera pruebas automáticas y documentación

**Límites críticos**

- Puede inventar APIs que no existen o son incorrectas
- El código generado debe ejecutarse y revisarse antes de integrar
- No garantiza ausencia de bugs ni errores lógicos sutiles
- Las pruebas generadas no sustituyen al análisis humano

El LLM es un acelerador, no un oráculo. Verifica siempre.

**Explicación**

El modelo ayuda a programar con tres capacidades: proponer código y explicaciones en lenguaje natural, interpretar mensajes de error y **trazas** de pila y generar pruebas y documentación. Sus límites críticos son que puede inventar APIs inexistentes o incorrectas, que el código debe ejecutarse y revisarse antes de integrarlo, que no garantiza la ausencia de errores lógicos sutiles y que las pruebas generadas no sustituyen el análisis humano.

Es un acelerador, no un oráculo: hacia donde la persona dirige y con su comprobación. Puede imaginarse como un compañero junior muy rápido y muy seguro de sí mismo que no ha ejecutado nada de lo que entrega. El primer límite es característico del código: una llamada con nombre verosímil y parámetros apropiados a una función que no existe en la versión usada, la versión en código de la cita inventada. Y si el mismo modelo escribe código y pruebas, pueden compartir los mismos errores de comprensión.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 11A · Especificar y generar una función con pruebas](../../laboratorios/11A/README.md)
<!-- /labs-seccion -->

---

## 1.2 Especificación funcional: describir el comportamiento requerido

Antes de pedir código a un LLM, es imprescindible articular con precisión qué debe hacer el sistema. Una especificación incompleta produce código impredecible. La siguiente plantilla cubre todos los elementos necesarios:

1. **Objetivo**: ¿Qué problema resuelve la función o componente?
2. **Entradas y salidas**: Tipos, formatos, rangos esperados y estructura del resultado
3. **Reglas de negocio**: Lógica condicional, validaciones y flujos alternativos
4. **Casos límite**: Nulos, vacíos, valores extremos y entradas malformadas
5. **Restricciones**: Rendimiento máximo aceptable, restricciones de seguridad y privacidad
6. **Criterios de aceptación**: Condiciones verificables que determinan que la implementación es correcta

**Explicación**

Antes de pedir código hay que articular con precisión qué debe hacer el sistema, porque una especificación incompleta produce código impredecible. La plantilla tiene seis elementos: objetivo, entradas y salidas (tipos, formatos, rangos y estructura del resultado), reglas de negocio (lógica condicional, validaciones y flujos alternativos), **casos límite** (nulos, vacíos, valores extremos y entradas malformadas), restricciones (rendimiento, seguridad y privacidad) y **criterios de aceptación** verificables.

Los criterios de aceptación hacen comprobable la petición y se convierten después en pruebas: una buena especificación es la mitad de los tests escritos de antemano. Los casos límite se omiten con frecuencia y previenen muchos errores: si el prompt no dice qué ocurre con una lista vacía o un valor nulo, el modelo supone el comportamiento más sencillo y el código fallará justo ahí.

---

## 1.3 Contexto técnico: aportar información de entorno

El LLM genera código más preciso y compatible cuando conoce el entorno exacto de ejecución. Omitir versiones o convenciones produce incompatibilidades difíciles de detectar. Incluye siempre la siguiente ficha técnica en el prompt (las versiones de los ejemplos son orientativas):

- **Lenguaje y versión**: Ej: Python 3.11, TypeScript 5.2, Java 21 LTS
- **Framework y librerías**: Ej: FastAPI 0.110, React 18, Spring Boot 3.2
- **Sistema operativo**: Relevante cuando hay rutas, permisos o llamadas al sistema
- **Convenciones del proyecto**: Estilo de código, nombrado, estructura de carpetas
- **Dependencias permitidas**: Lista blanca de paquetes aprobados por el equipo
- **Estructura existente**: Módulos relevantes que interactuarán con el nuevo código

**Explicación**

El modelo genera código más preciso y compatible cuando conoce el entorno exacto de ejecución; omitir versiones o convenciones produce incompatibilidades difíciles de detectar. La ficha técnica incluye lenguaje y versión (Python 3.11, TypeScript 5.2, Java 21), framework y librerías, sistema operativo cuando importa, convenciones del proyecto (estilo, nombrado, estructura), dependencias permitidas (lista blanca) y estructura existente con la que interactuará el código nuevo. Las versiones de los ejemplos son orientativas.

Un error típico es que el modelo use una API de una versión distinta de la utilizada: el código funciona en el ejemplo y falla en el proyecto, porque un modelo entrenado con material de varias épocas mezcla sintaxis antigua y moderna. La lista de dependencias evita que introduzca librerías no aprobadas, y la ficha puede reutilizarse en cada prompt o en un archivo de instrucciones del proyecto.

---

## 1.4 Generación de funciones: solicitar código acotado

Pedir funciones concretas y bien delimitadas produce resultados más útiles que solicitudes amplias. Cuanto más precisa es la firma y el comportamiento esperado, menos iteraciones se necesitan.

- **1. Firma y propósito**: Nombre, parámetros, tipo de retorno y descripción en una línea
- **Errores esperados**: Tipos de excepción que debe lanzar y en qué condiciones
- **2. Tipos y comportamiento**: Especificar si acepta nulls, si muta el estado, si es pura
- **Ejemplo de uso**: Una llamada ilustrativa con entrada y salida esperada
- **3. Validación de entradas**: Qué debe rechazar y cómo (excepción, código de error, None)
- **Evitar alcance excesivo**: No pedir la función y toda su infraestructura en un solo prompt

> Ejemplo ilustrativo: «Implementa en Python 3.11 la función parse\_date(raw: str) → date que acepta formatos ISO 8601 y DD/MM/YYYY. Lanza ValueError si el formato es inválido. Sin dependencias externas.»

**Explicación**

Pedir funciones concretas y bien delimitadas da mejores resultados que solicitudes amplias. La petición incluye firma y propósito, tipos y comportamiento (si acepta nulos, si muta estado, si es pura), validación de entradas (qué rechaza y cómo), errores esperados, un ejemplo de uso y evita el alcance excesivo, sin pedir la función y toda su infraestructura de golpe.

El ejemplo («implementa en Python 3.11 la función parse_date que acepta ISO 8601 y DD/MM/YYYY, lanza ValueError si el formato es inválido y sin dependencias externas») fija en dos líneas lenguaje, firma, formatos, error y restricción de dependencias. Las piezas acotadas reducen la superficie de error y facilitan la verificación. El ejemplo de uso aclara el comportamiento y, una vez generado el código, se convierte en la primera prueba.

---

## 1.5 Generación de módulos: escalar a componentes

Cuando el alcance supera una función, el prompt debe describir la responsabilidad del módulo completo, sus interfaces y la estructura de archivos esperada. La responsabilidad única es la guía de diseño.

- **Responsabilidad única**: Cada módulo hace una sola cosa bien. Especificarlo evita que el LLM genere clases con lógica mezclada.
- **Interfaces y dependencias**: Declarar qué consume el módulo y qué expone: métodos públicos, tipos de entrada/salida.
- **Estructura de archivos**: Indicar la estructura de directorios esperada para que el código encaje en el proyecto.
- **Manejo de errores**: Definir la estrategia global del módulo: excepciones tipadas, logging, propagación.
- **Separar lógica y configuración**: Pedir que los valores configurables queden fuera de la lógica de negocio.
- **Revisar integración**: Verificar manualmente que las interfaces generadas encajan con los módulos existentes.

**Explicación**

Cuando el alcance supera una función, el prompt debe describir la responsabilidad del módulo, sus interfaces y la estructura de archivos. Seis puntos: responsabilidad única (cada módulo hace una cosa bien), interfaces y dependencias (qué consume y qué expone), estructura de archivos, estrategia de errores (**excepciones** tipadas, registro, propagación), separación entre lógica y configuración y revisión manual de la integración.

El último es especialmente importante porque el modelo solo conoce lo que se le ha mostrado: puede generar un módulo coherente consigo mismo que llame a una función del proyecto con otro nombre o parámetros. Con responsabilidad única la especificación es corta, se genera con menos ambigüedad y se prueba con menos casos, y definir de antemano la estructura y los errores hace coherentes los módulos generados en sesiones distintas.

---

## 1.6 Restricciones de código: controlar dependencias y convenciones

Las restricciones en el prompt actúan como guardarraíles que evitan que el LLM introduzca librerías no aprobadas, rompa el estilo del proyecto o exponga información sensible. Incluirlas explícitamente es más efectivo que corregirlas después.

- **Versiones compatibles**: Indicar la versión mínima y máxima admitida de cada dependencia clave
- **Librerías permitidas**: Especificar la lista blanca; cualquier paquete fuera de ella debe rechazarse
- **Estilo existente**: Mencionar linter, formatter y convenciones de nombrado del repositorio
- **No incluir secretos**: Prohibir explícitamente hardcoding de tokens, contraseñas o rutas absolutas
- **Rendimiento**: Si hay límites de latencia o memoria, incluirlos como restricción verificable
- **Explicar decisiones**: Pedir al modelo que justifique los patrones y librerías elegidos

**Explicación**

Las restricciones del prompt actúan como guardarraíles y es más eficaz incluirlas que corregir después. Seis restricciones: versiones compatibles (mínima y máxima), librerías permitidas con lista blanca, estilo existente (linter, formateador, nombrado), no incluir secretos ni rutas absolutas, rendimiento como restricción verificable y explicar las decisiones, pidiendo al modelo que justifique patrones y librerías.

Esta última facilita detectar que ha elegido algo inadecuado o inexistente. La prohibición de secretos importa porque los modelos reproducen patrones de código real, donde es habitual encontrar claves de ejemplo en el propio fuente; hay que exigir que los valores sensibles salgan de variables de entorno o de un gestor de secretos. Las restricciones de rendimiento deben ser cuantificables: «que sea eficiente» no aporta nada comprobable.

---

[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-analisis-y-depuracion.md)
