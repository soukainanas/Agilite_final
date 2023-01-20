#Author: Manel, Soukaina, Pierre-Alexis, Mohamed

@tag
Feature: Cumul des points gagnés par etudiant
    En tant que Mairie
    Je veux enregistrer le nombre d'employes chaque jour
    Afin de savoir combien de personnes ont disparus 

    Scenario Outline: calcul automatique du nombre d'employes chaque jour

	Given le nombre d employes d une mairie "<mairie1>" "<mairie2>" "<mairie3>" "<mairie4>" 
	When le nombre d employes est positif
	Then le "<total>" des employes d une mairie doivent etre automatiquement calcules

	Examples: Total nombres employes par jour
	       | mairie1 | mairie2 | mairie3 | mairie4 | total |
	       |    1    |    2    |    2    |    4    |   9   |
	       |    1    |    1    |    1    |    3    |   6   |


    Scenario Outline: calcul automatique des points de l'étudiant

	Given des points attribues par differents professeurs "<point1>" "<point2>" "<point3>" "<point4>"
	When le nombre de points est positif
	Then le "<total>" des points de un etudiant doivent etre automatiquement calcules

	Examples: Attributed points
	       | point1 | point2 | point3 | point4 | total |
	       |    1   |    2   |    2   |    4   |   9   |
	       |    3   |    1   |    1   |    3   |   8   |
