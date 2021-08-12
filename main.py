# ===================================================== #
# imports:                                              #
# ===================================================== #
import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

import pygame, sys
import random
import time
from menu import*
from funs_pers import *
from data.dependencias import *
from nave import Nave
from missel import Missil
from asteroid import Asteroid
from pygame import mixer_music

# from data.itens.itens_codg.i_l import I_life
# from data.itens.itens_codg.i_m import I_missil
# from data.música.music_codg.musicas import Musicas
# from data.souds.souds_codg.souds import Efeito_sonoro


# ===================================================== #
# Lembretes:                                            #
# ===================================================== #
'''
 width, height
   x     y

'''
# ===================================================== #
# inicialização da janela:                              #
# ===================================================== #

pygame.init()
pygame.mixer.pre_init(44100, -16, 4, 10)

# ===================================================== #
# Personagem and object:                                #
# ===================================================== #


# ===================================================== #
# Draw, text and background:                            #
# ===================================================== #

def Fps():
    """
    Mostra o FPS no canto enferior esquerdo.
    """
    ver_fps = clock.get_fps()
    desenhar_text_m(f'FPS: {int(ver_fps)}', (255, 255, 255), tela, 10, 450, 15)

backg(TELA+"backg.jpg", object_backg, tela_dx, tela_dy)

# ===================================================== #
# Music:                                                #
# ===================================================== #

Musicas.trilha_1()

# =====================================================#
# Sounds:                                              #
# =====================================================#

pygame.mixer.set_num_channels(4)
pygame.mixer.set_reserved(3)
pygame.mixer.set_reserved(2)
pygame.mixer.set_reserved(1)

# =====================================================#
# loop:                                                #
# =====================================================#

#Novo_game()
perfil = load_game()

try:
        
    if __name__ == "__main__":

        imag("itens/Life 1.png", 35, 35, 20, 35, object_da_tela)
        imag("itens/ico_missel.png", 35, 38, 20, 80, object_da_tela)

        while gameLoop:

            # dt = time.time() - last_time
            # dt *= 60
            last_time = time.time()
            object_backg.draw(tela)
            objectGroup.draw(tela)
            object_da_tela.draw(tela)
            # pos += 3 * dt
            tempo += 1
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if not gameOver:
                            if perfil["muniçao"] > 0:
                                for i in range(1):
                                    Efeito_sonoro.missel()
                                    newtiro = Missil(objectGroup, tiroGrop)
                                    newtiro.rect.center = nave.rect.center
                                    perfil["muniçao"] -= 1
                    if event.button == 3:
                        print("3")          

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameLoop = False

                    elif event.key == pygame.K_SPACE:
                        if not gameOver:
                            if perfil["muniçao"] > 0:
                                Efeito_sonoro.missel()
                                newtiro = Missil(objectGroup, tiroGrop)
                                newtiro.rect.center = nave.rect.center
                                perfil["muniçao"] -= 1 
            
            if gameOver != True:

                if tempo == 1000:
                    print("WINS")
                    
                objectGroup.update()
                
                colisão = pygame.sprite.spritecollide(nave, asteroidGroup, True, pygame.sprite.collide_mask)
                i_muniçao = pygame.sprite.spritecollide(nave, itens_m, True, pygame.sprite.collide_mask)
                i_life = pygame.sprite.spritecollide(nave, itens_l, True, pygame.sprite.collide_mask)
                hits = pygame.sprite.groupcollide(tiroGrop , asteroidGroup ,True , True, pygame.sprite.collide_mask)

                if i_muniçao:
                    perfil["muniçao"] += 1
                    Efeito_sonoro.muni()

                elif i_life:
                    perfil["life"] += 1         
                    Efeito_sonoro.hp()

                elif colisão:
                    perfil["life"] -= 1
                    Efeito_sonoro.dano_1()

                if perfil["life"] < 1:
                    Efeito_sonoro.morte()
                    Musicas.stop_music()
                    gameOver = True

                elif hits:
                    misil.esplosao()
                    Efeito_sonoro.esplos_1()

                numero += 1
                if numero > 15:
                    numero = 0
                    if random.random() < 0.5:
                        newasteroid = Asteroid(objectGroup, asteroidGroup)

                    elif random.random() < 0.1:
                        newite_m = I_missil(objectGroup, itens_m)

                    elif random.random() < 0.1:
                        newite_l = I_life(objectGroup, itens_l)

            desenhar_text_m(f'= {perfil["life"]}', (255, 255, 255), tela, 39, 20, 20)
            desenhar_text_m(f'= {perfil["muniçao"]}', (255, 255, 255), tela, 39, 75, 20)
            Fps()

            clock.tick(framerate)
            pygame.display.update()

except Exception as __erro:
    print(__erro)