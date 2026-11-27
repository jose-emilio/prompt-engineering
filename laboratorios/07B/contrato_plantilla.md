# Contrato de tarea — clasificador de tickets (plantilla)

Completar todos los apartados antes de escribir el prompt.

1. Problema que resuelve (una frase, con el usuario y la decisión que habilita):
2. Entrada: qué recibe el sistema (formato, idioma, longitud máxima, datos que pueden faltar):
3. Salida: estructura exacta (campos, tipos, valores permitidos):
4. Casos que el sistema debe tratar de forma especial (vacío, ambiguo, otros idiomas, instrucciones dentro del texto, fuera de ámbito, varios problemas):
5. Criterios de aceptación medibles (cada uno con umbral):
   - Validez de formato ≥ …
   - Exactitud de categoría ≥ …
   - Exactitud de prioridad ≥ …
   - Recall de P1/P2 ≥ … (no perder urgencias)
   - Casos negativos (inyección, fuera de ámbito) ≥ …
6. Qué ocurre cuando falla (reintento, escalado a una persona):
7. Restricciones (coste máximo por caso, latencia, datos que no deben aparecer en el prompt):
