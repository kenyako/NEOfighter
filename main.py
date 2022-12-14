import pygame
import json
from os import listdir

from global_vars import *  # Импортируем нужные переменные
from scenes import *  # Импортируем сцены


"""
Main loop
"""

# Запускаем сие чудо
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("NEOfighter")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                reset_value_to_scenses_variable("currency_screen", "start")

        # Проверяем наличие конфигурационного файла
        if "settings.json" not in listdir():
            in_json = json.dumps(settings_temp)
            with open("settings.json", "w") as f:
                f.write(in_json)

        with open('./settings.json') as f:
            settings = json.load(f)

        currency_screen = settings['scenes']['currency_screen']

        # Менеджер сцен
        if currency_screen == "start":
            start_screen(screen, "NEOfighter", "Start Game!", "Continue")
        elif currency_screen == 'lvl_1':
            lvl_1(screen)
        elif currency_screen == 'lvl_2':
            lvl_2(screen)
        elif currency_screen == 'lose':
            end_screen(screen, "You Lose!", "Restart")
        elif currency_screen == 'win':
            end_screen(screen, "You Win!", "Restart")
        pygame.display.flip()

    pygame.quit()
