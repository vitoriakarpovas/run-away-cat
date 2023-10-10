import sys, pygame
from pygame.locals import *

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

font = pygame.font.SysFont('sans', 40)
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

gato = Gato()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        gato.rect.x -= 5
    if pressed[pygame.K_RIGHT]:
        gato.rect.x += 5

    screen.blit(imagem, (0, 0))
    screen.blit(gato.image, gato.rect)
    gato.update()

    score1 = font.render('Placar ' + str(placar), True, WHITE)
    screen.blit(score1, (600, 50))
    pygame.display.flip()
    clock.tick(60)
