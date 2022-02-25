import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/resource/enemies/asteroid.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [110, 70])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

        self.speed = 2 + random.random() * 3

    def destruir(self):
        self.kill()

    def update(self):
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
