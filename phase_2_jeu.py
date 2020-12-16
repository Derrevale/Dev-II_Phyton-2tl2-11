# Importation de la classe tableau
import copy
import random
from phase_1_position_bateau import *


def effectuer_tir(rangee: int, col: str, adversaire: object):
    """
    fonction servant a effectuer un tir sur le tableau adverse
    :param rangee: numero de la ligne
    :param col: numero de la colonne
    :param adversaire: objet Joueur correspond a l'adversaire
    :return:
    """
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
    elif adversaire.plateau_joueur.tableau[rangee][col] == "@":
        adversaire.plateau_joueur.tableau[rangee][col] = "@"
    else:
        print("Raté!")
        adversaire.plateau_joueur.tableau[rangee][col] = "X"


def choix_action(joueur_actu: object):
    """
    fonction servant a effectuer un choix qui permet au joueur de faire une roulette
    :param joueur_actu: objet Joueur correspondant au joueur dont c'est le tour de jeu
    :return: resultat_roulette
    """
    roulette = ["coup vertical", "coup horizontal", "rien", "rien"]
    resultat_roulette = ""
    if joueur_actu.portefeuille_joueur >= 150:
        choix_roulette = input(
            "{}, Vous avez actuellement {} euros dans votre portefeuille, voulez-vous faire tourner la roulette pour"
            " 150 euros? (o ou n) \n\n".format(joueur_actu.nom_joueur, joueur_actu.portefeuille_joueur))
        if choix_roulette == "o":
            joueur_actu.portefeuille_joueur = joueur_actu.portefeuille_joueur - 150
            resultat_roulette = random.choice(roulette)
            if resultat_roulette == "rien":
                print("Dommage, vous n'avez rien gagné !")
            else:
                print("Félicitations vous avez gagné le sort suivant : {} ".format(resultat_roulette))
    else:
        print("Vous n'avez pas assez d'argent pour faire tourner la roulette\n\n")
    return resultat_roulette


def coup_special(joueur_actu: object, plateau: list):
    """
    Fonction permettant d'executer le coup spécial obtenu à partir de la fonction précédente choix_action()
    :param joueur_actu: Object joueur correspondant au joueur actuel dont c'est le tour de jeu
    :param plateau: Objet plateau réprésentant le plateau de jeu du joueur adverse
    :return:
    """
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

    choix = choix_action(joueur_actu)
    if choix != "rien":
        if choix != "":
            col = input(
                "Veuillez choisir une colonne comme point de départ pour effectuer le coup spécial suivant : {} -> "
                .format(choix)).upper()
            rangee = int(input(
                "veuillez choisir une rangée comme point de départ pour effectuer le coup spécial suivant : {} -> "
                .format(choix)))
            col = coordonnees_plateau[col]
            rangee = rangee + 1
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


def plateau_invisible_adversaire(plateau_invisible: list, plateau_a_copier: list):
    """
    fonction servant a copier un tableau possédant des bateaux afin que le joueur adverse tir sur un tableau sans bateau
    :param plateau_invisible: liste vide
    :param plateau_a_copier: liste du tableau d'un objet Tableau correspondant au tableau du joueur actuel
    :return: affiche le tableau sans les bateaux
    """
    plateau_invisible = copy.deepcopy(plateau_a_copier)
    for elements in range(len(plateau_invisible)):
        for ele in range(len(plateau_invisible[elements])):
            if plateau_invisible[elements][ele] == "o":
                plateau_invisible[elements][ele] = "~"
    for elements in plateau_invisible:
        print(elements)


