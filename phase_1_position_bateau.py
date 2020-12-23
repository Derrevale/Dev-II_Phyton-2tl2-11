from bateau import Bateau


def afficher_tableau(tableau: list):
    """
    fonction servant a afficher chaque valeur d'un tableau
    :param tableau: list
    :return: aucun
    """
    for elements in tableau:
        print(elements)


def positionner_bateau(joueur: object, number_of_ships: int):
    """
    fonction permettant au joueur de placer ses bateaux
    :param joueur: objet Joueur correspondant au joueur qui dois placer son tableau
    :param number_of_ships: integer correspondant au nombre de bateau dans la partie
    :return: aucun
    :raises: IndexError si la valeur est hors list
    :raises: KeyError si la valeur n'est pas du bon type
    :raises: ValueError si la valeur n'est pas disponible

    """

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
            joueur.canonniere = canonniere
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

                if horizontal_ou_vertical != "h" and horizontal_ou_vertical != "v":
                    raise ValueError

                bateau.position_bateau_verif(coord_col, coord_rangee, bateau, joueur.plateau_joueur.tableau,
                                             horizontal_ou_vertical)
            except (IndexError, KeyError, ValueError):
                print("Erreur, veuillez introduire des coordonnées valides\n")
            else:

                bateau.position_bateau(coord_col, coord_rangee, bateau, joueur.plateau_joueur.tableau,
                                       horizontal_ou_vertical)

                break

    afficher_tableau(joueur.plateau_joueur.tableau)

    fin_de_tour = False
    while not fin_de_tour:
        print("Votre tour est fini , le joueur suivant peut s'installer devant l'ordinateur...\n\n\n")
        valid_fin_de_tour = input("joueur suivant êtes vous prêt o/n\n\n").upper()
        if valid_fin_de_tour == "O" or valid_fin_de_tour == "OUI":
            fin_de_tour = True
