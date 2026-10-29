"""Задача: убрать из массива подряд идущие дубликаты.

[1, 1, 2, 2, 3] -> [1, 2, 3]
[0, 0, 1, 1, 0] -> [0, 1, 0]

Запуск тестов:
    pip install pytest
    pytest answer_compress_numbers.py -v
"""

import pytest


# --------------------------------------------------------------------------
# Решение
# --------------------------------------------------------------------------

def compress_numbers(numbers):
    """Возвращает новый список без подряд идущих дубликатов.

    Сравниваются только соседние элементы, поэтому одинаковые значения в
    разных местах массива сохраняются: [0, 0, 1, 1, 0] -> [0, 1, 0].

    Входной список не изменяется.
    Сложность: O(n) по времени, O(n) по памяти.
    """
    result = []
    for value in numbers:
        if not result or result[-1] != value:
            result.append(value)
    return result


# --------------------------------------------------------------------------
# Автотесты
# --------------------------------------------------------------------------

# Базовые случаи

def test_example_1():
    assert compress_numbers([1, 1, 2, 2, 3]) == [1, 2, 3]


def test_example_2():
    """Дубликаты схлопываются только подряд: 0 в конце остаётся."""
    assert compress_numbers([0, 0, 1, 1, 0]) == [0, 1, 0]


def test_empty_list():
    assert compress_numbers([]) == []


def test_single_element():
    assert compress_numbers([5]) == [5]


def test_no_duplicates():
    assert compress_numbers([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_all_elements_equal():
    assert compress_numbers([7, 7, 7, 7, 7]) == [7]


# Граничные случаи

def test_alternating_values():
    assert compress_numbers([1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1]


def test_duplicates_at_start():
    assert compress_numbers([4, 4, 4, 1, 2]) == [4, 1, 2]


def test_duplicates_at_end():
    assert compress_numbers([1, 2, 3, 3, 3]) == [1, 2, 3]


def test_negative_numbers():
    assert compress_numbers([-1, -1, -2, -3, -3]) == [-1, -2, -3]


def test_float_values():
    assert compress_numbers([1.5, 1.5, 2.5, 0.0, 0.0]) == [1.5, 2.5, 0.0]


def test_zero_and_negative_zero():
    """-0.0 == 0.0 в Python, поэтому это подряд идущие дубликаты."""
    assert compress_numbers([0.0, -0.0, 1.0]) == [0.0, 1.0]


def test_bool_is_treated_as_int():
    """True == 1 в Python: поведение задокументировано тестом."""
    assert compress_numbers([1, True, 2]) == [1, 2]


def test_large_list():
    """200 000 элементов: проверяем, что решение не деградирует по скорости."""
    data = [0] * 100_000 + [1] * 100_000
    assert compress_numbers(data) == [0, 1]
    assert len(data) == 200_000


# Контракт функции

def test_returns_new_list():
    data = [1, 1, 2]
    assert compress_numbers(data) is not data


def test_does_not_mutate_input():
    data = [1, 1, 2, 2, 3]
    compress_numbers(data)
    assert data == [1, 1, 2, 2, 3]


def test_works_with_tuple():
    """Достаточно итерируемого объекта, не обязательно list."""
    assert compress_numbers((3, 3, 4)) == [3, 4]


# Параметризованный набор

@pytest.mark.parametrize(
    "source, expected",
    [
        ([1, 1, 2, 2, 3], [1, 2, 3]),
        ([0, 0, 1, 1, 0], [0, 1, 0]),
        ([], []),
        ([9], [9]),
        ([1, 2, 1], [1, 2, 1]),
        ([5, 5, 5, 6, 6], [5, 6]),
        ([-3, -3, -3], [-3]),
    ],
    ids=[
        "task-example-1",
        "task-example-2",
        "empty",
        "single",
        "repeat-not-consecutive",
        "two-groups",
        "all-negative-equal",
    ],
)
def test_compress_numbers_parametrized(source, expected):
    assert compress_numbers(source) == expected
