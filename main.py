# ===================================================== #
# imports:                                              #
# ===================================================== #

import os, sys



dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)


import pygame
import random
from data.cogs.win.menu import main_menu
from funs_pers import *
from data.dependencias import *
from pygame.locals import *


'''
 width, height
   x     y

'''

pygame.init()
pygame.mixer.pre_init(44100, -16, 4, 10)


def Fps():
    """
    Mostra o FPS no canto inferior esquerdo.
    """
    ver_fps = clock.get_fps()
    desenhar_text_m(f'FPS: {int(ver_fps)}', (255, 255, 255), tela, 10, 450, 15)

main_menu()

class Game_time_line():

    def __init__(self):
        self.perfil = load_game()
        self.gameLoop = True
        self.gameOver = False
        self.tempo = 0
        self.numero = 0
        self.reset = False
        self.naveGroup = naveGroup
        self.objectGroup = objectGroup
        self.object_backg = object_backg
        self.object_da_tela = object_da_tela
        self.asteroidGroup = asteroidGroup
        self.itens_m = itens_m
        self.itens_l = itens_l
        self.Asteroid = Asteroid()
        self.Nave = Nave()
        self.nave = naveGroup.add(self.Nave)


    def colisao(self):

        self.colisão = pygame.sprite.groupcollide(self.naveGroup, self.asteroidGroup,False, True, pygame.sprite.collide_mask)
        self.i_muniçao = pygame.sprite.groupcollide(self.naveGroup, self.itens_m,False, True, pygame.sprite.collide_mask)
        self.i_life = pygame.sprite.groupcollide(self.naveGroup, self.itens_l,False, True, pygame.sprite.collide_mask)
        self.hits = pygame.sprite.groupcollide(self.Nave.missel_ , self.asteroidGroup ,True , True, pygame.sprite.collide_mask)
        if self.i_muniçao:
            self.perfil["muniçao"] += 1
            Efeito_sonoro.muni()
            
        elif self.i_life:
            self.perfil["life"] += 1         
            Efeito_sonoro.hp()

        elif self.colisão:
            self.perfil["life"] -= 1
            Efeito_sonoro.dano_1()

        if self.perfil["life"] < 1:
            Efeito_sonoro.morte()
            Musicas.stop_music()
            self.gameOver = True

        elif self.hits:
            Efeito_sonoro.esplos_1()


    def estageo(self):

        pygame.init()
        # Musicas.trilha_2()
        backg("data/resource/win/backg.jpg", self.object_backg, tela_dx, tela_dy)
        imag("data/resource/itens/icons/ico_life.png", 35, 35, 20, 35, self.object_da_tela)
        imag("data/resource/itens/icons/ico_missel.png", 35, 38, 20, 80, self.object_da_tela)

        while self.gameLoop:

            # dt = time.time() - last_time
            # dt *= 60
            # pos += 3 * dt

            self.object_backg.draw(tela)
            self.objectGroup.draw(tela)
            self.naveGroup.draw(tela)
            self.Nave.missel_.draw(tela)
            self.object_da_tela.draw(tela)
            self.tempo += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameLoop = False
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not self.gameOver:
                            self.perfil["muniçao"] = self.Nave.missel(perfil=self.perfil)

                    if event.button == 3:
                        print("3")          

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset = True
                        self.Nave.destruir()
                        self.asteroidGroup.empty()
                        self.objectGroup.empty()
                        self.gameLoop = False
                    
                    elif event.key == pygame.K_ESCAPE:
                        main_menu()
    
                    elif event.key == pygame.K_SPACE:
                        if not self.gameOver:
                            self.perfil["muniçao"] = self.Nave.missel(perfil=self.perfil)

            if self.gameOver != True:
                if self.tempo == 1000:
                    print("WINS")

                self.objectGroup.update()
                self.naveGroup.update()
                self.Nave.missel_.update()

                self.colisao()

                self.numero += 1
                if self.numero > 15:
                    self.numero = 0
                    if random.random() < 0.5:
                        newasteroid = Asteroid(self.objectGroup, self.asteroidGroup)

                    elif random.random() < 0.1:
                        newite_m = I_missil(self.objectGroup, self.itens_m)

                    elif random.random() < 0.1:
                        newite_l = I_life(self.objectGroup, self.itens_l)

            desenhar_text_m(f'= {self.perfil["life"]}', (255, 255, 255), tela, 39, 20, 20)
            desenhar_text_m(f'= {self.perfil["muniçao"]}', (255, 255, 255), tela, 39, 75, 20)
            
            Fps()

            clock.tick(framerate)
            pygame.display.flip()

        return self.reset


