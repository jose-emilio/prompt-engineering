[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-salidas-estructuradas.md)

# 1 · Formatos de presentación

*Módulo 06: Control del formato de salida y parámetros de generación*

## 1.1 ¿Por qué importa el formato?

- **El formato no es cosmético**: Un formato bien elegido facilita la lectura, la comparación y el procesamiento automático. Es la diferencia entre una respuesta que se puede leer y una que se puede usar.
- **Flujo LLM → salida → consumidor**: El modelo genera texto. Ese texto lo consume alguien o algo: una persona, una aplicación, un pipeline de datos. Cada consumidor tiene expectativas distintas de forma y contenido.

- Legibilidad humana → Markdown, párrafos estructurados
- Procesamiento automático → JSON, CSV, XML
- Configuración → YAML
- Validación separada → estructura ≠ veracidad

Una salida bien formada puede ser semánticamente errónea. Valida estructura *y* contenido por separado.

**Explicación**

El formato no es cosmético: un formato bien elegido facilita la lectura, la comparación y el procesamiento automático, y es la diferencia entre una respuesta que se puede leer y otra que se puede usar. El modelo genera un texto que consume una persona, una aplicación o un proceso de datos, y cada consumidor espera algo distinto: **Markdown** y párrafos para personas, JSON, CSV o XML para procesamiento automático y YAML para configuración.

Una salida bien formada puede ser semánticamente errónea: un campo «país» con el valor «Marte» es un JSON válido y un dato absurdo. Por eso la **validación** de la estructura y la del contenido son procesos distintos y ambos son necesarios. La pregunta previa al prompt es siempre quién o qué leerá la salida.

---

## 1.2 Elegir formato según el consumidor

No existe un formato universal. La elección correcta depende de quién o qué va a consumir la salida. Usa la siguiente matriz como guía de decisión rápida.

| Formato | Mejor para… | Ejemplo de tarea |
|---|---|---|
| Párrafo | Explicaciones y contexto narrativo | Resumen ejecutivo |
| Lista | Pasos de acción o conjuntos discretos | Requisitos de un proyecto |
| Tabla | Comparaciones multidimensionales | Comparar tres proveedores |
| JSON / XML | Integración con sistemas o APIs | Extracción de entidades |
| CSV | Datos tabulares planos para análisis | Inventario de productos |
| YAML | Configuración legible por personas y máquinas | Pipeline de CI/CD |

**Explicación**

No existe un formato universal: la elección depende de quién o qué consumirá la salida. El párrafo sirve para explicaciones y contexto narrativo; la lista, para pasos o conjuntos discretos; la tabla, para comparaciones con varias dimensiones; JSON y XML, para integrar con sistemas o APIs; el CSV, para datos tabulares planos; y el YAML, para configuración legible por personas y máquinas.

La lógica es ajustar la forma del formato a la forma del contenido. Una regla útil es elegir el formato más sencillo que cumpla las necesidades del consumidor: pedir JSON cuando basta una lista añade riesgo sintáctico sin aportar nada, y pedir un párrafo cuando otro sistema debe procesar los datos obliga a un análisis posterior frágil. La compatibilidad debe confirmarse siempre con el sistema consumidor.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 06A · Salida consumible: Markdown, tabla y JSON validado](../../laboratorios/06A/README.md)
<!-- /labs-seccion -->

---

## 1.3 Markdown: estructura legible

**Markdown** es el marcado ligero por excelencia para salidas destinadas a personas. Permite estructurar sin sobrecargar, siempre que se use con moderación y consistencia.

**Elementos clave**

- Encabezados # H1, ## H2 … para jerarquía
- Listas ordenadas y no ordenadas para secuencias o conjuntos
- Tablas para comparaciones concisas
- Bloques de código \`\`\` para fragmentos técnicos
- Énfasis moderado: negrita y cursiva con propósito claro
- Consistencia: mismo estilo en todo el documento

**Ejemplo ilustrativo**

```text
# Informe de riesgos

## Resumen
Tres riesgos críticos.

## Acciones
1. Revisar plazos
2. Asignar responsables
- **Prioridad**: alta
```

**Explicación**

**Markdown** es el marcado ligero por excelencia para salidas destinadas a personas. Sus elementos clave son los encabezados para la jerarquía, las listas ordenadas y no ordenadas, las tablas, los bloques de código para fragmentos técnicos, el énfasis moderado con propósito claro y la consistencia de estilo en todo el documento.

Se lee bien en bruto y renderizado, y por eso es el formato por defecto de muchas interfaces de chat. Su riesgo es el exceso: negritas en cada frase, encabezados de un solo párrafo o listas de un elemento dificultan la lectura. Y la consistencia importa: si se alternan guiones y asteriscos para las listas o se saltan niveles de encabezado, la estructura se debilita. Conviene indicar en el prompt qué niveles de encabezado, qué tipo de lista y si se admite el énfasis.

---

## 1.4 Listas y tablas: elegir la estructura visual correcta

**¿Cuándo usar cada una?**

- Lista → secuencias ordenadas o conjuntos de ítems sin relación entre dimensiones
- Tabla → múltiples atributos comunes a varias entidades (dimensiones cruzadas)
- Evita tablas para contenido narrativo extenso: pierden legibilidad
- Define siempre nombre de columnas, orden de filas y unidades de medida

**Misma información, dos formatos**

```text
Como lista
- Proveedor A: 12.000 €, 3 meses
- Proveedor B: 9.500 €, 5 meses

