# Importation de la classe tableau
import copy
import random

from database_connection import *
from phase_1_position_bateau import *


def effectuer_tir(rangee: int, col: str, adversaire: object, joueur_actuel: object):
    """ Fonction servant a effectuer un tir sur le tableau adverse
    PRE :
        - rangee = int
        - col = str
        - aversaire = objet de classe Joueur
        - joueur_actuel =objet de classe Joueur
    POST :
        - col = coordonnees_plateau[col]
        - rangee = rangee + 1
        - adversaire.plateau_joueur.tableau[rangee][col] = "@" si adversaire.plateau_joueur.tableau[rangee][col] = "o"
        - print("Touché") si adversaire.plateau_joueur.tableau[rangee][col] = "@"
        - joueur_actuel +50 et adversaire-50 si adversaire.plateau_joueur.tableau[rangee][col] = "o"
        - print("Raté!") si adversaire.plateau_joueur.tableau[rangee][col] != "o" ou != "@"
        - adversaire.plateau_joueur.tableau[X][Y] = "X" si adversaire.plateau_joueur.tableau[X][Y] != "o" ou != "@"
        - adversaire + 25 si adversaire.plateau_joueur.tableau[X][Y] != "o" ou != "@"
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
        adversaire - 50
        joueur_actuel + 50
    elif adversaire.plateau_joueur.tableau[rangee][col] == "@":
        adversaire.plateau_joueur.tableau[rangee][col] = "@"
    else:
        print("Raté!")
        adversaire.plateau_joueur.tableau[rangee][col] = "X"
        adversaire + 25


def choix_action(joueur_actu: object):
    """ Fonction servant a effectuer un choix qui permet au joueur de faire une roulette
    PRE : -joueur_actu = objet de classe Joueur
    POST :
        - choix_roulette = input() si joueur_actu.portefeuille_joueur >=150
        - joueur_actu.portefeuille_joueur et joueur_actu - 150 si choix_roulette = "o"
        - resultat_roulette = random(roulette) si joueur_actu.portefeuille_joueur >=150
        - retourne resultat_roulette
    """
    roulette = ["coup vertical", "coup horizontal", "rien", "rien"]
    resultat_roulette = ""
    if joueur_actu.portefeuille_joueur >= 150:
        choix_roulette = input(
            "{}, Vous avez actuellement {} euros dans votre portefeuille, voulez-vous faire tourner la roulette pour"
            " 150 euros? (o ou n) \n\n".format(joueur_actu.nom_joueur, joueur_actu.portefeuille_joueur))
        print("score:", joueur_actu.score)
        if choix_roulette == "o":
            joueur_actu.portefeuille_joueur = joueur_actu.portefeuille_joueur - 150
            joueur_actu - 150
            resultat_roulette = random.choice(roulette)
            if resultat_roulette == "rien":
                print("Dommage, vous n'avez rien gagné !")
            else:
                print("Félicitations vous avez gagné le sort suivant : {} ".format(resultat_roulette))
    else:
        print("Vous n'avez pas assez d'argent pour faire tourner la roulette\n\n")
    return resultat_roulette


def coup_special(joueur_actu: object, plateau: list):
    """ Fonction permettant d'executer le coup spécial obtenu à partir de la fonction précédente choix_action()
    PRE :
        - joueur_actu = objet de classe Joueur
        - plateau = list
    POST :
        - si choix_action = "rien" ou "" fin de la fonction
        - col = input si choix_action = "coup horizontal" ou "coup vertical"
        - rangee = input si choix_action = "coup horizontal" ou "coup vertical"
        - boucle sur elements quand elements = 0-3
        - si plateau[X][Y + elements] == "o" alors plateau[X][Y + elements] = "@"sinon plateau[X][Y + elements] = "x"
            quand choix = "coup horizontal"
        - si plateau[X + elements][Y] == "o" alors plateau[X + elements][Y] = "@"sinon plateau[X + elements][Y] = "x"
            quand choix = "coup vertical"

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
    """ Fonction servant a copier un tableau possédant des bateaux afin que le joueur adverse tir sur un tableau
        sans bateau
    PRE :
        - plateau_invisible = list vide
        - plateau_a_copier = list remplie

    POST :
        - plateau_invisible = deepcopy plateau_a_copier
        - plateau_invisible[elements][ele] = "~" quand plateau_invisible[elements][ele] = "o"
        - affiche tableau_invisible
    """
    plateau_invisible = copy.deepcopy(plateau_a_copier)
    for elements in range(len(plateau_invisible)):
        for ele in range(len(plateau_invisible[elements])):
            if plateau_invisible[elements][ele] == "o":
                plateau_invisible[elements][ele] = "~"
    for elements in plateau_invisible:
        print(elements)


