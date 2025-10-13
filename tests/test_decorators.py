import pytest
from decorators import my_function

def test_my_function():
    my_function(2, 3)
    with open("my_log.txt", "r") as log_file:
        content = log_file.read()
    assert "my_function ok. Result: 5\n" in content


def test_decorator(capsys):
    def suum(x, y):
        return x + y

    suum(1,2)
    capture = capsys.readouterr()
    print(capture)


