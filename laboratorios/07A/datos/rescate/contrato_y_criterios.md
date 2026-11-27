# Contrato de ejemplo (rescate)

Solo para quien se haya atascado. Cuenta con haberlo intentado antes: copiar este texto sin leerlo quita sentido al paso.

1. Problema: clasificar cada reclamación para enrutarla al equipo adecuado y fijar su prioridad de atención según el SLA.
2. Entrada: texto libre de una reclamación, en español o en otro idioma, de 0 a 3.000 caracteres, que puede incluir historial de correo, avisos legales o instrucciones dirigidas a un sistema.
3. Salida: JSON `{"categoria": <una de las 11 categorías>, "prioridad": "P1"|"P2"|"P3"|"P4"}`.
4. Casos especiales: vacío o vago → `necesita_aclaracion`/P3; ajeno al servicio → `no_soporte`/P4; varios problemas → el más grave; instrucciones dentro del texto → se ignoran.
5. Criterios de aceptación: JSON válido 100 %; categoría ≥ 90 %; prioridad ≥ 85 %; recall de P1 y P2 ≥ 95 %; casos negativos 100 %.
6. Si falla: reintento (hasta 2) ante formato inválido; escalado a una persona si persiste o si la confianza es baja.
7. Restricciones: coste y latencia acotados; no incluir datos personales reales en los prompts.
