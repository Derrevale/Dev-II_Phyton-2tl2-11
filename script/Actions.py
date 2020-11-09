class Actions:
    choix = ""

    def modif_tableau(self):
        pass

    def effectuer_tir(self, tab, row, col):
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
        else:
            print("Raté!")
        tab[row][col] = "X"


    def verif_position(self):
        pass

    def choix_action(self):
        pass

    def coup_special(self):
        pass