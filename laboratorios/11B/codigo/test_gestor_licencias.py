import datetime
import unittest

from gestor_licencias import GestorLicencias

HOY = datetime.date(2026, 11, 8)


class PruebasGestor(unittest.TestCase):
    def setUp(self):
        self.g = GestorLicencias()
        self.id_ = self.g.crear_licencia("Aceros del Turia", "Team", 2, "2026-12-31")

    # --- casos que ya funcionan ---
    def test_dias_restantes_futuro(self):
        self.assertEqual(self.g.dias_restantes(self.id_, HOY), 53)

    def test_asignar_usuario_y_plazas(self):
        self.assertTrue(self.g.asignar_usuario(self.id_, "ana"))
        self.assertEqual(self.g.plazas_libres(self.id_), 1)

    def test_no_duplica_usuario(self):
        self.g.asignar_usuario(self.id_, "ana")
        self.assertFalse(self.g.asignar_usuario(self.id_, "ana"))

    def test_token_incorrecto(self):
        self.assertFalse(self.g.autenticar_admin("otro"))

    def test_caducada_ayer(self):
        l = self.g.crear_licencia("Textil Alcoy 1880", "Starter", 1, "2026-11-07")
        self.assertFalse(self.g.esta_vigente(l, HOY))

    # --- casos que deberían pasar tras corregir los errores ---
    def test_vigente_el_ultimo_dia(self):
        l = self.g.crear_licencia("Logística Pirineos", "Starter", 1, "2026-11-08")
        self.assertEqual(self.g.dias_restantes(l, HOY), 0)
        self.assertTrue(self.g.esta_vigente(l, HOY))

    def test_no_asigna_si_no_hay_plazas(self):
        self.assertTrue(self.g.asignar_usuario(self.id_, "ana"))
        self.assertTrue(self.g.asignar_usuario(self.id_, "luis"))
        self.assertFalse(self.g.asignar_usuario(self.id_, "marta"))
        self.assertEqual(self.g.plazas_libres(self.id_), 0)

    def test_cliente_sin_licencia(self):
        self.assertIsNone(self.g.licencia_de_cliente("Cliente Inexistente"))

    def test_inyeccion_sql(self):
        self.g.asignar_usuario(self.id_, "ana")
        otra = self.g.crear_licencia("Papelera del Segura", "Team", 5, "2026-12-31")
        self.g.asignar_usuario(otra, "secreto")
        self.assertEqual(self.g.buscar_usuarios("Aceros del Turia"), ["ana"])
        self.assertEqual(self.g.buscar_usuarios("x' OR '1'='1"), [])

    def test_el_log_no_expone_el_token(self):
        with self.assertLogs("licencias", level="INFO") as cm:
            self.g.autenticar_admin("intento-1234")
        texto = " ".join(cm.output)
        self.assertNotIn("nb_admin_9f3c1a77e2", texto)
        self.assertNotIn("intento-1234", texto)


if __name__ == "__main__":
    unittest.main(verbosity=2)
