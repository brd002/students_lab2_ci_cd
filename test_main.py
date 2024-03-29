import pytest
from main import sum_func


def data_addition():
    return (2, 5, 7), (1, 1, 2), (3.1, 3.3, 6.4)


def data_typing():
    return (2, 5, int), ("1", "1", str), (3.1, 3.3, float)


@pytest.mark.parametrize("a, b, expected_val", data_addition())
def test_sum_func(a, b, expected_val):
    assert sum_func(a, b) == expected_val


@pytest.mark.parametrize("a, b, expected_type", data_typing())
def test_sum_func_typing(a, b, expected_type):
    assert type(a) is expected_type
    assert type(b) is expected_type
