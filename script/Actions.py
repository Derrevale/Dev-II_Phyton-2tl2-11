class Actions:
    choix = ""

    def modif_tableau(self):
        pass

    def effectuer_tir(self, tab, row, col,adversaire):
        coordonnees_plateau = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6
        }
        col = coordonnees_plateau[col]
        row = row + 2
        if tab[row][col] == "o":
            print("Touché")

            for elements in adversaire.porte_avion.ship_coordinates:
                if elements[0]==col+1 and elements[1]==row:
                    print("dans if")
                    adversaire.porte_avion.ship_coordinates[0][2] = "X"
                    print(adversaire.porte_avion.ship_coordinates)


        else:
            print("Raté!")
        tab[row][col] = "X"


    def verif_position(self):
        pass

    def choix_action(self):
        pass

    def coup_special(self):
        pass