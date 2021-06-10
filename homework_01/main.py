"""
Домашнее задание №1
Функции и структуры данных
"""


def is_prime(num):
    """
    The function returns True if num is prime, one returns False otherwise
    """
    if num < 2:
        return False
    dev = 2
    while dev <= num / 2:
        if num % dev == 0:
            return False
        dev += 1
    return True


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_num, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    dict_func = {'odd': lambda num: num % 2 != 0,
                 'even': lambda num: num % 2 == 0,
                 'prime': is_prime}
    return list(filter(dict_func[type], list_num))
