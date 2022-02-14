import os
import pygame

WIDTH, HEIGHT = 960, 720

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

frame = pygame.image.load('Caixa de Charadas/src/wood-frame.png').convert_alpha()
frame_angled = pygame.transform.rotate(frame, 90)
frame_pronto = pygame.transform.scale(frame_angled, (980, 740))

pygame.display.set_caption('Caixa Misteriosa')

clicked = False

COLOR = "#705446"

def mostra_charada(event):

    pygame.font.init()

    font = pygame.font.Font('freesansbold.ttf', 23)

    text = font.render(
        """
            Tem raízes misteriosas,
            É mais alta que as frondosa
            Sobe, sobe e também desce,
            Mas não cresce nem decresce
        """,
    True, (255, 255, 255), (0, 0, 0, 0))

    textRect = text.get_rect()
    textRect.center = (WIDTH//2, HEIGHT//2)

    if event.type == pygame.MOUSEBUTTONDOWN:
        WIN.blit(text, textRect)
        pygame.display.update()
        print("você clicou o botão")

def draw_window(color):

    WIN.fill(color)
    WIN.blit(frame_pronto, (-10, -10))
    
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            else: mostra_charada(event)

        draw_window(COLOR)

    pygame.quit()

if __name__ == '__main__':
    main()

        