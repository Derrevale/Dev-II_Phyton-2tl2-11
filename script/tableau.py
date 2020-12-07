#dictionnaire ppour pouvoir attribuer une lettre a un chiffre
rep = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l'}

class CreerTableau:
    """documentation classe Creer_Tableau"""
    def __init__(self, dimension_tableau):
        self.dimension_tableau = dimension_tableau
        self.colonne = []
        self.tableau = []
        self.nom_joueur = ""

    def creation_tableau(self):
        myColonne=[]
        for i in range(self.dimension_tableau):
            if i==0:
                myColonne.append('/')
            myColonne.append(rep[i].upper())
        self.tableau.append(myColonne)
        for i in range(self.dimension_tableau):
            myLigne=[]
            for j in range(len(self.tableau[0])-1):
                if j==0:

                    myLigne.append(str(i))
                myLigne.append('~')
            self.tableau.append(myLigne)

