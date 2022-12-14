'''
В данном файле содержатся глобальные переменные
Для оптимального доступа из любого файла
'''

size = width, height = 800, 600  # Размеры окна

# Словарь с цветами, используемыми в коде
COLORS = {
    'main': '#222831',
    'second_main': '#393E46',
    'text': '#FFD369',
    'second_text': '#EEEEEE',
    'btn_inactive_color': "#393E46",
    'btn_active_color': "#4f5257"
}

FONT = './Fonts/retro-land-mayhem.ttf'  # Шрифт
currescy_screen = 'start'  # начальная сцена
alreadyPressed = False  # Переменная для считывании состоянии кнопки
