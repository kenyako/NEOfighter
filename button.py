import pygame
from global_vars import *

'''
В данном файле описан класс кнопки
'''


class Button:
    def __init__(self, screen, width, height, inactive_color, active_color):
        self.screen = screen
        self.width = width  # Длина кнопки
        self.height = height  # Ширина кнопки
        self.inactive_color = inactive_color  # Базовый цвет
        self.active_color = active_color  # Цвет при наведении

    def draw(self, btn_x, btn_y, btn_text=None, action=None):
        global alreadyPressed

        mouse = pygame.mouse.get_pos()  # Позиция мыши
        click = pygame.mouse.get_pressed()  # Обработка нажатия на кнопку мыши

        # Если курсор в пределах кнопки..
        if btn_x < mouse[0] < btn_x + self.width and \
                btn_y < mouse[1] < btn_y + self.height:
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
            # Отрисовываем кнопку со стандартным цветом
            pygame.draw.rect(
                self.screen,
                self.inactive_color,
                (btn_x, btn_y, self.width, self.height)
            )

        _fontSize = 30
        # Отрисовываем текст на кнопке
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
