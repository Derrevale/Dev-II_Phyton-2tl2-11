from script.Actions import *
from script.Tableau import *
from script.Joueur import *
from script.Bateau import *
import copy

partie_finie = False
partie_gagnee = False
tour_joueur = 0

plateau_joueur1 = CreerTableau()
plateau_joueur2 = CreerTableau()

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
number_of_ships = 1


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
            y.croiseur=croiseur
            bateau = croiseur

        print("Joueur {} le bateau que vous placez est le : {} avec une taille de : {}".format(y.name, bateau.nom_bateau,
                                                                                               bateau.taille_bateau))
        coord_col = input(
            "Joueur {}, veuillez choisir une colonne comme point de départ pour placer le {} : ".format(y.name,
                                                                                                        bateau.nom_bateau)).upper()
        coord_rangee = int(input(
            "Joueur {}, veuillez choisir une ligne comme point de départ pour placer le {} : ".format(y.name,
                                                                                                      bateau.nom_bateau)))
        bateau.position_bateau(coord_col, coord_rangee, bateau, z)
    print(y.porte_avion.coordonnees_bateau)
    x.afficher_tableau(z)
    fin_de_tour = False
    while fin_de_tour == False:
        print("Votre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour = input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour == "O" or valid_fin_de_tour == "OUI":
            fin_de_tour = True


def debut_partie():
    victoire=False

    positionner_bateau(plateau_joueur1, joueur1, liste_plateau1)
    positionner_bateau(plateau_joueur2, joueur2, liste_plateau2)
    while victoire==False:
        tour_de_jeu(joueur1, plateau_joueur2, liste_plateau2, joueur2, tableau_invisible_joueur2)
        tour_de_jeu(joueur2, plateau_joueur1, liste_plateau1, joueur1, tableau_invisible_joueur1)


def tour_de_jeu(x, y, z,adversaire, plateau_invisible):
    # x = joueur actuel
    # y = plateau joueur adverse
    # z = listeplateau joueur adverse

    plateau_invisible_adversaire(plateau_invisible, z)
    tir.coup_special(x, z)
    plateau_invisible_adversaire(plateau_invisible, z)
    print("Plateau du joueur : {}\n".format(x.name))
    choix_col_joueur = input(
        "Joueur : {}, Veuillez introduire la colonne : ".format(x.name))
    choix_rangee_joueur = int(
        input("Joueur : {}, Veuillez introduire la ligne : ".format(x.name)))
    tir.effectuer_tir(z, choix_rangee_joueur, choix_col_joueur.upper(),adversaire)
    print(z)
    plateau_invisible_adversaire(plateau_invisible, z)


    print("==========================================\n"
          "==========================================\n"
          "==========================================\n")


debut_partie()