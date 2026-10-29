"""Автотесты для compress_numbers.

Запуск:
    pip install pytest
    pytest -v
"""

import pytest

from compress_numbers import compress_numbers


# --- Базовые случаи ---------------------------------------------------------

def test_example_from_task_1():
    assert compress_numbers([1, 1, 2, 2, 3]) == [1, 2, 3]


def test_example_from_task_2():
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


def test_two_elements_equal():
    assert compress_numbers([2, 2]) == [2]


def test_two_elements_different():
    assert compress_numbers([2, 3]) == [2, 3]


# --- Граничные и содержательные случаи --------------------------------------

def test_alternating_values():
    assert compress_numbers([1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1]


def test_duplicates_at_the_end():
    assert compress_numbers([1, 2, 3, 3, 3]) == [1, 2, 3]


def test_duplicates_at_the_start():
    assert compress_numbers([4, 4, 4, 1, 2]) == [4, 1, 2]


def test_negative_numbers():
    assert compress_numbers([-1, -1, -2, -3, -3]) == [-1, -2, -3]


def test_float_values():
    assert compress_numbers([1.5, 1.5, 2.5, 0.0, 0.0]) == [1.5, 2.5, 0.0]


def test_zero_and_negative_zero():
    """-0.0 == 0.0 в Python, поэтому это подряд идущие дубликаты."""
    assert compress_numbers([0.0, -0.0, 1.0]) == [0.0, 1.0]


def test_bool_is_treated_as_int():
    """В Python True == 1, поведение задокументировано тестом."""
    assert compress_numbers([1, True, 2]) == [1, 2]


def test_large_list():
    """200 000 элементов: проверяем, что решение не деградирует по скорости."""
    data = [0] * 100_000 + [1] * 100_000
    result = compress_numbers(data)
    assert result == [0, 1]
    assert len(data) == 200_000  # входной список не тронут


def test_large_list_without_duplicates():
    data = [0, 1] * 50_000
    assert compress_numbers(data) == data


# --- Требования к контракту функции -----------------------------------------

def test_returns_new_list():
    data = [1, 1, 2]
    result = compress_numbers(data)
    assert result is not data


def test_does_not_mutate_input():
    data = [1, 1, 2, 2, 3]
    compress_numbers(data)
    assert data == [1, 1, 2, 2, 3]


def test_works_with_tuple():
    """Функция не требует именно list — достаточно итерируемого объекта."""
    assert compress_numbers((3, 3, 4)) == [3, 4]


# --- Параметризованный набор ------------------------------------------------

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
