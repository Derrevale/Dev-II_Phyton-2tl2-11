# Importation des fonctions depuis action.py
from action import *
from interface import *
from param_partie import *
# Importation permettant de récuperer les arguments utilisé lors de l'appel du code
import sys


# Initialisation des valeur par défaut


partie_finie = False
partie_gagnee = False
tour_joueur = 0
type_de_partie = "console"

# Fonction qui se lance lors du lancement du script pour selectionner si mode console ou gui
if __name__ == '__main__':
    # Vérification du nombre d'arguments nécessaire
    if len(sys.argv) < 2:
        print("Précisez une un mode de jeu en paramètre\nconsole/gui")
        sys.exit(1)

    argument = sys.argv[1]

    if argument == "console":
    # Partie en mode console
        print("On démarre en mode console")
        # Attribution du style de bataille (nombre de colonne et de ligne)
        dimension_tableau = selection_type_partie_console()

        # Attribution du nombre de bateau en fonction du style de bataille (petite ou grande)
        nombre_bateau = selection_nombre_bateau(dimension_tableau)

        # Attribution de nom de joueur
        nom_joueur1 = nom_de_joueur(1)
        nom_joueur2 = nom_de_joueur(2)

        tableau_invisible_joueur1 = []
        tableau_invisible_joueur2 = []

        # Création des 2 joueurs et de leurs tableaux
        joueur1 = creation_tableau_joueur(dimension_tableau, nom_joueur1)
        joueur2 = creation_tableau_joueur(dimension_tableau, nom_joueur2)

        debut_partie(joueur1,joueur2,tableau_invisible_joueur1,tableau_invisible_joueur2,nombre_bateau)

    elif argument == "gui":
    # Partie en mode GUI
        print("On démarre en mode gui")
        interface_jeu = Interface(1280,800)
        interface_jeu.lancement_jeu()
    else:
        print("Mode de jeu inconnu.\nPrécisez une un mode de jeu en paramètre\nconsole/gui")

    print("script par défaut")
