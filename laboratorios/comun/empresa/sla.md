# Acuerdo de nivel de servicio (SLA) y soporte — Altanoria (ficticio)

## 1. Disponibilidad mensual garantizada

| Plan | Disponibilidad mensual |
|---|---|
| Starter | 99,0 % |
| Team | 99,5 % |
| Enterprise | 99,9 % |

La disponibilidad se mide por mes natural como el porcentaje de minutos en los que el servicio responde correctamente a las comprobaciones de estado, descontando el mantenimiento programado.

Mantenimiento programado: hasta 4 horas al mes, avisado con al menos 72 horas de antelación en la página de estado. No computa como indisponibilidad.

Exclusiones: fallos de la red del cliente, uso contrario a las condiciones, fuerza mayor, servicios de terceros no gestionados por Altanoria (por ejemplo, el sistema de correo del cliente) y pruebas gratuitas.

## 2. Créditos por incumplimiento

Si la disponibilidad mensual es inferior a la garantizada del plan, el cliente tiene derecho a un crédito sobre la cuota mensual del producto afectado:

| Disponibilidad medida | Crédito |
|---|---|
| Inferior a la garantizada pero no más de 1 punto porcentual por debajo | 10 % de la cuota mensual |
| Más de 1 punto porcentual por debajo, pero igual o superior al 95,0 % | 25 % de la cuota mensual |
| Inferior al 95,0 % | 50 % de la cuota mensual |

- El crédito máximo por mes es el 50 % de la cuota mensual.
- Se solicita por escrito en un plazo de 30 días naturales desde el fin del mes afectado; si no se solicita, se pierde.
- El crédito se aplica a la factura siguiente; no se abona en efectivo.
- Es el único remedio por indisponibilidad, salvo lo dispuesto para Enterprise en su contrato.

## 3. Prioridades de incidencia

| Prioridad | Definición | Ejemplos |
|---|---|---|
| P1 — Crítica | Servicio caído o pérdida/exposición de datos con impacto en producción del cliente, sin alternativa. | Caída total; datos de otro cliente visibles; filtración de credenciales. |
| P2 — Alta | Degradación grave o bloqueo de un equipo o función principal; existe una alternativa muy limitada. | Latencia diez veces superior a la habitual; una integración clave falla. |
| P3 — Media | Error o consulta con solución alternativa aceptable; sin impacto en producción. | Un botón no responde; resultados incorrectos en un caso concreto. |
| P4 — Baja | Consulta informativa, sugerencia o mejora. | Solicitud de funcionalidad; duda de uso. |

## 4. Tiempos de primera respuesta

| Prioridad | Starter | Team | Enterprise |
|---|---|---|---|
| P1 | 1 día hábil | 4 horas (horario de soporte) | 1 hora (24x7) |
| P2 | 2 días hábiles | 8 horas (horario de soporte) | 4 horas (24x7) |
| P3 | 3 días hábiles | 2 días hábiles | 1 día hábil |
| P4 | 5 días hábiles | 3 días hábiles | 2 días hábiles |

- Horario de soporte: lunes a viernes, de 9:00 a 18:00 (hora peninsular española), excepto festivos nacionales y de la Comunitat Valenciana.
- Canales: Starter, correo electrónico; Team, correo y chat; Enterprise, correo, chat, teléfono y un gestor de cuenta asignado.
- El tiempo de primera respuesta no es un tiempo de resolución: Altanoria no garantiza plazos de resolución, salvo lo pactado en contratos Enterprise.

## 5. Escalado

Una incidencia se escala a Ingeniería cuando es P1 o P2, o cuando Soporte de nivel 1 no la resuelve en el doble del tiempo de primera respuesta. Cualquier incidencia con posible exposición de datos personales se comunica además al Responsable de Seguridad y Cumplimiento.
