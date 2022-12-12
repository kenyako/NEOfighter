# Project-PyGame: branch *[Michurin](https://github.com/kenyako/Project-PyGame/tree/Michurin)*

## Class *Button*
Класс кнопки (как бы очевидно это не звучало).
Содержит __init()__, определяющий *длину, ширину, базовый увет и цвет при наведении.*
Функция draw(), во-первых, **отрисовывает** кнопку, во-вторых, **обрабатывает наведение** и **нажатие** на неё.
Также по ключу *function* можно задать функцию, которая будет выполняться при нажатии на кнопку.

## Func *end_screen(screen, text_on_screen)*
Функция, отрисовывающая конечный экран, на котором содержится текст <text_on_screen> и кнопка.
Текст внутри кнопки располагается **строго посередине** кнопки!
***Свойства кнопки задаются отдельно внутри функции посредством изменения параметров инициализации экземпляра класса Button***
