import pytest
from src.utils import read_file


def test_read_file():
    result = read_file('fake_file.json')
    assert result == []