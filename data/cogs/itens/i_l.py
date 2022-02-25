import pygame
import random

class I_life(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        # self.image = pygame.image.load("data/itens/i_life.png")
        # self.image = pygame.transform.scale(self.image, [25, 25])
        # self.rect = pygame.Rect(10, 10, 25, 25)

        sprit_sheet = pygame.image.load("data/resource/itens/i_life_Sheet.png")
        self.animaçao = []
        
        for i in range(8):
            imag = sprit_sheet.subsurface((i * 12, 0), (12 ,12))
            imag = pygame.transform.scale(imag, [25, 25])
            self.animaçao.append(imag)

        self.index_lista = 0
        self.image = self.animaçao[int(self.index_lista)]
        self.rect = pygame.Rect(10, 10, 25, 25)
        
#=========================================================================#

        self.rect.x = 840 + random.randint(1, 400)
        self.rect.y = random.randint(1, 400)

        self.speed = 2 + random.random() * 3


    def update(self):
        
        if self.index_lista > 7:
            self.index_lista = 0
        self.index_lista += 0.15
        self.image = self.animaçao[int(self.index_lista)]

        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()
