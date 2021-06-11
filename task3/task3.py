import argparse
import csv
from datetime import datetime


ADD_WATER = 'top'
TAKE_WATER = 'scoop'


class Barrel:
    """Класс-бочка для сохранения данных и работы с водой :)."""
    def __init__(self, max_capacity: int, current_capacity: int) -> None:
        self.max_capacity = max_capacity
        self.current_capacity = current_capacity
        self.start_capacity = current_capacity
        # Статистика добавления воды в бочку
        self.tries_to_add_water_count = 0
        self.successfully_tries_to_add_water = 0
        self.tries_to_add_water_mistakes_percent = 0
        self.water_capacity_is_added = 0
        self.water_capacity_is_wasted = 0
        # Статистика забора воды из бочки
        self.tries_to_take_water_count = 0
        self.successfully_tries_to_take_water = 0
        self.tries_to_take_water_mistakes_percent = 0
        self.water_capacity_is_taken = 0
        self.water_capacity_do_not_taken = 0

    def try_to_add_water(self, value: int) -> bool:
        """Функция для проверки можно ли добавить воды в бочку. Записывает данные о попытке."""
        self.tries_to_add_water_count += 1
        if self.current_capacity + value <= self.max_capacity:
            self.current_capacity += value
            self.successfully_tries_to_add_water += 1
            self.water_capacity_is_added += value
            return True
        self.water_capacity_is_wasted += value
        return False

    def try_to_take_water(self, value: int) -> bool:
        """Функция для проверки можно ли взять воды из бочки. Записывает данные о попытке."""
        self.tries_to_take_water_count += 1
        if self.current_capacity - value >= 0:
            self.current_capacity -= value
            self.successfully_tries_to_take_water += 1
            self.water_capacity_is_taken += value
            return True
        self.water_capacity_do_not_taken += value
        return False


