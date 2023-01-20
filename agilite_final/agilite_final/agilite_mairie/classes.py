class Mairie:
    def __init__(self, nom, code_postal):
        self.name = nom
        self.code_postal = code_postal
        self.employees = []

    def set_nom(self, p_nom):
        self.name = p_nom

    def get_nom(self):
        return self.name

    def set_code_postal(self, p_code_postal):
        self.code_postal = p_code_postal

    def get_code_postal(self):
        return self.code_postal

    def set_get_nom(self, p_nom):
        self.set_nom(p_nom)
        return self.get_nom()

    def add_employee(self, employee):
        # self.extract(employee)
        self.employees.append(employee)

    # def extract(self, employee):
    #     self.extract(employee)

    def get_employees(self):
        return self.employees

class Employe:
    def __init__(self, nomE, mairie):
        self.mairie = mairie
        self.nomE = ""
        self.etiquette = ""
        self.total_mairie = '0'

    def get_mairie(self):
        return self.mairie

    def cree_etiquette(self, p_nom):
        self.etiquette = self.mairie.set_get_nom(p_nom)
        return self.etiquette

    def ajouter_total(self, total: int):
        self.total_mairie = str(int(self.total_mairie)+int(total))
        return self.total_mairie










