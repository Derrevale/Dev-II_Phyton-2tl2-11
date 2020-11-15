class Joueur:
    """documentation classe joueur test"""

    def __init__(self, name, board, wallet_amount=150):
        self.nom_joueur = name
        self.plateau_joueur = board
        self.portefeuille_joueur = wallet_amount

    @property
    def name(self):
        return self.nom_joueur