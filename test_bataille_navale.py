import unittest
import joueur
import tableau
import bateau
from database_connection import *
from param_partie import *


class TestBatailleNavale(unittest.TestCase):
    def setUp(self):
        """
        Creation de la méthode setUp permettant de générer un joueur fictif.
        """
        self.tab = tableau.Tableau(5)
        self.tab.creation_tableau()

        self.j = joueur.Joueur("joueurNumero1", self.tab, 200)
        self.j.score = 9000

        self.nbr_bateaux = 3
        self.bateau1 = bateau.Bateau("porte-avion", 4, "actif")
        self.bateau1.coordonnees_bateau = [1, 1, "o"], [1, 2, "o"], [1, 3, "o"], [1, 4, "o"]

        self.bateau2 = bateau.Bateau("torpilleur", 2, "actif")
        self.bateau2.coordonnees_bateau = [4, 1, "o"], [4, 2, "o"]

        self.bateau3 = bateau.Bateau("croiseur", 2, "actif")
        self.bateau3.coordonnees_bateau = [5, 1, "o"], [5, 2, "o"]

        self.bateau4 = bateau.Bateau("canonniere", 3, "actif")

        self.bateau5 = bateau.Bateau("destroyer", 3, "actif")

        self.j.porte_avion = self.bateau1
        self.j.torpilleur = self.bateau2
        self.j.croiseur = self.bateau3
        self.j.canonniere = self.bateau4
        self.j.destroyer = self.bateau5

    # TEST CLASSE Joueur

    def test_joueur_objet_de_joueur(self):
        """
        Méthode de classe permettant de vérifier si un objet est bien une instance de la classe joueur.
        :return: none
        """
        self.assertIsInstance(self.j, joueur.Joueur)

    def test_nom_joueur(self):
        joueur_nom = joueur.Joueur("Player ONE", self.tab, 200)
        self.assertEqual(joueur_nom.nom, "Player ONE")

    def test_soustraction_score_joueur(self):
        self.j - 100
        mon_reste = self.j.score
        self.assertEqual(mon_reste, 8900)

    def test_addtition_score_joueur(self):
        self.j + 100
        mon_reste = self.j.score
        self.assertEqual(mon_reste, 9100)

    # TEST CLASSE Bateau

    def test_bateau_objet_de_bateau(self):
        """
        Méthode de classe permettant de vérifier si un objet est bien une instance de la classe joueur.
        :return: none
        """
        self.assertIsInstance(self.bateau1, bateau.Bateau)

    def test_nombre_cases_bateaux(self):
        """
        Méthode permettant de vérifier la taille de chaque bateau selon le nombre de bateaux utilisés
        dans une partie donnée.
        :return: none
        """
        if self.nbr_bateaux == 3:
            self.assertEqual(self.bateau1.taille_bateau + self.bateau2.taille_bateau + self.bateau3.taille_bateau, 8)
        elif self.nbr_bateaux == 5:
            self.assertEqual(self.bateau1.taille_bateau + self.bateau2.taille_bateau + self.bateau3.taille_bateau
                             + self.bateau4.taille_bateau + self.bateau5.taille_bateau, 14)

    def test_bateau_verif_position_horizontal(self):
        plateau = self.tab.tableau
        plateau[1][1] = "o"
        my_bateau = self.bateau4
        with self.assertRaises(ValueError):
            my_bateau.position_bateau_verif("A", 0, my_bateau, plateau, "h")

    def test_bateau_verif_position_vertical(self):
        plateau = self.tab.tableau
        plateau[1][1] = "o"
        my_bateau = self.bateau4
        with self.assertRaises(ValueError):
            my_bateau.position_bateau_verif("A", 0, my_bateau, plateau, "v")

    def test_bateau_position_horizontal(self):
        plateau = self.tab.tableau
        my_bateau = self.bateau4
        my_bateau.position_bateau("A", 0, my_bateau, plateau, "h")
        self.assertEqual(plateau[1][1], "o")
        self.assertEqual(plateau[1][2], "o")
        self.assertEqual(plateau[1][3], "o")

    def test_bateau_position_vertical(self):
        plateau = self.tab.tableau
        my_bateau = self.bateau4
        my_bateau.position_bateau("A", 0, my_bateau, plateau, "v")
        self.assertEqual(plateau[1][1], "o")
        self.assertEqual(plateau[2][1], "o")
        self.assertEqual(plateau[3][1], "o")

    # TEST CLASSE Tableau

    def test_tableau_objet_de_tableau(self):
        """
        Méthode de classe permettant de vérifier si un objet est bien une instance de la classe joueur.
        :return: none
        """
        self.assertIsInstance(self.tab, tableau.Tableau)

    # TEST param_partie

    def test_selection_nbr_bateau(self):
        nbr_bat = selection_nombre_bateau(5)
        self.assertEqual(nbr_bat, 3)

    def test_creation_tab_joueur(self):
        mon_joueur = creation_tableau_joueur(10, "player")
        self.assertIsInstance(mon_joueur, joueur.Joueur)
        self.assertEqual(mon_joueur.nom, "player")
        self.assertEqual(mon_joueur.plateau_joueur.dimension_tableau, 10)

    def test_joueur_auto(self):
        mon_joueur = joueur_auto()
        self.assertIsInstance(mon_joueur, joueur.Joueur)

        self.assertIsInstance(mon_joueur.porte_avion, bateau.Bateau)
        self.assertIsInstance(mon_joueur.torpilleur, bateau.Bateau)
        self.assertIsInstance(mon_joueur.croiseur, bateau.Bateau)

        self.assertIsInstance(mon_joueur.plateau_joueur, tableau.Tableau)

        self.assertEqual(mon_joueur.nom, "nom_joueur1")
        self.assertEqual(mon_joueur.plateau_joueur.dimension_tableau, 6)

    def test_connection(self):
        cursor.execute("SELECT test_int,test_text from test_connection")
        tableau_score = cursor.fetchall()
        verif_int = tableau_score[0][0]
        verif_txt = tableau_score[0][1]
        self.assertEqual(verif_int, 99)
        self.assertEqual(verif_txt, "ceci est un test")

    def test_envois_score(self):
        envoi_score(self.j, self.j)
        envoi = connection.cursor()
        envoi.execute("SELECT Score_Partie from score_joueur where Pseudo_joueur = 'joueurNumero1'")
        verif = envoi.fetchall()
        self.assertEqual(verif[0][0], 9000)
        cursor.execute("DELETE from score_joueur where Pseudo_joueur = 'joueurNumero1'")
        connection.commit()


if __name__ == "__main__":
    unittest.main()
