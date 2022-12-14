'''
В данном файле содержатся глобальные переменные
Для оптимального доступа из любого файла
'''

gh_link = 'https://github.com/kenyako/NEOfighter'  # Ссылка на репозиторий

size = width, height = 800, 600  # Размеры окна

# Словарь с цветами, используемыми в коде
COLORS = {
    'main': '#222831',
    'second_main': '#393E46',
    'text': '#FFD369',
    'second_text': '#EEEEEE',
    'btn_inactive_color': "#393E46",
    'btn_active_color': "#4f5257",
    "btn_disable_color": "#2e3136"
}

FONT = './Fonts/retro-land-mayhem.ttf'  # Шрифт
alreadyPressed = False  # Переменная для считывании состоянии кнопки

settings_temp = {
    "scenes": {
        "currency_screen": "start",
        "last_scene": "start"
    }
}
