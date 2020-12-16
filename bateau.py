class Bateau:

    def __init__(self, nom: str, taille: int, etat="actif"):
        self.nom_bateau = nom
        self.coordonnees_bateau = []
        self.etat_bat = etat
        self.taille_bateau = taille
        self.emplacement = False

    def modifier_tableau(self):
        pass

    def position_bateau_verif(self, col: str, rangee: int, nom_navire: object, plateau: list, orientation: str):
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
        col = coordonnees_plateau[col]
        rangee = rangee + 1

        if orientation == "h":
            for elements in range(nom_navire.taille_bateau):
                if plateau[rangee][col + elements] == "o":
                    print("supperposition de bateau")
                    raise ValueError

        elif orientation == "v":

            for elements in range(nom_navire.taille_bateau):
                if plateau[rangee + elements][col] == "o":
                    print("erreur superposition de 2 bateaux")
                    raise ValueError

    def position_bateau(self, col: str, rangee: int, nom_navire: object, plateau: list, orientation: str):
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
