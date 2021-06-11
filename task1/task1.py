import argparse
from typing import Union
from typing import List


class Number:
    """Класс-число для работы со системами исчисления (далее - СИ). Поддерживает следующие СИ - bin, oct, int, hex."""
    def __init__(self, value: int, base: str) -> None:
        self.value = value
        self.changed_value = None
        self.base = len(base)
        self.target_base = None

        self.change_number_system_to_decimal()

    def change_number_system_to_decimal(self) -> None:
        """Функция, вызываемая при инициализации экземпляра класса, для перевода числа в десятичную СИ."""
        self.value = int(str(self.value), base=self.base)

    def change_number_system(self, target_base: str) -> Union[bin, oct, int, hex]:
        """Функция для изменения СИ с десятичной на заданную."""
        self.target_base = len(target_base)

        if self.target_base == 2:
            self.changed_value = bin(self.value)
        elif self.target_base == 8:
            self.changed_value = oct(self.value)
        elif self.target_base == 10:
            self.changed_value = int(str(self.value), self.target_base)
        elif self.target_base == 16:
            self.changed_value = hex(self.value)

        return self.changed_value


def get_data_from_file(path: str) -> List[str]:
    """Функция для получения данных из файла. Принимает путь к файлу (от корневой папки проекта)."""
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    return data


def main(path: str) -> None:
    """Функция-агрегатор для запуска скрипта."""
    data = get_data_from_file(path)
    for element in data:
        digit, current_base, target_base = element.split()

        try:
            number = Number(int(digit), current_base)
        except ValueError:
            print('При изменении системы исчисления возникла ошибка.')
            continue

        changed_number = number.change_number_system(target_base)
        if changed_number is None:
            print('При изменении системы исчисления возникла ошибка.')
        else:
            print(f'Перевод числа "{digit}" из [{len(current_base)}] в [{len(target_base)}] систему исчисления завершен '
                  f'успешно. Результат = "{changed_number}".')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Изменение системы исчисления у числа')
    parser.add_argument('file_path', type=str, help='Укажите путь к файлу с данными')
    args = parser.parse_args()

    main(args.file_path)
