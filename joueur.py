class Joueur:
    """Classe joueur représentant un Joueur d'une partie de Bataille Navale"""

    def __init__(self, nom: str, plateau: object, montant_portefeuille=250):
        """fonction d'initialisation de l'objet Joueur

        PRE :
            - nom: string
            - plateau: objet Tableau
            - montant_portefeuille: integer correspondant a la richesse du joueur
        POST :
            - self.nom_joueur = nom
            - self.plateau_joueur = plateau
            - self.portefeuille_joueur = montant_portefeuille
            - self.nom_des_bateaux = []
            - self.score = 2000
        """
        self.nom_joueur = nom
        self.plateau_joueur = plateau
        self.portefeuille_joueur = montant_portefeuille
        self.nom_des_bateaux = []
        self.score = 2000

    @property
    def nom(self):
        return self.nom_joueur

    def __add__(self, other: int):
        """Surcharge de l'operateur + pour Joueur

        PRE :
            self = objet Fraction
            other = integer
         POST : self.score + other
        """
        self.score = self.score + int(other)

    def __sub__(self, other: int):
        """Surcharge de l'operateur - pour Joueur

        PRE :
            - self = objet Fraction
            - other = integer
        POST : self.score - other
        """
        self.score = self.score - int(other)
