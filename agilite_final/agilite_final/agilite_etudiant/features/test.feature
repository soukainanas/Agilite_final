#Author: Mohamed, Pierre-Alexis

@tag
Feature: Cumul des points gagnés par etudiant
    En tant qu'Etudiant
    Je veux écrire mon nombre de point gagnés dans un cahier
    Afin de savoir combien de points j'ai rapporté à ma maison

    Scenario Outline: calcul automatique des points de l'étudiant


	Given des points attribues par differents professeurs "<point1>" "<point2>" "<point3>" "<point4>"
	When le nombre de points est positif
	Then le "<total>" des points de un etudiant doivent etre automatiquement calcules

	Examples: Attributed points
	       | point1 | point2 | point3 | point4 | total |
	       |    1   |    2   |    2   |    4   |   9   |
	       |    3   |    1   |    1   |    3   |   8   |


