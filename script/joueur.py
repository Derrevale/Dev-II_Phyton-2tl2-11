from bateau import *


class Joueur():
    """documentation classe joueur test"""

    def __init__(self, nom, plateau, montant_portefeuille=150):
        self.nom_joueur = nom
        self.plateau_joueur = plateau
        self.portefeuille_joueur = montant_portefeuille
        self.nom_des_bateaux=[]

    @property
    def nom(self):
        return self.nom_joueur