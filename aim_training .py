import pygame
from Game_Cible import Game


pygame.init()

TAILLE = (500, 600)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("monospace", 20)

lauched = True


game = Game(screen, myfont)

while lauched:
    dt = clock.tick() / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lauched = False
        else:
            game.input(event)

    game.update(dt)

    game.draw()

    pygame.display.update()
