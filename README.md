# Тестовое задание 
> Performance Lab. Тестовое задание на стажера IT (нагрузочное тестирование). Июнь 2021 г.

![Python 3.7.3](https://img.shields.io/badge/python-v3.7.3-blue) ![Task counter](https://img.shields.io/badge/tasks_counter-3/4-green)

### Структура проекта:
Каждое задание находится в отдельном одноименном каталоге (**task#**). 

Внутри каждого каталога находится одноименный с заданием исполняемый файл с решением (**task#.py**). 

Кроме того, там могут находиться мои данные для тестирования кода (**data_for_task#.txt**) и отдельный исполняемый файл с тестами (**test_task#.py**).

### Краткое описание каждого скрипта (задачи).

Точка входа - функция `main`. 

#### Задание 1:

Для запуска я предлагаю поместить файл с тестовыми данными в папку с проектом и, используя команду `python task1.py test1`, запустить скрипт. Результат работы скрипта выводится в консоль.

Я предполагаю, что тестовые данные будут находиться в файле и представлять собой набор строк с числами, разделенными пробелами (число, текущая система исчисления, целевая система исчисления):

*111111 01 0123456789*

*155 0123456789 01*

#### Задание 2.

Я VS это задание:

(картинка)

Запустить скрипт можно с помощью `python task3.py path_to_log_file`. Скрипт может спарсить данные из файла, создать экземпляры сферы и линии, а затем красиво показать их в консоли. К сожалению, адаптировать формулу нахождения точек пересечения сферы и прямой линии я не смог, поэтому с какой-то графикой решил даже не заморачиваться.

#### Задание 3.

Запуск скрипта с помощью команды `python task3.py path_to_log_file from_time until_time`. Предполагается, что аргументы будут переданы в следующем порядке - путь к файлу с логом, первая отметка времени (старт), вторая отметка времени (стоп). Результат работы скрипта будет сохранен в csv-файл (**task3_results.csv**) в папке с заданием.

#### Задание 4.

Запуск скрипта с помощью команды `python task4.py word1 word2`. Предполагается, что слова для сравнения будут переданы через пробел в качестве аргументов при запуске скрипта.
