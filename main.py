import pygame
import sys
import json
import os

from global_vars import *  # Импортируем нужные переменные
from scenes import *  # Импортируем сцены
from sprites import *  # Импортируем спрайты


"""
Main loop
"""


def load_image(name, colorkey=None):
    fullname = os.path.join('Data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image


def load_level(filename):
    filename = "Data/" + filename

    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None

    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '-':
                Wall(x, y)
            elif level[y][x] == '@':
                new_player = Player(x, y)

    return new_player


def terminate():
    pygame.quit()
    sys.exit()


# Запускаем сие чудо
if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("NEOfighter")

    player = generate_level(load_level('Levels/lvl_1.lvl'))

    clock = pygame.time.Clock()

    while True:
        # Период выполнения цикла игры
        pygame.time.delay(50)

        screen.fill(EMPTY_COLOR)

        # Проверяем наличие конфигурационного файла
        if "settings.json" not in os.listdir("./Data"):
            with open(SETTINGS_JSON, "w") as f:
                f.write(json.dumps(settings_temp))

        # Загружаем настройки
        with open(SETTINGS_JSON) as f:
            settings = json.load(f)

        currency_screen = settings['scenes']['currency_screen']

        # Менеджер сцен
        if currency_screen == "start":
            start_screen(screen, "NEOfighter", "Start Game!", "Continue")
        elif currency_screen == 'lvl_1':
            wall_group.update(screen)
            player.update(screen)
        elif currency_screen == 'lvl_2':
            lvl_2(screen)
        elif currency_screen == 'lose':
            end_screen(screen, "You Lose!", "Restart")
        elif currency_screen == 'win':
            end_screen(screen, "You Win!", "Restart")

        # Отслеживаем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings['scenes']['last_scene'] = currency_screen

                with open(SETTINGS_JSON, "w") as f:
                    f.write(json.dumps(settings))

                reset_value_to_scenes_variable("currency_screen", "start")

                # Функция, закрывающая окно
                terminate()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.go_right()
                elif event.key == pygame.K_a:
                    player.go_left()
                elif event.key == pygame.K_SPACE:
                    player.jump()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.stop()
                elif event.key == pygame.K_a:
                    player.stop()

        # Проверка на достижение границ окна
        if player:
            if player.rect.right > SCREEN_WIDTH - 30:
                player.rect.right = SCREEN_WIDTH - 30

            if player.rect.left < 30:
                player.rect.left = 30

        pygame.display.flip()
        clock.tick(20)
