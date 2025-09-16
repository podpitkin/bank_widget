import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number(num):
    assert get_mask_card_number("1234567890123456") == num


def test_get_card_number():
    assert get_mask_card_number("12345") == "Некорректный ввод"


@pytest.mark.parametrize("acc_num, expected", [
    ("12345678", "**5678"),
      ("123456", "**3456"),
])
def test_get_mask_account(acc_num, expected):
    assert get_mask_account(acc_num) == expected
