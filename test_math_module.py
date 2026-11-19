import pytest
from math_module import factorial, is_even


@pytest.mark.parametrize("number, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (6, 720),
])
def test_factorial_valid(number, expected):
    assert factorial(number) == expected


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)


def test_factorial_invalid_type():
    with pytest.raises(TypeError):
        factorial(3.5)


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (0, True),
    (-4, True),
    (3, False),
    (-7, False),
])
def test_is_even(number, expected):
    assert is_even(number) is expected