if __name__ == "__main__":

    while True:
        GAME_LINE = Game_time_line()
        GAME_LINE.estageo()

        if GAME_LINE.reset == True:
                GAME_LINE = Game_time_line()
                GAME_LINE.estageo()


    # while True:
    #     GAME_LINE.estageo()
    #     if GAME_LINE.reset == True:
    # 
    #         print("stage1")
    #         pass









"""
# try:
        
#     if __name__ == "__main__":

#         imag("itens/Life 1.png", 35, 35, 20, 35, object_da_tela)
#         imag("itens/ico_missel.png", 35, 38, 20, 80, object_da_tela)

#         while gameLoop:

#             # dt = time.time() - last_time
#             # dt *= 60
#             last_time = time.time()
#             object_backg.draw(tela)
#             objectGroup.draw(tela)
#             object_da_tela.draw(tela)
#             # pos += 3 * dt
#             tempo += 1
        
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     gameLoop = False
#                 elif event.type == pygame.MOUSEBUTTONDOWN:
#                     if event.button == 1:
#                         if not gameOver:
#                             if perfil["muniçao"] > 0:
#                                 for i in range(1):
#                                     Efeito_sonoro.missel()
#                                     newtiro = Missil(objectGroup, tiroGrop)
#                                     newtiro.rect.center = nave.rect.center
#                                     perfil["muniçao"] -= 1
#                     if event.button == 3:
#                         print("3")          

#                 elif event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_ESCAPE:
#                         gameLoop = False

#                     elif event.key == pygame.K_SPACE:
#                         if not gameOver:
#                             if perfil["muniçao"] > 0:
#                                 Efeito_sonoro.missel()
#                                 newtiro = Missil(objectGroup, tiroGrop)
#                                 newtiro.rect.center = nave.rect.center
#                                 perfil["muniçao"] -= 1 
            
#             if gameOver != True:

#                 if tempo == 1000:
#                     print("WINS")
                    
#                 objectGroup.update()
                
#                 colisão = pygame.sprite.spritecollide(nave, asteroidGroup, True, pygame.sprite.collide_mask)
#                 i_muniçao = pygame.sprite.spritecollide(nave, itens_m, True, pygame.sprite.collide_mask)
#                 i_life = pygame.sprite.spritecollide(nave, itens_l, True, pygame.sprite.collide_mask)
#                 hits = pygame.sprite.groupcollide(tiroGrop , asteroidGroup ,True , True, pygame.sprite.collide_mask)

#                 if i_muniçao:
#                     perfil["muniçao"] += 1
#                     Efeito_sonoro.muni()

#                 elif i_life:
#                     perfil["life"] += 1         
#                     Efeito_sonoro.hp()

#                 elif colisão:
#                     perfil["life"] -= 1
#                     Efeito_sonoro.dano_1()

#                 if perfil["life"] < 1:
#                     Efeito_sonoro.morte()
#                     Musicas.stop_music()
#                     gameOver = True

#                 elif hits:
#                     misil.esplosao()
#                     Efeito_sonoro.esplos_1()

#                 numero += 1
#                 if numero > 15:
#                     numero = 0
#                     if random.random() < 0.5:
#                         newasteroid = Asteroid(objectGroup, asteroidGroup)

#                     elif random.random() < 0.1:
#                         newite_m = I_missil(objectGroup, itens_m)

#                     elif random.random() < 0.1:
#                         newite_l = I_life(objectGroup, itens_l)

#             desenhar_text_m(f'= {perfil["life"]}', (255, 255, 255), tela, 39, 20, 20)
#             desenhar_text_m(f'= {perfil["muniçao"]}', (255, 255, 255), tela, 39, 75, 20)
#             Fps()

#             clock.tick(framerate)
#             pygame.display.update()

# except Exception as __erro:
#     print(__erro)
#     pass
"""