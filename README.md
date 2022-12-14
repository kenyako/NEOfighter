# NEOfighter: branch *«[Feature/Scene_manager](https://github.com/kenyako/NEOfighter/tree/Feature/Scene_manager)»*

## Менеджер сцен
По ключу **currency_screen** в файле *settings.json* хранится название текущей сцены.
В зависимости от значения в дальнейшем условии в главном цикле (`if currency_screen == "start":...`) отрисовывается определённая сцена.
Значение переменной изменяет **загрузчик**(loader) сцены: это функция, название которой состоит из *название_сцены*_loader(). Она изменяет значение по ключу **currency_screen** в JSON-файле.
После изменения значения **currency_screen** соответственно изменяется отрисовываемая сцена.
