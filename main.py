import pygame
import sys
import json
from os import listdir

from global_vars import *  # Импортируем нужные переменные
from scenes import *  # Импортируем сцены


"""
Main loop
"""


def terminate():
    pygame.quit()
    sys.exit()


# Запускаем сие чудо
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("NEOfighter")

    while True:
        # Период выполнения цикла игры
        pygame.time.delay(50)

        # Проверяем наличие конфигурационного файла
        if "settings.json" not in listdir("./Data"):
            with open(SETTINGS_JSON, "w") as f:
                f.write(json.dumps(settings_temp))

        # Загружаем настройки
        with open(SETTINGS_JSON) as f:
            settings = json.load(f)

        currency_screen = settings['scenes']['currency_screen']

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings['scenes']['last_scene'] = currency_screen

                with open(SETTINGS_JSON, "w") as f:
                    f.write(json.dumps(settings))

                reset_value_to_scenes_variable("currency_screen", "start")

                # Функция, закрывающая окно
                terminate()

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
