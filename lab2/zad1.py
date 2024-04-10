import pygame
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia okna gry
width, height = 600, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dziewiętnastokąt")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

rotation_angle = 0
scale_x = 1
scale_y = 1
trans_x = 0
trans_y = 0
skew = [0, 0]

# Funkcja do rysowania dziewiętnastokąta
def draw_nonagon(x, y, radius, rotation):
    points = []
    for i in range(19):
        angle = math.radians((360 / 19 * i) + rotation)
        # Zastosowanie transformacji
        new_x = x + radius * math.cos(angle) * scale_x
        new_y = y + radius * math.sin(angle) * scale_y
        points.append((new_x, new_y))
    pygame.draw.polygon(win, CZERWONY, points)

run = True

nonagon_surface = pygame.Surface((300, 300), pygame.SRCALPHA)
draw_nonagon(150, 150, 150, rotation_angle)
nonagon_rect = nonagon_surface.get_rect(center=(width//2, height//2))

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                rotation_angle = 0
                scale_x = 0.5
                scale_y = 0.5
                trans_x = 0
                trans_y = 0
                skew = [0, 0]
            elif event.key == pygame.K_2:
                rotation_angle = 45
                scale_x = 1
                scale_y = 1
                trans_x = 0
                trans_y = 0
                skew = [1, 0]
            elif event.key == pygame.K_3:
                rotation_angle = 180
                scale_x = 1
                scale_y = 1.5
                trans_x = 0
                trans_y = 0
                skew = [0, 0]
            elif event.key == pygame.K_4:
                rotation_angle = 180
                scale_x = 1
                scale_y = 1
                trans_x = 0
                trans_y = 0
                skew = [0, 0.5]
            elif event.key == pygame.K_5:
                scale_x = 2
                scale_y = 0.5
                trans_x = 0
                trans_y = -200
                skew = [0, 0]
            elif event.key == pygame.K_6:
                rotation_angle = 90
                scale_x = 2
                scale_y = 2
                trans_x = 0
                trans_y = 0
                skew = [0, 1]
            elif event.key == pygame.K_7:
                rotation_angle = 180
                scale_x = 1
                scale_y = 1.5
                trans_x = 0
                trans_y = 0
                skew = [0, 0]
            elif event.key == pygame.K_8:
                rotation_angle = 180
                scale_x = 1.25
                scale_y = 1
                trans_x = -100
                trans_y = 100
                skew = [1, 0]
            elif event.key == pygame.K_9:
                rotation_angle = 180
                scale_x = 1.25
                scale_y = 2
                trans_x = 100
                trans_y = 0
                skew = [1, 0]

    win.fill((0, 0, 0))

    draw_nonagon(width // 2, height // 2, 150, 0)

    pygame.display.update()

# Zamknięcie Pygame
pygame.quit()
