import unittest

from task1.task1 import Number
from task1.task1 import get_data_from_file


class TestChangeNumberSystem(unittest.TestCase):
    """Тестирование класса Number."""
    correct_data_bin_to_dec = {
        'value': 111111,
        'current_base': '01',
        'target_base': '0123456789',
        'expected_answer': 63
    }
    incorrect_data_bin_to_dec = {
        'value': None,
        'current_base': '01',
        'target_base': '01',
        'expected_answer': None
    }

    def test_bin_to_dec_with_correct_data(self):
        number = Number(self.correct_data_bin_to_dec['value'], self.correct_data_bin_to_dec['current_base'])
        self.assertEqual(
            number.change_number_system(self.correct_data_bin_to_dec['target_base']),
            self.correct_data_bin_to_dec['expected_answer']
        )

    def test_raise_value_error_with_incorrect_data(self):
        with self.assertRaises(ValueError):
            Number(self.incorrect_data_bin_to_dec['value'], self.incorrect_data_bin_to_dec['current_base'])


class TestFunctionToGetData(unittest.TestCase):
    """Тестирование функции get_data_from_file."""
    def test_get_data_from_file(self):
        response = get_data_from_file('task1/data_for_task1.txt')
        expected_response = [
            '111111 01 0123456789\n',
            '155 0123456789 01\n',
            'None 01 01\n',
            '10 01 01234567\n',
            '122353623523 0123456789 0123456789abcd\n'
        ]
        self.assertEqual(expected_response, response)


if __name__ == '__main__':
    unittest.main()
