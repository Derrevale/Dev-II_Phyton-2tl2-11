#interface pygame
import pygame

BLANC = (200, 200, 200)
BRUN = (160, 82, 45)


class Interface:
    def __init__(self, largeur_fenetre: int, hauteur_fenetre: int):
        self.largeur = largeur_fenetre
        self.hauteur = hauteur_fenetre

    def lancement_jeu(self):
        """

        :return:
        """
        global screen
        NOIR = (0,0,0)

        #Initialisation de pygame
        pygame.init()
        pygame.font.init()

        #Créé une fenêtre avec une certaine hauteur et largeur
        screen = pygame.display.set_mode((self.largeur, self.hauteur))

        #Nom de la fenêtre et icône
        pygame.display.set_caption("Projet bataille navale")
        icone = pygame.image.load("Images/icone-fenetre.svg")
        pygame.display.set_icon(icone)

        #Images représentant le décor de la fenêtre
        image_bataille_navale = pygame.image.load("Images/image-bataille-navale.svg")
        image_bataille_navale = pygame.transform.scale(image_bataille_navale, (125,125))
        image_canon = pygame.image.load("Images/canon.svg")
        image_canon = pygame.transform.scale(image_canon, (75,75))
        image_roulette = pygame.image.load("Images/roulette.svg")
        image_roulette = pygame.transform.scale(image_roulette, (75,75))
        image_piece = pygame.image.load("Images/piece.svg")
        image_piece = pygame.transform.scale(image_piece, (25,25))

        #Textes
        texte_effectuer_tir = pygame.font.SysFont("Effectuer un tir", 30)
        texte_effectuer_tir = texte_effectuer_tir.render("Effectuer un tir", True, (0, 0, 0))
        texte_nom_du_jeu = pygame.font.SysFont("Bataille navale", 30)
        texte_nom_du_jeu = texte_nom_du_jeu.render("Bataille navale", True, (0,0,0))
        texte_vue_premier_ecran = pygame.font.SysFont("Plateau adverse", 30)
        texte_vue_premier_ecran = texte_vue_premier_ecran.render("Plateau adverse", True, (0,0,0))
        texte_vue_deuxieme_ecran = pygame.font.SysFont("Votre plateau", 30)
        texte_vue_deuxieme_ecran = texte_vue_deuxieme_ecran.render("Votre plateau", True, (0,0,0))
        texte_tourner_roulette = pygame.font.SysFont("Tourner la roulette", 30)
        texte_tourner_roulette = texte_tourner_roulette.render("Tourner la roulette", True, (0,0,0))
        texte_etat_bateaux = pygame.font.SysFont("États des bateaux", 30)
        texte_etat_bateaux = texte_etat_bateaux.render("États des bateaux : ", True, (0,0,0))
        texte_prix_roulette = pygame.font.SysFont("150 ", 30)
        texte_prix_roulette = texte_prix_roulette.render("150 ", True, (0,0,0))

        rectangle_action = pygame.Rect((15, 550), (32, 32))
        emplacement_action = pygame.Surface((600,150))
        emplacement_action.fill(BRUN)
        rectangle_action2 = pygame.Rect((665, 550), (32,32))
        emplacement_action2 = pygame.Surface((600,150))
        emplacement_action2.fill(BRUN)
        rectangle_tir = pygame.Rect((30,570), (32,32))
        emplacement_tir = pygame.Surface((275,100))
        emplacement_tir.fill((255,0,0))
        rectangle_roulette = pygame.Rect((325,570), (32,32))
        emplacement_roulette = pygame.Surface((275,100))
        emplacement_roulette.fill((148,0,211))

        #Emplacements pour les différents plateaux appartenants aux deux joueurs
        rectangle_plateau1 = pygame.Rect((15,125), (32,32))
        emplacement_plateau1 = pygame.Surface((600, 420))
        emplacement_plateau1.fill((0,191,255))
        rectangle_plateau2 = pygame.Rect((665,125), (32,32))
        emplacement_plateau2 = pygame.Surface((600, 420))
        emplacement_plateau2.fill((0,191,255))

        en_cours = True

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
            screen.fill(BLANC)

            pygame.draw.line(screen, (70,130,180), (640, 0), (640, 800), 10)
            screen.blit(emplacement_action, rectangle_action)
            screen.blit(emplacement_action2, rectangle_action2)
            screen.blit(emplacement_plateau1, rectangle_plateau1)
            screen.blit(emplacement_plateau2, rectangle_plateau2)
            screen.blit(emplacement_tir, rectangle_tir)
            screen.blit(emplacement_roulette, rectangle_roulette)
            screen.blit(texte_effectuer_tir, (50, 610))
            screen.blit(texte_nom_du_jeu, (125, 40))
            screen.blit(texte_vue_premier_ecran, (225, 100))
            screen.blit(texte_vue_deuxieme_ecran, (900, 100))
            screen.blit(texte_tourner_roulette, (340,600))
            screen.blit(texte_etat_bateaux, (700, 560))
            screen.blit(texte_prix_roulette, (400,630))
            screen.blit(image_bataille_navale, (15, 15))
            screen.blit(image_canon, (225, 575))
            screen.blit(image_roulette, (525, 575))
            screen.blit(image_piece, (440, 625))
            x,y = pygame.mouse.get_pos()
            print(f"je suis x {x}")
            print(f"je suis y {y}")

            self.CreerGrille()
            pygame.display.update()


    def CreerGrille(self, surface, grid):
        taille_blocks = 45
        for x in range(len(grid)):
            for y in range(grid[x]):
                pygame.draw.rect(surface, grid[x][y], (top_left))

