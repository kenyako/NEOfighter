import pygame
from pygame import *

WIN_WIDTH = 800  # Ширина
WIN_HEIGHT = 600  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#393E46"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#222831"


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))  # Создание видимой поверхности
    bg.fill(Color(BACKGROUND_COLOR))

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

    while 1:
        pygame.display.update()
        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
        screen.blit(bg, (0, 0))

        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(Color(PLATFORM_COLOR))
                    screen.blit(pf, (x, y))

                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT
            x = 0


if __name__ == "__main__":
    main()
