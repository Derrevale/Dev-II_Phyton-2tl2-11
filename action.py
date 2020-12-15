# Importation de la classe tableau
import copy
import random

from bateau import Bateau
from tableau import *

# Importation de la classe joueur
from joueur import Joueur


def nom_de_joueur(x: int):
    # Fonction d'attribution des noms
    nom_joueur = input("\nJoueur " + str(x) + ", veuillez introduire votre nom : ")
    return nom_joueur


def selection_type_partie_console():
    petite_bat = "P"
    grande_bat = "G"
    lancement = False
    style_partie = input(
        "Choisisez le style de partie que vous voulez jouez."
        "\nGrande Bataille (10*10 , 5 Bateaux)"
        "\nPetite Bataille (06*06 , 3 Bateaux)"
        "\nG/P\n")

    # verification que la valeur entrée est correcte
    while not lancement:

        if style_partie.upper() == petite_bat:
            lancement = True
            nombre_ligne_colonne = 5

        elif style_partie.upper() == grande_bat:
            lancement = True
            nombre_ligne_colonne = 10
        else:
            print("erreur")
            style_partie = input(
                "Le choix entrez est incorecte veuillez réintroduire."
                "\nGrande Bataille (10*10 , 5 Bateaux)"
                "\nPetite Bataille (06*06 , 3 Bateaux)"
                "\nG/P\n")
    return nombre_ligne_colonne


def selection_nombre_bateau(x: int):
    nombre_bateau = 0
    if x == 5:
        nombre_bateau = 3
    elif x == 10:
        nombre_bateau = 5

    return nombre_bateau


def afficher_tableau(tableau: list):
    for elements in tableau:
        print(elements)


def creation_tableau_joueur(dimension: int, nom_joueur: str):
    plateau_joueur = CreerTableau(dimension)
    plateau_joueur.creation_tableau()
    return Joueur(nom_joueur, plateau_joueur)


def effectuer_tir(rangee: int, col: int, adversaire: object):
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
    if adversaire.plateau_joueur.tableau[rangee][col] == "o":
        adversaire.plateau_joueur.tableau[rangee][col] = "@"
        print("Touché")
        for elements in adversaire.porte_avion.coordonnees_bateau:
            if elements[0] == col + 1 and elements[1] == rangee:
                print("dans if")
                adversaire.porte_avion.coordonnees_bateau[0][2] = "X"
                adversaire.porte_avion.etat_bateau = "Touché"
                print(adversaire.porte_avion.coordonnees_bateau)
    elif adversaire.plateau_joueur.tableau[rangee][col] == "@":
        adversaire.plateau_joueur.tableau[rangee][col] = "@"
    else:
        print("Raté!")
        adversaire.plateau_joueur.tableau[rangee][col] = "X"


def choix_action(joueur_actu: object):
    roulette = ["coup vertical"]
    resultat_roulette = ""
    if joueur_actu.portefeuille_joueur >= 150:
        choix_roulette = input(
            "{}, Vous avez actuellement {} euros dans votre portefeuille, voulez-vous faire tourner la roulette pour"
            " 150 euros? (o ou n) \n\n".format(joueur_actu.nom_joueur, joueur_actu.portefeuille_joueur))
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


def plateau_invisible_adversaire(plateau_invisible: list, plateau_a_copier: list):
    plateau_invisible = copy.deepcopy(plateau_a_copier)
    for elements in range(len(plateau_invisible)):
        for ele in range(len(plateau_invisible[elements])):
            if plateau_invisible[elements][ele] == "o":
                plateau_invisible[elements][ele] = "~"
    for elements in plateau_invisible:
        print(elements)


