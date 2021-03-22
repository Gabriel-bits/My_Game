import pygame
import time

pygame.init()

class Efeito_sonoro():

    pygame.mixer.pre_init(44100, -16, 3, 10)
    pygame.mixer.set_num_channels(1)
    pygame.mixer.set_num_channels(2)
    pygame.mixer.set_num_channels(3)

    def b_1():
        s = pygame.mixer.Sound("data/souds/b_1.wav")
        s.play()

    def shoot():
        s1 = pygame.mixer.Sound("data/música/Shoot.wav")
        s1.play()

    def dano_1():
        s2 = pygame.mixer.Sound("data/souds/dano_1.wav")
        s2.play()

    def esplos_1():
        s3 = pygame.mixer.Sound("data/souds/esplos_1.wav")
        s3.play()

    def esplos_2():
        s4 = pygame.mixer.Sound("data/souds/esplos_2.wav")
        s4.play()

    def hp():
        s5 = pygame.mixer.Sound("data/souds/hp_1.wav")
        s5.play()

    def missel():
        s6 = pygame.mixer.Sound("data/souds/missel_1.wav")
        s6.play()

    def moeda():
        s7 = pygame.mixer.Sound("data/souds/moeda_1.wav")
        s7.play()

    def morte():
        s8 = pygame.mixer.Sound("data/souds/morte_1.wav")
        s8.play()

    def muni():
        s9 = pygame.mixer.Sound("data/souds/muni_1.wav")
        s9.play()
