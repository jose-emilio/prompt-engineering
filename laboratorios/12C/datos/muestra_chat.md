# Muestra de 30 incidencias (indicadores de Soporte)

Muestra pequeña para hacer el laboratorio sin Python, copiando los casos en un chat. Las respuestas correctas están al final, plegadas: no abrirlas hasta haber anotado las propias.

Treinta incidencias exportadas del sistema de Soporte (la primera línea es la cabecera). Pegar el bloque entero donde el prompt dice `{{muestra}}`. Como en el fichero completo, hay filas repetidas, productos escritos de varias formas, duraciones en horas, fechas en dos formatos y usuarios vacíos.

```csv
id,abierta,producto,prioridad,duracion,unidad,usuarios_afectados,causa,canal,reabierta
INC-6227,25/04/2026,AgentHub,P4,24,min,8,dependencia_externa,telefono,no
INC-6181,2026-10-02,AgentHub,P4,29,min,4800,bug_codigo,correo,no
INC-6036,2026-10-08,DocuMind,P3,29,min,61,dependencia_externa,correo,no
INC-6221,2026-09-12,Documind,P4,6,min,35,despliegue,portal,no
INC-6250,10/05/2026,Altanoria Copilot,P3,27,min,17,despliegue,chat,no
INC-6110,2026-10-22,AgentHub,P4,22,min,2,bug_codigo,telefono,no
INC-6027,12/02/2026,Documind,P4,17,min,3,configuracion,portal,no
INC-6097,01/03/2026,Altanoria Copilot,P3,25,min,26,bug_codigo,portal,no
INC-6126,2026-04-05,Altanoria Copilot,P3,60,min,3,configuracion,chat,no
INC-6017,08/04/2026,Docu Mind,P3,33,min,4,bug_codigo,telefono,no
INC-6131,2026-09-04,DocuMind,P4,31,min,,bug_codigo,telefono,no
INC-6101,2026-09-09,Documind,P2,5,min,5,bug_codigo,correo,no
INC-6239,2026-09-01,DocuMind,P4,13,min,,bug_codigo,portal,no
INC-6299,2026-02-06,DocuMind,P1,2.1,h,5,configuracion,telefono,no
INC-6275,07/08/2026,Altanoria Copilot,P4,22,min,9,configuracion,correo,no
INC-6328,26/10/2026,Copilot,P4,23,min,,configuracion,telefono,no
INC-6012,2026-05-23,DocuMind,P4,18,min,12,desconocida,portal,no
INC-6323,2026-09-21,AgentHub,P4,26,min,5,dependencia_externa,chat,no
INC-6198,2026-09-21,copilot,P3,52,min,41,dependencia_externa,portal,no
INC-6342,2026-10-08,Copilot,P1,1.4,h,5,configuracion,portal,no
INC-6279,04/05/2026,Copilot,P3,59,min,3,bug_codigo,correo,no
INC-6342,2026-10-08,Copilot,P1,1.4,h,5,configuracion,portal,no
INC-6345,2026-09-02,Agent Hub,P1,81,min,26,capacidad,portal,no
INC-6239,2026-09-01,DocuMind,P4,13,min,,bug_codigo,portal,no
INC-6184,2026-10-17,agenthub,P3,6,min,9,configuracion,correo,no
INC-6147,2026-06-25,DocuMind,P3,59,min,8,bug_codigo,telefono,no
INC-6007,2026-09-22,Altanoria Copilot,P4,35,min,10,capacidad,chat,no
INC-6044,2026-09-01,Altanoria Copilot,P1,2.6,h,33,desconocida,correo,no
INC-6320,2026-01-17,DocuMind,P3,58,min,24,configuracion,telefono,no
INC-6181,2026-10-02,AgentHub,P4,29,min,4800,bug_codigo,correo,no
```

<details>
<summary>Respuestas correctas de la muestra</summary>

Indicadores correctos de la muestra (30 filas, 27 incidencias distintas):

```json
{
  "incidencias_por_producto": {
    "AgentHub": 6,
    "Altanoria Copilot": 10,
    "DocuMind": 11
  },
  "duracion_media_min_por_producto": {
    "AgentHub": 31.3,
    "Altanoria Copilot": 54.3,
    "DocuMind": 35.9
  },
  "porcentaje_p1": 14.81,
  "incidencias_por_mes": {
    "2026-01": 1,
    "2026-02": 2,
    "2026-03": 1,
    "2026-04": 3,
    "2026-05": 3,
    "2026-06": 1,
    "2026-08": 1,
    "2026-09": 9,
    "2026-10": 6
  },
  "mediana_usuarios_afectados": 9.0,
  "causa_mas_frecuente": {
    "causa": "bug_codigo",
    "porcentaje": 33.3
  }
}
```

</details>