def tour_de_jeu(joueur_actuel: object, adversaire: object, plateau_invisible: list):
    """ Fonction définissant un tour de jeu d'un joueur
    PRE :
        - joueur_actuel = objet de classe Joueur
        - adversaire = objet de classe Joueur
        - plateau_invisible = list
    POST :
        - appel fonction plateau_invisible_adversaire
        - appel fonction coup_special
        - choix_col_joueur et choix_rangee_joueur = input
        - appel fonction effectuer_tir
    RAISE:
        - KeyError si la valeur n'est pas correcte
        - ValueError si la valeur n'est pas dans le type adequa
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
            effectuer_tir(choix_rangee_joueur, choix_col_joueur.upper(), adversaire, joueur_actuel)
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
    """ Fonction servant a verifier l'états d'un bateau et de modifier l'objet Bateau en fonction des tirs reussi
    PRE :
        - joueur_actuel = objet de classe Joueur
        - *arg = objet de classe Bateau
    POST :
        - boucle chaque bateau dans les arguments
        - si nom_du_bateau.coordonnees_bateau[elements][2] == "@" alors bateau.etat_bat = "touché" et counter.append @
        - quand len(counter) == nom_bateau.taille_bateau alors  bateau.etat_bat = "inactif" et joueur_actuel + 300
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
                        joueur_actuel + 300
                        joueur_actuel.portefeuille_joueur = joueur_actuel.portefeuille_joueur + 150
                        print("montant du portefeuille du joueur: ", joueur_actuel.portefeuille_joueur)
                    else:
                        print("pas toucher")
        print("L'état du bateau {} est le suivant : {} ".format(nom_du_bateau.nom_bateau, nom_du_bateau.etat_bat))


def rafraichir_position(adversaire: object, *arg):
    """ Fonction servant a modifier le tableau invisible afin de voir les tirs et les resultats sur un tableau et a
    ensuite l'afficher
    PRE :
        - adversaire = objet de classe Joueur
        - *arg = objet de classe Bateau
    POST :
        - boucle sur chaque bateau dans les arguments
        - col = nom_du_bateau.coordonnees_bateau[elements][1]
        - rangee = nom_du_bateau.coordonnees_bateau[elements][0]
        - si adversaire.plateau_joueur.tableau[X][Y] == "@" alors nom_du_bateau.coordonnees_bateau[elements][2] = "@"
    """
    for nom_du_bateau in arg:
        for elements in range(nom_du_bateau.taille_bateau):
            col = nom_du_bateau.coordonnees_bateau[elements][1]
            rangee = nom_du_bateau.coordonnees_bateau[elements][0]
            if adversaire.plateau_joueur.tableau[rangee][col] == "@":
                nom_du_bateau.coordonnees_bateau[elements][2] = "@"


