from script.Bateau import *


class Joueur(Bateau):
    """documentation classe joueur test"""

    def __init__(self, nom, plateau, montant_portefeuille=150):
        self.nom_joueur = nom
        self.plateau_joueur = plateau
        self.portefeuille_joueur = montant_portefeuille

    @property
    def nom(self):
        return self.nom_joueur