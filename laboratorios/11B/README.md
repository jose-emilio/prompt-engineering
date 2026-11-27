[← Laboratorios](../README.md) · [Módulo 11](../../modulos/11-desarrollo-de-software/README.md) · [← 11A](../11A/README.md) · [11C →](../11C/README.md)

# Laboratorio 11B · Depurar con evidencia y revisar código sin delegar el criterio

Módulo 11 · Prompt Engineering aplicado al desarrollo de software · Duración estimada: 60 minutos · Se hace con un chat o con código

| De un vistazo | |
|---|---|
| Qué vas a hacer | Corregir un módulo con cinco defectos aportando evidencia al asistente y revisar el código sin delegar el criterio. |
| Conviene haber hecho antes | Nada: se puede hacer en cualquier orden |
| Qué hace falta | Un chat con un asistente de IA y la hoja de cálculo del laboratorio. Para el camino con código, además, Python 3.9 o superior y acceso a un modelo (por API o local). |
| Cómo seguirlo | Camino con chat: seguir los pasos tal cual y saltar los bloques «Con código». Camino con código: hacer también esos bloques, que se abren pulsando su título. |
| Si algo no sale | [Qué hacer si algo falla](../comun/si-algo-falla.md) |

Hoja de ruta:

- Paso 1 · Leer antes de preguntar (8 min)
- Paso 2 · Reproducir los fallos (5 min)
- Paso 3 · Pedir ayuda con un prompt de depuración (17 min)
- Paso 4 · Evaluar cada propuesta antes de aceptarla (10 min)
- Paso 5 · Aplicar los cambios y verificar (5 min)
- Paso 6 · Buscar defectos adicionales (7 min)
- Paso 7 · Probar un parche a ciegas (4 min)
- Paso 8 · Redactar el informe (4 min)

<details>
<summary>Secciones del módulo relacionadas (10)</summary>

