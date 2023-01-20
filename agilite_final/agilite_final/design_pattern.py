from abc import ABCMeta, abstractstaticmethod


class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """Interface methode"""

class Etudiant(IPerson):
    def __init__(self):
        self.prenom = "prenom"
        self.nom = "nom"
        self.cahier = []

    def person_method(self) :
         print("L'etudiant John Doe")

class Employe:
    def __init__(self):
        self.mairie = "mairie"
        self.nomE = ""
        self.etiquette = ""
        self.total_mairie = '0'

    def person_method(self):
        print("l'employeur cristhope")


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Employe":
            return Employe()
        if person_type == "Etudiant":
            return  Etudiant()
        print ("Invalid type")
        return -1

if __name__ == "__main__":
    choice = input("what type of person do you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()


