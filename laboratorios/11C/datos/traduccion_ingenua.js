// Traducción «ingenua» de calcular_factura_copilot: la que escribiría quien traslada línea a línea el código de Python.
// Pasa los 106 casos de aceptación, pero no es equivalente: redondea con números decimales de coma flotante.
const PLANES = {
  Starter: { mensual: 12, anual: 10, minimo: 1 },
  Team: { mensual: 29, anual: 24, minimo: 5 },
  Enterprise: { mensual: 59, anual: 49, minimo: 50 },
};

function redondear(x) {
  return Math.round(x * 100) / 100;
}

function calcularFacturaCopilot(plan, usuarios, periodo = "mensual", educativo = false) {
  if (!(plan in PLANES)) throw new Error("Plan desconocido: " + plan);
  if (periodo !== "mensual" && periodo !== "anual") throw new Error("Periodo desconocido: " + periodo);
  if (typeof usuarios !== "number" || !Number.isInteger(usuarios) || usuarios < 1) throw new Error("usuarios debe ser un entero positivo");
  const { mensual, anual, minimo } = PLANES[plan];
  if (usuarios < minimo) throw new Error("El plan " + plan + " requiere al menos " + minimo + " usuarios");

  let base, volumen;
  if (periodo === "mensual") {
    base = redondear(mensual * usuarios);
    volumen = usuarios >= 100 ? 0.15 : usuarios >= 20 ? 0.1 : 0;
  } else {
    base = redondear(anual * usuarios * 12);
    volumen = 0;
  }
  const porcentaje = Math.max(volumen, educativo ? 0.3 : 0);

  const descuento = redondear(base * porcentaje);
  const subtotal = redondear(base - descuento);
  const iva = redondear(subtotal * 0.21);
  const total = redondear(subtotal + iva);
  return { base, descuento_pct: porcentaje, descuento, subtotal, iva, total };
}
