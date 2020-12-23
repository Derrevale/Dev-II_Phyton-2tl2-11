class Joueur:
    """documentation classe joueur"""

    def __init__(self, nom: str, plateau: object, montant_portefeuille=150):
        """
        fonction d'initialisation de l'objet Joueur
        :param nom: string correspondant au nom du joueur
        :param plateau: objet Tableau
        :param montant_portefeuille: integer correspondant a la richesse du joueur
        """
        self.nom_joueur = nom
        self.plateau_joueur = plateau
        self.portefeuille_joueur = montant_portefeuille
        self.nom_des_bateaux = []
        self.score = 2000

    @property
    def nom(self):
        return self.nom_joueur

    def __add__(self, other):
        self.portefeuille_joueur = self.portefeuille_joueur + int(other)
        self.score = self.portefeuille_joueur + int(other)

    def __sub__(self, other):
        self.portefeuille_joueur = self.portefeuille_joueur - int(other)
        self.score = self.portefeuille_joueur - int(other)
