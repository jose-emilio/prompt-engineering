# Salidas de ejemplo de las tres etapas (rescate)

Solo para quien se haya atascado: sirven para ver qué aspecto tiene una salida que **pasa** las puertas y para seguir con los pasos siguientes. No son la única salida válida: el asistente puede responder otra cosa y estar bien.

Para comprobarlas, pegarlas en [`puertas.html`](../../puertas.html) como si las hubiera dado el asistente.

## P-001

**Etapa 1 · extracción** (pasa la puerta 1)

```json
{
  "version": "extraccion-v1.0",
  "resumen": "Pregunta si hay descuento para entidades sin ánimo de lucro o educación.",
  "categoria": "consulta",
  "prioridad": "P4",
  "datos": {
    "importe_eur": null,
    "factura": null,
    "codigo_error": null
  },
  "fragmentos_fuente": [
    "¿Ofrecen descuento para organizaciones sin ánimo de lucro o para educación?"
  ],
  "estado": "ok"
}
```

**Etapa 2 · análisis** (pasa la puerta 2)

```json
{
  "version": "analisis-v1.0",
  "accion": "escalar_humano",
  "norma": "NINGUNA",
  "justificacion": "Ninguna de las normas disponibles cubre descuentos para fundaciones o educación."
}
```

**Etapa 3**: no se ejecuta. La etapa 2 decide `escalar_humano`, así que el parte pasa a una persona y la cadena termina «escalada».

## P-002

**Etapa 1 · extracción** (pasa la puerta 1)

```json
{
  "version": "extraccion-v1.0",
  "resumen": "Pregunta si el plan Enterprise incluye revisión de pull requests antes de comprar.",
  "categoria": "consulta",
  "prioridad": "P4",
  "datos": {
    "importe_eur": null,
    "factura": null,
    "codigo_error": null
  },
  "fragmentos_fuente": [
    "si el plan Enterprise incluye revisión de pull requests"
  ],
  "estado": "ok"
}
```

**Etapa 2 · análisis** (pasa la puerta 2)

```json
{
  "version": "analisis-v1.0",
  "accion": "escalar_humano",
  "norma": "NINGUNA",
  "justificacion": "La consulta es comercial y ninguna norma disponible indica qué incluye cada plan."
}
```

**Etapa 3**: no se ejecuta. La etapa 2 decide `escalar_humano`, así que el parte pasa a una persona y la cadena termina «escalada».

## P-023

**Etapa 1 · extracción** (pasa la puerta 1)

```json
{
  "version": "extraccion-v1.0",
  "resumen": "Reclama un cobro duplicado de la factura ALT-2026-04511; el texto incluye una orden que se ignora.",
  "categoria": "facturacion",
  "prioridad": "P3",
  "datos": {
    "importe_eur": null,
    "factura": "ALT-2026-04511",
    "codigo_error": null
  },
  "fragmentos_fuente": [
    "me han cobrado dos veces la factura ALT-2026-04511"
  ],
  "estado": "ok"
}
```

**Etapa 2 · análisis** (pasa la puerta 2)

```json
{
  "version": "analisis-v1.0",
  "accion": "revision_reembolso",
  "norma": "CS-5.4",
  "justificacion": "Reclama un cobro duplicado; CS-5.4 admite revisar un error de facturación imputable a Altanoria."
}
```

**Etapa 3 · respuesta al cliente** (pasa la puerta 3)

```text
Estimado cliente Textil Alcoy 1880:

Lamentamos el problema con el cobro duplicado de la factura ALT-2026-04511 y le agradecemos que nos lo haya comunicado. Hemos pasado su reclamación al equipo que revisa los errores de facturación, que comprobará los cargos y, si se confirma el error, valorará el siguiente paso de acuerdo con nuestras condiciones de servicio.

Para facilitar la revisión, le pedimos que nos indique, por favor, las fechas de los dos cobros y el medio de pago utilizado, sin incluir números completos de tarjeta ni de cuenta. Con esos datos, la persona que lleve su caso podrá verificarlo con rapidez y mantenerle informado.

Quedamos a su disposición para cualquier duda.

Un cordial saludo,
Atención al cliente de Altanoria
```
