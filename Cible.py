import random


class Cible:

    temps = 0.006
    VIVANT = 1
    MISS = 2
    MORT = 0
    HIT = 3

    def __init__(self, taille):
        self.taille = taille
        self.tempo = 0
        self.status = Cible.VIVANT
        self.random_init()

    def random_init(self):
        self.r = 40
        self.x = random.randint(self.r, self.taille[0] - self.r)
        self.y = random.randint(self.r, self.taille[1] - self.r)
        self.tempo = 0

    def update(self, dt):
        self.tempo += dt
        if self.status == Cible.HIT:
            self.random_init()
        elif self.status == Cible.MISS or self.status == Cible.VIVANT:
            if self.tempo >= Cible.temps:
                self.r -= 0.1
                self.tempo = 0
            if self.r <= 0:
                self.status = Cible.MORT
        else: 
            pass


    def shoot(self, pos):
        if (pos[0] - self.x) * (pos[0] - self.x) + (pos[1] - self.y) * (
            pos[1] - self.y
        ) <= self.r * self.r:
            self.status = Cible.HIT
        else:
            self.status = Cible.MISS
        
        



