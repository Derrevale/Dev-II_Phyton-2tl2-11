from joueur import Joueur
from tableau import Tableau
from bateau import Bateau


def nom_de_joueur(x: int):
    """ Fonction servant a recuperer un str donner par l'utilisateur
    PRE : X = int
    POST: un string correspondant a nom_joueur
    """
    # Fonction d'attribution des noms
    nom_joueur = input("\nJoueur " + str(x) + ", veuillez introduire votre nom : ")
    return nom_joueur


def selection_type_partie_console():
    """ Fonction permettant a l'utilisateur de choisir le type de partie grande/petite
    PRE : -
    POST :
        - recupère style_partie str "P" "TEST" "G"
        - boucle si style_partie différent de "P" "TEST" "G"
        - retourne nombre_ligne_colonne = int 5 / 10 / 8
    """
    petite_bat = "P"
    grande_bat = "G"
    test_bat = "TEST"
    lancement = False
    nombre_ligne_colonne = 5
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

        elif style_partie.upper() == test_bat:
            lancement = True
            nombre_ligne_colonne = 8
        else:
            print("erreur")
            style_partie = input(
                "Le choix entrez est incorecte veuillez réintroduire."
                "\nGrande Bataille (10*10 , 5 Bateaux)"
                "\nPetite Bataille (06*06 , 3 Bateaux)"
                "\nG/P\n")
    return nombre_ligne_colonne


def selection_nombre_bateau(x: int):
    """ Fonction servant a attribuer le nombre de bateau en fonction de la dimension du tableau de jeu
    PRE : x = integer
    POST :
        - nombre_bateau = 3 si x == 5
        - nombre_bateau = 1 si x == 8
        - nombre_bateau = 5 si x == 10
        - retourne nombre_bateau
    """
    nombre_bateau = 0
    if x == 5:
        nombre_bateau = 3
    elif x == 8:
        nombre_bateau = 1
    elif x == 10:
        nombre_bateau = 5

    return nombre_bateau


def creation_tableau_joueur(dimension: int, nom_joueur: str):
    """ Fonction servant a creer un objet Tableau et un objet Joueur et attribuer a Joueur le tableau
    PRE:
        - dimension = int
        - nom_joueur = str
    POST :
        - création objet plateau_joueur de classe Tableau(dimension)
        - creation d'un tableau dans l'objet plateau_joueur
        - creation d'un objet Joueur possedant un nom et un objet Tableau
        - retourne l'objet de classe Joueur
    """
    plateau_joueur = Tableau(dimension)
    plateau_joueur.creation_tableau()
    return Joueur(nom_joueur, plateau_joueur)


def joueur_auto():
    """ Fonction de création d'un joueur complet avec ses bateaux leur positions et un tableau précompléter

    PRE : -
    POST :
        - joueur1 = objet de classe Joueur(plateau_joueur(6 * 6) nom_joueur = "nom_joueur1")
        - porte_avion = objet de classe Bateau(nom_bateau = "porte_avion" taille = 4)
        - croiseur = objet de classe Bateau(nom_bateau = "croiseur" taille = 2)
        - torpilleur = objet de classe Bateau(nom_bateau = "torpilleur" taille = 2)
        - appel fonction position_bateau pour porte_avion,torpilleur,croiseur
        - joueur1.porte_avion = objet de classe Bateau porte_avion
        - joueur1.torpilleur = objet de classe Bateau torpilleur
        - joueur1.croiseur = objet de classe Bateau croiseur
        - retourne objet de classe Joueur joueur1
    """
    joueur1 = creation_tableau_joueur(6, "nom_joueur1")
    porte_avion = Bateau("porte_avion", 4)
    croiseur = Bateau("croiseur", 2)
    torpilleur = Bateau("torpilleur", 2)
    porte_avion.position_bateau("A", 0, porte_avion, joueur1.plateau_joueur.tableau, "h")
    croiseur.position_bateau("A", 2, croiseur, joueur1.plateau_joueur.tableau, "h")
    torpilleur.position_bateau("A", 4, torpilleur, joueur1.plateau_joueur.tableau, "h")
    joueur1.porte_avion = porte_avion
    joueur1.torpilleur = torpilleur
    joueur1.croiseur = croiseur
    return joueur1