def tour_de_jeu(joueur_actuel: object, adversaire: object, plateau_invisible: list):
    while True:
        try:

            plateau_invisible_adversaire(plateau_invisible, adversaire.plateau_joueur.tableau)
            choix_col_joueur = input(
                "Joueur : {}, Veuillez introduire la colonne : ".format(joueur_actuel.nom))
            choix_rangee_joueur = int(
                input("Joueur : {}, Veuillez introduire la ligne : ".format(joueur_actuel.nom)))
            effectuer_tir(choix_rangee_joueur, choix_col_joueur.upper(), adversaire)
        except KeyError:
            print("Erreur, veuillez introduire des coordonnées valides\n")
            continue
        except ValueError:
            print("Erreur, veuillez introduire des coordonnées valides\n")
            continue
        else:
            plateau_invisible_adversaire(plateau_invisible, adversaire.plateau_joueur.tableau)
            break

    print("==========================================\n"
          "==========================================\n"
          "==========================================\n")


def positionner_bateau(joueur: object, number_of_ships: int):
    for elements in range(1, number_of_ships + 1):
        afficher_tableau(joueur.plateau_joueur.tableau)
        if elements == 1:
            porte_avion = Bateau("porte-avion", 4)
            joueur.porte_avion = porte_avion
            joueur.nom_des_bateaux.append("porte-avion")
            bateau = porte_avion

        elif elements == 2:
            torpilleur = Bateau("torpilleur", 2)
            joueur.torpilleur = torpilleur
            joueur.nom_des_bateaux.append("torpilleur")
            bateau = torpilleur

        elif elements == 3:
            croiseur = Bateau("croiseur", 2)
            joueur.croiseur = croiseur
            joueur.nom_des_bateaux.append("croiseur")
            bateau = croiseur

        elif elements == 4:
            canonniere = Bateau("canonniere", 3)
            joueur.Canonniere = canonniere
            joueur.nom_des_bateaux.append("canonniere")
            bateau = canonniere
        elif elements == 5:
            destroyer = Bateau("destroyer", 3)
            joueur.destroyer = destroyer
            joueur.nom_des_bateaux.append("destroyer")
            bateau = destroyer

        print("Joueur {} le bateau que vous placez est le : {} avec une taille de : {}".format(joueur.nom,
                                                                                               bateau.nom_bateau,
                                                                                               bateau.taille_bateau))
        while True:

            try:
                coord_col = input(
                    "Joueur {}, veuillez choisir une colonne comme point de départ pour placer le {} : ".format(
                        joueur.nom,
                        bateau.nom_bateau)).upper()
                coord_rangee = int(input(
                    "Joueur {}, veuillez choisir une ligne comme point de départ pour placer le {} : ".format(
                        joueur.nom,
                        bateau.nom_bateau)))
                horizontal_ou_vertical = input(
                    "Voulez vous le placer horizontalement ou verticalement ? (h ou v)\n\n").lower()

                bateau.position_bateau_verif(coord_col, coord_rangee, bateau, joueur.plateau_joueur.tableau,
                                             horizontal_ou_vertical)
            except IndexError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
            except ZeroDivisionError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
            except KeyError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
                continue
            except ValueError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
                continue
            else:
                print(coord_col)
                bateau.position_bateau(coord_col, coord_rangee, bateau, joueur.plateau_joueur.tableau,
                                       horizontal_ou_vertical)

                break

    afficher_tableau(joueur.plateau_joueur.tableau)

    fin_de_tour = False
    while fin_de_tour == False:
        print("Votre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour = input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour == "O" or valid_fin_de_tour == "OUI":
            fin_de_tour = True


def verif_bateau(joueur_actuel: object, *arg):
    counter = []
    for nom_du_bateau in arg:
        for elements in range(nom_du_bateau.taille_bateau):
            if nom_du_bateau.etat_bateau == "inactif":
                print("ce bateau a déjà été détruit")
                break
            if nom_du_bateau.coordonnees_bateau[elements][2] == "@":
                print("{} est endommagé".format(nom_du_bateau.nom_bateau))
                counter.append("@")
                nom_du_bateau.etat_bateau = "Touché"
                if len(counter) == nom_du_bateau.taille_bateau:
                    nom_du_bateau.etat_bateau = "inactif"
                    if nom_du_bateau.etat_bateau == "inactif":
                        joueur_actuel.portefeuille_joueur = joueur_actuel.portefeuille_joueur + 150
                        print(joueur_actuel.portefeuille_joueur)
                    else:
                        print("pas encore")
        print("L'état du bateau {} est le suivant : {} ".format(nom_du_bateau.nom_bateau, nom_du_bateau.etat_bateau))


def rafraichir_position(adversaire: object, *arg):
    for nom_du_bateau in arg:
        for elements in range(nom_du_bateau.taille_bateau):
            col = nom_du_bateau.coordonnees_bateau[elements][1]
            rangee = nom_du_bateau.coordonnees_bateau[elements][0]
            if adversaire.plateau_joueur.tableau[rangee][col] == "@":
                nom_du_bateau.coordonnees_bateau[elements][2] = "@"
        print(nom_du_bateau.coordonnees_bateau)


def verif_win(joueur: object, number_of_ship: int):
    # y = joueur_1 ou 2
    if number_of_ship == 3:
        if joueur.porte_avion.etat_bateau and joueur.torpilleur.etat_bateau and joueur.croiseur.etat_bateau == "inactif":
            return True
    elif number_of_ship == 2:
        if joueur.porte_avion.etat_bateau and joueur.torpilleur.etat_bateau == "inactif":
            return True
    elif number_of_ship == 1:
        if joueur.porte_avion.etat_bateau == "inactif":
            return True


def debut_partie(joueur1: object, joueur2: object,
                 tableau_invisible_joueur1: list, tableau_invisible_joueur2: list,
                 number_of_ships: int):
    # Victoire devient True quand un joueur détruit tout les bateaux adverse
    victoire = False
    # PHASE 1 PLACEMENT BATEAU

    positionner_bateau(joueur1, number_of_ships)
    positionner_bateau(joueur2, number_of_ships)

    # PHASE  2 VERIFICATION DE L ETAT DES BATEAUX
    while victoire == False:

        if number_of_ships == 3:
            petite_partie(joueur1,
                          joueur2,
                          tableau_invisible_joueur1, tableau_invisible_joueur2
                          )


        elif number_of_ships == 5:
            grande_partie(joueur1,
                          joueur2,
                          tableau_invisible_joueur1, tableau_invisible_joueur2,
                          )

        if verif_win(joueur2, number_of_ships) == True:
            victoire = True
            print("le joueur 1 a gagné")

        if verif_win(joueur1, number_of_ships) == True:
            victoire = True
            print("le joueur 2 a gagné")


def petite_partie(joueur1: object,
                  joueur2: object,
                  tableau_invisible_joueur1: list, tableau_invisible_joueur2: list
                  ):
    print("plateau du joueur 2 : \n")

    tour_de_jeu(joueur1, joueur2, tableau_invisible_joueur2)

    rafraichir_position(joueur2, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur)
    verif_bateau(joueur1, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, tableau_invisible_joueur1)

    rafraichir_position(joueur2, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur)
    verif_bateau(joueur2, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur)


def grande_partie(joueur1: object, joueur2: object,
                  tableau_invisible_joueur1: list, tableau_invisible_joueur2: list,
                  ):
    print("plateau du joueur 2 : \n")

    tour_de_jeu(joueur1, joueur2, tableau_invisible_joueur2)

    rafraichir_position(joueur2, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur, joueur2.cannoniere,
                        joueur2.destroyer)
    verif_bateau(joueur1, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur, joueur2.cannoniere,
                 joueur2.destroyer)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, tableau_invisible_joueur1)

    rafraichir_position(joueur2, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur, joueur1.cannoniere,
                        joueur1.destroyer)
    verif_bateau(joueur2, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur, joueur1.cannoniere,
                 joueur1.destroyer)
