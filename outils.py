from tableau import *
from action import *
import copy



def nom_de_joueur(x):
    # Fonction d'attribution des noms
    nom_joueur = input("\nJoueur " + str(x) + ", veuillez introduire votre nom : ")
    return nom_joueur

def attribution_COLONNE_tableau():
    # Fonction d'attribution du nombre de colonne max
    nbColonne = int(input("\nJoueurs, veuillez introduire le nombre de Colonne (Min 5, Max 12, Default 6) :"))
    if (nbColonne > 12):
        print("\nvaleur trop haute , attribution par defaut")
        nbColonne = 6
    elif (nbColonne < 5):
        print("\nvaleur trop basse , attribution par defaut")
        nbColonne = 6
    print("\nNombre de COLONNE :", nbColonne)
    return nbColonne


def attribution_LIGNE_tableau():
    # Fonction d'attribution du nombre de ligne max
    nbLigne = int(input("\nJoueurs, veuillez introduire le nombre de Ligne (Min 5, Max 12, Default 6) :"))
    if (nbLigne > 12):
        print("\nvaleur trop haute , attribution par defaut")
        nbLigne = 6
    elif (nbLigne < 5):
        print("\nvaleur trop basse , attribution par defaut")
        nbLigne = 6
    print("\nNombre de LIGNE :", nbLigne)
    return nbLigne


def attribution_NOMBRE_bateau():
    # Fonction d'attribution du nombres de bateaux
    nbBateau = int(
        input("Joueurs, veuillez introduire le nombre de bateau lors de la partie  (Min 1, Max 3, Default 3) :"))
    if (nbBateau > 3):
        print("\nvaleur trop haute , attribution par defaut")
        nbBateau = 3
    elif (nbBateau < 1):
        print("\nvaleur trop basse , attribution par defaut")
        nbBateau = 1
    print("\nNombre de BATEAU :", nbBateau)
    return nbBateau


def plateau_invisible_adversaire(plateau_invisible, plateau_a_copier):
    plateau_invisible = copy.deepcopy(plateau_a_copier)
    for elements in range(len(plateau_invisible)):
        for ele in range(len(plateau_invisible[elements])):
            if plateau_invisible[elements][ele] == "o":
                plateau_invisible[elements][ele] = "~"
    for elements in plateau_invisible:
        print(elements)


def tour_de_jeu(x, y, z, adversaire, plateau_invisible):
    # x = joueur actuel
    # z = listeplateau joueur adverse

    while True:
        try:
            plateau_invisible_adversaire(plateau_invisible, z)
            plateau_invisible_adversaire(plateau_invisible, z)
            choix_col_joueur = input(
                "Joueur : {}, Veuillez introduire la colonne : ".format(x.nom))
            choix_rangee_joueur = int(
                input("Joueur : {}, Veuillez introduire la ligne : ".format(x.nom)))
            effectuer_tir(z, choix_rangee_joueur, choix_col_joueur.upper(), adversaire)
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


def positionner_bateau(x, y, z, number_of_ships):
    # x = plateau_joueur1 ou plateau_joueur2
    # y = joueur_1 ou 2
    # z = listeplateau 1 ou 2
    for elements in range(1, number_of_ships + 1):
        x.afficher_tableau(z)
        if elements == 1:
            porte_avion = Bateau("porte-avion", 3)
            y.porte_avion = porte_avion
            y.nom_des_bateaux.append("porte-avion")
            bateau = porte_avion

        elif elements == 2:
            torpilleur = Bateau("torpilleur", 2)
            y.torpilleur = torpilleur
            y.nom_des_bateaux.append("torpilleur")
            bateau = torpilleur
        else:
            croiseur = Bateau("croiseur", 2)
            y.croiseur = croiseur
            y.nom_des_bateaux.append("croiseur")
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
            nom_du_bateau.etat_bateau = "Touché"
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


