import random
from script.Joueur import *


class Actions:

    def modif_tableau(self):
        pass

    def effectuer_tir(self, tab, rangee, col, adversaire):
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
        if tab[rangee][col] == "o":
            tab[rangee][col] = "@"
            print("Touché")
            for elements in adversaire.porte_avion.coordonnees_bateau:
                if elements[0] == col+1 and elements[1] == rangee:
                    print("dans if")
                    adversaire.porte_avion.coordonnees_bateau[0][2] = "X"
                    adversaire.porte_avion.etat_bateau="Touché"
                    print(adversaire.porte_avion.coordonnees_bateau)
        elif tab[rangee][col] == "@":
            tab[rangee][col] = "@"
        else:
            print("Raté!")
            tab[rangee][col] = "X"

    def verif_position(self):
        pass

    def choix_action(self, x):
        roulette = ["coup vertical"]
        resultat_roulette = ""
        if x.portefeuille_joueur >= 150:
            choix_roulette = input(
                "{}, Vous avez actuellement {} euros dans votre portefeuille, voulez-vous faire tourner la roulette pour"
                " 150 euros? (o ou n) \n\n".format(x.nom_joueur, x.portefeuille_joueur))
            if choix_roulette == "o":
                # x.portefeuille_joueur = x.portefeuille_joueur - 150
                resultat_roulette = random.choice(roulette)
                if resultat_roulette == "rien":
                    print("Dommage, vous n'avez rien gagné !")
                else:
                    print("Félicitations vous avez gagné le sort suivant : {} ".format(resultat_roulette))
        else:
            print("Vous n'avez pas assez d'argent pour faire tourner la roulette\n\n")
        return resultat_roulette

    def coup_special(objet, x, plateau):
        coordonnees_plateau = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6
        }

        choix = objet.choix_action(x)
        print(type(choix))
        if choix != "rien":
            if choix != "":
                col = input(
                    "Veuillez choisir une colonne comme point de départ pour effectuer le coup spécial suivant : {} -> ".format(choix)).upper()
                rangee = int(input(
                    "veuillez choisir une rangée comme point de départ pour effectuer le coup spécial suivant : {} -> ".format(choix)))
                col = coordonnees_plateau[col]
                rangee = rangee + 2
                if choix == "coup horizontal":
                    print("Coup horizontal!")
                    for elements in range(3):
                        if plateau[rangee][col + elements] == "o":
                            plateau[rangee][col + elements] = "@"
                        else:
                            plateau[rangee][col + elements] = "x"

                elif choix == "coup vertical":
                    print("coup vertical !")
                    for elements in range(3):
                        if plateau[rangee + elements][col] == "o":
                            plateau[rangee + elements][col] = "@"
                        else:
                            plateau[rangee + elements][col] = "x"