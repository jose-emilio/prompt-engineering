#!/usr/bin/env node
// Comprueba una traducción de calcular_factura_copilot con los 106 casos de aceptación (necesita Node.js 18 o superior).
//
//   node comprobar.js facturacion.js
//   node comprobar.js traduccion_v1.js --max 20
//   node comprobar.js facturacion.js --malla
//   node comprobar.js facturacion.js --probar Team 25 mensual false
//
// Sin argumentos comprueba facturacion.js. La función debe llamarse calcularFacturaCopilot y devolver un objeto con las claves
// base, descuento_pct, descuento, subtotal, iva y total (números). No se admiten bibliotecas: solo JavaScript estándar.
"use strict";
const fs = require("fs");
const path = require("path");
const nucleo = require("./comprobar_nucleo.js");
const CASOS = require("./datos/casos_aceptacion.js");
const MALLA = require("./datos/malla_equivalencia.js");

const argumentos = process.argv.slice(2);
if (argumentos.includes("-h") || argumentos.includes("--help")) {
  console.log(fs.readFileSync(__filename, "utf8").split("\n").filter(l => l.startsWith("//")).map(l => l.replace(/^\/\/ ?/, "")).join("\n"));
  console.log("\nOpciones:\n  --max N      número de fallos que se muestran (por defecto 10)\n  --malla      comprueba la malla de equivalencia (2.188 entradas) en lugar de los 106 casos\n  --probar P U PERIODO EDU   llama a la función con una entrada y muestra el resultado\n  -h, --help   esta ayuda");
  process.exit(0);
}
let fichero = "facturacion.js", maximo = 10, probar = null, malla = false;
for (let i = 0; i < argumentos.length; i++) {
  if (argumentos[i] === "--max") maximo = parseInt(argumentos[++i], 10);
  else if (argumentos[i] === "--malla") malla = true;
  else if (argumentos[i] === "--probar") { probar = argumentos.slice(i + 1, i + 5); break; }
  else fichero = argumentos[i];
}
let cargado;
try { cargado = nucleo.cargar(fs.readFileSync(path.resolve(fichero), "utf8"), require); }
catch (e) { console.log("No se puede comprobar " + fichero + ": " + e.message); process.exit(1); }
cargado.avisos.forEach(a => console.log("Aviso: " + a));
if (probar) {
  const [plan, usuarios, periodo, educativo] = probar;
  const u = /^-?\d+(\.\d+)?$/.test(usuarios) ? Number(usuarios) : usuarios === "true" ? true : usuarios;
  try { console.log(JSON.stringify(cargado.funcion(plan, u, periodo || "mensual", educativo === "true"), null, 2)); }
  catch (e) { console.log("Lanza un error: " + e.message); }
  process.exit(0);
}
console.log(nucleo.informe(nucleo.ejecutar(cargado.funcion, malla ? nucleo.expandirMalla(MALLA) : CASOS), maximo));
