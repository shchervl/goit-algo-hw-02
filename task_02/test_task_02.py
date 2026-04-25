import pytest

from task_02 import is_palindrome


@pytest.mark.parametrize("s", [
    "racecar",       # непарна кількість символів
    "abba",          # парна кількість символів
    "a",             # один символ
    "",              # порожній рядок
    "Madam",         # регістр
    "A man a plan a canal Panama",  # пробіли + регістр
    "Was it a car or a cat I saw",
])
def test_is_palindrome(s):
    assert is_palindrome(s) is True


@pytest.mark.parametrize("s", [
    "hello",
    "world",
    "python",
    "ab",
])
def test_is_not_palindrome(s):
    assert is_palindrome(s) is False


def test_case_insensitive():
    assert is_palindrome("RaceCar") is True


def test_ignores_spaces():
    assert is_palindrome("race car") is True


def test_odd_length():
    assert is_palindrome("level") is True


def test_even_length():
    assert is_palindrome("noon") is True
