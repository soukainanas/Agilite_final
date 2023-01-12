from agilite_mairie.classes import Mairie, Employe
from agilite_etudiant.classes import Etudiant, Cahier



mairie = Mairie("Mairie de Paris", "75000")
employe = Employe("John Doe", mairie)

etudiant = Etudiant('Max','Dupont')
cahier = Cahier(etudiant)