def verif_win(y,number_of_ship):
    # y = joueur_1 ou 2
    if number_of_ship == 3:
        if y.porte_avion.etat_bateau and y.torpilleur.etat_bateau and y.croiseur.etat_bateau == "inactif":
            return True
    elif number_of_ship == 2:
        if y.porte_avion.etat_bateau and y.torpilleur.etat_bateau == "inactif":
            return True
    elif number_of_ship == 1:
        if y.porte_avion.etat_bateau == "inactif":
            return True

def debut_partie(plateau_joueur1, joueur1, liste_plateau1,
                 plateau_joueur2, joueur2, liste_plateau2,
                 tableau_invisible_joueur1, tableau_invisible_joueur2,
                 number_of_ships):
    victoire = False

    positionner_bateau(plateau_joueur1, joueur1, liste_plateau1, number_of_ships)
    positionner_bateau(plateau_joueur2, joueur2, liste_plateau2, number_of_ships)


    while victoire == False:

        if number_of_ships == 3:
            verif_3_BATEAUX(plateau_joueur1, joueur1, liste_plateau1,
                             plateau_joueur2, joueur2, liste_plateau2,
                             tableau_invisible_joueur1, tableau_invisible_joueur2,
                             )

        elif number_of_ships == 2:
            verif_2_BATEAUX(plateau_joueur1, joueur1, liste_plateau1,
                             plateau_joueur2, joueur2, liste_plateau2,
                             tableau_invisible_joueur1, tableau_invisible_joueur2,
                             )

        elif number_of_ships == 1:
            verif_1_BATEAUX(plateau_joueur1, joueur1, liste_plateau1,
                             plateau_joueur2, joueur2, liste_plateau2,
                             tableau_invisible_joueur1, tableau_invisible_joueur2,
                             )

        if verif_win(joueur2,number_of_ships) == True:
            victoire = True
            print("le joueur 1 a gagné")

        if verif_win(joueur1,number_of_ships) == True:
            victoire = True
            print("le joueur 2 a gagné")


def verif_3_BATEAUX(plateau_joueur1, joueur1, liste_plateau1,
                    plateau_joueur2, joueur2, liste_plateau2,
                    tableau_invisible_joueur1, tableau_invisible_joueur2,
                    ):
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

def verif_2_BATEAUX(plateau_joueur1, joueur1, liste_plateau1,
                    plateau_joueur2, joueur2, liste_plateau2,
                    tableau_invisible_joueur1, tableau_invisible_joueur2,
                    ):
    print("plateau du joueur 2 : \n")
    tour_de_jeu(joueur1, plateau_joueur2, liste_plateau2, joueur2, tableau_invisible_joueur2)
    rafraichir_position(liste_plateau2, joueur2.porte_avion)
    verif_bateau(joueur2.porte_avion, joueur1)
    rafraichir_position(liste_plateau2, joueur2.torpilleur)
    verif_bateau(joueur2.torpilleur, joueur1)


    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, plateau_joueur1, liste_plateau1, joueur1, tableau_invisible_joueur1)
    rafraichir_position(liste_plateau1, joueur1.porte_avion)
    verif_bateau(joueur1.porte_avion, joueur2)
    rafraichir_position(liste_plateau1, joueur1.torpilleur)
    verif_bateau(joueur1.torpilleur, joueur2)

def verif_1_BATEAUX(plateau_joueur1, joueur1, liste_plateau1,
                    plateau_joueur2, joueur2, liste_plateau2,
                    tableau_invisible_joueur1, tableau_invisible_joueur2,
                    ):
    print("plateau du joueur 2 : \n")
    tour_de_jeu(joueur1, plateau_joueur2, liste_plateau2, joueur2, tableau_invisible_joueur2)
    rafraichir_position(liste_plateau2, joueur2.porte_avion)
    verif_bateau(joueur2.porte_avion, joueur1)


    print("plateau du joueur 1 : \n")
    tour_de_jeu(joueur2, plateau_joueur1, liste_plateau1, joueur1, tableau_invisible_joueur1)
    rafraichir_position(liste_plateau1, joueur1.porte_avion)
    verif_bateau(joueur1.porte_avion, joueur2)


