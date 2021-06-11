import argparse
from ast import literal_eval as le


class AbstractFigure:
    """Абстрактный класс для понтов в ООП."""
    def show_parameters(self) -> dict:
        return self.__dict__


class Sphere(AbstractFigure):
    """Класс-сфера для сохранения атрибутов."""
    def __init__(self, x: int, y: int, z: int, radius: float) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius


class Line(AbstractFigure):
    """Класс-линия для сохранения атрибутов."""
    def __init__(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2


def get_data_from_file(path: str) -> list:
    """Функция для получения данных из файла. Принимает путь к файлу (от корневой папки проекта)."""
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    return data


def convert_str_to_dict(data: str) -> dict:
    """Функция для приведения строки с данными в формат словаря."""
    # 'le' не работает с [], поэтому меняем их на ()
    substring = data.replace('[', '(').replace(']', ')')

    # Для корректной работы 'le' требуется, чтобы ключи словаря были в кавычках
    index_counter = -1
    for symbol in substring:
        index_counter += 1
        try:
            next_symbol = substring[index_counter + 1]
        except IndexError:
            break
        if not symbol.isalpha() and substring[index_counter + 1].isalpha():
            index_counter += 1
            substring = substring[:index_counter] + "'" + substring[index_counter:]
        elif symbol.isalpha() and not next_symbol.isalpha():
            index_counter += 1
            substring = substring[:index_counter] + "'" + substring[index_counter:]

    # Превращаем воду в вин... Строку в словарь :)
    result = le(substring)
    return result


def collision_is_found(sphere: Sphere, line: Line) -> bool:
    """Функция для поиска коллизий между сферой и отрезком. Когда-нибудь будет здесь написана..."""
    pass


def main(path: str) -> None:
    """Функция-агрегатор для запуска скрипта."""
    data = get_data_from_file(path)

    for line in data:
        data_to_draw = convert_str_to_dict(line)

        sphere = Sphere(
            x=data_to_draw['sphere']['center'][0],
            y=data_to_draw['sphere']['center'][1],
            z=data_to_draw['sphere']['center'][2],
            radius=data_to_draw['sphere']['radius']
        )

        # 'le' превращает кортежи в множества, поэтому требуется определенная магия для распаковки координат
        line_info = tuple(data_to_draw['line'])
        x1, y1, z1 = line_info[0]
        x2, y2, z2 = line_info[1]
        line = Line(x1=x1, y1=y1, z1=z1, x2=x2, y2=y2, z2=z2)

        print(f'Удалось спарсить данные сферы: {sphere.show_parameters()}')
        print(f'Удалось спарсить данные отрезка: {line.show_parameters()}')

        if collision_is_found(sphere=sphere, line=line):
            print('Коллизия обнаружена')
        else:
            pass
            # print('Коллизия не обнаружена')

    print('Спасибо за использование скрипта. На этом наши полномочия всё.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скрипт для поиска точек столкновения')
    parser.add_argument('file_path', type=str, help='Укажите путь к файлу с данными')
    args = parser.parse_args()

    main(args.file_path)
