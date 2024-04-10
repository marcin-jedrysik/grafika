import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # rysowanie kwadratów
    pygame.draw.line(win, CZERWONY, (116, 90), (500, 90), 20)
    pygame.draw.line(win, CZERWONY, (116, 510), (500, 90), 20)
    pygame.draw.line(win, CZERWONY, (116, 510), (500, 510), 20)
    pygame.display.update()
