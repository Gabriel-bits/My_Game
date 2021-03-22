import pygame
from funs_pers import * 

class Nave(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        sprit_sheet = pygame.image.load("data/personagens/Nave_Sheet.png")
        self.animaçao_nave = []
        
        for i in range(6):
            imag = sprit_sheet.subsurface((i * 62, 0), (62,37))
            imag = pygame.transform.scale(imag, [110, 70])
            self.animaçao_nave.append(imag)

        self.index_lista = 0
        self.image = self.animaçao_nave[int(self.index_lista)]
        self.rect = pygame.Rect(450, 150, 100, 100)
        
    
    def update(self):
        keys = pygame.key.get_pressed()
        
        if self.index_lista > 5:
            self.index_lista = 0
        self.index_lista += 0.25    
        self.image = self.animaçao_nave[int(self.index_lista)]
        
        if keys[pygame.K_d]:
            self.rect.x += 3
        if keys[pygame.K_a]:
            self.rect.x -= 3
        if keys[pygame.K_s]:
            self.rect.y += 3
        if keys[pygame.K_w]:
            self.rect.y -= 3
        
        elif keys[pygame.K_LSHIFT]:

            if keys[pygame.K_d]:
                self.rect.x += 5
            if keys[pygame.K_a]:
                self.rect.x -= 5


        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        if self.rect.bottom > 510:
            self.rect.bottom = 510
            self.speed = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0
        if self.rect.right > 830:
            self.rect.right = 830
            self.speed = 0

            

        # self.image = pygame.image.load("data/personagens/Nave.png")
        # self.image = pygame.transform.scale(self.image, [110, 70])
        # self.rect = pygame.Rect(450, 150, 100, 100)
        # self.speed = 0
        # self.acceleration = 0.1
        
        