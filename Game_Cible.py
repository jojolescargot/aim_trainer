import pygame
from Cible import Cible
from math import sqrt, log


class Game:

    COLOR = {
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
        "BLACK": (0, 0, 0),
        "PURPLE": (255, 0, 255),
    }
    PLAY = 1
    LOSE = 0

    def __init__(self, window, font):
        self.window = window
        self.taille = self.window.get_size()
        self.font = font
        self.nb_cible = 2
        self.liste_de_cible = []
        self.score = 0
        self.state = self.PLAY
        self.level = 1
        for _ in range(self.nb_cible):
            self.liste_de_cible.append(Cible(self.taille))

    def input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.state == Game.PLAY:
                    for cible in self.liste_de_cible:
                        cible.shoot(event.pos)
                else:
                    self.restart()

    def draw(self):
        self.window.fill(Game.COLOR["BLACK"])

        if self.state == Game.PLAY:
            for cible in self.liste_de_cible:

                pygame.draw.circle(
                    self.window, Game.COLOR["RED"], (cible.x, cible.y), cible.r
                )

            scoretext = self.font.render(
                f"Ton score : {self.score}", 1, Game.COLOR["PURPLE"]
            )
            width, height = scoretext.get_size()
            self.window.blit(scoretext, (self.taille[0] - width, 0))
        elif self.state == Game.LOSE:
            losing_text = self.font.render(
                f"GAME OVER Your Score = {self.score}", 1, Game.COLOR["PURPLE"]
            )
            text_rect = losing_text.get_rect(
                **{"center": (self.taille[0] // 2, self.taille[1] // 2)}
            )
            self.window.blit(losing_text, text_rect)

    def update(self, dt):
        miss = True
        if self.state == Game.PLAY:
            for cible in self.liste_de_cible:
                cible.update(dt)
                if cible.status == Cible.MORT:
                    self.state = Game.LOSE
                    break
                elif cible.status == Cible.HIT:
                    miss = False
                    self.score += 1
                    if self.score % 10 == 0:
                        self.level += 1
                        Cible.temps = Cible.temps / log(self.level)
                    cible.status = Cible.VIVANT
                elif cible.status == Cible.MISS:
                    miss = True and miss
                    cible.status = Cible.VIVANT
                else:
                    miss = False
            if miss:
                self.state = self.LOSE

    def restart(self):
        self.score = 0
        self.level = 1
        self.state = Game.PLAY
        Cible.temps = 0.006
        for x in self.liste_de_cible:
            x.random_init()
            x.status = Cible.VIVANT
