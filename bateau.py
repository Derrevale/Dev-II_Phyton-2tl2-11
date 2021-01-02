coordonnees_plateau = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10
}


class Bateau:
    """Classe servant a créé un objet bateau avec un nom , une taille, un tableau contenant ses coordonnées

    Author : V. Derreumaux, S.Volont
    Date : November 2020
    """

    def __init__(self, nom: str, taille: int, etat="actif"):
        """Construit un objet bateau basé sur un nom et une taille

        PRE :
            - nom = str
            - taille = int
        POST :
            -self.nom_bateau = nom
            -self.taille_bateau = taille
            -self.etat_bat = "actif"
            -self.coordonnees_bateau = []
            -self.emplacement = False
        """
        self.nom_bateau = nom
        self.coordonnees_bateau = []
        self.etat_bat = etat
        self.taille_bateau = taille
        self.emplacement = False

    def position_bateau_verif(self, col: str, rangee: int, nom_navire: object, plateau: list, orientation: str):
        """méthode de verification des positions du bateaux

        PRE :
            - col = str A-J
            - rangee = int
            - nom_navire = objet Bateau
            - plateau = list
            - orientation = str
        POST :
            - if orientation = h / v

        RAISES :
            - ValueError if plateau[rangee][col + elements] == "o":
        """
        col = coordonnees_plateau[col]
        rangee = rangee + 1

        if orientation == "h":
            for elements in range(nom_navire.taille_bateau):
                if plateau[rangee][col + elements] == "o":

                    raise ValueError

        elif orientation == "v":

            for elements in range(nom_navire.taille_bateau):
                if plateau[rangee + elements][col] == "o":

                    raise ValueError

    def position_bateau(self, col: str, rangee: int, nom_navire: object, plateau: list, orientation: str):
        """ Methode qui permet de positionner un bateau sur un tableau et d'attribuer ces coordonnees a l'objet Bateau

        PRE :
            - col = str A-J
            - rangee = int
            - nom_navire = objet Bateau
            - plateau = list
            - orientation = str
        POST :
            - col = int -> (coordonnees_plateau[col])
            - position = [rangee,col,"o"]
            - objet Bateau.coordonnees_bateau.append(position)
            - plateau[X+element][Y] = "o" si orientation = v
            - plateau[X][Y+element] = "o" si orientation = h
        """
        col = coordonnees_plateau[col]
        rangee = rangee + 1

        if orientation == "h":
            for elements in range(nom_navire.taille_bateau):
                position = [rangee, col + elements, "o"]
                self.coordonnees_bateau.append(position)
                plateau[nom_navire.coordonnees_bateau[0][0]][nom_navire.coordonnees_bateau[0][1] + elements] = "o"

        elif orientation == "v":
            for elements in range(nom_navire.taille_bateau):
                position = [rangee + elements, col, "o"]
                self.coordonnees_bateau.append(position)
                plateau[nom_navire.coordonnees_bateau[0][0] + elements][nom_navire.coordonnees_bateau[0][1]] = "o"
