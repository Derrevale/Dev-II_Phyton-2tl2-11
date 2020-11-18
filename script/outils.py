from script.Tableau import *

def nom_de_joueur(x):
    # Fonction d'attribution des noms
    nom_joueur = input("\nJoueur "+str(x)+", veuillez introduire votre nom : ")
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
    print("\nNombre de COLONNE :",nbColonne)
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
    print("\nNombre de LIGNE :",nbLigne)
    return nbLigne

def attribution_NOMBRE_bateau():
    # Fonction d'attribution du nombres de bateaux
    nbBateau = int(input("Joueurs, veuillez introduire le nombre de bateau lors de la partie  (Min 1, Max 3, Default 3) :"))
    if(nbBateau>3):
        print("\nvaleur trop haute , attribution par defaut")
        nbBateau=3
    elif(nbBateau<1):
        print("\nvaleur trop basse , attribution par defaut")
        nbBateau=1
    print("\nNombre de BATEAU :",nbBateau)
    return nbBateau



