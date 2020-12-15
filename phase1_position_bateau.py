from bateau import Bateau


def afficher_tableau(tableau: list):
    for elements in tableau:
        print(elements)


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