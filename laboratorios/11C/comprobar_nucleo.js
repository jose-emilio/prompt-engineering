// Núcleo de la comprobación del laboratorio 11C: lo usan comprobar.html (navegador) y comprobar.js (Node.js).
// Carga una traducción de calcular_factura_copilot, la ejecuta con los casos de aceptación y clasifica cada fallo.
(function (raiz, fabrica) {
  if (typeof module === "object" && module.exports) module.exports = fabrica();
  else raiz.ComprobarNucleo = fabrica();
})(this, function () {
  const NOMBRES = ["calcularFacturaCopilot", "calcular_factura_copilot"];   // el primero es el que pide el laboratorio
  const CLAVES = ["base", "descuento_pct", "descuento", "subtotal", "iva", "total"];
  const TOLERANCIA = 0.005;

  // Devuelve { funcion, nombre, avisos } o lanza un Error con el motivo si el código no se puede cargar.
  function cargar(codigo, requerir) {
    const avisos = [];
    let fuente = codigo.replace(/^\s*export\s+default\s+/gm, "").replace(/^\s*export\s+/gm, "");
    if (/^\s*import\s.+from\s/m.test(fuente))
      throw new Error("El código usa `import`: el laboratorio pide un fichero sin módulos ES (usa solo JavaScript estándar).");
    const modulo = { exports: {} };
    const silencio = { log() {}, info() {}, warn() {}, error() {}, debug() {} };
    const sinBibliotecas = function (nombre) {
      if (requerir) return requerir(nombre);
      throw new Error("El código usa la biblioteca «" + nombre + "»: no hay bibliotecas, solo JavaScript estándar.");
    };
    const comprobaciones = NOMBRES.map(n => `typeof ${n} === "function" ? ${n} : undefined`).join(", ");
    let hallado;
    try {
      hallado = new Function("module", "exports", "require", "console", fuente + `\n;return [${comprobaciones}];`)(modulo, modulo.exports, sinBibliotecas, silencio);
    } catch (e) {
      throw new Error("El código no se puede cargar: " + String(e.message).split("\n")[0]);
    }
    for (let i = 0; i < NOMBRES.length; i++) {
      const f = hallado[i] || (modulo.exports && modulo.exports[NOMBRES[i]]) || (typeof modulo.exports === "function" && i === 0 ? modulo.exports : undefined);
      if (typeof f === "function") {
        if (i > 0) avisos.push("La función se llama «" + NOMBRES[i] + "» y se pedía «" + NOMBRES[0] + "».");
        return { funcion: f, nombre: NOMBRES[i], avisos };
      }
    }
    throw new Error("No se encuentra ninguna función llamada «" + NOMBRES[0] + "» en el código.");
  }

  function texto(v) { try { return typeof v === "string" ? JSON.stringify(v) : JSON.stringify(v) || String(v); } catch (e) { return String(v); } }

  function evaluar(funcion, caso) {
    const entrada = [caso.plan, caso.usuarios, caso.periodo, caso.educativo];
    let r;
    try { r = funcion(...entrada); }
    catch (e) {
      if (caso.error) return null;
      return { categoria: "error de más", detalle: "lanzó «" + (e && e.message ? e.message : e) + "» y debía devolver el cálculo" };
    }
    if (caso.error) return { categoria: "no lanza error", detalle: "debía lanzar un error y devolvió " + texto(r) };
    if (r === null || typeof r !== "object") return { categoria: "formato", detalle: "no devuelve un objeto (devuelve " + texto(r) + ")" };
    let mayor = 0, primero = null;
    for (const k of CLAVES) {
      if (!(k in r)) return { categoria: "formato", detalle: "falta la clave «" + k + "»" };
      if (typeof r[k] !== "number") return { categoria: "formato", detalle: "«" + k + "» es " + (typeof r[k] === "string" ? "un texto (" + texto(r[k]) + ")" : "de tipo " + typeof r[k]) + " y debe ser un número" };
      const dif = Math.abs(r[k] - caso.esperado[k]);
      if (!(dif <= TOLERANCIA)) { // también atrapa NaN
        mayor = Math.max(mayor, isNaN(dif) ? Infinity : dif);
        primero = primero || k;
      }
    }
    if (mayor === 0) return null;
    const k = primero; const dif = r[k] - caso.esperado[k];
    return {
      categoria: mayor <= 0.011 ? "redondeo" : "regla de negocio",
      detalle: "«" + k + "»: esperado " + caso.esperado[k] + " y obtenido " + r[k] + " (diferencia " + (Math.round(dif * 100) / 100) + ")"
    };
  }

  function ejecutar(funcion, casos) {
    const fallos = [];
    for (const caso of casos) {
      const f = evaluar(funcion, caso);
      if (f) fallos.push(Object.assign({ linea: caso.linea, entrada: [caso.plan, caso.usuarios, caso.periodo, caso.educativo] }, f));
    }
    const por_categoria = {};
    for (const f of fallos) por_categoria[f.categoria] = (por_categoria[f.categoria] || 0) + 1;
    return { total: casos.length, pasan: casos.length - fallos.length, fallos, por_categoria };
  }

  // Convierte la malla compacta (datos/malla_equivalencia.js) en casos como los de casos_aceptacion.js.
  function expandirMalla(malla) {
    return malla.filas.map(function (f, i) {
      return { linea: "m" + (i + 1), plan: malla.planes[f[0]], usuarios: f[1], periodo: malla.periodos[f[2]], educativo: f[3] === 1,
               esperado: { base: f[4], descuento_pct: f[5], descuento: f[6], subtotal: f[7], iva: f[8], total: f[9] } };
    });
  }

  function etiqueta(linea) { return typeof linea === "number" ? "Línea " + linea : "Malla " + linea.slice(1); }

  function descripcion(entrada) { return "(" + entrada.map(texto).join(", ") + ")"; }

  function informe(resultado, maximo) {
    maximo = maximo || 10;
    const l = ["Casos que pasan: " + resultado.pasan + "/" + resultado.total];
    const cats = Object.keys(resultado.por_categoria);
    if (cats.length) l.push("Fallos por categoría: " + cats.map(c => c + " " + resultado.por_categoria[c]).join(", "));
    resultado.fallos.slice(0, maximo).forEach(f => l.push("  " + etiqueta(f.linea) + " " + descripcion(f.entrada) + " · " + f.categoria + ": " + f.detalle));
    if (resultado.fallos.length > maximo) l.push("  … y " + (resultado.fallos.length - maximo) + " fallos más");
    return l.join("\n");
  }

  return { cargar, ejecutar, informe, descripcion, expandirMalla, NOMBRES, CLAVES };
});
