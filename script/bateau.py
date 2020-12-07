class Bateau:

    def __init__(self, nom, taille, etat="actif"):
        self.nom_bateau = nom
        self.coordonnees_bateau = []
        self.etat_bateau = etat
        self.taille_bateau = taille


    def modifier_tableau(self):
        pass

    def position_bateau(self, col, rangee, nom_navire, plateau):
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

        horizontal_ou_vertical = input("Voulez vous le placer horizontalement ou verticalement ? (h ou v)\n\n").lower()
        if horizontal_ou_vertical == "h":
            for elements in range(nom_navire.taille_bateau):
                position = [rangee, col+elements, "o"]
                self.coordonnees_bateau.append(position)
                plateau[nom_navire.coordonnees_bateau[0][0]][nom_navire.coordonnees_bateau[0][1] + elements] = "o"
                print(position)

        elif horizontal_ou_vertical == "v":
            for elements in range(nom_navire.taille_bateau):
                position = [rangee + elements, col, "o"]
                self.coordonnees_bateau.append(position)
                plateau[nom_navire.coordonnees_bateau[0][0] + elements][nom_navire.coordonnees_bateau[0][1]] = "o"
                print(position)