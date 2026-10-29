"""Задача: убрать из массива подряд идущие дубликаты.

Примеры:
    [1, 1, 2, 2, 3] -> [1, 2, 3]
    [0, 0, 1, 1, 0] -> [0, 1, 0]
"""


def compress_numbers(numbers):
    """Возвращает новый список без подряд идущих дубликатов.

    Сравниваются только соседние элементы, поэтому одинаковые значения
    в разных местах массива сохраняются: [0, 0, 1, 1, 0] -> [0, 1, 0].

    Входной список не изменяется.
    Сложность: O(n) по времени, O(n) по памяти.

    >>> compress_numbers([1, 1, 2, 2, 3])
    [1, 2, 3]
    >>> compress_numbers([0, 0, 1, 1, 0])
    [0, 1, 0]
    >>> compress_numbers([])
    []
    """
    result = []
    for value in numbers:
        if not result or result[-1] != value:
            result.append(value)
    return result


if __name__ == "__main__":
    print(compress_numbers([1, 1, 2, 2, 3]))
    print(compress_numbers([0, 0, 1, 1, 0]))
