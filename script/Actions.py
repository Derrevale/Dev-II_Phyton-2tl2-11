import random
from script.Joueur import *


class Actions:

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

    def choix_action(self, x):
        roulette = ["rien", "coup vertical", "coup horizontal", "rien", "rien"]
        resultat_roulette = ""
        if x.player_wallet >= 150:
            roulette_choice = input(
                "{}, Vous avez actuellement {} euros dans votre portefeuille, voulez-vous faire tourner la roulette pour"
                " 150 euros? (o ou n) \n\n".format(x.player_name, x.player_wallet))
            if roulette_choice == "o":
                # x.player_wallet = x.player_wallet - 150
                resultat_roulette = random.choice(roulette)
                if resultat_roulette == "rien":
                    print("Dommage, vous n'avez rien gagné !")
                else:
                    print("Félicitations vous avez gagné le sort suivant : {} ".format(resultat_roulette))
        else:
            print("Vous n'avez pas assez d'argent pour faire tourner la roulette\n\n")
        return resultat_roulette

    def coup_special(this_object,x, plateau):
        coordonnees_plateau = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6
        }

        choice = this_object.choix_action(x)
        print(type(choice))
        if choice != "rien":
            col = input(
                "Veuillez choisir une colonne comme point de départ pour effectuer le coup spécial suivant : {} -> ".format(choice)).upper()
            row = int(input(
                "veuillez choisir une rangée comme point de départ pour effectuer le coup spécial suivant : {} -> ".format(choice)))
            col = coordonnees_plateau[col]
            row = row + 2
            if choice == "coup horizontal":
                print("Coup horizontal!")
                for elements in range(3):
                    plateau[row][col + elements] = "x"

            elif choice == "coup vertical":
                print("coup vertical !")
                for elements in range(3):
                    plateau[row + elements][col] = "x"