import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das variáveis do jogo
largura, altura = 640, 480
tamanho_cobra = 20
velocidade = 15

# Cores
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)
cor_fundo = (0, 0, 0)

# Criação da janela do jogo
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Cobrinha')
clock = pygame.time.Clock()

# Função para desenhar a cobra na tela
def desenhar_cobra(cor, cobra_lista):
    for posicao in cobra_lista:
        pygame.draw.rect(tela, cor, [posicao[0], posicao[1], tamanho_cobra, tamanho_cobra])

# Loop do jogo
def jogo():
    game_over = False
    game_close = False

    # Posição inicial da cobra
    x_cobra, y_cobra = largura // 2, altura // 2
    delta_x, delta_y = 0, 0
    cobra_lista = []
    comprimento_cobra = 1

    # Posição inicial da comida
    comida_x = round(random.randrange(0, largura - tamanho_cobra) / 20) * 20
    comida_y = round(random.randrange(0, altura - tamanho_cobra) / 20) * 20

    while not game_over:

        while game_close == True:
            tela.fill(cor_fundo)
            fonte = pygame.font.SysFont(None, 50)
            texto = fonte.render("Você perdeu! Pressione Q para sair ou C para jogar novamente", True, cor_cobra)
            tela.blit(texto, (largura // 8, altura // 2))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -tamanho_cobra
                    delta_y = 0
                elif event.key == pygame.K_RIGHT:
                    delta_x = tamanho_cobra
                    delta_y = 0
                elif event.key == pygame.K_UP:
                    delta_y = -tamanho_cobra
                    delta_x = 0
                elif event.key == pygame.K_DOWN:
                    delta_y = tamanho_cobra
                    delta_x = 0

        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            game_close = True

        x_cobra += delta_x
        y_cobra += delta_y
        tela.fill(cor_fundo)
        pygame.draw.rect(tela, cor_comida, [comida_x, comida_y, tamanho_cobra, tamanho_cobra])
        cobra_cabeca = []
        cobra_cabeca.append(x_cobra)
        cobra_cabeca.append(y_cobra)
        cobra_lista.append(cobra_cabeca)
        if len(cobra_lista) > comprimento_cobra:
            del cobra_lista[0]

        for segmento in cobra_lista[:-1]:
            if segmento == cobra_cabeca:
                game_close = True

        desenhar_cobra(cor_cobra, cobra_lista)

        pygame.display.update()

        if x_cobra == comida_x and y_cobra == comida_y:
            comida_x = round(random.randrange(0, largura - tamanho_cobra) / 20) * 20
            comida_y = round(random.randrange(0, altura - tamanho_cobra) / 20) * 20
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()
