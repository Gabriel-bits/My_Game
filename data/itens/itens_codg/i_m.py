import pygame
import random

class I_missil(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/itens/i_missel.png")
        self.image = pygame.transform.scale(self.image, [25, 25])
        self.rect = pygame.Rect(10, 10, 25, 25)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

        self.speed = 2 + random.random() * 3


    def update(self, *args):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
