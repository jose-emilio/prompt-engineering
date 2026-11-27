# Muestra para comparar zero-shot y few-shot

Muestra pequeña para hacer el laboratorio sin Python, copiando los casos en un chat. Las respuestas correctas están al final, plegadas: no abrirlas hasta haber anotado las propias.

## Ejemplos etiquetados (para el prompt few-shot)

- (facturacion) Una duda sobre facturación: si paso del plan Team al plan Enterprise a mitad de mes, ¿cómo se calcula la prorrata? Solo quiero entender el cálculo, no hay ningún problema con la factura.
- (acceso) Un nuevo miembro del equipo, Raquel Herrero Guillén, no está recibiendo la invitación para unirse al espacio de DocuMind, a pesar de haber intentado reenviarla en dos ocasiones.
- (rendimiento) A veces, no siempre, AgentHub tarda bastante en responder entre las 12 y las 13 h. No es bloqueante, pero lo notamos.
- (integracion) Desde hace dos días, el conector de Confluence no ha logrado sincronizar los documentos en Altanoria Copilot, acumulando más de 3.000 pendientes, lo que hace que el equipo de Finanzas trabaje con datos obsoletos.
- (error) El botón 'Copiar' de los bloques de código no hace nada en Firefox. En Chrome sí funciona.
- (funcionalidad) Propongo la posibilidad de asignar etiquetas a los flujos de AgentHub según el proyecto al que pertenecen, con el fin de poder filtrarlos en la lista; actualmente contamos con más de 200 flujos y gestionarlos se ha vuelto complicado.
- (seguridad) Creemos haber detectado una vulnerabilidad: introduciendo cierto texto en el campo de nombre del flujo, se ejecuta una etiqueta HTML en el panel. Podemos enviar los detalles por canal seguro.
- (cancelacion) Queremos cancelar la suscripción de Altanoria Copilot al finalizar el mes. ¿Qué pasos debemos seguir y qué pasa con nuestros datos?
- (consulta) ¿Podrían indicarme cuál es el tiempo promedio de respuesta que debemos anticipar al utilizar Altanoria Copilot bajo el plan Starter? Esta información es crucial para la planificación adecuada de nuestro proyecto, ya que actualmente no contamos con ningún problema o incidencia pendiente.

## Tickets de prueba (clasificarlos)

**P-001**

> Hola,
>
> La extensión de PyCharm bloquea el editor cada pocos minutos y el equipo de Atención al cliente no puede programar. Ya hemos reinstalado dos veces.
>
> Gracias.

**P-002**

> Hola equipo de soporte:
>
> En la última factura emitida con número ALT-2026-08735, aún se reflejan 6 licencias, cuando solicitamos la reducción a 1 para el próximo ciclo. ¿Sería posible corregir este error en la facturación?
>
> Muchas gracias de antemano.

**P-003**

> El informe mensual de Altanoria Copilot muestra un total distinto al de la suma de sus líneas (3.480,00 € frente a la suma real). Parece un error de cálculo. Por otro lado, ¿Es viable configurar AgentHub para que solo permita accesos desde el rango de IP de nuestra oficina? Me gustaría saber si esta funcionalidad está disponible en el plan Team.

**P-004**

> Hola equipo de soporte:
>
> Me gustaría saber cómo se gestiona la renovación automática de DocuMind y, además, me interesa conocer con qué antelación se notifica a los usuarios sobre cualquier cambio en el precio.
>
> Le paso también el PDF de la factura.

**P-005**

> El cobro realizado el 14 de julio de 2026 por un importe de 2.400,00 € supera lo acordado, ya que nos estábais aplicando la tarifa estándar en lugar del descuento por volumen que ya habíamos firmado. Por otro lado, la información en AgentHub se está eliminando en vez de actualizarse durante la sincronización con Google Drive, lo que nos ha provocado una pérdida de datos durante 40 minutos y, en este momento, no contamos con el método para detenerlo.

**P-006**

> Desde el lunes, la indexación de documentos en DocuMind ha pasado a tardar más de seis horas, cuando antes se completaba en solo 20 minutos, lo que obliga al equipo de Atención al cliente a trabajar con información obsoleta.
>
> Un saludo,
> Silvia Galiana Uribe

**P-007**

> El informe mensual de Altanoria Copilot muestra un total distinto al de la suma de sus líneas (599,00 € frente a la suma real). Parece un error de cálculo.
>
> Saludos cordiales,
> Bruno Lozano Mascarell
> Consultora Atalaya
>
> Obtener Outlook para Android

**P-008**

> ¿cuántos usuarios mínimos hay que contratar en el plan team? somos 120 personas.
>
> Quedo a la espera.

**P-009**

> Hola equipo de soporte:
>
> Algunas respuestas de DocuMind se quedan cargando unos 30 segundos y luego terminan bien. Nos pasa dos o tres veces al día, sin un patrón claro.
>
> Gracias y un saludo.
> Carlos Ibáñez Segarra

**P-010**

> Me pregunto si AgentHub es compatible con Jira Cloud, ya que no logro encontrarlo dentro de la lista de conectores disponibles. Por otro lado, se han registrado accesos no autorizados desde naciones en las que no tenemos presencia operativa utilizando las credenciales de administrador asignadas a Banco Mediterráneo Digital dentro del sistema Altanoria Copilot, y durante la noche de hoy se realizó la exportación de información perteneciente a nuestros clientes.

<details>
<summary>Respuestas correctas de la muestra</summary>

| id | categoria |
|---|---|
| P-001 | integracion |
| P-002 | facturacion |
| P-003 | error |
| P-004 | consulta |
| P-005 | facturacion |
| P-006 | rendimiento |
| P-007 | error |
| P-008 | consulta |
| P-009 | rendimiento |
| P-010 | funcionalidad |

</details>
