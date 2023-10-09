#----------------PARTE 1-------------------------------------

# Importa as bibliotecas utilizadas
import sys, pygame
from pygame.locals import *
from random import *

# Inicializa a biblioteca pygame
pygame.init()

# Cria a surface 
size = (800, 600)
screen = pygame.display.set_mode(size)

# Define um titulo para a janela
pygame.display.set_caption("Jogo do Gatinho")

#Carrega a imagem de fundo
imagem = pygame.image.load("ceu_azul.png")
gato = pygame.image.load("gato.png")

# Define as cores em RGB
BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Declarando a fonte do placar e variável contadora
font = pygame.font.SysFont('sans',40)
placar = 0

# Declara a posicao X e Y do gato 
posicaoGato = [400, 100]

# Armazena num vetor a Velocidade de movimentacao do circulo 
velocidadeGato = 5

# Variáveis de posição do gato
X_gato = 0
Y_gato = 0

# Variável para contagem de tempo, utilizado para controlar a velocidade de quadros (de atualizações da tela)
clock = pygame.time.Clock()

#criando objeto Clock
CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # configurado o timer do Pygame para execução a cada 1 segundo


#----------------PARTE 2-------------------------------------

# Loop principal do jogo
while True:
    
    # Verifica se algum evento aconteceu
    for event in pygame.event.get():
        # Verifica se foi um evento de saida (pygame.QUIT), 
        # em caso afirmativo fecha a aplicacao
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Verifica se alguma tecla foi pressionada, e captura o evento
    pressed = pygame.key.get_pressed()

    #Verifica qual tecla (seta) foi pressionada e atualiza o vetor Posicao de acordo com a Velocidade
    if pressed[pygame.K_LEFT]: posicaoPapaBolinhas[0] -= velocidadePapaBolinhas[0]
    if pressed[pygame.K_RIGHT]: posicaoPapaBolinhas[0] += velocidadePapaBolinhas[0]

    #blita a imagem de fundo na tela
    screen.blit(imagem, (0, 0))

    # Desenha o gato na tela
    screen.blit(gato, posicaoGato)


    # Velocidade de queda do círculo Vermelho
    Y_Gato += 5 

    # Valores da bola vermelha é atribuido 
    posicaoBolasVermelhas = [X_vermelho,Y_vermelho]
   
    # Desenha o círculo vermelho
    pygame.draw.circle(screen, RED, posicaoBolasVermelhas, 10)

    # Se o círculo vermelho ultapassar a  tela ela é reiniciada
    if Y_vermelho > 600 or Y_vermelho < 20:
        direcao_vermelha *= -1
            

    # Se o papa bolinhas encostar no círculo vermelho o círculo vermelho é reiniciado
    # CB: Círculo Branco    CV: Círculo Vermelho 
    #        y + altura CB          y CV                    y CB                y + altura CV            x + largura CB           x CV                x CB                 x CV
    if (posicaoPapaBolinhas[1] + 20 >= Y_vermelho - 10  and posicaoPapaBolinhas[1] - 20 <= Y_vermelho + 10) and (posicaoPapaBolinhas[0] +20  >= X_vermelho - 10 and posicaoPapaBolinhas[0] - 20 <= X_vermelho + 20): 
        criar = True
        placar = placar+1
        pygame.mixer.music.load('catch.mp3')
        pygame.mixer.music.play(0)

    # renderizando as fontes do placar na tela
    score1 = font.render('Placar '+str(placar), True, (WHITE))
    screen.blit(score1, (600, 50))

    #rendrizando as fontes do cronometro na tela do usuario
    timer1 = font.render('Tempo ' + str(temporizador), True, (YELLOW))
    screen.blit(timer1, (50, 50))
        
    # Atualiza a tela visivel ao usuario
    pygame.display.flip()

    # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
    clock.tick(60)

#final de jogo
#Limpando a tela do jogo
frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (800, 600)))


textofinal = font.render('Fim de Jogo - Placar final: ' + str(placar), True, (RED))
size = font.size(str(textofinal))
screen.blit(textofinal, (size[0]/2., size[1]/2.))


#atualizamos a tela com uma nova tela de informação final ao jogador
pygame.display.flip()
#pequeno loop game esperando o usuario encerrar
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