def verif_win(joueur: object, number_of_ship: int):
    """ Fonction servant a verifie l'etats des bateaux
    PRE :
        - joueur = objet de classe Joueur
        - number_of_ship = int 1 / 3 / 5
    POST :
        - return True   si joueur.porte_avion.etat_bat == "inactif"
                        and joueur.torpilleur.etat_bat == "inactif"
                        and joueur.croiseur.etat_bat == "inactif"
                        quand number_of_ship == 3

        -return True   si joueur.porte_avion.etat_bat == "inactif"
                        quand number_of_ship == 1

        -return True   si joueur.porte_avion.etat_bat == "inactif"
                        and joueur.torpilleur.etat_bat == "inactif"
                        and joueur.croiseur.etat_bat == "inactif"
                        and joueur.canonniere.etat_bat == "inactif"
                        and joueur.destroyer.etat_bat == "inactif":
                        quand number_of_ship == 5
    """
    if number_of_ship == 3:
        if joueur.porte_avion.etat_bat == "inactif" and joueur.torpilleur.etat_bat == "inactif" and joueur.croiseur.etat_bat == "inactif":
            return True
    if number_of_ship == 1:
        if joueur.porte_avion.etat_bat == "inactif":
            return True
    elif number_of_ship == 5:
        if joueur.porte_avion.etat_bat == "inactif" and joueur.torpilleur.etat_bat == "inactif" and joueur.croiseur.etat_bat == "inactif" \
                and joueur.canonniere.etat_bat == "inactif" and joueur.destroyer.etat_bat == "inactif":
            return True


def lancement_partie(joueur1: object, joueur2: object,
                     tableau_invisible_joueur1: list, tableau_invisible_joueur2: list,
                     number_of_ships: int):
    """ Fonction servant initialiser et a jouer une partie qui changera en fonction du nombre de bateau
    PRE :
        - joueur1 = objet de classe Joueur
        - joueur2 = objet de classe Joueur
        - tableau_invisible_joueur1 = list
        - tableau_invisible_joueur2 = list
        - number_of_ship = int 1 / 3 / 5
    POST :
        - appel fonction positionner_bateau
        - si number_of_ship == 3 appel fonction petite_partie
        - si number_of_ship == 1 appel fonction test_partie
        - si number_of_ship == 5 appel fonction grande_partie
        - si l'appel de la fonction verif_win renvoie True alors fin de partie print("victoire joueurX")
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

        elif number_of_ships == 1:
            test_partie(joueur1, joueur2, tableau_invisible_joueur1, tableau_invisible_joueur2)

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

    envoi_score(joueur1, joueur2)
    afficher_score(joueur1, joueur2)


def petite_partie(joueur1: object,
                  joueur2: object,
                  tableau_invisible_joueur1: list, tableau_invisible_joueur2: list
                  ):
    """ Fonction correspondant a un tour de jeu complet avec 3 bateaux
    PRE :
        - joueur1 = objet de classe Joueur
        - joueur2 = objet de classe Joueur
        - tableau_invisible_joueur1 = list
        - tableau_invisible_joueur2 = list
    POST :
        - appel fonction tour_de_jeu
        - appel fonction rafraichir_position
        - appel fonction verif_bateau

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
    """ Fonction correspondant a un tout de jeu complet avec 5 bateaux
    :PRE :
        - joueur1 = objet de classe Joueur
        - joueur2 = objet de classe Joueur
        - tableau_invisible_joueur1 = list
        - tableau_invisible_joueur2 = list
    POST :
        - appel fonction tour_de_jeu
        - appel fonction rafraichir_position
        - appel fonction verif_bateau
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


def test_partie(joueur1: object,
                joueur2: object,
                tableau_invisible_joueur1: list, tableau_invisible_joueur2: list
                ):
    """ Fonction correspondant a un tout de jeu complet avec 1 bateaux
    PRE :
        - joueur1 = objet de classe Joueur
        - joueur2 = objet de classe Joueur
        - tableau_invisible_joueur1 = list
        - tableau_invisible_joueur2 = list
    POST :
        - appel fonction tour_de_jeu
        - appel fonction rafraichir_position
        - appel fonction verif_bateau
    """
    print("plateau du joueur 2 : \n")

    tour_de_jeu(joueur1, joueur2, tableau_invisible_joueur2)

    rafraichir_position(joueur2, joueur2.porte_avion)
    verif_bateau(joueur1, joueur2.porte_avion)

    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, joueur1, tableau_invisible_joueur1)

    rafraichir_position(joueur1, joueur1.porte_avion)
    verif_bateau(joueur2, joueur1.porte_avion)
