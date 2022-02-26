# importações ----------------------------------------------- #
import pygame, sys
from pygame.locals import *

from data.dependencias import *
from funs_pers import backg,imag,b_imag,desenhar_text_m,Loading
from data.cogs.win.telas import * 


# janela, inicializações ---------------------------------------- #

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16, 2, 4096)
pygame.mixer.music.set_volume(0.05222)

objectGroup = pygame.sprite.Group()
Bots_opcoes = pygame.sprite.Group()
Bots_menu = pygame.sprite.Group()


backg("data/resource/win/backg.jpg", object_backg, tela_dx, tela_dy)




def game():
    tempo = 0
    running = True
    while running:
        pygame.sprite.Group().update()
        object_backg.draw(tela)
        objectGroup.draw(tela)

        desenhar_text_m('Loading...', (255, 255, 255), tela, 20, 450, 25)
        
        for event in pygame.event.get():
    
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        objectaleatori.empty()
        Loading()
        if tempo == 10:
            tempo = 0
            return
            
        tempo += 1
        pygame.display.update()
        clock.tick(60)

def options():
    n = 0
    running = True
    Bots_menu.empty()
    while running:
        pygame.sprite.Group().update()
        object_backg.draw(tela)
        objectGroup.draw(tela)
        Bots_menu.draw(tela)
        desenhar_text_m('opcoes', (255, 255, 255), tela, 30, 20, 30)
        b_imag("data/resource/bottons/layout_.png", 170, 70, -10, 10, Bots_menu)

        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                        
        clock.tick(60)
        pygame.display.update()

def main_menu():
    while True:
        pygame.sprite.Group().update()
        object_backg.draw(tela)
        objectGroup.draw(tela)
        objectaleatori.draw(tela)
        Bots_menu.draw(tela)

        mx, my = pygame.mouse.get_pos()          
        b_imag("data/resource/players/Nave.png",110, 70, 450, 150, objectaleatori)
        b_imag("data/resource/bottons/layout_.png", 170, 70, -10, 10, Bots_menu)

        desenhar_text_m('Menu', (255, 255, 255), tela, 30, 20, 30)
        desenhar_text_m('Play..', (255, 255, 255), tela, 87, 127, 30)
        desenhar_text_m('Opcoes', (255, 255, 255), tela, 87, 227, 30)

        button_1 = b_imag("data/resource/bottons/Layout.png", 180, 65, 55, 103, Bots_menu)
        button_2 = b_imag("data/resource/bottons/Layout.png", 180, 65, 55, 203, Bots_menu)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        try:
            if button_1.collidepoint((mx, my)):
                if click:
                    Efeito_sonoro.b_1()
                    game()
                    return
            if button_2.collidepoint((mx, my)):
                if click:
                    Efeito_sonoro.b_1()
                    options()
        except UnboundLocalError:        
            pass

        click = False
        clock.tick(60)
        pygame.display.update()
        
        
def Pause():
    while True:
        imag("data/resource/win/backg.jpg", tela_dx, tela_dy, 0, 0,objectaleatori) 
        pygame.sprite.Group().update()
        objectGroup.draw(tela)
        object_backg.draw(tela)
        objectaleatori.draw(tela)

        mx, my = pygame.mouse.get_pos()

        reset = b_imag("data/resource/players/Nave.png",110, 70, 450, 150, objectaleatori)

        if reset.collidepoint((mx, my)):
            if click:
                return

        click = False
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True



        pygame.display.update()
        clock.tick(60)