- [§2.1 Explicación de código: comprender código existente](../../modulos/11-desarrollo-de-software/02-analisis-y-depuracion.md#21-explicación-de-código-comprender-código-existente)
- [§2.4 Depuración: aportar evidencia del fallo](../../modulos/11-desarrollo-de-software/02-analisis-y-depuracion.md#24-depuración-aportar-evidencia-del-fallo)
- [§2.5 Trazas y excepciones: interpretar evidencia](../../modulos/11-desarrollo-de-software/02-analisis-y-depuracion.md#25-trazas-y-excepciones-interpretar-evidencia)
- [§2.6 Validar correcciones: no aceptar parches sin pruebas](../../modulos/11-desarrollo-de-software/02-analisis-y-depuracion.md#26-validar-correcciones-no-aceptar-parches-sin-pruebas)
- [§2.7 Refactorización: mejorar estructura preservando comportamiento](../../modulos/11-desarrollo-de-software/02-analisis-y-depuracion.md#27-refactorización-mejorar-estructura-preservando-comportamiento)
- [§3.7 Revisión de código: evaluar con criterios explícitos](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#37-revisión-de-código-evaluar-con-criterios-explícitos)
- [§3.8 Seguridad del código generado: reconocer riesgos](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#38-seguridad-del-código-generado-reconocer-riesgos)
- [§3.9 Regla fundamental: no confiar en código sin ejecutar](../../modulos/11-desarrollo-de-software/03-traduccion-pruebas-y-seguridad.md#39-regla-fundamental-no-confiar-en-código-sin-ejecutar)
- [§4.1 Prompt de debugging: integrar contexto y evidencia](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#41-prompt-de-debugging-integrar-contexto-y-evidencia)
- [§4.9 Errores frecuentes: consolidar prácticas seguras](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#49-errores-frecuentes-consolidar-prácticas-seguras)

</details>

## Justificación del laboratorio

El módulo de gestión de licencias de Altanoria Copilot entra en producción la semana próxima, y QA y Seguridad han reportado problemas: una excepción inesperada, un fallo de lógica y dos defectos de seguridad. Corregirlos con ayuda de un asistente de IA es rápido, pero tiene una trampa. Un asistente propone parches con la misma seguridad cuando acierta que cuando no, y un parche que arregla un síntoma puede abrir un agujero nuevo o romper otro caso.

La habilidad que se practica aquí no es escribir código, sino dirigir la corrección sin delegar el criterio: leer antes de preguntar, reproducir el fallo, pedir ayuda aportando evidencia (el comportamiento esperado, el observado y la traza), evaluar cada propuesta con una lista de comprobación, aplicar los cambios de uno en uno comprobando que no se rompe nada y dejar constancia de cada decisión, incluidos los parches rechazados. Se compara además qué pasa cuando se pide ayuda con evidencia y cuando se pide a ciegas («revisa este método»).

Al final se tiene un informe con los defectos, su causa raíz, el parche, la prueba que lo demuestra, lo que se rechazó y por qué, y lecciones sobre cómo pedir ayuda.

## Objetivos

Corregir un módulo real con cinco defectos (dos de lógica, uno de gestión de excepciones y dos de seguridad) usando un asistente de IA, pero sin delegarle el criterio: aportar evidencia al pedir ayuda, evaluar cada propuesta, rechazar las incorrectas, verificar con pruebas y finalmente hacer una revisión de código con criterios explícitos.

Al terminar el laboratorio se habrá conseguido:

- Construir un prompt de depuración: contexto, código, comportamiento esperado y observado, traza y qué se ha probado.
- Interpretar una traza o un informe de QA y relacionarlos con el código.
- Evaluar parches propuestos: ¿corrige la causa o el síntoma?, ¿rompe algo?, ¿cambia la API?
- Reconocer riesgos de seguridad habituales: inyección SQL, registro de secretos, comparación no segura de tokens.
- Usar el modelo como revisor con una lista de criterios, y contrastar con una revisión propia.
- Aplicar la regla: **no confiar en código sin ejecutar**.

Conceptos que se usan:

- **Depuración con evidencia**. Un prompt como «esto falla» no permite diagnosticar. Una buena petición incluye el código relevante, la entrada, el resultado esperado y el obtenido, la traza completa y lo ya probado.
- **Causa raíz y síntoma**. Un parche que silencia el error (capturar la excepción y devolver `None`) puede ocultar la causa. Hay que distinguir qué falla y por qué.
- **Seguridad del código generado**. Los modelos suelen producir código funcional pero con vulnerabilidades de uso común: concatenar entradas en consultas SQL, registrar secretos, validar poco. Se revisa siempre.
- **Regresión**. Cada corrección debe demostrarse con una prueba que fallaba y pasa, sin romper las que ya pasaban.

## Recursos necesarios

> Sin acceso a una API: Pedir las correcciones en un chat; las pruebas `unittest` se ejecutan en local sin API. Véase la [guía para trabajar sin API](../comun/sin-api.md).

- Un asistente de chat y, para ejecutar las pruebas del módulo en el camino con código, Python 3.9 o superior (solo biblioteca estándar; no hace falta API).
- Carpeta [`codigo/`](codigo/):
  - [`gestor_licencias.py`](codigo/gestor_licencias.py): gestor de licencias de Altanoria Copilot (SQLite en memoria), con defectos a propósito.
  - [`test_gestor_licencias.py`](codigo/test_gestor_licencias.py): 10 pruebas `unittest`; 5 pasan y 5 fallan al empezar.
  - [`codigo/trazas/`](codigo/trazas/): una traza de excepción, un informe de QA y un informe de Seguridad.
- Hoja de cálculo: [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), con los métodos, el registro de cada defecto y de la decisión sobre cada propuesta, las diez pruebas, la revisión de defectos adicionales y los datos del informe.

Ejecutar las pruebas desde la carpeta `codigo/`:

```bash
python -m unittest -v test_gestor_licencias
```

Antes de empezar, conviene abrir la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), donde ir anotando lo que cada paso pide.

Guías comunes: [cómo copiar un fichero del repositorio](../comun/README.md#cómo-copiar-un-fichero-del-repositorio); [preparar el entorno para el camino con código](../comun/README.md#preparar-el-entorno-para-el-camino-con-código); [qué hacer si algo falla](../comun/si-algo-falla.md). Cada script explica sus opciones con `python <script> --help`.

## Pasos de ejecución

Los pasos se hacen en orden. Camino con código: se ejecutan las pruebas del módulo en el propio ordenador (solo hace falta Python 3.9 o superior, sin instalar nada) y se pide la ayuda a un chat. Camino con chat: se usan los cinco defectos descritos en lenguaje llano y se evalúan las propuestas del asistente sin ejecutar nada.

### Paso 1 · Leer antes de preguntar (8 minutos)
1. Abrir la carpeta [`codigo/`](codigo/). El módulo es [`gestor_licencias.py`](codigo/gestor_licencias.py): un gestor de licencias que guarda los datos en una base de datos SQLite en memoria y que contiene defectos a propósito. Hay tres trazas en [`codigo/trazas/`](codigo/trazas/): una traza de excepción, un informe de QA y un informe de Seguridad.
2. Leer el módulo y las trazas antes de usar el asistente. En la hoja de cálculo [`datos/hoja_de_resultados.xlsx`](datos/hoja_de_resultados.xlsx), la pestaña «Defectos» ya trae los cinco síntomas. Escribir en el documento de texto, para cada uno, la hipótesis de dónde está el fallo y qué prueba lo demostraría (no se anota en la hoja).

Camino con chat: leer en su lugar los cinco síntomas de [`datos/muestra_chat.md`](datos/muestra_chat.md), descritos en lenguaje llano (por ejemplo, «una licencia que caduca hoy figura como caducada el mismo día»), y escribir una hipótesis por cada uno en el documento de texto.

Comprobación: el documento de texto tiene una hipótesis por defecto, escrita antes de consultar al asistente.

### Paso 2 · Reproducir los fallos (5 minutos)
Camino con chat: para cada uno de los cinco síntomas de la muestra, pensar qué prueba fallaría y cuál sería su resultado esperado (se anota en el documento de texto).

<details>
<summary>Con código: ejecutar las pruebas y reproducir los fallos</summary>

Abrir una terminal en la carpeta `laboratorios/11B/codigo` y ejecutar:

```bash
python -m unittest -v test_gestor_licencias
```

Deben fallar exactamente cinco pruebas de las diez. Marcar en la pestaña «Pruebas» cuáles pasan al empezar y elegir en la pestaña «Defectos» la prueba que falla de cada defecto.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: la pestaña «Pruebas» cuenta cinco pruebas que pasan al empezar (con código), o los cinco defectos tienen su síntoma leído (con chat).

### Paso 3 · Pedir ayuda con un prompt de depuración (17 minutos)
Para cada defecto (en esta versión corta, tres de ellos, los que se prefieran), redactar un prompt con esta estructura, aportando la evidencia, y usarlo con el asistente en una conversación nueva:

````text
Contexto: módulo de gestión de licencias en Python 3.9 (sqlite3, sin dependencias externas).
Código relevante:
```python
{pegar el método}
```
Comportamiento esperado: {qué debería ocurrir}
Comportamiento observado: {qué ocurre} + traza o salida de la prueba
Restricciones: no cambiar la API pública; no añadir dependencias; cambio mínimo; no modificar las pruebas.
Pide: (1) causa raíz, (2) parche mínimo en formato diff, (3) una prueba que lo demuestre.
````

Camino con código: el comportamiento observado es el mensaje de la prueba que falla (copiarlo de la salida del paso anterior). Camino con chat: pegar el módulo completo y el síntoma en lenguaje llano. Marcar en la pestaña «Defectos» si se le pidió con evidencia (la traza). La causa raíz y el parche que propone el asistente se quedan en el chat.

Comprobación: hay una propuesta del asistente por defecto, con causa raíz y parche, y la pestaña «Defectos» indica si se pidió con evidencia.

### Paso 4 · Evaluar cada propuesta antes de aceptarla (10 minutos)
Para cada propuesta, responder a las cinco preguntas de esta lista antes de aplicarla:

```text
1. ¿Corrige la causa raíz o solo el síntoma?
2. ¿Cambia la API pública o el comportamiento de otros casos?
3. ¿Introduce un problema nuevo?
4. ¿Es el cambio mínimo?
5. ¿Hay una prueba que lo cubra?
```

Decidir si se acepta, se rechaza o se pide un cambio, y anotarlo en la columna «Decisión» de la pestaña «Defectos» (el motivo se escribe en el informe). Debe quedar documentado al menos un rechazo: si el asistente acierta siempre, probar a pedirle una corrección sin aportar la traza y comparar.

Después, mostrar las columnas «Causa real» y «Corrección real» (botón «+») y contestar si la causa y el parche propuestos coinciden con los reales.

Comprobación: cada propuesta tiene una decisión (aceptar, rechazar o cambiar); la hoja indica si hay al menos un rechazo documentado y cuántas causas y parches coinciden con los reales.

### Paso 5 · Aplicar los cambios y verificar (5 minutos)
Camino con chat: para cada propuesta aceptada, elegir en la pestaña «Defectos» la prueba que demostraría que funciona y contestar si podría romper otro caso.

<details>
<summary>Con código: aplicar los cambios y ejecutar las pruebas</summary>

Aplicar los cambios de uno en uno en [`gestor_licencias.py`](codigo/gestor_licencias.py). Después de cada uno, abrir una terminal en la carpeta `laboratorios/11B/codigo` y ejecutar todas las pruebas:

```bash
python -m unittest -v test_gestor_licencias
```

El defecto corregido debe pasar y no debe romperse ninguna otra. Anotar en la pestaña «Pruebas» cuáles pasan después de cada corrección; la hoja cuenta cuántas de las diez pasan y marca las regresiones.

Si el script falla, la respuesta llega vacía o se agota el tiempo de espera, véase [Si algo falla](../comun/si-algo-falla.md).

</details>

Comprobación: la hoja muestra cuántas pruebas pasan (con código) o, sin código, cada corrección tiene su prueba elegida.

### Paso 6 · Buscar defectos adicionales (7 minutos)
Una vez corregidos los defectos conocidos, pedir al asistente una revisión de código con estos criterios y contrastarla con la revisión propia:

````text
Revisa este módulo Python con estos criterios y lista solo hallazgos concretos, cada uno con la línea afectada y una corrección mínima:
- Validación de entradas y manejo de None.
- Gestión de errores y mensajes.
- Seguridad (inyección, secretos, comparaciones de tokens, registro de datos personales).
- Concurrencia y consistencia de la base de datos.
- Legibilidad y documentación.
No propongas cambios de estilo ni cambies la API pública.

```python
{pegar gestor_licencias.py}
```
````

Anotar cada hallazgo en la pestaña «Revisión» (el método, si es real o falsa alarma, y quién lo encuentra); la hoja cuenta cuántos son reales, cuántos son falsas alarmas y cuántos aporta uno y no el otro.

Comprobación: la pestaña «Revisión» muestra tres cifras: hallazgos reales, falsas alarmas y hallazgos que solo ha encontrado uno de los dos revisores.

### Paso 7 · Probar un parche a ciegas (4 minutos)
Para uno de los defectos de seguridad, pedir al asistente que lo corrija sin decirle cuál es el problema («revisa este método»). Responder en la pestaña «A ciegas»: ¿lo encuentra?, ¿propone un parche correcto?, ¿rompe alguna prueba?

Comprobación: la pestaña «A ciegas» indica si el asistente encuentra el defecto sin ayuda.

### Paso 8 · Redactar el informe (4 minutos)
Escribir un informe en el documento de texto: los defectos, la causa raíz de cada uno, el parche aplicado y la prueba asociada, las propuestas rechazadas y por qué, y las lecciones sobre cómo pedir ayuda.

Comprobación: el informe incluye al menos un parche rechazado con su motivo.

## Conclusiones

### Qué se ha conseguido

Se han corregido defectos reales de un módulo con ayuda de un asistente sin delegar el criterio. Lo que se aprende es el método: leer antes de preguntar, reproducir el fallo, pedir ayuda con evidencia, evaluar cada propuesta con una lista, aplicar un cambio cada vez comprobando todas las pruebas y registrar también lo rechazado. Se ha visto además que una petición a ciegas («revisa este método») produce parches menos fiables, y que los defectos de seguridad (inyección, secretos, comparaciones de tokens) no los detectan las pruebas funcionales: hay que buscarlos con una revisión dirigida.

### Preguntas de reflexión

Cada pregunta incluye su respuesta, plegada: conviene intentar responder antes de abrirla.

1. ¿Qué diferencia hubo entre pedir ayuda con evidencia y sin ella?

   <details>
   <summary>Respuesta</summary>

   Con evidencia los parches son más mínimos y precisos; sin ella aumenta el riesgo de cambios innecesarios y de soluciones al síntoma.

   </details>

2. ¿Algún parche del asistente «silenciaba» el síntoma en lugar de corregir la causa?

   <details>
   <summary>Respuesta</summary>

   Es frecuente en el defecto 3 (capturar la excepción) y en el 5 (enmascarar el token).

   </details>

3. ¿Por qué un fallo de seguridad pasa desapercibido con pruebas funcionales?

   <details>
   <summary>Respuesta</summary>

   Porque las pruebas funcionales comprueban lo que el código hace con entradas normales; un ataque necesita entradas maliciosas que no se piensan al escribir la prueba.

   </details>

4. ¿Qué defectos encontró la revisión del asistente que no estaban en las trazas? ¿Y cuáles se le escaparon?

   <details>
   <summary>Respuesta</summary>

   Suele encontrar el secreto en el código y la falta de validaciones; puede pasar por alto problemas de lógica de negocio que requieren conocer el dominio.

   </details>

5. ¿Qué cambios en el proceso de desarrollo reducirían estos defectos (revisión por pares, análisis estático, pruebas de seguridad)?

   <details>
   <summary>Respuesta</summary>

   Revisión por pares, análisis estático, pruebas de seguridad en la integración continua y formación en codificación segura.

   </details>

### Autoevaluación

- [ ] Se leyó el código y se formularon hipótesis antes de preguntar.
- [ ] Cada prompt de depuración incluye código, esperado, observado, traza y restricciones.
- [ ] Se ejecutaron las diez pruebas tras cada cambio.
- [ ] Hay una propuesta del asistente rechazada y justificada.
- [ ] No se cambió la API pública.
- [ ] Los problemas de seguridad se corrigen con técnicas adecuadas (consultas parametrizadas, no registrar secretos, comparación en tiempo constante).
- [ ] El informe describe la causa raíz de cada defecto y no solo el parche.

### Errores típicos

- Aceptar un parche porque “parece correcto” sin ejecutar las pruebas.
- Corregir varios defectos a la vez.
- Modificar las pruebas para que pasen.
- Ocultar el síntoma con un `try/except` genérico.
- Dejar secretos en el código o en los registros.

### Solución de referencia

Se consulta después de haber intentado el laboratorio.

<details>
<summary>Abrir la solución de referencia</summary>

### Qué hace cada método (Paso 1)

| Método | Qué hace | Contrato que declara |
|---|---|---|
| `crear_licencia` | Inserta una licencia con cliente, plan, plazas y fecha de caducidad, y devuelve su id | `caduca` es el último día de validez |
| `licencia_de_cliente` | Devuelve el id de la licencia de un cliente | `None` si no tiene |
| `dias_restantes` | Calcula los días que quedan hasta la caducidad | 0 si caduca hoy (aún vigente) |
| `esta_vigente` | Dice si la licencia es válida en una fecha | Válida hasta el final del día de caducidad, incluido |
| `plazas_libres` | Plazas de la licencia menos las asignadas | — |
| `asignar_usuario` | Asigna una plaza a un usuario | `True` si se asignó; `False` si no hay plazas o ya la tenía |
| `buscar_usuarios` | Lista los usuarios asignados a las licencias de un cliente | — |
| `autenticar_admin` | Comprueba un token de administración | — |

Los tres primeros defectos son métodos que no cumplen su contrato (vigencia del último día, plazas a 0 y cliente sin licencia) y los dos de seguridad están en los métodos que manejan datos sensibles (la búsqueda con una consulta construida con texto y la autenticación): una hipótesis razonable antes de preguntar al asistente es comparar lo que dice el comentario con lo que hace el código.

### Los cinco defectos

| # | Tipo | Dónde | Causa raíz | Prueba que falla | Corrección |
|---|---|---|---|---|---|
| 1 | Lógica | `esta_vigente` | Usa `> 0` cuando el último día de validez ya es 0 días restantes; una licencia que caduca hoy se considera caducada | `test_vigente_el_ultimo_dia` | `>= 0` |
| 2 | Lógica | `asignar_usuario` | Compara `plazas_libres < 0`; con 0 libres deja asignar de más | `test_no_asigna_si_no_hay_plazas` | `<= 0` |
| 3 | Excepción | `licencia_de_cliente` | `filas[0][0]` falla (IndexError) si el cliente no tiene licencia; el contrato dice «devuelve None si no tiene» | `test_cliente_sin_licencia` | Usar `fetchone()` y devolver `None` si no hay fila |
| 4 | Seguridad | `buscar_usuarios` | Concatena el nombre del cliente en la consulta SQL: inyección SQL (`x' OR '1'='1` devuelve usuarios de otros clientes); además registra la consulta completa | `test_inyeccion_sql` | Consulta parametrizada con `?` |
| 5 | Seguridad | `autenticar_admin` | Registra el token recibido y el esperado en el log; compara con `==` (vulnerable a ataques de temporización) | `test_el_log_no_expone_el_token` | No registrar secretos; `hmac.compare_digest` |

### Módulo corregido (referencia)

```python
"""Gestor de licencias de Altanoria Copilot (módulo de práctica).

CONTIENE ERRORES a propósito. El laboratorio consiste en encontrarlos y
corregirlos con ayuda de un LLM, sin delegar el criterio.
"""
import datetime
import hmac
import logging
import sqlite3

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger("licencias")

TOKEN_ADMIN = "nb_admin_9f3c1a77e2"  # NOTA: en un sistema real vendría de una variable de entorno o un gestor de secretos


class GestorLicencias:
    def __init__(self, ruta=":memory:"):
        self.con = sqlite3.connect(ruta)
        self.con.execute(
            "CREATE TABLE IF NOT EXISTS licencias ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, cliente TEXT NOT NULL, "
            "plan TEXT NOT NULL, plazas INTEGER NOT NULL, caduca TEXT NOT NULL)"
        )
        self.con.execute(
            "CREATE TABLE IF NOT EXISTS asignaciones ("
            "licencia_id INTEGER NOT NULL, usuario TEXT NOT NULL)"
        )

    # ---------- altas y consultas ----------
    def crear_licencia(self, cliente, plan, plazas, caduca):
        """`caduca` es una fecha ISO (AAAA-MM-DD): el último día de validez."""
        cur = self.con.execute(
            "INSERT INTO licencias (cliente, plan, plazas, caduca) VALUES (?, ?, ?, ?)",
            (cliente, plan, plazas, caduca),
        )
        self.con.commit()
        return cur.lastrowid

    def licencia_de_cliente(self, cliente):
        """Devuelve el id de la licencia del cliente o None si no tiene."""
        fila = self.con.execute(
            "SELECT id FROM licencias WHERE cliente = ? ORDER BY id LIMIT 1", (cliente,)
        ).fetchone()
        return fila[0] if fila else None

    # ---------- vigencia ----------
    def dias_restantes(self, licencia_id, hoy=None):
        """Días que quedan hasta la caducidad. 0 si caduca hoy (aún vigente)."""
        hoy = hoy or datetime.date.today()
        caduca = self.con.execute(
            "SELECT caduca FROM licencias WHERE id = ?", (licencia_id,)
        ).fetchone()[0]
        return (datetime.date.fromisoformat(caduca) - hoy).days

    def esta_vigente(self, licencia_id, hoy=None):
        """Una licencia es válida hasta el final del día de caducidad (incluido)."""
        return self.dias_restantes(licencia_id, hoy) >= 0

    # ---------- asignaciones ----------
    def plazas_libres(self, licencia_id):
        plazas = self.con.execute(
            "SELECT plazas FROM licencias WHERE id = ?", (licencia_id,)
        ).fetchone()[0]
        usadas = self.con.execute(
            "SELECT COUNT(*) FROM asignaciones WHERE licencia_id = ?", (licencia_id,)
        ).fetchone()[0]
        return plazas - usadas

    def asignar_usuario(self, licencia_id, usuario):
        """Asigna una plaza. Devuelve True si se asignó; False si no hay plazas
        o el usuario ya la tenía."""
        existe = self.con.execute(
            "SELECT 1 FROM asignaciones WHERE licencia_id = ? AND usuario = ?",
            (licencia_id, usuario),
        ).fetchone()
        if existe:
            return False
        if self.plazas_libres(licencia_id) <= 0:
            return False
        self.con.execute(
            "INSERT INTO asignaciones (licencia_id, usuario) VALUES (?, ?)",
            (licencia_id, usuario),
        )
        self.con.commit()
        return True

    # ---------- búsqueda y administración ----------
    def buscar_usuarios(self, cliente):
        """Lista los usuarios asignados a las licencias de un cliente."""
        filas = self.con.execute(
            "SELECT a.usuario FROM asignaciones a JOIN licencias l "
            "ON a.licencia_id = l.id WHERE l.cliente = ?",
            (cliente,),
        ).fetchall()
        return [f[0] for f in filas]

    def autenticar_admin(self, token):
        correcto = hmac.compare_digest(str(token), TOKEN_ADMIN)
        log.info("Intento de autenticación de administrador: %s", "correcto" if correcto else "fallido")
        return correcto
```

Tras las correcciones, `python -m unittest -v test_gestor_licencias` debe mostrar 10 pruebas correctas.

### Parches del asistente que conviene rechazar (ejemplos habituales)

| Defecto | Propuesta problemática | Por qué rechazarla |
|---|---|---|
| 3 (IndexError) | Envolver en `try/except IndexError: return None` | Funciona, pero captura una excepción en lugar de evitarla; puede ocultar otros errores. Es aceptable solo si se justifica; el parche preferible es usar `fetchone()`. |
| 4 (inyección) | «Escapar» las comillas con `replace("'", "''")` | Mitigación frágil; la solución correcta son consultas parametrizadas. |
| 5 (token) | Registrar solo los 4 primeros caracteres | Sigue exponiendo parte del secreto; la comprobación de tiempo no cambia. |
| 1 y 2 | Cambiar la prueba en lugar del código | Cambia el contrato para que el test pase. |
| 4 | Cambiar la firma para recibir un id de cliente | Rompe la API pública. |

### Cómo cambia la calidad de la ayuda con la evidencia

- Sin traza ni esperado/observado («revisa este método»): el asistente suele encontrar los defectos más conocidos (inyección SQL) pero puede proponer cambios de estilo y pasar por alto los de lógica (`> 0` frente a `>= 0`), que dependen de la intención descrita en la documentación del método.
- Con evidencia: localiza la causa en la mayoría de casos y propone parches mínimos; aun así hay que ejecutar las pruebas.

### Revisión adicional: hallazgos reales que el asistente suele aportar

- `TOKEN_ADMIN` está escrito en el código: debe venir de una variable de entorno o un gestor de secretos.
- `crear_licencia` no valida plan, plazas ni formato de fecha.
- No hay restricción de unicidad en `asignaciones` (usuario duplicado en carreras concurrentes).
- `dias_restantes` no controla que la licencia exista (`fetchone()` devuelve `None`).
- No se cierra la conexión; faltan transacciones explícitas.

Falsas alarmas habituales: sugerir cambiar SQLite por otro motor sin motivo; reportar «falta de pruebas» sin concretar.

### Resultados medidos con un modelo real

> Medición realizada el 24 de noviembre de 2026 con Gemma 4 (8 B, cuantizado Q4_K_M) en local con Ollama, con la ventana de contexto ampliada a 16.384 tokens, una sola ejecución y un script de medición propio (el laboratorio se hace por chat). Sirve como referencia de orden de magnitud; con otro modelo o en otra fecha los números cambiarán, y con conjuntos pequeños una diferencia de pocos puntos es ruido.

Con las trazas como evidencia y la salida de las pruebas, en una sola respuesta el modelo identificó cuatro de los cinco defectos y, al aplicar su módulo corregido, 8 de las 10 pruebas pasaron y 2 siguieron fallando. Detalles a revisar:

- Se dejó un defecto sin diagnosticar: el de las plazas (`asignar_usuario` compara con `< 0` y deja asignar de más cuando ya no quedan plazas libres). No lo mencionó en las causas y la prueba `test_no_asigna_si_no_hay_plazas` siguió fallando: una respuesta convincente que lista cuatro causas no garantiza que sean todas.
- Arregló el síntoma del token a medias y dejó la fuga: enmascaró el token proporcionado («Token proporcionado (oculto)»), pero siguió escribiendo en el registro el token esperado, de modo que `test_el_log_no_expone_el_token` falló. Tampoco usó `hmac.compare_digest`, así que no corrigió el riesgo de temporización.
- Corrigió bien la vigencia (`>= 0`), el cliente sin licencia (devolver `None`) y la inyección SQL (consulta parametrizada con `?`), mantuvo la API pública y no tocó las pruebas.

Por eso el laboratorio pide ejecutar las pruebas después de aplicar el parche y mirar cada línea que cambia la salida de seguridad.

</details>

### Para seguir

- Escribir pruebas adicionales para los casos de borde que no cubre el conjunto (usuario con espacios, licencias de varios clientes, plazas a 0).
- Ejecutar una herramienta de análisis estático de seguridad y comparar con la revisión del asistente.
- Pedir al asistente que refactorice el módulo para separar acceso a datos y reglas de negocio, y verificar con las mismas pruebas ([§2.7 Refactorización: mejorar estructura preservando comportamiento](../../modulos/11-desarrollo-de-software/02-analisis-y-depuracion.md#27-refactorización-mejorar-estructura-preservando-comportamiento)).
- Escribir una especificación breve de la corrección de uno de los defectos (objetivo, alcance, criterios de aceptación y definición de «hecho», [§4.7 Anatomía de una buena especificación](../../modulos/11-desarrollo-de-software/04-prompts-completos-flujo-y-cierre.md#47-anatomía-de-una-buena-especificación)) y pedir al asistente que la implemente contra ella; comparar con el resultado de pedir el cambio directamente: ¿cuál fue más fácil de revisar?

---

[← Laboratorios](../README.md) · [Módulo 11](../../modulos/11-desarrollo-de-software/README.md) · [← 11A](../11A/README.md) · [11C →](../11C/README.md)
