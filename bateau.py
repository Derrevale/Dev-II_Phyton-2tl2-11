class Bateau:

    def __init__(self, nom, taille, etat="actif"):
        self.nom_bateau = nom
        self.coordonnees_bateau = []
        self.etat_bateau = etat
        self.taille_bateau = taille
        self.emplacement = False


    def modifier_tableau(self):
        pass
    def position_bateau_verif(self, col, rangee, nom_navire, plateau,orientation):
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
                if plateau[rangee][col+elements] == "o":
                    print("supperposition de bateau")
                    lance_error=1/0



        elif orientation == "v":

            for elements in range(nom_navire.taille_bateau):
                if plateau[rangee + elements][col] == "o":
                    print("erreur superposition de 2 bateaux")
                    lance_error = 1 / 0



    def position_bateau(self, col, rangee, nom_navire, plateau,orientation):
        coordonnees_plateau = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6
        }
        col = coordonnees_plateau[col]
        rangee = rangee + 1

        if orientation == "h":
            for elements in range(nom_navire.taille_bateau):
                position = [rangee, col+elements, "o"]
                self.coordonnees_bateau.append(position)
                plateau[nom_navire.coordonnees_bateau[0][0]][nom_navire.coordonnees_bateau[0][1] + elements] = "o"
                print(position)

        elif orientation == "v":
            for elements in range(nom_navire.taille_bateau):
                position = [rangee + elements, col, "o"]
                self.coordonnees_bateau.append(position)
                plateau[nom_navire.coordonnees_bateau[0][0] + elements][nom_navire.coordonnees_bateau[0][1]] = "o"
                print(position)