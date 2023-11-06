import sys, pygame
from pygame.locals import *
import random

pygame.init()

size = (626, 626)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jogo do Gatinho")

gato = pygame.image.load("gato.png")
imagem = pygame.image.load("agua.png")
platform = pygame.image.load("tabua.png")
home = pygame.image.load("home.png")
controles = pygame.image.load("controles.png")
controles = pygame.transform.scale(controles, (450, 450))
game_over = pygame.image.load("game_over.png")
onda = pygame.image.load("wave.png")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont('sans', 50)
placar = 0
tela = 1
tempo = 0
tela_controle = True
clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT + 1
pygame.time.set_timer(CLOCKTICK, 1000)
VELOCIDADE_PLATAFORMA = 5

class Gato:
    def __init__(self):
        self.image = pygame.transform.scale(gato, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (size[0] // 2, size[1])  # Inicia no chão
        self.velocidade_y = 0

    def update(self):
        self.velocidade_y += 1  # Simula a gravidade
        self.rect.y += self.velocidade_y

        if self.rect.bottom > size[1]:
            self.rect.bottom = size[1]
            self.velocidade_y = -20  # "Pular" novamente

        # Evite que o gato suba muito perto da parte de cima da tela
        if self.rect.top < 100:
            self.rect.top = 100

class Plataforma:
    def __init__(self, x, y, width, height):
        self.image = pygame.transform.scale(platform, (130, 40))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

gato = Gato()
plataformas = []

primeira_plataforma = Plataforma(size[0] // 2 - 60, 500, 120, 20)
plataformas.append(primeira_plataforma)

def remover_plataforma():
    if plataformas:
        if plataformas[0].rect.top > size[1]:
            plataformas.pop(0)

def mover_plataformas():
    for plataforma in plataformas[:4]:  
        plataforma.rect.y += VELOCIDADE_PLATAFORMA

def criar_plataformas():
    if not plataformas:
        y = size[1] - 20  # Defina a altura da primeira plataforma (20 pixels acima do chão)
    else:
        y = plataformas[-1].rect.y - random.randint(100, 150)  # Diferença de altura aleatória

    if y < 100:
        y = 100  # Garanta que as plataformas não subam muito alto

    # Calcule a posição horizontal da próxima plataforma com base na posição da plataforma anterior
    x = random.randint(max(0, plataformas[-1].rect.x - 50), min(size[0] - 120, plataformas[-1].rect.x + 50))

    width = 120
    height = 20
    nova_plataforma = Plataforma(x, y, width, height)
    plataformas.append(nova_plataforma)
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CLOCKTICK:
            placar += 2
            tempo +=1
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if tela == 1:
                if pos[0] > 200 and pos[0] < 418 and pos[1] > 369 and pos[1] < 473:
                    tela = 2
                if pos[0] > 21 and pos[0] < 131 and pos[1] > 547 and pos[1] < 608:
                    tela = 3
            if tela == 3:
                if pos[0] > 455 and pos[0] < 493 and pos[1] > 107 and pos[1] < 156:
                    tela = 1
            if tela == 4:
                print(pos)
                if pos[0] > 50 and pos[0] < 295 and pos[1] > 455 and pos[1] < 578:
                    tela = 2
                if pos[0] > 349 and pos[0] < 591 and pos[1] > 455 and pos[1] < 578:
                    tela = 1

    if tela == 1:
        screen.blit(home, (0, 0))
        pygame.display.flip()
        
    if tela == 2:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            gato.rect.x -= 5
        if pressed[pygame.K_RIGHT]:
            gato.rect.x += 5

        for plataforma in plataformas:
            if gato.rect.colliderect(plataforma.rect):
                if gato.velocidade_y > 0 and gato.rect.bottom <= plataforma.rect.centery:
                    gato.velocidade_y = -20
                    mover_plataformas()

        if gato.rect.left <= 0:
            gato.rect.left = 0

        if gato.rect.right >= size[0]:
            gato.rect.right = size[0]

        screen.blit(imagem, (0, 0))
        screen.blit(gato.image, gato.rect)
        gato.update()

        remover_plataforma()
        criar_plataformas()
        mover_plataformas()
        print(gato.rect.y)

        for plataforma in plataformas[:4]:
            screen.blit(plataforma.image, plataforma.rect.topleft)

        if tempo > 3:
            screen.blit(onda, (0, 515))
            if gato.rect.x > 515:
                tela = 4

        score1 = font.render('Placar ' + str(placar), True, YELLOW)
        screen.blit(score1, (350, 50))
        pygame.display.flip()
        clock.tick(60)

    if tela == 3:
        screen.blit(controles, (80, 80))
        pygame.display.flip()

    if tela == 4:
        screen.blit(game_over, (0, 0))
        pygame.display.flip()
