import pygame, random
pygame.init()
pygame.mixer.pre_init(42050, -16, 2, 4096)
class Musicas():

    def stop_music():
        pygame.mixer.music.stop()
        
    
    def trilha_1():
        pygame.mixer.init()
        m = pygame.mixer.music.load("data/resource/songs/Minha_beta.mp3")
        m = pygame.mixer.music.queue("data/resource/songs/Minha_beta.mp3")
        m = pygame.mixer.music.play(-1)

    def trilha_2():
        m1 = pygame.mixer.music.load("data/resource/songs/the_field.mp3")
        m1 = pygame.mixer.music.play(-1)

    def Musicas_aleatorias():
        N = random.randint(1, 2)
        if N == 1:
            Musicas.trilha_1()
        else:
            Musicas.trilha_2()

class Playlists_Musics():

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


