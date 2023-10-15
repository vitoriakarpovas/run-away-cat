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
        self.rect.center = (150, 330)
        self.velocidade_y = 0

    def update(self):
        self.velocidade_y += 1  # Simula a gravidade
        self.rect.y += self.velocidade_y

        if self.rect.bottom > 626:  # Quando toca na parte de baixo da tela
            self.rect.bottom = 626
            self.velocidade_y = -20  # "Pular" para cima

class Plataforma:
    def __init__(self):
        self.image = pygame.Surface((120, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (random.randint(0,600), random.randint(0,600))  # Defina a posição da plataforma

    def appear(self):
        screen.blit(self.image, self.rect.topleft)

gato = Gato()
plataformas = []

for i in range(0,15):
    plataformas.append(Plataforma())
    
plataforma = Plataforma()

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

    if gato.rect.colliderect(plataforma.rect) and gato.velocidade_y > 0:
        gato.velocidade_y = -20

    if gato.rect.left <= 0:
        gato.rect.left = 0

    if gato.rect.right >= 626:
        gato.rect.right = 626


    screen.blit(imagem, (0, 0))
    screen.blit(gato.image, gato.rect)
    gato.update()
    
    plataforma.appear()

    score1 = font.render('Placar ' + str(placar), True, YELLOW)
    screen.blit(score1, (350, 50))
    pygame.display.flip()
    clock.tick(60)
