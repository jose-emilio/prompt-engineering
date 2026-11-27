Fichero `datos/incidencias_2026.csv` (una fila por incidencia, separador coma, codificación UTF-8):

- `id`: identificador de la incidencia (texto). Algunas filas están repetidas por un error de exportación.
- `abierta`: fecha de apertura, en dos formatos: `AAAA-MM-DD` o `DD/MM/AAAA`.
- `producto`: Altanoria Copilot, DocuMind o AgentHub, escritos de varias formas («Copilot», «Docu Mind», «agenthub»…).
- `prioridad`: P1 (más grave) a P4.
- `duracion` y `unidad`: duración de la incidencia (número con decimales) y su unidad, `min` o `h`.
- `usuarios_afectados`: número entero; vacío cuando no consta.
- `causa`: configuracion, despliegue, dependencia_externa, capacidad, bug_codigo, datos, seguridad o desconocida.
- `canal`: correo, chat, telefono o portal.
- `reabierta`: `si` o `no`.
