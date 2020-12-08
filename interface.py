#interface pygame
import pygame

largeur = 1280
hauteur = 800
BLANC = (200,200,200)
test_couleur = (160,82,45)
NOIR = (0,0,0)
#Initialisation de pygame
pygame.init()
#Créé une fenêtre avec une certaine hauteur et largeur

screen = pygame.display.set_mode((largeur, hauteur))
#Nom de la fenêtre et icône
pygame.display.set_caption("Projet bataille navale")
icone = pygame.image.load("Images/icone-fenetre.svg")
pygame.display.set_icon(icone)

rectangle_action = pygame.Rect((15, 500), (32, 32))
emplacement_action = pygame.Surface((600,150))
emplacement_action.fill(test_couleur)
rectangle_action2 = pygame.Rect((665, 500), (32,32))
emplacement_action2 = pygame.Surface((600,150))
emplacement_action2.fill(test_couleur)
rectangle_plateau1 = pygame.Rect((15,75), (32,32))
emplacement_plateau1 = pygame.Surface((600, 420))
emplacement_plateau1.fill((0,191,255))
rectangle_plateau2 = pygame.Rect((665,75), (32,32))
emplacement_plateau2 = pygame.Surface((600, 420))
emplacement_plateau2.fill((0,191,255))
rectangle_tir = pygame.Rect((30,525), (32,32))
emplacement_tir = pygame.Surface((275,100))
emplacement_tir.fill((255,0,0))



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
    pygame.display.flip()
    pygame.display.update()