from bateau import Bateau


def afficher_tableau(tableau: list):
    """ Fonction servant a afficher chaque valeur d'un tableau
    PRE : -tableau = list
    POST : print(elements) quand elements est dans tableau
    """
    for elements in tableau:
        print(elements)


def positionner_bateau(joueur: object, number_of_ships: int):
    """ Fonction permettant au joueur de placer ses bateaux
    PRE :
        - joueur = objet de classe Joueur
        - number_of_ships = integer
    POST :
        - appel afficher_tableau(joueur.plateau_joueur.tableau)
        - boucle elements quand elements = range(1,nombre_of_ship+1)
        - si element == 1
            - creation objet Bateau porte_avion
            - attribution porte_avion a joueur

        - si element == 2
            - creation objet Bateau torpilleur
            - attribution torpilleur a joueur

        - si element == 3
            - creation objet Bateau croiseur
            - attribution croiseur a joueur

        - si element == 4
            - creation objet Bateau cannonniere
            - attribution cannoniere a joueur

        - si element == 5
            - creation objet Bateau destroyer
            - attribution destroyer a joueur

        - appel fonction position_bateau_verif
        - appel fonction positionner_bateau
        - appel afficher_tableau(joueur.plateau_joueur.tableau) quand un bateau est positionner
    RAISE:
        - IndexError si la valeur > list
        - KeyError si la valeur != str
        - ValueError la valeur != str

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
