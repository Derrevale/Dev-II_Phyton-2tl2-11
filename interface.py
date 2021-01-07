import pygame
import param_partie
from phase_2_jeu import *


class Interface:
    """
    Classe permettant de créer une fenêtre d'interface.
    """

    def __init__(self, largeur_fenetre: int, hauteur_fenetre: int):
        """
        Constructeur de l'instance de la classe Interface permettant de définir la largeur et la hauteur
        de la fenêtre de l'interface graphique.

        PRE : - largeur_fenetre : int
              - hauteur_fenetre : int
        POST : -self.largeur = largeur_fenetre
               -self.hauteur = hauteur_fenetre

        """
        self.largeur = largeur_fenetre
        self.hauteur = hauteur_fenetre

    def lancement_jeu(self):
        """
        Méthode de classe permettant de lancer le jeu bataille navale en interface graphique.
        PRE : -
        POST : -
        """
        global screen
        coordonnees_plateau = {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
            5: "E",
            6: "F",
            7: "G",
            8: "H",
            9: "I",
            10: "J"
        }
        margin = 35
        hauteur = 20
        largeur = 20
        joueur_auto = param_partie.joueur_auto()
        joueur_adverse = param_partie.joueur_auto()

        # Initialisation de pygame
        pygame.init()

        # Créé une fenêtre avec une certaine hauteur et largeur
        screen = pygame.display.set_mode((self.largeur, self.hauteur))
        screen.fill((255, 255, 255))

        # Nom et icône de la fenêtre
        pygame.display.set_caption("Projet bataille navale")
        icone = pygame.image.load("Images/icone-fenetre.svg")
        pygame.display.set_icon(icone)

        # Images représentant le décor de la fenêtre
        image_bataille_navale = pygame.image.load("Images/image-bataille-navale.svg")
        image_bataille_navale = pygame.transform.scale(image_bataille_navale, (125, 125))
        image_canon = pygame.image.load("Images/canon.svg")
        image_canon = pygame.transform.scale(image_canon, (75, 75))
        image_roulette = pygame.image.load("Images/roulette.svg")
        image_roulette = pygame.transform.scale(image_roulette, (75, 75))
        image_piece = pygame.image.load("Images/piece.svg")
        image_piece = pygame.transform.scale(image_piece, (25, 25))

        # Textes affchés sur la fenêtre
        texte_effectuer_tir = pygame.font.SysFont("Effectuer un tir", 30)
        texte_effectuer_tir = texte_effectuer_tir.render("Effectuer un tir", True, (0, 0, 0))
        texte_nom_du_jeu = pygame.font.SysFont("Bataille navale", 30)
        texte_nom_du_jeu = texte_nom_du_jeu.render("Bataille navale", True, (0, 0, 0))
        texte_vue_premier_ecran = pygame.font.SysFont("Plateau adverse", 30)
        texte_vue_premier_ecran = texte_vue_premier_ecran.render("Plateau adverse", True, (0, 0, 0))
        texte_tourner_roulette = pygame.font.SysFont("Tourner la roulette", 30)
        texte_tourner_roulette = texte_tourner_roulette.render("Tourner la roulette", True, (0, 0, 0))
        texte_prix_roulette = pygame.font.SysFont("150 ", 30)
        texte_prix_roulette = texte_prix_roulette.render("150 ", True, (0, 0, 0))

        # Emplacements pour les différentes actions
        rectangle_action = pygame.Rect((15, 550), (32, 32))
        emplacement_action = pygame.Surface((600, 150))
        rectangle_tir = pygame.Rect((30, 570), (32, 32))
        emplacement_tir = pygame.Surface((275, 100))
        emplacement_tir.fill((255, 0, 0))
        rectangle_roulette = pygame.Rect((325, 570), (32, 32))
        emplacement_roulette = pygame.Surface((275, 100))
        emplacement_roulette.fill((148, 0, 211))

        # Emplacements pour les différents plateaux appartenants aux deux joueurs
        rectangle_plateau1 = pygame.Rect((15, 125), (32, 32))
        emplacement_plateau1 = pygame.Surface((600, 420))
        emplacement_plateau1.fill((0, 191, 255))
        emplacement_plateau2 = pygame.Surface((600, 420))
        emplacement_plateau2.fill((0, 191, 255))
        screen.blit(emplacement_plateau1, rectangle_plateau1)

        victoire = False

        col = 0
        rang = 0
        emplacement_colonne = 0
        emplacement_rangee = 0
        # On créé une grille qui va nous permettre de savoir quand l'une des cases est sélectionnée
        # si la valeur est de 1 dans le tableau, cela signifie qu'une case est sélectionnée et 0 dans le cas contraire.
        grille = []
        for row in range(len(joueur_auto.plateau_joueur.tableau)):
            grille.append([])
            for column in range(len(joueur_auto.plateau_joueur.tableau[row])):
                grille[row].append(0)

        while not victoire:

            screen.blit(emplacement_action, rectangle_action)

            screen.blit(emplacement_tir, rectangle_tir)
            screen.blit(emplacement_roulette, rectangle_roulette)
            screen.blit(texte_effectuer_tir, (50, 610))
            screen.blit(texte_nom_du_jeu, (125, 40))
            screen.blit(texte_vue_premier_ecran, (225, 100))
            screen.blit(texte_tourner_roulette, (340, 600))
            screen.blit(texte_prix_roulette, (400, 630))
            screen.blit(image_bataille_navale, (15, 15))
            screen.blit(image_canon, (225, 575))
            screen.blit(image_roulette, (525, 575))
            screen.blit(image_piece, (440, 625))

            for event in pygame.event.get():
                # Nous récupérons l'événement "quitter" si la croix de la fenêtre est cliquée.
                if event.type == pygame.QUIT:
                    victoire = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Si le bouton de la souris est préssé, nous effectuons les actions suivantes.
                    position = pygame.mouse.get_pos()  # récupère la position de la souris à l'emplacement du clique
                    xpos = position[0]  # récupère la valeur de l'abcisse de la fenêtre
                    ypos = position[1]  # récipère la valeur de l'ordonnéée de la fenêtre

                    if 15 < xpos < 615 and 125 < ypos < 550:
                        # Vérifie si nous sommes bien à l'emplacement de l'affichage du tableau adverse.
                        try:
                            emplacement_colonne = position[0]
                            emplacement_rangee = position[1]

                            col = (position[0] - 100) // (hauteur + margin)
                            rang = (position[1] - 100) // (largeur + margin)
                            if grille[rang][col] == 1:
                                grille[rang][col] = 0
                            else:
                                if 0 < rang < len(joueur_auto.plateau_joueur.tableau):
                                    for x in range(len(grille)):
                                        for y in range(len(grille)):
                                            grille[x][y] = 0
                                    grille[rang][col] = 1
                                else:
                                    raise IndexError
                        except IndexError:
                            print("Nous ne somme pas dans la zone d'attaque")
                    elif 30 < xpos < 300 and 570 < ypos < 670:
                        # définit la zone où il faut cliquer pour atteindre le bouton de tir
                        colo = coordonnees_plateau[col]
                        effectuer_tir(rang - 1, colo, joueur_adverse, joueur_auto)
                        rafraichir_position(joueur_adverse, joueur_adverse.porte_avion, joueur_adverse.torpilleur,
                                            joueur_adverse.croiseur)
                        verif_bateau(joueur_auto, joueur_adverse.porte_avion, joueur_adverse.torpilleur,
                                     joueur_adverse.croiseur)
                        if verif_win(joueur_adverse, 3):
                            victoire = True
                            print("Victoire")

                        if grille[rang][col] == 1:
                            if joueur_auto.plateau_joueur.tableau[rang][col] == "x" or \
                                    joueur_auto.plateau_joueur.tableau[rang][col] == "@":
                                pass
                            else:
                                print("TIR")
                                if joueur_auto.plateau_joueur.tableau[rang][col] == "o":
                                    joueur_auto.plateau_joueur.tableau[rang][col] = "@"
                                    image_feu = pygame.image.load("Images/fire.png")
                                    image_feu = pygame.transform.scale(image_feu, (25, 25))
                                    screen.blit(image_feu, (emplacement_colonne - 10, emplacement_rangee - 10))
                                else:
                                    joueur_auto.plateau_joueur.tableau[rang][col] = "x"
                                    print(joueur_auto.plateau_joueur.tableau)
                                    image_target_x = pygame.image.load("Images/close.png")
                                    image_target_x = pygame.transform.scale(image_target_x, (20, 20))
                                    screen.blit(image_target_x, (emplacement_colonne - 10, emplacement_rangee - 10))

                    # définit la zone où il faut cliquer pour atteindre le bouton de la roulette
                    elif 325 < xpos < 600 and 570 < ypos < 670:
                        print("bouton roulette")

            for rangee in range(1, len(joueur_auto.plateau_joueur.tableau)):
                for colonne in range(1, len(joueur_auto.plateau_joueur.tableau[rangee])):
                    color = (255, 255, 255)
                    if grille[rangee][colonne] == 1:
                        color = (255, 0, 0)
                    # Créé un tableau sur une surface "screen", avec une certaine couleur "color", le rectangle
                    # à dessiner selon des positions et dimensions et également la valeur de la largeur utilisée pour l'
                    # épaisseur de la ligne déssinée
                    pygame.draw.rect(screen, color, [(margin + largeur) * colonne + 100,
                                                     (margin + hauteur) * rangee + 100,
                                                     35,
                                                     35], 1)

            pygame.display.update()
