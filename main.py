import pygame
import sys
import json
import os

from global_vars import *  # Импортируем нужные переменные
from scenes import *  # Импортируем сцены
from load_image_func import *


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

    player, gun = generate_level(load_level('Levels/lvl_1.lvl'))

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

            if player.rect.right > SCREEN_WIDTH - 50:
                lvl_2_loader()

            # Отрисовка объектов первой сцены
            wall_group.update(screen)
            player.update(screen)
            screen.blit(pygame.transform.scale(load_image(
                './Sprites/portal.png'), (30, 110)), (720, 170))
            # portal_group.draw(screen)
            gun.update(screen)
            trampoline_group.draw(screen)
            all_sprites.draw(screen)
            bullets.draw(screen)
            monster_group.draw(screen)

        elif currency_screen == 'lvl_2':
            lvl_2(screen)

        elif currency_screen == 'lose':
            end_screen(screen, "You Lose!", "Restart")

        elif currency_screen == 'win':
            end_screen(screen, "You Win!", "Restart")

        # Отслеживаем события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Сохранение параметров

                settings['scenes']['last_scene'] = currency_screen

                settings['saves']['coord_x'] = player.rect.x
                settings['saves']['coord_y'] = player.rect.y
                settings['saves']['have_gun'] = player.get_weapon
                settings['saves']['count_ammo'] = gun.cartridges_counter

                with open(SETTINGS_JSON, "w") as f:
                    f.write(json.dumps(settings))

                reset_value_to_scenes_variable("currency_screen", "start")

                # Функция, закрывающая окно
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Если нажата ЛКМ
                if event.button == 1:
                    gun.shoot()

            # Подключение клавиш для управления
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
