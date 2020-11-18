from script.Actions import *
from script.Tableau import *
from script.Joueur import *
from script.Bateau import *
import copy

partie_finie = False
partie_gagnee = False
tour_joueur = 0

plateau_joueur1 = CreerTableau(5,5)
plateau_joueur1.creation_tableau()
plateau_joueur2 = CreerTableau(5,5)

liste_plateau1 = plateau_joueur1.tableau
liste_plateau2 = plateau_joueur2.tableau

tableau_invisible_joueur1 = []
tableau_invisible_joueur2 = []


def plateau_invisible_adversaire(plateau_invisible, plateau_a_copier):
    plateau_invisible = copy.deepcopy(plateau_a_copier)
    for elements in range(len(plateau_invisible)):
        for ele in range(len(plateau_invisible[elements])):
            if plateau_invisible[elements][ele] == "o":
                plateau_invisible[elements][ele] = "~"
    for elements in plateau_invisible:
        print(elements)


tir = Actions()

nom_joueur1 = input("Joueur 1, veuillez introduire votre nom : ")
nom_joueur2 = input("Joueur 2, veuillez introduire votre nom : ")

joueur1 = Joueur(nom_joueur1, plateau_joueur1)
joueur2 = Joueur(nom_joueur2, plateau_joueur2)
number_of_ships = 3


def positionner_bateau(x, y, z):
    # x = plateau_joueur1 ou plateau_joueur2
    # y = joueur_1 ou 2
    # z = listeplateau 1 ou 2
    for elements in range(1, number_of_ships + 1):
        x.afficher_tableau(z)
        if elements == 1:
            porte_avion = Bateau("porte-avion", 3)
            y.porte_avion = porte_avion
            bateau = porte_avion

        elif elements == 2:
            torpilleur = Bateau("torpilleur", 2)
            y.torpilleur = torpilleur
            bateau = torpilleur
        else:
            croiseur = Bateau("croiseur", 2)
            y.croiseur = croiseur
            bateau = croiseur
        print("Joueur {} le bateau que vous placez est le : {} avec une taille de : {}".format(y.nom, bateau.nom_bateau,
                                                                                               bateau.taille_bateau))
        while True:
            try:
                coord_col = input(
                    "Joueur {}, veuillez choisir une colonne comme point de départ pour placer le {} : ".format(y.nom,
                                                                                                                bateau.nom_bateau)).upper()
                coord_rangee = int(input(
                    "Joueur {}, veuillez choisir une ligne comme point de départ pour placer le {} : ".format(y.nom,
                                                                                                              bateau.nom_bateau)))
                bateau.position_bateau(coord_col, coord_rangee, bateau, z)
            except KeyError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
                continue
            except ValueError:
                print("Erreur, veuillez introduire des coordonnées valides\n")
                continue
            else:
                break
    print(y.nom_joueur)
    print(y.porte_avion.coordonnees_bateau)
    x.afficher_tableau(z)
    fin_de_tour = False
    while fin_de_tour == False:
        print("Votre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour = input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour == "O" or valid_fin_de_tour == "OUI":
            fin_de_tour = True


def verif_bateau(nom_du_bateau, x):
    counter = []
    for elements in range(nom_du_bateau.taille_bateau):
        if nom_du_bateau.etat_bateau == "inactif":
            print("ce bateau a déjà été détruit")
            break
        if nom_du_bateau.coordonnees_bateau[elements][2] == "@":
            print("{} est endommagé".format(nom_du_bateau.nom_bateau))
            counter.append("@")
            if len(counter) == nom_du_bateau.taille_bateau:
                nom_du_bateau.etat_bateau = "inactif"
                if nom_du_bateau.etat_bateau == "inactif":
                    x.portefeuille_joueur = x.portefeuille_joueur + 150
                    print(x.portefeuille_joueur)
                else:
                    print("pas encore")
    print("L'état du bateau {} est le suivant : {} ".format(nom_du_bateau.nom_bateau, nom_du_bateau.etat_bateau))


def rafraichir_position(z, nom_du_bateau):
    for elements in range(nom_du_bateau.taille_bateau):
        col = nom_du_bateau.coordonnees_bateau[elements][1]
        rangee = nom_du_bateau.coordonnees_bateau[elements][0]
        if z[rangee][col] == "@":
            nom_du_bateau.coordonnees_bateau[elements][2] = "@"
    print(nom_du_bateau.coordonnees_bateau)


def verif_win(y):
    # y = joueur_1 ou 2
    if y.porte_avion.etat_bateau and y.torpilleur.etat_bateau and y.croiseur.etat_bateau== "inactif":
        return True


def debut_partie():
    positionner_bateau(plateau_joueur1, joueur1, liste_plateau1)
    positionner_bateau(plateau_joueur2, joueur2, liste_plateau2)
    victoire = False
    print(joueur1.porte_avion.coordonnees_bateau)
    print(joueur2.porte_avion.coordonnees_bateau)

    while victoire == False:
        print("plateau du joueur 2 : \n")
        tour_de_jeu(joueur1, plateau_joueur2, liste_plateau2, joueur2, tableau_invisible_joueur2)
        rafraichir_position(liste_plateau2, joueur2.porte_avion)
        verif_bateau(joueur2.porte_avion, joueur1)
        rafraichir_position(liste_plateau2, joueur2.torpilleur)
        verif_bateau(joueur2.torpilleur, joueur1)
        rafraichir_position(liste_plateau2, joueur2.croiseur)
        verif_bateau(joueur2.croiseur, joueur1)

        print("plateau du joueur 1 : \n")
        tour_de_jeu(joueur2, plateau_joueur1, liste_plateau1, joueur1, tableau_invisible_joueur1)
        rafraichir_position(liste_plateau1, joueur1.porte_avion)
        verif_bateau(joueur1.porte_avion, joueur2)
        rafraichir_position(liste_plateau1, joueur1.torpilleur)
        verif_bateau(joueur1.torpilleur, joueur2)
        rafraichir_position(liste_plateau1, joueur1.croiseur)
        verif_bateau(joueur1.croiseur, joueur2)

        if verif_win(joueur2) == True:
            victoire = True
            print("le joueur 1 a gagné")

        if verif_win(joueur1) == True:
            victoire = True
            print("le joueur 2 a gagné")


def tour_de_jeu(x, y, z, adversaire, plateau_invisible):
    # x = joueur actuel
    # z = listeplateau joueur adverse

    while True:
        try:
            plateau_invisible_adversaire(plateau_invisible, z)
            tir.coup_special(x, z)
            plateau_invisible_adversaire(plateau_invisible, z)
            choix_col_joueur = input(
                "Joueur : {}, Veuillez introduire la colonne : ".format(x.nom))
            choix_rangee_joueur = int(
                input("Joueur : {}, Veuillez introduire la ligne : ".format(x.nom)))
            tir.effectuer_tir(z, choix_rangee_joueur, choix_col_joueur.upper(), adversaire)
        except KeyError:
            print("Erreur, veuillez introduire des coordonnées valides\n")
            continue
        except ValueError:
            print("Erreur, veuillez introduire des coordonnées valides\n")
            continue
        else:
            plateau_invisible_adversaire(plateau_invisible, z)
            break

    print("==========================================\n"
          "==========================================\n"
          "==========================================\n")


debut_partie()
