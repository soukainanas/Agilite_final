#Author: Manel, Soukaina

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