Como tabla
| Proveedor | Coste    | Plazo   |
|-----------|----------|---------|
| A         | 12.000 € | 3 meses |
| B         | 9.500 €  | 5 meses |
```

Una lista con un solo elemento se lee mejor como una oración. Una tabla con una sola columna es una lista disfrazada.

**Explicación**

Una lista es adecuada para secuencias ordenadas o conjuntos de elementos sin relación entre dimensiones; una tabla, cuando varios atributos son comunes a varias entidades. Hay que evitar tablas para contenido narrativo extenso y definir siempre las columnas, el orden de las filas y las unidades. Una lista de un solo elemento se lee mejor como oración, y una tabla de una sola columna es una lista disfrazada.

Con la tabla se compara de un vistazo; con la lista se sigue un orden. En el prompt se concreta pidiendo el formato y sus parámetros, por ejemplo «una tabla con las columnas Proveedor, Precio mensual en euros y Plazo de entrega en días, ordenada por precio», lo que hace la salida comparable entre ejecuciones.

---

## 1.5 Informes y plantillas: documentos repetibles

Cuando necesitas que el LLM genere un documento con estructura fija (un informe de análisis, una ficha de cliente, un acta de reunión) debes especificar la plantilla en el prompt. La plantilla reduce variabilidad y garantiza completitud.

- **Secciones y orden**: Enumera explícitamente las secciones del documento y el orden en que deben aparecer. El modelo respetará la secuencia indicada.
- **Contenido mínimo por sección**: Indica qué debe contener cada apartado: «*incluye al menos tres hallazgos con evidencia*» evita secciones vacías o genéricas.
- **Audiencia y propósito**: Especifica a quién va dirigido el informe y para qué se usará. Esto condiciona el tono, el nivel de detalle y el vocabulario.
- **Longitud y campos obligatorios**: Establece una extensión aproximada por sección y distingue campos obligatorios de opcionales para controlar la completitud.

**Explicación**

Para generar documentos de estructura fija (informes, fichas, actas) hay que especificar la plantilla en el prompt, lo que reduce la variabilidad y garantiza la completitud. Se indican las secciones y su orden, el contenido mínimo de cada una («incluye al menos tres hallazgos con evidencia»), la audiencia y el propósito, y la longitud y los **campos obligatorios**.

La ventaja principal es la repetibilidad: un acta generada con la misma plantilla tendrá siempre las mismas secciones en el mismo orden, lo que facilita compararlas, archivarlas y buscar información. Además protege de omisiones, porque si un dato no existe, la sección puede contener «No consta», que informa más que una sección ausente.

---

## 1.6 Formato y criterios de aceptación

Hacer verificable la salida significa definir de antemano qué condiciones debe cumplir para ser aceptada. Sin criterios explícitos, la validación es subjetiva e inconsistente.

**Checklist de validación (ilustrativo)**

- ✅ Número y nombre de campos correcto
- ✅ Orden de secciones respetado
- ✅ Tipos de valores adecuados (número, fecha, cadena)
- ✅ Convenciones de fecha y unidades aplicadas
- ✅ Regla para ausencias declarada (null, vacío, omitido)
- ✅ Sin campos inventados fuera del esquema

**Principio clave**

Un formato correcto no garantiza que el contenido sea verdadero o útil. La validación estructural y la validación semántica son dos procesos distintos y complementarios.

Define los criterios de aceptación antes de enviar el prompt, no después de leer la respuesta.

**Explicación**

Hacer verificable la salida significa definir de antemano las condiciones de aceptación; sin ellas, la validación es subjetiva. La lista de comprobación incluye: número y nombre de campos correctos, orden de secciones respetado, tipos adecuados (número, fecha, cadena), convenciones de fecha y unidades aplicadas, regla de ausencias declarada (null, vacío u omitido) y ausencia de campos inventados fuera del **esquema**.

Un formato correcto no garantiza un contenido verdadero o útil: la validación estructural y la semántica son distintas y complementarias. Los criterios se definen antes de enviar el prompt, no después de leer la respuesta, porque fijarlos después permite adaptarlos para aceptar lo que ya se tiene. Gran parte puede automatizarse; el contenido, en cambio, requiere reglas de negocio, comparación con una fuente o revisión humana.

---

[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-salidas-estructuradas.md)
