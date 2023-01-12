import unittest
from classes import Etudiant, Cahier



class Test_etudiant(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_change_prenom(self):
        etudiant = Etudiant('Max', 'Dupont')
        self.assertEqual(etudiant.change_prenom('Tom'), "Tom")

    def test_ajout_cahier(self):
        etudiant = Etudiant('Max','Dupont')
        Cahier(etudiant)
        Cahier(etudiant)
        self.assertEqual(len(etudiant.cahier), 2)



class Test_cahier(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ecrire_page_de_garde(self):
        etudiant = Etudiant('Max', 'Dupont')
        cahier = Cahier(etudiant)
        cahier.ecrire_page_de_garde() == 'Max'
        self.assertEqual(cahier.page_de_garde, 'Max')



if __name__ == '__main__':
    unittest.main()
