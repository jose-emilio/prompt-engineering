[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-inyeccion-de-prompts-y-jailbreaking.md)

# 1 · Amenazas y privacidad

*Módulo 09: Seguridad, privacidad y uso responsable*

## 1.1 Modelo de amenazas en sistemas LLM

Un sistema basado en LLM expone múltiples superficies de ataque. Comprender cada una es el primer paso para diseñar controles eficaces. Ningún componente debe considerarse inherentemente seguro.

- **Entradas del usuario**: Mensajes directos y prompts de los usuarios finales.
- **Documentos y datos recuperados**: Contenido externo obtenido mediante RAG o búsqueda.
- **Memoria y registros**: Historial de conversación y contexto almacenado.

**Sistema basado en LLM**

- **Instrucciones del sistema y de la aplicación**: Configuración y reglas inyectadas por el desarrollador.
- **Herramientas y conectores**: APIs, funciones e integraciones que el modelo puede invocar.
- **Salidas y acciones externas**: Texto generado y efectos posteriores.

1

2

3

4

5

6

Cada superficie requiere controles específicos. La combinación de herramientas y recuperación documental representa el mayor riesgo compuesto.

**Explicación**

Un sistema basado en un LLM tiene varias superficies de ataque y ningún componente debe considerarse inherentemente seguro. Son seis: las entradas del usuario, las instrucciones del sistema y de la aplicación, los documentos y datos recuperados, las herramientas y conectores, la memoria y los registros y las salidas y acciones externas.

Para cada superficie se pregunta quién puede introducir contenido, qué podría hacer ese contenido y qué control lo impediría. Cada una requiere controles específicos, y la combinación de herramientas y recuperación documental representa el mayor riesgo compuesto: un texto malicioso incluido en un documento puede convertirse en una acción real cuando el sistema, además, puede actuar.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 09B · Red team de un asistente de buzón](../../laboratorios/09B/README.md)
<!-- /labs-seccion -->

---

## 1.2 Privacidad y datos personales

Antes de construir cualquier prompt, es fundamental clasificar la información disponible y determinar qué categorías pueden incluirse legítimamente en el contexto del modelo.

**Categorías protegidas**

- PII: nombre, DNI, correo, teléfono, dirección
- Datos sensibles: salud, origen étnico, ideología, biometría
- Datos corporativos: clientes, empleados, contratos
- Credenciales: contraseñas, tokens, claves de API

**Principios aplicables**

- Minimización: usar solo los datos estrictamente necesarios
- Finalidad: no reutilizar datos para propósitos distintos
- Proporcionalidad: el riesgo asumido debe justificarse
- Base legal: verificar legitimidad del tratamiento (RGPD) y evaluar su impacto (EIPD) si procede

**Explicación**

Antes de construir un prompt hay que clasificar la información disponible y decidir qué categorías pueden incluirse legítimamente. Las categorías protegidas son los datos personales identificativos (nombre, documento, correo, teléfono, dirección), los datos sensibles (salud, origen étnico, ideología, biometría), los datos corporativos (clientes, empleados, contratos) y las credenciales (contraseñas, tokens, claves de API).

Cuatro principios orientan el tratamiento: **minimización** (solo lo estrictamente necesario), finalidad (no reutilizar datos para otros propósitos), proporcionalidad (el riesgo asumido debe justificarse) y base legal (verificar la legitimidad del tratamiento según el RGPD y, si procede, hacer una evaluación de impacto). Los modelos de lenguaje añaden la facilidad de enviar grandes cantidades de datos a un servicio externo con un simple copiar y pegar, a menudo sin plena conciencia de ello.

<!-- labs-seccion -->
> **Para practicar esta sección:** [Laboratorio 09A · Minimizar y anonimizar antes de enviar datos a un modelo](../../laboratorios/09A/README.md)
<!-- /labs-seccion -->

---

## 1.3 Qué no introducir en prompts

El texto que se envía a un modelo puede quedar registrado, ser analizado para mejoras del servicio o estar disponible para terceros según las condiciones del proveedor. La prudencia en la selección de datos es una responsabilidad profesional.

**🔴 Nunca incluir**

- Contraseñas, claves privadas y tokens de acceso
- Datos personales innecesarios para la tarea
- Información corporativa clasificada sin autorización

**🟡 Evaluar con cautela**

- Nombres propios y datos de contacto no esenciales
- Fragmentos de contratos o acuerdos de confidencialidad
- Datos de clientes aunque estén semiagregados

**🟢 Alternativas seguras**

- Usar datos sintéticos o conjuntos de ejemplo anonimizados
- Revisar políticas y condiciones de uso del servicio LLM
- Validar con el equipo legal o de compliance si hay duda

**Explicación**

El texto que se envía a un modelo puede quedar registrado, ser analizado para mejorar el servicio o estar disponible para terceros según las condiciones del proveedor, y la prudencia en la selección de datos es una responsabilidad profesional. Un código de tres niveles lo organiza: en rojo, lo que nunca debe incluirse (contraseñas, claves, tokens, datos personales innecesarios, información corporativa clasificada sin autorización); en amarillo, lo que se evalúa con cautela (nombres y datos de contacto no esenciales, fragmentos de contratos o confidencialidad, datos de clientes aunque estén semiagregados); y en verde, las alternativas seguras (datos sintéticos o anonimizados, revisar las condiciones del servicio y consultar a legal o cumplimiento ante la duda).

