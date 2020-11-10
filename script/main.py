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


def positionner_bateau(x,y,z,j2):
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

        print("Joueur {} le bateau que vous placez est le : {} avec une taille de : {}".format(y.name,bateau.ship_name,
                                                                                                     bateau.ship_size))
        coord_col = input(
            "Joueur {}, veuillez choisir une colonne comme point de départ pour placer le {} : ".format(y.name,
                bateau.ship_name)).upper()
        coord_row = int(input(
            "Joueur {}, veuillez choisir une ligne comme point de départ pour placer le {} : ".format(y.name,
                bateau.ship_name)))
        bateau.position_bateau(coord_col, coord_row, bateau, z)
    x.afficher_tableau(z)
    fin_de_tour=False
    while fin_de_tour==False:
        print("\n\n\n\n\n\n\n\n\nVotre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour=input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour=="O":
            fin_de_tour=True



def debut_partie():
    positionner_bateau(plateau_joueur1,joueur1,list_plateau1)

    positionner_bateau(plateau_joueur2,joueur2,list_plateau2)

    while game_finished == False:
        if tour_joueur == 0:
            print("Plateau du joueur 2 : {}\n".format(joueur2.player_name))
            plateau_joueur2.afficher_tableau(list_plateau2)
            choix_row_joueur1 = int(
                input("Joueur numéro 1 : {}, Veuillez introduire la ligne : ".format(joueur1.player_name)))
            choix_col_joueur1 = input(
                "Joueur numéro 1 : {}, Veuillez introduire la colonne : ".format(joueur1.player_name))
            tir.effectuer_tir(list_plateau2, choix_row_joueur1, choix_col_joueur1.upper())
            plateau_joueur2.afficher_tableau(list_plateau2)
            tour_joueur = tour_joueur + 1

            print("==========================================\n"
                  "==========================================\n"
                  "==========================================\n")

            # if int(input("")) == 99:
            #     game_finished = True
        else:
            print("Plateau du joueur 1: {}\n".format(joueur1.player_name))
            plateau_joueur1.afficher_tableau(list_plateau1)
            choix_row_joueur2 = int(
                input("Joueur numéro 2 : {}, Veuillez introduire la ligne : ".format(joueur2.player_name)))
            choix_col_joueur2 = input(
                "Joueur numéro 2 : {}, Veuillez introduire la colonne : ".format(joueur2.player_name))
            tir.effectuer_tir(list_plateau1, choix_row_joueur2, choix_col_joueur2.upper())
            plateau_joueur1.afficher_tableau(list_plateau1)
            tour_joueur = 0

            print("==========================================\n"
                  "==========================================\n"
                  "==========================================\n")


debut_partie()