class LogsAnalyzer:
    """Класс для работы с логом. Отвечает за создание бочек и сохранение/вывод информации."""
    def __init__(self, from_time: str, until_time: str) -> None:
        self.from_time = from_time
        self.until_time = until_time
        self.barrel = None

    def add_new_barrel(self, max_capacity: int, current_capacity: int) -> Barrel:
        """Функция для создания новой бочки с данными из лога за требуемый период."""
        self.barrel = Barrel(
            max_capacity=max_capacity,
            current_capacity=current_capacity
        )
        return self.barrel

    def calculate_statistics(self) -> None:
        """Функция для подсчета % ошибок при добавлении/заборе воды из бочки. Округляет % до сотых."""
        try:
            self.barrel.tries_to_add_water_mistakes_percent = \
                100 - ((self.barrel.successfully_tries_to_add_water * 100) / self.barrel.tries_to_add_water_count)
            self.barrel.tries_to_add_water_mistakes_percent = \
                round(self.barrel.tries_to_add_water_mistakes_percent, 3)
            self.barrel.tries_to_take_water_mistakes_percent = \
                100 - ((self.barrel.successfully_tries_to_take_water * 100) / self.barrel.tries_to_take_water_count)
            self.barrel.tries_to_take_water_mistakes_percent = \
                round(self.barrel.tries_to_take_water_mistakes_percent, 3)
        except ZeroDivisionError:
            pass

    def save_statistics_to_csv(self) -> None:
        """Функция для записи собранной статистики в csv-файл."""
        with open('task3/task3_results.csv', mode='w', encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter=':', lineterminator='\r')
            file_writer.writerow(['Период', f'{self.from_time} - {self.until_time}'])
            file_writer.writerow(['Количество попыток налить воды', f'{self.barrel.tries_to_add_water_count} раз.'])
            file_writer.writerow([
                'Процент ошибок при попытках налить воды',
                f'{self.barrel.tries_to_add_water_mistakes_percent}%.'
            ])
            file_writer.writerow(['Объем воды добавлен в бочку', f'{self.barrel.water_capacity_is_added} л.'])
            file_writer.writerow(['Объем воды потрачен впустую', f'{self.barrel.water_capacity_is_wasted} л.'])
            file_writer.writerow(['Количество попыток набрать воды', f'{self.barrel.tries_to_take_water_count} раз.'])
            file_writer.writerow([
                'Процент ошибок при попытках набрать воды',
                f'{self.barrel.tries_to_take_water_mistakes_percent}%.'
            ])
            file_writer.writerow(['Объем воды забран из бочки', f'{self.barrel.water_capacity_is_taken} л.'])
            file_writer.writerow([
                'Объем воды, который не сумели набрать из бочки',
                f'{self.barrel.water_capacity_do_not_taken} л.'
            ])
            file_writer.writerow(['В начале указанного периода в бочке было', f'{self.barrel.start_capacity} л.'])
            file_writer.writerow(['В конце указанного периода в бочке было', f'{self.barrel.current_capacity} л.'])

    def print_statistics_to_console(self) -> None:
        """Функция для вывода собранной статистики в консоль."""
        print(f'Количество попыток налить воды {self.barrel.tries_to_add_water_count} раз.')
        print(f'Процент ошибок при попытках налить воды {self.barrel.tries_to_add_water_mistakes_percent}%.')
        print(f'Объем воды добавлен в бочку {self.barrel.water_capacity_is_added} л.')
        print(f'Объем воды потрачен впустую {self.barrel.water_capacity_is_wasted} л.')
        print('*****')
        print(f'Количество попыток набрать воды {self.barrel.tries_to_take_water_count} раз.')
        print(f'Процент ошибок при попытках набрать воды {self.barrel.tries_to_take_water_mistakes_percent}%.')
        print(f'Объем воды забран из бочки {self.barrel.water_capacity_is_taken} л.')
        print(f'Объем воды, который не сумели набрать из бочки {self.barrel.water_capacity_do_not_taken} л.')
        print('*****')
        print(f'В начале указанного периода в бочке было {self.barrel.start_capacity} л.')
        print(f'В конце указанного периода в бочке было {self.barrel.current_capacity} л.')


def get_data_from_log(path_to_file: str) -> list:
    """Функция для получения данных из файла с логом."""
    try:
        with open(path_to_file, 'r', encoding='UTF-8') as file:
            data = file.readlines()
        return data
    except FileNotFoundError:
        raise SystemExit(f'Не удалось открыть файл {path_to_file}.')


def main(path: str, from_time: str, until_time: str):
    """Функция-агрегатор для запуска скрипта."""
    data = get_data_from_log(path)
    data_to_analyze = data[3:]

    analyzer = LogsAnalyzer(from_time, until_time)
    barrel = analyzer.add_new_barrel(int(data[1]), int(data[2]))

    for element in data_to_analyze:
        try:
            date, another_data = element.split(' – ')
            name, text = another_data.split(' - ')
        except ValueError:
            continue

        if analyzer.from_time <= date <= analyzer.until_time:
            text_list = text.split()
            action, value = text_list[1], text_list[-1]
            if action == ADD_WATER:
                barrel.try_to_add_water(int(value[:-1]))
            elif action == TAKE_WATER:
                barrel.try_to_take_water(int(value[:-1]))
            else:
                continue

    analyzer.calculate_statistics()
    analyzer.save_statistics_to_csv()
    analyzer.print_statistics_to_console()  # Не несет полезной функции, только для удобства разработчика.


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Получение лога за период времени')
    parser.add_argument('file_path', type=str, help='Укажите путь к файлу с логом')
    parser.add_argument('from_time', type=str, help='Укажите с какого периода времени следует отбирать данные')
    parser.add_argument('until_time', type=str, help='Укажите до какого периода времени следует отбирать данные')
    args = parser.parse_args()

    main(args.file_path, args.from_time, args.until_time)
