import pygame, random

pygame.init()
pygame.mixer.pre_init(42050, -16, 2, 4096)
class Musicas():

    def stop_music():
        pygame.mixer.music.stop()
    
    def trilha_1():
        pygame.mixer.init()
        m = pygame.mixer.music.load("data/música/Minha_beta.mp3")
        m = pygame.mixer.music.queue("data/música/Minha_beta.mp3")
        m = pygame.mixer.music.play(1)

    def trilha_2():
        m1 = pygame.mixer.music.load("data/música/the_field.mp3")
        m1 = pygame.mixer.music.play()

    def Musicas_aleatrias():
        N = random.randint(1, 2)
        if N == 1:
            trilha_1()
        else:
            trilha_2()

class Plyalists_Musics():

    def P_m():
        
        ml = pygame.mixer.music.set_endevent(1)
        m1 = True
        if ml== 0:
            n += 1
            m1 = True
            if m1 == True:
                m1 = False
        
                if n == 1:
                    pm = pygame.mixer.music.load("data/música/the_field.mp3")
                    pm = pygame.mixer.music.play(1)
                
                if n == 2:
                    pm = pygame.mixer.music.load("data/música/the_field.mp3")
                    pm = pygame.mixer.music.play(1)

                if n == 3:
                    pm = pygame.mixer.music.load("data/música/the_field.mp3")
                    pm = pygame.mixer.music.play(1)

                if n == 4:
                    pm = pygame.mixer.music.load("data/música/the_field.mp3")
                    pm = pygame.mixer.music.play(1)


