from script.Tableau import *


def nom_de_joueur(x):

    nom_joueur = input("Joueur "+str(x)+", veuillez introduire votre nom : ")
    return nom_joueur

def attribution_COLONNE_tableau():
    nbColonne = int(input("Joueurs, veuillez introduire le nombre de Colonne : (Min 5)"))
    return nbColonne

def attribution_LIGNE_tableau():
    nbLigne = int(input("Joueurs, veuillez introduire le nombre de Ligne : (Min 5)"))
    return nbLigne


