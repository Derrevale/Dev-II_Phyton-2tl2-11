class CreerTableau:
    def __init__(self):
        self.tableau = [
                    ['/ ', 'A', 'B', 'C', 'D', 'E', 'F'],
                    ["--------------------------------"],
                    ['0:', '~', '~', '~', '~', '~', '~'],
                    ['1:', '~', '~', '~', '~', '~', '~'],
                    ['2:', '~', '~', '~', '~', '~', '~'],
                    ['3:', '~', '~', '~', '~', '~', '~'],
                    ['4:', '~', '~', '~', '~', '~', '~'],
                    ['5:', '~', '~', '~', '~', '~', '~'],
                    ["--------------------------------"]
                  ]
        self.ligne = []
        self.nom_joueur = ""

    def afficher_tableau(self, plateau):
        for elements in plateau:
            print(elements)

    def changement_tableau(self):
        pass