def tour_de_jeu(joueur_actuel: object, adversaire: object, plateau_invisible: list):
    """
    fonction définissant un tour de jeu d'un joueur
    :param joueur_actuel: objet Joueur correspondant au joueur actuel
    :param adversaire: objet Joueur correspondant au joueur adverse
    :param plateau_invisible: list d'un plateau assossier au joueur actuel sans bateau
    :return:
    :raises: KeyError si la valeur n'est pas correcte
    :raises: ValueError si la valeur n'est pas dans le type adequa
    """
    while True:
        try:

            plateau_invisible_adversaire(plateau_invisible, adversaire.plateau_joueur.tableau)
            coup_special(joueur_actuel, adversaire.plateau_joueur.tableau)
            plateau_invisible_adversaire(plateau_invisible, adversaire.plateau_joueur.tableau)
            choix_col_joueur = input(
                "Joueur : {}, Veuillez introduire la colonne : ".format(joueur_actuel.nom))
            choix_rangee_joueur = int(
                input("Joueur : {}, Veuillez introduire la ligne : ".format(joueur_actuel.nom)))
            effectuer_tir(choix_rangee_joueur, choix_col_joueur.upper(), adversaire)
        except (KeyError, ValueError):
            print("Erreur, veuillez introduire des coordonnées valides\n")
            continue
        else:
            plateau_invisible_adversaire(plateau_invisible, adversaire.plateau_joueur.tableau)
            break

    print("==========================================\n"
          "==========================================\n"
          "==========================================\n")


def verif_bateau(joueur_actuel: object, *arg):
    """
    fonction servant a verifier l'états d'un bateau et de modifier l'objet Bateau en fonction des tirs reussi
    :param joueur_actuel: objet Joueur correspondant au joueur dont c'est le tour
    :param arg: objet Bateau contenant une liste avec ses positions , son nom et sa taille
    :return:
    """
    for nom_du_bateau in arg:
        counter = []
        for elements in range(nom_du_bateau.taille_bateau):
            if nom_du_bateau.etat_bat == "inactif":
                print("ce bateau a déjà été détruit")
                break
            if nom_du_bateau.coordonnees_bateau[elements][2] == "@":
                print("{} est endommagé".format(nom_du_bateau.nom_bateau))
                counter.append("@")
                nom_du_bateau.etat_bat = "Touché"
                if len(counter) == nom_du_bateau.taille_bateau:
                    nom_du_bateau.etat_bat = "inactif"
                    if nom_du_bateau.etat_bat == "inactif":
                        joueur_actuel.portefeuille_joueur = joueur_actuel.portefeuille_joueur + 150
                        print("montant du portefeuille du joueur: ", joueur_actuel.portefeuille_joueur)
                    else:
                        print("pas toucher")
        print("L'état du bateau {} est le suivant : {} ".format(nom_du_bateau.nom_bateau, nom_du_bateau.etat_bat))


def rafraichir_position(adversaire: object, *arg):
    """
    fonction servant a modifier le tableau invisible afin de voir les tirs et les resultats sur un tableau et a ensuite
    l'afficher
    :param adversaire: objet Joueur correspondant a l'adversaire
    :param arg: objet Bateau possede par le joueur adverse
    :return:
    """
    for nom_du_bateau in arg:
        for elements in range(nom_du_bateau.taille_bateau):
            col = nom_du_bateau.coordonnees_bateau[elements][1]
            rangee = nom_du_bateau.coordonnees_bateau[elements][0]
            if adversaire.plateau_joueur.tableau[rangee][col] == "@":
                nom_du_bateau.coordonnees_bateau[elements][2] = "@"


def verif_win(joueur: object, number_of_ship: int):
    """
    fonction servant a verifie l'etats des bateaux
    :param joueur: objet Joueur
    :param number_of_ship: integer correspondant au nombre de bateaux dans la partie
    :return: true si les bateaux sont a l'etats inactifs
    """
    if number_of_ship == 3:
        if joueur.porte_avion.etat_bat and joueur.torpilleur.etat_bat and joueur.croiseur.etat_bat == "inactif":
            return True
    elif number_of_ship == 5:
        if joueur.porte_avion.etat_bat and joueur.torpilleur.etat_bat and joueur.croiseur.etat_bat \
                and joueur.canonniere.etat_bat and joueur.destroyer.etat_bat == "inactif":
            return True


