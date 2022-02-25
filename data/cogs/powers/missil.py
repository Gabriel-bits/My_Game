import pygame
import random
from data.dependencias import *

class Missil(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # self.image = pygame.image.load("data/personagens/missil.png")
        # self.image = pygame.transform.scale(self.image, [20, 20])
        # self.rect = pygame.Rect(10, 10, -20, -14)
        # self.speed = 6

        sprit_sheet = pygame.image.load("data/resource/powers/missil/Missil_Sheet.png").convert_alpha()
        self.animaçao_missil_defalt = []
       
        for i in range(4):
            imag = sprit_sheet.subsurface((i * 40, 0), (40, 14))
            imag = pygame.transform.scale(imag, [25*2, 13*2])
            self.animaçao_missil_defalt.append(imag)
            
             
        for i in range(4):
            imag = sprit_sheet.subsurface((i * 40, 14), (40, 14))
            imag = pygame.transform.scale(imag, [25*2, 13*2])
            self.animaçao_missil_defalt.append(imag)
            

        self.index_lista = 0
        self.image = self.animaçao_missil_defalt[int(self.index_lista)]
        self.rect = pygame.Rect(10, 10, -20, -14)
        self.rect.center = pos
        self.speed = 6
        
        self.animar = False
#================================================================================#

        # sprit_sheet_e = pygame.image.load("data/personagens/Esplosao-Sheet.png")
        # self.animaçao_missil_es = []
        
        # for i in range(4):
        #     imag2 = sprit_sheet_e.subsurface((i * 40, 0), (40, 14))
        #     imag2 = pygame.transform.scale(imag2, [25*2, 13*2])
        #     self.animaçao_missil_es.append(imag2)

        # self.index_lista2 = 0
        # self.image = self.animaçao_missil_es[int(self.index_lista2)]
        # self.rect = pygame.Rect(10, 10, 10, 10)
        # self.speed = 6
        # self.animar = None


    def esplosao(self):
        self.animar = True
        #print(self.animar)

        self.index_lista = 4
        self.image = self.animaçao_missil_defalt[int(self.index_lista)] 
        return self.animar

    def logic(self):

        if self.animar == True:
            print(1)
            if self.index_lista > 7:
                self.index_lista = 0
                self.kill
            self.index_lista += 0.80 
            self.image = self.animaçao_missil_defalt[int(self.index_lista)]


        if self.animar == False:
            if self.index_lista > 3:
                self.index_lista = 0
            self.index_lista += 0.20  
            self.image = self.animaçao_missil_defalt[int(self.index_lista)]
            
        self.rect.x += self.speed
        if self.rect.left > 840:
            self.kill()

    def update(self):
        self.logic()
