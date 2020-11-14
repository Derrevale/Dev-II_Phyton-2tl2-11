from script.Actions import *
from script.Tableau import *
from script.Joueur import *
from script.Bateau import *
import copy

game_finished = False
game_won = False
tour_joueur = 0

plateau_joueur1 = CreerTableau()
plateau_joueur2 = CreerTableau()

list_plateau1 = plateau_joueur1.tableau
list_plateau2 = plateau_joueur2.tableau

tableau_invisible_joueur1 = []
tableau_invisible_joueur2 = []


def plateau_invisible_adversaire(invisible_board, board_to_copy):
    invisible_board = copy.deepcopy(board_to_copy)
    for elements in range(len(invisible_board)):
        for ele in range(len(invisible_board[elements])):
            if invisible_board[elements][ele] == "o":
                invisible_board[elements][ele] = "~"
    for elements in invisible_board:
        print(elements)




tir = Actions()

player_name1 = input("Joueur 1, veuillez introduire votre nom : ")
player_name2 = input("Joueur 2, veuillez introduire votre nom : ")

joueur1 = Joueur(player_name1, plateau_joueur1)
joueur2 = Joueur(player_name2, plateau_joueur2)
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

        print("Joueur {} le bateau que vous placez est le : {} avec une taille de : {}".format(y.name, bateau.ship_name,
                                                                                               bateau.ship_size))
        coord_col = input(
            "Joueur {}, veuillez choisir une colonne comme point de départ pour placer le {} : ".format(y.name,
                                                                                                        bateau.ship_name)).upper()
        coord_row = int(input(
            "Joueur {}, veuillez choisir une ligne comme point de départ pour placer le {} : ".format(y.name,
                                                                                                      bateau.ship_name)))
        bateau.position_bateau(coord_col, coord_row, bateau, z)
    print(y.porte_avion.ship_coordinates)
    x.afficher_tableau(z)
    fin_de_tour = False
    while fin_de_tour == False:
        print("Votre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour = input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour == "O" or valid_fin_de_tour == "OUI":
            fin_de_tour = True


def debut_partie():
    victoire=False

    positionner_bateau(plateau_joueur1, joueur1, list_plateau1)
    positionner_bateau(plateau_joueur2, joueur2, list_plateau2)
    while victoire==False:
        tour_de_jeu(joueur1, plateau_joueur2, list_plateau2,joueur2, tableau_invisible_joueur2)
        tour_de_jeu(joueur2, plateau_joueur1, list_plateau1,joueur1, tableau_invisible_joueur1)


def tour_de_jeu(x, y, z,adversaire, board_invisible):
    # x = joueur actuel
    # y = plateau joueur adverse
    # z = listeplateau joueur adverse

    plateau_invisible_adversaire(board_invisible, z)
    tir.coup_special(x, z)
    plateau_invisible_adversaire(board_invisible, z)
    print("Plateau du joueur : {}\n".format(x.name))
    choix_col_joueur = input(
        "Joueur : {}, Veuillez introduire la colonne : ".format(x.name))
    choix_row_joueur = int(
        input("Joueur : {}, Veuillez introduire la ligne : ".format(x.name)))
    tir.effectuer_tir(z, choix_row_joueur, choix_col_joueur.upper(),adversaire)
    plateau_invisible_adversaire(board_invisible, z)


    print("==========================================\n"
          "==========================================\n"
          "==========================================\n")


debut_partie()