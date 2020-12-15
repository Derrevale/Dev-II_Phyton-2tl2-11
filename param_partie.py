from joueur import Joueur
from tableau import Tableau


def nom_de_joueur(x: int):
    """
    fonction servant a recuperer un str donner par l'utilisateur
    :param x: integer correspondant au numero du joueur
    :return: un string correspondant a nom_joueur
    """
    # Fonction d'attribution des noms
    nom_joueur = input("\nJoueur " + str(x) + ", veuillez introduire votre nom : ")
    return nom_joueur


def selection_type_partie_console():
    """
    fonction permettant a l'utilisateur de choisir le type de partie grande/petite
    :return: un integer nombre_ligne_colonne correspondant au dimension du tableau
    """
    petite_bat = "P"
    grande_bat = "G"
    lancement = False
    style_partie = input(
        "Choisisez le style de partie que vous voulez jouez."
        "\nGrande Bataille (10*10 , 5 Bateaux)"
        "\nPetite Bataille (06*06 , 3 Bateaux)"
        "\nG/P\n")

    # verification que la valeur entrée est correcte
    while not lancement:

        if style_partie.upper() == petite_bat:
            lancement = True
            nombre_ligne_colonne = 5

        elif style_partie.upper() == grande_bat:
            lancement = True
            nombre_ligne_colonne = 10
        else:
            print("erreur")
            style_partie = input(
                "Le choix entrez est incorecte veuillez réintroduire."
                "\nGrande Bataille (10*10 , 5 Bateaux)"
                "\nPetite Bataille (06*06 , 3 Bateaux)"
                "\nG/P\n")
    return nombre_ligne_colonne


def selection_nombre_bateau(x: int):
    """
    fonction servant a attribuer le nombre de bateau en fonction de la dimension du tableau de jeu
    :param x: integer correspondant au dimension tu tableau
    :return: un integer correspondant au nombre de bateau dans la partie
    """
    nombre_bateau = 0
    if x == 5:
        nombre_bateau = 3
    elif x == 10:
        nombre_bateau = 5

    return nombre_bateau


def creation_tableau_joueur(dimension: int, nom_joueur: str):
    """
    fonction servant a creer un objet Tableau et un objet Joueur et attribuer a Joueur le tableau
    :param dimension: integer correspondant aux dimension du tableau de jeu
    :param nom_joueur: string correspondant au nom entrer par le joueur
    :return: objet Joueur possedant un nom et un objet Tableau contenant un tableau de la taille de la dimension donnee
    """
    plateau_joueur = Tableau(dimension)
    plateau_joueur.creation_tableau()
    return Joueur(nom_joueur, plateau_joueur)
