"""Contratos de cada etapa (versión 1.0). Un contrato = qué entra, qué sale y qué errores se contemplan."""

CATEGORIAS = ["facturacion", "acceso", "rendimiento", "integracion", "error", "funcionalidad",
              "seguridad", "cancelacion", "consulta", "necesita_aclaracion", "no_soporte"]
ACCIONES = ["responder", "revision_reembolso", "escalar_humano", "pedir_datos", "rechazar"]

NORMAS = {
    "CS-4.3": "Pago de facturas a 30 días; interés de demora del 8 % anual.",
    "CS-5.1": "La suscripción mensual puede cancelarse en cualquier momento; surte efecto al final del periodo pagado.",
    "CS-5.3": "Reembolso íntegro si se cancela una suscripción anual en los 30 días siguientes a la contratación o primera renovación.",
    "CS-5.4": "Las suscripciones mensuales no son reembolsables, salvo error de facturación imputable a Altanoria.",
    "CS-10.1": "El Servicio se presta «tal cual» respecto de la exactitud de los contenidos generados; el cliente revisa las salidas.",
    "CS-12": "Las brechas de seguridad con datos personales se notifican sin dilación indebida y como máximo en 48 horas.",
    "SLA-2": "Créditos por incumplimiento de disponibilidad: 10 %, 25 % o 50 % de la cuota; se solicitan en 30 días y no se abonan en efectivo.",
    "SLA-4": "Tiempos de primera respuesta por prioridad y plan; no hay garantía de tiempo de resolución.",
    "NINGUNA": "Ninguna norma aplicable.",
}

# --- Etapa 1: extracción ---
ESQUEMA_ETAPA1 = {
    "type": "object", "additionalProperties": False,
    "required": ["version", "resumen", "categoria", "prioridad", "datos", "fragmentos_fuente", "estado"],
    "properties": {
        "version": {"type": "string", "enum": ["extraccion-v1.0"]},
        "resumen": {"type": "string", "minLength": 5, "maxLength": 300},
        "categoria": {"type": "string", "enum": CATEGORIAS},
        "prioridad": {"type": "string", "enum": ["P1", "P2", "P3", "P4"]},
        "datos": {"type": "object", "additionalProperties": False,
                  "required": ["importe_eur", "factura", "codigo_error"],
                  "properties": {"importe_eur": {"type": ["number", "null"], "minimum": 0},
                                 "factura": {"type": ["string", "null"]},
                                 "codigo_error": {"type": ["string", "null"]}}},
        "fragmentos_fuente": {"type": "array", "items": {"type": "string"}},
        "estado": {"type": "string", "enum": ["ok", "revisar"]},
    },
}

# --- Etapa 2: análisis ---
ESQUEMA_ETAPA2 = {
    "type": "object", "additionalProperties": False,
    "required": ["version", "accion", "norma", "justificacion"],
    "properties": {
        "version": {"type": "string", "enum": ["analisis-v1.0"]},
        "accion": {"type": "string", "enum": ACCIONES},
        "norma": {"type": "string", "enum": list(NORMAS)},
        "justificacion": {"type": "string", "minLength": 10, "maxLength": 400},
    },
}

# --- Etapa 3: respuesta (texto libre con límites) ---
PALABRAS_MIN, PALABRAS_MAX = 60, 160
PROMESAS_PROHIBIDAS = ["garantizamos que", "en menos de", "hoy mismo", "resolveremos hoy", "le devolveremos el 100", "sin falta"]
