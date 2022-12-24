import pygame

PLATFORM_COLOR = "#222831"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32


def draw_lvl_1(screen):

    level = [
        "-------------------------",
        "-------------------------",
        "-     -----------       -",
        "-       -------         -",
        "-        -----          -",
        "-         --            -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                    ----",
        "-                    ----",
        "------               ----",
        "------               ----",
        "------               ----",
        "------       ----    ----",
        "------       ----    ----",
        "------       ----    ----",
        "-------------------------",
        "-------------------------"]

    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))

            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT
        x = 0
