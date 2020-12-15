from joueur import Joueur
from tableau import CreerTableau


def nom_de_joueur(x: int):
    # Fonction d'attribution des noms
    nom_joueur = input("\nJoueur " + str(x) + ", veuillez introduire votre nom : ")
    return nom_joueur


def selection_type_partie_console():
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
    nombre_bateau = 0
    if x == 5:
        nombre_bateau = 3
    elif x == 10:
        nombre_bateau = 5

    return nombre_bateau

def creation_tableau_joueur(dimension: int, nom_joueur: str):
    plateau_joueur = CreerTableau(dimension)
    plateau_joueur.creation_tableau()
    return Joueur(nom_joueur, plateau_joueur)
