<<<<<<< HEAD
# Project-PyGame: branch *«[Michurin](https://github.com/kenyako/Project-PyGame/tree/Michurin)»*

## Глобальные переменные
* **COLORS** – словарь, содержащий в себе все цвета на сцене
* **FONT** – шрифт, который используется на сцене
* **ACTIVE_SCREEN** – название текущей сцены
* **alreadyPressed** – переменная, которая хранит последнее состоянии кнопки.
=======
# NEOfighter
![https://img.shields.io/badge/Python-3.7.5-blue](https://img.shields.io/badge/Python-3.8.0-blue)
![GitHub all releases](https://img.shields.io/github/downloads/kenyako/NEOfighter/total)

## Index
* [Team members](https://github.com/kenyako/NEOfighter/#team-members)
* [Methodology of work in the project](https://github.com/kenyako/NEOfighter/#methodology-of-work-in-the-project)
* [Game concept](https://github.com/kenyako/NEOfighter/#game-concept)

## Team members
* [@kenyako](https://github.com/kenyako) – **Team Lead, Developer, Logic Architect**
* [@MichurinDev](https://github.com/MichurinDev) – **Developer, UI-Designer**
* [@Svetikk4](https://github.com/Svetikk4) – **Developer, Level-Designer**
>>>>>>> origin/LeadBranch

**Нажатие ЛКМ -> `alreadyPressed = True` -> Отжатие ЛКМ -> Выполнение нужного алгоритма -> `alreadyPressed = False`**

<<<<<<< HEAD
## Class *Button*
Класс кнопки (как бы очевидно это не звучало).
Содержит __init()__, определяющий *длину, ширину, базовый увет и цвет при наведении.*
Функция *draw()*, во-первых, **отрисовывает** кнопку, во-вторых, **обрабатывает наведение** и **нажатие** на неё.
Также по ключу *function* можно задать функцию, которая будет выполняться при нажатии на кнопку.

## Func *end_screen(screen, text_on_screen)*
Функция, отрисовывающая конечный экран, на котором содержится текст *text_on_screen* и кнопка.
Текст внутри кнопки располагается **строго посередине** кнопки!
***Свойства кнопки задаются отдельно внутри функции посредством изменения параметров инициализации экземпляра класса Button***

## Менеджер сцен
По ключу **currency_screen** в файле *settings.json* хранится название текущей сцены.
В зависимости от значения в дальнейшем условии в главном цикле (`if currency_screen == "start":...`) отрисовывается определённая сцена.
Значение переменной изменяет **загрузчик**(loader) сцены: это функция, название которой состоит из *название_сцены*_loader(). Она изменяет значение по ключу **currency_screen** в JSON-файле.
После изменения значения **currency_screen** соответственно изменяется отрисовываемая сцена.
=======
## Game concept
* **Genre:** Platformer
* **Graphics:** Pixel

The goal of the game is to complete all the levels, that is, to get to the end point of this level
The player is a character armed with various items to attack and defend against enemies

Mechanics:
* Health Counter
* Ammo counter
* Shooting
* Selection of subjects
* The ability to restore the health of the character
* Objects on the level for interacting with the character (interactive obstacles, boosters, etc.)
* Teleportation by portals
>>>>>>> origin/LeadBranch
