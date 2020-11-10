from script.Actions import *
from script.Tableau import *
from script.Joueur import *
from script.Bateau import *

game_finished = False
game_won = False
tour_joueur = 0

plateau_joueur1 = CreerTableau()
plateau_joueur2 = CreerTableau()
plateau_invisible_joueur1 = CreerTableau().tableau
plateau_invisible_joueur2 = CreerTableau().tableau

list_plateau1 = plateau_joueur1.tableau
list_plateau2 = plateau_joueur2.tableau

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
            bateau = Bateau("porte-avion", 3)
        elif elements == 2:
            bateau = Bateau("torpilleur", 2)
        else:
            bateau = Bateau("croiseur", 2)

        print("Joueur {} le bateau que vous placez est le : {} avec une taille de : {}".format(y.name, bateau.ship_name,
                                                                                               bateau.ship_size))
        coord_col = input(
            "Joueur {}, veuillez choisir une colonne comme point de départ pour placer le {} : ".format(y.name,
                                                                                                        bateau.ship_name)).upper()
        coord_row = int(input(
            "Joueur {}, veuillez choisir une ligne comme point de départ pour placer le {} : ".format(y.name,
                                                                                                      bateau.ship_name)))
        bateau.position_bateau(coord_col, coord_row, bateau, z)
    x.afficher_tableau(z)
    fin_de_tour = False
    while fin_de_tour == False:
        print("Votre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour = input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour == "O" or valid_fin_de_tour == "OUI":
            fin_de_tour = True


def debut_partie():
    positionner_bateau(plateau_joueur1, joueur1, list_plateau1)
    positionner_bateau(plateau_joueur2, joueur2, list_plateau2)
    tour_de_jeu(joueur1,plateau_joueur2, list_plateau2)
    tour_de_jeu(joueur2, plateau_joueur1, list_plateau1)

def tour_de_jeu(x, y, z):
    # x = joueur actuel
    # y = plateau joueur adverse
    # z = listeplateau joueur adverse

    print("Plateau du joueur : {}\n".format(x.name))
    y.afficher_tableau(z)
    choix_col_joueur = input(
        "Joueur : {}, Veuillez introduire la colonne : ".format(x.name))
    choix_row_joueur = int(
        input("Joueur : {}, Veuillez introduire la ligne : ".format(x.name)))
    tir.effectuer_tir(z, choix_row_joueur, choix_col_joueur.upper())

    y.afficher_tableau(z)

    print("==========================================\n"
          "==========================================\n"
          "==========================================\n")


debut_partie()
