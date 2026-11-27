# Muestra de 6 correos (extracción a JSON)

Muestra pequeña para hacer el laboratorio sin Python, copiando los casos en un chat. Las respuestas correctas están al final, plegadas: no abrirlas hasta haber anotado las propias.

C-001 (fecha del correo: 2026-10-11)

> De: cristina.cano@logisticapirin.example · Asunto: Solicitud de baja
>
> Buenos días:
>
> Queremos dar de baja AgentHub Enterprise. Lo comunicamos el martes pasado.
>
> Saludos,
> Cristina Cano Campos
> Logística Pirineos

C-002 (fecha del correo: 2026-08-25)

> De: cristina.pla@quesosartesano.example · Asunto: Reclamación de factura
>
> Buenos días:
>
> Reclamamos la factura ALT-2026-07753: figura un importe de 87 euros que no corresponde a el servicio. Según nuestro pedido el importe correcto era -13 €.
>
> Saludos,
> Cristina Pla Herrero
> Quesos Artesanos Manchegos

C-003 (fecha del correo: 2026-05-03)

> De: daniel.esteve@bancomediterra.example · Asunto: Reclamación de factura
>
> Buenos días:
>
> Reclamamos la factura ALT-2026-06004: figura un importe de 87,00 € que no corresponde a AgentHub. Según nuestro pedido el importe correcto era -13 €.
>
> Atentamente,
> Daniel Esteve Vidal
> Banco Mediterráneo Digital

C-004 (fecha del correo: 2026-05-26)

> De: bruno.revert@renovablessier.example · Asunto: Consulta comercial
>
> Buenos días:
>
> Estamos valorando AgentHub Enterprise para 20 personas. ¿Pueden enviarnos una propuesta con descuento por volumen?
>
> Gracias.
> Bruno Revert Peiró
> Renovables Sierra Norte

C-005 (fecha del correo: 2026-03-13)

> De: ismael.olmos@aguasdecantabr.example · Asunto: Reclamación de factura
>
> Buenos días:
>
> Reclamamos la factura ALT-2026-09124: figura un importe de 599,00 € que no corresponde a DocuMind Starter.
>
> Gracias.
> Ismael Olmos Muñoz
> Aguas de Cantabria

C-006 (fecha del correo: 2026-06-29)

> De: mario.millan@editorialcuatr.example · Asunto: Incidencia en el servicio
>
> Buenos días:
>
> Desde hoy Altanoria Copilot Team falla en Editorial Cuatro Vientos. Afecta a 3 personas. No es bloqueante.
>
> Un cordial saludo,
> Mario Millán Herrero
> Editorial Cuatro Vientos

<details>
<summary>Respuestas correctas de la muestra</summary>

**C-001**

```json
{
  "id": "C-001",
  "remitente": "Cristina Cano Campos",
  "empresa": "Logística Pirineos",
  "producto": "AgentHub",
  "plan": "Enterprise",
  "tipo_solicitud": "cancelacion",
  "fecha_hecho": "2026-10-06",
  "importe_reclamado_eur": null,
  "referencia_factura": null,
  "codigo_error": null,
  "usuarios_afectados": null,
  "urgencia": "media"
}
```

**C-002**

```json
{
  "id": "C-002",
  "remitente": "Cristina Pla Herrero",
  "empresa": "Quesos Artesanos Manchegos",
  "producto": null,
  "plan": null,
  "tipo_solicitud": "factura",
  "fecha_hecho": "2026-08-22",
  "importe_reclamado_eur": 87.0,
  "referencia_factura": "ALT-2026-07753",
  "codigo_error": null,
  "usuarios_afectados": null,
  "urgencia": "media"
}
```

**C-003**

```json
{
  "id": "C-003",
  "remitente": "Daniel Esteve Vidal",
  "empresa": "Banco Mediterráneo Digital",
  "producto": "AgentHub",
  "plan": null,
  "tipo_solicitud": "factura",
  "fecha_hecho": null,
  "importe_reclamado_eur": 87.0,
  "referencia_factura": "ALT-2026-06004",
  "codigo_error": null,
  "usuarios_afectados": null,
  "urgencia": "media"
}
```

**C-004**

```json
{
  "id": "C-004",
  "remitente": "Bruno Revert Peiró",
  "empresa": "Renovables Sierra Norte",
  "producto": "AgentHub",
  "plan": "Enterprise",
  "tipo_solicitud": "comercial",
  "fecha_hecho": null,
  "importe_reclamado_eur": null,
  "referencia_factura": null,
  "codigo_error": null,
  "usuarios_afectados": 20,
  "urgencia": "baja"
}
```

**C-005**

```json
{
  "id": "C-005",
  "remitente": "Ismael Olmos Muñoz",
  "empresa": "Aguas de Cantabria",
  "producto": "DocuMind",
  "plan": "Starter",
  "tipo_solicitud": "factura",
  "fecha_hecho": null,
  "importe_reclamado_eur": 599.0,
  "referencia_factura": "ALT-2026-09124",
  "codigo_error": null,
  "usuarios_afectados": null,
  "urgencia": "media"
}
```

**C-006**

```json
{
  "id": "C-006",
  "remitente": "Mario Millán Herrero",
  "empresa": "Editorial Cuatro Vientos",
  "producto": "Altanoria Copilot",
  "plan": "Team",
  "tipo_solicitud": "incidencia",
  "fecha_hecho": "2026-06-29",
  "importe_reclamado_eur": null,
  "referencia_factura": null,
  "codigo_error": null,
  "usuarios_afectados": 3,
  "urgencia": "baja"
}
```

</details>
