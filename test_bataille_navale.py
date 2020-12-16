import unittest
import joueur
import tableau
import bateau


class Test_bataille_navale(unittest.TestCase):
    def setUp(self):
        """
        Creation de la méthode setUp permettant de générer un joueur fictif.
        :return: none
        """
        self.tab = tableau.Tableau(5)
        self.tab.creation_tableau()
        self.j = joueur.Joueur("joueurNumero1", self.tab, 200)
        self.nbr_bateaux = 3
        self.bateau1 = bateau.Bateau("porte-avion", 4, "actif")
        self.bateau1.coordonnees_bateau = [1, 1, "o"], [1, 2, "o"], [1, 3, "o"], [1, 4, "o"]
        self.bateau2 = bateau.Bateau("torpilleur", 2, "actif")
        self.bateau2.coordonnees_bateau = [4, 1, "o"], [4, 2, "o"]
        self.bateau3 = bateau.Bateau("croiseur", 2, "actif")
        self.bateau3.coordonnees_bateau = [5, 1, "o"], [5, 2, "o"]
        self.j.porte_avion = self.bateau1
        self.j.torpilleur = self.bateau2
        self.j.croiseur = self.bateau3

    def test_joueur_objet_de_joueur(self):
        self.assertIsInstance(self.j, joueur.Joueur)

    def test_position_bateau_verif(self):

        for elements in range(self.nbr_bateaux):
            nom_bateau = self.bateau1
            if elements == 0:
                nom_bateau = self.bateau1
            elif elements == 1:
                nom_bateau = self.bateau2
            elif elements == 2:
                nom_bateau = self.bateau3
            for positions in nom_bateau.coordonnees_bateau:
                if int(positions[0]) and int(positions[1]) > (len(self.tab.tableau)):
                    raise IndexError


if __name__ == "__main__":
    unittest.main()
