# Tres especificaciones de ejemplo para analizar

Las tres piden lo mismo: añadir el plan Business a la función de facturación. Se puntúan en el Paso 7 con la lista de seis puntos.

## Especificación A

Añade el plan Business al cálculo de facturas de Copilot. Que funcione bien y quede limpio.

## Especificación B

Objetivo: el equipo comercial necesita que el formulario de precios calcule también el plan Business.

Alcance: la función `calcularFacturaCopilot`.

Criterio: 20 usuarios en Business con facturación mensual dan un total de 849,42 €.

Lo demás, igual que en los otros planes.

## Especificación C

Objetivo y contexto: Altanoria lanza un plan intermedio, Business. El equipo comercial necesita que el formulario de precios lo calcule igual que los demás planes.

Alcance y exclusiones: entra la función `calcularFacturaCopilot` de `facturacion.js`. No se toca la forma del resultado (las seis claves) ni los planes Starter, Team y Enterprise.

Criterios de aceptación:
- `("Business", 20, "mensual", false)` da base 780,00; descuento 78,00 (10 %); subtotal 702,00; IVA 147,42; total 849,42.
- `("Business", 20, "anual", false)` da base 7.920,00; sin descuento; total 9.583,20.
- Los 106 casos de `datos/casos_aceptacion.csv` siguen pasando.

Restricciones técnicas: JavaScript ES2020, sin bibliotecas ni módulos y la misma firma `calcularFacturaCopilot(plan, usuarios, periodo = "mensual", educativo = false)`.
