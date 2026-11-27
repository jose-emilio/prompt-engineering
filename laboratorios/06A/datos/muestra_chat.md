# Muestra de 5 notas de incidencia (convertir a JSON)

Muestra pequeña para hacer el laboratorio sin Python, copiando los casos en un chat. Las respuestas correctas están al final, plegadas: no abrirlas hasta haber anotado las propias.

**INC-4001**

> INC-4001 — Naviera Bética nos avisó el 25 de marzo de 2026 sobre Altanoria Copilot. Empezó a las 21:50 y duró 5 minutos. Prioridad P4. Afecta a unos 2 usuarios. Causa: un despliegue defectuoso. Acciones: reinicio del servicio, ampliación de capacidad y reindexado de documentos. Resuelta.

**INC-4002**

> Nota de turno: sobre las 18:30 del 27 de septiembre de 2026, Papelera del Segura reportó un problema con DocuMind (INC-4002, P4). Tras revisar, era datos corruptos en el índice. Hemos aplicado reversión del despliegue, ampliación de capacidad y corrección de configuración. Tiempo total: 5 minutos. No consta impacto en usuarios. Resuelta.

**INC-4003**

> Nota de turno: sobre las 19:20 del 5 de septiembre de 2026, Clínica Dental Sonrisa reportó un problema con AgentHub (INC-4003, P3). Tras revisar, era un incidente de seguridad. Hemos aplicado renovación del certificado y ampliación de capacidad. Tiempo total: 10 minutos. Afecta a unos 120 usuarios. Resuelta. No procede crédito.

**INC-4004**

> Ticket INC-4004 (P2). Cliente: Grupo Hortelano. Producto: Altanoria Copilot. Inicio 16 de octubre de 2026 a las 09:00h, 25 min de duración. Origen: un despliegue defectuoso. Se hizo: aplicación de parche y renovación del certificado. Afecta a unos 3 usuarios. Resuelta. No procede crédito.

**INC-4005**

> Ticket INC-4005 (P1). Cliente: Inmobiliaria Costa Azahar. Producto: Altanoria Copilot. Inicio 28 de marzo de 2026 a las 05:30h, 95 min de duración. Origen: un bug en el código. Se hizo: aplicación de parche y reinicio del servicio. No consta impacto en usuarios. Sigue abierta, en seguimiento. No procede crédito.

<details>
<summary>Respuestas correctas de la muestra</summary>

**INC-4001**

```json
{
  "id": "INC-4001",
  "cliente": "Naviera Bética",
  "producto": "Altanoria Copilot",
  "prioridad": "P4",
  "inicio": "2026-03-25T21:50",
  "duracion_minutos": 5,
  "usuarios_afectados": 2,
  "causa_raiz": "despliegue",
  "acciones": [
    "reinicio del servicio",
    "ampliación de capacidad",
    "reindexado de documentos"
  ],
  "resuelta": true,
  "credito_sla_eur": null
}
```

**INC-4002**

```json
{
  "id": "INC-4002",
  "cliente": "Papelera del Segura",
  "producto": "DocuMind",
  "prioridad": "P4",
  "inicio": "2026-09-27T18:30",
  "duracion_minutos": 5,
  "usuarios_afectados": 0,
  "causa_raiz": "datos",
  "acciones": [
    "reversión del despliegue",
    "ampliación de capacidad",
    "corrección de configuración"
  ],
  "resuelta": true,
  "credito_sla_eur": null
}
```

**INC-4003**

```json
{
  "id": "INC-4003",
  "cliente": "Clínica Dental Sonrisa",
  "producto": "AgentHub",
  "prioridad": "P3",
  "inicio": "2026-09-05T19:20",
  "duracion_minutos": 10,
  "usuarios_afectados": 120,
  "causa_raiz": "seguridad",
  "acciones": [
    "renovación del certificado",
    "ampliación de capacidad"
  ],
  "resuelta": true,
  "credito_sla_eur": null
}
```

**INC-4004**

```json
{
  "id": "INC-4004",
  "cliente": "Grupo Hortelano",
  "producto": "Altanoria Copilot",
  "prioridad": "P2",
  "inicio": "2026-10-16T09:00",
  "duracion_minutos": 25,
  "usuarios_afectados": 3,
  "causa_raiz": "despliegue",
  "acciones": [
    "aplicación de parche",
    "renovación del certificado"
  ],
  "resuelta": true,
  "credito_sla_eur": null
}
```

**INC-4005**

```json
{
  "id": "INC-4005",
  "cliente": "Inmobiliaria Costa Azahar",
  "producto": "Altanoria Copilot",
  "prioridad": "P1",
  "inicio": "2026-03-28T05:30",
  "duracion_minutos": 95,
  "usuarios_afectados": 0,
  "causa_raiz": "bug_codigo",
  "acciones": [
    "aplicación de parche",
    "reinicio del servicio"
  ],
  "resuelta": false,
  "credito_sla_eur": null
}
```

</details>
