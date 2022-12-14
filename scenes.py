import pygame
from global_vars import *  # Импортируем глобальные переменные
from button import Button  # Импортируем класс кнопки
import json


def reset_value_to_scenses_variable(key, value):
    print("CALL")
    with open('./settings.json') as f:
        settings = json.load(f)

    settings['scenes'][key] = value

    with open('./settings.json', 'w') as f:
        json.dump(settings, f)


def start_scr_loader():
    reset_value_to_scenses_variable("currency_screen", "start")


def start_screen(screen, text_on_screen, text_on_button):
    """
    Конечный экран игры, на котором отображается надпись <text_on_screen>
    и кнопка перезапуска
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render(text_on_screen, True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 75

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        width // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        text_on_button, lvl_1_loader)


def lvl_1_loader():
    print("CALL loader")
    reset_value_to_scenses_variable("currency_screen", "lvl_1")


def lvl_1(screen):
    """
    Уровень 1
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render("Level 1", True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 50

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        width // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        "Go to Lvl 2 ->", lvl_2_loader)


def lvl_2_loader():
    reset_value_to_scenses_variable("currency_screen", "lvl_2")


def lvl_2(screen):
    """
    Уровень 2
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render("Level 2", True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 50

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        (width - btn_width - 5) // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        "Go Win ->", win_scr_loader)

    btn2 = Button(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn2.draw(
        (width + btn_width + 5) // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        "Go Lose ->", lose_scr_loader)


def win_scr_loader():
    reset_value_to_scenses_variable("currency_screen", "win")


def lose_scr_loader():
    reset_value_to_scenses_variable("currency_screen", "lose")


def end_screen(screen, text_on_screen, text_on_button):
    """
    Конечный экран игры, на котором отображается надпись <text_on_screen>
    и кнопка перезапуска
    """
    # Закрашиваем окно
    screen.fill(COLORS['main'])

    # Отрисовываем текст с результатом
    font_size = 60
    font = pygame.font.Font(FONT, font_size)
    text = font.render(text_on_screen, True, COLORS['text'])

    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 75

    screen.blit(text, (text_x, text_y))

    btn_width, btn_height = 300, 100

    # Создаем экземпляр класса Button (кнопку на экране завершения игры)
    btn = Button(
        screen, btn_width, btn_height,
        COLORS['btn_inactive_color'],
        COLORS['btn_active_color']
        )

    # Отрисовываем кнопку на нужных координатах
    btn.draw(
        width // 2 - btn_width // 2,
        height // 2 - btn_height // 2 + 75,
        text_on_button, start_scr_loader)
