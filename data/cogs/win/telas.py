import pygame, sys 
from data.dependencias import *
from funs_pers import*

pygame.init()

pygame.mixer.music.set_volume(0.05222)
def intro_game():
    Musicas.trilha_1()
    tempo = 0
    running = True
    backg("data/resource/win/backg.jpg", object_backg, tela_dx, tela_dy)
    while running:

        pygame.sprite.Group().update()
        object_backg.draw(tela)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_KP_ENTER:
                    return

        desenhar_text_m(" Press Enter ", (255, 255, 255), tela, 360, 450, 20)
        tempo += 1
        pygame.display.update()
        clock.tick(60)
intro_game()

def game_over():

    while True:
        mx, my = pygame.mouse.get_pos()
        pygame.sprite.Group().update()
        objectGroup.draw(tela)
        object_backg.draw(tela)
        backg(TELA+"backg.jpg", object_backg, tela_dx, tela_dy)

        button_1 = desenhar_text_m('Play..', (255, 255, 255), tela, 87, 127, 30)

        try:
            if button_1.collidepoint((mx, my)):
                if click:
                    Efeito_sonoro.b_1()
                    perfil = load_game()
                    return
            # if button_2.collidepoint((mx, my)):
            #     if click:
            #         Efeito_sonoro.b_1()
        except UnboundLocalError:        
            print("UnboundLocalError")
            
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

#game_over()
"""
while running:

    pygame.sprite.Group().update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()
    clock.tick(60)
"""
