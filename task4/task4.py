import argparse


MAGIC_SYMBOL = '*'


def compare_strings(string1: str, string2: str) -> None:
    """Фукнция для сравнения двух любых строк."""
    if string1 == string2:
        print('ОК')
    else:
        print('КО')


def main(word1: str, word2: str) -> None:
    """Функция-агрегатор для запуска скрипта. Константа 'волшебный символ' заменяет любые символы во второй строке."""
    if MAGIC_SYMBOL in word2:
        magic_symbol_index = word2.index(MAGIC_SYMBOL)
        compare_strings(word1[:magic_symbol_index], word2[:magic_symbol_index])
    else:
        compare_strings(word1, word2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Сравнение двух слов. Магический символ == "*".')
    parser.add_argument('word1', type=str, help='Введите первое слово для сравнения.')
    parser.add_argument('word2', type=str, help='Введите второе слово для сравнения.')
    args = parser.parse_args()

    main(args.word1, args.word2)
