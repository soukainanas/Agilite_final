import unittest
from classes import Mairie, Employe



class MairieTestCase(unittest.TestCase):
    def setUp(self):
        self.mairie = Mairie("Mairie de Paris", "75000")
        self.employe = Employe("John Doe", self.mairie)

    def tearDown(self):
        pass

    def test_unitary(self):
        mairie1 = Mairie("Creteil", "94000")
        self.assertEqual("Bonneuil", mairie1.set_get_nom("Bonneuil"))

    def test_employee_label(self):
        label = self.employe.cree_etiquette("Mairie de Paris")
        self.assertEqual("Mairie de Paris", label)

    def test_mairie_name(self):
        self.assertEqual("Mairie de Paris", self.mairie.get_nom())

    def test_mairie_postal_code(self):
        self.assertEqual("75000", self.mairie.get_code_postal())


if __name__ == '__main__':
    unittest.main()
