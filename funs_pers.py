import pygame, sys, json, os
from pygame.locals import *

pygame.init()

# def Fps(tela):
#     """
#     Mostra o FPS no canto enferior esquerdo.
#     """
#     ver_fps = clock.get_fps()
#     desenhar_text_m(f'FPS: {int(ver_fps)}', (255, 255, 255), tela, 10, 450, 15)

def Loading():
    from data.cogs.enemies.asteroid import Asteroid
    from data.cogs.powers.missil import Missil
    from data.cogs.players.nave import Nave
    from data.cogs.itens.i_m import I_missil
    from data.cogs.itens.i_l import I_life
    from data.cogs.sounds.sounds import Efeito_sonoro
    from data.cogs.songs.songs import Musicas
    
# def controle():
#     for event in pygame.event.get():
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             print("h")
#             if muniçao > 0:
#                 for i in range(1):
#                     Efeito_sonoro.shoot()
#                     newtiro = Missil(objectGroup, tiroGrop)
#                     newtiro.rect.center = nave.rect.center
#                     muniçao -= 1

#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 if muniçao > 0:
#                     for i in range(1):
#                         Efeito_sonoro.missel()
#                         newtiro = Missil(objectGroup, tiroGrop)
#                         newtiro.rect.center = nave.rect.center
#                         muniçao -= 1

#--------------------------------------------------------------------#
# Imagens, background, botoes etc... 
#--------------------------------------------------------------------#

def backg(file, Group, tx, ty):
    """
    Para add um background simples dando o                                   
    diretorio, grupo de sprits e os tamanho X e Y
    """
    bg = pygame.sprite.Sprite(Group)
    bg.image = pygame.image.load(f"{file}").convert()
    bg.image = pygame.transform.scale(bg.image, [tx, ty])
    bg.rect = bg.image.get_rect()

def imag(file, tx, ty, pos_x, pos_y, group):
    """
    Para add imagem png ou não.
    """
    img = pygame.sprite.Sprite(group)
    img.image = pygame.image.load(f"{file}").convert_alpha()
    img.image = pygame.transform.scale(img.image, [tx, ty])
    img.rect = img.image.get_rect()
    img.rect.center = (pos_x, pos_y)

def b_imag(file, tx, ty, px, py, group):
    """
    Para adicionar imagem/botão:            
    file = arquivo / tx, ty = tamanho           
    px, py = posição / group = objectGroup
    """
    bm = pygame.sprite.Sprite(group)
    bm.image = pygame.image.load(f"{file}")
    bm.image = pygame.transform.scale(bm.image, [tx, ty])
    bm.rect = pygame.Rect(px, py, tx, ty)
    return bm.rect

def anima_H(file, quadros, cort_x, cort_y, tx, ty, px, py):
    sprit_sheet = pygame.image.load(f"data/{file}")
    animaçao = []

    for i in range(quadros):
        imag = sprit_sheet.subsurface((i * cort_x, 0), (cort_x, cort_y))
        imag = pygame.transform.scale(imag, [tx, ty])
        animaçao.append(imag)

    index_lista = 0
    image = animaçao[int(index_lista)]
    rect = pygame.Rect(px, py, tx, ty)

    return rect

#--------------------------------------------------------------------#
# Fontes na tela
#--------------------------------------------------------------------#

def desenhar_text(text, font_p, color, surface, x, y, tamanho):
    """
    font independente de variaveis externas como :                   

    font = pygame.font.SysFont("...", tamanho)
    """
    font = pygame.font.SysFont(f"{font_p}", tamanho)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect

def desenhar_text_d(text, font_d, color, surface, x, y, tamanho):
    """
    font dependente de variaveis externas, como                  
    uma variavel definida no fora desta fonção.             
    exp:                              

    variavel:
    font = pygame.font.SysFont("...", tamanho)
    """
    
    textobj = font_d.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect

def desenhar_text_m(text, color, surface, x, y, tamanho):
    """
    font do mine :D
    """
    try:
        
        font_ = pygame.font.SysFont("Minecraft", tamanho)
        textobj = font_.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    except:
        pygame.init()
        pass

    return textrect

#--------------------------------------------------------------------#
# Carregar e salvar o perfil do jogador
#--------------------------------------------------------------------#

def Novo_game():
    """
    Cria um novo perfil/arquivo que armazena
    atributos do personage
    """
    perfil = {
        "nome":"Gg",
        "life":3 ,
        "muniçao":10 ,
    }

    with open("profile.json", "w") as f:
        json.dump(perfil, f)


def salvar_game(var):
    """
    guarda as informações de uma variavel em uma arquivo json.       
    *(necessário ser do tipo dicionario !!)*    
    """
    with open("profile.json", "w") as f:
        json.dump(var, f)

def load_game():
    """
    carrega/deserializa as imformaçoes e para a variavel                
    perfil = {}  <-- type = dict!!
    """
    perfil = {}
    if os.path.exists("profile.json"):
        with open("profile.json", "r") as f:
            perfil = json.load(f)
    return perfil






