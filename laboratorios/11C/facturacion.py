"""Cálculo de la factura de Altanoria Copilot (versión en Python que se traduce a JavaScript en el laboratorio 11C)."""
from decimal import Decimal, ROUND_HALF_UP

PLANES = {  # plan: (precio mensual, precio anual por mes, mínimo de usuarios)
    "Starter": (Decimal("12"), Decimal("10"), 1),
    "Team": (Decimal("29"), Decimal("24"), 5),
    "Enterprise": (Decimal("59"), Decimal("49"), 50),
}
IVA = Decimal("0.21")


def _r(x):
    return Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calcular_factura_copilot(plan, usuarios, periodo="mensual", educativo=False):
    if plan not in PLANES:
        raise ValueError(f"Plan desconocido: {plan!r}")
    if periodo not in ("mensual", "anual"):
        raise ValueError(f"Periodo desconocido: {periodo!r}")
    if isinstance(usuarios, bool) or not isinstance(usuarios, int) or usuarios < 1:
        raise ValueError("usuarios debe ser un entero positivo")
    mensual, anual, minimo = PLANES[plan]
    if usuarios < minimo:
        raise ValueError(f"El plan {plan} requiere al menos {minimo} usuarios")

    if periodo == "mensual":
        base = _r(mensual * usuarios)
        volumen = Decimal("0.15") if usuarios >= 100 else Decimal("0.10") if usuarios >= 20 else Decimal("0")
    else:
        base = _r(anual * usuarios * 12)
        volumen = Decimal("0")
    porcentaje = max(volumen, Decimal("0.30") if educativo else Decimal("0"))

    descuento = _r(base * porcentaje)
    subtotal = _r(base - descuento)
    iva = _r(subtotal * IVA)
    total = _r(subtotal + iva)
    return {"base": float(base), "descuento_pct": float(porcentaje), "descuento": float(descuento),
            "subtotal": float(subtotal), "iva": float(iva), "total": float(total)}
