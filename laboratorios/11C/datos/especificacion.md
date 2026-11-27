# Especificación: cálculo de la factura de Altanoria Copilot

Implementar en Python (3.9 o superior, sin dependencias externas) la función:

```python
def calcular_factura_copilot(plan: str, usuarios: int,
                             periodo: str = "mensual",
                             educativo: bool = False) -> dict:
    ...
```

## Reglas de negocio (extraídas del catálogo de planes)

1. Planes válidos: `"Starter"`, `"Team"`, `"Enterprise"`. Cualquier otro valor → `ValueError`.
2. Periodos válidos: `"mensual"` y `"anual"`. Cualquier otro valor → `ValueError`.
3. Usuarios: entero positivo. Un valor no entero, booleano o menor que 1 → `ValueError`.
4. Mínimo de usuarios por plan: Starter 1, Team 5, Enterprise 50. Por debajo del mínimo → `ValueError`.
5. Precio por usuario y mes (euros, sin IVA):

   | Plan | Mensual | Anual (precio por mes) |
   |---|---|---|
   | Starter | 12 | 10 |
   | Team | 29 | 24 |
   | Enterprise | 59 | 49 |

6. Base:
   - Mensual: `precio_mensual × usuarios` (una mensualidad).
   - Anual: `precio_anual_por_mes × usuarios × 12` (se factura el año completo).
7. Descuento por volumen: solo en facturación mensual. 10 % si hay 20 o más usuarios; 15 % si hay 100 o más. Se aplica sobre la base.
8. Descuento educativo/sin ánimo de lucro: 30 % sobre la base, si `educativo` es `True`, en cualquier periodo.
9. No son acumulables: si corresponden ambos descuentos, se aplica el mayor de los dos porcentajes.
10. IVA: 21 % sobre el subtotal (base menos descuento).
11. Redondeo: cada importe monetario se redondea a 2 decimales, mitad hacia arriba (`ROUND_HALF_UP`), en este orden: base → descuento → subtotal → IVA → total. Se recomienda usar `decimal.Decimal` para evitar errores de coma flotante.

## Salida

Diccionario con estas claves (todas `float`):

| Clave | Significado |
|---|---|
| `base` | Importe antes de descuentos |
| `descuento_pct` | Porcentaje de descuento aplicado, en forma decimal (0.10, 0.15, 0.30 o 0.0) |
| `descuento` | Importe del descuento |
| `subtotal` | Base menos descuento |
| `iva` | IVA del subtotal |
| `total` | Subtotal más IVA |

## Ejemplos

| Entrada | Salida |
|---|---|
| `("Team", 10, "mensual", False)` | base 290.00; descuento 0.0 → 0.00; subtotal 290.00; iva 60.90; total 350.90 |
| `("Team", 25, "mensual", False)` | base 725.00; 10 % → 72.50; subtotal 652.50; iva 137.03 (137.025 → 137.03); total 789.53 |
| `("Starter", 3, "anual", True)` | base 360.00; 30 % → 108.00; subtotal 252.00; iva 52.92; total 304.92 |