def lancement_partie(joueur1: object, joueur2: object,
                     tableau_invisible_joueur1: list, tableau_invisible_joueur2: list,
                     number_of_ships: int):
    """
    fonction servant initialiser et a jouer une partie qui changera en fonction du nombre de bateau
    :param joueur1: objet Joueur correspondant au premier joueur
    :param joueur2: objet Joueur correspondant a son adversaire
    :param tableau_invisible_joueur1: liste correpondant au tableau sur lesquel le joueur 1 vas tirer
    :param tableau_invisible_joueur2: liste correpondant au tableau sur lesquel le joueur 2 vas tirer
    :param number_of_ships: integer représentant le nombre de bateau lors de cette partie
    :return:
    """
    # Victoire devient True quand un joueur détruit tout les bateaux adverse
    victoire = False
    # PHASE 1 PLACEMENT BATEAU

    positionner_bateau(joueur1, number_of_ships)
    positionner_bateau(joueur2, number_of_ships)

    # PHASE  2 VERIFICATION DE L ETAT DES BATEAUX
    while not victoire:

        if number_of_ships == 3:
            petite_partie(joueur1, joueur2, tableau_invisible_joueur1, tableau_invisible_joueur2)

        elif number_of_ships == 5:
            grande_partie(joueur1,
                          joueur2,
                          tableau_invisible_joueur1, tableau_invisible_joueur2,
                          )

        if verif_win(joueur2, number_of_ships):
            victoire = True
            print("le joueur 1 a gagné")

        if verif_win(joueur1, number_of_ships):
            victoire = True
            print("le joueur 2 a gagné")


def petite_partie(joueur1: object,
                  joueur2: object,
                  tableau_invisible_joueur1: list, tableau_invisible_joueur2: list
                  ):
    """
    fonction correspondant a un tout de jeu complet avec 3 bateaux
    :param joueur1: objet Joueur correspondant au premier joueur
    :param joueur2: objet Joueur correspondant a son adversaire
    :param tableau_invisible_joueur1: liste correpondant au tableau sur lesquel le joueur 1 vas tirer
    :param tableau_invisible_joueur2: liste correpondant au tableau sur lesquel le joueur 2 vas tirer
    :return:
    """
    print("plateau du joueur 2 : \n")

    tour_de_jeu(joueur1, joueur2, tableau_invisible_joueur2)

    rafraichir_position(joueur2, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur)
    verif_bateau(joueur1, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, tableau_invisible_joueur1)

    rafraichir_position(joueur1, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur)
    verif_bateau(joueur2, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur)


def grande_partie(joueur1: object, joueur2: object,
                  tableau_invisible_joueur1: list, tableau_invisible_joueur2: list,
                  ):
    """

    fonction correspondant a un tout de jeu complet avec 5 bateaux
    :param joueur1: objet Joueur correspondant au premier joueur
    :param joueur2: objet Joueur correspondant a son adversaire
    :param tableau_invisible_joueur1: liste correpondant au tableau sur lesquel le joueur 1 vas tirer
    :param tableau_invisible_joueur2: liste correpondant au tableau sur lesquel le joueur 2 vas tirer
    """
    print("plateau du joueur 2 : \n")

    tour_de_jeu(joueur1, joueur2, tableau_invisible_joueur2)

    rafraichir_position(joueur2, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur, joueur2.canonniere,
                        joueur2.destroyer)
    verif_bateau(joueur1, joueur2.porte_avion, joueur2.torpilleur, joueur2.croiseur, joueur2.canonniere,
                 joueur2.destroyer)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, tableau_invisible_joueur1)

    rafraichir_position(joueur1, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur, joueur1.canonniere,
                        joueur1.destroyer)
    verif_bateau(joueur2, joueur1.porte_avion, joueur1.torpilleur, joueur1.croiseur, joueur1.canonniere,
                 joueur1.destroyer)
