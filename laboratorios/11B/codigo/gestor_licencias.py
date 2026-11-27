"""Gestor de licencias de Altanoria Copilot (módulo de práctica).

CONTIENE ERRORES a propósito. El laboratorio consiste en encontrarlos y
corregirlos con ayuda de un LLM, sin delegar el criterio.
"""
import datetime
import logging
import sqlite3

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
log = logging.getLogger("licencias")

TOKEN_ADMIN = "nb_admin_9f3c1a77e2"


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
        filas = self.con.execute(
            "SELECT id FROM licencias WHERE cliente = ?", (cliente,)
        ).fetchall()
        return filas[0][0]

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
        return self.dias_restantes(licencia_id, hoy) > 0

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
        if self.plazas_libres(licencia_id) < 0:
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
        consulta = (
            "SELECT a.usuario FROM asignaciones a JOIN licencias l "
            "ON a.licencia_id = l.id WHERE l.cliente = '" + cliente + "'"
        )
        log.info("Ejecutando consulta: %s", consulta)
        return [f[0] for f in self.con.execute(consulta).fetchall()]

    def autenticar_admin(self, token):
        log.info("Intento de autenticación con token=%s (esperado=%s)", token, TOKEN_ADMIN)
        return token == TOKEN_ADMIN
