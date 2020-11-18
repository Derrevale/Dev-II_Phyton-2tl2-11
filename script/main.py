
from script.Tableau import *
from script.Joueur import *
from script.Bateau import *

from script.outils import *

# Initialisation des valeurs par défaut
partie_finie = False
partie_gagnee = False
tour_joueur = 0

# Initialisation des noms de joueurs
nom_joueur1 = nom_de_joueur(1)
nom_joueur2 = nom_de_joueur(2)

# Attribution des dimensions du tableau
ligne_MAX = attribution_COLONNE_tableau()
colonne_MAX = attribution_LIGNE_tableau()

# Attribution du nombre(s) de bateau(x) dans la partie
number_of_ships = attribution_NOMBRE_bateau()

# Création des tableaux des joueurs
plateau_joueur1 = CreerTableau(colonne_MAX,ligne_MAX)
plateau_joueur1.creation_tableau()

plateau_joueur2 = CreerTableau(colonne_MAX,ligne_MAX)
plateau_joueur2.creation_tableau()

# Attribution des plateaux a une liste ////// je ne sais pas ou ça sert
liste_plateau1 = plateau_joueur1.tableau
liste_plateau2 = plateau_joueur2.tableau

# Création des tableau vide
tableau_invisible_joueur1 = []
tableau_invisible_joueur2 = []

# Attribution du nom et de leur tableau au joueurs
joueur1 = Joueur(nom_joueur1, plateau_joueur1)
joueur2 = Joueur(nom_joueur2, plateau_joueur2)





debut_partie(plateau_joueur1, joueur1, liste_plateau1,
             plateau_joueur2, joueur2, liste_plateau2,
             tableau_invisible_joueur1,tableau_invisible_joueur2,
             number_of_ships)
