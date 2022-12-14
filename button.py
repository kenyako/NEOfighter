import pygame
from global_vars import *

'''
В данном файле описан класс кнопки
'''


class Button:
    def __init__(
            self, screen, width, height,
            inactive_color=None, active_color=None
            ):
        self.screen = screen
        self.width = width  # Длина кнопки
        self.height = height  # Ширина кнопки
        self.inactive_color = inactive_color  # Базовый цвет
        self.active_color = active_color  # Цвет при наведении

    def draw(self, btn_x, btn_y, btn_text, action=None, btn_image=None):
        global alreadyPressed

        mouse = pygame.mouse.get_pos()  # Позиция мыши
        click = pygame.mouse.get_pressed()  # Обработка нажатия на кнопку мыши

        # Если курсор в пределах кнопки..
        if btn_x < mouse[0] < btn_x + self.width and \
                btn_y < mouse[1] < btn_y + self.height:

            if btn_text:
                # Отрисовываем кнопку с цветом <active_color>
                pygame.draw.rect(
                    self.screen,
                    self.active_color,
                    (btn_x, btn_y, self.width, self.height)
                )

            # Если по ней кликнули ЛКМ и ключ action задан
            if click[0] and action is not None:
                alreadyPressed = True
            else:
                if alreadyPressed:
                    action()
                    alreadyPressed = False

        # А ели за пределами кнопки..
        else:
            if btn_text:
                # Отрисовываем кнопку со стандартным цветом
                pygame.draw.rect(
                    self.screen,
                    self.inactive_color,
                    (btn_x, btn_y, self.width, self.height)
                )

        if btn_text:
            # Отрисовываем текст на кнопке
            _fontSize = 30
            text_on_btn = pygame.font.Font(
                FONT,
                _fontSize
            )\
                .render(btn_text, True, COLORS['second_text'])
            self.screen.blit(
                text_on_btn,
                (btn_x + (self.width // 2 - text_on_btn.get_width() // 2),
                    btn_y + (self.height // 2 - text_on_btn.get_height() // 2))
            )

        # Если передан путь к картинке..
        elif btn_image is not None:
            image_on_btn = pygame.image.load(btn_image)
            image_rect = image_on_btn.get_rect(bottomright=size)
            self.screen.blit(
                image_on_btn,
                image_rect
            )
