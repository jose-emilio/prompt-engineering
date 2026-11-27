# Muestra de 6 casos de facturación para comprobar sin ejecutar código

Muestra pequeña para hacer el laboratorio sin Python, copiando los casos en un chat. Las respuestas correctas están al final, plegadas: no abrirlas hasta haber anotado las propias.

Función: calcula el total de una factura de Altanoria Copilot (plan, usuarios, periodo, descuento educativo). Reglas en `datos/especificacion.md`.

Sin ejecutar código, pedir al chat que calcule estos casos paso a paso y comparar sus resultados con los correctos:

- Plan Team, 6 usuarios, facturación mensual, educativo: no
- Plan Team, 21 usuarios, facturación mensual, educativo: no
- Plan Starter, 1 usuarios, facturación anual, educativo: sí
- Plan Enterprise, 101 usuarios, facturación mensual, educativo: no
- Plan Starter, 20 usuarios, facturación mensual, educativo: sí
- Plan Team, 100 usuarios, facturación anual, educativo: no

<details>
<summary>Respuestas correctas de la muestra</summary>

| plan | usuarios | periodo | educativo | base | descuento | iva | total |
|---|---|---|---|---|---|---|---|
| Team | 6 | mensual | False | 174.0 | 0.0 | 36.54 | 210.54 |
| Team | 21 | mensual | False | 609.0 | 60.9 | 115.1 | 663.2 |
| Starter | 1 | anual | True | 120.0 | 36.0 | 17.64 | 101.64 |
| Enterprise | 101 | mensual | False | 5959.0 | 893.85 | 1063.68 | 6128.83 |
| Starter | 20 | mensual | True | 240.0 | 72.0 | 35.28 | 203.28 |
| Team | 100 | anual | False | 28800.0 | 0.0 | 6048.0 | 34848.0 |

</details>
