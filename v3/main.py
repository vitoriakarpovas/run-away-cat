import sys, pygame
from pygame.locals import *
import random

pygame.init()

size = (626, 626)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jogo do Gatinho")

gato = pygame.image.load("gato.png")
imagem = pygame.image.load("ceu_azul.png")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

font = pygame.font.SysFont('sans', 50)
placar = 0
clock = pygame.time.Clock()
CLOCKTICK = pygame.USEREVENT + 1
pygame.time.set_timer(CLOCKTICK, 1000)

class Gato:
    def __init__(self):
        self.image = pygame.transform.scale(gato, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (size[0] // 2, size[1])  # Define a posição inicial do gato no chão
        self.velocidade_y = 0

    def update(self):
        self.velocidade_y += 1  # Simula a gravidade
        self.rect.y += self.velocidade_y

        if self.rect.bottom > size[1]:  # Quando toca na parte de baixo da tela
            self.rect.bottom = size[1]
            self.velocidade_y = -20  # "Pular" para cima

class Plataforma:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def appear(self):
        screen.blit(self.image, self.rect.topleft)

gato = Gato()
plataformas = []

primeira_plataforma = Plataforma(size[0] // 2 - 60, 500, 120, 20)
plataformas.append(primeira_plataforma)

def criar_plataformas():
    x = random.randint(0, size[0] - 120)
    
    # Garanta que a nova plataforma tenha uma distância máxima de 50 pixels da última plataforma criada
    if plataformas:
        while abs(x - plataformas[-1].rect.x) < 50:
            x = random.randint(0, size[0] - 120)
    
    if plataformas:
        y = plataformas[-1].rect.y - 100  # Defina a diferença de altura desejada (100 pixels)
    else:
        y = 400  # Defina uma altura inicial para a primeira plataforma
    if y < 100:
        y = 100  # Garanta que as plataformas não subam muito alto
    width = 120
    height = 20
    nova_plataforma = Plataforma(x, y, width, height)
    plataformas.append(nova_plataforma)


for i in range(4):
    criar_plataformas()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == CLOCKTICK:
            placar += 2

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        gato.rect.x -= 5
    if pressed[pygame.K_RIGHT]:
        gato.rect.x += 5

    for plataforma in plataformas:
        if gato.rect.colliderect(plataforma.rect):
            if gato.velocidade_y > 0 and gato.rect.bottom <= plataforma.rect.centery:
                gato.velocidade_y = -20

    if gato.rect.left <= 0:
        gato.rect.left = 0

    if gato.rect.right >= size[0]:
        gato.rect.right = size[0]

    screen.blit(imagem, (0, 0))
    screen.blit(gato.image, gato.rect)
    gato.update()

    for plataforma in plataformas:
        plataforma.appear()

    score1 = font.render('Placar ' + str(placar), True, YELLOW)
    screen.blit(score1, (350, 50))
    pygame.display.flip()
    clock.tick(60)
