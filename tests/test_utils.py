from string import ascii_lowercase

import pytest

from src.utils.defaults import default
from src.utils.strings import randstr


def test_randstr() -> None:
    string = randstr(ascii_lowercase, 10)
    assert isinstance(string, str)
    assert len(string) == 10
    assert all(i in ascii_lowercase for i in string)


def test_default() -> None:
    class LocalException(Exception):
        pass

    assert default(1, 2, LocalException) == 1
    assert default(None, 2, LocalException) == 2

    with pytest.raises(LocalException):
        default(None, None, LocalException)