El destino de lo escrito depende de las condiciones del proveedor y del tipo de contrato o cuenta: algunos servicios empresariales garantizan no usar datos para entrenar y limitar la retención, y otros, en sus versiones gratuitas, pueden conservar y analizar las conversaciones. Ante la duda en el nivel amarillo, se aplica la alternativa verde.

---

## 1.4 Minimización y anonimización

Reducir la exposición de datos antes de enviarlos al modelo es la medida de privacidad más efectiva. Seudonimizar (sustituir por marcadores y guardar la tabla aparte) es reversible; anonimizar (que nadie pueda reidentificar a la persona) es irreversible y difícil de conseguir de verdad.

**Antes — Ejemplo ilustrativo ⚠️**

```text
Analiza el caso de María García, DNI 12345678X, empleada de Acme S.A., con salario de 42.000 € y diagnóstico de hipertensión desde 2021.
```

Este prompt expone PII, dato laboral y dato de salud innecesariamente.

**Después — Versión minimizada y seudonimizada ✅**

```text
Analiza el caso de un empleado (ID: EMP-091), sector tecnológico, rango salarial medio-alto, con condición crónica controlada.
```

Se preserva la utilidad del análisis. «EMP-091» es un seudónimo: la tabla que lo une a la persona se guarda aparte.

- **Aportar solo campos necesarios**: Revisar cada campo del prompt: si no es imprescindible para la tarea, eliminarlo.
- **Evaluar riesgo de reidentificación**: La combinación de datos aparentemente inocuos puede revelar identidades. Validar antes de enviar.
- **Eliminar metadatos superfluos**: Nombres de archivo, fechas y rutas de sistema pueden contener información sensible.

**Explicación**

Reducir la exposición de datos antes de enviarlos es la medida de privacidad más eficaz. El ejemplo contrasta un prompt con nombre completo, documento de identidad, empresa, salario exacto y un diagnóstico médico con fecha (que expone innecesariamente datos personales, laborales y de salud) con una versión minimizada y seudonimizada: un empleado identificado con un código, sector tecnológico, rango salarial medio-alto y una condición crónica controlada. Se conserva la utilidad del análisis sin exponer datos identificables.

Tres prácticas: aportar solo los campos necesarios, evaluar el riesgo de reidentificación (la combinación de datos aparentemente inocuos puede señalar a una persona, sobre todo en grupos pequeños) y eliminar metadatos superfluos como nombres de archivo, fechas o rutas. Conviene distinguir tres términos. Seudonimizar es sustituir los identificadores por marcadores (como el código del empleado o un [DNI_1]) y guardar aparte la correspondencia que los une a la persona: se puede revertir, así que los datos siguen siendo personales. Anonimizar es eliminar o generalizar de modo que nadie pueda volver a identificar a la persona, ni siquiera con información adicional: es irreversible y muy difícil de lograr de verdad, porque no basta con quitar el nombre; hay que valorar si el conjunto restante permite identificar a alguien. El resultado debe revisarse aunque se automatice. En el laboratorio 09A se practica la seudonimización.

---

## 1.5 Gobernanza de uso

Las organizaciones deben establecer reglas claras sobre cómo, cuándo y con qué datos se pueden utilizar herramientas de IA. Sin política explícita, cada usuario toma decisiones individualmente, multiplicando el riesgo.

| Dimensión | Permitido | Restringido | Prohibido |
|---|---|---|---|
| Datos de entrada | Datos públicos, sintéticos | Datos internos no clasificados | PII, credenciales, datos sensibles |
| Herramientas | LLMs autorizados por TI | Herramientas en evaluación | Servicios no aprobados |
| Retención | Según política de empresa | Logs de auditoría limitados | Almacenamiento sin control |
| Responsable | Usuario + área de negocio | Supervisión de compliance | Sin responsable asignado |

**Explicación**

Las organizaciones deben fijar reglas claras sobre cómo, cuándo y con qué datos se usan herramientas de IA; sin política explícita, cada usuario decide por su cuenta y se multiplica el riesgo. La tabla organiza la política en cuatro dimensiones y tres niveles: en datos de entrada, se permiten datos públicos y sintéticos, se restringen los internos no clasificados y se prohíben los personales, credenciales y sensibles; en herramientas, se permiten las autorizadas por tecnología, se restringen las que están en evaluación y se prohíben las no aprobadas; en retención, se sigue la política de la empresa, con registros de auditoría limitados y sin almacenamiento incontrolado; y en responsabilidad, el usuario y el área de negocio, con supervisión de cumplimiento y nunca sin responsable asignado.

Los tres niveles dan una regla clara para lo que está bien, una de cautela para los casos intermedios y una línea roja. El uso de servicios no aprobados (uso en la sombra) es una de las vías principales de fuga, y ofrecer alternativas autorizadas, útiles y fáciles reduce el incentivo.

---

[← Anterior](00-objetivos-del-modulo.md) · [Índice del módulo](README.md) · [Siguiente →](02-inyeccion-de-prompts-y-jailbreaking.md)
