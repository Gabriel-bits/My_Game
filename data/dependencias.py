import pygame, time
from funs_pers import *
from asteroid import Asteroid
from missel import Missil
from nave import Nave
from data.itens.itens_codg.i_m import I_missil
from data.itens.itens_codg.i_l import I_life


# ===================================================== #
# Tela:                                                 #
# ===================================================== #

pygame.init()
tela = pygame.display.set_mode([840, 480])
pygame.display.set_caption("Meu Jogo")

# ===================================================== #
# Variaveis:                                            #
# ===================================================== #

tela_dx = 840
tela_dy = 480
tela_d = [840, 480]
tempo = 0
pos = 0
framerate = 100
gameLoop = True
gameOver = False
click = False
numero = 10


clock = pygame.time.Clock()
last_time = time.time()
keys = pygame.key.get_pressed()
Mause = pygame.mouse.get_pressed(num_buttons=3)
mj = pygame.time.get_ticks()


# ===================================================== #
# Variaveis para diretoris:                             #
# ===================================================== #

TELA = "tela/"
MUSIC = "música/"
SOUDS = "souds/"
PERSO = "personagens/"

# ===================================================== #
# Grupos de object/sprits:                                #
# ===================================================== #




objectGroup = pygame.sprite.Group()
object_backg = pygame.sprite.Group()
object_da_tela = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
tiroGrop = pygame.sprite.Group()
objectaleatori = pygame.sprite.Group()
itens_m = pygame.sprite.Group()
itens_l = pygame.sprite.Group()

Bots_opcoes = pygame.sprite.Group()
Bots_menu = pygame.sprite.Group()


# ===================================================== #
# Personagem and object:                                #
# ===================================================== #

misil = Missil(tiroGrop)
nave = Nave(objectGroup)
asteroid = Asteroid(asteroidGroup)
iten_mu = I_missil(itens_m)

#======================{FIM}======================#











#logica antiga--------------------------#
'''
        if not gameOver:

            objectGroup.update()
            colisão = pygame.sprite.spritecollide(nave, asteroidGroup, True, pygame.sprite.collide_mask)
            i_muniçao = pygame.sprite.spritecollide(nave, itens_m, True, pygame.sprite.collide_mask)
            i_life = pygame.sprite.spritecollide(nave, itens_l, True, pygame.sprite.collide_mask)
            hits = pygame.sprite.groupcollide(tiroGrop , asteroidGroup ,True, True, pygame.sprite.collide_mask)

            if i_muniçao:
                muniçao += 1
                Efeito_sonoro.muni()

            elif i_life:
                life_ += 1         
                Efeito_sonoro.hp()

            elif colisão:
                life_ -= 1
                Efeito_sonoro.dano_1()
      
            elif life_ == 0:
                Efeito_sonoro.morte()

                gameOver = True

            elif hits:
                Efeito_sonoro.esplos_1()

            numero += 1
            if numero > 15:
                numero = 0
                if random.random() < 0.5:
                    newasteroid = Asteroid(objectGroup, asteroidGroup)

                elif random.random() < 0.1:
                    newite_m = I_missil(objectGroup, itens_m)

                elif random.random() < 0.01:
                    newite_l = I_life(objectGroup, itens_l)
'''