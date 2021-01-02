# dictionnaire ppour pouvoir attribuer une lettre a un chiffre
rep = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l'}


class Tableau:
    """Classe representant un tableau de jeu"""

    def __init__(self, dimension_tableau: int):
        """ constructeur de l'objet de classe Tableau
        PRE :
            - dimension_tableau = int max 11
        POST :
            - self.dimension_tableau = dimension_tableau
            - self.colonne = []
            - self.ligne = []
            - self.nom_joueur = ""
        """
        self.dimension_tableau = dimension_tableau
        self.colonne = []
        self.tableau = []
        self.nom_joueur = ""

    def creation_tableau(self):
        """ Fonction de crèation d'un tableau de jeu a partir des informations de l'objet de classe Tableau

        PRE : -
        POST :
            - my_colonne = []
            - my_ligne = []
            - boucle sur i quand i est dans range(self.dimension_tableau)
            - my_colonne.append("/") quand i = 0
            - my_colonne.append rep.upper quand i est dans range(self.dimension_tableau)
            - tableau.append(my_ligne)
            - boucle sur i quand i est dans range(self.dimension_tableau)
            - my_ligne.append(str(i)) quand j = 0
            - myligne.append("~") quand i est dans range(self.dimension_tableau)
            - tableau.append(my_ligne)
        """
        my_colonne = []
        for i in range(self.dimension_tableau):
            if i == 0:
                my_colonne.append('/')
            my_colonne.append(rep[i].upper())
        self.tableau.append(my_colonne)
        for i in range(self.dimension_tableau):
            my_ligne = []
            for j in range(len(self.tableau[0]) - 1):
                if j == 0:
                    my_ligne.append(str(i))
                my_ligne.append('~')
            self.tableau.append(my_ligne)
