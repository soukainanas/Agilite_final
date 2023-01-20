class Etudiant():
    def __init__(self, prenom: str, nom: str):
        self.prenom = prenom
        self.nom = nom
        self.cahier = []

    def set_nom(self, nom: str):
        self.nom = nom

    def set_prenom(self, prenom: str):
        self.prenom = prenom

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def old_change_prenom(self, prenom: str):
        self.prenom = prenom
        return self.prenom

    def change_prenom(self, prenom: str):
        self.set_prenom(prenom)
        return self.get_prenom()




class Cahier():
    def __init__(self, etudiant: Etudiant):
        self.page_de_garde = ''
        self.page_points = '0'
        self.etudiant = etudiant
        self.etudiant.cahier.append(self)

    def ecrire_page_de_garde(self):
        self.page_de_garde = self.etudiant.get_prenom()
        return self.page_de_garde

    def ajouter_points(self, point: int):
        self.page_points = str(int(self.page_points)+int(point))
        return self.page_points








