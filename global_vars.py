'''
В данном файле содержатся глобальные переменные
Для оптимального доступа из любого файла
'''

# Ссылка на репозиторий
gh_link = 'https://github.com/kenyako/NEOfighter'

# Размеры окна
size = width, height = 800, 600

# Словарь с цветами, используемыми в коде
COLORS = {
    'main': '#222831',
    'second_main': '#393E46',
    'text': '#FFD369',
    'second_text': '#EEEEEE',
    'btn_inactive_color': "#393E46",
    'btn_active_color': "#4f5257",
    "btn_disable_color": "#2e3136",
    "platform_color": "#222831",
    "empty_color": '#393E46'
}

# Шрифт
FONT = './Data/Fonts/retro-land-mayhem.ttf'

# Переменная для считывании состоянии кнопки
alreadyPressed = False


settings_temp = {
    "scenes": {
        "currency_screen": "start",
        "last_scene": "start"
    }
}

# Файл JSON для сохранения
SETTINGS_JSON = './Data/settings.json'
