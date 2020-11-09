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
number_of_ships = 3

for elements in range(1, number_of_ships + 1):
    plateau_joueur1.afficher_tableau(list_plateau1)
    coord_col = input("Joueur numéro 1, veuillez choisir une colonne comme point de départ pour placer le bateau numéro {} : ".format(elements))
    coord_row = int(input("Joueur numéro 1, veuillez choisir une rangée comme point de départ pour placer le bateau numéro {} : ".format(elements)))
    porte_avion = Bateau("porte-avion", 3)
    porte_avion.position_bateau(coord_col, coord_row,porte_avion, list_plateau1)



plateau_joueur1.afficher_tableau(list_plateau1)

while game_finished == False:
    if tour_joueur == 0:
        print("Plateau du joueur 2 : {}\n".format(joueur2.player_name))
        plateau_joueur2.afficher_tableau(list_plateau2)
        choix_row_joueur1 = int(input("Joueur numéro 1 : {}, Veuillez introduire la rangée : ".format(joueur1.player_name)))
        choix_col_joueur1 = input("Joueur numéro 1 : {}, Veuillez introduire la colonne : ".format(joueur1.player_name))
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
        choix_row_joueur2 = int(input("Joueur numéro 2 : {}, Veuillez introduire la rangée : ".format(joueur2.player_name)))
        choix_col_joueur2 = input("Joueur numéro 2 : {}, Veuillez introduire la colonne : ".format(joueur2.player_name))
        tir.effectuer_tir(list_plateau1, choix_row_joueur2, choix_col_joueur2.upper())
        plateau_joueur1.afficher_tableau(list_plateau1)
        tour_joueur = 0

        print("==========================================\n"
              "==========================================\n"
              "==========================================\n")




